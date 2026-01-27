## Módulo 7: Almacenamiento

Este módulo presenta las diversas opciones de almacenamiento de datos que AWS ofrece, basadas en **cuatro tecnologías principales**, permitiendo a los estudiantes elegir el servicio adecuado según diferentes casos de uso.

## Sección 1: Amazon Elastic Block Store (Amazon EBS)

Esta sección proporciona una visión general de **Amazon Elastic Block Store (EBS)**, el servicio de **almacenamiento en bloques** de AWS diseñado para usarse con instancias **Amazon EC2**. Se explican sus conceptos fundamentales, tipos de volúmenes, características principales, rendimiento (IOPS), precios, así como el uso de **instantáneas** y la transferencia de datos.

## Conceptos de almacenamiento: bloques vs objetos

Antes de profundizar en Amazon EBS, es importante entender los tipos de almacenamiento más comunes en AWS.

### Almacenamiento en bloques

- Los datos se dividen en bloques de tamaño fijo.
- Se comporta como un disco duro tradicional.
- Ideal para sistemas operativos, bases de datos y aplicaciones que requieren acceso rápido y consistente.

**Ejemplo en AWS**:

- Amazon EBS

### Almacenamiento en objetos

- Los datos se almacenan como objetos con metadatos.
- No se monta como un sistema de archivos tradicional.
- Altamente escalable y duradero.

**Ejemplo en AWS**:

- Amazon S3

|Característica|Bloques (EBS)|Objetos (S3)|
|---|---|---|
|Acceso|Bajo nivel|API|
|Uso típico|SO, BBDD|Backups, archivos|
|Montaje|Sí|No|
|Latencia|Muy baja|Mayor|

## Interacción con Amazon EBS desde la Consola de AWS

Amazon EBS se gestiona principalmente a través de **Amazon EC2**, ya que los volúmenes se **asocian a instancias**.

Desde la consola se pueden:

- Crear volúmenes EBS.
- Adjuntar y desadjuntar volúmenes a instancias EC2.
- Cambiar tipo, tamaño y rendimiento del volumen.
- Crear y administrar instantáneas.
- Eliminar volúmenes no utilizados.

## Tipos de volúmenes de Amazon EBS

Amazon EBS ofrece distintos tipos de volúmenes según el rendimiento y el coste.

### 1. Volúmenes SSD

#### General Purpose SSD (gp3 / gp2)

- Uso general.
- Buen equilibrio entre costo y rendimiento.
- Adecuado para la mayoría de cargas de trabajo.

**Casos de uso**:

- Sistemas operativos.
- Aplicaciones comunes.
- Bases de datos pequeñas y medianas.

#### Provisioned IOPS SSD (io1 / io2)

- Alto rendimiento y baja latencia.
- IOPS configurables.
- Diseñado para aplicaciones críticas.

**Casos de uso**:

- Bases de datos empresariales.
- Sistemas de alta transaccionalidad.

### 2. Volúmenes HDD

#### Throughput Optimized HDD (st1)

- Optimizado para grandes volúmenes de datos secuenciales.
- Menor costo.

**Casos de uso**:

- Big Data.
- Data warehouses.

#### Cold HDD (sc1)

- Almacenamiento de bajo costo.
- Acceso poco frecuente.

**Casos de uso**:

- Datos históricos.
- Archivos de respaldo.

## Características de Amazon EBS

### Alta disponibilidad

- Replicación automática dentro de la misma zona de disponibilidad
- Protección frente a fallos de hardware.

### Persistencia

- Los datos persisten aunque la instancia EC2 se detenga.
- No se pierden al reiniciar la instancia.

### Escalabilidad

- Se puede aumentar tamaño y rendimiento sin detener la instancia (en la mayoría de casos).

### Seguridad

- Cifrado en reposo y en tránsito.
- Integración con AWS KMS.
- Control de acceso mediante IAM.

## Amazon EBS: volúmenes, IOPS y precios

### Rendimiento (IOPS)

- Depende del tipo de volumen.
- Los volúmenes io1/io2 permiten aprovisionar IOPS específicos.
- gp3 permite desacoplar capacidad e IOPS.
### Precios

- Se paga por:
    - Tamaño del volumen (GB/mes).
    - IOPS aprovisionados (en algunos tipos).
    - Almacenamiento de instantáneas.

- No hay costo por operaciones de lectura/escritura.

## Amazon EBS: instantáneas y transferencia de datos

### Instantáneas (Snapshots)

- Copias de seguridad incrementales almacenadas en Amazon S3.
- Permiten:
    - Recuperación ante fallos.
    - Creación de nuevos volúmenes.
    - Migración entre zonas de disponibilidad o regiones.

### Transferencia de datos

- Dentro de la misma zona de disponibilidad: baja latencia.
- Entre zonas o regiones: puede generar costos adicionales.
- Las instantáneas facilitan la replicación de datos entre regiones

## Idea clave de la sección

> **Amazon EBS proporciona almacenamiento en bloques persistente, seguro y de alto rendimiento para instancias EC2, siendo esencial para sistemas operativos y aplicaciones críticas.**

---

## Sección 2: Amazon Simple Storage Service (Amazon S3)

Esta sección describe **Amazon Simple Storage Service (Amazon S3)**, el servicio de **almacenamiento de objetos** de AWS, sus principales casos de uso, cómo **escala automáticamente**, el concepto de **redundancia de datos dentro de una región** y una introducción a su **modelo de precios**.

## Almacenamiento

Amazon S3 proporciona **almacenamiento de objetos**, donde los datos se guardan como **objetos** dentro de **buckets**.

Cada objeto está compuesto por:

- Datos
- Metadatos
- Un identificador único (clave del objeto)

Este modelo es ideal para almacenar grandes volúmenes de información no estructurada.

## Información general sobre Amazon S3

**Amazon S3** es un servicio:

- Altamente **escalable**
- **Duradero** (diseñado para 11 nueves de durabilidad)
- **Disponible** a nivel global
- Totalmente gestionado por AWS

### Casos de uso comunes

- Copias de seguridad y recuperación ante desastres.
- Almacenamiento de archivos estáticos.
- Data lakes y análisis de datos.
- Distribución de contenido.
- Almacenamiento de logs y archivos multimedia.

## Clases de almacenamiento de Amazon S3

Amazon S3 ofrece varias **clases de almacenamiento**, adaptadas a diferentes patrones de acceso y costos.
### Clases más utilizadas

- **S3 Standard**
    - Acceso frecuente.
    - Alta disponibilidad y durabilidad.

- **S3 Intelligent-Tiering**
    - Optimiza costos automáticamente según el uso.
    - Mueve objetos entre capas de acceso.

- **S3 Standard-IA (Infrequent Access)**
    - Acceso poco frecuente.
    - Menor costo de almacenamiento, con cargo por acceso.

- **S3 One Zone-IA**
    - Almacena datos en una sola zona de disponibilidad.
    - Menor costo, menor redundancia.

- **S3 Glacier / Glacier Deep Archive**
    - Archivado a largo plazo.
    - Coste muy bajo, acceso lento.

## Direcciones URL de buckets de Amazon S3

Los objetos almacenados en S3 pueden accederse mediante **URLs**, que siguen dos estilos principales:

### 1. Estilo virtual-hosted

- El nombre del bucket forma parte del dominio.
- Es el estilo recomendado y más moderno.

**Ejemplo conceptual**:  
`bucket.s3.region.amazonaws.com/objeto`

### 2. Estilo path-style

- El nombre del bucket forma parte de la ruta.
- Uso limitado y en desuso para nuevas implementaciones.

**Ejemplo conceptual**:  
`s3.region.amazonaws.com/bucket/objeto`

## Almacenamiento de los datos con redundancia en una región

Amazon S3 **replica automáticamente los datos** dentro de una región:
- Los objetos se almacenan en **múltiples zonas de disponibilidad**.
- Protección frente a fallos de hardware, red o centros de datos.
- No requiere configuración adicional por parte del usuario.

Esto garantiza una **alta durabilidad y disponibilidad** de los datos.

## Diseño para ofrecer un escalado sin interrupciones

Amazon S3 está diseñado para **escalar de forma automática**:

- No hay límites prácticos de almacenamiento.
- No se requiere aprovisionar capacidad.
- Maneja miles de solicitudes por segundo sin intervención del usuario.

### Ventajas del escalado automático

- Ideal para cargas impredecibles.
- Permite crecimiento progresivo sin rediseño.
- Soporte para aplicaciones globales.

## Acceso a los datos desde cualquier lugar

Amazon S3 permite acceder a los datos:

- Desde la consola de AWS.
- Mediante APIs REST.
- Con SDKs de AWS.
- A través de URLs públicas o privadas.

### Control de acceso

- Políticas de bucket.
- Políticas IAM.
- Listas de control de acceso (ACLs).
- Integración con CloudFront para distribución global.

## Precios de almacenamiento en Amazon S3

El modelo de precios de Amazon S3 se basa en el **pago por uso**:
### Se cobra por:

- Cantidad de datos almacenados (GB/mes)
- Clase de almacenamiento utilizada.
- Solicitudes realizadas (PUT, GET, LIST).
- Transferencia de datos salientes.
### Optimización de costos

- Uso de clases IA y Glacier.
- Políticas de ciclo de vida.
- S3 Intelligent-Tiering.

## Idea clave de la sección

> **Amazon S3 ofrece almacenamiento de objetos altamente duradero, escalable y accesible globalmente, con un modelo de precios flexible adaptado al uso real.**

---
## Sección 3: Amazon Elastic File System (Amazon EFS)

Esta sección presenta **Amazon Elastic File System (EFS)**, el servicio de **almacenamiento de archivos** totalmente gestionado de AWS. Se describen sus **casos de uso**, **características**, **arquitectura**, cómo se **implementa** y los principales **recursos disponibles** para su gestión.

## Almacenamiento

Amazon EFS proporciona **almacenamiento de archivos** basado en el protocolo **NFS (Network File System)**.

- Se comporta como un sistema de archivos tradicional.
- Puede montarse simultáneamente en **múltiples instancias EC2**.
- Ideal para aplicaciones que requieren acceso compartido a archivos.

## Características de Amazon EFS

### Escalado automático

- Crece y se reduce automáticamente según la cantidad de datos.
- No requiere aprovisionamiento de capacidad.

### Alta disponibilidad y durabilidad

- Los datos se replican automáticamente dentro de una región.
- Diseñado para soportar fallos de infraestructura.

### Acceso concurrente

- Múltiples instancias EC2 pueden acceder al mismo sistema de archivos al mismo tiempo.
- Ideal para entornos distribuidos.

### Rendimiento elástico

- Ajusta el rendimiento en función del tamaño del sistema de archivos.
- Soporta cargas de trabajo variables

### Seguridad

- Cifrado de datos en reposo y en tránsito.
- Control de acceso mediante IAM y políticas de seguridad de red.

## Arquitectura de Amazon EFS

La arquitectura de Amazon EFS está diseñada para ser **regional y altamente disponible**.

### Componentes clave

- **Sistema de archivos EFS**: recurso principal.
- **Mount targets**: puntos de montaje en subredes de una VPC.
- **Grupos de seguridad**: controlan el acceso NFS.
- **Zonas de disponibilidad**: redundancia automática.

Cada zona de disponibilidad tiene su propio **mount target**, lo que permite:

- Acceso local de baja latencia.
- Alta disponibilidad ante fallos zonales.

## Implementación de Amazon EFS

### Pasos generales de implementación

1. Crear un sistema de archivos EFS.
2. Asociarlo a una VPC.
3. Crear mount targets en las subredes necesarias.
4. Configurar grupos de seguridad.
5. Montar el sistema de archivos en instancias EC2 mediante NFS.

### Casos de uso comunes

- Sistemas de archivos compartidos.
- Aplicaciones web escaladas horizontalmente.
- Procesamiento de datos y análisis.
- Entornos de desarrollo colaborativos.
- Sistemas de gestión de contenido (CMS).

## Recursos de Amazon EFS

Amazon EFS proporciona múltiples recursos y herramientas para su gestión:
### Consola de administración de AWS

- Creación y monitoreo de sistemas de archivos.
- Visualización de métricas y uso.
### Integración con otros servicios AWS

- Amazon EC2.
- AWS Lambda (con EFS).
- Amazon ECS y EKS.
- AWS Backup.

### Monitoreo y métricas

- Integración con Amazon CloudWatch.
- Métricas de rendimiento, capacidad y latencia.

## Comparación rápida con otros servicios de almacenamiento

|Servicio|Tipo|Uso principal|
|---|---|---|
|EBS|Bloques|SO y bases de datos|
|S3|Objetos|Almacenamiento masivo|
|EFS|Archivos|Acceso compartido|

## Idea clave de la sección

> **Amazon EFS proporciona un sistema de archivos compartido, altamente disponible y escalable, ideal para aplicaciones distribuidas que requieren acceso concurrente a los mismos datos.**

---
## Sección 4: Amazon S3 Glacier

Esta sección explica las funcionalidades de **Amazon S3 Glacier**, el servicio de **almacenamiento de archivado y largo plazo** de AWS. Se describen sus **casos de uso**, cómo funciona el **ciclo de vida de migración de datos desde Amazon S3**, las **clases de almacenamiento**, así como los aspectos de **seguridad y cifrado**.

