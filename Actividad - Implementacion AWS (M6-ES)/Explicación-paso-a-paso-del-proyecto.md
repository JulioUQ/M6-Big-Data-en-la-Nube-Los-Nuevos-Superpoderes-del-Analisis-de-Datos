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

Para conectarme con la EC2 sigo los siguientes pasos:
1. En el panel de AWS en el servicio EC2 clicko sobre Conectar.
2. Copio el ejemplo de ssh que se indica al final de la pagina. (ssh -i "KeyPair-Mastodon-producer.pem" ec2-user@ec2-13-220-109-136.compute-1.amazonaws.com)
3. En la carpeta donde se encuentra el par de claves del EC2 abro una terminal e indico este chunk de codigo para entrar en la EC2.
4. Instalo python y sus dependencias:
	- sudo dnf update -y
	- sudo dnf install -y python3-pip
	- pip3 install --user boto3 requests

## Secrets Manager

He utilizado el servicio Secrets Manager de AWS para almacenar secretos, que se ejecuta en la nube de AWS. Los pasos han sido los siguientes:

1. En el panel de AWS selecciono el servicio Secrets Manager.
2. En el apartado 'Secretos' presiono sobre 'Almacenar un secreto nuevo'.
3. Como tipo de secreto selecciono 'Otro tipo de secreto (Clave API, token OAuth, otros.)'.
4. Doy nombre al par clave-valor, añadiendo el token de Mastodon o de HuggingFace, para cada secreto respectivamente (Secreto MastodonProducer y secreto AWS-model_uoc).
5. Nombro el secreto de manera que me ayude a encontrar el secreto mas adelante.
6. El resto de apartados y secciones permanecen por defecto.

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

He generado una funcion lambda con el objetivo de procesar datos de la transmisión, transformarlos y entregarlos a mi servicio S3 de forma fiable. Los pasos han sido los siguientes:

1. En el panel de AWS selecciono el servicio lamda.
2. En el apartado 'Funciones' presiono sobre 'Crear funcion'.
3. 






---


aws kinesis describe-stream \
--stream-name twitter-streaming-intake \
 --region us-east-1
aws sts get-caller-identity

https://mastodon.social

sudo dnf update -y
sudo dnf install -y python3-pip
pip3 install --user streamlit pandas matplotlib boto3 pyathena

streamlit run nombre_del_archivo.py
8081
8051