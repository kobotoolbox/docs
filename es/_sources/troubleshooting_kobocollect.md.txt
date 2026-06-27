# Solución de problemas de la aplicación Android KoboCollect

**-- Por favor, reporta cualquier problema no cubierto en nuestro
[foro de la comunidad](https://community.kobotoolbox.org/)--**

<p class="note">
    Para obtener más información sobre cómo conectar KoboCollect a tu cuenta de KoboToolbox, configurar los ajustes de KoboCollect y recolectar datos con la aplicación, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html">Configuración de la aplicación KoboCollect</a>, <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html">Personalizar la configuración de KoboCollect</a> y <a href="https://support.kobotoolbox.org/es/data_collection_kobocollect.html">Recolección de datos con KoboCollect</a>.
</p>

_Mensajes de error frecuentes con guías de solución de problemas:_

**Error: Mensaje 'Error getting form list' al seleccionar 'Download form'**

**Solución:** Las soluciones más probables para este problema son:

1. Verifica tu URL; es probable que hayas cometido un pequeño error tipográfico en la URL que ingresaste en los ajustes. Consulta [este artículo](kobocollect_on_android_latest.md) sobre cómo configurar tu teléfono o tablet Android para la recolección de datos.

2. Otra posible explicación es que tu teléfono no estaba conectado a Internet cuando seleccionaste **Download form**, por ejemplo, cuando estás conectado a una red WiFi en un lugar público que requiere que inicies sesión a través de tu navegador. [Este artículo](kobocollect_on_android_latest.md) explica con más detalle cómo conectar tu dispositivo con tu cuenta.

**Error: Generic Exception: No peer certificate o Form listing failed. Error:
javx.net.ssl.SSLPeerUnverifiedException...**

Este error aparece cuando KoboCollect intenta comunicarse con el servidor pero no puede establecer una conexión segura (SSL/HTTPS).

**Solución:**

1. Es muy probable que tu dispositivo esté usando una fecha incorrecta. Verifica que la fecha sea correcta y vuelve a intentarlo. _Consulta el manual de tu teléfono o tablet para saber cómo configurar la fecha._ Los dispositivos Android restablecen su fecha al año 2000 u otro año si la batería llega al 0%, razón por la cual este error puede aparecer con frecuencia si tu equipo tiene tendencia a agotar la batería por completo.

2. También puedes ver este mensaje de error si estás usando un punto de acceso WiFi que requiere que inicies sesión después de conectarte.

**Error: KoboCollect ha fallado**

**Solución:**

1. Si esto **ocurre** mientras intentas **cargar envíos o descargar un nuevo formulario**, tu dispositivo tiene una interrupción significativa en su conexión a Internet. Aunque puede parecer alarmante, no es grave: simplemente repite el proceso de carga o descarga.

2. Si esto **ocurre** mientras intentas **abrir un nuevo formulario** en tu teléfono, las siguientes posibles causas pueden ayudarte a resolver el problema:

    - El formulario que intentas abrir tiene errores en los cálculos, restricciones o rutinas de omisión. Esto es poco frecuente, ya que el sistema ya habría detectado los errores.
    - El formulario que intentas abrir es demasiado grande o tiene numerosas acciones (cálculos, listas extensas de respuestas u otros procedimientos complejos) que la memoria de tu dispositivo no puede gestionar. Consulta [este artículo](devices_for_data_collection.md) sobre los dispositivos recomendados.

**Error: Unable to edit this blank form because the corresponding blank form is not present or was deleted**

**Solución:**

Este tipo de mensaje de error ocurre cuando intentas editar tu formulario guardado y el formulario en blanco correspondiente no está presente o fue eliminado.

Si esto ocurre, recupera el formulario en blanco correspondiente desde tu cuenta de KoboToolbox haciendo clic en **Download form** en la pantalla de inicio y luego selecciona el formulario específico que requiere modificaciones.

**Error: Unable to install KoboCollect android app in a device. Shows the following error message (can't create directory/storage/sdcard0/odk)**

**Solución:**

Ves este mensaje de error cuando tu dispositivo no tiene espacio de almacenamiento disponible. Para solucionar este problema, libera espacio en tu dispositivo desinstalando algunas aplicaciones innecesarias y luego intenta instalar KoboCollect nuevamente.