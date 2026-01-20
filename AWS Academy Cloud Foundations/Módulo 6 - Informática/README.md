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



**Sección 5: Optimización de costos con Amazon EC2**  
- Modelos de precios de Amazon EC2
- Beneficios de los modelos de precios Amazon EC2
- Caos de uso de los modelos de precios de Amazon EC2
- Los cuatro pilares de la optimización de costos
	- Pilar 1: Adaptación del tamaño
	- Pilar 2: Aumento de la elasticidad
	- Pilar 3: Modelo de precios óptimo
	- Pilar 4: Optimización de las opciones de almacenamiento
- Medicion, monitoreo y mejoras

**Sección 5: Introducción a AWS Lambda**  
Proporciona los fundamentos de **AWS Lambda**, la solución serverless de AWS para ejecutar código sin aprovisionar servidores.

**Sección 6: Introducción a AWS Elastic Beanstalk**  
Explica cómo **AWS Elastic Beanstalk** facilita la implementación y escalado de aplicaciones web y servicios desarrollados con diversos lenguajes y frameworks.