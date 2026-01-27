# Laboratorio 3: Introducción a Amazon EC2

## Información general y objetivos del laboratorio

En este laboratorio, se proporciona información general básica sobre iniciar, modificar el tamaño, administrar y supervisar una instancia de Amazon EC2.

**Amazon Elastic Compute Cloud (Amazon EC2)** es un servicio web que proporciona capacidad de cómputo con tamaño modificable en la nube. Está diseñado con el fin de simplificar el uso del cómputo en la nube a escala web para los desarrolladores.

La sencilla interfaz de servicios web de Amazon EC2 permite obtener y configurar capacidad con una fricción mínima. Proporciona un control completo sobre los recursos informáticos y permite ejecutarse en el entorno informático acreditado de Amazon. Amazon EC2 reduce el tiempo necesario para obtener y arrancar nuevas instancias de servidor a solo minutos, lo que permite escalar rápidamente la capacidad, ya sea de forma ascendente o descendente, en función de sus necesidades.

Amazon EC2 cambia el modelo económico de la informática y permite pagar solo por la capacidad que utiliza realmente. Amazon EC2 proporciona a los desarrolladores las herramientas necesarias para crear aplicaciones resistentes a errores y para aislarse de los casos de error más comunes.

Después de completar este laboratorio, debería poder realizar lo siguiente:

- Iniciar un servidor web con protección de terminación habilitada.
    
- Supervisar la instancia de EC2.
    
- Modificar el grupo de seguridad que utiliza el servidor web para permitir el acceso con protocolo HTTP.
    
- Modificar el tamaño de la instancia de Amazon EC2 a la escala necesaria y habilitar la protección de detención.
    
- Explorar los límites de EC2.
    
- Probar la protección de detención.
    
- Detener la instancia de EC2.
    

## Duración

El tiempo estimado para completar este laboratorio es de **35 minutos**.

## Restricciones de los servicios de AWS

En el entorno de este laboratorio, es posible que el acceso a los servicios de AWS y a sus respectivas acciones esté restringido a los servicios que son necesarios para completar las instrucciones del laboratorio. Puede que encuentre errores si intenta acceder a otros servicios o ejecutar acciones aparte de las que se detallan en este laboratorio.

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

## Tarea 1: Lanzar una instancia de Amazon EC2

En esta tarea, lanzará una instancia de Amazon EC2 con _protección de terminación_ y _protección de detención_. La protección de terminación impide que termine la instancia de EC2 por accidente y la protección de detención impide que la detenga por accidente. También especificará un script de datos de usuario cuando lance la instancia que implementará un servidor web sencillo.

4. En la **Consola de administración de AWS**, seleccione **Servicios**, elija **Informática** y, luego, **EC2**.
    
    **Nota**: Verifique que la consola de EC2 está administrando recursos en la región **Norte de Virginia** (us-east-1). Puede comprobarlo en el menú desplegable de la parte superior de la pantalla, a la izquierda de su nombre de usuario. Si ya no aparece Norte de Virginia, elija la región Norte de Virginia en el menú de regiones antes de continuar con el siguiente paso.
    
5. Elija el menú desplegable de Lanzar instancia y seleccione **Lanzar instancia**.
    

### Paso 1: Nombre y etiquetas

6. Asigne a la instancia el nombre `Web Server`.
    
    El nombre que le de a esta instancia se guardará como una etiqueta. Las etiquetas le permiten clasificar los recursos de AWS de maneras diversas, por ejemplo, según la finalidad, el propietario o el entorno. Esto resulta útil cuando se tienen muchos recursos del mismo tipo: se puede identificar rápidamente un recurso específico con las etiquetas que le hayan asignado. Cada etiqueta consta de una clave y un valor, ambos definidos por el usuario. Si lo desea, puede definir varias etiquetas para asociarlas a la instancia.
    
    En este caso, la etiqueta que se creará constará de una _clave_ llamada `Name` con un _valor_ de `Web Server`
    

### Paso 2: Imágenes de aplicaciones y sistemas operativos (Imagen de máquina de Amazon)

7. En la lista de AMI de _Inicio rápido_ disponibles, mantenga seleccionado el valor predeterminado **Amazon Linux** de la AMI.
    
8. También mantenga seleccionado el valor predeterminado **Amazon Linux 2023 AMI**.
    
    Una **Imagen de máquina de Amazon (AMI)** proporciona la información necesaria para lanzar una instancia, que es un servidor virtual en la nube. La AMI incluye lo siguiente:
    
    - Una plantilla para el volumen raíz de la instancia (por ejemplo, un sistema operativo o un servidor de aplicaciones con aplicaciones)
        
    - Permisos de lanzamiento que controlan qué cuentas de AWS pueden utilizar la AMI para lanzar instancias
        
    - Una asignación de dispositivos de bloques que especifica los volúmenes que deben adjuntarse a la instancia (si hay) cuando se lanza.
        
    
    En la lista de **Inicio rápido**, se incluyen las AMI más utilizadas También puede crear su propia AMI o elegir una de AWS Marketplace, una tienda en línea donde se puede vender o comprar software que se ejecuta en AWS.
    

### Paso 3: Tipo de instancia

9. En el panel _Tipo de instancia_, deje seleccionado el valor predeterminado **t2.micro**.
    
    Amazon EC2 ofrece una amplia variedad de _tipos de instancias_ optimizados para adaptarse a diferentes casos prácticos. Los tipos de instancia abarcan diferentes combinaciones de capacidad de CPU, memoria, almacenamiento y redes y brindan flexibilidad a la hora de elegir la combinación de recursos adecuada para sus aplicaciones. Cada tipo de instancia incluye uno o varios _tamaños de instancia_, lo que permite escalar los recursos según los requisitos de la carga de trabajo de destino.
    
    Un tipo de instancia t2.micro tiene 1 CPU virtual y 1 GiB de memoria.
    
    **Nota**: Es posible que en este laboratorio no pueda utilizar otros tipos de instancia.
    

### Paso 4: Par de claves (inicio de sesión)

10. Para el **nombre del par de claves: _obligatorio_**, seleccione **vockey**.
    
    Amazon EC2 utiliza la criptografía de clave pública para cifrar y descifrar la información de inicio de sesión. Para asegurarse de que podrá iniciar sesión en el SO invitado de la instancia que creó, identifique un par de claves existente o cree un nuevo par de claves al lanzar la instancia. A continuación, Amazon EC2 instalará la clave en el sistema operativo invitado cuando se lance la instancia. De este modo, cuando intente conectarse a la instancia y proporcione la clave privada, podrá conectarse a la instancia.
    
    **Nota**: En este laboratorio no utilizará el par de claves que especificó para iniciar sesión en su instancia.
    

### Paso 5: Configuración de red

11. Junto a la configuración de red, seleccione **Editar**.
    
12. En **VPC**, seleccione **Lab VPC** (VPC de laboratorio).
    
    La VPC de laboratorio se creó con una plantilla de AWS CloudFormation durante el proceso de configuración del laboratorio. Esta VPC contiene dos subredes públicas en dos zonas de disponibilidad diferentes.
    
    **Nota**: Mantenga la subred predeterminada **PublicSubnet1**. Es la subred en la que se ejecutará la instancia. Observe también que, de forma predeterminada, a la instancia se le asignará una dirección IP pública.
    
13. En **Firewall (grupos de seguridad)**, seleccione **Crear grupo de seguridad** y configure:
    
    - **Nombre del grupo de seguridad:** `Web Server security group`
        
    - **Descripción:** `Security group for my web server`
        
        Un _grupo de seguridad_ funciona como un firewall virtual que controla el tráfico de una o más instancias. Cuando se inicia una instancia, se asocia uno o varios grupos de seguridad a ella. Se agregan _reglas_ a cada grupo de seguridad que permiten que el tráfico fluya a sus instancias asociadas o desde ellas. Las reglas de un grupo de seguridad se pueden modificar en cualquier momento; las nuevas reglas se aplican automáticamente a todas las instancias que estén asociadas al grupo de seguridad.
        
    - En **Reglas de entrada de los grupos de seguridad**, observe que existe una regla. **Elimine** esta regla.
        

### Paso 6: Configurar almacenamiento

14. En la sección _Configurar almacenamiento_, mantenga la configuración predeterminada.
    
    Amazon EC2 almacena datos en un disco virtual asociado a la red que se denomina _Elastic Block Store_.
    
    Se iniciará la instancia de Amazon EC2 con un volumen de disco predeterminado de 8 GiB. Este será el volumen raíz (también conocido como volumen “de arranque”).
    

### Paso 7: Detalles avanzados

15. Expanda **Detalles avanzados**.
    
