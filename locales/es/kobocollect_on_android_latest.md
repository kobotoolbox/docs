# Configuración de la aplicación KoboCollect
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/kobocollect_on_android_latest.md" class="reference">23 abr 2026</a>


<iframe src="https://www.youtube.com/embed/qC2Bz8jZkIM?si=xSyTOxOMR6nE8tum&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect es una aplicación gratuita y de código abierto de KoboToolbox diseñada para la recolección de datos en dispositivos móviles Android. Sus capacidades sin conexión y su compatibilidad con la mayoría de los dispositivos Android la hacen ideal para el trabajo de campo.

Antes de usar KoboCollect, debes [crear una cuenta de KoboToolbox](https://support.kobotoolbox.org/es/creating_account.html) en el sitio web de KoboToolbox e [implementar formularios de recolección de datos](https://support.kobotoolbox.org/es/quick_start.html).

<p class="note">
 Este artículo explica cómo configurar KoboCollect en un dispositivo Android y conectarlo a una cuenta de KoboToolbox para la recolección de datos. Para obtener más información sobre la configuración de los ajustes de KoboCollect y la recolección de datos con la aplicación, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html">Personalizar la configuración de KoboCollect</a> y <a href="https://support.kobotoolbox.org/es/data_collection_kobocollect.html">Recolección de datos con KoboCollect</a>.
</p>

## Elegir un dispositivo para KoboCollect

KoboCollect funciona solo en **teléfonos y tabletas Android.** Al elegir un dispositivo, considera lo siguiente:

- Debe ejecutar una versión de Android compatible con KoboCollect. Las versiones más recientes de la aplicación requieren Android 8.0 o superior.
- Debe ser adecuado para tus condiciones de campo en términos de duración de la batería, tamaño de pantalla y durabilidad.
- Debe tener suficiente almacenamiento para tus formularios y envíos, especialmente si recolectas fotos, audio, video o almacenas muchos envíos sin conexión antes de cargarlos.
- Debe tener el hardware que requiere tu formulario, como GPS o cámara.
- Debe poder conectarse de manera confiable a Wi-Fi o datos móviles para que los formularios y envíos se puedan descargar y cargar según sea necesario.

En general, los teléfonos pueden ser mejores para la portabilidad, mientras que las tabletas pueden ser mejores para cuestionarios más largos o flujos de trabajo más complejos.

<p class="note">
<strong>Nota:</strong>
No existe una lista exhaustiva de dispositivos compatibles para usar KoboCollect. Sin embargo, existe una <a href="https://github.com/getodk/collect#test-devices">lista oficial de dispositivos</a> en los que se prueba la aplicación, que son las opciones más confiables.
</p>

## Instalar la aplicación KoboCollect

La aplicación KoboCollect se puede descargar desde [Google Play Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android). Te recomendamos usar siempre la última versión de la aplicación, ya que incluye funcionalidades y correcciones de errores que no están disponibles en versiones anteriores.

<p class="note">
<strong>Nota:</strong>
Aunque KoboCollect sigue funcionando en cualquier teléfono o tableta Android con Android 5.1 o superior, ahora se requiere Android 8.0 o superior para obtener las versiones más recientes de la aplicación. La última versión disponible para dispositivos más antiguos seguirá estando disponible en Play Store y en <a href="https://github.com/kobotoolbox/collect/releases">GitHub</a>.
</p>

## Configurar la aplicación KoboCollect

Para recolectar datos con KoboCollect, debes configurar la aplicación KoboCollect en tu dispositivo móvil para conectarte al servidor de KoboToolbox. Esto te permite descargar formularios implementados desde KoboToolbox y enviar los datos recolectados de vuelta al servidor.

Para conectar KoboCollect al servidor de KoboToolbox, necesitarás tu **URL de KoboCollect**, tu **nombre de usuario** y tu **contraseña**. Después de la configuración manual inicial, puedes [generar un código QR](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) para configurar otros dispositivos.

<p class="note">
    <strong>Nota:</strong> En la aplicación KoboCollect, las cuentas de usuario se llaman <strong>Proyectos</strong>.
</p>

### Configurar KoboCollect manualmente
Para configurar KoboCollect manualmente, necesitarás identificar tu **URL de KoboCollect**. Esta URL es específica de KoboCollect y difiere de la URL utilizada para acceder a tu cuenta de KoboToolbox.

Tu URL de KoboCollect depende del servidor de tu cuenta:

| **Servidor de KoboToolbox**    | **URL de KoboCollect**                     |
| :----------------- | :--------------------------------------------- |
| Servidor Global               | https://kc.kobotoolbox.org/ |
| Servidor con sede en la Unión Europea      | https://kc-eu.kobotoolbox.org/ |
| Servidor Privado           | Único para cada organización            |

También puedes encontrar la URL de KoboCollect en la plataforma de KoboToolbox. Ve a la ventana **FORMULARIO** de tu proyecto y selecciona **Aplicación Android** en el menú desplegable **Recolectar datos**. La URL de KoboCollect se mostrará en el paso 3.

![Select Android app in browser](images/kobocollect_on_android_latest/select_android_app_in_browser.png)

Una vez que hayas identificado tu URL de KoboCollect, sigue estos pasos para configurar la conexión al servidor:

1. Abre la aplicación KoboCollect.
2. Selecciona **Entrar los detalles del proyecto manualmente**.
3. Ingresa la **URL de KoboCollect**, tu **nombre de usuario** y **contraseña**.
4. Haz clic en **Agregar**.
5. Cuando se complete la configuración, se mostrará el menú principal.

### Configurar KoboCollect con un código QR

Usar un código QR configura eficientemente KoboCollect en múltiples dispositivos con la **misma configuración de servidor** (URL de KoboCollect, nombre de usuario, contraseña y <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html">configuraciones del proyecto</a>). Esto puede ser útil para evitar repetir pasos manuales o para configurar dispositivos de encuestadores sin compartir contraseñas de cuenta.

<p class="note">
    <strong>Nota:</strong> Para usar el método del código QR, primero debes configurar manualmente un dispositivo y luego copiar el código QR generado a los otros dispositivos.
</p>

Para acceder a tu código QR:

1. Ve al menú **Proyecto** y selecciona el proyecto que deseas copiar.
2. Haz clic en **Ajustes**.
3. Selecciona **Manejo de formularios**.
4. Haz clic en **Volver a configurar**.
5. Elige **Código QR**. Tu código QR aparecerá en la pantalla.
6. **Toma una captura de pantalla** del código QR para compartirlo y configurar otros dispositivos. También puedes volver a este menú en cualquier momento para acceder al código QR nuevamente.

Para configurar otros dispositivos usando el código QR:

1. Abre **KoboCollect** en el dispositivo que deseas configurar.
2. Haz clic en **Configurar con código QR**.
3. Escanea un código QR con la cámara del dispositivo, o haz clic en los <i class="k-icon-more"></i> **tres puntos** en la esquina superior derecha y selecciona **Importar código QR** para usar una captura de pantalla guardada en tu dispositivo.

Si la configuración es exitosa, la aplicación se configurará automáticamente.

<p class="note">
    <strong>Nota:</strong> El código QR contiene las credenciales de tu cuenta, incluida tu contraseña. Cualquier persona que lo escanee tendrá los mismos permisos de acceso que la cuenta desde la que se generó. Si solo deseas que alguien recolecte datos (por ejemplo, un encuestador), <strong>asegúrate de que la cuenta utilizada para generar el código QR no tenga permisos para ver, editar o eliminar datos.</strong> Para mantener tus datos seguros, evita compartir códigos QR de cuentas con acceso completo.
</p>

### Configurar múltiples proyectos en KoboCollect

Los usuarios pueden conectar múltiples cuentas de KoboToolbox y cambiar fácilmente entre diferentes proyectos dentro de la misma aplicación KoboCollect, independientemente de si están en el mismo servidor o en servidores diferentes.

Para configurar proyectos adicionales en KoboCollect:

1. Haz clic en el **ícono de Proyecto** ubicado en la esquina superior derecha.
2. En el menú **Proyecto**, haz clic en **Agregar proyecto**.
3. Configura un nuevo proyecto usando el método manual o escaneando un código QR.
4. Cuando se complete la configuración, se mostrará el menú principal.
5. Haz clic en el **ícono de Proyecto** para abrir el menú. Ambos proyectos ahora deberían ser visibles.

Se pueden agregar proyectos adicionales repitiendo el mismo proceso. El proyecto activo se mostrará primero en el menú **Proyecto**. Para cambiar a un proyecto diferente, simplemente haz clic en su ícono.

<p class="note">
    Para obtener más información sobre cómo cambiar la forma en que se muestran los proyectos para facilitar el reconocimiento y el cambio, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#project-display-settings">Configuración de visualización del proyecto</a>.
</p>

### Configurar un proyecto en KoboCollect sin autenticación

También es posible acceder a proyectos en KoboCollect sin contraseña. Esto es útil para proyectos con muchos encuestadores, ya que evita la necesidad de crear cuentas individuales o compartir credenciales.

<p class="note">
    <strong>Nota:</strong> Este método requiere habilitar "Permitir envíos a este formulario sin nombre de usuario ni contraseña" para tus formularios. Para obtener más información sobre la configuración de uso compartido a nivel de proyecto, consulta <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html">Compartir proyectos con configuraciones a nivel de proyecto</a>.
</p>

Para conectarte a KoboCollect sin autenticación:
1. Habilita "Permitir envíos a este formulario sin nombre de usuario ni contraseña" para tus formularios.
2. [Opcional] Crea una cuenta de KoboToolbox dedicada para los recolectores de datos y [comparte tus formularios](https://support.kobotoolbox.org/es/managing_permissions.html) con esta cuenta.
3. Conéctate a KoboCollect usando las siguientes credenciales:
    - **URL**: URL de KoboCollect seguida del nombre de usuario de la cuenta (`https://[kobocollect_url]/[username]`)
    - **Nombre de usuario**: (Dejar en blanco)
    - **Contraseña**: (Dejar en blanco)

Este método permite a los usuarios descargar y enviar datos a cualquier formulario compartido con `username` que no [requiera autenticación](https://support.kobotoolbox.org/es/project_sharing_settings.html).

Para diferenciar a los encuestadores y rastrear los envíos, puedes pedirles que ingresen un nombre de usuario personalizado, número de teléfono y dirección de correo electrónico en la [configuración de identidad del usuario y del dispositivo](https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings).

<p class="note">
    <strong>Nota:</strong> Este método puede ser útil cuando tu cuenta usa <a href="https://support.kobotoolbox.org/es/two_factor_authentication.html">autenticación de dos factores</a>, ya que no podrás descargar formularios ni enviar datos usando el método normal.
</p>