## Módulo 6: Informática o Cómputo

Este módulo proporciona una **introducción a los servicios de cómputo de AWS**, ofreciendo a los estudiantes una visión completa de las opciones de cómputo disponibles y cómo optimizarlas.

## Sección 1: Información general sobre los servicios de cómputo

Esta sección proporciona una **visión general de los servicios de cómputo de AWS**, ayudando a entender cómo seleccionar el servicio adecuado según las necesidades de la aplicación o el negocio.

### Servicios de cómputo de AWS

- AWS ofrece múltiples servicios de cómputo para **diferentes tipos de cargas de trabajo**, incluyendo:
    
    - **Instancias virtuales** (Amazon EC2)
    - **Funciones serverless** (AWS Lambda)
    - **Contenedores** (Amazon ECS, Amazon EKS, AWS Fargate)
    - Plataformas gestionadas (AWS Elastic Beanstalk, AWS Batch)

### Categorización de servicios de cómputo

- Los servicios se pueden agrupar según el **modelo de gestión** y **nivel de abstracción**:
    1. **Infraestructura como Servicio (IaaS)**: EC2, Elastic Block Store (EBS)
    2. **Plataforma como Servicio (PaaS)**: Elastic Beanstalk
    3. **Función como Servicio (FaaS / Serverless)**: AWS Lambda
    4. **Contenedores**: ECS, EKS, Fargate

### Elección del servicio de cómputo óptimo

- Factores a considerar al seleccionar un servicio:
    - **Tipo de carga de trabajo**: web, análisis de datos, procesamiento por lotes
    - **Escalabilidad requerida**: manual vs automática
    - **Tiempo de ejecución y gestión**: ¿desea gestionar servidores o dejar que AWS lo haga?
    - **Costo y eficiencia**: comparar precios según uso y necesidades

- El servicio óptimo depende del **equilibrio entre control, facilidad de uso y costo**.

---

## Sección 2: Amazon EC2 – Parte 1

Esta sección introduce los **conceptos fundamentales de Amazon Elastic Compute Cloud (EC2)** y guía sobre cómo lanzar y configurar instancias para distintos casos de uso.

---
### Amazon Elastic Compute Cloud (Amazon EC2)

- **EC2** es un servicio que permite **provisionar servidores virtuales escalables en la nube**.
- Proporciona **control total sobre la infraestructura**, incluyendo:
    - Elección de sistemas operativos
    - Configuración de red
    - Almacenamiento y seguridad

- Permite ejecutar **aplicaciones desde una sola instancia hasta arquitecturas distribuidas de alta disponibilidad**.

---

### Lanzamiento de una instancia de Amazon EC2

Para iniciar una instancia, se siguen **pasos clave**:

#### 1. Seleccionar una AMI (Amazon Machine Image)

- Una **AMI** contiene el sistema operativo, software preinstalado y configuraciones necesarias para ejecutar la instancia.
- AWS ofrece AMIs **prediseñadas**, y también se pueden crear **AMIs personalizadas**.

#### 2. Seleccionar un tipo de instancia

- Define la **capacidad de cómputo, memoria y almacenamiento** de la instancia.
- Consideraciones al elegir un tipo de instancia:
    - **Denominaciones y tamaños**: series como t3, m5, c6, etc., y tamaños desde micro hasta extra grande.
    - **Caso de uso**: optimizar según procesamiento, memoria, gráficos o cargas balanceadas.
    - **Características de red**: capacidad de ancho de banda y rendimiento de la red.

---

### Ejemplo: Creación de una nueva AMI

- Se puede crear una **AMI personalizada** a partir de una instancia existente:
    1. Configurar la instancia con el sistema operativo y software deseado.
    2. Guardar la instancia como una AMI.
    3. Lanzar nuevas instancias usando esta AMI personalizada.

---
## Sección 3: Optimización de costos de Amazon EC2 – Parte 2

