# Inicio del Laboratorio para el alumnado de AWS Academy

Comienzo dirigiéndome al enlace de [AWS Academy Cloud Foundations](https://awsacademy.instructure.com/courses/149697?invitation=Kb35BtXx0Gax6BbHTLf6mFZFQ7OyCio2V1CS5bD8) y tras logearme con mi usuario y contraseña de estudiante accedo al panel de control donde tengo activos los dos siguientes servicios:

1. [AWS Academy Cloud Foundations [149697]](https://awsacademy.instructure.com/courses/149697): Haz una breve descripción del curso.
2. [# AWS Academy Learner Lab [149699]](https://awsacademy.instructure.com/courses/149699): El *Laboratorio para el alumnado de AWS Academy* proporciona un entorno de pruebas de larga duración para la exploración ad hoc de los servicios de AWS

Una vez dentro del laboratorio para el alumnado de _AWS Academy_ me dirijo al apartado de 'Contenidos' y a la sección 'Laboratorio para el alumnado AWS _Academy_' donde puedo comenzar el laboratorio y acceder a los servicios de AWS.

# Objetivo del proyecto

<font color="#ffc000">El proyecto tiene como objetivo el desarrollo de un flujo de datos (data stream) escalable, diseñado para la ingesta y procesamiento de información proveniente de diversas fuentes de texto no estructurado, tales como Twitter, Mastodon, Reddit o Amazon entre otras.</font>
  
<font color="#ffc000">Adicional a la captura de datos, la arquitectura integra un motor de análisis de sentimiento basado en la API de HuggingFace y un sistema de visualización analítica orientado a la identificación de dinámicas conversacionales. Para este caso de uso y prototipo funcional, se utilizará la red social Mastodon como fuente de datos, centrando el análisis en la actividad y el sentimiento de los usuarios de todo el mundo.</font>
# Página de inicio y servicios usados de AWS

Una vez dentro puedo acceder a los distintos servicios de AWS, para mi proyecto de análisis de datos he utilizado las siguientes: EC2, Athena, S3, CloudWatch, Kinesis, Lambda y Secrets Manager.

El proyecto se desarrolla mediante un pipeline de procesamiento de datos distribuido en cuatro fases principales, en donde se usan servicios de AWS acorde a cada necesidad.
## EC2

He utilizado el servicio EC2 de AWS para crear una maquina virtual, o instancia, que se ejecuta en la nube de AWS. Los pasos han sido los siguientes:

1. En el panel de AWS selecciono el servicio EC2.
2. En el apartado 'Instancias' presiono sobre 'Lanzar una Instancia'
3. Le doy un nombre a mi 'Instancia', en este caso 'Mastodon-Producer'.
4. Como imagen de aplicaciones y sistemas operativos (Imagenes de máquina de Amazon (AMI)), selecciono 'Inicio rápido' y 'Amazon Linux'.
5. Como Tipo de instancia selecciono 't3.micro' que viene por defecto.
6. Posteriormente configuro un par de claves (inicio de sesión), y la nombro de manera acorde a la instancia como 'Key-MastodonProducer'.
7. En configuraciones de red dejo todo por defecto, y creo un grupo de seguridad donde permito el trafico de SSH desde mi IP.
8. Por último dejo el apartado de configurar almacenamiento con sus valores por defecto.
9. En detalles avanzados unicamente selecciono 'LabInstanceProfile' como perfil de instancia de IAM, el resto lo dejo con sus valores por defecto.

Ahora en el panel puedo ver mi instancia junto a sus propiedades como: Nombre, Id de la Instancia, Estado de la instancia (En ejecución), tipo de isntancia, comprobacion de estado (3/3 comprobaciones superadas), estado de alarma, zona de disponibilidad, dns de ipv4 publica, direccion ip, etc...

## S3

He generado un contenedor de datos almacenados en S3, o bucket mediante el servicio S3 de AWS. Los pasos han sido los siguientes:

1. En el panel de AWS selecciono el servicio S3.
2. En el apartado de 'bucket de uso general' presiono sobre 'crear bucket'.
3. Le doy nombre a mi 'bucket' en este caso 'bucketmastodonjubedaq'.
4. Dejo el resto de apartados (Propiedad de objetos, Configuración de bloqueo de acceso público para este bucket, Control de versiones de buckets, Etiquetas - *opcional*, Cifrado predeterminado, Configuración avanzada) con sus valores por defecto y clicko sobre 'Crear bucket'

Una vez creado el bucket, genero 3 carpetas que seran los directorios que alimentaré con los datos del streaming (rawdata/), los datos procesados tras pasar por la api de huggingface (processeddata/), y datos almacenados en la BBDD del servicio Athena de AWS (athena/). Los pasos son los siguientes:

1. Dentro del buquet que he creado, selecciono la opcion 'Crear carpeta'.
2. Le doy el nombre a la carpeta, respectivamente.
3. Dejo el resto de apartados (Cifrado del lado del servidor) por defecto.

## Kinesis

He generado una secuencia de datos con el objetivo de ingerir datos de transmisión, transformarlos y entregarlos a mi servicio S3 de forma fiable. Los pasos han sido los siguientes:

1. En el panel de AWS selecciono el servicio Kinesis.
2. En el apartado 'Secuencias de datos' presiono sobre 'Crear secuencia de datos'.
3. Le doy nombre a mi secuencia de datos en este caso 'mastodon-intake'.
4. En capacidad de secuencia de datos, indico la opcion 'aprovisionado' y dejo el resto de valores por defecto.
5. Dejo el resto de apartados (Tamaño maximo de registro, configuracón del flujo de datos, etiquetas: opcional) con sus valores por defecto.

## Lambda








# Segmentacion del uso de los servicios

El proyecto se desarrolla mediante un pipeline de procesamiento de datos distribuido en cuatro fases principales, en donde se usan servicios de AWS acorde a cada necesidad.

### 1. Captura de los datos

* Secrets Manager: Centraliza la gestión de credenciales. Se utiliza para almacenar de forma segura la URL de origen de Mastodon y las API Keys necesarias para la extracción y el posterior análisis de sentimientos (HuggingFace).  

* EC2: Capacidad de cómputo inicial mediante una instancia virtual en donde reside un script en Python que actúa como productor, realizando la llamada a la API de Mastodon e iniciando el streaming de datos en tiempo real.  

* Kinesis: Usado para el Data Stream. Es la "tubería" que transporta el flujo masivo de datos desde la instancia EC2 hacia las funciones de procesamiento en Lambda.

### 2. Procesado de datos

* Lambda: Ejecuta funciones sin servidor. Se encarga de transformar los datos crudos provenientes de Kinesis y estructurarlos antes de su almacenamiento en S3. Este proceso se realiza en _batches_ para optimizar las ejecuciones de lambda.  

* S3: Almacenamiento de datos. En esta fase, se utiliza un bucket con una subcarpeta específica para alojar los datos estructurados de mastodon listos para el análisis.

### 3. Motor de analisis de sentimientos

* Lambda: Una segunda función se activa ante eventos de escritura en S3, es decir cuando se recibe un _batch_ nuevo desde el streaming inicial. Esta función realiza una llamada a la API de HuggingFace que utiliza un modelo de _deep learning_ para procesar el texto y asignar una categoría de sentimiento a cada registro.  

* S3: Los resultados finales enriquecidos con las métricas del análisis de sentimientos se almacenan en otra subcarpeta, separándolos de los datos de origen _(raw)_.

### 4. Analitica y reportes

* Athena: Se almacenan los datos ya procesados en una tabla particionada por fecha. Mediante un evento de Event Bridge se añaden los datos no particionados (los que se generan en un nuevo dia) a la tabla. Una vez añadida la partición de fecha (a las 00:05), los registros se actualizan automaticamente. Esto permite ejecutar consultas directamente sobre los datos almacenados en S3 utilizando lenguaje estándar SQL. Los resultados de las consultas se almacenan en otra subcarpeta "_athena-results_" en S3.  

* EC2: En una segunda instancia dedicada, se ejecuta una aplicación de streamlit en Python para la visualización de datos. Esta consume la información procesada a través de PyAthena para generar reportes y dashboards. Mediante la creación de un grupo de seguridad, se permite el acceso desde red externa a través del puerto TCP 8501 de las IPs autorizadas.

## Esquema y flujo de datos

1. Usando una instancia de EC2 que es host de un scrypt de python, hacemos una llamada a la API de la red social Mastodon e iniciamos el stream de los datos.  

2. Usamos Kinesis como la tuberia por donde fluye el stream de data.  

3. A traves de una funcion lambda, procesamos los datos que estan siendo transmitidos en Kinesis y los almacenamos como data inicial (raw) en un bucket de S3.  

4. Con una segunda funcion en lambda, la cual se activa cada vez que ingresa un nuevo archivo 'raw' en S3. Hacemos uso del motor de analisis de sentimiento de la API de HuggingFace. Como resultado, obtenemos un sentimiento idenficado por cada registro. Los datos procesados que luego enviada a una carpeta del bucket de S3 (processed) utilizando la misma funcion lambda. 

5. A traves de Athena, generamos tablas y bases de datos que permitan analizar de forma estructurada los datos resultantes y procesados.  

6. En una segunda instancia de EC2. A traves de un scrypt de python, generamos una app con dashboards interactivos.
---

sudo dnf update -y
sudo dnf install -y python3-pip
pip3 install --user boto3 requests

aws kinesis describe-stream \
--stream-name twitter-streaming-intake \
 --region us-east-1
aws sts get-caller-identity

https://mastodon.social

sudo dnf update -y
sudo dnf install -y python3-pip
pip3 install --user streamlit pandas matplotlib boto3 pyathena

streamlit run nombre_del_archivo.py
