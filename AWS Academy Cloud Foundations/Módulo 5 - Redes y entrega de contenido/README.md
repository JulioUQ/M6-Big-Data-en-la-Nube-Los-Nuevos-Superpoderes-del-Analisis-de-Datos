
## Módulo 5: Redes y entrega de contenido

El propósito de este módulo es presentar los **fundamentos de los servicios de entrega de contenido y redes de AWS**, incluyendo **Amazon Virtual Private Cloud (VPC)**, **Amazon Route 53** y **Amazon CloudFront**. Los estudiantes tendrán la oportunidad de etiquetar diagramas de VPC, diseñar y crear su propia VPC, y entender cómo se integran estos servicios en la infraestructura de AWS.

---
## Sección 1: Conceptos básicos de redes

Esta sección introduce los **conceptos fundamentales de redes** que se utilizarán a lo largo del módulo. Comprender estos conceptos es esencial para diseñar, implementar y administrar redes en la nube de AWS.

---

### Red y subred

- Una **red** es un conjunto de dispositivos que pueden comunicarse entre sí.
- Una **subred** es una división lógica de una red más grande.
- Las subredes permiten:
    - Organizar mejor los recursos.
    - Aislar cargas de trabajo.
    - Mejorar la seguridad y el control del tráfico.

---
### Direcciones IPv4 e IPv6

- **IPv4**:
    - Utiliza direcciones de 32 bits.
    - Ejemplo: `192.168.1.1`.
    - Tiene un número limitado de direcciones disponibles.
        
- **IPv6**:
    - Utiliza direcciones de 128 bits.
    - Ejemplo: `2001:0db8:85a3::8a2e:0370:7334`.
    - Proporciona un espacio de direcciones mucho mayor y es compatible con redes modernas.

---
### Notación CIDR (Classless Inter-Domain Routing)

- CIDR define el **rango de direcciones IP** disponibles en una red o subred.
- Se expresa como una dirección IP seguida de una barra y un número.
- Ejemplo: `10.0.0.0/16`.
- Permite:
    - Asignar direcciones IP de forma eficiente.
    - Crear subredes de distintos tamaños.
---
### Modelo de interconexión de sistemas abiertos (OSI)

- El **modelo OSI** es un marco conceptual que describe cómo se transmiten los datos en una red.
- Está compuesto por **siete capas**, cada una con una función específica:
    1. Física
    2. Enlace de datos
    3. Red
    4. Transporte
    5. Sesión
    6. Presentación
    7. Aplicación

- Ayuda a:
    - Comprender cómo funcionan las comunicaciones de red.
    - Diagnosticar y resolver problemas de conectividad.

---
## Sección 2: Amazon Virtual Private Cloud (Amazon VPC)

Esta sección proporciona una **visión general de Amazon VPC**, el servicio de AWS que permite crear una red virtual aislada en la nube. Amazon VPC es la base para desplegar recursos como instancias EC2, bases de datos y servicios internos de forma segura y controlada.

---
### VPC y subredes

- Una **VPC** es una red virtual definida por el usuario dentro de AWS.
- Permite:
    - Controlar el rango de direcciones IP.
    - Definir subredes.
    - Configurar rutas y reglas de seguridad.
        
- Las **subredes**:
    - Son segmentos de una VPC.
    - Se asocian a una única zona de disponibilidad.
    - Pueden ser **públicas** o **privadas** según su configuración de enrutamiento.
---
### Direccionamiento IP

- Al crear una VPC se define un **bloque CIDR** (por ejemplo, `10.0.0.0/16`).
- Este bloque determina el rango total de direcciones IP disponibles.
- Las subredes utilizan subconjuntos del bloque CIDR de la VPC.

---
### Direcciones IP reservadas

- AWS **reserva automáticamente cinco direcciones IP** en cada subred:
    1. Dirección de red.
    2. Dirección del router de la VPC.
    3. Dirección del servidor DNS.
    4. Dirección reservada para uso futuro.
    5. Dirección de difusión (no utilizada, pero reservada).

- Estas direcciones no pueden asignarse a recursos.
---
### Tipos de direcciones IP públicas

- **IP pública**:
    - Se asigna automáticamente a una instancia.
    - Cambia al detener y reiniciar la instancia.

- **Elastic IP (EIP)**:
    - Dirección IP pública estática.
    - Permanece asociada a la cuenta hasta que se libera.
    - Útil para servicios que requieren una IP fija.
---
### Interfaz de red elástica (Elastic Network Interface – ENI)

- Una **ENI** es un componente virtual que permite la conectividad de red de una instancia.

- Incluye:
    - Direcciones IP privadas y públicas.
    - Grupos de seguridad.
    - Direcciones MAC.

- Permite:
    - Separar tráfico.
    - Reasignar interfaces entre instancias.

---
### Tablas de enrutamiento y rutas

- Las **tablas de enrutamiento** determinan cómo se dirige el tráfico dentro de la VPC.
- Cada subred debe estar asociada a una tabla de enrutamiento.
- Las **rutas** especifican:
    - El destino (por ejemplo, `0.0.0.0/0`).
    - El objetivo (Internet Gateway, NAT Gateway, VPC peering, etc.).

- La correcta configuración de rutas define si una subred es pública o privada.
---
## Sección 3: VPC Networking

Esta sección describe las **principales opciones de conectividad y comunicación de red dentro y fuera de una Amazon VPC**, permitiendo conectar recursos entre sí, con Internet y con infraestructuras locales de forma segura y escalable.

---
### Puerta de enlace de Internet (Internet Gateway)

- Una **Internet Gateway (IGW)** permite la comunicación entre recursos de una VPC y **Internet**.
- Es un componente **horizontalmente escalable y altamente disponible**.
- Para que una subred sea pública:
    - Debe tener una ruta hacia una IGW.
    - Las instancias deben tener una dirección IP pública o Elastic IP.
- Permite tráfico entrante y saliente según las reglas de seguridad.

---

### NAT Gateway (Network Address Translation)

- Un **NAT Gateway** permite que recursos en **subredes privadas** accedan a Internet **sin ser accesibles desde Internet**.
    
- Casos de uso comunes:
    - Actualizaciones del sistema.
    - Acceso a repositorios externos.

- Características:
    - Servicio administrado por AWS.
    - Alta disponibilidad dentro de una zona de disponibilidad.
    - Requiere una Elastic IP.

- Se ubica en una subred pública y se referencia desde subredes privadas mediante rutas.

---
### Puntos de enlace de la VPC (VPC Endpoints)

- Permiten conectarse a servicios de AWS **sin utilizar Internet**.
- El tráfico permanece dentro de la red de AWS.
- Tipos principales:
    - **Gateway Endpoint**: para Amazon S3 y DynamoDB.
    - **Interface Endpoint (AWS PrivateLink)**: para otros servicios de AWS y servicios de terceros.

- Mejoran la seguridad y reducen la latencia.
---
### Uso compartido de VPC e interconexión de VPC

- **VPC Peering**:
    - Conecta dos VPC para que se comuniquen entre sí.
    - Puede ser dentro de la misma región o entre regiones.
    - No admite tránsito (no hay enrutamiento en cadena).

- **VPC Sharing**:
    - Permite compartir subredes con otras cuentas de AWS mediante AWS Organizations.
    - Facilita la gestión centralizada de redes.

---
### Conectividad híbrida y de gran escala

#### AWS Site-to-Site VPN

- Conecta una VPC con una red local (on-premises) a través de Internet.
- Utiliza túneles IPsec cifrados.
- Ideal para implementaciones rápidas o de bajo coste.
#### AWS Direct Connect

- Proporciona una **conexión dedicada y privada** entre AWS y la infraestructura local.
    
- Ofrece:
    - Mayor ancho de banda.
    - Latencia consistente.
    - Mayor fiabilidad.

