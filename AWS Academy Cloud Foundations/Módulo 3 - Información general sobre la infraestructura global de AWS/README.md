## Módulo 3: Información general sobre la infraestructura global de AWS

Este módulo proporciona una visión general de la **infraestructura global de la nube de AWS**, explicando cómo está diseñada para ofrecer **alta disponibilidad, escalabilidad, seguridad y baja latencia** a nivel mundial.

### Objetivo del módulo

Comprender cómo AWS organiza su infraestructura global y cómo estos componentes permiten diseñar arquitecturas **resilientes, eficientes y de alto rendimiento**.

---

## Sección 1: Infraestructura global de AWS

Esta sección presenta los **componentes fundamentales** que conforman la infraestructura global de AWS y el papel que desempeña cada uno.

### Infraestructura global de AWS

- Conjunto de **centros de datos interconectados** distribuidos por todo el mundo.
- Diseñada para proporcionar:
    - Alta disponibilidad
    - Tolerancia a fallos
    - Escalabilidad bajo demanda

---

### Regiones de AWS

- Una **región** es una ubicación geográfica independiente donde AWS agrupa recursos.
    
- Cada región:
    - Está físicamente separada de las demás.
    - Es independiente para reducir el impacto de fallos a gran escala.

---

### Factores para seleccionar una región

Al elegir una región de AWS, se deben considerar los siguientes factores:

- **Latencia** cercana a los usuarios finales.
- **Requisitos legales y normativos** (residencia de datos).
- **Disponibilidad de servicios** en esa región.
- **Costos** asociados a los servicios.

---

### Zonas de disponibilidad (Availability Zones)

- Son **centros de datos independientes** dentro de una región.
- Están diseñadas para:
    - Aislar fallos.
    - Permitir arquitecturas de alta disponibilidad.

- Se conectan entre sí mediante enlaces de **alta velocidad y baja latencia**.

---

### Infraestructura de red

- AWS utiliza una **red privada global**.
- Permite:
    - Comunicación segura entre servicios.
    - Alto rendimiento entre regiones y zonas de disponibilidad.

---
### Puntos de presencia (Points of Presence)

- Incluyen:
    - **Edge Locations**
    - **Regional Edge Caches**

- Se utilizan principalmente por servicios como:
    - Amazon CloudFront
    - Amazon Route 53

- Mejoran el rendimiento al **reducir la latencia** en la entrega de contenido.
---
### Centros de datos de AWS

- Instalaciones físicas altamente seguras.
    
- Incorporan:
    - Controles estrictos de acceso.
    - Energía redundante.
    - Sistemas avanzados de refrigeración.
---
### Características de la infraestructura de AWS

- Alta disponibilidad y resiliencia.
- Escalabilidad global.
- Seguridad integrada desde el diseño.
- Flexibilidad para múltiples tipos de cargas de trabajo.

---
### Sección 2: Información general de servicios y categorías de AWS

Esta sección presenta las **principales categorías de servicios de AWS** y proporciona una visión general de los servicios más relevantes que se analizarán a lo largo del curso. AWS organiza sus servicios en categorías para facilitar su identificación y uso según las necesidades del negocio y los requisitos técnicos.

### Servicios básicos de AWS

#### Servicios de almacenamiento

Permiten almacenar y recuperar datos de forma segura, escalable y duradera.

- Amazon Simple Storage Service (Amazon S3)
- Amazon Elastic Block Store (Amazon EBS)
- Amazon Elastic File System (Amazon EFS)
- Amazon S3 Glacier

#### Servicios de informática (cómputo)

Proporcionan capacidad de procesamiento bajo demanda.

- Amazon Elastic Compute Cloud (Amazon EC2)
- AWS Lambda
- AWS Elastic Beanstalk
- Servicios de contenedores (Amazon ECS, Amazon EKS)

#### Servicios de bases de datos

Permiten almacenar y gestionar datos estructurados y no estructurados.

- Amazon Relational Database Service (Amazon RDS)
- Amazon DynamoDB
- Amazon Redshift
- Amazon Aurora

#### Servicios de redes y entrega de contenido

Facilitan la conectividad, el enrutamiento y la entrega eficiente de contenido.

- Amazon Virtual Private Cloud (Amazon VPC)
- Amazon Route 53
- Amazon CloudFront
- Elastic Load Balancing (ELB)

#### Servicios de seguridad, identidad y conformidad

Ayudan a proteger recursos, controlar accesos y cumplir normativas.

- AWS Identity and Access Management (IAM)
- AWS Organizations
- AWS Shield
- AWS Key Management Service (AWS KMS)

#### Servicios de administración de costos de AWS

Permiten supervisar, controlar y optimizar los costos.

- AWS Billing and Cost Management
- AWS Cost Explorer
- AWS Budgets

#### Servicios de administración y gobernanza

Facilitan la operación, supervisión y control de entornos en AWS.

- Amazon CloudWatch
- AWS CloudTrail
- AWS Config
- AWS Trusted Advisor

Esta clasificación ayuda a comprender cómo los distintos servicios de AWS trabajan juntos para crear soluciones completas en la nube.

---
## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Identificar las diferencias entre las regiones , las zonas de disponibilidad y las ubicaciones de borde de AWS.
- Identificar los servicios de AWS y sus categorias.
### Pregunta del examen de muestra

¿Que componente de la infraestructura global de AWS utiliza Amazon CloudFront para garantizar una entrega con baja latencia?
- Ubicaciones al borde.

El módulo finaliza con una **actividad práctica de exploración** de la **Consola de administración de AWS**, que permite al estudiante familiarizarse con su interfaz y navegación.