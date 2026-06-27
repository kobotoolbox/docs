# Agregar metadatos en el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/form_meta.md" class="reference">23 Apr 2026</a>

Las preguntas de metadatos recopilan automáticamente información sobre el proceso de recolección de datos, como la fecha, la hora y el dispositivo utilizado, sin requerir ninguna respuesta de los encuestados. También puedes grabar audio en segundo plano durante la recolección de datos.

Las preguntas de metadatos están **ocultas para los encuestados**, y **los campos de metadatos no se pueden editar** en la tabla de datos de KoboToolbox. Esta información de fondo sirve para la auditoría, ayuda a mantener la integridad de los datos y puede utilizarse en el análisis de datos.

Este artículo explica cómo agregar y gestionar preguntas de metadatos en el Formbuilder, describe las opciones de metadatos disponibles e indica cómo el registro de auditoría y la grabación de audio en segundo plano pueden contribuir a la calidad de los datos y al monitoreo durante la recolección de datos.

## Agregar preguntas de metadatos en el Formbuilder

Para agregar preguntas de metadatos en el Formbuilder:

1. Haz clic en <i class="k-icon-settings"></i> **Diseño y configuración** en la esquina superior derecha de la pantalla.
2. En la sección **Metadatos**, selecciona las preguntas de metadatos que deseas incluir en tu formulario.

![Metadatos del formulario](images/question_types/access.png)

Las preguntas de metadatos disponibles en el Formbuilder son:

| Metadatos | Descripción |
|:---|:---|
| start time | Registra la fecha y hora exactas en que se inicia un envío. |
| end time | Registra la fecha y hora en que se finaliza un envío. |
| today | Registra la fecha del envío. |
| audit | Captura un [registro detallado](https://support.kobotoolbox.org/es/form_meta.html#audit-metadata-question) del proceso de entrevista, incluyendo la hora de inicio, la hora de finalización, la ubicación y las acciones del usuario durante todo el proceso de recolección de datos. Esta pregunta de metadatos no es compatible con los formularios web. |
| username | En KoboCollect, registra el nombre de usuario guardado en la <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings">configuración de la aplicación KoboCollect</a>. Si no se ha configurado ningún nombre de usuario, registra el utilizado para iniciar sesión en el servidor.<br>Al usar formularios web, el nombre de usuario de la cuenta solo se registra si se <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requiere autenticación</a>.<br><br><strong>Nota:</strong> Dado que el campo <code>username</code> puede editarse en KoboCollect, es posible que no coincida con la cuenta utilizada para autenticarse en el servidor. Para ver qué cuenta envió los datos, consulta el campo generado por el sistema <code>_submitted_by</code>. |
| phone number | Registra el número de teléfono almacenado en la <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings">configuración de la aplicación KoboCollect</a>. Esta pregunta de metadatos no es compatible con los formularios web. |
| device id | Registra la identificación única del dispositivo o navegador utilizado para recolectar datos. El ID del dispositivo se genera automáticamente y los usuarios no pueden modificarlo.<br><br><strong>Nota:</strong> En KoboCollect, el ID del dispositivo se actualiza cada vez que se reinstala la aplicación en un dispositivo. En los formularios web, el <code>deviceid</code> se restablece cada vez que se utiliza una nueva ventana del navegador. |
| start geopoint early | Captura las coordenadas GPS cuando se abre el formulario por primera vez. Puede utilizarse para activar el GPS del dispositivo con anticipación, de modo que las preguntas GPS posteriores puedan obtener lecturas precisas más rápidamente. |

<p class="note">
<strong>Nota:</strong> Los metadatos del formulario son diferentes de los <a href="https://support.kobotoolbox.org/es/viewing_validating_data.html#system-generated-submission-fields">campos de envío generados por el sistema</a>. Los metadatos del formulario deben habilitarse durante el desarrollo del formulario para que se recopilen, mientras que los campos generados por el sistema se agregan automáticamente a cada envío.
</p>

## Pregunta de metadatos de auditoría

La pregunta de metadatos de auditoría registra un registro detallado del proceso de entrevista mientras se completa un formulario en la [aplicación Android KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html). Captura información como cuándo se abrió y guardó el formulario, qué preguntas se visualizaron, cuánto tiempo pasaron los encuestados en cada pantalla y otras acciones del usuario durante la recolección de datos.

El registro de auditoría puede ayudar a:

- Monitorear el comportamiento de los encuestadores
- Identificar las preguntas que tardan más en responderse
- Entender cómo los encuestadores navegan por un formulario
- Apoyar los procesos de aseguramiento de la calidad de los datos y de validación

Los registros de auditoría se guardan como archivos CSV y se cargan con cada envío. Estos archivos pueden descargarse como archivos adjuntos multimedia y analizarse por separado. Dado que los registros utilizan datos de marca de tiempo, generalmente se requiere un procesamiento adicional para el análisis.

<p class="note">
    Para más información sobre los archivos CSV exportados, consulta la <a href="https://docs.getodk.org/form-audit-log/">documentación completa de registro de auditoría de ODK</a>.
</p>

La pregunta de metadatos de auditoría no es compatible con los [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html).

### Configuración de auditoría

Se pueden configurar ajustes opcionales adicionales para la pregunta de metadatos de auditoría. Estos incluyen:

- Agregar la ubicación GPS de los eventos
- Habilitar el seguimiento de cambios para registrar las respuestas que se modifican después de guardar un formulario y antes de enviarlo
- Solicitar a los encuestadores que indiquen el motivo de la edición de un formulario guardado
- Requerir que los encuestadores ingresen tu nombre de usuario antes de completar o editar un formulario

Los ajustes disponibles se enumeran en la [documentación de registro de auditoría de ODK](https://docs.getodk.org/form-audit-log/) como parámetros. En el Formbuilder, ingresa los parámetros opcionales directamente en el cuadro de texto **Configuración de auditoría**.

![Configuración de auditoría](images/question_types/audit_settings.png)

## Habilitar la grabación de audio en segundo plano

La grabación de audio en segundo plano te permite capturar una grabación de audio mientras un formulario está abierto y siendo completado. La grabación se guarda como parte del envío del formulario y puede [descargarse posteriormente como archivo de audio](https://support.kobotoolbox.org/es/managing_media_responses.html#downloading-media-files).

<p class="note">
<strong>Nota:</strong> Antes de usar esta función, asegúrate de que tu dispositivo tenga suficiente espacio de almacenamiento para los archivos de audio. También debes obtener el <strong>consentimiento informado</strong> de los encuestados antes de grabar. Ten siempre en cuenta las implicaciones éticas y cumple con las leyes de protección de datos aplicables en tu área de trabajo.
</p>

Para habilitar la grabación de audio en segundo plano en el Formbuilder:

1. Abre el panel **Diseño y configuración**.
3. En la sección **Audio de fondo**, haz clic en "Activar la grabación de sonido de fondo."
    - Una vez habilitado, el texto del botón cambiará a "Esta encuesta se grabará."
4. Si es necesario, cambia la calidad del audio en el menú desplegable **Calidad del audio**.
    - Para una descripción general de los ajustes de calidad de audio, consulta [Configurar la calidad del audio](#configuring-audio-quality). **Solo voz** es la calidad de audio predeterminada y más baja.
5. Una vez habilitado, el audio se grabará en segundo plano tanto en KoboCollect como en los formularios web mientras se completa el formulario.

![Habilitar audio de fondo](images/recording_interviews/background_audio.png)

<p class="note">
Para más información, consulta <a href="https://support.kobotoolbox.org/es/recording-interviews.html#recording-interviews-with-background-audio-recordings">Recolectar datos cualitativos con KoboToolbox</a>.
</p>

### Configurar la calidad del audio

La calidad del audio afecta el tamaño del archivo que se almacena en el servidor. Los usuarios del [Community Plan](https://www.kobotoolbox.org/pricing/) tienen un límite de 1 GB de almacenamiento de archivos gratuito. Por lo tanto, es recomendable gestionar el tamaño de los archivos de audio que recolectas eligiendo un ajuste de calidad adecuado. La tabla a continuación ofrece una descripción general de los ajustes de calidad de audio y los tamaños de archivo correspondientes.

| Calidad      | Extensión | Codificación | Tasa de bits | Frecuencia de muestreo | Tamaño del archivo |
|:------------ |:---------|:------------|:-------------|:-----------------------|:------------------|
| Normal       | .m4a     | AAC         | 64 kbps      | 32 kHz                 | ~ 30 MB/hora      |
| Baja         | .m4a     | AAC         | 24 kbps      | 32 kHz                 | ~ 11 MB/hora      |
| Solo voz     | .amr     | AMR         | 12.2 kbps    | 8 kHz                  | ~ 5 MB/hora       |

El ajuste predeterminado **Solo voz** es adecuado para entrevistas en entornos tranquilos. Para grabaciones con varios hablantes o algo de ruido de fondo, el ajuste de calidad **Baja** es más apropiado. El ajuste **Normal** ofrece la mayor calidad de audio, pero utiliza más espacio de almacenamiento.

## Configurar metadatos en KoboCollect

El número de teléfono y el nombre de usuario predeterminados del usuario pueden [configurarse](https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings) y modificarse en la aplicación KoboCollect.

Para configurar los metadatos del usuario en KoboCollect:

1. Abre la aplicación KoboCollect.
2. Toca el **ícono del proyecto** en la esquina superior derecha de la pantalla.
3. Toca **Ajustes**.
4. Desplázate hacia abajo hasta **Identidad del usuario y del dispositivo**, luego **Metadatos del formulario**.
5. Ingresa el nombre de usuario y/o el número de teléfono. También puedes ver el ID del dispositivo actual.