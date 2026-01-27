## Módulo 10: Escalado automático y supervisión

El objetivo de este módulo es presentar **tres servicios fundamentales de AWS** que permiten crear arquitecturas dinámicas y escalables.

---
## Sección 1: Elastic Load Balancing (ELB)

**Elastic Load Balancing (ELB)** es un servicio de AWS que **distribuye automáticamente el tráfico entrante** de tus aplicaciones entre múltiples destinos, como:

- Instancias **EC2**
    
- Contenedores **ECS/EKS**
    
- Direcciones IP
    
- Funciones **AWS Lambda**
    

Su objetivo es **aumentar la disponibilidad, escalabilidad y resiliencia** de las aplicaciones en la nube.

---

## Tipos de balanceadores de carga

AWS ofrece tres tipos principales de ELB, según las necesidades de la aplicación:

1. **Application Load Balancer (ALB)**
    
    - Opera a nivel de **capa 7 (HTTP/HTTPS)**.
        
    - Ideal para **aplicaciones web modernas y microservicios**.
        
    - Soporta **enrutamiento basado en rutas y host**.
        
2. **Network Load Balancer (NLB)**
    
    - Opera a nivel de **capa 4 (TCP/UDP)**.
        
    - Diseñado para **altas cargas, baja latencia y millones de solicitudes por segundo**.
        
    - Mantiene la **IP estática** para clientes.
        
3. **Gateway Load Balancer (GWLB)**
    
    - Diseñado para **dispositivos virtuales de red, firewalls y appliances de seguridad**.
        
    - Combina **balanceo y enrutamiento de tráfico**.
        

---

## Cómo funciona Elastic Load Balancing

1. ELB recibe **tráfico entrante** de usuarios o clientes.
    
2. Analiza la **salud y disponibilidad** de los destinos registrados (EC2, Lambda, IP).
    
3. Distribuye las solicitudes **de manera automática** según:
    
    - Algoritmo de balanceo (round robin, least connections, etc.)
        
    - Estado de las instancias
        
    - Reglas de enrutamiento (en ALB)
        
4. Reconfigura automáticamente el balanceo si **nuevas instancias se agregan o fallan**.
    

**Beneficio clave:** no necesitas gestionar manualmente el tráfico ni preocuparte por fallos de una sola instancia.

---

## Casos de uso de Elastic Load Balancing

- **Alta disponibilidad de aplicaciones web**
    
- **Microservicios y contenedores** (ECS/EKS)
    
- **Escalado automático** con Auto Scaling
    
- **Distribución de tráfico de API** y balanceo de carga global
    
- **Mejorar tolerancia a fallos** en múltiples AZ
    

---

## Monitoreo del balanceador de carga

AWS proporciona métricas y herramientas para monitorear ELB:

- **Amazon CloudWatch**
    
    - Métricas clave: RequestCount, Latency, HealthyHostCount, UnhealthyHostCount.
        
    - Alertas configurables para detectar problemas de tráfico o salud.
        
- **Access Logs**
    
    - Registros detallados de cada solicitud HTTP(S) atendida por el ELB.
        
- **AWS X-Ray**
    
    - Permite rastrear solicitudes y latencias a través de la aplicación.
        

**Beneficio:** visibilidad completa sobre el rendimiento y la disponibilidad de tus aplicaciones.

---

## Idea clave de la sección

> **Elastic Load Balancing distribuye el tráfico de forma automática entre múltiples destinos, aumentando la disponibilidad, escalabilidad y resiliencia de las aplicaciones en AWS, con monitoreo y ajuste continuo según la salud de los recursos.**

---
## Sección 2: Amazon CloudWatch

**Amazon CloudWatch** es un servicio de **monitorización y observabilidad** que proporciona métricas, logs y alarmas para **supervisar, analizar y optimizar** los recursos y aplicaciones que se ejecutan en AWS y on-premises.

Su objetivo es **proporcionar visibilidad completa del estado operativo**, permitiendo **detectar problemas, responder a cambios de rendimiento y mejorar la eficiencia**.

---

## Funcionalidades principales

1. **Supervisión de aplicaciones y recursos**
    
    - Monitorea instancias EC2, bases de datos RDS, contenedores ECS/EKS, funciones Lambda, ELB, S3, etc.
        
    - Recoge métricas como CPU, memoria, IOPS, latencia, uso de disco, entre otras.
        
2. **Responder a cambios de rendimiento**
    
    - Configura alarmas automáticas para reaccionar ante problemas.
        
    - Permite **automatizar acciones** mediante notificaciones (SNS) o escalado automático (Auto Scaling).
        
3. **Optimización de recursos**
    
    - Detecta infrautilización o sobrecarga de recursos.
        
    - Mejora eficiencia de costes y rendimiento.
        
4. **Visión unificada del estado operativo**
    
    - Consolida métricas, logs y trazas en **tableros personalizados**.
        
    - Permite análisis de tendencias y correlación de eventos.
        

---

## Alarmas de Amazon CloudWatch

Las **alarmas** permiten **monitorear métricas y ejecutar acciones automáticamente** cuando se cumplen ciertas condiciones.

### Componentes de una alarma

- **Métrica**: la medida que se monitorea (ej.: CPUUtilization).
    
- **Umbral (Threshold)**: valor crítico que activa la alarma.
    
- **Periodo**: intervalo de tiempo para evaluar la métrica.
    
- **Acción**: respuesta automática, como:
    
    - Notificación vía **SNS**
        
    - Escalado automático con **Auto Scaling**
        
    - Ejecución de funciones **Lambda**
        

### Tipos de alarmas

- **Estado OK**: métrica dentro del rango esperado.
    
- **Estado Alarm**: métrica fuera del umbral configurado.
    
- **Estado Insufficient Data**: no hay suficientes datos para evaluar.
    

---

## Servicios relacionados y complementarios

- **Amazon CloudWatch Logs**: almacena y analiza logs de aplicaciones y sistemas.
    
- **CloudWatch Dashboards**: visualización personalizada de métricas.
    
- **CloudWatch Events / EventBridge**: automatización y respuesta a eventos del sistema.
    
- **AWS X-Ray**: rastreo distribuido de solicitudes para detectar cuellos de botella.
    

---

## Beneficios de Amazon CloudWatch

- Detectar **problemas de rendimiento** antes de que afecten al usuario.
    
- Mejorar **resiliencia y fiabilidad** de la aplicación.
    
- Optimizar **costes y uso de recursos** mediante monitoreo continuo.
    
- Automatizar la **respuesta a incidentes**.
    

---

## Idea clave de la sección

> **Amazon CloudWatch proporciona métricas, logs y alarmas para monitorear, analizar y optimizar el rendimiento y la fiabilidad de aplicaciones y recursos en AWS, permitiendo respuestas automáticas ante problemas.**

    
---
## Sección 3: Amazon EC2 Auto Scaling

**Amazon EC2 Auto Scaling** es un servicio que **mantiene la disponibilidad y el rendimiento de las aplicaciones** al **ajustar automáticamente el número de instancias EC2** en función de la demanda o políticas definidas.

Su objetivo es **asegurar que siempre haya suficientes recursos para manejar la carga de trabajo**, evitando tanto la sobrecarga como el desperdicio de recursos.

---

## ¿Por qué es importante el escalado?

- Permite **adaptarse a la variabilidad de tráfico** sin intervención manual.
    
- Mejora la **disponibilidad**: asegura que las instancias suficientes estén siempre disponibles.
    
- Optimiza **costes**: se eliminan instancias innecesarias cuando baja la demanda.
    
- Permite **responder rápidamente** a picos de tráfico o fallos de instancias.
    

**Ejemplo práctico:** Amazon.com maneja millones de solicitudes por segundo y ajusta sus instancias automáticamente según la demanda de usuarios durante eventos de ventas masivas.

---

## Amazon EC2 Auto Scaling

Es una **herramienta que combina monitorización, reglas y grupos de instancias** para:

- Lanzar nuevas instancias EC2 cuando aumenta la demanda.
    
- Terminar instancias sobrantes cuando disminuye la carga.
    
- Mantener un **nivel de disponibilidad mínimo definido**.
    

---

## Tráfico que llega a Amazon.com

- Ejemplo real: el tráfico web puede variar **en segundos, minutos o días**.
    
- Auto Scaling permite **responder automáticamente** a estas fluctuaciones sin intervención humana.
    
- Garantiza que la **experiencia del usuario sea consistente**, incluso ante picos masivos de tráfico.
    

---

## Grupos de Auto Scaling

Un **grupo de Auto Scaling (ASG)** es la unidad central del escalado automático:

- Contiene **un conjunto de instancias EC2 idénticas**.
    
- Define **parámetros de escalado**: mínimo, máximo y deseado.
    
- Controla **la distribución de instancias** entre zonas de disponibilidad (AZ).
    
- Permite **políticas de escalado dinámico o programado**.
    

---

## Cómo funciona Amazon EC2 Auto Scaling

1. **Definir un grupo de Auto Scaling**
    
    - Seleccionar AMI, tipo de instancia, subredes y política de escalado.
        
2. **Monitorear métricas con CloudWatch**
    
    - Ej.: CPU, memoria, tráfico de red o métricas personalizadas.
        
3. **Aplicar políticas de escalado**
    
    - Escalado dinámico: aumenta/disminuye instancias según métricas en tiempo real.
        
    - Escalado programado: ajusta instancias según horarios predefinidos.
        
4. **Mantener la disponibilidad**
    
    - Si una instancia falla, se reemplaza automáticamente.
        
    - Se asegura que el grupo cumpla el tamaño deseado.
        

---

## Implementación del escalado dinámico

- **Políticas basadas en métricas**
    
    - Ej.: aumentar instancias si CPU > 70% durante 5 minutos.
        
- **Políticas de destino de utilización**
    
    - Mantiene un **valor objetivo**, como mantener CPU promedio al 50%.
        
- **Escalado predictivo**
    
    - Ajusta instancias anticipando patrones de tráfico (por ejemplo, horas punta).
        

---

## AWS Auto Scaling (servicio centralizado)

AWS ofrece **Auto Scaling no solo para EC2**, sino también para:

- **DynamoDB**: ajustar throughput.
    
- **Aurora / RDS**: escalar réplicas de lectura.
    
- **ECS/EKS**: escalar contenedores según demanda.
    
- **Application Auto Scaling**: servicio unificado para recursos múltiples.
    

**Beneficio:** permite **gestionar de forma centralizada múltiples tipos de escalado**, manteniendo consistencia y eficiencia en toda la arquitectura.

---

## Idea clave de la sección

> **Amazon EC2 Auto Scaling asegura que las aplicaciones tengan suficientes recursos para manejar la demanda, optimizando la disponibilidad y reduciendo costos mediante escalado automático basado en métricas y políticas predefinidas.**

---

