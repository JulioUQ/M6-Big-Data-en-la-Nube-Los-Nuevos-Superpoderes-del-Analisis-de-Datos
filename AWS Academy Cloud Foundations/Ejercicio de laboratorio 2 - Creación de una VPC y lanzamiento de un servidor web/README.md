# Laboratorio 2: Creación de una VPC y lanzamiento de un servidor web

## Información general y objetivos del laboratorio

En este laboratorio se utiliza **Amazon Virtual Private Cloud (VPC)** para crear una red virtual personalizada y añadir componentes adicionales. También se crea un **grupo de seguridad** y se configura una **instancia de Amazon EC2** para ejecutar un **servidor web**, que se lanza dentro de una subred de la VPC.

**Amazon VPC** permite iniciar recursos de AWS en una red virtual definida por el usuario, similar a una red tradicional en un centro de datos, pero con la ventaja de la infraestructura escalable de AWS. Una VPC puede abarcar múltiples **zonas de disponibilidad**.

### Al finalizar este laboratorio, será capaz de:

- Crear una VPC
    
- Crear subredes
    
- Configurar un grupo de seguridad
    
- Iniciar una instancia de EC2 dentro de una VPC
    

---

## Duración

⏱️ **Tiempo estimado:** 30 minutos

---

## Restricciones de los servicios de AWS

En este entorno de laboratorio, el acceso a los servicios de AWS puede estar restringido únicamente a aquellos necesarios para completar las tareas indicadas. Pueden aparecer errores si se intenta acceder a servicios o acciones no contemplados en el laboratorio.

---

## Situación

En este laboratorio se implementará la siguiente infraestructura:

- Una VPC personalizada
    
- Subredes públicas y privadas
    
- Puerta de enlace de Internet
    
- Puerta de enlace NAT
    
- Instancia EC2 con servidor web
    

_(Arquitectura proporcionada en el laboratorio)_

---

## Acceso a la Consola de administración de AWS

1. Seleccione **Start Lab (Iniciar laboratorio)** en la parte superior.
    
2. Espere a que el icono del círculo junto al enlace de AWS se muestre en **verde**.
    
3. Seleccione el enlace **AWS** en la esquina superior izquierda para abrir la consola.
    
4. Acepte ventanas emergentes si el navegador lo solicita.
    
5. Organice las pestañas para ver simultáneamente la consola y las instrucciones.
    

💡 **Sugerencia:** Puede extender la sesión seleccionando _Start Lab_ antes de que el temporizador llegue a 0:00.

---

## Obtención de créditos por su trabajo

Al finalizar el laboratorio deberá enviarlo para obtener una calificación basada en su progreso.

⚠️ **Importante:**  
Los nombres de recursos y configuraciones deben coincidir **exactamente** con los indicados (distingue mayúsculas y minúsculas).

---

# Tarea 1: Crear una VPC

En esta tarea se utiliza la opción **VPC and more (VPC y más)** para crear automáticamente:

- Una VPC
    
- Una puerta de enlace de Internet
    
- Una subred pública
    
- Una subred privada
    
- Dos tablas de enrutamiento
    
- Una puerta de enlace NAT
    

### Pasos

1. En **Servicios**, busque y seleccione **VPC**.
    
2. Verifique que la región sea **N. Virginia (us-east-1)**.
    
3. Seleccione **Panel de VPC** → **Crear VPC**.
    
    - Si no aparece, elija **Lanzar el asistente de VPC**.
        

### Configuración de la VPC

- **Opción:** VPC y más
    
- **Generación automática de etiquetas:**
    
    - Proyecto: `lab`
        
- **Bloque CIDR IPv4:** `10.0.0.0/16`
    
- **Zonas de disponibilidad:** 1
    
- **Subredes públicas:** 1
    
- **Subredes privadas:** 1
    

#### Personalizar bloques CIDR

- Subred pública (us-east-1a): `10.0.0.0/24`
    
- Subred privada (us-east-1a): `10.0.1.0/24`
    

#### Otras configuraciones

- **Puerta de enlace NAT:** En 1 AZ
    
- **Puntos de enlace de VPC:** Ninguno
    
- **DNS (hostnames y resolución):** Habilitados
    

### Vista previa esperada

- **VPC:** `lab-vpc`
    
- **Subredes:**
    
    - Pública: `lab-subnet-public1-us-east-1a`
        
    - Privada: `lab-subnet-private1-us-east-1a`
        
- **Tablas de enrutamiento:**
    
    - `lab-rtb-public`
        
    - `lab-rtb-private1-us-east-1a`
        
- **Conexiones:**
    
    - `lab-igw`
        
    - `lab-nat-public1-us-east-1a`
        

Seleccione **Crear VPC** y espere a que todos los recursos estén disponibles.

---

## Conceptos clave de la Tarea 1

- **Puerta de enlace de Internet (IGW):** Permite comunicación entre la VPC e Internet.
    
- **Subred pública:** Tiene una ruta `0.0.0.0/0` hacia la IGW.
    
- **Puerta de enlace NAT:** Permite a instancias en subredes privadas acceder a Internet sin ser accesibles desde él.
    
- **Subred privada:** No tiene acceso directo a Internet.
    

---

# Tarea 2: Crear subredes adicionales

Se crearán subredes en una **segunda zona de disponibilidad** para mejorar la **alta disponibilidad**.

## Crear segunda subred pública

- **VPC:** lab-vpc
    
- **Nombre:** `lab-subnet-public2`
    
- **Zona:** us-east-1b
    
- **CIDR:** `10.0.2.0/24`
    

## Crear segunda subred privada

- **VPC:** lab-vpc
    
- **Nombre:** `lab-subnet-private2`
    
- **Zona:** us-east-1b
    
- **CIDR:** `10.0.3.0/24`
    

---

## Configurar tablas de enrutamiento

### Subredes privadas

1. Seleccione `lab-rtb-private1-us-east-1a`
    
2. Verifique ruta:
    
    - `0.0.0.0/0` → `nat-xxxxxxxx`
        
3. En **Asociaciones de subredes**, asocie:
    
    - `lab-subnet-private1-us-east-1a`
        
    - `lab-subnet-private2`
        

### Subredes públicas

1. Seleccione `lab-rtb-public`
    
2. Verifique ruta:
    
    - `0.0.0.0/0` → `igw-xxxxxxxx`
        
3. Asocie:
    
    - `lab-subnet-public1-us-east-1a`
        
    - `lab-subnet-public2`
        

---

# Tarea 3: Crear un grupo de seguridad

Los **grupos de seguridad** actúan como firewalls virtuales.

### Configuración

- **Nombre:** Web Security Group
    
- **Descripción:** Enable HTTP access
    
- **VPC:** lab-vpc
    

### Regla de entrada

- **Tipo:** HTTP
    
- **Fuente:** Anywhere-IPv4
    
- **Descripción:** Permit web requests
    

Seleccione **Crear grupo de seguridad**.

---

# Tarea 4: Iniciar una instancia de servidor web

### Lanzar instancia EC2

1. Acceda a **EC2** → **Lanzar instancia**
    
2. **Nombre:** Web Server 1
    

### AMI

- Amazon Linux
    
- Amazon Linux 2023 AMI
    

### Tipo de instancia

- `t2.micro`
    

### Par de claves

- `vockey`
    

### Configuración de red

- **VPC:** lab-vpc
    
- **Subred:** `lab-subnet-public2`
    
- **IP pública:** Habilitar
    
- **Grupo de seguridad:** Web Security Group
    

### Almacenamiento

- Configuración predeterminada (8 GiB, gp3)
    

---

## Script de datos de usuario

```bash
#!/bin/bash
# Install Apache Web Server and PHP
dnf install -y httpd wget php mariadb105-server
# Download Lab files
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-ACCLFO-2/2-lab2-vpc/s3/lab-app.zip
unzip lab-app.zip -d /var/www/html/
# Turn on web server
chkconfig httpd on
service httpd start
```

Este script instala Apache, PHP y despliega una aplicación web automáticamente al iniciar la instancia.

---

## Verificación

1. Espere a que la instancia muestre **2/2 comprobaciones superadas**.
    
2. Copie el **DNS público (IPv4)**.
    
3. Ábralo en el navegador.
    

Deberá visualizar una página web con el logotipo de AWS y metadatos de la instancia.

---

# Envío del trabajo

1. Seleccione **Submit (Enviar)**.
2. Confirme con **Yes (Sí)**.
3. Consulte **Grades (Calificaciones)** y **Submission Report** si es necesario.
4. Puede reenviar el laboratorio tantas veces como desee.

---