16. En **Protección de terminación**, seleccione **Habilitar**.
    
    Cuando una instancia de Amazon EC2 ya no es necesaria, se puede _terminar_, lo que significa que se borra y se liberan sus recursos. No se puede volver a acceder a una instancia terminada y no se pueden recuperar los datos que contenía. Si quiere evitar que la instancia se termine por accidente, puede habilitar la _protección de terminación_ para la instancia, lo que impide que se finalice mientras este ajuste permanezca activado.
    
17. Desplácese hasta el final de la página y copie y pegue el código que se muestra a continuación en el cuadro **Datos de usuario**:
    
    #!/bin/bash
    
    dnf install -y httpd
    
    systemctl enable httpd
    
    systemctl start httpd
    
    echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
    
    Cuando se inicia una instancia, puede transmitirle los _datos de usuario_ a la instancia y utilizarlos para realizar tareas automatizadas de instalación y configuración después de que se inicie la instancia.
    
    La instancia ejecuta Amazon Linux 2023. El _script de shell_ que especificó se ejecutará como usuario _raíz_ del SO invitado cuando se inicie la instancia. Este script hará lo siguiente:
    
    - Instalar un servidor web Apache (httpd)
        
    - Configurar el servidor web para que se inicie de forma automática durante el arranque
        
    - Ejecutar el servidor web una vez que haya terminado de instalarse
        
    - Crear una página web sencilla
        

### Paso 8: Lanzar la instancia

18. En la parte inferior del panel **Resumen** elija Lanzar instancia
    
    Verá un mensaje de resultado correcto.
    

19. Elija Ver todas las instancias
    
    - En la sección Instancias, seleccione **Servidor web**.
        
    - Revise la información que se muestra en la pestaña **Detalles**. Allí figura información sobre el tipo de instancia y la configuración de seguridad y de red.
        
        La instancia tiene asignado un _DNS IPv4 público_ que puede utilizar para contactar con ella desde Internet.
        
        Para ver más información, arrastre hacia arriba el divisor de la ventana.
        
        Al principio, la instancia aparecerá con estado _Pendiente_, lo que indica que se está lanzando. A continuación, cambiará a _Inicializando_ y, por último, a _En ejecución_.
        
    
20. Espere a que aparezca lo siguiente en la instancia:
    
    - **Estado de instancia:** _En ejecución_
        
    - **Comprobaciones de estado:** _2/2 comprobaciones superadas_
        

**¡Felicitaciones!** Ha lanzado de manera correcta la primera instancia de Amazon EC2.

## Tarea 2: Supervisar la instancia

La supervisión es un factor importante a la hora de mantener el rendimiento, la disponibilidad y la fiabilidad de las instancias de Amazon Elastic Compute Cloud (Amazon EC2) y las soluciones de AWS.

21. Seleccione la pestaña **Comprobaciones de estado**.
    
    Con la supervisión del estado de las instancias, puede determinar de forma rápida si Amazon EC2 ha detectado algún problema que pudiera impedir que las instancias ejecuten aplicaciones. Amazon EC2 realiza comprobaciones automatizadas en cada instancia de EC2 en ejecución para identificar problemas de hardware y software.
    
    Observe que se superaron las comprobaciones de **Accesibilidad del sistema** y la de **Accesibilidad de la instancia**.
    
22. Seleccione la pestaña **Supervisión**.
    
    En esta pestaña, se muestran las métricas de Amazon CloudWatch de la instancia. En este momento, no aparecen muchas métricas debido a que la instancia se acaba de iniciar.
    
    Puede elegir el ícono de los tres puntos en cualquier gráfico y seleccionar **Ampliar** para ver la métrica elegida desplegada.
    
    Amazon EC2 envía métricas sobre las instancias de EC2 a Amazon CloudWatch. La supervisión básica (cinco minutos) se encuentra habilitada de forma predeterminada. También se puede habilitar la supervisión detallada (un minuto).
    
23. En el menú Acciones  que se encuentra en la parte superior de la consola, seleccione **Monitoreo y solución de problemas** **Obtener registro del sistema**.
    
    En Registro del sistema, se muestra el resultado de la consola de la instancia, que es una herramienta valiosa para el diagnóstico de problemas. Resulta especialmente útil para solucionar problemas de kernel y de configuración de servicios que podrían causar la terminación de una instancia o hacer que esta se torne inaccesible antes de poder iniciar el daemon de SSH. Si no ve ningún registro del sistema, espere unos minutos e inténtelo de nuevo.
    
