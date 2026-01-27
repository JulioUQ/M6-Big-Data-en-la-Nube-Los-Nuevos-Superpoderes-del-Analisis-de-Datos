# Actividad: AWS Lambda

## Información general sobre el laboratorio


En esta actividad práctica, creará una función de AWS Lambda. También creará un evento de Amazon EventBridge para activar la función cada minuto. La función usa un rol de AWS Identity and Access Management (AWS IAM). Este rol de IAM permite que la función detenga una instancia de Amazon Elastic Compute Cloud (Amazon EC2) que se esté ejecutando en la cuenta de Amazon Web Services (AWS).

## Duración

Esta actividad tarda aproximadamente **30 minutos** en completarse.

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

## Tarea 1: Crear una función de Lambda

4. En el cuadro de búsqueda que se encuentra a la derecha de **Servicios**, busque y seleccione **Lambda** para abrir la consola de AWS Lambda.
    
5. Seleccione **Crear una función**.
    
6. En la pantalla **Crear una función**, establezca la siguiente configuración:
    
    - Seleccione **Crear desde cero**.
        
    - Nombre de la función: `myStopinator`
        
    - Tiempo de ejecución: **Python 3.11**
        
    - Elija **Cambiar rol de ejecución predeterminado**
        
    - Rol de ejecución: **utilice un rol existente**
        
    - Rol existente: en la lista desplegable, elija **myStopinatorRole**
        
7. Seleccione **Crear una función**.
    

## Tarea 2: Configurar el desencadenador

En esta tarea, configurará un evento programado para activar la función de Lambda estableciendo un evento de Amazon EventBridge como el evento de origen (o desencadenador). Se puede configurar la función de Lambda para que opere de manera muy similar a un trabajo cron en un servidor Linux, o a una tarea programada en un servidor Microsoft Windows. Sin embargo, no es necesario que se ejecute un servidor para alojarla.

8. Elija **Agregar desencadenador**.
    
9. Elija el menú desplegable **Seleccionar un desencadenador** y elija **EventBridge (CloudWatch Events)**.
    
10. Para la regla, elija **Crear una nueva regla** y establezca la siguiente configuración:
    
    - Nombre de la regla: `everyMinute`
    - Tipo de regla: **expresión de programación**
    - Expresión de programación: `rate(1 minute)`
    
    **Nota**: Un stopinator de función de Lambda más realista basado en una programación probablemente se activaría con una expresión cron en lugar de una expresión rate. Sin embargo, para fines de esta actividad, con una expresión rate nos aseguramos de que la función de Lambda se active con la rapidez necesaria para que pueda ver los resultados.
    
11. Seleccione **Agregar**.
    

## Tarea 3: Configurar la función de Lambda

En esta tarea, pegará algunas líneas de código para actualizar dos valores en el código de la función. No hace falta que escriba código para completar esta tarea.

12. Debajo del panel **Información general de la función**, seleccione **Código** y, luego, elija _lambda_function.py_ para mostrar y editar el código de la función de Lambda.
    
13. En el panel **Código fuente**, elimine el código existente. Copie el siguiente código y péguelo en el cuadro:
    
    import boto3
    
    region = '<REPLACE_WITH_REGION>'
    
    instances = ['<REPLACE_WITH_INSTANCE_ID>']
    
    ec2 = boto3.client('ec2', region_name=region)
    
    def lambda_handler(event, context):
    
        ec2.stop_instances(InstanceIds=instances)
    
        print('stopped your instances: ' + str(instances))
    
    **Nota:** Después de pegar el código en el cuadro **Código fuente**, revise la línea 5. Si se agregó un punto (.), elimínelo.
    

14. Reemplace el marcador de posición `<REPLACE_WITH_REGION>` por la región real que está utilizando. Para ello, realice lo siguiente:
    
    Elija la región en la esquina superior derecha y use el código de región. Por ejemplo, el código de región para EE. UU. Este (Norte de Virginia) es _us-east-1_.
    
    **Importante**: Mantenga las comillas simples (' ') alrededor de la región en el código. Por ejemplo, para Norte de Virginia, sería `'us-east-1'`
    
15. **Sección de desafío**: Verifique que una instancia de EC2 llamada _instance1_ se está ejecutando en su cuenta y copie el **ID de instancia** de _instance1_.
    
    Se recomienda que averigüe cómo hacer esta tarea sin una orientación paso a paso específica. Sin embargo, si necesita orientación detallada, seleccione este texto para revelar pasos específicos: Abra otra pestaña del navegador y vaya a https://console.aws.amazon.com/ec2. Elija Instancias. Tenga en cuenta que existe una instancia de EC2 llamada *instance1* y que está en el estado en ejecución. En la pestaña Detalles de instance1, copie el ID de instancia (comenzará con i-) Nota: Deje esta pestaña del navegador abierta. Volverá a ella en un momento.
    
16. Vuelva a la pestaña del navegador de la **consola de AWS Lambda** y reemplace `<REPLACE_WITH_INSTANCE_ID>` por el ID de instancia real que acaba de copiar.
    
    **Importante**: Mantenga las comillas simples (' ') alrededor del ID de instancia en el código.
    
    Ahora, el código debe ser similar al siguiente ejemplo. Sin embargo, podría tener un valor diferente para la región y tendrá un valor diferente para el ID de instancia.
    
    ![diagrama de la arquitectura](https://labs.vocareum.com/web/4721338/4945485.0/ASNLIB/public/docs/lang/es-la/images/lambda-activity-2.png)
    
17. Elija el menú **Archivo** y **guarde** los cambios. Después, en la esquina superior derecha del cuadro **Código fuente**, elija **Implementar**.
    
    Su función de Lambda ahora está totalmente configurada. Debería intentar detener su instancia cada minuto.
    
18. Elija **Monitorear** (la pestaña cerca de la parte superior de la página).
    
    Tenga en cuenta que uno de los gráficos muestra cuántas veces se invocó la función. También hay un gráfico que muestra el recuento de errores y la tasa de éxito como un porcentaje.
    

## Tarea 4: Verificar que la función de Lambda funcionó

19. Vuelva a la pestaña del navegador de la **consola de Amazon EC2** y vea si se detuvo su instancia.
    
    **Sugerencia**: Puede elegir el ícono de actualización o actualizar la página del navegador para ver el cambio de estado más rápido.
    
20. Intente volver a iniciar la instancia. ¿Qué cree que podría suceder?
    
    Seleccione **aquí** para revelar la respuesta. La instancia se detendrá nuevamente en 1 minuto.

## Envío del trabajo

21. Para registrar su progreso, seleccione **Submit** (Enviar) en la parte superior de estas instrucciones.
    
22. Cuando se le solicite, seleccione **Yes** (Sí).
    
    Después de un par de minutos, aparece el panel de calificaciones y le muestra cuántos puntos obtuvo por cada tarea. Si los resultados no se muestran después de algunos minutos, seleccione **Grades** (Calificaciones) en la parte superior de estas instrucciones.
    
    **Importante:** Algunas de las comprobaciones realizadas por el proceso de envío en este laboratorio solo le otorgarán créditos si han transcurrido 5 minutos cómo mínimo desde que completó la acción. Si no recibe los créditos la primera vez que hace el envío, puede que deba esperar un par de minutos y enviar nuevamente para recibir los créditos por estos elementos.
    
    **Sugerencia:** Puede enviar su trabajo varias veces. Después de modificar el trabajo, vuelva a seleccionar **Submit** (Enviar). Su último envío quedó registrado para este laboratorio.
    

23. Para obtener comentarios detallados sobre su trabajo, seleccione **Submission Report** (Informe de envío).
    
    **Sugerencia:** En los casos de las comprobaciones por las que no recibió todos los puntos, a veces, se indican detalles útiles en el informe de envío.
    

## Actividad completada

¡Felicitaciones! Ha completado la actividad.

24. Haga clic en End Lab (Finalizar laboratorio) en la parte superior de esta página y, a continuación, elija Yes (Sí) para confirmar que desea finalizar la actividad.
    
    Aparece un panel que muestra el mensaje: _DELETE has been initiated… You may close this message box now_ (Se ha iniciado la ELIMINACIÓN… Ya puede cerrar este cuadro de mensaje).
    
25. Para cerrar el panel, vaya a la esquina superior derecha y seleccione la **X**.
    

© 2023, Amazon Web Services, Inc. y sus filiales. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial.