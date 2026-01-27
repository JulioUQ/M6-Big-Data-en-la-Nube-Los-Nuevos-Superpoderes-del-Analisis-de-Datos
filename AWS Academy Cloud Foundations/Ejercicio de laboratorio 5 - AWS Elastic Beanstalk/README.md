# Actividad: AWS Elastic Beanstalk

## Información general sobre el laboratorio

Esta actividad le proporcionará una cuenta de Amazon Web Services (AWS) en la que se creó previamente un entorno de AWS Elastic Beanstalk para usted. Implementará código y observará los recursos de AWS que componen el entorno de Elastic Beanstalk.

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

## Tarea 1: Acceder al entorno de Elastic Beanstalk

4. En la consola, en el cuadro de búsqueda a la derecha de _***Servicios***_, busque y seleccione _***Elastic Beanstalk***_.
    
    Se abrirá una página titulada **Entornos**, que mostrará una tabla con los detalles de una aplicación de Elastic Beanstalk existente.
    
    **Nota**: Si el estado en la columna **Estado** no es correcto, todavía no ha finalizado el arranque. Espere un momento y cambiará a correcto.
    
    ![elastic-beanstalk-app](https://labs.vocareum.com/web/4721338/4945487.0/ASNLIB/public/docs/lang/es-la/images/application.png)
    
5. En la columna **Nombre del entorno**, elija el nombre del entorno.
    
    Se abrirá la página **Panel** del entorno Elastic Beanstalk.
    
6. Observe que la página muestra que el estado de su aplicación es correcto.
    
    El entorno de Elastic Beanstalk está listo para alojar una aplicación. Sin embargo, aún no tiene ningún código en ejecución.
    
7. Prueba de acceso al entorno.
    
    - Cerca de la parte superior de la página, elija el enlace del dominio (la URL termina en _elasticbeanstalk.com_).
        
        Al elegir la URL, se abrirá una nueva pestaña del navegador. Sin embargo, debería ver que aparece un mensaje **HTTP Status 404 - Not Found** (Estado HTTP 404: no encontrado).
        
        _Este comportamiento es normal_ porque aún no se está ejecutando ninguna aplicación en este servidor de aplicaciones.
        
    - Vuelva a la pestaña de la consola de Elastic Beanstalk.
        
        En el siguiente paso, implementará el código en su entorno de Elastic Beanstalk.
        

## Tarea 2: Implementar una aplicación de ejemplo en Elastic Beanstalk

8. Para descargar una aplicación de muestra, seleccione este enlace: [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/samples/tomcat.zip](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/samples/tomcat.zip)
    

9. De vuelta en el panel de Elastic Beanstalk, seleccione **Cargar e implementar**.
    
10. Seleccione **Elegir archivo**, luego navegue hasta el archivo **tomcat.zip** que acaba de descargar y ábralo.
    
11. Seleccione **Implementar**.
    
    Elastic Beanstalk tardará uno o dos minutos en actualizar el entorno e implementar la aplicación.
    
12. Una vez finalizada la implementación, seleccione el enlace URL del dominio (o, si aún tiene abierta la pestaña del navegador que mostraba el estado 404, actualice esa página).
    
    Se mostrará la aplicación web que implementó.
    
    ![web-app](https://labs.vocareum.com/web/4721338/4945487.0/ASNLIB/public/docs/lang/es-la/images/web-app.png)
    
    ¡Felicitaciones, ha implementado correctamente una aplicación en Elastic Beanstalk!
    
13. De vuelta en la consola de Elastic Beanstalk, seleccione **Configuración** en el panel izquierdo.
    
    Observe los detalles.
    
    Por ejemplo, el panel **Instance traffic and scaling** (Escalado y tráfico de instancias), indica los grupos de seguridad de EC2, las instancias mínimas y máximas y los detalles del tipo de instancia de las instancias de Amazon Elastic Compute Cloud (Amazon EC2) que alojan la aplicación web.
    
14. En el panel **Networking, database, and tags** (Redes, bases de datos y etiquetas), no se muestran los detalles de configuración porque el entorno no incluye una base de datos.
    
15. En la fila **Networking, database, and tags** (Redes, bases de datos y etiquetas), seleccione **Edit** (Editar).
    
    Tenga en cuenta que si lo desea, puede habilitar fácilmente una base de datos en este entorno: solo tiene que establecer algunas configuraciones básicas y elegir **Apply** (Aplicar). (Sin embargo, para esta actividad, no es necesario agregar una base de datos).
    
    - En la parte inferior de la página, seleccione **Cancel** (Cancelar).
    
16. En el panel izquierdo, en _Environment_ (Entorno), seleccione **Monitoring** (Supervisión).
    
    Navegue por los gráficos para ver los tipos de información que están disponibles.
    

## Tarea 3: Explorar los recursos de AWS que admiten la aplicación

17. En la consola, en el cuadro de búsqueda a la derecha de _***Servicios***_, busque y seleccione **EC2**.
    
18. Elija **Instancias**.
    
    Observe que se están ejecutando dos instancias que admiten su aplicación web (ambas contienen _samp_ en sus nombres).
    
19. Si desea seguir explorando los recursos del servicio Amazon EC2 creados por Elastic Beanstalk, puede hacerlo. Encontrará:
    
    - Un _grupo de seguridad_ con el puerto 80 abierto
    - Un _equilibrador de carga_ al que pertenecen ambas instancias
    - Un _grupo de Auto Scaling_ que ejecuta de dos a seis instancias, en función de la carga de la red
    
    Aunque Elastic Beanstalk creó estos recursos para usted, seguirá teniendo acceso a ellos.
    

## Envío del trabajo

20. Para registrar su progreso, seleccione **Submit** (Enviar) en la parte superior de estas instrucciones.
    
21. Cuando se le solicite, seleccione **Yes** (Sí).
    
    Después de un par de minutos, aparece el panel de calificaciones y le muestra cuántos puntos obtuvo por cada tarea. Si los resultados no se muestran después de algunos minutos, seleccione **Grades** (Calificaciones) en la parte superior de estas instrucciones.
    
    **Importante:** Algunas de las comprobaciones realizadas por el proceso de envío en este laboratorio solo le otorgarán créditos si han transcurrido 5 minutos cómo mínimo desde que completó la acción. Si no recibe los créditos la primera vez que hace el envío, puede que deba esperar un par de minutos y enviar nuevamente para recibir los créditos por estos elementos.
    
    **Sugerencia:** Puede enviar su trabajo varias veces. Después de modificar el trabajo, vuelva a seleccionar **Submit** (Enviar). Su último envío quedó registrado para este laboratorio.
    
22. Para obtener comentarios detallados sobre su trabajo, seleccione **Submission Report** (Informe de envío).
    
    **Sugerencia:** En los casos de las comprobaciones por las que no recibió todos los puntos, a veces, se indican detalles útiles en el informe de envío.
    

## Actividad completada

¡Felicitaciones! Ha completado la actividad.

23. En la parte superior de esta página, haga clic en End Lab (Finalizar laboratorio) y, a continuación, elija Yes (Sí) para confirmar que desea finalizar la actividad.
    
    Aparece un panel que muestra el mensaje: _DELETE has been initiated… You may close this message box now_ (Se ha iniciado la ELIMINACIÓN… Ya puede cerrar este cuadro de mensaje).
    
24. Para cerrar el panel, vaya a la esquina superior derecha y seleccione la **X**.
    

© 2023, Amazon Web Services, Inc. y sus filiales. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial.