# Laboratorio 4: Trabajo con EBS

## Información general sobre el laboratorio

![[Pasted image 20260127090625.png]]

Este laboratorio se enfoca en Amazon Elastic Block Store (Amazon EBS), un mecanismo de almacenamiento subyacente clave para las instancias de Amazon EC2. En este laboratorio, aprenderá a crear un volumen de Amazon EBS, adjuntarlo a una instancia, implementar un sistema de archivos en el volumen y crear un respaldo mediante una instantánea.

## Temas tratados

Al final de este laboratorio, podrá hacer lo siguiente:

- Crear un volumen de Amazon EBS
- Adjuntar el volumen a una instancia de EC2 y montarlo en ella
- Crear una instantánea del volumen
- Crear un nuevo volumen a partir de la instantánea
- Adjuntar el volumen nuevo a la instancia de EC2 y montarlo en ella

## Duración

El tiempo estimado para completar este laboratorio es de **30 minutos**.

## Restricciones de los servicios de AWS

En el entorno de este laboratorio, es posible que el acceso a los servicios de AWS y a sus respectivas acciones esté restringido a los servicios que son necesarios para completar las instrucciones del laboratorio. Puede que encuentre errores si intenta acceder a otros servicios o ejecutar acciones aparte de las que se detallan en este laboratorio.

### ¿Qué es Amazon Elastic Block Store?

**Amazon Elastic Block Store (Amazon EBS)** ofrece almacenamiento persistente para las instancias de Amazon EC2. Los volúmenes de Amazon EBS están adjuntos a la red y su duración es independiente de la vida de una instancia. Los volúmenes de Amazon EBS tienen un alto nivel de disponibilidad y fiabilidad, y pueden utilizarse como particiones de arranque de instancias de Amazon EC2 o adjuntarse a una instancia de Amazon EC2 en ejecución como dispositivos de bloques estándar.

Cuando se utilizan como particiones de arranque, las instancias de Amazon EC2 pueden detenerse y, luego, reiniciarse, lo que le permite pagar solo por los recursos de almacenamiento utilizados al mismo tiempo que conserva el estado de la instancia. Los volúmenes de Amazon EBS tienen una durabilidad mucho mayor que la de los almacenes de instancias Amazon EC2 locales porque se replican de forma automática en el backend (en una única zona de disponibilidad).

Sin embargo, si se quiere aún más durabilidad, con Amazon EBS es posible crear instantáneas uniformes puntuales de los volúmenes, que luego se almacenan en Amazon Simple Storage Service (Amazon S3) y se replican automáticamente en varias zonas de disponibilidad. Estas instantáneas se pueden utilizar como punto de partida para nuevos volúmenes de Amazon EBS y permiten proteger la durabilidad de los datos a largo plazo. También puede compartirlas fácilmente con colegas y otros desarrolladores de AWS.

En esta guía de laboratorio, se explican los conceptos básicos de Amazon EBS paso a paso. Sin embargo, solo se presenta información general sobre los conceptos de Amazon EBS. Para obtener más información, consulte la [documentación de Amazon EBS](http://aws.amazon.com/ebs/).

### Funciones de los volúmenes de Amazon EBS

Los volúmenes de Amazon EBS tienen las siguientes características:

- **Almacenamiento persistente:** la vida útil de los volúmenes es independiente de cualquier instancia de Amazon EC2.
    
- **De uso general:** los volúmenes de Amazon EBS son dispositivos de bloque sin formato y sin procesar que se pueden utilizar en cualquier sistema operativo.
    
- **Alto rendimiento:** los volúmenes de Amazon EBS son iguales o mejores que las unidades locales de Amazon EC2.
    
- **Alto nivel de fiabilidad:** los volúmenes de Amazon EBS tienen redundancia incorporada dentro de una zona de disponibilidad.
    
- **Diseñados para ofrecer resiliencia:** la tasa anual de errores (AFR) de Amazon EBS oscila entre un 0,1 % y 1 %.
    
- **Tamaño variable:** los tamaños de los volúmenes varían de 1 GB a 16 TB.
    
- **Fáciles de usar:** los volúmenes de Amazon EBS se pueden crear, adjuntar, respaldar, restaurar y eliminar fácilmente.
    

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

## Tarea 1: Crear un nuevo volumen de EBS

En esta tarea, creará y adjuntará un volumen de Amazon EBS a una nueva instancia de Amazon EC2.

4. En la Consola de administración de AWS, en el cuadro de búsqueda junto a Servicios , busque y seleccione **EC2**.
    
5. En el panel de navegación izquierdo, elija **Instancias**.
    
    Ya se lanzó una instancia de Amazon EC2 llamada **Lab** (Laboratorio) para el laboratorio.
    

6. Anote el valor de la **Zona de disponibilidad** correspondiente a la instancia. Será similar a _us-east-1a_.
    
7. En el panel de navegación izquierdo, seleccione **Volúmenes**.
    
    Verá un volumen existente que estará siendo utilizado por la instancia de Amazon EC2. Dicho volumen tiene un tamaño de 8 GiB, lo que permite distinguirlo fácilmente del volumen que creará a continuación, que será de 1 GiB.
    
8. Haga clic en Crear volumen y configure lo siguiente:
    
    - **Tipo de volumen:** _General Purpose SSD (gp2)_ (SSD de uso general [gp2]).
        
    - **Tamaño (GiB):** `1`. **NOTA**: Es posible que no pueda crear volúmenes grandes.
        
    - **Zona de disponibilidad:** seleccione la misma zona de disponibilidad que la de su instancia de EC2.
        
    - Seleccione Agregar etiqueta)
        
    - En el editor de etiquetas, ingrese lo siguiente:
        
        - **Clave:** `Name`
            
        - **Valor:** `My Volume`
            
9. Seleccione Crear volumen
    
    El nuevo volumen aparecerá en la lista y su estado cambiará de _Creando_ a _Disponible_. Tal vez deba hacer clic en **actualizar** para ver el nuevo volumen.
    

## Tarea 2: Adjuntar el volumen a una instancia

En esta tarea, adjuntará el nuevo volumen de EBS a la instancia de Amazon EC2.

10. Seleccione **My Volume** (Mi volumen).
    
11. En el menú **Acciones**, elija **Asociar volumen**.
    
12. Haga clic en el campo **Instancia** y, a continuación, seleccione la instancia **Lab** (Laboratorio).
    
    Observe que el campo **Dispositivo** está establecido en _/dev/sdf_. También observe el mensaje que aparece: "Newer Linux kernels may rename your devices to _/dev/xvdf_ through _/dev/xvdp_ internally, even when the device name entered here (and shown in the details) is _/dev/sdf_ through _/dev/sdp_" (Con los kernels de Linux más recientes, puede cambiar el nombre de sus dispositivos internamente a /dev/xvdf mediante /dev/xvdp, incluso si el nombre del dispositivo ingresado aquí [y que aparece en los detalles] fuera /dev/sdf mediante /dev/sdp).
    
13. Seleccione Asociar volumen
    
    El estado del volumen ahora será _In-use_ (En uso).
    

## Tarea 3: Conectarse a la instancia de Amazon EC2

En esta tarea, se conectará a la instancia de EC2 con EC2 Instance Connect que ofrece acceso a un terminal en el navegador.

14. En la Consola de administración de AWS, en el cuadro de búsqueda junto a Servicios , busque y seleccione **EC2**.
    
15. Elija **Instancias**.
    
16. Seleccione la instancia de **Lab** y luego seleccione **Conectar**.
    
17. Con la pestaña **EC2 Instance Connect** seleccionada, elija **Conectar**.
    
    Se abre una sesión de terminal de EC2 Instance Connect y muestra el mensaje `$`.
    

## Tarea 4: Crear y configurar el sistema de archivos

En esta tarea, agregará el volumen nuevo a una instancia de Linux como un sistema de archivos ext3 en el punto de montaje /mnt/data-store.

18. Vea el almacenamiento disponible de la instancia:
    
    Ejecute el siguiente comando:
    
    df -h
    
    Debería ver un resultado similar al siguiente:
    
    Filesystem      Size  Used Avail Use% Mounted on
    
    devtmpfs        4.0M     0  4.0M   0% /dev
    
    tmpfs           475M     0  475M   0% /dev/shm
    
    tmpfs           190M  2.8M  188M   2% /run
    
    /dev/xvda1      8.0G  1.6G  6.5G  20% /
    
    tmpfs           475M     0  475M   0% /tmp
    
    tmpfs            95M     0   95M   0% /run/user/1000
    
    El resultado muestra el volumen de disco original de 8 GB **/dev/xvda1** montado en `/` que indica que es el volumen raíz. Aloja el sistema operativo Linux de la instancia de EC2.
    
    No aparece el otro volumen de 1 GB que adjuntó a la instancia Lab, porque no ha creado un sistema de archivos en él ni ha montado el disco. Esas acciones son necesarias para que el sistema operativo Linux pueda usar el nuevo espacio de almacenamiento. Realizará esas acciones a continuación.
    
19. Cree un sistema de archivos ext3 en el volumen nuevo:
    
    sudo mkfs -t ext3 /dev/sdf
    
    El resultado debe indicar que se creó un nuevo sistema de archivos en el volumen adjunto.
    
20. Cree un directorio para montar el volumen de almacenamiento nuevo:
    
    sudo mkdir /mnt/data-store
    
21. Monte el volumen nuevo:
    
    sudo mount /dev/sdf /mnt/data-store
    
    Para configurar la instancia de Linux y poder montar este volumen siempre que se inicie la instancia, deberá agregar una línea a _/etc/fstab_. Ejecute el siguiente comando para hacer eso:
    
    echo "/dev/sdf   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab
    
22. Consulte el archivo de configuración para ver el parámetro de la última línea:
    
    cat /etc/fstab
    
23. Consulte de nuevo el almacenamiento disponible:
    
    df -h
    
    El resultado será similar a este:
    
    Filesystem      Size  Used Avail Use% Mounted on
    
    devtmpfs        484M     0  484M   0% /dev
    
    tmpfs           492M     0  492M   0% /dev/shm
    
    tmpfs           492M  460K  491M   1% /run
    
    tmpfs           492M     0  492M   0% /sys/fs/cgroup
    
    /dev/xvda1      8.0G  1.5G  6.6G  19% /
    
    tmpfs            99M     0   99M   0% /run/user/0
    
    tmpfs            99M     0   99M   0% /run/user/1000
    
    /dev/xvdf       976M  1.3M  924M   1% /mnt/data-store
    
    Observe la última línea. El resultado ahora muestra _/dev/xvdf_ que es el nuevo volumen montado.
    
24. Cree un archivo en el volumen montado y escriba algo en él.
    
    sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"
    
25. Compruebe que se haya escrito el texto en el volumen.
    
    cat /mnt/data-store/file.txt
    

Deje la sesión de EC2 Instance Connect en ejecución. Volverá a utilizarla más adelante en este laboratorio.

## Tarea 5: Crear una instantánea de Amazon EBS

En esta tarea, creará una instantánea del volumen de EBS.

Cuando lo desee, podrá crear una cantidad ilimitada de instantáneas uniformes de un momento específico de los volúmenes de Amazon EBS. Las instantáneas de Amazon EBS se almacenan en Amazon S3 con un alto nivel de durabilidad. Se pueden crear volúmenes de Amazon EBS nuevos a partir de instantáneas para clonar o restaurar respaldos. Las instantáneas de Amazon EBS también pueden compartirse fácilmente entre usuarios de AWS o copiarse entre regiones de AWS.

26. En la **Consola de EC2**, elija **Volúmenes** y seleccione **My Volumen** (Mi volumen).
    
27. En el menú **Acciones**, seleccione **Crear instantánea**.
    
28. Elija Agregar etiqueta, luego, configure lo siguiente:
    
    - **Clave:** `Name`
    - **Valor:** `My Snapshot`
    - Seleccione Crear instantánea

29. En el panel de navegación izquierdo, elija **Instantáneas**.
    
    Se mostrará la instantánea. Al principio, el estado será _Pendiente_, lo que significa que la instantánea se está creando. Después cambiará al estado _Completado_.
    
    Nota: Solo se copian en las instantáneas los bloques de almacenamiento en uso, por lo que los bloques vacíos no ocupan espacio de almacenamiento de instantáneas.
    
30. En su sesión de EC2 Instance Connect, elimine el archivo que creó en el volumen.
    
    sudo rm /mnt/data-store/file.txt
    
31. Verifique que el archivo se eliminó.
    
    ls /mnt/data-store/
    
    Se ha eliminado el archivo.
    

## Tarea 6: Restaurar la instantánea de Amazon EBS

Si alguna vez quiere recuperar datos almacenados en una instantánea, puede **restaurar** la instantánea en un volumen de EBS nuevo.

### Crear un volumen a partir de la instantánea

32. En la **consola de EC2**, seleccione **My Snapshot** (Mi instantánea).
    
33. En el menú **Acciones**, seleccione **Crear volumen a partir de una instantánea**.
    
34. En **Zona de disponibilidad**, seleccione la misma zona de disponibilidad que utilizó antes.
    
35. Elija Agregar etiqueta, luego, configure lo siguiente:
    
    - **Clave:** `Name`
    - **Valor:** `Restored Volume`
    - Seleccione Crear volumen
    
    **Nota**: Cuando se restaura una instantánea en un volumen nuevo, también se puede modificar la configuración, como el tipo de volumen, el tamaño o la zona de disponibilidad.
    

### Adjuntar el volumen restaurado a la instancia de EC2

36. En el panel de navegación izquierdo, seleccione **Volúmenes**.
    
37. Seleccione **Volumen restaurado**.
    
38. En el menú **Acciones**, seleccione **Asociar volumen**.
    
39. Haga clic en el campo **Instancia** y, a continuación, seleccione la instancia **Lab** (Laboratorio) que aparece.
    
    Observe que el campo **Dispositivo** está establecido en _/dev/sdg_. Utilizará este identificador de dispositivo en una tarea posterior.
    
40. Seleccione Asociar volumen
    
    El estado del volumen ahora será _In-use_ (En uso).
    

### Montar el volumen restaurado

41. Cree un directorio para montar el volumen de almacenamiento nuevo:
    
    sudo mkdir /mnt/data-store2
    
42. Monte el volumen nuevo:
    
    sudo mount /dev/sdg /mnt/data-store2
    
43. Compruebe que el volumen montado contenga el archivo que creó en los pasos anteriores.
    
    ls /mnt/data-store2/
    
    Debería ver un archivo .txt.
    

## Envío del trabajo

44. Para registrar su progreso, seleccione **Submit** (Enviar) en la parte superior de estas instrucciones.
    
45. Cuando se le solicite, seleccione **Yes** (Sí).
    
    Después de un par de minutos, aparece el panel de calificaciones y le muestra cuántos puntos obtuvo por cada tarea. Si los resultados no se muestran después de algunos minutos, seleccione **Grades** (Calificaciones) en la parte superior de estas instrucciones.
    
    **Sugerencia:** Puede enviar su trabajo varias veces. Después de modificar el trabajo, vuelva a seleccionar **Submit** (Enviar). Su último envío quedó registrado para este laboratorio.
    
46. Para obtener comentarios detallados sobre su trabajo, seleccione **Submission Report** (Informe de envío).
    
    **Sugerencia:** En los casos de las comprobaciones por las que no recibió todos los puntos, a veces, se indican detalles útiles en el informe de envío.
    

## Conclusión

¡Felicitaciones! Aprendió a realizar correctamente lo siguiente:

- Crear un volumen de Amazon EBS
    
- Adjuntar el volumen a una instancia de EC2
    
- Crear un sistema de archivos en el volumen
    
- Agregar un archivo al volumen
    
- Crear una instantánea del volumen
    
- Crear un volumen nuevo a partir de la instantánea
    
- Adjuntar el volumen nuevo a la instancia de EC2 y montarlo en ella
    
- Comprobar que el archivo que creó antes se encuentre en el volumen creado recientemente
    

## Laboratorio completado

¡Felicitaciones! Ha completado el laboratorio.

47. Seleccione End Lab (Finalizar laboratorio) en la parte superior de esta página y, a continuación, seleccione Yes (Sí) para confirmar que desea finalizar el laboratorio.  
    
    Aparecerá un panel en el que se indica: “DELETE has been initiated... You may close this message box now” (Se ha iniciado la ELIMINACIÓN… Ya puede cerrar este cuadro de mensaje).
    
48. Seleccione la **X** en la esquina superior derecha para cerrar el panel.
    

© 2023, Amazon Web Services, Inc. y sus filiales. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial.