# Laboratorio 5: Creación de un servidor de base de datos e interacción con la base de datos mediante una aplicación

## Información general y objetivos del laboratorio

Este laboratorio se ha diseñado para reforzar el concepto del uso de instancias de base de datos administradas por AWS con el objetivo de satisfacer las necesidades de las bases de datos relacionales.

_**Amazon Relational Database Service**_ (Amazon RDS) facilita la configuración, operación y escalado de una base de datos relacional en la nube. Proporciona una capacidad rentable y de tamaño ajustable y, al mismo tiempo, permite gestionar las tareas de administración de base de datos que consumen mucho tiempo, lo que permite centrarse en las aplicaciones y el negocio. Amazon RDS le ofrece seis motores de base de datos conocidos entre los que elegir: Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL y MariaDB.

Al final de este laboratorio, podrá hacer lo siguiente:

- Lanzar una instancia de base de datos de Amazon RDS con alta disponibilidad
- Configurar la instancia de base de datos para permitir conexiones desde su servidor web
- Abrir una aplicación web e interactuar con su base de datos

## Duración

El tiempo estimado para completar este laboratorio es de **30 minutos**.

## Restricciones de los servicios de AWS

En el entorno de este laboratorio, es posible que el acceso a los servicios de AWS y a sus respectivas acciones esté restringido a los servicios que son necesarios para completar las instrucciones del laboratorio. Puede que encuentre errores si intenta acceder a otros servicios o ejecutar acciones aparte de las que se detallan en este laboratorio.

## Situación

Cuando inicia el laboratorio, se proporciona la siguiente infraestructura:

![[Pasted image 20260127120801.png]]

Al final del laboratorio, tendrá la siguiente infraestructura:

![[Pasted image 20260127120816.png]]

## Acceso a la Consola de administración de AWS

1. En la parte superior de estas instrucciones, seleccione **Start Lab** (Iniciar laboratorio).
    
    - Comienza la sesión del laboratorio.
        
    - En la parte superior de esta página aparece un temporizador en el que se muestra el tiempo restante de la sesión.
        
        **Sugerencia:** Para actualizar la duración de la sesión en cualquier momento, elija **Start Lab** (Iniciar laboratorio) antes de que el temporizador llegue a 0:00.
        
    - Antes de continuar, espere a que el ícono del círculo situado a la derecha del enlace de AWS en la esquina superior izquierda aparezca en verde.
        

2. Para conectarse a la Consola de administración de AWS, elija el enlace de **AWS** en la esquina superior izquierda.
    
    - Se abre una nueva pestaña en el navegador y lo conecta a la consola.
        
        **Sugerencia:** Si no se abre una pestaña nueva del navegador, por lo general aparece un anuncio o un ícono en la parte superior de este, el cual indica que el navegador no permite que se abran ventanas emergentes en el sitio. Seleccione el anuncio o el ícono y, a continuación, elija **Permitir ventanas emergentes**.
        
3. Ubique la pestaña de la Consola de administración de AWS de modo que aparezca al lado de estas instrucciones. Idealmente, debería poder ver ambas pestañas del navegador a la vez para que sea más sencillo seguir los pasos del laboratorio.
    

## Obtención de créditos por su trabajo

Al final de este laboratorio, se le indicará que envíe el laboratorio para recibir una puntuación basada en su progreso.

**Sugerencia:** El script que verifica su trabajo solo puede otorgar puntos si nombra los recursos y ajusta las configuraciones como se especificó. En concreto, los valores en estas instrucciones que aparecen en `This Format` se deben ingresar exactamente como se documentó (distingue entre mayúsculas y minúsculas).

## Tarea 1: Crear un grupo de seguridad para la instancia de base de datos de RDS

En esta tarea, creará un grupo de seguridad para permitir que su servidor web acceda a la instancia de base de datos de RDS. El grupo de seguridad se utilizará al lanzar la instancia de base de datos.

4. En la Consola de administración de AWS, en el cuadro de búsqueda junto a Servicios , busque y seleccione **VPC**.
    
5. En el panel de navegación izquierdo, seleccione **Grupos de seguridad**.
    
6. Seleccione Crear grupo de seguridad y configure lo siguiente:
    
    - **Nombre del grupo de seguridad:** `DB Security Group`
        
    - **Descripción:** `Permit access from Web Security Group`
        
    - **VPC:** _Lab VPC_ (VPC de laboratorio)
        
        **Sugerencia**: Elija la X al lado de VPC que ya está seleccionada, luego, seleccione **Lab VPC** (VPC de laboratorio) en el menú.
        
    
7. En el panel **Reglas de entrada**, seleccione Agregar regla
    
    Actualmente, el grupo de seguridad no tiene reglas. Agregará una regla para permitir el acceso desde el _grupo de seguridad web_.
    
8. Configure los siguientes ajustes:
    
    - **Tipo:** _MySQL/Aurora (3306)_
    - **Fuente:** Coloque el cursor en el campo a la derecha de Personalizado, escriba `sg` y seleccione _Web Security Group_ (Grupo de seguridad web).
    
    Así se configura el grupo de seguridad de base de datos para permitir el ingreso del tráfico al puerto 3306 desde cualquier instancia de EC2 asociada con el _grupo de seguridad web_.
    
9. Elija Crear grupo de seguridad
    
    Utilizará este grupo de seguridad al iniciar la base de datos de Amazon RDS.
    

## Tarea 2: Crear un grupo de subredes de base de datos

Para esta tarea, creará un _Grupo de subredes de base de datos_ que se emplea para informar a RDS acerca de qué subredes se pueden utilizar para la base de datos. Cada grupo de subredes de base de datos requiere subredes en al menos dos zonas de disponibilidad.

10. En la Consola de administración de AWS, en el cuadro de búsqueda junto a Servicios , busque y seleccione **RDS**.
    
11. En el panel de navegación izquierdo, elija **Grupos de subredes**.
    
    Si el panel de navegación no se encuentra visible, elija el ícono de menú en la esquina superior izquierda.
    
12. Elija Crear grupo de subredes de base de datos y, a continuación, configure lo siguiente:
    
    - **Nombre:** `DB-Subnet-Group`
        
    - **Descripción:** `DB Subnet Group`
        
    - **VPC:** _Lab VPC_ (VPC de laboratorio)
        
13. Desplácese a la sección **Agregar subredes**.
    
14. Expanda la lista de valores en **Zonas de disponibilidad** y seleccione las primeras dos zonas: **us-east-1a** y **us-east-1b**.
    
15. Expanda la lista de valores en **Subredes** y seleccione las subredes asociadas con los rangos de CIDR **10.0.1.0/24** y **10.0.3.0/24**.
    
    Estas subredes deberían aparecer ahora en la tabla **Subredes seleccionadas**.
    
16. Elija Crear
    
    Utilizará este grupo de subredes de base de datos en la creación de la base de datos de la siguiente tarea.
    

## Tarea 3: Crear una instancia de base de datos de Amazon RDS

En esta tarea, deberá configurar y iniciar un despliegue Multi-AZ de Amazon RDS de una instancia de base de datos de MySQL.

Los despliegues _**Multi-AZ**_ de Amazon RDS proporcionan mejoras en la disponibilidad y durabilidad de las instancias de base de datos (DB), lo que las hace adecuadas para las cargas de trabajo de bases de datos de producción. Cuando aprovisiona una instancia de base de datos Multi-AZ, Amazon RDS crea automáticamente una instancia de base de datos primaria y, de forma sincronizada, replica los datos en una instancia en espera en una zona de disponibilidad (AZ) diferente.

17. En el panel de navegación izquierdo, seleccione **Bases de datos**.
    
