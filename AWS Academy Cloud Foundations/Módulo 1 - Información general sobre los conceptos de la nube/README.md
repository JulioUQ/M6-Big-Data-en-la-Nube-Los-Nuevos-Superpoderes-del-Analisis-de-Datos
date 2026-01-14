Este módulo introduce los fundamentos de la computación en la nube y el ecosistema de AWS. A lo largo de sus secciones, el estudiante comprenderá qué es la nube, por qué aporta ventajas frente a los modelos tradicionales y cómo AWS ofrece un conjunto integrado de servicios para cumplir objetivos empresariales y tecnológicos.

## **Sección 1: Introducción a la computación en la nube**

Esta sección sienta las bases para entender qué es la computación en la nube, cómo se diferencia de la informática tradicional y qué modelos existen para consumir servicios en la nube.

### **¿Qué es la informática en la nube?**

La **computación en la nube** es un modelo que permite acceder bajo demanda a recursos informáticos —como servidores, almacenamiento, bases de datos, redes, software o capacidad de cómputo— a través de Internet, sin necesidad de poseer ni gestionar físicamente la infraestructura.

Sus características clave son:

- **Acceso bajo demanda**: los recursos se pueden aprovisionar cuando se necesitan.
- **Pago por uso**: solo se paga por los recursos utilizados.
- **Escalabilidad y elasticidad**: los recursos pueden aumentar o disminuir rápidamente.
- **Acceso desde cualquier lugar** con conexión a Internet.
- **Gestión delegada**: el proveedor cloud se encarga del mantenimiento físico.

En lugar de comprar hardware y configurarlo manualmente, la nube permite consumir tecnología como un servicio.

### **Infraestructura como software**

En la computación en la nube, la infraestructura deja de gestionarse manualmente y pasa a definirse mediante **software**.

Esto significa que:

- Servidores, redes y almacenamiento se crean mediante **configuraciones y código**, no mediante instalaciones físicas.
- La infraestructura puede automatizarse, reproducirse y versionarse.
- Las operaciones son más rápidas, consistentes y menos propensas a errores humanos.

Este enfoque es la base de conceptos como **Infraestructura como Código (IaC)** y permite que la TI sea más ágil y flexible, alineándose mejor con las necesidades del negocio.

---

### **Modelo de informática tradicional**

En el modelo tradicional (on-premise):

- La empresa **compra y mantiene** sus propios servidores, redes y sistemas de almacenamiento.
- Es necesario **prever la capacidad máxima** desde el inicio, lo que suele implicar sobrecostes.
- La ampliación de recursos es lenta (compra, instalación, configuración).
- El mantenimiento, la seguridad física, la refrigeración y la energía son responsabilidad de la organización.

Este modelo ofrece control total, pero con **altos costes iniciales**, menor flexibilidad y mayor complejidad operativa.

---

### **Modelo de informática en la nube**

En el modelo cloud:

- Los recursos se **alquilan** a un proveedor (como AWS).
- No se requiere inversión inicial en hardware.
- La capacidad se adapta dinámicamente a la demanda.
- El proveedor se encarga de la infraestructura física y su disponibilidad.

Este enfoque permite:

- Reducir costes.
- Acelerar la innovación.
- Enfocar los esfuerzos en el desarrollo y el negocio, no en la gestión del hardware.

---

### **Modelo de servicio en la nube (IaaS, PaaS, SaaS)**

_(De mayor a menor control sobre los recursos de TI)_

Los servicios en la nube se clasifican según el **nivel de control y responsabilidad** que mantiene el cliente:

#### **IaaS – Infraestructura como Servicio**

- El proveedor ofrece recursos básicos (servidores, red, almacenamiento).
- El cliente gestiona sistemas operativos, aplicaciones y datos.
- Ofrece **máximo control** dentro de la nube.

👉 Similar a tener un servidor tradicional, pero virtual y bajo demanda.

---

#### **PaaS – Plataforma como Servicio**

- El proveedor gestiona infraestructura y sistema operativo.
- El cliente se centra en el desarrollo y despliegue de aplicaciones.
- Reduce la complejidad operativa.

👉 Ideal para desarrolladores que no quieren administrar servidores.

---

#### **SaaS – Software como Servicio**

- El proveedor gestiona todo: infraestructura, plataforma y aplicación.
- El usuario solo consume el software.

👉 Ejemplos comunes: correo electrónico web, CRM, herramientas colaborativas.

📌 **Idea clave**:  
Cuanto más se avanza de IaaS a SaaS, **menos control** tiene el cliente, pero **menos responsabilidad técnica** asume.

---

### **Modelos de implementación de informática en la nube**

Existen diferentes formas de desplegar la nube según las necesidades de la organización:

#### **Nube pública**

- Los recursos son compartidos entre múltiples clientes.
- Gestionada por un proveedor externo.
- Alta escalabilidad y bajo coste.

#### **Nube privada**

- Infraestructura dedicada a una sola organización.
- Puede estar en un centro propio o externo.
- Mayor control y personalización.

#### **Nube híbrida**

- Combina nube privada y pública.
- Permite mover cargas de trabajo entre ambas.
- Muy común en procesos de migración.

#### **Multicloud**

- Uso de servicios de varios proveedores cloud.
- Reduce dependencia de un único proveedor.

---

### **Similitudes entre AWS y la TI tradicional**

Aunque AWS es una plataforma cloud, comparte muchos conceptos con la TI tradicional:

- Uso de **servidores**, **redes**, **firewalls** y **almacenamiento**.
- Necesidad de diseñar arquitecturas seguras y eficientes.
- Aplicación de buenas prácticas de seguridad, respaldo y monitorización.

La diferencia clave es **cómo se accede y gestiona** esa infraestructura:

- En AWS todo es **virtual, automatizable y bajo demanda**.
- Los tiempos, costes y escalabilidad mejoran drásticamente.

---

## **Sección 2: Ventajas de la computación en la nube**

Esta sección explica los **principales beneficios** de la computación en la nube frente a los modelos tradicionales en instalaciones propias (_on-premises_). Estas ventajas impactan tanto a nivel **técnico** como **económico y organizativo**.

### **Cambiar sus gastos de capital por gastos variables**

En la informática tradicional, las empresas deben realizar **grandes inversiones iniciales** (_CapEx_) para comprar servidores, almacenamiento, licencias y equipamiento de red, independientemente de si se utilizan al máximo o no.

En la nube:

- Se pasa a un modelo de **gastos operativos** (_OpEx_).
- Se paga **solo por los recursos consumidos**.
- No es necesario invertir por adelantado en infraestructura.

📌 **Ventaja clave**: mayor flexibilidad financiera y menor riesgo, especialmente para proyectos nuevos o cargas de trabajo variables.

---
### **Economías de escala masivas**

Los proveedores de nube operan centros de datos a una escala global enorme:

- Compran hardware en grandes volúmenes.
- Optimizan energía, refrigeración y mantenimiento.
- Reparten costes entre millones de clientes.

Gracias a esto:

- Los costes unitarios son **mucho más bajos** que en un centro de datos propio.
- Los clientes se benefician indirectamente de estas economías de escala.

📌 **Resultado**: más potencia y servicios avanzados a menor coste.

---

### **Evitar asumir estimaciones sobre capacidad**

En entornos tradicionales, es necesario **predecir la demanda futura**:

- Si se compra de menos, el sistema se queda corto.
- Si se compra de más, se desperdicia dinero en recursos infrautilizados.

Con la nube:

- Los recursos se ajustan **en tiempo real**.
- Se puede escalar hacia arriba o hacia abajo según la necesidad.
- No es necesario planificar a largo plazo con estimaciones rígidas.

📌 **Beneficio**: se elimina la incertidumbre y el desperdicio de recursos.

---

### **Aumentar la velocidad y la agilidad**

En un entorno on-premises:

- Aprovisionar un servidor puede llevar semanas o meses.
- Requiere compras, instalaciones y configuraciones manuales.

En la nube:

- Los recursos se crean **en minutos o segundos**.
- Los equipos pueden experimentar, probar y desplegar rápidamente.
- Se acelera el desarrollo y la innovación.

📌 **Impacto organizativo**: los equipos de TI dejan de ser un cuello de botella y pasan a ser un facilitador del negocio.

---

### **Dejar de gastar dinero en la ejecución y el mantenimiento de centros de datos**

Gestionar un centro de datos propio implica:

- Costes de electricidad, refrigeración y espacio físico.
- Mantenimiento de hardware.
- Seguridad física.
- Personal especializado.

En la nube:

- El proveedor se encarga de toda la infraestructura física.
- La empresa se centra en **sus aplicaciones y datos**.

📌 **Ventaja estratégica**: menos carga operativa y más foco en actividades de valor para el negocio.

---

### **Adquirir escala mundial en cuestión de minutos**

Con infraestructura tradicional:

- Expandirse a otros países requiere grandes inversiones.
- Es necesario montar nuevos centros de datos o alquilar espacio.

Con la nube:

- Se pueden desplegar aplicaciones en **múltiples regiones del mundo**.
- La expansión global se realiza rápidamente.
- Se mejora la latencia y la experiencia del usuario final.

📌 **Clave**: capacidad de operar a nivel global sin infraestructura propia distribuida.

---

## **Sección 3: Introducción a Amazon Web Services (AWS)**

Esta sección presenta **Amazon Web Services (AWS)** como una plataforma de computación en la nube y explica cómo sus servicios se organizan, se combinan entre sí y permiten crear soluciones tecnológicas alineadas con objetivos empresariales.

---

### **¿Qué son los servicios web?**

Los **servicios web** son aplicaciones o funcionalidades accesibles a través de Internet mediante interfaces estandarizadas (APIs). Permiten que distintos sistemas se comuniquen entre sí sin importar el lenguaje de programación o el sistema operativo.

Características principales:

- Se accede a ellos a través de la red.
- Exponen funcionalidades específicas (almacenamiento, cálculo, autenticación, etc.).
- Se consumen bajo demanda.
- Se integran fácilmente con otros servicios.

📌 **Idea clave**: AWS ofrece sus capacidades de infraestructura y plataforma en forma de **servicios web**, accesibles mediante APIs.

---

### **¿Qué es AWS?**

**Amazon Web Services (AWS)** es una plataforma de servicios de computación en la nube ofrecida por Amazon. Proporciona una amplia variedad de servicios bajo demanda para:

- Computación
- Almacenamiento
- Bases de datos
- Redes
- Seguridad
- Analítica
- Inteligencia artificial
- Administración y costes

AWS permite a empresas y desarrolladores:

- Crear y desplegar aplicaciones sin gestionar infraestructura física.
- Escalar recursos de forma flexible.
- Pagar únicamente por el uso real.

📌 **Concepto clave**: AWS no es un único producto, sino un **ecosistema de servicios integrados**.

---

### **Categorías de los servicios de AWS**

Para facilitar su comprensión y uso, los servicios de AWS se agrupan en **categorías funcionales**, según el tipo de necesidad que cubren. Algunas de las principales son:

- **Computación**
- **Almacenamiento**
- **Bases de datos**
- **Redes y entrega de contenido**
- **Seguridad, identidad y cumplimiento**
- **Administración y gobernanza**
- **Costes y facturación**
- **Analítica, IA y Machine Learning** (entre otras)

Esta clasificación ayuda a identificar rápidamente qué servicios utilizar según el problema a resolver.

---

### **Elección de un servicio de computación en AWS**

AWS ofrece múltiples servicios de computación, cada uno diseñado para distintos casos de uso. Algunos ejemplos destacados:

#### **Amazon EC2**

- Servidores virtuales en la nube.
- Ofrece control total sobre el sistema operativo y la configuración.
- Adecuado para cargas tradicionales o personalizadas.

#### **AWS Lambda**

- Ejecución de código sin gestionar servidores.
- Basado en eventos.
- Ideal para arquitecturas _serverless_.

#### **AWS Elastic Beanstalk**

- Plataforma que simplifica el despliegue de aplicaciones.
- Gestiona automáticamente la infraestructura subyacente.
- Permite centrarse en el código.

#### **Amazon Lightsail**

- Solución simplificada para proyectos pequeños.
- Paquetes preconfigurados con coste predecible.
- Ideal para pruebas, webs sencillas o aprendizaje.

#### **Amazon EKS**

- Servicio gestionado de Kubernetes.
- Permite ejecutar contenedores a gran escala.
- Orientado a arquitecturas modernas basadas en microservicios.

📌 **Idea clave**: no existe “un único” servicio correcto; la elección depende del **nivel de control, complejidad y escalabilidad** necesarios.

---

### **Servicios que se tratan en este curso**

El curso se centra en las categorías fundamentales de AWS, esenciales para comprender y diseñar arquitecturas en la nube:

- **Computación**: ejecución de aplicaciones y servicios.
- **Seguridad, identidad y cumplimiento**: control de accesos y protección de recursos.
- **Bases de datos**: almacenamiento estructurado de datos.
- **Almacenamiento**: gestión de datos persistentes.
- **Administración y gobernanza**: monitorización, automatización y control.
- **Costes y facturación**: seguimiento y optimización del gasto.
- **Redes y entrega de contenido**: conectividad y distribución global.

Estas áreas forman la base de cualquier solución en AWS.

---

### **Tres formas de interactuar con AWS**

AWS ofrece distintas interfaces para gestionar y consumir sus servicios:

#### **Consola de administración de AWS**

- Interfaz web gráfica.
- Fácil de usar y visual.
- Ideal para aprendizaje, pruebas y gestión manual.

#### **AWS Command Line Interface (CLI)**

- Herramienta de línea de comandos.
- Permite automatizar tareas.
- Adecuada para usuarios técnicos y scripts.

#### **AWS SDK (Software Development Kit)**

- Bibliotecas para distintos lenguajes de programación.
- Permite integrar AWS directamente en aplicaciones.
- Usado por desarrolladores para automatizar y escalar soluciones.

📌 **Resumen**: todas las interfaces interactúan con AWS mediante APIs; solo cambia la forma de acceso.

---
## **Sección 4: AWS Cloud Adoption Framework (AWS CAF)**

Esta sección introduce el **AWS Cloud Adoption Framework (CAF)**, un marco de trabajo que ayuda a las organizaciones a **planificar, ejecutar y gobernar** su transición a la nube. El CAF identifica los **cambios organizativos, técnicos y operativos** necesarios para una adopción exitosa.

---

### **Marco de adopción de la nube de AWS (AWS CAF)**

El **AWS CAF** es un conjunto de **directrices, buenas prácticas y perspectivas** diseñado para:

- Reducir riesgos durante la migración a la nube.
- Alinear la tecnología con los objetivos del negocio.
- Facilitar la toma de decisiones estratégicas.
- Acelerar la adopción de la nube de forma estructurada.

El marco reconoce que migrar a la nube **no es solo un cambio tecnológico**, sino también un cambio cultural, organizativo y de procesos.

---
### **Seis perspectivas principales**

El AWS CAF se estructura en **seis perspectivas**, cada una centrada en un área clave de la organización. Estas perspectivas permiten evaluar el estado actual, identificar brechas y definir acciones necesarias para la adopción de la nube.

Las seis perspectivas son:

1. Negocios
2. Personal
3. Gobernanza
4. Plataforma
5. Seguridad
6. Operaciones

Cada perspectiva aborda un conjunto específico de responsabilidades y objetivos.

---
### **Perspectiva de negocios**

La **perspectiva de negocios** se centra en garantizar que la adopción de la nube:

- Apoye los objetivos estratégicos de la organización.
- Genere valor medible.
- Justifique la inversión realizada.

Incluye aspectos como:

- Modelos de negocio.
- Gestión financiera.
- Análisis de costes y beneficios.
- Indicadores de rendimiento (KPIs).

📌 **Objetivo principal**: asegurar que la nube impulse el crecimiento y la competitividad del negocio.

---
### **Perspectiva del personal**

La **perspectiva del personal** aborda el impacto de la nube en las personas y la organización interna.

Se centra en:

- Definición de nuevos roles y responsabilidades.
- Formación y desarrollo de competencias en la nube.
- Gestión del cambio cultural.
- Colaboración entre equipos.

📌 **Idea clave**: el éxito de la adopción cloud depende en gran medida de que el personal esté preparado y alineado con el cambio.

---
### **Perspectiva de la gobernanza**

La **perspectiva de gobernanza** se enfoca en establecer:

- Políticas claras.
- Procesos de control.
- Marcos de cumplimiento normativo.

Incluye:

- Gestión de riesgos.
- Cumplimiento legal y regulatorio.
- Control de costes.
- Definición de estándares y buenas prácticas.

📌 **Objetivo**: garantizar que el uso de la nube sea coherente, controlado y conforme a las normas de la organización y del sector.

---
### **Perspectiva de la plataforma**

La **perspectiva de la plataforma** cubre los aspectos técnicos relacionados con la infraestructura y los servicios de AWS.

Incluye:

- Diseño de arquitecturas cloud.
- Selección de servicios adecuados.
- Automatización y aprovisionamiento.
- Integración con sistemas existentes.

📌 **Enfoque principal**: construir una base tecnológica sólida, escalable y fiable sobre AWS.

---

### **Perspectiva de seguridad**

La **perspectiva de seguridad** garantiza que los datos y sistemas estén protegidos durante y después de la migración a la nube.

Abarca:

- Gestión de identidades y accesos.
- Protección de datos.
- Detección y respuesta ante incidentes.
- Cumplimiento de estándares de seguridad.

📌 **Concepto clave**: la seguridad en la nube es una **responsabilidad compartida** entre AWS y el cliente.

---

### **Perspectiva de las operaciones**

La **perspectiva de operaciones** se centra en la gestión diaria de los sistemas en la nube.

Incluye:

- Monitorización y alertas.
- Gestión de incidencias.
- Optimización del rendimiento.
- Automatización de operaciones.

📌 **Objetivo**: garantizar que los servicios funcionen de forma eficiente, estable y continua una vez desplegados en la nube.

---

## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Definir los diferentes tipos de modelos de informática en la nube
- Describir seis ventajas de la informática en la nube
- Reconocer los servicios fundamentales de AWS y sus categorías principales
- Examinar el Marco de adopción de la nube de AWS.

### Pregunta del examen de muestra

¿Por qué AWS es más económico que los centros de datos tradicionales para aplicaciones con diferentes cargas de trabajo de informática?