#### AWS Transit Gateway

- Actúa como un **hub central** para conectar:
    - Múltiples VPC.
    - Redes locales.
    - VPN y Direct Connect.

- Simplifica arquitecturas de red complejas y reduce la cantidad de conexiones punto a punto.

---
## Sección 4: Seguridad de VPC

Esta sección explica cómo proteger los recursos dentro de una Amazon VPC mediante **mecanismos de control de tráfico**, utilizando **grupos de seguridad** y **listas de control de acceso a la red (Network ACL)**.

---

### Grupos de seguridad (Security Groups)

- Los **grupos de seguridad** actúan como un **firewall virtual a nivel de instancia**.
- Controlan el tráfico:
    - **Entrante (inbound)**: qué tráfico puede llegar a la instancia.
    - **Saliente (outbound)**: qué tráfico puede salir de la instancia.

- Características clave:
    - Son **stateful** (con estado): si se permite una conexión entrante, la respuesta se permite automáticamente.
    - Solo contienen **reglas de permiso** (no hay reglas de denegación).
    - Se asocian a **interfaces de red elásticas (ENI)**.

- Buenas prácticas:
    - Aplicar el principio de **mínimo privilegio**.
    - Usar grupos de seguridad separados según el rol de la aplicación.

---

### Listas de control de acceso a la red (Network ACL)

- Las **ACL de red** actúan como un **firewall a nivel de subred**.
- Controlan el tráfico:
    - Entrante y saliente hacia y desde la subred.

- Características clave:
    - Son **stateless** (sin estado): se deben permitir explícitamente las respuestas.
    - Admiten **reglas de permiso y de denegación**.
    - Las reglas se evalúan en orden numérico (de menor a mayor).

- Cada subred debe estar asociada a una ACL de red (por defecto o personalizada).

---
### ACL de red

- AWS proporciona una **ACL de red predeterminada** que:
    - Permite todo el tráfico entrante y saliente.

- Las **ACL personalizadas**:
    - Inicialmente deniegan todo el tráfico.
    - Requieren reglas explícitas para permitir comunicaciones.

- Casos de uso comunes:
    - Bloquear rangos de direcciones IP específicas.
    - Añadir una capa adicional de seguridad a nivel de red.
---

### Comparación entre grupos de seguridad y ACL de red

|Característica|Grupos de seguridad|ACL de red|
|---|---|---|
|Nivel de aplicación|Instancia (ENI)|Subred|
|Estado|Stateful|Stateless|
|Reglas|Solo permitir|Permitir y denegar|
|Evaluación de reglas|Todas las reglas aplican|Ordenadas por número|
|Uso principal|Control detallado por recurso|Control general de red|

---

## Sección 5: Amazon Route 53

Esta sección cubre los conceptos de **resolución de nombres de dominio (DNS)** y explica cómo **Amazon Route 53** permite enrutar el tráfico de los usuarios de forma **altamente disponible, escalable y tolerante a fallos**, siendo una pieza clave en arquitecturas globales.

### Resolución de DNS con Amazon Route 53

- El **Sistema de Nombres de Dominio (DNS)** traduce nombres de dominio legibles (por ejemplo, `www.ejemplo.com`) en **direcciones IP**.
    
- Amazon Route 53 es un servicio de **DNS administrado**, diseñado para ofrecer:
    
    - Baja latencia
    - Alta disponibilidad
    - Escalabilidad automática

- Route 53 responde a las consultas DNS dirigiendo a los usuarios al recurso más adecuado.

### Amazon Route 53

- Es un servicio **altamente disponible y tolerante a fallos**.
    
- Se integra de forma nativa con otros servicios de AWS como:
    
    - Amazon EC2
    - Elastic Load Balancing
    - Amazon S3
    - AWS Global Accelerator

- Permite registrar dominios, gestionar zonas hospedadas y configurar políticas de enrutamiento avanzadas.

### Direccionamiento admitido por Amazon Route 53

Amazon Route 53 puede dirigir el tráfico DNS hacia distintos tipos de recursos, entre ellos:

- Instancias de **Amazon EC2**
- **Elastic Load Balancers**
- **Buckets de Amazon S3** configurados como sitios web
- **Direcciones IP** (IPv4 e IPv6)
- Recursos externos a AWS

### Caso de uso: Implementación en varias regiones

- Route 53 permite distribuir el tráfico entre **múltiples regiones de AWS**.

- Beneficios principales:
    - Mayor **disponibilidad**
    - Menor **latencia para los usuarios**
    - Resiliencia ante fallos regionales

- Se combina habitualmente con **Elastic Load Balancing** y **Auto Scaling**.

### Conmutación por error a nivel de DNS con Amazon Route 53

- Route 53 admite **políticas de enrutamiento con conmutación por error (failover)**.
- Funciona junto con **comprobaciones de estado (health checks)** para:
    - Detectar recursos no disponibles
    - Redirigir automáticamente el tráfico a un recurso de respaldo

- Esta conmutación ocurre a nivel de **DNS**, no a nivel de aplicación.

### Conmutación por error a nivel de DNS para una aplicación web de varias capas

- En una arquitectura de varias capas (web, aplicación y base de datos):
    - Route 53 dirige el tráfico a la capa web disponible.
    - Si la región principal falla, el tráfico se redirige a una región secundaria.

- Mejora la **continuidad del servicio** y la **experiencia del usuario**.

---
## Sección 6: Amazon CloudFront

Esta sección analiza **Amazon CloudFront**, el servicio de **red de entrega de contenido (CDN)** de AWS, y cómo ayuda a mejorar la **velocidad**, **disponibilidad** y **rendimiento** de aplicaciones y sitios web al distribuir el contenido a través de una red global.

### Entrega de contenido y latencia de red

- La **latencia de red** es el tiempo que tarda el contenido en viajar desde el servidor hasta el usuario final.

- Cuanto mayor es la distancia entre el usuario y el origen del contenido, mayor es la latencia.
- Amazon CloudFront reduce la latencia al:
    - Almacenar en caché copias del contenido en ubicaciones cercanas a los usuarios.
    - Entregar el contenido desde el **punto de presencia (Edge Location)** más próximo.

- Es especialmente útil para:
    - Sitios web
    - Contenido estático (imágenes, vídeos, archivos)
    - APIs y contenido dinámico

### Infraestructura de Amazon CloudFront

- CloudFront utiliza una **red global de puntos de presencia (Edge Locations)** distribuidos por todo el mundo.
- Estos puntos de presencia forman parte de la **infraestructura global de AWS**.
- Componentes clave de la infraestructura de CloudFront:
    - **Origen (Origin)**: recurso que almacena el contenido original (por ejemplo, Amazon S3, EC2, ELB).
    - **Distribución de CloudFront**: configuración que define cómo se entrega el contenido.
    - **Edge Locations**: ubicaciones que almacenan y sirven el contenido en caché.

- Beneficios principales:
    - Menor latencia
    - Mayor disponibilidad
    - Protección contra picos de tráfico
    - Integración con servicios de seguridad como **AWS Shield** y **AWS WAF**

---

## Conclusión del modulo

En resumen, en este modulo, aprendió a hacer lo siguiente:
- Reconocer los conceptos básicos de las redes.
- Describir las redes virtuales en la nube con Amazon VPC.
- Etiquetar un diagrama de red.
- Diseñar una arquitectura básica de VPC.
- Indicar los pasos para crear una VPC.
- Identificar los grupos de seguridad.
- Crear su propia VPC y agregarle componentes adicionales para generar una red personalizada.
- Identificar los aspectos fundamentales de Amazon Route 53.
- Reconocer los beneficios de Amazon CloudFront.
### Pregunta del examen de muestra

¿Qué servicio de redes AWS permite a una empresa crear una red virtual dentro de AWS?
- Amazon VPC.