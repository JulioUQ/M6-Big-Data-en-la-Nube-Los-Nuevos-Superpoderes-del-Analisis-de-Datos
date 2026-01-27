## Módulo 8: Bases de datos

Este módulo presenta cuatro de los **servicios de bases de datos más utilizados de AWS**, con énfasis en la selección del servicio adecuado según los casos de uso.

## Sección 1: Amazon Relational Database Service (Amazon RDS)

Esta sección proporciona una visión general de **Amazon Relational Database Service (RDS)**, explicando la diferencia entre **bases de datos no administradas y administradas**, los desafíos de las bases de datos relacionales tradicionales y cómo **Amazon RDS simplifica su gestión**, incluyendo **alta disponibilidad mediante Multi-AZ** y **réplicas de lectura**.

## Comparación entre servicios no administrados y administrados

### Bases de datos no administradas

- El usuario gestiona:
    - Sistema operativo.
    - Motor de base de datos.
    - Parches y actualizaciones.
    - Copias de seguridad.
    - Alta disponibilidad y recuperación.

**Ejemplo:**
- Base de datos instalada manualmente en EC2.

### Bases de datos administradas

- AWS se encarga de:
    - Instalación del motor.
    - Aplicación de parches.
    - Backups automáticos.
    - Monitoreo y recuperación.

- El usuario se centra en:
    - Datos.
    - Consultas.
    - Diseño del esquema.

**Ejemplo**:
- Amazon RDS.

## Desafíos de las bases de datos relacionales

Las bases de datos relacionales tradicionales presentan varios retos:

- Alta complejidad operativa.
- Gestión manual de copias de seguridad.
- Escalado limitado.
- Alta disponibilidad difícil de implementar    
- Recuperación ante fallos costosa y compleja.

Amazon RDS reduce significativamente estos desafíos.

## Amazon RDS

**Amazon RDS** es un servicio totalmente administrado para bases de datos relacionales.

### Motores soportados

- Amazon Aurora
- MySQL
- PostgreSQL
- MariaDB
- Oracle
- SQL Server

## Responsabilidades con los servicios administrados

### AWS se encarga de:

- Infraestructura.
- Sistema operativo.
- Motor de base de datos.
- Backups automáticos.
- Alta disponibilidad.

### El cliente se encarga de:

- Diseño del esquema.
- Gestión de datos.
- Consultas y optimización.
- Control de accesos a nivel de datos.

## Instancias de base de datos de Amazon RDS

Una **instancia de base de datos RDS** es el entorno donde se ejecuta el motor de base de datos.

### Componentes

- Tipo de instancia (CPU y memoria).
- Motor de base de datos.
- Almacenamiento asociado.
- Configuración de red y seguridad.

## Amazon RDS en una nube virtual privada (VPC)

Amazon RDS se despliega dentro de una **Amazon VPC**:

- Aislamiento de red.
- Control total de subredes.
- Acceso mediante grupos de seguridad.
- Integración con aplicaciones EC2 y Lambda.

## Alta disponibilidad con la implementación Multi-AZ

### Implementación Multi-AZ

- Replica los datos automáticamente en otra zona de disponibilidad.
- Failover automático ante fallos.
- No requiere intervención del usuario.

### Beneficios

- Alta disponibilidad.
- Mayor tolerancia a fallos.
- Recuperación automática.

## Réplicas de lectura de Amazon RDS

Las **réplicas de lectura** permiten escalar las lecturas:

- Copia asíncrona de la base de datos principal.
- Ideales para cargas de lectura intensiva.
- No proporcionan alta disponibilidad (solo escalado).

## Casos de uso

Amazon RDS es ideal para:

- Aplicaciones web.
- Sistemas de gestión empresarial.
- Aplicaciones transaccionales.
- Sistemas que requieren SQL estándar.

## Cuándo utilizar Amazon RDS

Usa Amazon RDS cuando:

- Necesitas una base de datos relacional.
- Quieres reducir la carga operativa.
- Requieres alta disponibilidad.
- Buscas backups automáticos y escalabilidad.

## Amazon RDS: facturación por horas de reloj y características

### Facturación

- Se cobra por:
    - Tipo de instancia        
    - Almacenamiento.
    - IOPS (según tipo).
    - Transferencia de datos.

- Facturación por hora o segundo (según motor)

## Amazon RDS: tipo de compra y múltiples instancias

### Tipos de compra

- On-Demand.
- Instancias reservadas (ahorro a largo plazo).

### Múltiples instancias

- Instancia principal.
- Réplicas de lectura.
- Instancia secundaria Multi-AZ.

## Amazon RDS: almacenamiento

### Opciones de almacenamiento

- General Purpose SSD.
- Provisioned IOPS SSD.
- Escalado de almacenamiento automático.

## Idea clave de la sección

> **Amazon RDS simplifica la administración de bases de datos relacionales, ofreciendo alta disponibilidad, escalabilidad y seguridad sin la complejidad operativa tradicional.**

---
## Sección 2: Amazon DynamoDB