18. Seleccione Crear base de datos
    
    Si ve el mensaje **Switch to the new database creation flow** (Cambiar al nuevo flujo de creación de base de datos) en la parte superior de la pantalla, selecciónelo.
    
19. Seleccione **MySQL** en **Opciones del motor**.
    
20. En **Plantillas**, elija **Desarrollo y pruebas**.
    
21. En **Disponibilidad y durabilidad**, elija **Instancia de base de datos Multi-AZ**.
    
22. En **Configuración**, configure lo siguiente:
    
    - **Identificador de instancia de base de datos:** `lab-db`
        
    - **Nombre de usuario maestro:** `main`
        
    - **Contraseña maestra:** `lab-password`
        
    - **Confirmar la contraseña:** `lab-password`
        
23. En **Clase de instancia de base de datos**, configure lo siguiente:
    
    - Seleccione **Clases con ráfagas (incluye clases t)**.
        
    - Seleccione _db.t3.micro_
        
24. En **Almacenamiento**, configure lo siguiente:
    
    - **Tipo de almacenamiento:** _Uso general (SSD)_
        
    - **Almacenamiento asignado:** _20_
        
25. En **Conectividad**, configure lo siguiente:
    
    - **Nube virtual privada (VPC):** _Lab VPC_ (VPC del laboratorio)
        
26. En **Grupos de seguridad de VPC existentes**, en la lista desplegable:
    
    - Seleccione _Grupo de seguridad de base de datos_.
        
    - Anule la selección de _default_ (predeterminado).
        
27. En Monitoreo, realice lo siguiente:
    
    - _Desmarque_ la opción **Habilitar el monitoreo mejorado**.
        
28. En parte inferior de la página, expanda **Configuración adicional**, luego, configure lo siguiente:
    
    - **Nombre de base de datos inicial:** `lab`
        
    - _Desmarque_ la opción **Habilitar copias de seguridad automáticas**.
        
        Esto desactivará los respaldos, lo que no suele recomendarse, pero permitirá una implementación más rápida de la base de datos para este laboratorio.
        
    - _Desmarque_ la opción **Habilitar el cifrado**
        
    
29. Seleccione Crear base de datos
    
    Ahora se iniciará la base de datos.
    
    Si recibe un error que indica “not authorized to perform: iam:CreateRole” (no tiene autorización para realizar la operación: iam:CreateRole), asegúrese de que desmarcó la opción _Habilitar el monitoreo mejorado_ en el paso anterior.
    
