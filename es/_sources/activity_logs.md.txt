# Seguimiento a la actividad del proyecto y de la cuenta

**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/3bd66258a8d08aa1daafa90640a1fc8e4efe3b23/source/activity_logs.md" class="reference">16 Dic 2025</a>

En KoboToolbox, puedes monitorear la actividad del proyecto y de la cuenta usando **registros de actividad.** Estos registros guardan las acciones y eventos clave en tu cuenta o proyectos, proporcionando un historial detallado de acceso y actividad.

Los registros de actividad pueden ser útiles para:

-   **Monitoreo de seguridad:** Ver quién accedió a tu cuenta y desde dónde.
-   **Seguimiento de cambios:** Saber cuándo se modificaron elementos del proyecto.
-   **Responsabilidad:** Identificar qué miembros del equipo hicieron cambios específicos.
-   **Solución de problemas:** Entender cuándo y cómo pueden haber ocurrido problemas.

KoboToolbox proporciona dos tipos de registros de actividad para ayudarte a monitorear diferentes aspectos de tu trabajo:

-   **Registros de acceso a la cuenta:** Muestran todos los inicios de sesión en tu cuenta.
-   **Registros del historial del proyecto:** Rastrean todas las acciones y cambios realizados por cualquier usuario dentro de un proyecto y sus datos.

## Registros de acceso a la cuenta

Los registros de acceso a la cuenta guardan todos los eventos de autenticación (inicios de sesión) de tu cuenta de KoboToolbox. Te ayudan a monitorear la seguridad de la cuenta mostrándote cuándo y dónde se accedió a tu cuenta.

Para acceder a tus registros de acceso a la cuenta:

1. [Inicia sesión](https://www.kobotoolbox.org/sign-up/) en tu cuenta de KoboToolbox.
2. Haz clic en el ícono de tu perfil en la esquina superior derecha.
3. Haz clic en **Configuraciones de la cuenta** y ve a la ventana **Seguridad**.
4. Encuentra tus registros de acceso a la cuenta en **ACTIVIDAD RECIENTE DE LA CUENTA.**

Los registros de acceso muestran la siguiente información:

-   Fecha y hora de cada inicio de sesión
-   Dirección IP (información de ubicación)
-   Fuente (información del dispositivo y navegador)

![Registros de actividad de acceso en la ventana de seguridad](/images/activity_logs/access_logs.png)

<p class="note">
    <strong>Nota:</strong> Las autenticaciones similares que ocurran dentro de 60 minutos entre sí se agruparán juntas.
</p>

### Exportar registros de acceso a la cuenta

Desde la sección **ACTIVIDAD RECIENTE DE LA CUENTA** en **Configuraciones de la cuenta > Seguridad**, también puedes exportar todos los registros de acceso. Para hacerlo:

1. Haz clic en <i class="k-icon-download"></i> **Exportar datos de actividad** en la esquina superior derecha de la tabla. Esto activará el proceso de exportación de datos.
2. Una vez que el proceso esté completo, recibirás un correo electrónico con un enlace para descargar el archivo.
    - El tiempo que toma recibir el correo electrónico depende del tamaño de los datos de actividad.
3. Al hacer clic en la URL del correo electrónico se inicia la descarga del archivo CSV o [se abre una nueva página web](https://support.kobotoolbox.org/es/activity_logs.html#troubleshooting), dependiendo de la configuración de tu navegador.

<p class="note">
    <strong>Nota:</strong> El archivo exportado incluye información más detallada sobre los eventos de autenticación, incluyendo el tipo de autenticación y el momento exacto.
</p>

### Cerrar sesión en todos los dispositivos

Finalmente, desde la sección **ACTIVIDAD RECIENTE DE LA CUENTA** en **Configuraciones de la cuenta > Seguridad**, puedes forzar a todos los dispositivos actualmente conectados a tu cuenta a cerrar sesión inmediatamente. Para hacerlo:

1. Haz clic en <i class="k-icon-logout"></i> **Cerrar sesión en todos los dispositivos** en la esquina superior derecha de la tabla.
2. Cerrarás sesión de tu sesión actual inmediatamente. Cualquier otro dispositivo que haya iniciado sesión en tu cuenta también cerrará sesión.

## Registros del historial del proyecto

Los registros del historial del proyecto proporcionan un registro detallado de todas las acciones dentro de un proyecto. Muestran cada cambio realizado por usuarios o procesos automatizados, dándote visibilidad completa de la actividad del proyecto.

<p class="note">
    <strong>Nota:</strong> Solo los propietarios del proyecto y los usuarios con permisos de <strong>Gestionar el proyecto</strong> pueden ver los registros del historial del proyecto.
</p>

Para acceder a los registros del historial de tu proyecto:

1. Abre un proyecto y ve a la página **CONFIGURACIONES**.
2. Ve a la ventana **Actividad**.
3. Se mostrará una tabla con toda la actividad del proyecto, ordenada por fecha. Cada acción se lista con el nombre de usuario de la persona que la realizó y la marca de tiempo de cuándo ocurrió.

Si necesitas más información sobre una actividad, haz clic en **Ver detalles** para una vista expandida. Esto muestra toda la información disponible sobre el evento, incluyendo acciones del backend y metadatos asociados.

![Pantalla de actividad reciente del proyecto](images/activity_logs/Logs-image3.jpg)

Las siguientes acciones se capturan en los registros del historial del proyecto:

| Categoría                | Acciones                                                                                                           |
| :-----------------------| :---------------------------------------------------------------------------------------------------------------------------|
| Proyecto         | Cambios de nombre del proyecto, implementación y reimplementación, archivar y desarchivar, actualizaciones de servicios REST y conexiones de proyectos.                        |
| Formulario            | Ediciones de formularios, cargas de XLSForm, creación de <a href="https://support.kobotoolbox.org/es/qualitative_analysis.html">preguntas de análisis cualitativo</a>.                                                     |
| Datos | Exportaciones de datos, cambios de archivos multimedia, eliminación o modificación de envíos.                     |
| Permisos           | Cambios en el acceso de usuarios o configuraciones de acceso público, transferencias de propiedad.           |

<p class="note">
    <strong>Nota:</strong> Añadir envíos aparece en los registros exportados, pero no en la interfaz de KoboToolbox.
</p>

### Filtrar registros del historial del proyecto

Puedes filtrar el registro del historial del proyecto por acción para ver rápidamente actualizaciones de partes específicas del proyecto.

Para filtrar tus registros del historial del proyecto:

1. En la página **CONFIGURACIONES > Actividad** del proyecto, haz clic en **Filtrar por** encima de la tabla de registros del historial del proyecto.
2. Del menú desplegable, selecciona una acción para filtrar la tabla.

### Exportar registros del historial del proyecto

Desde la página **CONFIGURACIONES > Actividad** del proyecto, también puedes exportar todos los registros del historial del proyecto. Para hacerlo:

1. Haz clic en <i class="k-icon-download"></i> **Exportar todos los datos** en la esquina superior derecha de la tabla. Al hacer clic en este botón se activará el proceso de exportación de datos.
2. Una vez que el proceso esté completo, recibirás un correo electrónico con un enlace para descargar el archivo.
    - El tiempo que toma recibir el correo electrónico depende del tamaño de los datos de actividad.
3. Al hacer clic en la URL del correo electrónico se inicia la descarga del archivo CSV o [se abre una nueva página web](https://support.kobotoolbox.org/es/activity_logs.html#troubleshooting), dependiendo de la configuración de tu navegador.

## Solución de problemas

<details>
  <summary><strong>Actividades recientes no mostradas</strong></summary>
  Si las actividades recientes no se muestran, verifica lo siguiente:
    <br><br>
    <ul>
        <li>Estás viendo el proyecto correcto.</li>
        <li>Tienes los permisos correctos para ver los registros del historial del proyecto (es decir, propietario del proyecto o permisos de <strong>Gestionar el proyecto</strong>).</li>
    </ul>
</details>

<br>

<details>
  <summary><strong>Registros de actividad antiguos no disponibles</strong></summary>
  Los registros se conservan por un período limitado antes de que se eliminen automáticamente y no puedan recuperarse.
    <br><br>
El período de retención puede ajustarse a nivel de administrador para organizaciones que usan un servidor privado. Si necesitas acceso a datos de actividad más antiguos en un <a href="https://www.kobotoolbox.org/enterprise/#comparison-table">servidor privado</a>, contacta a tu administrador para solicitar un período de retención más largo.
</details>

<br>

<details>
  <summary><strong>El archivo de exportación de datos de actividad se abre como una página web</strong></summary>
  Cuando haces clic en el enlace recibido por correo electrónico para descargar un archivo de exportación de datos de actividad, puede abrir una página web con texto en lugar de descargar el archivo csv.
    <br><br>
    Para descargar el archivo .csv desde la página web:
    <br><br>
    <ol>
<li>Haz clic derecho en la página y selecciona <strong>Guardar página como…</strong>.</li>
<li>Mantén el formato como <strong>Código fuente de la página</strong> y guarda el archivo en la ubicación de tu elección.</li>
</ol>
</details>

<br>

<details>
  <summary><strong>Mensaje de error al hacer clic en el enlace de exportación</strong></summary>
  Si haces clic en el enlace y ves un mensaje de error como 403 Prohibido o 404 Página no encontrada, intenta abrir el enlace en un navegador diferente (por ejemplo, Safari). El enlace de exportación también puede haber expirado. Si es así, reinicia el proceso de exportación para generar un nuevo enlace.
</details>