Esta sección introduce **Amazon DynamoDB**, el servicio de **base de datos NoSQL clave-valor y documentos** totalmente gestionado de AWS. Se destacan su **modelo de datos**, su **escalabilidad bajo demanda** y el uso de **particiones** para gestionar grandes volúmenes de información con baja latencia.

## Comparación entre bases de datos relacionales y no relacionales

### Bases de datos relacionales (SQL)

- Modelo basado en tablas con esquema fijo.
- Relaciones entre tablas mediante claves.
- Escalado principalmente vertical.
- Uso de SQL para consultas.

**Ejemplos**:

- Amazon RDS
- Amazon Aurora

### Bases de datos no relacionales (NoSQL)

- Esquema flexible.
- Datos almacenados como clave-valor o documentos.
- Escalado horizontal nativo.
- Diseñadas para alta disponibilidad y baja latencia.

**Ejemplo**:
- Amazon DynamoDB

|Característica|Relacional|No relacional|
|---|---|---|
|Esquema|Fijo|Flexible|
|Escalado|Vertical|Horizontal|
|Latencia|Variable|Muy baja|
|Casos de uso|Transaccional|Grandes volúmenes|

## ¿Qué es Amazon DynamoDB?

**Amazon DynamoDB** es una base de datos **NoSQL completamente administrada**, que ofrece:

- Rendimiento de milisegundos de un solo dígito.
- Escalado automático.
- Alta disponibilidad integrada.
- Sin servidores que administrar.

Está diseñada para aplicaciones que requieren:

- Acceso rápido.
- Escalabilidad masiva.
- Disponibilidad continua.

## Componentes principales de Amazon DynamoDB

### Tabla

- Recurso principal de DynamoDB.
- Almacena los datos en forma de elementos.

### Elementos (Items)

- Cada fila de la tabla.
- Representa una entidad única.
- Tamaño máximo limitado.

### Atributos

- Pares clave-valor dentro de un elemento.
- No todos los elementos necesitan tener los mismos atributos.

### Clave primaria

- Identificador único del elemento.
- Puede ser:
    - Clave de partición.
    - Clave de partición + clave de ordenación.

## Los elementos de una tabla deben tener una clave

En DynamoDB **todos los elementos deben tener una clave primaria**, que garantiza la unicidad.

### Tipos de clave primaria

#### Clave de partición
- DynamoDB usa esta clave para distribuir los datos.
- Determina en qué partición se almacena el elemento.

#### Clave compuesta (partición + ordenación)

- Permite múltiples elementos con la misma clave de partición.
- La clave de ordenación organiza los elementos relacionado

## Partición de datos y escalabilidad

DynamoDB divide automáticamente los datos en **particiones**:

- Cada partición almacena una parte de los datos.
- El sistema escala añadiendo particiones.
- El usuario no gestiona las particiones directamente.

### Beneficios
- Escalado horizontal transparente.
- Alto rendimiento constante.
- Manejo eficiente de grandes volúmenes de datos.

## Casos de uso comunes

Amazon DynamoDB es ideal para:

- Aplicaciones web y móviles a gran escala.
- Juegos en línea.
- Sistemas IoT.
- Carritos de compra y catálogos.
- Aplicaciones serverless con AWS Lambda.

## Idea clave de la sección

> **Amazon DynamoDB ofrece una base de datos NoSQL altamente escalable y de baja latencia, ideal para aplicaciones modernas que manejan grandes volúmenes de datos sin esquema rígido.**

---
## Sección 3: Amazon Redshift

Esta sección describe **Amazon Redshift**, el servicio de **almacenamiento de datos (data warehouse)** de AWS, diseñado para **consultas analíticas a gran escala**. Se explica su **arquitectura de procesamiento paralelo**, la compatibilidad con herramientas estándar y los **casos de uso más comunes** para análisis de grandes volúmenes de datos.

## Introducción a Amazon Redshift

**Amazon Redshift** es un servicio totalmente administrado que permite:

- Analizar grandes conjuntos de datos (terabytes o petabytes).
- Ejecutar consultas complejas de forma rápida.
- Utilizar SQL estándar para análisis.

Está optimizado para **lecturas intensivas y agregaciones**, no para transacciones frecuentes.

## Arquitectura de procesamiento en paralelo

Amazon Redshift utiliza una arquitectura **MPP (Massively Parallel Processing)**.

### Componentes principales

#### Nodo líder (Leader Node)

- Recibe las consultas SQL del cliente.
- Descompone las consultas en tareas más pequeñas.
- Coordina la ejecución y agrega los resultados.

#### Nodos de cómputo (Compute Nodes)

- Ejecutan las tareas en paralelo.
- Almacenan los datos localmente.
- Procesan fragmentos de las tablas.

### Beneficios del procesamiento paralelo

- Consultas más rápidas.
- Escalado horizontal.
- Uso eficiente de recursos.

## Distribución y almacenamiento de datos

- Los datos se distribuyen entre nodos.
- Se utilizan claves de distribución.
- El almacenamiento está optimizado para lectura analítica.

Esto permite manejar **conjuntos de datos muy grandes** con alto rendimiento.

## Compatibilidad

Amazon Redshift es compatible con:

- SQL estándar.
- Herramientas de BI y analítica.
- Integración con Amazon S3 (data lake).
- AWS Glue, Athena y QuickSight.

También soporta:

- Carga de datos desde S3, DynamoDB y otras fuentes.
- Integración con pipelines de datos.

## Casos de uso de Amazon Redshift

Amazon Redshift es ideal para:

- Data warehousing empresarial.
- Análisis de grandes volúmenes de datos históricos.
- Inteligencia de negocio (BI).
- Informes complejos y agregaciones.
- Análisis de logs y eventos.

## Comparación rápida con otras bases de datos

|Servicio|Tipo|Uso principal|
|---|---|---|
|RDS|Relacional|Transacciones|
|DynamoDB|NoSQL|Baja latencia|
|Redshift|Data warehouse|Analítica|

## Idea clave de la sección

> **Amazon Redshift permite analizar grandes volúmenes de datos de forma rápida mediante procesamiento paralelo, siendo ideal para cargas analíticas y de inteligencia de negocio.**

---

## Sección 4: Amazon Aurora

Esta sección presenta **Amazon Aurora**, el motor de base de datos relacional administrado de AWS, compatible con **MySQL y PostgreSQL**, y explica por qué en muchos escenarios es la **mejor alternativa a Amazon RDS tradicional**. Se detallan sus **beneficios**, así como su diseño de **alta disponibilidad y resiliencia** mediante múltiples zonas de disponibilidad.

## Amazon Aurora

**Amazon Aurora** es un motor de base de datos relacional diseñado específicamente para la nube de AWS.

### Características principales

- Compatible con **MySQL** y **PostgreSQL**.
- Totalmente administrado por AWS.
- Rendimiento superior frente a motores estándar.
- Diseñado para alta disponibilidad y escalabilidad.

Aurora se utiliza a través del servicio **Amazon RDS**, pero con una arquitectura propia.

## Beneficios del servicio Amazon Aurora

### 1. Alto rendimiento

- Hasta 5 veces más rápido que MySQL estándar.
- Hasta 3 veces más rápido que PostgreSQL estándar.
- Optimizado para cargas transaccionales.

### 2. Escalabilidad

- Almacenamiento que crece automáticamente.
- Soporte para múltiples réplicas de lectura.
- Escalado sin interrupciones.

### 3. Gestión simplificada

- Backups automáticos continuos.
- Recuperación punto en el tiempo.
- Parches gestionados por AWS    

### 4. Seguridad integrada

- Cifrado en reposo y en tránsito.
- Integración con AWS IAM y KMS.
- Aislamiento en VPC.

## Alta disponibilidad

Amazon Aurora está diseñado para funcionar de forma **altamente disponible** de manera nativa.

### Arquitectura Multi-AZ

- Los datos se replican automáticamente en **seis copias**.
- Distribuidas en **tres zonas de disponibilidad**.
- Failover automático rápido ante fallos.
### Ventajas

- Minimiza tiempos de inactividad.
- Alta durabilidad de los datos.
- No requiere configuración compleja por parte del usuario.

## Diseño resiliente

El diseño de Aurora prioriza la **resiliencia** ante fallos:

- Separación de cómputo y almacenamiento.
- Recuperación automática ante fallos de nodos.
- Sustitución transparente de instancias defectuosas.
- Replicación continua de datos.

Esto permite que la base de datos siga operando incluso ante fallos de infraestructura.

## ¿Cuándo elegir Amazon Aurora?

Amazon Aurora es la mejor opción cuando:

- Se necesita alto rendimiento relacional.
- Se requiere alta disponibilidad por defecto.
- Se busca escalabilidad automática.
- Se quiere compatibilidad con MySQL o PostgreSQL sin gestionar la infraestructura.

## Comparación rápida: RDS vs Aurora

|Característica|RDS tradicional|Aurora|
|---|---|---|
|Arquitectura|Clásica|Nativa cloud|
|Rendimiento|Estándar|Alto|
|Replicación|Limitada|Multi-AZ avanzada|
|Escalabilidad|Manual|Automática|


## Idea clave de la sección

> **Amazon Aurora combina la potencia de las bases de datos relacionales con una arquitectura cloud-native altamente disponible y resiliente, siendo ideal para aplicaciones críticas.**


---
## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Describir Amazon RDS
- Identificar la funcionalidad en Amazon RDS
- Describir Amazon DynamoDB
- Identificar la funcionalidad en Amazon DynamoDB
- Describir Amazon Redshift
- Describir Amazon Aurora
- Realizar tareas en BBDD de RDS, como lanzamientos, configuraciones e interacciones.
### Pregunta del examen de muestra

¿Cuál de las siguientes opciones representa un servicio de BBDD NoSQL completamente administrado?
- Amazon DynamoDB.