## Almacenamiento

Amazon S3 Glacier forma parte de la familia **Amazon S3** y está diseñado para:

- Almacenamiento de datos a largo plazo.
- Acceso poco frecuente.
- Coste muy bajo frente a almacenamiento estándar.

No está pensado para acceso inmediato, sino para **recuperaciones planificadas**.

## Revisión de Amazon S3 Glacier

Amazon S3 Glacier:

- Es altamente duradero.
- Está optimizado para archivado.
- Permite definir tiempos de recuperación flexibles.
- Se gestiona directamente desde Amazon S3.

Actualmente, Amazon S3 Glacier se utiliza principalmente a través de sus **clases de almacenamiento**, no como un servicio independiente.

## Amazon S3 Glacier

Amazon S3 Glacier ofrece distintas opciones según la frecuencia y urgencia de acceso:

### Clases principales

- **S3 Glacier Instant Retrieval**
- **S3 Glacier Flexible Retrieval**
- **S3 Glacier Deep Archive**

Cada una equilibra **coste, tiempo de recuperación y disponibilidad**.

## Casos de uso de Amazon S3 Glacier

Amazon S3 Glacier es ideal para:

- Copias de seguridad a largo plazo.
- Datos históricos.
- Archivos legales y regulatorios.
- Datos que deben conservarse durante años.
- Recuperación ante desastres.

## Uso de Amazon S3 Glacier

El uso de S3 Glacier suele darse mediante:

- Carga directa de objetos en clases Glacier.
- Migración automática desde S3 Standard o IA
- Recuperación bajo demanda cuando se necesita el dato.

### Tipos de recuperación

- **Instantánea** (Instant Retrieval).
- **Estándar**.
- **Bulk** (más lenta y económica).

## Políticas de ciclo de vida

Las **políticas de ciclo de vida de S3** permiten automatizar la migración de datos:

- Definir reglas basadas en la antigüedad del objeto.
- Mover objetos entre clases de almacenamiento.
- Eliminar datos tras un periodo definido.

**Ejemplo típico**:

- S3 Standard → S3 IA → S3 Glacier → S3 Glacier Deep Archive

## Clases de almacenamiento de Amazon S3

Resumen de las clases relacionadas con archivado:

- **S3 Standard / IA**: acceso frecuente o esporádico.
- **S3 Glacier Instant Retrieval**: archivado con acceso inmediato.
- **S3 Glacier Flexible Retrieval**: archivado con recuperación en minutos u horas.
- **S3 Glacier Deep Archive**: archivado a muy largo plazo, recuperación en horas.

## Comparación del almacenamiento S3 vs S3 Glacier

|Característica|Amazon S3|Amazon S3 Glacier|
|---|---|---|
|Acceso|Inmediato|Retardado|
|Coste|Más alto|Muy bajo|
|Uso|Datos activos|Archivado|
|Recuperación|Instantánea|Planificada|

## Cifrado del lado del servidor

Amazon S3 Glacier soporta **cifrado automático del lado del servidor**:

- SSE-S3: claves gestionadas por AWS.
- SSE-KMS: integración con AWS KMS.
- Datos cifrados en reposo sin configuración compleja.

## Seguridad con Amazon S3 Glacier

### Controles de seguridad

- Políticas IAM.
- Políticas de bucket.
- Control de acceso basado en roles.
- Auditoría mediante AWS CloudTrail.

### Cumplimiento y protección

- Integración con políticas de retención.
- Protección frente a eliminación accidental.
- Cumplimiento normativo y legal.

## Idea clave de la sección

> **Amazon S3 Glacier ofrece almacenamiento seguro, duradero y de muy bajo coste para datos que deben conservarse a largo plazo y a los que se accede de forma ocasional.**

---
## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Identificar los diferentes tipos de almacenamiento 
- Describir Amazon S3
- Identificar la funcionalidad en Amazon S3
- Describir Amazon EBS
- Identificar la funcionalidad en Amazon EBS
- Ejecutar funciones en Amazon EBS para crear una solución de almacenamiento de Amazon EC2
- Describir Amazon EFS
- Identificar la funcionalidad en Amazon EFS
- Describir Amazon S3 Glacier
- Identificar la funcionalidad en Amazon S3 Glacier
- Diferenciar entre Amazon EBS, Amazon S3 y Amazon S3 Glacier.
### Pregunta del examen de muestra

Una empresa desea almacenar los datos a los que accede con poca frecuencia ¿Cuál es la mejor solución y la más rentable que debe considerar?
- Amazon S3 Glacier.