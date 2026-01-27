# Laboratorio 6: Escalado y balanceo de carga de la arquitectura

## Información general y objetivos del laboratorio

En este laboratorio, aprenderá a utilizar los servicios de Elastic Load Balancing (ELB) y Auto Scaling para balancear la carga y escalar la infraestructura de forma automática.

**Elastic Load Balancing** distribuye de forma automática el tráfico entrante de las aplicaciones entre varias instancias de Amazon EC2. Además, permite desarrollar tolerancia a errores para las aplicaciones ya que proporciona de forma sencilla la capacidad de balanceo de carga necesaria con el fin de dirigir el tráfico de la aplicación.

**Auto Scaling** permite mantener la disponibilidad de las aplicaciones y aumentar o reducir de forma automática la capacidad de Amazon EC2 según las condiciones que se definan. Puede utilizar Auto Scaling para asegurarse de que ejecuta la cantidad deseada de instancias de Amazon EC2. Con Auto Scaling, también se puede aumentar de forma automática la cantidad de instancias de Amazon EC2 durante los picos de demanda para mantener el rendimiento y reducir la capacidad durante los períodos de baja demanda con el objetivo de minimizar los costos. Auto Scaling es adecuado para aplicaciones con patrones de demanda estables o para aquellas cuyo uso varía cada hora, día o semana.

Al final de este laboratorio, podrá hacer lo siguiente:

- Crear una Imagen de máquina de Amazon (AMI) a partir de una instancia en ejecución.
    
- Crear un equilibrador de carga.
    
- Crear una plantilla de lanzamiento y un grupo de escalado automático.
    
- Escalar automáticamente las nuevas instancias
    
- Crear alarmas de Amazon CloudWatch y monitorear el rendimiento de la infraestructura.
    

## **Duración**

El tiempo estimado para completar este laboratorio es de **30 minutos**.

## Restricciones de los servicios de AWS

En el entorno de esta sesión de laboratorio, es posible que el acceso a los servicios de AWS y a las acciones del servicio esté restringido a los servicios necesarios para completar las instrucciones de la sesión. Puede que encuentre errores si intenta acceder a otros servicios o ejecutar acciones aparte de las que se detallan en este laboratorio.

**Advertencia**: Cualquier intento de tener 20 o más instancias en ejecución simultánea (independientemente del tamaño) dará lugar a la desactivación inmediata de la cuenta de AWS, y todos los recursos de la cuenta se eliminarán al instante.

## Situación

Empezará con la siguiente infraestructura:

![Arquitectura inicial](https://labs.vocareum.com/web/4721338/4945493.0/ASNLIB/public/docs/lang/es-la/images/starting-architecture.png)

El estado final de la infraestructura es el siguiente:

![Arquitectura final](https://labs.vocareum.com/web/4721338/4945493.0/ASNLIB/public/docs/lang/es-la/images/final-architecture.png)

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

## Tarea 1: crear una AMI para Auto Scaling

En esta tarea, creará una AMI a partir del _Web Server 1_ (Servidor web 1) existente. Esto permitirá guardar el contenido del disco de arranque para que se puedan lanzar instancias nuevas con un contenido idéntico.

4. En la **Consola de administración de AWS**, en el cuadro de búsqueda junto a Servicios , busque y seleccione **EC2**.
    
5. En el panel de navegación izquierdo, elija **Instancias**.
    
    Primero, confirmará que la instancia se encuentre en ejecución.
    
6. Espere hasta que en **Comprobaciones de estado** de **Web Server 1** (Servidor web 1) se muestre el mensaje _2/2 comprobaciones superadas_. Si es necesario, seleccione para actualizar el estado.
    
    Ahora, creará una AMI basada en esta instancia.
    
7. Seleccione **Web Server 1** (Servidor web 1).
    
8. En el menú Acciones , seleccione **Imagen y plantillas** > **Crear imagen** y configure lo siguiente:
    
    - **Nombre de la imagen:** `WebServerAMI`
        
    - **Descripción de la imagen:** `Lab AMI for Web Server`
        
9. Seleccione Crear imagen
    
    En un anuncio de confirmación, se muestra el **ID de AMI** de la nueva AMI.
    
    Utilizará esta AMI cuando inicie el grupo de escalado automático más adelante en el laboratorio.
    

## Tarea 2: crear un equilibrador de carga

En esta tarea, primero creará un grupo de destino y, luego, un equilibrador de carga para equilibrar el tráfico en varias instancias de EC2 y zonas de disponibilidad.

10. En el panel de navegación izquierdo, elija **Grupos de destino**.
    
    **Análisis**: Los _grupos de destino_ definen a dónde _enviar_ el tráfico que llega al equilibrador de carga. El equilibrador de carga de aplicación puede enviar tráfico a varios grupos de destino en función de la URL de la solicitud entrante, como, por ejemplo, que las solicitudes de las aplicaciones móviles vayan a un conjunto diferente de servidores. La aplicación web solo utilizará un grupo de destino.
    
    - Elija Crear grupo de destino
        
    - Elija un tipo de destino: **Instancias**
        
    - **Nombre del grupo de destino**, ingrese: `LabGroup`
        
    - Seleccione **Lab VPC** (VPC del laboratorio) en el menú desplegable **VPC**.
        
11. Elija Siguiente. Aparece la pantalla **Registrar destinos**.
    
    Nota: Los _Destinos_ son las instancias individuales que responderán a las solicitudes del equilibrador de carga.
    
    Todavía no tiene ninguna instancia de aplicación web, por lo que puede omitir este paso.
    
12. Revise la configuración y elija Crear grupo de destino
    
13. En el panel de navegación izquierdo, elija **Balanceadores de carga**.
    
14. En la parte superior de la pantalla, seleccione Crear balanceador de carga.
    
    A continuación, se muestran diferentes tipos de equilibradores de carga. Utilizará un _equilibrador de carga de aplicación_ que funciona a nivel de solicitud (capa 7), a través del cual se dirige el tráfico a los destinos (instancias de EC2, contenedores, direcciones IP y funciones de Lambda) según el contenido de la solicitud. Para obtener más información, consulte: [Comparación de equilibradores de carga](https://aws.amazon.com/elasticloadbalancing/features/#compare)
    
15. En **Equilibrador de carga de aplicación**, seleccione Crear
    
16. En **Nombre del balanceador de carga**, ingrese: `LabELB`
    
17. Desplácese a la sección **Mapeo de red**, luego, haga lo siguiente:
    
    - En **VPC**, elija **Lab VPC** (VPC de laboratorio).
        
        Ahora especificará qué _subredes_ debe utilizar el equilibrador de carga. Será un equilibrador de carga orientado a Internet, por lo que seleccionará ambas subredes públicas.
        
    - Elija la zona de disponibilidad que aparece en **primer** lugar, luego, seleccione **Subred pública 1** en el menú desplegable Subred que se muestra debajo de ella.
        
    - Elija la zona de disponibilidad que aparece en **segundo** lugar, luego, seleccione **Subred pública 2** en el menú desplegable Subred que se muestra debajo de ella.
        
        Ahora debería tener dos subredes seleccionadas: la **Subred pública 1** y la **Subred pública 2**.
        
18. En la sección **Grupos de seguridad**, configure lo siguiente:
    
    - Elija el menú desplegable Grupos de seguridad y seleccione **Web Security Group** (Grupo de seguridad web).
        
    - Debajo del menú desplegable, elija la **X** junto al grupo de seguridad predeterminado para eliminarlo.
        
        Ahora, el grupo de seguridad **Web Security Group** (Grupo de seguridad web) debería ser el único que aparece.
        
19. Para la fila del agente de escucha HTTP:80, configure la acción Predeterminada en **LabGroup**.
    
20. Desplácese hasta la parte inferior y seleccione Crear balanceador de carga
    
    Se creó correctamente el equilibrador de carga.
    
    - Elija Ver el balanceador de carga
        
        El equilibrador de carga mostrará un estado de _aprovisionando_. No es necesario esperar hasta que se encuentre listo. Continúe con la siguiente tarea.
        

## Tarea 3: crear una plantilla de lanzamiento y un grupo de escalado automático

En esta tarea, creará una _plantilla de lanzamiento_ para el grupo de Auto Scaling. Una plantilla de lanzamiento consiste en una plantilla que utiliza un grupo de escalado automático para lanzar instancias de EC2. Cuando se crea una plantilla de lanzamiento, se especifica la información de las instancias, tales como la AMI, el tipo de instancia, un par de claves y un grupo de seguridad.

21. En el panel de navegación izquierdo, elija **Plantillas de lanzamiento**.
    
22. Elija Crear plantilla de lanzamiento
    
23. Configure los ajustes de la plantilla de lanzamiento y créela:
    
    - **Nombre de la plantilla de lanzamiento:** `LabConfig`
        
    - En **Orientación sobre Auto Scaling**, seleccione _Provide guidance to help me set up a template that I can use with EC2 Auto Scaling_ (Proporcionar orientación para ayudarme a configurar una plantilla que pueda utilizar con EC2 Auto Scaling).
        
    - En el área Imágenes de aplicaciones y sistemas operativos (Imagen de máquina de Amazon), seleccione _Mis AMI_.
        
    - **Imagen de máquina de Amazon (AMI)**: elija _Web Server AMI_ (AMI de servidor web)
        
    - **Tipo de instancia:** elija _t2.micro_
        
    - **Nombre del par de claves**: elija _vockey_
        
    - **Firewall (grupos de seguridad)**: elija _Seleccionar un grupo de seguridad existente_.
        
    - **Grupos de seguridad**: elija _Web Security Group_ (Grupo de seguridad web).
        
    - Desplácese hacia abajo hasta la sección **Detalles avanzados** y expándala.
        
    - Desplácese hacia abajo hasta la configuración de **Monitorización detallada de CloudWatch**. Seleccione _Habilitar_
        
        Nota: Esto permitirá que Auto Scaling reaccione rápidamente a los cambios de utilización.
        
    - Elija Crear plantilla de lanzamiento
        
        A continuación, creará un grupo de escalado automático que utilice esta plantilla de lanzamiento.
        
24. En el cuadro de diálogo de Listo, elija la plantilla de lanzamiento **LabConfig**.
    
25. En el menú Acciones , seleccione _Crear grupo de Auto Scaling_
    
26. Configure los detalles en el Paso 1 (Elegir la plantilla o la configuración de lanzamiento):
    
    - **Nombre del grupo de Auto Scaling:** `Lab Auto Scaling Group`
        
    - **Lanzar plantilla**: confirme que esté seleccionada la plantilla _LabConfig_ que acaba de crear.
        
    - Elija Siguiente
        
27. Configure los detalles en el Paso 2 (Elegir las opciones de lanzamiento de la instancia):
    
    - **VPC**: seleccione _Lab VPC_ (VPC de laboratorio).
        
    - **Zonas de disponibilidad y subredes**: elija _Subred privada 1_ y, a continuación, seleccione _Subred privada 2_.
        
    - Elija Siguiente
        
28. Configure los detalles en el Paso 3 (Configurar opciones avanzadas):
    
    - Seleccione **Asociar a un balanceador de carga existente**
        
        - **Grupos de destino del balanceador de carga existentes**: seleccione _LabGroup_.
            
    - En el panel **Configuración adicional**:
        
        - Seleccione **Enable group metrics collection within CloudWatch** (Habilitar la recopilación de métricas de grupo en CloudWatch)
            
        
        De este modo, se capturarán métricas en intervalos de 1 minuto, lo que permite que Auto Scaling reaccione rápidamente a los patrones de uso cambiantes.
        
    - Elija Siguiente
        
29. Configure los detalles en el Paso 4 (Configurar políticas de escalado y tamaño de grupo, opcional):
    
    - En **Tamaño de grupo**, configure lo siguiente:
        
        - **Capacidad deseada:** 2
            
        - **Capacidad mínima:** 2
            
        - **Capacidad máxima:** 6
            
            Esto permite que Auto Scaling agregue o elimine instancias automáticamente, y siempre mantenga entre dos y seis instancias en ejecución.
            
    - En **Políticas de escalado**, seleccione _Política de escalado de seguimiento de destino_ y configure lo siguiente:
        
        - **Nombre de la política de escalado:** `LabScalingPolicy`
            
        - **Tipo de métrica:** _utilización de CPU promedio_
            
        - **Valor de destino:** `60`
            
            De este modo, se le indica a Auto Scaling que mantenga un uso _promedio_ de CPU del 60 % _en todas las instancias_. Auto Scaling aumenta o reduce la capacidad de forma automática, según sea necesario, para mantener la métrica en el valor de destino especificado o en un valor próximo. Se ajusta a las fluctuaciones de la métrica debido a un patrón de carga fluctuante.
            
    - Elija Siguiente
        
30. Configure los detalles en el Paso 5 (Agregar notificaciones, opcional):
    
    Auto Scaling puede enviar una notificación cuando se produce un evento de escalado. Deberá utilizar los valores predeterminados.
    
    - Elija Siguiente
        
31. Configure los detalles en el Paso 6 (Agregar etiquetas, opcional):
    
    Las etiquetas que se apliquen al grupo de escalado automático se propagarán automáticamente a las instancias que se lancen.
    
    - Elija Agregar etiqueta y configure lo siguiente:
        
        - **Clave:** `Name`
            
        - **Valor:** `Lab Instance`
            
    - Elija Siguiente
        
32. Configure los detalles en el Paso 6 (Revisar):
    
    - Revise los detalles de tu grupo de escalado automático
        
    - Seleccione Crear grupo de Auto Scaling
        
        En el grupo de Auto Scaling, se mostrará inicialmente un recuento de instancias igual a cero, pero se iniciarán instancias nuevas para alcanzar el recuento **deseado** de 2 instancias.
        

## Tarea 4: comprobar el funcionamiento del balanceo de carga

En esta tarea, verificará el correcto funcionamiento del balanceo de carga.

33. En el panel de navegación izquierdo, elija **Instancias**.
    
    Verá dos instancias nuevas llamadas **Lab Instance** (Instancia de laboratorio). Auto Scaling las ha iniciado.
    
    Si no se visualizan las instancias o sus nombres, espere 30 segundos y seleccione Actualizar , en la esquina superior derecha.
    
    A continuación, asegúrese de que las instancias nuevas hayan superado la comprobación de estado.
    
34. En el panel de navegación izquierdo, elija **Grupos de destino**.
    
35. Seleccione _LabGroup_
    
36. Elija la pestaña **Destinos**.
    
    En el grupo de destino deben aparecer dos instancias de destino denominadas instancia de laboratorio.
    
37. Espere a que el **Estado** de ambas instancias cambie a _en buen estado_.
    
    Seleccione Actualizar en la parte superior derecha para verificar si hay actualizaciones.
    
    Si el estado de una instancia es _En buen estado_, significa que la instancia superó la comprobación de estado del equilibrador de carga. Esto significa que el balanceador de carga enviará tráfico a la instancia.
    
    Ahora, puede acceder al grupo de escalado automático mediante el equilibrador de carga.
    
38. En el panel de navegación izquierdo, elija **Balanceadores de carga**.
    
39. Seleccione el equilibrador de carga _LabELB_.
    
40. En el panel Detalles, copie el **Nombre de DNS** del equilibrador de carga y asegúrese de omitir “(A Record)” (Registro A).
    
    Debería ser similar a: _LabELB-1998580470.us-west-2.elb.amazonaws.com_
    
41. Abra una pestaña nueva en el navegador web, pegue el nombre de DNS que acaba de copiar y presione la Enter (Intro).
    
    La aplicación debe aparecer en el navegador. Esto indica que el Balanceador de carga recibió la solicitud, la envió a una de las instancias EC2 y luego arrojó el resultado.
    

## Tarea 5: realizar pruebas de Auto Scaling

Ha creado un grupo de escalado automático con un mínimo de dos instancias y un máximo de seis. En el momento hay dos instancias en ejecución porque dos es el tamaño mínimo y el grupo no está sujeto a ninguna carga. Ahora, aumentará la carga para que Auto Scaling agregue instancias adicionales.

42. Regrese a la Consola de administración de AWS, pero no cierre la pestaña de la aplicación, ya que pronto deberá volver a ella.
    
43. En el cuadro de búsqueda junto a Servicios , busque y seleccione **CloudWatch**.
    
44. En el panel de navegación izquierdo, elija **Todas las alarmas**.
    
    Se mostrarán dos alarmas. El grupo de escalado automático creó estas alarmas de forma automática. Dichas alarmas mantendrán la carga promedio de CPU cerca del 60 % y, al mismo tiempo, respetarán la limitación de tener entre dos y seis instancias.
    
    **Nota**: Siga estos pasos únicamente si no ve las alarmas en 60 segundos.
    
    - En el menú Servicios , elija **EC2**.
        
    - En el panel de navegación izquierdo, elija **Grupos de Auto Scaling**.
        
    - Seleccione **Lab Auto Scaling Group** (Grupo de Auto Scaling de laboratorio).
        
    - En la mitad inferior de la página, seleccione la pestaña **Escalado automático**.
        
    - Seleccione **LabScalingPolicy**.
        
    - Seleccione Acciones y **Editar**.
        
    - Cambie **Valor de destino** a `50`.
        
    - Seleccione Actualizar
        
    - En el menú Servicios , elija **CloudWatch**.
        
    - En el panel de navegación izquierdo, elija **Todas las alarmas** y verifique que se vean dos alarmas.
        

45. Seleccione la alarma **OK**, que en su nombre contiene _AlarmHigh_.
    
    Si en ninguna alarma aparece **OK**, espere un minuto y seleccione Actualizar en la esquina superior derecha, hasta que cambie el estado de la alarma.
    
    **OK** indica que la alarma _no_ se ha activado. La alarma **CPU Utilization > 60** (Uso de CPU > 60) agrega instancias cuando el uso promedio de CPU es alto. En este momento, el gráfico debería mostrar niveles muy bajos de uso de CPU.
    
    Ahora, le indicará a la aplicación que realice cálculos que deberían aumentar el nivel de uso de CPU.
    
46. Regrese a la pestaña del navegador donde se encuentra la aplicación web.
    
47. Seleccione **Load Test** (Prueba de carga) junto al logotipo de AWS.
    
    Esto hará que la aplicación genere cargas elevadas. La página del navegador se actualizará de forma automática para que todas las instancias del grupo de escalado automático generen carga. No cierre esta pestaña.
    
48. Regrese a la pestaña del navegador donde se encuentra la consola de **CloudWatch**.
    
    En menos de 5 minutos, la alarma **AlarmLow** debería cambiar a **OK** y el estado de la alarma **AlarmHigh** debería cambiar a _Con alarma_.
    
    Puede seleccionar Actualizar en la parte superior derecha cada 60 segundos para actualizar la pantalla.
    
    Debería ver en el gráfico **AlarmHigh** un porcentaje en aumento del uso de CPU. Cuando se cruce la línea del 60 % por más de 3 minutos, Auto Scaling agregará más instancias.
    
49. Espere hasta que la alarma **AlarmHigh** entre en estado _Con alarma_.
    
    Ahora puede visualizar las instancias adicionales que se iniciaron.
    
50. En el cuadro de búsqueda junto a Servicios , busque y seleccione **EC2**.
    
51. En el panel de navegación izquierdo, elija **Instancias**.
    
    Debería haber más de dos instancias etiquetadas como **Lab Instance** (Instancia de laboratorio) en ejecución. Las instancias nuevas se crearon con Auto Scaling como respuesta a la alarma de CloudWatch.
    

## Tarea 6: terminar el Servidor web 1

En esta tarea, terminará el _Web Server 1_ (Servidor web 1). Esta instancia se utilizó para crear la AMI que usó el grupo de escalado automático, pero ya no es necesaria.

52. Seleccione **Web Server 1** (Servidor web 1) y asegúrese de que sea la única instancia seleccionada.
    
53. En el menú Estado de la instancia , seleccione **Estado de la instancia** > **Terminar instancia**.
    
54. Seleccione Terminar
    

## Envío del trabajo

55. Para registrar su progreso, seleccione **Submit** (Enviar) en la parte superior de estas instrucciones.
    
56. Cuando se le solicite, seleccione **Yes** (Sí).
    
    Después de un par de minutos, aparece el panel de calificaciones y le muestra cuántos puntos obtuvo por cada tarea. Si los resultados no se muestran después de algunos minutos, seleccione **Grades** (Calificaciones) en la parte superior de estas instrucciones.
    
    **Sugerencia:** Puede enviar su trabajo varias veces. Después de modificar el trabajo, vuelva a seleccionar **Submit** (Enviar). Su último envío quedó registrado para este laboratorio.
    
57. Para obtener comentarios detallados sobre su trabajo, seleccione **Submission Report** (Informe de envío).
    
    **Sugerencia:** En los casos de las comprobaciones por las que no recibió todos los puntos, a veces, se indican detalles útiles en el informe de envío.
    

## Laboratorio completado

¡Felicitaciones! Completó el laboratorio.

58. Seleccione End Lab (Finalizar laboratorio) en la parte superior de esta página y, a continuación, seleccione Yes (Sí) para confirmar que desea finalizar el laboratorio.
    
    Aparecerá un panel que indica “DELETE has been initiated… You may close this message box now” (Se ha iniciado la ELIMINACIÓN… Ya puede cerrar este cuadro de mensaje).
    
59. Seleccione la **X** en la esquina superior derecha para cerrar el panel.
    

_© 2024 Amazon Web Services, Inc. y sus filiales. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial._