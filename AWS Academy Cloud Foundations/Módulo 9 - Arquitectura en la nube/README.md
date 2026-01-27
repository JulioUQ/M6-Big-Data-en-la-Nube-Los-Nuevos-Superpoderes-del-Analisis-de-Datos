## Módulo 9: Arquitectura en la nube

El propósito de este módulo es enseñar a **diseñar y crear arquitecturas en la nube siguiendo las mejores prácticas** de AWS.

## Sección 1: Marco de AWS Well-Architected

Esta sección introduce el **AWS Well-Architected Framework**, un conjunto de **principios, pilares y mejores prácticas** que ayudan a diseñar y evaluar arquitecturas en la nube que sean **seguras, eficientes, resilientes y rentables**.

El marco sirve como **referencia oficial de AWS** para tomar decisiones arquitectónicas correctas y detectar riesgos en sistemas existentes.

## Arquitectura: diseño y creación

En AWS, la **arquitectura** se refiere a la forma en la que los servicios se combinan para construir una solución.

### Diseño de arquitectura en la nube

Un buen diseño debe:

- Cumplir los requisitos funcionales.
- Adaptarse a cambios de demanda.
- Minimizar riesgos operativos.
- Optimizar costes.
- Garantizar seguridad y disponibilidad.

### Enfoque recomendado

AWS promueve un diseño:

- **Iterativo** (mejora continua).
- **Automatizado**.
- Basado en **servicios administrados**.
- Preparado para fallos.

## ¿Qué es el marco de buena arquitectura de AWS?

El **AWS Well-Architected Framework** es una guía que:

- Define **qué es una buena arquitectura** en la nube.
- Proporciona **preguntas clave** para evaluar sistemas.
- Ayuda a identificar **riesgos arquitectónicos**.
- Facilita decisiones técnicas alineadas con AWS.

No es un conjunto de reglas rígidas, sino un **marco flexible** que se adapta a distintos casos de uso.

## Objetivos del AWS Well-Architected Framework

- Diseñar sistemas **seguros y confiables**.
- Mejorar el rendimiento y la eficiencia.
- Reducir costes innecesarios.
- Facilitar la operación y el mantenimiento.
- Aumentar la resiliencia ante fallos.

## Pilares del marco de buena arquitectura de AWS

El marco se basa en **seis pilares fundamentales**:

1. **Excelencia Operacional**
2. **Seguridad**
3. **Fiabilidad (Reliability)**
4. **Eficiencia del rendimiento**
5. **Optimización de costes**
6. **Sostenibilidad**

Cada pilar aborda un conjunto específico de prácticas y decisiones arquitectónicas.

## Organización del pilar

Cada pilar del marco está organizado de forma similar.

### Estructura de un pilar

- **Principios de diseño**
- **Áreas clave**
- **Preguntas de evaluación**
- **Buenas prácticas**

Esta estructura permite:

- Evaluar arquitecturas existentes.
- Detectar riesgos.
- Priorizar mejoras.
- Evolucionar el sistema de forma controlada.

## Principios generales del marco

Aunque cada pilar tiene sus propios principios, existen ideas comunes:

- Automatizar siempre que sea posible.
- Diseñar para fallos.
- Escalar bajo demanda.
- Probar y mejorar continuamente.
- Usar servicios administrados.

## Herramienta AWS Well-Architected Tool

AWS proporciona una herramienta específica para aplicar este marco.

### AWS Well-Architected Tool

- Servicio gratuito dentro de AWS.
- Permite evaluar cargas de trabajo.
- Basado en cuestionarios por pilar.
- Identifica **riesgos altos y medios**.
- Genera recomendaciones prácticas.

### Casos de uso

- Revisión de arquitecturas existentes.
- Preparación para auditorías.
- Mejora continua de sistemas.
- Diseño de nuevas soluciones.

## Idea clave de la sección

> **El AWS Well-Architected Framework es la referencia fundamental para diseñar, evaluar y mejorar arquitecturas en la nube de forma estructurada y alineada con las mejores prácticas de AWS.**

---
## Sección 2: Excelencia operativa

### Pilar de Excelencia Operativa (AWS Well-Architected Framework)

Esta sección se centra en el **Pilar de Excelencia Operativa**, cuyo objetivo es **ejecutar y supervisar sistemas de forma eficaz**, mejorar procesos continuamente y **responder rápidamente ante incidentes**, manteniendo la **fiabilidad y disponibilidad** de las cargas de trabajo.
## Pilar de Excelencia Operativa

La **Excelencia Operativa** se refiere a la capacidad de:

- Ejecutar sistemas de forma consistente.
- Obtener información sobre su funcionamiento.
- Responder a eventos operativos.
- Mejorar procesos y procedimientos de manera continua.

Este pilar es clave para garantizar que los sistemas:

- Funcionen como se espera.
- Se recuperen rápidamente ante fallos.
- Evolucionen sin afectar al servicio.

## Relación entre fiabilidad y disponibilidad

Dentro de la excelencia operativa:

- **Fiabilidad**: capacidad del sistema para funcionar correctamente durante un periodo de tiempo.
- **Disponibilidad**: capacidad del sistema para estar accesible cuando se necesita.

Una buena excelencia operativa **mejora directamente** ambos aspectos.

## Principios de diseño para la excelencia operativa

AWS define varios principios que deben guiar el diseño de sistemas operativamente excelentes:

### 1. Realizar operaciones como código

- Automatizar tareas operativas
- Usar plantillas (CloudFormation, Terraform).
- Reducir errores humanos

### 2. Realizar cambios pequeños, frecuentes y reversibles

- Minimizar el impacto de fallos.
- Facilitar la detección de errores.
- Permitir retrocesos rápidos (_rollback_).

### 3. Refinar los procedimientos operativos con frecuencia

- Revisar procesos tras incidentes.
- Aprender de los fallos.
- Documentar mejoras.

### 4. Anticiparse a los fallos

- Probar escenarios de error.
- Simular fallos (game days).
- Preparar planes de respuesta.

### 5. Aprender de todos los fallos operativos

- Analizar causas raíz.
- Evitar culpas.
- Fomentar la mejora continua.

## Preguntas sobre la excelencia operativa

El marco Well-Architected propone **preguntas clave** para evaluar una arquitectura desde este pilar.

### Observabilidad

- ¿Cómo se supervisa la carga de trabajo?
- ¿Qué métricas, logs y alarmas existen?
- ¿Se detectan problemas antes de que afecten al usuario?

### Gestión de cambios

- ¿Cómo se implementan los cambios?
- ¿Existen mecanismos de rollback?
- ¿Se prueban los cambios antes de producción?

### Respuesta a eventos

- ¿Cómo se gestionan incidentes?
- ¿Hay procedimientos documentados?
- ¿Quién responde y cómo?

### Mejora continua

- ¿Se revisan los fallos ocurridos?
- ¿Se aplican las lecciones aprendidas?
- ¿Se actualizan procesos y herramientas?

## Servicios AWS relacionados con la excelencia operativa

Algunos servicios clave que apoyan este pilar:

- **Amazon CloudWatch**: métricas, logs y alarmas.
- **AWS CloudTrail**: auditoría de acciones.
- **AWS Systems Manager**: automatización y gestión.
- **AWS Config**: control de configuración.
- **AWS CloudFormation**: infraestructura como código.


## Idea clave de la sección

> **La excelencia operativa permite mantener sistemas fiables y disponibles mediante automatización, monitoreo continuo y mejora constante de los procesos.**

---
## Sesión 3: Seguridad

### Pilar de Seguridad (AWS Well-Architected Framework)

Esta sección se centra en el **pilar de Seguridad**, cuyo objetivo es **proteger la información, los sistemas y los activos**, utilizando prácticas de seguridad proactivas, controles de acceso adecuados y cumplimiento normativo. Garantiza que las soluciones en la nube sean **resilientes frente a amenazas y accesos no autorizados**.

## Principios de diseño para la seguridad

AWS define varios principios fundamentales que guían el diseño seguro de sistemas en la nube:

### 1. Implementar la defensa en profundidad

- Uso de **múltiples capas de seguridad** (red, infraestructura, datos y aplicaciones).
- Minimizar el impacto de fallos o ataques en una capa específica.

### 2. Aplicar controles de seguridad estrictos

- **Principio de menor privilegio**: dar solo los permisos necesarios.
- Políticas de acceso basadas en roles (IAM).
- Gestión de credenciales segura.

### 3. Automatizar la seguridad

- Usar herramientas de monitoreo y auditoría.
- Aplicar parches y actualizaciones automáticamente.
- Detectar anomalías mediante alertas automáticas.

### 4. Proteger los datos en reposo y en tránsito

- Cifrado de datos usando **AWS KMS**.
- Protocolos de comunicación seguros (TLS/HTTPS).
- Claves gestionadas centralmente.

### 5. Preparar detección y respuesta a incidentes

- Implementar **logs y auditoría continua**.
- Planes de respuesta ante incidentes.
- Capacitación de equipos y pruebas periódicas.

### 6. Evaluar y mejorar continuamente

- Revisar configuraciones de seguridad.
- Aplicar mejoras basadas en auditorías y nuevas amenazas.
- Integración de seguridad desde el diseño (_Security by Design_).

## Preguntas sobre la seguridad

Para evaluar una arquitectura desde el pilar de Seguridad, AWS propone preguntas clave:

### Gestión de identidad y acceso

- ¿Se aplican roles y políticas IAM según el principio de menor privilegio?
- ¿Se gestionan de forma segura las credenciales y claves de acceso?

### Protección de datos

- ¿Se cifran los datos en reposo y en tránsito?
- ¿Se gestionan correctamente las claves de cifrado?

### Detección de amenazas y monitoreo

- ¿Se registran eventos y accesos en CloudTrail y CloudWatch?
- ¿Existen alertas configuradas para actividades sospechosas?

### Resiliencia ante incidentes

- ¿Existen planes de respuesta y recuperación ante incidentes?
- ¿Se realizan pruebas periódicas de estos planes?

### Cumplimiento y auditoría

- ¿Se cumplen normas de seguridad y regulaciones aplicables?
- ¿Se revisan periódicamente las políticas y controles?

## Servicios AWS relacionados con seguridad

Algunos servicios clave que ayudan a implementar el pilar de seguridad:

- **AWS Identity and Access Management (IAM)**: control de usuarios y permisos.
- **AWS Key Management Service (KMS)**: gestión de claves de cifrado.
- **Amazon GuardDuty**: detección de amenazas.
- **AWS CloudTrail**: auditoría de acciones y eventos.
- **AWS Security Hub**: panel centralizado de seguridad y cumplimiento.
- **AWS Config**: auditoría y control de configuraciones de seguridad.

## Idea clave de la sección

> **El pilar de seguridad garantiza que las soluciones en la nube estén protegidas frente a amenazas, accesos no autorizados y fallos, mediante controles, cifrado, monitoreo y respuesta activa a incidentes.**

---

## Sección 4: Fiabilidad

### Pilar de Fiabilidad (Reliability)

El **pilar de fiabilidad** se centra en **diseñar sistemas que funcionen correctamente y se recuperen rápidamente ante fallos**, garantizando la **continuidad del negocio** y la disponibilidad del servicio ante cualquier incidente.

La fiabilidad no solo implica **evitar errores**, sino también **detectar, responder y recuperarse** de ellos de manera eficiente.

---

## Principios de diseño para la fiabilidad

AWS define varios principios clave para asegurar la fiabilidad de las arquitecturas en la nube:

### 1. Diseñar para fallos

- Asumir que los componentes pueden fallar.
    
- Distribuir los sistemas en **múltiples zonas de disponibilidad** (Multi-AZ).
    
- Implementar **recuperación automática (failover)**.
    

### 2. Automatizar la recuperación

- Usar **instancias redundantes** y escalado automático.
    
- Configurar **mecanismos de failover** y recuperación ante fallos de servicios.
    
- Minimizar la intervención manual.
    

### 3. Escalar horizontalmente

- Añadir más instancias o recursos en lugar de depender de un solo nodo.
    
- Permite soportar incrementos de tráfico sin degradar la disponibilidad.
    

### 4. Probar la resiliencia

- Realizar **simulaciones de fallos** (_chaos engineering_).
    
- Probar procedimientos de recuperación.
    
- Detectar puntos débiles antes de que afecten al usuario final.
    

### 5. Gestionar dependencias externas

- Evaluar la fiabilidad de servicios de terceros.
    
- Usar **tolerancia a fallos y redundancia** en integraciones externas.
    

### 6. Monitorear y responder a eventos

- Detectar errores o degradación del servicio con **CloudWatch, CloudTrail y X-Ray**.
    
- Configurar alertas y procedimientos de respuesta automáticos.
    
- Analizar incidentes para mejorar continuamente.
    

---

## Servicios AWS que apoyan la fiabilidad

- **Amazon Route 53**: balanceo de carga global y failover.
    
- **Amazon EC2 Auto Scaling**: escalado automático y recuperación de instancias.
    
- **Elastic Load Balancing (ELB)**: distribución de tráfico entre múltiples instancias.
    
- **Amazon S3 y EFS**: almacenamiento redundante y duradero.
    
- **Amazon RDS Multi-AZ**: bases de datos altamente disponibles.
    
- **AWS CloudWatch**: monitoreo y alertas automáticas.
    

---

## Idea clave de la sección

> **El pilar de fiabilidad garantiza que los sistemas sean capaces de operar correctamente, recuperarse de fallos y mantener la continuidad del negocio mediante redundancia, escalabilidad y monitoreo constante.**


--- 
## Sección 5: Eficiencia del rendimiento

### Pilar de Eficiencia del Rendimiento (Performance Efficiency)

El **pilar de eficacia del rendimiento** se centra en **usar los recursos de manera óptima para satisfacer las necesidades del sistema**, aprovechando la nube para **adaptar la capacidad y mejorar la eficiencia** de forma continua.

Su objetivo es mantener **alto rendimiento sin desperdicio de recursos**.

---

### Principios de diseño para la eficiencia del rendimiento

1. **Elegir la arquitectura correcta**
    
    - Seleccionar servicios y recursos que se adapten a la carga de trabajo.
        
    - Usar servicios administrados cuando sea posible.
        
2. **Escalar horizontal y verticalmente**
    
    - Escalado horizontal: añadir más instancias para distribuir carga.
        
    - Escalado vertical: aumentar recursos en instancias existentes.
        
3. **Automatizar la adaptación**
    
    - Ajustar recursos según la demanda con **Auto Scaling, Lambda o servicios serverless**.
        
    - Evitar sobredimensionar recursos de forma estática.
        
4. **Monitorizar y ajustar continuamente**
    
    - Medir métricas clave: latencia, throughput, uso de CPU/memoria.
        
    - Mejorar continuamente según patrones de uso.
        
5. **Elegir servicios innovadores**
    
    - Usar soluciones de nube específicas para mejorar rendimiento (por ejemplo, Aurora para bases de datos relacionales).
        

---

### Preguntas sobre la eficacia del rendimiento

Para evaluar este pilar, AWS propone preguntas como:

- ¿Se han elegido los recursos y servicios adecuados para la carga de trabajo?
    
- ¿Se monitoriza el rendimiento continuamente?
    
- ¿Se ajusta automáticamente la capacidad ante cambios de demanda?
    
- ¿Se usan tecnologías avanzadas para mejorar eficiencia y rendimiento?
    
- ¿Se prueban y optimizan periódicamente los diseños?
    

---

### Servicios AWS que apoyan la eficiencia del rendimiento

- **Amazon EC2 Auto Scaling**: escalar instancias según demanda.
    
- **AWS Lambda**: ejecución serverless bajo demanda.
    
- **Amazon Aurora Serverless**: escalado automático de bases de datos.
    
- **Amazon CloudWatch y X-Ray**: monitoreo de métricas y rendimiento.
    

---

### Idea clave de la sección

> **El pilar de eficiencia del rendimiento asegura que los sistemas utilicen los recursos de manera óptima, se adapten a la demanda y mantengan alto rendimiento en la nube.**

---

## Sección 6: Optimización de costes

### Pilar de Optimización de Costes (Cost Optimization)

Este pilar se centra en **maximizar el valor del gasto en la nube**, garantizando que los sistemas sean **rentables y escalables**, sin comprometer la seguridad ni el rendimiento.

Su objetivo es **gastar lo justo y eficiente**, aprovechando los modelos de pago por uso de AWS.

---

### Principios de diseño para la optimización de costes

1. **Pagar solo por lo que se usa**
    
    - Elegir servicios con facturación por consumo real.
        
    - Evitar recursos infrautilizados.
        
2. **Escalar según demanda**
    
    - Ajustar la capacidad automáticamente.
        
    - Evitar mantener recursos sobredimensionados.
        
3. **Elegir opciones de compra óptimas**
    
    - Instancias reservadas, Savings Plans o spot instances para ahorrar.
        
    - Evaluar costos frente a rendimiento.
        
4. **Optimizar almacenamiento y bases de datos**
    
    - Elegir clases de almacenamiento adecuadas (S3 Standard vs Glacier).
        
    - Monitorear IOPS y volumenes para no pagar de más.
        
5. **Medir, monitorear y mejorar**
    
    - Revisar continuamente los gastos.
        
    - Aplicar buenas prácticas y alertas de presupuesto.
        

---

### Preguntas sobre la optimización de costes

Algunas preguntas clave para evaluar este pilar:

- ¿Se utiliza un modelo de pago por uso o instancias reservadas adecuadas?
    
- ¿Se eliminan o apagan recursos innecesarios?
    
- ¿Se monitorizan y analizan los gastos regularmente?
    
- ¿Se optimizan el almacenamiento y los servicios según demanda?
    
- ¿Se implementan alertas y presupuestos para controlar los costes?
    

---

### Servicios AWS que apoyan la optimización de costes

- **AWS Cost Explorer**: analizar gasto y uso de recursos.
    
- **AWS Budgets**: establecer alertas de presupuesto.
    
- **AWS Trusted Advisor**: recomendaciones de ahorro de costos.
    
- **Instancias Spot y Reserved Instances**: reducir costes de computación.
    
- **S3 Glacier y clases de almacenamiento IA**: optimizar almacenamiento.
    

---

### Idea clave de la sección

> **El pilar de optimización de costes asegura que los sistemas sean eficientes económicamente, escalables y sostenibles, maximizando el valor de cada dólar invertido en la nube.**


--- 
## Sección 7: Fiabilidad y Disponibilidad

Esta sección profundiza en los conceptos de **fiabilidad** y **alta disponibilidad**, factores esenciales al diseñar sistemas que **resistan fallos, mantengan la continuidad del servicio y garanticen una experiencia consistente para los usuarios**.

---

## ¿Qué es la fiabilidad?

La **fiabilidad** se refiere a la capacidad de un sistema para **funcionar correctamente y sin interrupciones durante un periodo de tiempo determinado**.

- Un sistema fiable **cumple con su propósito incluso ante fallos menores**.
    
- Depende de la redundancia, recuperación ante errores y calidad de los componentes.
    

**Ejemplo:**

- Un servicio web que procesa transacciones correctamente aun si una instancia EC2 falla.
    

---

## ¿Qué es la disponibilidad?

La **disponibilidad** indica **el porcentaje de tiempo que un sistema está accesible y operativo para los usuarios**.

- Alta disponibilidad significa que el servicio está **funcional casi todo el tiempo**, minimizando interrupciones.
    
- Se suele medir en “nueves de disponibilidad”:
    
    - 99% → ~3,65 días/año de caída permitida
        
    - 99,9% → ~8,76 horas/año
        
    - 99,99% → ~52,6 minutos/año
        

---

## Comprensión de las métricas de fiabilidad

Las métricas clave incluyen:

1. **MTBF (Mean Time Between Failures)**
    
    - Tiempo medio entre fallos de un sistema.
        
    - Indica la **robustez de los componentes**.
        
2. **MTTR (Mean Time To Repair)**
    
    - Tiempo medio para **recuperar un sistema tras un fallo**.
        
    - Una menor MTTR aumenta la disponibilidad.
        
3. **Disponibilidad (%)**
    
    - Se calcula como:  
        [  
        Disponibilidad = \frac{MTBF}{MTBF + MTTR} \times 100  
        ]
        

---

## Alta disponibilidad

**Alta disponibilidad (HA)** consiste en diseñar sistemas que sigan funcionando **aunque fallen uno o varios componentes**.

### Estrategias de alta disponibilidad:

- **Redundancia**: duplicar instancias y recursos críticos.
    
- **Distribución geográfica**: usar múltiples zonas de disponibilidad (Multi-AZ).
    
- **Failover automático**: conmutación automática a recursos saludables.
    
- **Balanceo de carga**: distribuir tráfico entre instancias disponibles.
    

---

## Factores que influyen en la disponibilidad

1. **Diseño de arquitectura**
    
    - Multi-AZ y Multi-Region.
        
    - Balanceo de carga y escalado automático.
        
2. **Resiliencia del software**
    
    - Manejo de errores, retries y tolerancia a fallos.
        
3. **Capacidad de monitoreo y alertas**
    
    - Detectar y responder rápidamente a fallos.
        
4. **Mantenimiento y actualizaciones**
    
    - Parcheo planificado sin interrumpir servicio crítico.
        
5. **Dependencias externas**
    
    - Fiabilidad de servicios de terceros o APIs externas.
        

---

### Idea clave de la sección

> **Fiabilidad y disponibilidad aseguran que los sistemas permanezcan operativos y resistentes frente a fallos, mediante redundancia, monitoreo, recuperación rápida y diseño robusto.**

---
## Sección 8: AWS Trusted Advisor

### ¿Qué es AWS Trusted Advisor?

**AWS Trusted Advisor** es un **servicio de soporte y auditoría en la nube**, que analiza tu cuenta de AWS y proporciona **recomendaciones prácticas** para optimizar tus recursos, mejorar la seguridad y reducir costos.

- Evalúa **configuración y uso de servicios**.
    
- Identifica **riesgos y oportunidades de mejora**.
    
- Facilita decisiones alineadas con **las mejores prácticas de AWS**.
    

---

## Funcionalidades principales

AWS Trusted Advisor proporciona información en cinco áreas clave:

1. **Cost Optimization (Optimización de costos)**
    
    - Identifica recursos infrautilizados.
        
    - Sugiere instancias que podrían reservarse o apagarse.
        
    - Detecta almacenamiento que se puede mover a opciones más económicas.
        
2. **Performance (Rendimiento)**
    
    - Recomienda mejoras en instancias EC2 y otros servicios.
        
    - Señala cuellos de botella potenciales.
        
    - Sugerencias para optimizar bases de datos y recursos de red.
        
3. **Security (Seguridad)**
    
    - Detecta configuraciones inseguras de IAM, grupos de seguridad o S3.
        
    - Recomienda habilitar cifrado y autenticación.
        
    - Ayuda a cumplir buenas prácticas de seguridad.
        
4. **Fault Tolerance (Tolerancia a fallos / Fiabilidad)**
    
    - Señala recursos no redundantes.
        
    - Recomienda Multi-AZ o Multi-Region.
        
    - Detecta instancias sin copias de seguridad o snapshots.
        
5. **Service Limits (Límites de servicio)**
    
    - Muestra uso actual frente a límites de AWS.
        
    - Previene interrupciones por alcanzar cuotas de servicio.
        

---

## Tipos de recomendaciones

Trusted Advisor clasifica sus hallazgos según **prioridad y gravedad**:

1. **Alerta crítica**
    
    - Requiere atención inmediata.
        
    - Ej.: instancias sin parches, buckets públicos.
        
2. **Advertencia**
    
    - Mejora o riesgo moderado.
        
    - Ej.: instancias subutilizadas.
        
3. **Informativa / optimización**
    
    - Recomendaciones de eficiencia.
        
    - Ej.: mover almacenamiento a S3 Glacier.
        

Cada recomendación incluye:

- Descripción del problema.
    
- Impacto potencial.
    
- Pasos sugeridos para resolverlo.
    

---

## Beneficios de AWS Trusted Advisor

- **Reducción de costos:** identifica recursos infrautilizados o sobredimensionados.
    
- **Mejora de seguridad:** asegura configuraciones alineadas con buenas prácticas.
    
- **Mayor fiabilidad:** ayuda a detectar puntos únicos de fallo.
    
- **Optimización del rendimiento:** recomendaciones sobre instancias y recursos críticos.
    

---

## Idea clave de la sección

> **AWS Trusted Advisor proporciona recomendaciones prácticas para optimizar costos, rendimiento, seguridad y fiabilidad, ayudando a mantener arquitecturas alineadas con las mejores prácticas de AWS.**

---

## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Describir el marco de buena arquitectura de AWS, incluidos los 5 pilares.
- Identificar los principios del diseño del marco de buena arquitectura de AWS 
- Explicar la importancia de fiabilidad y la alta disponibilidad
- Identificar como AWS Trusted Advisor ayuda a los clientes 
- Interpretar las recomendaciones de AWS Trusted Advisor
### Pregunta del examen de muestra

Un ingeniero de SysOps que trabaja en una empresa quiere proteger sus datos en transito y en reposo. ¿Qué servicios podría utilizar para proteger los datos?
- Elastic Load Balancing | Amazon EBS | Amazon S3.