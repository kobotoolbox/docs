# Tipos de preguntas en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/question_types_xls.md" class="reference">23 abr 2026</a>

Al agregar preguntas a un XLSForm, necesitarás elegir el **tipo de pregunta** apropiado. El tipo de pregunta dependerá del tipo de información que deseas recolectar: algunos tipos de preguntas son más adecuados para texto, otros para números, fechas o entradas de selección múltiple.

El tipo de pregunta en XLSForm se ingresa en la columna `type` de la **hoja survey**. Siempre usa la ortografía exacta y el uso de mayúsculas y minúsculas. Puedes agregar [apariencias](https://support.kobotoolbox.org/es/appearances_xls.html) adicionales a la mayoría de los tipos de preguntas para modificar su visualización o funcionalidad.

<p class="note">
<strong>Nota:</strong> Si bien XLSForm está completamente integrado en KoboToolbox, algunos tipos de preguntas tienen nombres y funcionalidades diferentes en el <a href="https://support.kobotoolbox.org/es/formbuilder.html">Formbuilder</a> que en XLSForm.
</p>

Este artículo cubre los tipos de preguntas disponibles en XLSForm, incluyendo sus descripciones y equivalentes en el Formbuilder. Se proporcionan enlaces al final de cada sección para obtener más información sobre las funcionalidades de los tipos de preguntas y apariencias durante la recolección de datos.

<p class="note">
Para obtener más información sobre la creación de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">Crear un XLSForm</a>.
</p>

### Tipos de pregunta de selección múltiple

Las preguntas de selección múltiple permiten a los encuestados elegir entre opciones predefinidas. Para las preguntas `select_one`, `select_multiple` y `rank`, las [opciones de respuesta](https://support.kobotoolbox.org/es/option_choices_xls.html) se definen en la **hoja choices** del XLSForm.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `select_one` | Permite a los encuestados seleccionar una opción de una lista predefinida. | Seleccionar una |
| `select_multiple` | Permite a los encuestados seleccionar múltiples opciones de una lista predefinida. | Seleccionar varias |
| `rank` | Permite a los encuestados clasificar elementos u opciones en una lista de opciones. | Clasificación |
| `acknowledge` | Una sola casilla de verificación que los encuestados pueden seleccionar para reconocer su acuerdo con una declaración. | Consentimiento |
| `select_one_from_file` | Permite a los encuestados seleccionar una opción de una lista predefinida, almacenada en un archivo CSV externo. | Seleccionar una de un archivo |
| `select_multiple_from_file` | Permite a los encuestados seleccionar múltiples opciones de una lista predefinida, almacenada en un archivo CSV externo. | Seleccionar varias de un archivo |


<p class="note">
Para obtener más información sobre los tipos de preguntas de selección múltiple en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/select_one_and_select_many.html">Pregunta de selección múltiple en KoboToolbox</a>.
</p>


### Tipos de preguntas numéricas

Las preguntas numéricas se utilizan para recolectar números enteros, números decimales o valores dentro de un rango especificado.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `integer` | Permite a los encuestados ingresar números enteros. | Número |
| `decimal` | Permite a los encuestados ingresar números que pueden contener puntos decimales. | Decimal |
| `range` | Permite a los encuestados seleccionar un valor numérico dentro de un rango especificado limitado por valores mínimos y máximos, <a href="https://support.kobotoolbox.org/es/question_options_xls.html#question-parameters">configurado</a> en la columna `parameters`. | Rango |


<p class="note">
Para obtener más información sobre los tipos de preguntas numéricas en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/number_decimal_range.html">Preguntas digitales en KoboToolbox</a>.
</p>


### Tipos de preguntas de texto y nota

Las preguntas de texto se utilizan para recolectar respuestas abiertas, mientras que las preguntas de nota proporcionan información o dan instrucciones a los encuestados.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `text` | Proporciona un cuadro de texto para recolectar respuestas abiertas cuando las opciones no se pueden predefinir fácilmente, como nombres, opiniones o descripciones detalladas. | Texto |
| `note` | Proporciona información al encuestado sin requerir ninguna entrada, como instrucciones o explicaciones. | Nota |


<p class="note">
Para obtener más información sobre los tipos de preguntas de texto y nota en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/text_questions.html">Preguntas de tipo Texto en KoboToolbox</a> y <a href="https://support.kobotoolbox.org/es/note_questions.html">Preguntas de tipo Nota en KoboToolbox</a>.
</p>

### Tipos de preguntas multimedia

Las preguntas multimedia permiten a los encuestados cargar o grabar archivos de imágenes, audio y video, o escanear códigos de barras directamente en sus formularios.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `image` | Permite a los encuestados cargar imágenes o tomar fotos al usar la aplicación KoboCollect. La calidad de los archivos de imagen se puede <a href="https://support.kobotoolbox.org/es/question_options_xls.html#question-parameters">ajustar</a> en la columna `parameters`. | Foto |
| `audio` | Permite a los encuestados cargar un archivo de audio o grabar audio como respuesta a una pregunta específica. La calidad de los archivos de audio se puede <a href="https://support.kobotoolbox.org/es/question_options_xls.html#question-parameters">ajustar</a> en la columna `parameters`. | Audio |
| `video` | Permite a los encuestados cargar videos o grabar videos al usar la aplicación KoboCollect. | Video |
| `file` | Permite a los encuestados cargar archivos, como archivos de texto, hojas de cálculo y archivos PDF. Los tipos de archivos aceptados se pueden <a href="https://support.kobotoolbox.org/es/question_options_xls.html#additional-question-options">restringir</a> especificando extensiones de archivo en la columna `body::accept` (por ejemplo, `.pdf, .docx`). | Archivo |
| `barcode` | Escanea un código QR para recolectar información integrada usando la cámara del dispositivo en KoboCollect. | Código de barras |
| `background-audio` | Recolecta audio continuamente mientras el formulario está abierto. La grabación de audio comienza cuando se abre el formulario y continúa hasta que se cierra el formulario. | Grabación de sonido de fondo |


<p class="note">
Para obtener más información sobre los tipos de preguntas multimedia en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/photo_audio_video_file.html">Preguntas Multimedia en KoboToolbox</a> y <a href="https://support.kobotoolbox.org/es/recording-interviews.html#recording-interviews-with-background-audio-recordings">Recolectar datos cualitativos con KoboToolbox</a>.
</p>

### Tipos de preguntas GPS

Las preguntas GPS se utilizan para capturar las coordenadas geográficas de una ubicación, ruta o área directamente dentro de tus formularios.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `geopoint` | Recolecta una única ubicación geográfica, como las coordenadas de una escuela, clínica o casa específica. La precisión predeterminada y la precisión de advertencia se pueden <a href="https://support.kobotoolbox.org/es/question_options_xls.html#question-parameters">configurar</a> en la columna `parameters`. | Punto |
| `geotrace` | Registra múltiples puntos GPS que forman una línea, por ejemplo, para rastrear un camino, trazar una ruta o mapear un drenaje. | Línea |
| `geoshape` | Recolecta puntos que forman un área cerrada, como una parcela de tierra o un campo. | Área |


<p class="note">
Para obtener más información sobre los tipos de preguntas GPS en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/gps_questions.html">Preguntas GPS en KoboToolbox</a>.
</p>

### Tipos de preguntas de fecha y hora

Las preguntas de fecha y hora se utilizan para capturar fechas de calendario específicas, horas o ambas en una sola respuesta.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `date` | Captura una fecha de calendario específica, típicamente en el formato de día, mes y año. | Fecha |
| `time` | Captura una hora específica en horas y minutos. | Hora |
| `datetime` | Captura tanto una fecha como una hora en una sola respuesta combinada. | Fecha y hora |


<p class="note">
Para obtener más información sobre las preguntas de fecha y hora en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/date_time.html">Preguntas de Fecha y Hora en KoboToolbox</a>.
</p>

### Tipos de preguntas de cálculo y ocultas

Las preguntas de cálculo y ocultas se utilizan para realizar cálculos automáticos dentro de un formulario basados en respuestas anteriores o para almacenar valores predefinidos.

| Tipo XLSForm | Descripción | Equivalente en el Formbuilder |
| :--- | :--- | :--- |
| `calculate` | Realiza automáticamente cálculos dentro de un formulario basados en respuestas a preguntas anteriores. | Cálculo |
| `hidden` | Almacena valores predefinidos que no son visibles para el encuestado. El valor se <a href="https://support.kobotoolbox.org/es/question_options_xls.html#default-responses">almacena</a> en la columna `default`. | Oculto |

Para obtener más información sobre los cálculos en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/calculations_xls.html">Agregar cálculos a un XLSForm</a>.

<p class="note">
Para práctica con diferentes tipos de preguntas en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals de la KoboToolbox Academy</a>.
</p>