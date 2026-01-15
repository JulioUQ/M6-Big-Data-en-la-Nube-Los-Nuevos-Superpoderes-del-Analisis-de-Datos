
## Módulo 4: Seguridad en la nube de AWS

Este módulo introduce el **enfoque de seguridad de AWS**, explicando cómo AWS y el cliente **comparten responsabilidades** y qué servicios y prácticas permiten proteger **cuentas, identidades y datos** en la nube.

### Objetivo del módulo

Comprender cómo funciona la seguridad en AWS, qué responsabilidades asume AWS y cuáles recaen en el cliente, y conocer los servicios clave para implementar un entorno seguro y conforme.

---

### Secciones del módulo

### Sección 1: Modelo de responsabilidad compartida de AWS

Esta sección presenta el **Modelo de responsabilidad compartida de AWS**, que define claramente qué aspectos de la seguridad son responsabilidad de AWS y cuáles corresponden al cliente. Este modelo es fundamental para entender cómo proteger correctamente los recursos en la nube.

#### Responsabilidad de AWS: _seguridad de la nube_

AWS es responsable de proteger la infraestructura que ejecuta todos los servicios de la nube, incluyendo:

- Centros de datos físicos.
- Hardware, servidores y dispositivos de red.
- Infraestructura global (regiones, zonas de disponibilidad y red).
- Capa de virtualización y software administrado por AWS.

AWS garantiza que esta infraestructura sea **segura, resiliente y conforme** a estándares internacionales.

#### Responsabilidad del cliente: _seguridad en la nube_

El cliente es responsable de proteger todo lo que implementa y configura dentro de AWS, incluyendo:

- Configuración de sistemas operativos y aplicaciones.
- Administración de identidades y accesos (usuarios, roles y permisos).
- Protección de datos (cifrado y control de acceso).
- Configuración de redes, grupos de seguridad y ACL.

El nivel de responsabilidad del cliente **varía según el servicio** que utilice (IaaS, PaaS o SaaS).

#### Características del servicio y responsabilidad en materia de seguridad

- En servicios **IaaS** (como Amazon EC2), el cliente tiene mayor control y mayor responsabilidad.
- En servicios **PaaS** (como Amazon RDS o AWS Lambda), AWS asume más responsabilidades operativas.
- En servicios completamente administrados, AWS gestiona la mayor parte de la seguridad subyacente.

Comprender este modelo permite diseñar arquitecturas seguras y evitar configuraciones incorrectas que puedan generar riesgos.

---

### Sección 2: AWS Identity and Access Management (AWS IAM)

Esta sección introduce los **conceptos clave de AWS Identity and Access Management (IAM)**, el servicio que permite administrar **quién puede acceder a los recursos de AWS** y **qué acciones puede realizar** cada identidad.

### IAM: componentes esenciales

AWS IAM se basa en los siguientes componentes principales:

- **Identidades**: usuarios, grupos y roles.
- **Políticas**: definen permisos mediante reglas.
- **Autenticación**: proceso de verificación de identidad.
- **Autorización**: definición de acciones permitidas.

---
### Autenticarse como usuario de IAM para obtener acceso

- Un **usuario de IAM** representa a una persona o aplicación.
- Los usuarios se autentican mediante:
    - Nombre de usuario y contraseña (Consola de AWS).
    - Claves de acceso (AWS CLI, SDK y API).

- Se recomienda **no utilizar el usuario raíz** para tareas diarias.

---
### MFA en IAM (Autenticación multifactor)

- MFA agrega una **capa adicional de seguridad**.
- Requiere algo que el usuario _sabe_ (contraseña) y algo que _tiene_ (dispositivo MFA).
- AWS recomienda habilitar MFA:
    - En el usuario raíz.
    - En usuarios de IAM con permisos administrativos.

---
### Autorización: qué acciones están permitidas

- La **autorización** determina:
    - Qué acciones puede realizar una identidad.
    - Sobre qué recursos.
    - En qué condiciones.

- La autorización en IAM se controla mediante **políticas**.
---
### IAM: autorización

- IAM evalúa las políticas asociadas a una identidad.
- De forma predeterminada:
    - **Todo está denegado**.
    - Solo se permite lo que esté explícitamente autorizado.

---
### Políticas de IAM

- Son documentos en formato **JSON**.
- Definen permisos mediante declaraciones (_statements_).
- Especifican:
    - Acciones (`Action`).
    - Recursos (`Resource`).
    - Efecto (`Allow` o `Deny`).

---
### Políticas basadas en recursos

- Se adjuntan directamente a un recurso de AWS.
- Definen **quién puede acceder** a ese recurso.

- Ejemplos comunes:
    - Políticas de buckets de Amazon S3.
    - Políticas de colas de Amazon SQS.

---
### Permisos de IAM

- Los permisos determinan qué operaciones están permitidas.

- Se otorgan mediante:
    - Políticas administradas por AWS.
    - Políticas administradas por el cliente.
    - Políticas en línea.

---
### Grupos de IAM

- Un **grupo** es una colección de usuarios.
- Las políticas se asignan al grupo, no a cada usuario individual.
- Facilitan la administración de permisos.

---
### Roles de IAM

- Un **rol** no está asociado a una persona específica.
- Se asume temporalmente para obtener permisos.
- Se utilizan comúnmente para:
    - Servicios de AWS.
    - Aplicaciones.
    - Acceso entre cuentas.

---
### Ejemplo de uso de un rol de IAM

- Una instancia de **Amazon EC2** necesita acceder a Amazon S3.
- Se crea un **rol de IAM** con permisos para S3.
- El rol se asigna a la instancia EC2.
- La aplicación accede a S3 **sin usar claves de acceso**.

Este enfoque mejora la seguridad al evitar el uso de credenciales estáticas.

---

## Sección 3: Protección de una nueva cuenta de AWS

Esta sección proporciona una **guía práctica para asegurar una nueva cuenta de AWS** desde el primer momento. Se centra en reducir riesgos comunes mediante el uso correcto de identidades, la activación de controles de seguridad y la supervisión de la actividad y los costos.

---
### Acceso de usuario raíz de la cuenta de AWS frente al acceso de IAM

- El **usuario raíz** tiene **acceso total e ilimitado** a todos los recursos de la cuenta.
- AWS recomienda **no usar el usuario raíz para actividades diarias**.
- En su lugar, se deben crear **usuarios de IAM** con permisos específicos según su función.
- El acceso diario debe realizarse siempre mediante **usuarios o roles de IAM**.

---
### Protección de una nueva cuenta de AWS: usuario raíz de la cuenta

Buenas prácticas para el usuario raíz:

- Utilizarlo **solo para tareas críticas**, como:
    - Cambiar información de la cuenta.
    - Configurar opciones de facturación.
    - Cerrar la cuenta.

- Proteger sus credenciales de forma estricta.
- No crear claves de acceso para el usuario raíz.
---
### Protección de una nueva cuenta de AWS: MFA

- La **autenticación multifactor (MFA)** agrega una capa adicional de seguridad.
    
- Requiere:
    - Algo que el usuario sabe (contraseña).
    - Algo que el usuario tiene (dispositivo MFA).

- AWS recomienda:
    - **Habilitar MFA en el usuario raíz**.
    - Habilitar MFA en usuarios de IAM con permisos administrativos.

- Reduce significativamente el riesgo de accesos no autorizados.
---
### Protección de una nueva cuenta de AWS: AWS CloudTrail

- **AWS CloudTrail** registra la actividad de la cuenta.

- Permite:
    - Auditar acciones realizadas por usuarios y servicios.
    - Detectar actividades sospechosas.
    - Cumplir requisitos de seguridad y conformidad.

- Se recomienda:
    - Habilitar CloudTrail desde el inicio.
    - Almacenar los registros de forma segura (por ejemplo, en Amazon S3).
---
### Protección de una nueva cuenta de AWS: informes de facturación

- Los **informes y alertas de facturación** ayudan a detectar:
    - Gastos inesperados.
    - Uso no autorizado de recursos.

- Buenas prácticas:
    - Activar alertas de facturación.
    - Revisar periódicamente los informes de costos.

- Esto contribuye tanto a la **seguridad** como al **control financiero**.
---
# **Sección 4: Protección de cuentas**

Además de IAM, AWS ofrece **servicios y mecanismos adicionales** para reforzar la seguridad de las cuentas, especialmente en entornos con **múltiples cuentas**, aplicaciones públicas y datos sensibles. Esta sección cubre las principales herramientas.

---

## 1. Políticas de control de servicios (SCP)

### ¿Qué son las SCP?

Las **Service Control Policies (SCP)** son políticas de seguridad que se utilizan dentro de **AWS Organizations** para definir **límites máximos de permisos** en una o varias cuentas de AWS.

📌 **Idea clave**:

> Una SCP **no concede permisos**, solo **restringe** los permisos que pueden concederse mediante IAM.

---
### ¿Dónde se aplican?

- A nivel de:
    - Organización
    - Unidad organizativa (OU)
    - Cuenta individual

---
### ¿Cómo funcionan?

El permiso final de un usuario es la intersección de:
1. Permisos IAM (usuarios, grupos, roles)
2. Permisos permitidos por la SCP

Si una acción está **denegada por una SCP**, **nadie puede ejecutarla**, ni siquiera el usuario root de la cuenta.

---

### Ejemplos comunes de SCP

- Bloquear el uso de ciertos servicios (por ejemplo, S3 o EC2)
- Evitar acciones peligrosas:
    - `iam:DeleteUser`
    - `organizations:LeaveOrganization`

- Restringir regiones:
    - Permitir recursos solo en `eu-west-1`

---

### Caso práctico (resultado esperado)

✔️ Se garantiza que ninguna cuenta pueda:

- Eliminar registros de auditoría
- Desactivar CloudTrail
- Crear recursos fuera de regiones permitidas

---
## 2. AWS Key Management Service (AWS KMS)

### ¿Qué es AWS KMS?

**AWS KMS** es un servicio administrado para **crear, administrar y controlar claves criptográficas** utilizadas para cifrar datos en AWS.

---
### ¿Qué protege?

- Datos en reposo en servicios como:
    - Amazon S3
    - Amazon EBS
    - Amazon RDS
    - Amazon Redshift
---
### Funciones principales

- Creación de **Customer Managed Keys (CMK)**
- Integración nativa con servicios AWS
- Control de acceso mediante políticas IAM y políticas de clave
- Registro de uso en **AWS CloudTrail**

---
### Tipos de claves

- **AWS Managed Keys**: creadas y gestionadas por AWS
- **Customer Managed Keys**: control total por el cliente
- **Claves importadas**: claves externas traídas a AWS

---
### Caso práctico (resultado esperado)

✔️ Los datos:

- Están cifrados automáticamente
- Solo pueden descifrarse por usuarios/servicios autorizados
- Cumplen requisitos de seguridad y normativas (RGPD, ISO, etc.)

---
## 3. Amazon Cognito

### ¿Qué es Amazon Cognito?

**Amazon Cognito** es un servicio de **gestión de identidades para aplicaciones**, especialmente móviles y web.

📌 No se usa para administrar usuarios internos de AWS, sino **usuarios finales**.

---
### ¿Qué permite?

- Registro e inicio de sesión de usuarios
- Autenticación:
    - Usuario/contraseña
    - MFA
    - Proveedores externos (Google, Facebook, Apple, SAML)

- Emisión de tokens (JWT)
- Integración con servicios AWS
---
### Componentes principales

- **User Pools**: gestión de usuarios
- **Identity Pools**: acceso temporal a recursos AWS
---
### Caso práctico (resultado esperado)

✔️ Una aplicación:

- Gestiona usuarios sin crear usuarios IAM
- Aplica autenticación segura
- Accede a AWS de forma controlada y temporal
---
## 4. AWS Shield

### ¿Qué es AWS Shield?

**AWS Shield** es un servicio administrado que protege aplicaciones contra **ataques de denegación de servicio distribuido (DDoS)**.

---
### Tipos de protección

#### 🔹 AWS Shield Standard

- Incluido automáticamente
- Protege contra ataques DDoS comunes
- Funciona con:
    - CloudFront
    - Route 53
    - Elastic Load Balancing

---
#### 🔹 AWS Shield Advanced

- Servicio de pago
- Protección ampliada contra ataques sofisticados
- Acceso al **DDoS Response Team (DRT)**
- Integración con AWS WAF

---
### Caso práctico (resultado esperado)

✔️ La aplicación:

- Mantiene disponibilidad frente a ataques
- Reduce el impacto económico y operativo
- Se beneficia de mitigación automática

---
## 5. Resumen final de la sección (RESUELTO)

|Servicio|¿Qué protege?|Uso principal|
|---|---|---|
|SCP|Cuentas completas|Límites globales de seguridad|
|AWS KMS|Datos|Cifrado y gestión de claves|
|Amazon Cognito|Usuarios finales|Autenticación de apps|
|AWS Shield|Infraestructura|Protección DDoS|

---
# **Sección 5: Protección de datos en AWS**

La protección de datos es uno de los pilares de la seguridad en AWS. AWS proporciona **múltiples capas de seguridad** para proteger los datos **en reposo**, **en tránsito** y mediante **controles de acceso**, especialmente en servicios clave como **Amazon S3**.

---
## 1. Cifrado de datos en AWS

### 1.1 Cifrado de datos en reposo

El **cifrado en reposo** protege los datos almacenados frente a accesos no autorizados, incluso si el almacenamiento físico se ve comprometido.

### Opciones de cifrado en reposo

- **Cifrado del lado del servidor (Server-Side Encryption – SSE)**
    - SSE-S3: gestionado completamente por AWS
    - SSE-KMS: gestionado con **AWS KMS**
    - SSE-C: claves proporcionadas por el cliente

- **Cifrado del lado del cliente**
    - El cliente cifra los datos antes de enviarlos a AWS.

### Resultado esperado

✔️ Los datos almacenados permanecen cifrados automáticamente  
✔️ El acceso a datos cifrados está controlado por IAM y KMS  
✔️ Cumplimiento de normativas (RGPD, ISO 27001, HIPAA, etc.)

---
### 1.2 Cifrado de datos en tránsito

El **cifrado en tránsito** protege los datos mientras se mueven entre:

- Clientes ↔ AWS
- Servicios internos de AWS
### Mecanismos utilizados

- **HTTPS (TLS)**
- Certificados digitales gestionados por:
    - AWS Certificate Manager (ACM)
### Resultado esperado

✔️ Los datos no pueden ser interceptados o modificados  
✔️ Comunicación segura extremo a extremo

---
## 2. Protección de datos en Amazon S3

Amazon S3 es uno de los servicios más utilizados para almacenar datos, por lo que AWS proporciona **controles específicos** para protegerlos.

---

### 2.1 Opciones de cifrado en Amazon S3

Amazon S3 admite cifrado automático en reposo:

|Método|Gestión de claves|Uso recomendado|
|---|---|---|
|SSE-S3|AWS|Casos simples|
|SSE-KMS|Cliente (KMS)|Entornos regulados|
|SSE-C|Cliente|Requisitos externos|

📌 **Mejor práctica**: habilitar **cifrado por defecto del bucket**

---
### 2.2 Control de acceso a datos en S3

Los accesos a S3 se controlan mediante:

- **IAM Policies**
- **Bucket Policies**
- **ACLs** (menos recomendadas)
- **AWS Organizations + SCP**

---
### 2.3 Protección de datos sensibles

Opciones avanzadas:

- **Bloqueo de acceso público**
- **Versionado**
- **Object Lock**
- **MFA Delete**

---

## 3. Protección de buckets de Amazon S3

### 3.1 Bloqueo de acceso público (Public Access Block)

Función clave para evitar filtraciones de datos.

Permite:

- Bloquear acceso público a nivel:
    - Cuenta
    - Bucket

✔️ Evita configuraciones accidentales de acceso público

---
### 3.2 Bucket Policies

Las **políticas de bucket** permiten controlar:

- Quién puede acceder
- Desde dónde (IP, VPC)
- Si se requiere cifrado
- Uso obligatorio de HTTPS

Ejemplo de restricciones habituales:

- Denegar acceso sin TLS
- Permitir acceso solo desde una VPC

---
### 3.3 Versionado de objetos

Permite:

- Recuperar versiones anteriores
- Proteger frente a borrados accidentales
- Soportar recuperación ante ransomware

✔️ Cada modificación crea una nueva versión

---
### 3.4 Object Lock

Protección contra eliminación o modificación:

- **Modo Governance**
- **Modo Compliance**

📌 Ideal para:

- Registros legales
- Copias de seguridad
- Cumplimiento normativo

---
### 3.5 Registro y auditoría

Servicios implicados:

- **AWS CloudTrail**
- **S3 Access Logs**

Permiten:

- Saber quién accede
- Cuándo y desde dónde
- Qué acciones se realizaron

---
## 4. Protección de objetos de Amazon S3

### Controles a nivel de objeto

- Permisos individuales
- Cifrado específico
- Versiones independientes
---
### Resultado esperado

✔️ Cada objeto está cifrado  
✔️ Acceso controlado por políticas  
✔️ Auditoría completa del acceso

---
## 5. Resumen final de la sección (RESUELTO)

|Aspecto|Mecanismo|
|---|---|
|Datos en reposo|SSE / KMS|
|Datos en tránsito|HTTPS / TLS|
|Protección S3|Bucket Policies|
|Prevención de filtraciones|Public Access Block|
|Recuperación|Versionado / Object Lock|
|Auditoría|CloudTrail / Logs|

---
# **Sección 6: Trabajar para la garantía de la conformidad**

La **conformidad (compliance)** en AWS se refiere al cumplimiento de **leyes, normativas y estándares de seguridad** que rigen el tratamiento de datos y la operación de sistemas. AWS proporciona **infraestructura conforme** y herramientas que ayudan a los clientes a **demostrar y mantener** ese cumplimiento.

---
## 1. Programas de conformidad de AWS

### ¿Qué son los programas de conformidad?

AWS mantiene certificaciones y acreditaciones reconocidas internacionalmente que validan que su infraestructura cumple con requisitos legales y normativos.

📌 **Responsabilidad compartida**:

- AWS: seguridad **de** la nube (infraestructura)
- Cliente: seguridad **en** la nube (configuración y uso)

---

### Principales certificaciones de AWS

|Norma / Regulación|Finalidad|
|---|---|
|ISO 27001|Gestión de seguridad de la información|
|ISO 27017|Controles de seguridad en la nube|
|ISO 27018|Protección de datos personales|
|SOC 1, SOC 2, SOC 3|Controles de seguridad y auditoría|
|PCI DSS|Seguridad de datos de tarjetas|
|GDPR / RGPD|Protección de datos personales|
|HIPAA|Información sanitaria|
|FedRAMP|Sector público (EE. UU.)|

✔️ AWS audita y mantiene estas certificaciones de forma continua

---
## 2. AWS Config

### ¿Qué es AWS Config?

**AWS Config** es un servicio que permite:

- Evaluar
- Auditar
- Registrar configuraciones de recursos AWS

Proporciona una **vista histórica** de los cambios de configuración.

---
### Funcionalidades principales

- Inventario de recursos
- Historial de cambios
- Evaluación automática de reglas de conformidad
- Notificaciones ante incumplimientos

---

### Reglas de AWS Config

- **Managed Rules**: reglas predefinidas por AWS
- **Custom Rules**: reglas creadas por el cliente (Lambda)

Ejemplos:

- Buckets S3 sin cifrado
- Instancias sin etiquetas obligatorias
- Security Groups con puertos abiertos

---

## 3. AWS Artifact

### ¿Qué es AWS Artifact?

**AWS Artifact** es un portal de autoservicio que permite:

- Acceder a informes de conformidad de AWS
- Descargar documentos oficiales de auditoría

---
### Tipos de documentos disponibles

- Informes **SOC**
- Certificados **ISO**
- Informes **PCI**
- Documentación para **RGPD**, **HIPAA**, etc.

---

### AWS Artifact Agreements

Permite:
- Firmar acuerdos legales con AWS
- Aceptar términos regulatorios específicos

Ejemplo:
- Acuerdos de procesamiento de datos (DPA)

---
## 4. Relación entre servicios de conformidad

|Servicio|Función|
|---|---|
|Programas AWS|Certificación de la infraestructura|
|AWS Config|Control continuo de configuraciones|
|AWS Artifact|Evidencia y documentación legal|

---
## 5. Resumen final de la sección (RESUELTO)

- AWS ofrece infraestructura certificada
- El cliente configura y mantiene la conformidad
- AWS Config detecta incumplimientos
- AWS Artifact proporciona pruebas oficiales
- Se reduce el esfuerzo de auditoría

---
## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Reconocer el modelo de responsabilidad compartida
- Identificar la responsabilidad el cliente y de AWS
- Reconocer usuarios, grupos, roles de IAM
- Describir los diferentes tipos de credenciales de seguridad de IAM
- Identificar los pasos para proteger una nueva cuenta de AWS
- Explorar los usuarios y grupos de IAM
- Reconocer como proteger los datos de AWS
- Reconocer los programas de conformidad de AWS
### Pregunta del examen de muestra

¿Cuál de las siguientes opciones es responsabilidad de AWS según el modelo de responsabilidad compartida de AWS?
- Ubicaciones al borde.