30. Seleccione **lab-db** (elija el enlace en sí).
    
    Deberá esperar **aproximadamente 4 minutos** para que la base de datos se encuentre disponible. El proceso de implementación implica la implementación de una base de datos en dos zonas de disponibilidad diferentes.
    
    Mientras espera, puede revisar las [preguntas frecuentes de Amazon RDS](https://aws.amazon.com/rds/faqs/) o tomar un café.
    
31. Espere hasta que **Información** cambie a **Modificando** o **Disponible**.
    
32. Desplácese hacia abajo hasta la sección **Conectividad y seguridad** y copie el campo **Punto de enlace**.
    
    Tendrá un aspecto similar a lo siguiente: _lab-db.xxxx.us-east-1.rds.amazonaws.com_.
    
33. Pegue el valor de Punto de enlace en un editor de texto. Lo utilizará luego en el laboratorio.
    
lab-db.cjayao1mwbkb.us-east-1.rds.amazonaws.com

## Tarea 4: Interactuar con la base de datos

En esta tarea, abrirá una aplicación web que se ejecuta en un servidor web creado por usted. La configurará para que use la base de datos que creó recién.

34. Para descubrir la dirección IP del **WebServer** (Servidor web), seleccione el menú desplegable Detalles de AWS, situado sobre estas instrucciones. Copie el valor de la dirección IP.
    
35. Abra una nueva pestaña del navegador web, pegue la dirección IP de _WebServer_ (Servidor web) y presione Intro.
    
    Se visualizará la aplicación web, que mostrará información acerca de la instancia de EC2.
    
36. Haga clic en el enlace de **RDS** situado en la parte superior de la página.
    
    Ahora, configurará la aplicación para que se conecte a la base de datos.
    
37. Configure los siguientes ajustes:
    
    - **Punto de enlace:** pegue el punto de enlace que copió anteriormente en un editor de texto
    - **Base de datos:** `lab`
    - **Nombre de usuario:** `main`
    - **Contraseña:** `lab-password`
    - Seleccione **Enviar**.
    
    Se visualizará un mensaje en el cual se explica que la aplicación está ejecutando un comando para copiar información en la base de datos. Después de algunos segundos, verá una **libreta de direcciones** en la aplicación.
    
    La aplicación de la libreta de direcciones utiliza la base de datos de RDS para almacenar información.
    
38. Agregue, edite y elimine contactos para probar la aplicación web.
    
    Los datos se conservan en la base de datos y se replican automáticamente en la segunda zona de disponibilidad.
    

## Envío del trabajo

39. Para registrar su progreso, seleccione **Submit** (Enviar) en la parte superior de estas instrucciones.
    
40. Cuando se le solicite, seleccione **Yes** (Sí).
    
    Después de un par de minutos, aparece el panel de calificaciones y le muestra cuántos puntos obtuvo por cada tarea. Si los resultados no se muestran después de algunos minutos, seleccione **Grades** (Calificaciones) en la parte superior de estas instrucciones.
    
    **Sugerencia:** Puede enviar su trabajo varias veces. Después de modificar el trabajo, vuelva a seleccionar **Submit** (Enviar). Su último envío quedó registrado para este laboratorio.
    
41. Para obtener comentarios detallados sobre su trabajo, seleccione **Submission Report** (Informe de envío).
    
    **Sugerencia:** En los casos de las comprobaciones por las que no recibió todos los puntos, a veces, se indican detalles útiles en el informe de envío.
    

## Laboratorio completado

¡Felicitaciones! Ha completado el laboratorio.

42. Seleccione End Lab (Finalizar laboratorio) en la parte superior de esta página y, a continuación, seleccione Yes (Sí) para confirmar que desea finalizar el laboratorio.
    
    Aparecerá un panel en el que se indica: “DELETE has been initiated... You may close this message box now” (Se ha iniciado la ELIMINACIÓN… Ya puede cerrar este cuadro de mensaje).
    
43. Seleccione la **X** en la esquina superior derecha para cerrar el panel.
    

_© 2023 Amazon Web Services, Inc. y sus filiales. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial._

---

### Atribuciones

**Bootstrap v3.3.5: [http://getbootstrap.com](https://getbootstrap.com/ "http://getbootstrap.com")/**

La licencia MIT (MIT)

Copyright (c) 2011-2016 Twitter, Inc.

Mediante este documento se concede permiso, de manera gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el “Software”) para utilizar el Software sin restricciones, incluidos, sin limitación, derechos de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar o vender copias del Software, y permitir que lo hagan las personas a las que se les proporcione el Software, sujeto a las siguientes condiciones:

El aviso de derechos de autor anterior y este aviso de permisos se deben incluir en todas las copias o partes importantes del Software.

EL SOFTWARE SE PROPORCIONA “TAL CUAL”, SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUIDAS, SIN LIMITACIÓN, LAS GARANTÍAS DE COMERCIABILIDAD, ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INCUMPLIMIENTO. EN NINGÚN CASO, LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE CUALQUIER RECLAMACIÓN, DAÑOS NI OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN CONTRACTUAL, EXTRACONTRACTUAL O DE OTRA ÍNDOLE, QUE SE DERIVE O RELACIONE CON EL SOFTWARE, SU UTILIZACIÓN U OTRAS OPERACIONES LLEVADAS A CABO CON ÉL.