# Mensaje personalizado de confirmación de envío
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/22959ee8b91c5f4cb42545d225dec591a0d409c0/source/custom_submission_message.md" class="reference">29 Jul 2026</a>

Los mensajes personalizados de confirmación de envío te permiten mostrar un mensaje personalizado después de que un encuestado envíe un formulario exitosamente.

Los mensajes personalizados de confirmación de envío se pueden usar para:

- **Confirmar registros de eventos:** Por ejemplo, para confirmar el registro, proporcionar detalles del evento e incluir un enlace para descargar el calendario.
- **Proporcionar incentivos condicionales:** Para mostrar un mensaje basado en la elegibilidad del encuestado, como un código de cupón o un mensaje de agradecimiento.
- **Apoyar flujos de trabajo de seguimiento:** Para mostrar un número de ticket, un resumen de los datos enviados o un enlace al siguiente paso en un proceso.

Esta funcionalidad debe configurarse en [XLSForm](https://support.kobotoolbox.org/es/getting_started_xlsform.html).

## Configurar un mensaje personalizado de confirmación de envío

Para configurar un mensaje personalizado de confirmación de envío en XLSForm:

1. En la **hoja settings**, añade tres columnas: `name`, `namespaces` y `attribute::kobo:submitMessage`
    - En la columna `name`, ingresa `data`
    - En la columna `namespaces`, ingresa `kobo="http://kobotoolbox.org/xforms"`
    - En la columna `attribute::kobo:submitMessage`, ingresa `/data/submitMessage`.

**hoja settings**

| name | namespaces     | attribute::kobo:submitMessage              |
| :--- | :------- | :----------------- |
| text | kobo="http://kobotoolbox.org/xforms" | /data/submitMessage |
| settings |

2. En la **hoja survey**, crea una pregunta de tipo `calculate`.
    - En la columna `name`, ingresa `submitMessage`
    - En la columna `calculation`, ingresa el mensaje de confirmación que deseas usar.

**hoja survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- |:------------|
| calculate | submitMessage |  | `"Thank you for registering. Click [here](http://kobotoolbox.org) for more information about the event."` |
| survey |

<p class="note">
  Para ver un ejemplo de esta funcionalidad en la práctica, descarga un XLSForm de ejemplo <a href="https://docs.google.com/spreadsheets/d/1CgjrpJcDX1pLmf-B-PUZ4-KFs2pPuntD/edit?usp=sharing&ouid=104272235398180261217&rtpof=true&sd=true">aquí</a>.
</p>

## Personalizar el mensaje de confirmación de envío

Puedes usar funciones y Markdown en la columna `calculation` para personalizar el mensaje.

### Usar declaraciones condicionales

Usa `if()` para mostrar diferentes mensajes según las respuestas del formulario.

Por ejemplo: `if(${eligible} = 'yes', 'You are eligible.', 'You are not eligible.')`

### Mostrar etiquetas de opciones

Usa `jr:choice-name()` para mostrar la [etiqueta](https://support.kobotoolbox.org/es/glossary.html#label) de una opción seleccionada en lugar de su [nombre de opción](https://support.kobotoolbox.org/es/glossary.html#choice-name).

Por ejemplo: `concat('You are registered for ', jr:choice-name(${event}, '${event}'))`

### Dar formato al mensaje de confirmación de envío

Usa Markdown para añadir formato al mensaje de confirmación de envío, como hipervínculos, texto en negrita, texto en cursiva o listas.

Por ejemplo: `'**Congratulations!** You are eligible. Click [here](http://kobotoolbox.org) for more information.'`

<p class="note">
  Para más información sobre cómo dar formato al texto usando Markdown, consulta <a href="https://support.kobotoolbox.org/es/form_style_xls.html#styling-text">Personalizar formularios usando XLSForm</a>.
</p>

## Crear mensajes de confirmación de envío en varios idiomas

En formularios multilingües, puedes mostrar el mensaje de confirmación de envío en el idioma seleccionado por el encuestado.

Para configurar mensajes de confirmación de envío multilingües:

1. En la **hoja survey**, crea una pregunta de tipo `select_one` para almacenar el mensaje.
2. Ingresa `false` en la columna `relevant` para ocultar la pregunta en el formulario.
3. En la **hoja choices**, añade el mensaje de confirmación de envío como una opción.
4. [Traduce](https://support.kobotoolbox.org/es/language_xls.html) la etiqueta de la opción a cada idioma del formulario.
5. En la columna `calculation` de la fila `submitMessage`, ingresa: `jr:choice-name('choice_name', '${question_name}')`
    - `choice_name` es el nombre de la opción donde se almacena tu mensaje
    - `question_name` es el nombre de la pregunta `select_one` creada anteriormente

El mensaje de confirmación de envío aparecerá en el idioma seleccionado en la parte superior del formulario.

<p class="note">
  Para ver un ejemplo de un formulario que muestra un mensaje de confirmación de envío en varios idiomas, descarga un XLSForm de ejemplo <a href="https://docs.google.com/spreadsheets/d/1NXwXbG6PaSFX1HZGEDMdji6XiUIHfkHG/edit?usp=sharing&rtpof=true&sd=true">aquí</a>.
</p>

## Compatibilidad

Los mensajes personalizados de confirmación de envío están diseñados para usarse con [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html). Solo funcionan con los siguientes [modos de recolección de datos](https://support.kobotoolbox.org/es/data_through_webforms.html#data-collection-modes):

- Solo en línea (envío único)
- Solo en línea (una vez por encuestado)

También pueden aparecer en [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html), pero KoboCollect trata el mensaje como texto sin formato, por lo que el formato Markdown y los enlaces no se renderizan. Ten en cuenta tu método de recolección de datos y prueba el mensaje antes de recolectar datos con tu formulario.