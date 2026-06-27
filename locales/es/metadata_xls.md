# Metadatos en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/metadata_xls.md" class="reference">23 Apr 2026</a>

Las preguntas de metadatos recopilan automáticamente información sobre el proceso de recolección de datos, como la fecha, la hora y el dispositivo utilizado, sin requerir ninguna entrada del encuestado. También puedes grabar audio de fondo durante la recolección de datos.

Las preguntas de metadatos están ocultas para los encuestados, y los campos de metadatos no se pueden editar en la tabla de datos de KoboToolbox. Esta información de fondo facilita la auditoría, ayuda a mantener la integridad de los datos y puede utilizarse en el análisis de datos.

<p class="note">
<strong>Nota:</strong> Este artículo se centra en agregar preguntas de metadatos en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agregar preguntas de metadatos en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/form_meta.html">Agregar metadatos en el Formbuilder</a>.
</p>

## Agregar preguntas de metadatos en XLSForm

Las preguntas de metadatos se agregan a XLSForm de la misma manera que cualquier otro tipo de pregunta:

1. Ingresa el `type` (tipo) de la pregunta de metadatos en una nueva fila, usando el nombre exacto que se muestra [en la tabla a continuación](https://support.kobotoolbox.org/es/metadata_xls.html#available-metadata-questions-in-xlsform).
2. Incluye un `name` (nombre) para la pregunta.
3. Las etiquetas de las preguntas no son obligatorias, ya que no se muestran en el formulario.

**hoja survey**

| type | name       | label        |
|:-----|:-----------|:-------------|
| start | start_time |              |
| end   | end_time   |              |
| survey |

## Preguntas de metadatos disponibles en XLSForm

Las preguntas de metadatos disponibles en XLSForm incluyen:

| Tipo       | Descripción |
|:--------------------|:-------------|
| `start` | Registra la fecha y hora exactas en que se inicia un envío. |
| `end` | Registra la fecha y hora en que se finaliza un envío. |
| `today` | Registra la fecha del envío. |
| `deviceid` | Registra la identificación única del dispositivo o navegador utilizado para recolectar datos. El <code>deviceid</code> se genera automáticamente y los usuarios no pueden modificarlo.<br><br>**Nota:** En KoboCollect, el <code>deviceid</code> se actualiza cada vez que la aplicación se reinstala en un dispositivo. Al usar formularios web, el <code>deviceid</code> se restablece cada vez que se abre una nueva ventana del navegador. |
| `username` | En KoboCollect, registra el nombre de usuario guardado en la <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings">configuración de la aplicación KoboCollect</a>. Si no se ha configurado ningún nombre de usuario, registra el utilizado para iniciar sesión en el servidor.<br>Al usar formularios web, el nombre de usuario de la cuenta solo se registra si se <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requiere autenticación</a>.<br><br>**Nota:** Dado que el campo `username` puede editarse en KoboCollect, es posible que no coincida con la cuenta utilizada para autenticarse en el servidor. Para ver qué cuenta envió los datos, consulta el campo `_submitted_by` generado automáticamente. |
| `phonenumber` | Registra el número de teléfono almacenado en la <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings">configuración de la aplicación KoboCollect</a>. Esta pregunta de metadatos no es compatible con formularios web. |
| `email` | Registra la dirección de correo electrónico de la <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings">configuración de la aplicación KoboCollect</a>. Esta pregunta de metadatos no es compatible con formularios web. |
| `start-geopoint` | Captura las coordenadas GPS cuando el formulario se abre por primera vez. Puede utilizarse para activar el GPS del dispositivo con anticipación, de modo que las preguntas GPS posteriores puedan obtener lecturas precisas más rápidamente. |
| `background-geopoint` | Captura las coordenadas GPS cuando se responde una pregunta específica. La pregunta debe especificarse en la columna `trigger` de la pregunta `background-geopoint`. |
| `background-audio` | Graba audio de fondo mientras el formulario está abierto. Para obtener más información sobre esta funcionalidad, consulta <a href="https://support.kobotoolbox.org/es/recording-interviews.html#recording-interviews-with-background-audio-recordings">Recolectar datos cualitativos con KoboToolbox</a>. |
| `audit` | Captura un registro detallado del proceso de entrevista, incluyendo la hora de inicio, la hora de finalización, la ubicación y las acciones del usuario durante todo el proceso de recolección de datos. Esta pregunta de metadatos no es compatible con formularios web.<br><br>Para obtener más información sobre el uso de la pregunta de auditoría y la configuración de sus ajustes, consulta <a href="https://docs.getodk.org/form-audit-log/">Form Audit Log (ODK)</a>. |

<p class="note">
<strong>Nota:</strong>
    Los metadatos del formulario son diferentes de los <a href="https://support.kobotoolbox.org/es/viewing_validating_data.html#system-generated-submission-fields">campos de envío generados por el sistema</a>. Los metadatos del formulario deben habilitarse durante el desarrollo del formulario para que se recolecten, mientras que los campos de envío generados por el sistema se agregan automáticamente en cada envío.
</p>

## Configurar metadatos en KoboCollect

El correo electrónico, el número de teléfono y el nombre de usuario predeterminados del usuario pueden [configurarse](https://support.kobotoolbox.org/es/kobocollect_settings.html#user-and-device-identity-settings) y modificarse en la aplicación KoboCollect:

1. Abre la aplicación KoboCollect.
2. Haz clic en el **ícono del proyecto** en la esquina superior derecha de la pantalla.
3. Haz clic en **Ajustes**.
4. Desplázate hacia abajo hasta **Identidad del usuario y del dispositivo** y luego hasta **Metadatos del formulario**.
5. Ingresa el nombre de usuario, el número de teléfono y/o la dirección de correo electrónico. También puedes ver el ID del dispositivo actual.

## Configurar la calidad de audio de las grabaciones de audio de fondo

Al grabar entrevistas en segundo plano, la calidad del audio afecta el tamaño del archivo almacenado en el servidor. Los usuarios del [Community Plan](https://www.kobotoolbox.org/pricing/) tienen un límite de 1 GB de almacenamiento de archivos gratuito. Por lo tanto, es recomendable gestionar el tamaño de los archivos de audio que recolectas eligiendo una configuración de calidad adecuada.

Para ajustar la calidad de audio de la grabación de audio de fondo:

1. Agrega una columna `parameters` a tu XLSForm.
2. En la fila `background-audio`, ingresa una de las siguientes opciones:
    - `quality=normal`
    - `quality=low`
    - `quality=voice-only`

**hoja survey**

| type             | name       | label | parameters       |
|:-----------------|:-----------|:------|:----------------|
| background-audio | recording  |       | quality=normal  |
| survey |

La tabla a continuación ofrece una descripción general de las configuraciones de calidad de audio y los tamaños de archivo correspondientes.

| Parámetro XLSForm   | Extensión | Codificación | Tasa de bits | Frecuencia de muestreo | Tamaño de archivo |
|:------------------  |:---------|:------------|:------------|:----------------------|:-----------------|
| quality=normal      | .m4a     | AAC         | 64 kbps     | 32 kHz                | ~ 30 MB/hora     |
| quality=low         | .m4a     | AAC         | 24 kbps     | 32 kHz                | ~ 11 MB/hora     |
| quality=voice-only  | .amr     | AMR         | 12.2 kbps   | 8 kHz                 | ~ 5 MB/hora      |

La configuración predeterminada `voice-only` es adecuada para entrevistas en entornos silenciosos. Para grabaciones con varios interlocutores o algo de ruido de fondo, la configuración de calidad `low` es más apropiada. La configuración `normal` ofrece la mayor calidad de audio, pero utiliza más espacio de almacenamiento.