Esta sección se centra en **cómo configurar instancias EC2 de manera eficiente para optimizar costos**, considerando los **cuatro pilares de la optimización de costos**: selección de recursos, ajuste de capacidad, gestión de licencias y uso eficiente del almacenamiento y la red.

---

### Configuración de la instancia EC2

Al lanzar una instancia, se deben considerar los siguientes elementos para optimizar costos:

1. **Especificar la configuración de red**
    - Selección de subred, IP pública o privada según necesidad.
    - Uso de tablas de enrutamiento y gateways para eficiencia de tráfico.

2. **Asociar un rol de IAM (opcional)**
    - Permite que la instancia acceda a recursos de AWS sin usar credenciales estáticas.

    - Ayuda a reducir riesgos de seguridad y costos de administración.

3. **Especificar un script de datos de usuario (opcional)**
    - Automatiza configuraciones al iniciar la instancia.
    - Reduce la necesidad de intervención manual y posibles errores que generen costos adicionales.

---

### Especificar el almacenamiento

- La elección correcta del almacenamiento impacta directamente en **costos y rendimiento**.
    
- **Opciones de almacenamiento de Amazon EC2:**
    - **Amazon EBS (Elastic Block Store)**: almacenamiento en bloques persistente.
    - **Instancias de almacenamiento efímero**: almacenamiento temporal local de la instancia.
    - **Amazon S3**: almacenamiento externo y económico para datos no transaccionales.

- **Ejemplos de selección de almacenamiento:**
    - Uso de EBS General Purpose (gp3) para aplicaciones de propósito general.
    - Almacenamiento efímero para cachés o datos temporales que no requieren persistencia.
    - Integración con S3 para archivos grandes o históricos.

---
## Sección 4: Servicios de contenedores – Amazon EC2 – Parte 3

Esta sección introduce **Docker**, explica las diferencias entre **máquinas virtuales y contenedores**, y presenta cómo **los servicios de contenedores de AWS** se integran con EC2 para ejecutar aplicaciones de manera flexible y escalable.

---

### Contenedores vs Máquinas Virtuales

- **Máquinas virtuales (VMs)**:
    - Ejecutan un sistema operativo completo sobre un hipervisor.
    - Mayor consumo de recursos (CPU, memoria, almacenamiento).
        
- **Contenedores**:
    - Comparten el mismo núcleo del sistema operativo.
    - Más ligeros, portables y rápidos de iniciar.
    - Ideales para microservicios y despliegue ágil.

---

### Configuración de instancias EC2 para contenedores

Al usar contenedores en EC2, considere los siguientes elementos:

1. **Agregar etiquetas**
    - Etiquetas de recursos para identificar, organizar y administrar instancias y contenedores.
        
2. **Configurar el grupo de seguridad**
    - Controla el tráfico entrante y saliente de las instancias que ejecutan contenedores.
    - Garantiza seguridad sin afectar la conectividad de la aplicación.
        
3. **Identificar o crear el par de claves**
    - Permite el acceso seguro por SSH a las instancias EC2 que ejecutan contenedores.
        
4. **Ciclo de vida de las instancias EC2**
    - Comprender fases: lanzamiento, configuración, ejecución, terminación.
    - Permite planificar escalado y mantenimiento de aplicaciones contenerizadas.

5. **Dirección IP elástica (opcional)**
    - Asigna IP fija a instancias críticas para acceso externo constante.

6. **Metadatos de la instancia EC2**
    - Información sobre la instancia para automatización y monitoreo de contenedores.

7. **Amazon CloudWatch para monitoreo**
    - Supervisión de métricas de CPU, memoria y red de instancias y contenedores.
    - Configuración de alarmas para eventos críticos o escalado automático.

---

**Servicios de contenedores de AWS**
- **Amazon Elastic Container Service (ECS)**: gestión de contenedores Docker escalables.
- **AWS Fargate**: ejecución de contenedores sin administrar servidores.
- **Amazon Elastic Kubernetes Service (EKS)**: despliegue de Kubernetes gestionado.
- **Amazon Elastic Container Registry (ECR)**: almacenamiento y gestión de imágenes de contenedores.

---

## Sección 5: Optimización de costos con Amazon EC2

Esta sección explica cómo **reducir y controlar los costos** asociados al uso de **Amazon EC2**, comprendiendo los **modelos de precios disponibles**, sus **casos de uso**, y aplicando buenas prácticas basadas en los **cuatro pilares de la optimización de costos**. El objetivo es **pagar solo por lo que realmente se necesita**, manteniendo rendimiento y disponibilidad.

## Modelos de precios de Amazon EC2

Amazon EC2 ofrece varios modelos de precios para adaptarse a diferentes patrones de uso:

### 1. Instancias bajo demanda (On-Demand Instances)

- Se pagan por segundo o por hora, sin compromisos a largo plazo.
- Flexibilidad total para iniciar y detener instancias cuando se necesite.
- Precio más alto en comparación con otros modelos.

**Cuándo usarlas**:

- Cargas de trabajo impredecibles.
- Pruebas, desarrollo y entornos temporales.
- Aplicaciones que no pueden interrumpirse.

### 2. Instancias reservadas (Reserved Instances – RI)

- Compromiso de uso por **1 o 3 años**.
- Descuentos significativos frente a On-Demand.
- Existen distintos tipos según flexibilidad y forma de pago.

**Tipos comunes**:

- **Standard RI**: mayor descuento, menor flexibilidad.
- **Convertible RI**: permite cambiar familia o tipo de instancia.
- **Savings Plans (alternativa moderna)**: compromiso de gasto por hora, más flexible.

**Cuándo usarlas**:

- Cargas de trabajo estables y predecibles.
- Aplicaciones en producción de larga duración.

### 3. Instancias Spot

- Utilizan capacidad sobrante de AWS.
- Pueden ofrecer descuentos de hasta un **90%**.
- AWS puede interrumpirlas con poco aviso.

**Cuándo usarlas**:

- Procesos batch.
- Big Data, machine learning, renderizado.
- Trabajos tolerantes a fallos o interrupciones.

### 4. Hosts dedicados y instancias dedicadas

- Recursos físicos exclusivos para un solo cliente.
- Coste más elevado.
- Útiles para requisitos normativos o licencias específicas.

## Beneficios de los modelos de precios de Amazon EC2

- **Flexibilidad**: elegir el modelo según la carga de trabajo.
- **Ahorro de costos**: descuentos significativos con reservas y Spot.
- **Escalabilidad económica**: pagar solo por lo que se usa.
- **Optimización progresiva**: combinar varios modelos en una misma arquitectura.

## Casos de uso de los modelos de precios de Amazon EC2

|Modelo|Caso de uso típico|
|---|---|
|On-Demand|Desarrollo, pruebas, cargas impredecibles|
|Reserved / Savings Plans|Producción estable y continua|
|Spot|Procesamiento masivo, trabajos tolerantes a fallos|
|Dedicated|Requisitos legales o licencias específicas|

## Los cuatro pilares de la optimización de costos

La optimización de costos en AWS se apoya en cuatro pilares fundamentales:

### Pilar 1: Adaptación del tamaño (Right Sizing)

Consiste en **ajustar el tipo y tamaño de instancia** a las necesidades reales:
- Evitar instancias sobredimensionadas.
- Analizar uso real de CPU, memoria y red.
- Cambiar familias de instancias si es necesario (por ejemplo, de general purpose a compute optimized).

**Herramientas útiles**:
- Amazon CloudWatch
- AWS Compute Optimizer

### Pilar 2: Aumento de la elasticidad

Busca **adaptar los recursos automáticamente a la demanda**:
- Escalar instancias solo cuando se necesiten.
- Detener recursos no utilizados.
- Automatizar apagado de entornos fuera de horario laboral.

**Ejemplos**:

- Auto Scaling Groups
- Programación de apagado/encendid
- Uso de Spot Instances para picos de carga

### Pilar 3: Modelo de precios óptimo

Seleccionar el **modelo de precios adecuado** para cada carga:

- Combinar On-Demand, Reserved y Spot.
- Migrar cargas estables a Savings Plans.
- Revisar periódicamente compromisos de reserva.

**Clave**: no usar un único modelo para todo.

### Pilar 4: Optimización de las opciones de almacenamiento

El almacenamiento también impacta directamente en el costo:

- Elegir el tipo de volumen EBS adecuado (gp3, io1, st1, sc1).
- Eliminar snapshots y volúmenes no utilizados.
- Usar S3 para datos que no requieren acceso frecuente.
- Aplicar políticas de ciclo de vida.

## Medición, monitoreo y mejora continua

La optimización de costos no es un proceso puntual, sino continuo:

### Medición

- Analizar gastos por servicio, cuenta o proyecto.
- Uso de etiquetas (tags) para asignación de costos.
### Monitoreo

- AWS Cost Explorer
- AWS Budgets
- CloudWatch

### Mejora continua

- Revisiones periódicas de arquitectura.
- Ajuste de instancias y modelos de precios.
- Automatización de buenas prácticas.

### Idea clave de la sección

> **Optimizar costos en EC2 no significa reducir rendimiento, sino usar los recursos adecuados en el momento adecuado y al precio adecuado.**

---
## Sección 6: Servicios de contenedores

Esta sección presenta los **fundamentos de los contenedores**, explica qué es **Docker** y en qué se diferencian los **contenedores de las máquinas virtuales**, y describe los principales **servicios de contenedores de AWS**, incluyendo **Amazon ECS** y **Kubernetes**. También se introducen otros servicios relacionados que complementan los entornos contenerizados en AWS.

## Conceptos básicos de contenedores

Un **contenedor** es una unidad estándar de software que empaqueta:

- El código de la aplicación
- Las dependencias necesarias
- Las librerías y configuraciones

Todo ello se ejecuta de forma **aislada** del sistema anfitrión, pero compartiendo el mismo **sistema operativo**.

### Características clave

- Portabilidad entre entornos (desarrollo, pruebas y producción).
- Arranque rápido.
- Uso eficiente de recursos.
- Ideal para arquitecturas de microservicios.

## ¿Qué es Docker?

**Docker** es la plataforma más popular para crear, distribuir y ejecutar contenedores.

### Componentes principales de Docker

- **Imagen Docker**  
    Plantilla inmutable que contiene la aplicación y sus dependencias.
    
- **Contenedor Docker**  
    Instancia en ejecución de una imagen.
    
- **Dockerfile**  
    Archivo que define cómo construir una imagen.
    
- **Docker Engine**  
    Motor que permite ejecutar contenedores.

### Beneficios de Docker

- Consistencia entre entornos.
- Facilidad de despliegue.
- Versionado de aplicaciones.
- Integración nativa con servicios de AWS.

## Contenedores frente a máquinas virtuales

### Máquinas virtuales (VMs)

- Ejecutan un sistema operativo completo.
- Mayor consumo de CPU, memoria y almacenamiento
- Arranque más lento.
- Aislamiento fuerte a nivel de hardware virtualizado.

### Contenedores

- Comparten el núcleo del sistema operativo.
- Mucho más ligeros.
- Arranque casi instantáneo.
- Ideal para escalado rápido y microservicios.

|Característica|Máquinas virtuales|Contenedores|
|---|---|---|
|Sistema operativo|Completo|Compartido|
|Consumo de recursos|Alto|Bajo|
|Tiempo de arranque|Lento|Rápido|
|Portabilidad|Media|Muy alta|

## Amazan Elastic Container Service (Amazon ECS)

**Amazon ECS** es un servicio totalmente gestionado para ejecutar y administrar contenedores Docker en AWS.

### Características principales

- No requiere instalar ni administrar software de orquestación.
- Integración nativa con servicios AWS (IAM, CloudWatch, ALB).
- Escalado automático de tareas y servicios.
- Compatible con imágenes almacenadas en **Amazon ECR**.


## Opciones de clúster de Amazon ECS

Amazon ECS ofrece dos formas principales de ejecutar contenedores:

### 1. ECS con instancias EC2

- El usuario administra las instancias EC2.
- Mayor control sobre el sistema operativo y recursos.
- Requiere gestión de parches y escalado de instancias.

**Casos de uso**:

- Necesidad de control detallado.
- Cargas de trabajo específicas o personalizadas.

### 2. ECS con AWS Fargate

- Modelo **serverless** para contenedores.
- No se administran servidores ni clústeres.
- Pago solo por CPU y memoria utilizados.

**Casos de uso**:

- Arquitecturas modernas.
- Reducción de carga operativa.
- Escalado automático sin gestión de infraestructura.

---

## ¿Qué es Kubernetes?

**Kubernetes** es una plataforma de código abierto para la **orquestación de contenedores**, ampliamente adoptada en entornos cloud e híbridos.

### Funciones principales

- Despliegue automatizado de contenedores.
- Escalado automático.
- Gestión de fallos.
- Balanceo de carga.

## Kubernetes en AWS: Amazon EKS

**Amazon Elastic Kubernetes Service (EKS)** es la versión gestionada de Kubernetes en AWS.

### Ventajas de Amazon EKS

- Control plane gestionado por AWS.
- Compatibilidad total con Kubernetes estándar.
- Integración con IAM, VPC y CloudWatch.
- Soporte para nodos EC2 y Fargate.

## Otros servicios relacionados con contenedores en AWS

### Amazon Elastic Container Registry (ECR)

- Registro privado para imágenes Docker.
- Alta seguridad y control de accesos.
- Integración directa con ECS y EKS.
### AWS App Runner

- Despliegue rápido de aplicaciones contenerizadas.
- Ideal para aplicaciones web y APIs.
- Menor complejidad operativa

### AWS Lambda y contenedores

- Lambda permite ejecutar código sin servidores.
- Soporta imágenes de contenedor como origen.
- Ideal para tareas event-driven y microservicios ligeros.

## Idea clave de la sección

> **Los contenedores permiten desarrollar, desplegar y escalar aplicaciones de forma rápida y consistente, y AWS ofrece múltiples servicios para gestionarlos según el nivel de control y simplicidad requerido.**

---

## Sección 7: Introducción a AWS Lambda

Esta sección introduce **AWS Lambda**, el servicio _serverless_ de AWS que permite **ejecutar código sin aprovisionar ni administrar servidores**. Se explican sus beneficios, cómo se integra con otros servicios de AWS mediante **eventos**, cómo se configura una función Lambda y cuáles son sus **límites principales**.

## AWS Lambda: ejecute código sin servidores

**AWS Lambda** permite ejecutar funciones de código en respuesta a eventos, sin necesidad de:

- Crear o administrar servidores.
- Configurar sistemas operativos.
- Gestionar escalado o alta disponibilidad.

El desarrollador solo se encarga del **código**, mientras que AWS gestiona automáticamente:

- La infraestructura.
- El escalado.
- La tolerancia a fallos.

### Lenguajes soportados (principales)

- Python
- Node.js
- Java
- C#
- Go
- Ruby
- Imágenes de contenedores

## Beneficios de AWS Lambda

### 1. Modelo completamente serverless

- No hay instancias EC2 ni clústeres que administrar.
- Ideal para arquitecturas modernas y event-driven.

### 2. Escalado automático

- Escala desde **cero hasta miles de ejecuciones simultáneas**.
- Ajuste automático según la carga.

### 3. Pago por uso

- Se paga únicamente por:
    - Número de ejecuciones.
    - Tiempo de ejecución (en milisegundos).

- No hay costos cuando no se ejecuta la función.

### 4. Alta disponibilidad integrada

- Ejecuta funciones en múltiples zonas de disponibilidad.
- No requiere configuración adicional.

### 5. Integración con servicios AWS

- Fácil integración con S3, DynamoDB, API Gateway, EventBridge, entre otros.


## Orígenes de eventos de AWS Lambda

Una función Lambda puede ejecutarse automáticamente cuando ocurre un evento en AWS.
### Orígenes de eventos comunes

#### Servicios de almacenamiento y datos
- **Amazon S3**: carga o eliminación de objetos.
- **Amazon DynamoDB**: cambios en tablas (Streams).
- **Amazon RDS** (mediante eventos).

#### Servicios de computación e integración

- **Amazon API Gateway**: invocación vía HTTP/REST.
- **AWS Application Load Balancer**.
- **Amazon EventBridge / CloudWatch Events**.

#### Servicios de mensajería

- **Amazon SQS**.
- **Amazon SNS**.
- **Amazon Kinesis**.

## Configuración de una función de AWS Lambda

Al crear una función Lambda se deben definir varios elementos clave:

### 1. Código de la función

- Puede subirse como archivo ZIP o imagen de contenedor.
- Incluye la lógica que se ejecutará ante un evento.
### 2. Runtime

- Define el lenguaje de programación.
- AWS proporciona entornos de ejecución gestionados.

### 3. Rol de ejecución (IAM Role)

- Permite a la función acceder a otros servicios AWS.
- Aplica el principio de **menor privilegio**.

### 4. Memoria y CPU

- La memoria se configura manualmente.
- La CPU se ajusta automáticamente según la memoria asignada.

### 5. Tiempo de espera (Timeout)

- Tiempo máximo de ejecución de la función.
- Debe ajustarse según la complejidad del proceso.

### 6. Variables de entorno

- Permiten configurar valores sin modificar el código.
- Útiles para entornos (dev, test, prod).

## Límites de AWS Lambda

AWS Lambda tiene límites que deben considerarse al diseñar la arquitectura:

### Límites principales

- **Duración máxima de ejecución**: 15 minutos.
- **Memoria**: hasta 10 GB.
- **Almacenamiento temporal (/tmp)**: limitado.
- **Concurrencia**: límite por región y cuenta.
- **Tamaño del paquete de despliegue**.

### Consideraciones de diseño

- No es ideal para procesos largos o persistentes.
- Para tareas complejas, puede combinarse con Step Functions.
- Es recomendable dividir procesos grandes en funciones pequeñas.


## Idea clave de la sección

> **AWS Lambda permite ejecutar código de forma escalable y rentable sin gestionar servidores, siendo ideal para arquitecturas event-driven y microservicios.**

---

## Sesión 8: Introducción a AWS Elastic Beanstalk

Esta sesión introduce **AWS Elastic Beanstalk**, un servicio de **plataforma como servicio (PaaS)** que permite **implementar, ejecutar y escalar aplicaciones web** sin necesidad de gestionar directamente la infraestructura subyacente. Elastic Beanstalk se encarga del aprovisionamiento, balanceo de carga, escalado automático y monitoreo.

## AWS Elastic Beanstalk

**AWS Elastic Beanstalk** es un servicio que permite desplegar aplicaciones desarrolladas en distintos lenguajes y frameworks, mientras AWS gestiona automáticamente:

- Instancias EC2
- Balanceadores de carga
- Auto Scaling
- Monitoreo y logging
- Actualizaciones del sistema operativo y la plataforma

El usuario se centra principalmente en el **código de la aplicación**, no en la infraestructura.

### Lenguajes y plataformas soportadas

- Java
- .NET
- Python
- Node.js
- PHP
- Ruby
- Go
- Docker

## Implementaciones de AWS Elastic Beanstalk

Elastic Beanstalk permite diferentes **tipos de entornos**, según el tipo de aplicación y la carga de trabajo.

### 1. Entorno web

- Diseñado para aplicaciones web y APIs.
- Incluye automáticamente:
    - Balanceador de carga
    - Instancias EC2
    - Auto Scaling Group

- Recibe tráfico HTTP/HTTPS desde Internet.

**Casos de uso**:

- Aplicaciones web tradicionales.
- Servicios REST.
- Backends de aplicaciones móviles.

### 2. Entorno de trabajo (Worker Environment)

- Procesa tareas en segundo plano.
- Utiliza **Amazon SQS** para recibir trabajos.
- Ideal para procesos asíncronos.

**Casos de uso**:

- Procesamiento de colas.
- Envío de correos.
- Procesos batch o diferidos.

### 3. Implementación con Docker

- Permite desplegar aplicaciones contenerizadas.
- Compatible con Dockerfile o docker-compose.
- Puede ejecutarse sobre instancias EC2.

**Ventaja**:

- Mayor control sobre el entorno de ejecución.
- Consistencia entre desarrollo y producción.

### 4. Entornos de una sola instancia

- Ejecuta la aplicación en una única instancia EC2.
- Menor costo.
- No ofrece alta disponibilidad.

**Casos de uso**:

- Desarrollo y pruebas.
- Aplicaciones internas.

## Beneficios de AWS Elastic Beanstalk

### 1. Simplicidad de uso

- Despliegue rápido de aplicaciones.
- Configuración mínima inicial.
- Ideal para equipos que quieren enfocarse en el desarrollo.

### 2. Escalado automático integrado

- Ajusta el número de instancias según la demanda.
- Soporte para escalado horizontal.

### 3. Gestión automática de infraestructura

- AWS gestiona parches, actualizaciones y configuración base.
- Menor carga operativa.

### 4. Integración con servicios AWS

- CloudWatch para métricas y logs.
- IAM para control de accesos.
- RDS, S3, DynamoDB fácilmente integrables.

### 5. Control y personalización

- Acceso a recursos subyacentes si es necesario.
- Posibilidad de ajustar configuraciones avanzadas.
- Uso de archivos `.ebextensions` para personalización.

### 6. Coste eficiente

- No tiene coste adicional por el servicio.
- Solo se paga por los recursos utilizados (EC2, ELB, almacenamiento).

## Elastic Beanstalk vs otros servicios

|Servicio|Nivel de gestión|Caso de uso|
|---|---|---|
|EC2|Infraestructura|Control total|
|Elastic Beanstalk|Plataforma|Aplicaciones web gestionadas|
|Lambda|Serverless|Ejecución por eventos|
|ECS/EKS|Contenedores|Microservicios|

## Idea clave de la sesión

> **Elastic Beanstalk permite desplegar y escalar aplicaciones web de forma sencilla, combinando automatización con la posibilidad de personalización cuando se necesita.**

---

## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Proporcionar información general sobre los diferentes servicios informáticos de AWS en la nube.
- Demostrar por que se debe utilizar Amazon Elastic Compute Cloud ( Amazon EC2).
- Identificar la funcionalidad en la consola de Amazon EC2
- Realizar funciones básicas en Amazon EC2 para crear un entorno informático virtual.
- Identificar los elementos de optimización de costos con Amazon EC2
- Demostrar cuando se utiliza AWS Elastic Beanstalk
- Demostrar cuando se utiliza AWS Lambda
- Identificar como ejecutar aplicaciones en contenedores en un clúster de servidores administrados.
### Pregunta del examen de muestra

¿Qué servicio de AWS permite que los desarrolladores implementes rápidamente recursos que pueden utilizar diferentes lenguajes de programación como.NET y Java.?
- AWS Elastic Beanstalk.