24. Desplácese por el resultado. Observe que se instaló el paquete HTTP a partir de los **datos de usuario** que agregó al crear la instancia.
    
    ![Resultados de la consola](https://labs.vocareum.com/web/4721338/4945483.0/ASNLIB/public/docs/lang/es-la/images/Console-output.png)
    
25. Seleccione **Cancelar**.
    
26. Asegúrese de que el **Servidor web** siga seleccionado. A continuación, en el menú Acciones , seleccione **Monitoreo y solución de problemas** **Obtener captura de pantalla de la instancia**.
    
    Así se vería la consola de la instancia de Amazon EC2 si estuviera asociada a una pantalla.
    
    ![Captura de pantalla](https://labs.vocareum.com/web/4721338/4945483.0/ASNLIB/public/docs/lang/es-la/images/Screen-shot.png)
    
    Si no puede acceder a la instancia a través de SSH o RDP, puede hacer una captura de pantalla de la instancia y verla como una imagen. Esto permite ver el estado de la instancia y solucionar los problemas más rápidamente.
    
27. Seleccione **Cancelar**.
    
    **¡Felicitaciones!** Ha explorado varias formas de supervisar una instancia.
    

## Tarea 3: Actualizar el grupo de seguridad y acceder al servidor web

Cuando lanzó la instancia de EC2, proporcionó un script que instaló un servidor web y creó una página web sencilla. En esta tarea, accederá al contenido del servidor web.

28. Asegúrese de que el **Servidor web** siga seleccionado. Elija la pestaña **Detalles**.
    
29. Copie la **Dirección IPv4 pública** de la instancia en el portapapeles.
    
30. Abra una nueva pestaña del navegador web, pegue la dirección IP que acaba de copiar y presione **Intro**.
    
    **Pregunta:** ¿Puede acceder al servidor web? ¿Por qué no?
    
    En este momento, **no** puede acceder al servidor web porque el _grupo de seguridad_ no permite tráfico entrante en el puerto 80, que se usa para solicitudes web HTTP. Esto es un ejemplo del uso de un grupo de seguridad como firewall para restringir el tráfico de red entrante y saliente que se permite en una instancia.
    
    A fin de corregir esto, ahora debe actualizar el grupo de seguridad para permitir el tráfico web en el puerto 80.
    
31. Deje abierta la pestaña del navegador y vuelva a la pestaña **Consola de EC2**.
    
32. En el panel de navegación izquierdo, seleccione **Grupos de seguridad**.
    
33. Seleccione **Grupo de seguridad del servidor web**.
    
34. Elija la pestaña **Reglas de entrada**.
    
    Actualmente, el grupo de seguridad no tiene reglas de entrada.
    
35. Seleccione Editar reglas de entrada, seleccione Agregar regla y, a continuación, configure lo siguiente:
    
    - **Tipo:** _HTTP_
        
    - **Fuente:** _Anywhere-IPv4_
        
    - Elija Guardar reglas
        
36. Regrese a la pestaña del servidor web que abrió antes y actualice la página.
    
    Debería ver este mensaje: _Hello From Your Web Server!_ (¡Hola desde tu servidor web!).
    
    **¡Felicitaciones!** Ha modificado de manera correcta el grupo de seguridad para permitir el tráfico HTTP en la instancia de Amazon EC2.
    

## Tarea 4: Modificar el tamaño de la instancia, tipo de instancia y volumen de EBS

A medida que cambien sus necesidades, podría descubrir que su instancia se encuentra sobreutilizada (es demasiado pequeña) o infrautilizada (es demasiado grande). En ese caso, puede cambiar el _tipo de instancia_. Por ejemplo, si una instancia _t2.micro_ es demasiado pequeña para la carga de trabajo, puede cambiarla a una instancia _m5.medium_. Del mismo modo, puede cambiar el tamaño de un disco.

### Detener la instancia

Para poder cambiar el tamaño de una instancia, antes debe _detenerla_.

Cuando se detiene una instancia, se apaga. Una instancia de EC2 detenida no genera cargos de tiempo de ejecución, pero sí se mantienen los cargos de almacenamiento por los volúmenes de Amazon EBS que están asociados a ella.

37. En la **Consola de administración de EC2**, en el panel de navegación izquierdo, seleccione **Instancias** y, luego, elija la instancia del **Servidor web**.
    
38. En el menú Estado de la instancia , elija **Detener instancia**.
    
39. Elija Detener.
    
    La instancia se apagará de forma normal y, a continuación, dejará de ejecutarse.
    
40. Espere hasta que el **Estado de la instancia** muestre: _Detenida_.
    

### Cambiar el tipo de instancia y habilitar la protección de detención

41. Seleccione la instancia del servidor web, luego, en el menú Acciones , elija **Configuración de la instancia** **Cambiar tipo de instancia**, luego, configure lo siguiente:
    
    - **Tipo de instancia:** _t2.small_
        
    - Seleccione Aplicar
        
        Cuando la instancia se inicie de nuevo, se ejecutará como una instancia _t2.small_, que tiene el doble de memoria que una instancia _t2.micro_. **NOTA**: Es posible que en este laboratorio no pueda utilizar otros tipos de instancia.
        
    
42. Seleccione la instancia del servidor web, luego, en el menú Acciones , elija **Configuración de la instancia** **Cambiar la protección de detención**. Seleccione **Habilitar** y, luego, Guardar para guardar el cambio.
    
    Cuando detiene una instancia, esta se apaga. Cuando inicie la instancia posteriormente, normalmente se migra a un nuevo equipo host y se le asigna una nueva dirección IPv4 _pública_. Una instancia retiene su dirección IPv4 _privada_. Cuando se detiene una instancia, no se elimina. Se retienen los volúmenes de EBS y los datos en esos volúmenes.
    

### Modificar el tamaño del volumen de EBS

43. Con la instancia del servidor web aún seleccionada, elija la pestaña **Almacenamiento**, seleccione el nombre del ID de volumen y, a continuación, marque la casilla que aparece junto al volumen.
    
44. En el menú Acciones , seleccione **Modificar volumen**.
    
    El tamaño actual del volumen de disco es de 8 GiB. A continuación, aumentará el tamaño del disco.
    
45. Cambie el tamaño a: `10` **NOTA**: Es posible que en este laboratorio no pueda crear volúmenes de Amazon EBS mayores que 10 GB.
    
46. Seleccione Modificar.
    
47. Seleccione Modificar nuevamente para confirmar y aumentar el tamaño del volumen.
    

### Iniciar la instancia con tamaño modificado

A continuación, inicie nuevamente la instancia, pero ahora con más memoria y más espacio en el disco.

48. En el panel de navegación izquierdo, elija **Instancias**.
    
49. Seleccione la instancia **Servidor web**.
    
50. En el menú Estado de la instancia , seleccione **Iniciar instancia**.
    
    **¡Felicitaciones!** Ha modificado el tamaño de la instancia de Amazon EC2 de manera correcta. En esta tarea, cambió el tipo de instancia de _t2.micro_ a _t2.small_. También modificó el volumen del disco raíz de 8 GiB a 10 GiB.
    

## Tarea 5: Explorar los límites de EC2

Amazon EC2 permite utilizar diferentes recursos. Entre estos recursos, se incluyen imágenes, instancias, volúmenes e instantáneas. Cuando se crea una cuenta en AWS, estos recursos tienen límites predeterminados que dependen de la región.

51. En la Consola de administración de AWS, en el cuadro de búsqueda junto a **Servicios**, busque y seleccione `Service Quotas`.
    
52. Seleccione **Servicios de AWS** en el menú de navegación y, a continuación, en la barra de búsqueda _Buscar servicios_, busque `ec2` y seleccione **Amazon Elastic Compute Cloud (Amazon EC2)**.
    
53. En la barra de búsqueda _Buscar cuotas_, busque `running on-demand`, pero no seleccione nada. En cambio, observe la lista filtrada de cuotas de servicio que coinciden con los criterios.
    
    Tenga en cuenta que hay límites en el número y tipos de instancias que pueden ejecutarse en una región. Por ejemplo, hay un límite para la cantidad de instancias de _Running On-Demand Standard..._ (Ejecutar las instancias estándar bajo demanda) que puede iniciar en esta región. Al lanzar instancias, la solicitud no debe hacer que el uso supere el límite de instancias definidas actualmente para esa región.
    
    Si es propietario de una cuenta de AWS, puede solicitar un aumento para muchos de estos límites.
    

## Tarea 6: Probar la protección de detención

Puede detener la instancia cuando no necesite acceso, pero todavía desee retenerla. En esta tarea, aprenderá a utilizar la _protección de detención_.

54. En la Consola de administración de AWS, en el cuadro de búsqueda junto a **Servicios**, busque y seleccione `EC2` para volver a la consola de EC2.
    
55. En el panel de navegación izquierdo, elija **Instancias**.
    
56. Seleccione la instancia del **servidor web** y en el menú Estado de la instancia , seleccione **Detener instancia**.
    
57. Seleccione Detener
    
    Tenga en cuenta que hay un mensaje que dice: _Failed to stop the instance i-1234567xxx. The instance 'i-1234567xxx' may not be stopped. Modify its 'disableApiTermination' instance attribute and try again._ (Error al detener la instancia i-1234567xxx. No se puede detener la instancia “i-1234567xxx”. Modifique el atributo de instancia 'disableApiStop' e inténtelo de nuevo).
    
    Esto demuestra que la protección de detención que habilitó anteriormente en este laboratorio ahora ofrece una protección que previene la detención accidental de una instancia. Si realmente quiere terminar la instancia, deberá desactivar la protección de detención.
    
58. En el menú Acciones , seleccione **Configuración de la instancia** **Cambiar protección de detención**.
    
59. Desmarque la casilla **Habilitar**.
    
60. Elija Guardar
    
    Ahora puede detener la instancia.
    
61. Vuelva a seleccionar la instancia del **servidor web** y en el menú Estado de la instancia , seleccione **Detener instancia**.
    
62. Elija Detener.
    
    **¡Felicitaciones!** Ha probado la protección de detención y ha detenido la instancia de manera correcta.
    

## Envío del trabajo

63. Para registrar su progreso, seleccione **Submit** (Enviar) en la parte superior de estas instrucciones.
    

64. Cuando se le solicite, seleccione **Yes** (Sí).
    
    Después de un par de minutos, aparece el panel de calificaciones y le muestra cuántos puntos obtuvo por cada tarea. Si los resultados no se muestran después de algunos minutos, seleccione **Grades** (Calificaciones) en la parte superior de estas instrucciones.
    
    **Importante:** Algunas de las comprobaciones realizadas por el proceso de envío en este laboratorio solo le otorgarán créditos si han transcurrido 5 minutos cómo mínimo desde que completó la acción. Si no recibe los créditos la primera vez que hace el envío, puede que deba esperar un par de minutos y enviar nuevamente para recibir los créditos por estos elementos.
    
    **Sugerencia:** Puede enviar su trabajo varias veces. Después de modificar el trabajo, vuelva a seleccionar **Submit** (Enviar). Su último envío quedó registrado para este laboratorio.
    
65. Para obtener comentarios detallados sobre su trabajo, seleccione **Submission Report** (Informe de envío).
    
    **Sugerencia:** En los casos de las comprobaciones por las que no recibió todos los puntos, a veces, se indican detalles útiles en el informe de envío.
    

## Laboratorio completado

¡Felicitaciones! Ha completado el laboratorio.

66. Seleccione End Lab (Finalizar laboratorio) en la parte superior de esta página y, a continuación, seleccione Yes (Sí) para confirmar que desea finalizar el laboratorio.  
    
    Aparecerá un panel al final del laboratorio que indica “You may close this message box now” (Ya puede cerrar este cuadro de mensaje).
    
67. Seleccione la **X** en la esquina superior derecha para cerrar el panel.
    

## Recursos adicionales

- [Lanzar la instancia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html)
    
- [Tipos de instancias de Amazon EC2](https://aws.amazon.com/ec2/instance-types)
    
- [Imágenes de máquina de Amazon (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
    
- [Amazon EC2: datos de usuario y scripts de shell](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)
    
- [Volumen de dispositivo raíz de Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html)
    
- [Etiquetar los recursos de Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)
    
- [Grupos de seguridad](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html)
    
- [Pares de claves de Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
    
- [Comprobaciones de estado de las instancias](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html?icmpid=docs_ec2_console)
    
- [Obtener resultados de la consola y reiniciar instancias](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html)
    
- [Métricas y dimensiones de Amazon EC2](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ec2-metricscollected.html)
    
- [Modificar el tamaño de la instancia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)
    
- [Detener e iniciar la instancia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)
    
- [Límites de servicio de Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
    
- [Terminar la instancia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html)
    
- [Protección de terminación para una instancia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html)
    

© 2023, Amazon Web Services, Inc. y sus filiales. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial.