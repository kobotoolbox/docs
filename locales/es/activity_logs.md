# Registros de actividad
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/d6f09be2d6f022db661e2a4d9da0b962db44633e/source/activity_logs.md" class="reference">15 de mayo de 2025</a>

Los registros de actividad son registros digitales que capturan acciones y eventos importantes en tu cuenta de KoboToolbox. Los registros de actividad te brindan un historial detallado del acceso a la cuenta y la actividad del proyecto.
Estos registros pueden ser útiles para:

-   Monitoreo de seguridad: Ver quién accedió a tu cuenta y desde dónde
-   Seguimiento de cambios: Saber cuándo se modificaron elementos del proyecto
-   Responsabilidad: Identificar qué miembros del equipo realizaron cambios específicos
-   Solución de problemas: Comprender cuándo y cómo pueden haber ocurrido problemas

KoboToolbox proporciona dos tipos de registros de actividad para ayudarte a monitorear diferentes aspectos de tu trabajo:

-   **Registros de acceso:** Apoyan la seguridad de la cuenta al mostrar todos los inicios de sesión.
-   **Registros de historial del proyecto:** Rastrean todas las acciones y cambios realizados por cualquier usuario/a dentro de un proyecto específico y sus datos.


<p class="note">
  <b>Nota:</b> Los registros de actividad son una adición relativamente reciente a KoboToolbox. Estamos trabajando activamente para expandir estas funcionalidades en los próximos meses y proporcionar un registro aún más detallado de las acciones en tus cuentas y proyectos.
</p>

## Registros de acceso

Los registros de acceso registran todos los eventos de autenticación (inicios de sesión) para tu cuenta de KoboToolbox. Te ayudan a monitorear la seguridad de la cuenta mostrándote cuándo y dónde se accedió a tu cuenta.

Se pueden encontrar bajo el título 'Actividad reciente de la cuenta', al cual puedes acceder fácilmente abriendo la Configuración de tu cuenta en la sección Seguridad.

Los registros de acceso muestran:

-   Fecha y hora de cada inicio de sesión
-   Dirección IP (información de ubicación)
-   Fuente (información del dispositivo y navegador)

![image](/images/activity_logs/Logs-image01.jpg)

Ten en cuenta que eventos similares (autenticaciones) que ocurran dentro de 60 minutos entre sí se agruparán juntos.

### Exportar registros de acceso

![image](images/activity_logs/Logs-image02.jpg)

Esta sección también te permite exportar todos tus registros de acceso haciendo clic en el botón 'Exportar datos de registro' en la esquina superior derecha de la tabla. Al hacer clic en este botón se activará el proceso de exportación de datos:
1. Comenzará el procesamiento de los registros en un archivo de exportación .csv
2. Se mostrará una ventana modal informándote que el proceso ha comenzado y cuáles son los siguientes pasos.
3. Recibirás un correo electrónico con un enlace para descargar el archivo una vez que esté listo. La cantidad de datos incluidos en tus registros determinará cuánto tiempo puede tomar recibir el correo electrónico.
4. Al hacer clic en la URL del correo electrónico debería comenzar inmediatamente la descarga del archivo .csv, dependiendo de la configuración de tu navegador.

El archivo de exportación incluirá información más detallada de todos los eventos de autenticación, incluyendo el tipo de autenticación y el momento exacto.

### Cerrar sesión en todos los dispositivos

Puedes forzar que todos los dispositivos que actualmente tienen sesión iniciada en tu cuenta cierren sesión inmediatamente haciendo clic en el enlace 'Cerrar sesión en todos los dispositivos' a la izquierda del botón de exportación de datos.

Esta acción también cerrará tu sesión actual.

## Registros de historial del proyecto

Los registros de historial del proyecto proporcionan un registro detallado de todas las actividades dentro de un proyecto específico. Muestran cada acción realizada, ya sea por usuarios/as o procesos automatizados, brindándote visibilidad completa del historial de tu proyecto.

Para ver los registros de un proyecto específico, ve a la ventana CONFIGURACIÓN de tu proyecto y dirígete a la sección Actividad.

![image](/images/activity_logs/Logs-image3.jpg)

En esta página encontrarás una vista de tabla con toda la actividad del proyecto, ordenada por fecha. Cada acción única se enumera junto con el/la usuario/a que la realizó y la marca de fecha asociada con esa actividad.

Los registros de historial del proyecto capturan casi todas las acciones posibles que se pueden realizar en un proyecto.

| Categoría                      | Acciones incluidas                                                                                                                                |
| :------------------------------| :-------------------------------------------------------------------------------------------------------------------------------------------------|
| Cambios del proyecto           | Actualizaciones del nombre del proyecto, Despliegues y redespliegues, Archivar y desarchivar, Conexiones del proyecto                            |
| Cambios del formulario         | Cargas de XLSForm, Ediciones del formulario, Creación de preguntas de análisis cualitativo                                                       |
| Cambios de manejo de datos     | Exportaciones de datos, Modificaciones de archivos adjuntos multimedia, Cambios en la configuración de compartir datos, Modificaciones de servicio REST |
| Permisos                       | Actualizaciones de acceso de usuarios/as, Configuración de acceso público, Transferencias de propiedad                                            |
| Envíos                         | El/la usuario/a modifica o elimina envíos. Agregar envíos se muestra en la exportación de registros, pero no en la interfaz de KoboToolbox       |

### Encontrar e investigar actividades específicas

Puedes filtrar el registro de historial por tipo de actividad (por ejemplo, despliegues, ediciones de formulario, cambios de permisos, etc.) usando la funcionalidad de alternancia en la esquina superior derecha. Esto también permitirá a los/as propietarios/as y administradores/as del proyecto rastrear cambios/actualizaciones en aspectos específicos del proyecto rápidamente.

![image](/images/activity_logs/Logs-GIF01.gif)

También puedes exportar todos los datos del historial de tu proyecto usando el botón de exportación en la esquina superior derecha de tu tabla.
Si necesitas más información sobre una actividad específica, simplemente haz clic en 'Ver detalles' para una vista ampliada de esa entrada. Esto mostrará toda la información sobre ese evento, revelando lo que ocurrió en el backend y cualquier metadato asociado.

## Problemas comunes con los registros de actividad

**"No veo actividades recientes"**
-   Verifica que estés viendo el proyecto correcto
-   Asegúrate de tener los permisos correctos para ver los registros. Solo los/as propietarios/as del proyecto y usuarios/as con permisos de 'administrar proyecto' pueden ver los registros.
-   Ten en cuenta que los registros solo están disponibles por un período de 60 días. Los registros más antiguos se eliminan y no son recuperables. Este período se puede configurar a nivel de administrador/a para organizaciones con un servidor privado.

**"Necesito datos de registro más antiguos"**
-   Los datos más allá del período de retención se eliminan automáticamente y no son recuperables. Si necesitas tener acceso a datos de registro de más de 60 días y estás usando un servidor privado, puedes contactar a tu administrador/a para aumentar el período de retención.

**"No puedo descargar el archivo de exportación de datos de registro"**
-   Cuando haces clic en el enlace que recibiste por correo electrónico para descargar el archivo de exportación de datos de registro, puede abrir una página web con texto en lugar de descargar el archivo csv.
-   Para descargar el archivo .csv desde la página web, haz clic derecho en la página y selecciona Guardar página como…. Mantén el formato como "Código fuente de la página"
-   Si haces clic en el enlace y obtienes un mensaje de error, como 403 Prohibido, intenta abrir el enlace con otro navegador (por ejemplo, Safari).

![image](/images/getting_started_organization_feature/organizations_project_views.gif)