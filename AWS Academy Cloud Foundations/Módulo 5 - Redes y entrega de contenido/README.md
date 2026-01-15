
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


**Sección 5: Amazon Route 53**  
Cubre la **resolución de nombres de dominio (DNS)** y las capacidades de **Amazon Route 53**, incluyendo la conmutación por error de DNS y su relación con la **alta disponibilidad**, que se explorará en detalle en el Módulo 10.

**Sección 6: Amazon CloudFront**  
Analiza las funciones y beneficios de **Amazon CloudFront** como servicio de entrega de contenido (CDN) para mejorar la disponibilidad y velocidad de distribución de contenidos.