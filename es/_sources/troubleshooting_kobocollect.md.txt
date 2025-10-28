# Solución de problemas de la aplicación de Android de KoboCollect
<a href="../troubleshooting_kobocollect.html">Read in English</a> | <a href="../fr/troubleshooting_kobocollect.html">Lire en français</a> | <a href="../ar/troubleshooting_kobocollect.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/f6c6ac34b1fe55e7aab87f7b61c26e1607b4306b/source/troubleshooting_kobocollect.md" class="reference">24 Sep 2025</a>

**-- Por favor, informa cualquier problema no cubierto en nuestro
[Foro de la comunidad](https://community.kobotoolbox.org/)--**

<p class="note">
    Para obtener más información sobre cómo conectar KoboCollect a tu cuenta de KoboToolbox, configurar los ajustes de KoboCollect y recolectar datos con la aplicación, consulta <a href="kobocollect_on_android_latest.html">Primeros pasos con KoboCollect</a>, <a href="kobocollect_settings.html">Personalizar los ajustes de KoboCollect</a> y <a href="data_collection_kobocollect.html">Recolección de datos usando KoboCollect</a>.
</p>


_Mensajes de error comunes con guías de solución de problemas:_

**Error: Mensaje 'Error al obtener la lista de formularios' después de seleccionar 'Descargar formulario'**

**Solución de problemas:** Las soluciones más probables para este problema son:

1. Verifica tu URL, es muy probable que tengas un pequeño error tipográfico en la URL que ingresaste en
   los ajustes. Consulta [este artículo](kobocollect_on_android_latest.md) sobre cómo configurar
   tu teléfono/tableta Android para la recolección de datos.

2. Otra posible explicación es que tu teléfono no estaba conectado a
   Internet cuando seleccionaste **Descargar formulario**, por ejemplo, cuando estás
   conectado/a a una red WiFi en un lugar público que requiere que inicies sesión
   a través de tu navegador. [Este artículo](kobocollect_on_android_latest.md) explica con
   mayor detalle cómo conectar tu dispositivo con tu cuenta.

**Error: Excepción genérica: No hay certificado de par o La lista de formularios falló. Error:
javx.net.ssl.SSLPeerUnverifiedException...**

Este error aparece cuando KoboCollect intenta comunicarse con el servidor pero
no puede establecer una conexión segura (SSL/HTTPS).

**Solución de problemas:**

1. Es muy probable que tu dispositivo esté usando la fecha incorrecta. Verifica que la fecha sea
   correcta y luego intenta nuevamente. _Por favor, consulta el manual de tu teléfono/tableta sobre cómo
   configurar la fecha._ Los dispositivos Android restablecen sus fechas a 2000 u otro año si
   la batería llega a 0%, por lo que este error puede aparecer con frecuencia si
   tu equipo tiene la tendencia de agotar completamente la batería.

2. También puedes ver este mensaje de error si estás usando un punto de acceso WiFi que
   requiere que inicies sesión después de conectarte.

**Error: KoboCollect se ha cerrado inesperadamente**

**Solución de problemas:**

1. Si esto **ocurre** mientras intentas **cargar envíos o descargar un
   nuevo formulario**, entonces tu dispositivo tiene una interrupción significativa en su conexión a
   Internet. Aunque suena alarmante, es inofensivo: Simplemente repite el
   proceso de carga o descarga.

2. Si esto **ocurre** mientras intentas **abrir un nuevo formulario** en tu teléfono,
   entonces las siguientes posibles razones podrían ayudarte a resolver:

    - El formulario que estás intentando abrir tiene errores en los cálculos,
      restricciones o rutinas de salto. Esto es raro ya que el sistema ya habría
      verificado los errores.
    - El formulario que estás intentando abrir es demasiado grande o tiene numerosas
      acciones (cálculos, lista grande de respuestas u otros procedimientos complejos) que no pueden ser manejados por la capacidad de memoria de tu dispositivo.
      Por favor, consulta [este artículo](devices_for_data_collection.md) sobre
      dispositivos recomendados.

**Error: No se puede editar este formulario en blanco porque el formulario en blanco correspondiente no
está presente o fue eliminado**

**Solución de problemas:**

Este tipo de mensaje de error ocurre cuando intentas editar tu formulario guardado cuando el
formulario en blanco correspondiente no está presente o fue eliminado.

Si esto ocurre, recupera el formulario en blanco correspondiente de tu cuenta de KoboToolbox
haciendo clic en **Descargar formulario** en la pantalla de inicio y luego selecciona el
formulario particular que requiere modificaciones.

**Error: No se puede instalar la aplicación de Android de KoboCollect en un dispositivo. Muestra el
siguiente mensaje de error (no se puede crear el directorio/storage/sdcard0/odk)**

**Solución de problemas:**

Ves este mensaje de error cuando tu dispositivo no tiene espacio de almacenamiento. Para superar
este problema, libera espacio en tu dispositivo desinstalando alguna aplicación innecesaria y luego intenta
instalar KoboCollect.