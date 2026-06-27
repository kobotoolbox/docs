# Agregar preguntas con el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/35c2ef4865450c612c41e9e784bd674a9f99756a/source/question_types.md" class="reference">20 Mar 2026</a>

El editor de formularios de KoboToolbox **(Formbuilder)** te permite agregar preguntas fácilmente a tu formulario mientras construyes tu encuesta o cuestionario.

Este artículo explica cómo agregar preguntas a tu formulario, definir opciones de respuesta cuando corresponda, y ofrece una descripción general de los tipos de preguntas disponibles en el Formbuilder para apoyar un diseño de formulario efectivo.

## Agregar una pregunta

Para agregar una pregunta a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ ADD QUESTION.**
4. Elige el [tipo de pregunta](#tipos-de-preguntas-en-el-formbuilder).

![Agregar una pregunta al Formbuilder](images/question_types/add_question.png)

<p class="note">
<strong>Nota:</strong> Una vez seleccionado el tipo de pregunta, no se puede cambiar en el Formbuilder. Para cambiar el tipo de pregunta de una pregunta existente, elimina la pregunta y crea una nueva con la misma etiqueta.
</p>

### Definir nombres de columna de datos

Después de agregar una pregunta a tu formulario, se recomienda definir un **Nombre de columna de datos** en la **Configuración** de la pregunta. El nombre de columna de datos se utiliza para identificar la pregunta en la lógica del formulario y en el conjunto de datos exportado.

De forma predeterminada, KoboToolbox crea el nombre de columna de datos eliminando los espacios y las letras mayúsculas de la etiqueta de la pregunta. Por ejemplo, si la etiqueta de la pregunta es "Nombre del encuestado", el nombre de columna de datos será `nombre_del_encuestado`.

<p class="note">
    Para obtener más información sobre los nombres de columna de datos, consulta <a href="https://support.kobotoolbox.org/es/question_options.html#data-column-name">Opciones de preguntas en el Formbuilder</a>.
</p>

## Agregar opciones de respuesta

Al agregar preguntas de Seleccionar una o Seleccionar varias a tu formulario, se te pedirá que ingreses opciones de respuesta.

- Puedes ingresar tantas opciones de respuesta como quieras.
- Para reordenar la lista de opciones, haz clic y arrastra un elemento a la posición deseada.
- Haz clic en el icono de papelera <i class="k-icon-trash"></i> junto a la etiqueta de una opción para eliminarla.

![Eliminar opción](images/question_types/delete_choice.png)

<p class="note">
<strong>Nota:</strong> Gestionar listas de opciones largas en el Formbuilder puede llevar mucho tiempo. Si tu formulario incluye muchas opciones o la misma lista de opciones se usa en varias preguntas, generalmente es más fácil crear y gestionar estas listas usando XLSForm. Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/option_choices_xls.html#">Administrar opciones de respuesta en XLSForm</a>.
</p>

### Definir valores XML para las opciones de respuesta

Junto a cada opción, verás un campo con la etiqueta **AUTOMATIC.** Este campo contiene el [valor XML](https://support.kobotoolbox.org/es/glossary.html#xml-value) de esa opción.

El valor XML es un nombre interno breve que KoboToolbox utiliza para guardar e identificar la opción seleccionada en tus datos. De forma predeterminada, KoboToolbox crea el valor XML eliminando los espacios y las letras mayúsculas de la etiqueta de la opción. Por ejemplo, si la etiqueta de la opción es "Opción 1", el valor XML será `opcion_1`.

En algunos casos, es posible que quieras definir tu propio valor XML. Esto puede ser útil si la etiqueta de la opción es muy larga o si quieres usar un nombre más claro o coherente. Para hacerlo, haz clic en **AUTOMATIC** y reemplázalo con tu propio valor personalizado.

<p class="note">
<strong>Nota:</strong> Se recomienda definir valores XML para todas las opciones cuando se usen escrituras no latinas, como chino, árabe o nepalés, para garantizar que tus datos se almacenen y exporten correctamente.
</p>

## Tipos de preguntas en el Formbuilder

Los siguientes tipos de preguntas están disponibles en el Formbuilder:

| Tipo de pregunta | Descripción |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| <i class="k-icon-qt-select-one"></i> Seleccionar una | Permite a los encuestados [seleccionar una opción](https://support.kobotoolbox.org/es/select_one_and_select_many.html) de una lista predefinida. |
| <i class="k-icon-qt-select-many"></i> Seleccionar varias | Permite a los encuestados [seleccionar varias opciones](https://support.kobotoolbox.org/es/select_one_and_select_many.html) de una lista predefinida. |
| <i class="k-icon-qt-text"></i> Texto | Proporciona un [cuadro de texto](https://support.kobotoolbox.org/es/text_questions.html) para recolectar respuestas abiertas. |
| <i class="k-icon-qt-number"></i> Número | Permite a los encuestados ingresar [números enteros](https://support.kobotoolbox.org/es/number_decimal_range.html). |
| <i class="k-icon-qt-decimal"></i> Decimal | Permite a los encuestados [ingresar números](https://support.kobotoolbox.org/es/number_decimal_range.html) que pueden contener decimales. |
| <i class="k-icon-qt-date"></i> Fecha | Captura una [fecha de calendario](https://support.kobotoolbox.org/es/date_time.html) específica, incluyendo año, mes y día. |
| <i class="k-icon-qt-time"></i> Hora | Captura una [hora específica](https://support.kobotoolbox.org/es/date_time.html) en horas y minutos. |
| <i class="k-icon-qt-date-time"></i> Fecha y hora | Captura [una fecha y una hora](https://support.kobotoolbox.org/es/date_time.html) en una sola respuesta combinada. |
| <i class="k-icon-qt-point"></i> Punto | Registra una [ubicación GPS única](https://support.kobotoolbox.org/es/gps_questions.html). |
| <i class="k-icon-qt-line"></i> Línea | Registra [varios puntos GPS](https://support.kobotoolbox.org/es/gps_questions.html) que forman una línea. |
| <i class="k-icon-qt-area"></i> Área | Registra [varios puntos GPS](https://support.kobotoolbox.org/es/gps_questions.html) que forman un área cerrada. |
| <i class="k-icon-qt-photo"></i> Foto | Permite a los encuestados [cargar imágenes](https://support.kobotoolbox.org/es/photo_audio_video_file.html) o tomar fotos (cuando se usa la [aplicación KoboCollect](https://support.kobotoolbox.org/es/glossary.html#kobocollect)). |
| <i class="k-icon-qt-audio"></i> Audio | Permite a los encuestados [cargar un archivo de audio](https://support.kobotoolbox.org/es/photo_audio_video_file.html) o grabar audio. |
| <i class="k-icon-qt-video"></i> Video | Permite a los encuestados [cargar videos](https://support.kobotoolbox.org/es/photo_audio_video_file.html) o grabar videos (cuando se usa la [aplicación KoboCollect](https://support.kobotoolbox.org/es/glossary.html#kobocollect)). |
| <i class="k-icon-qt-barcode"></i> Código de barras / Código QR | Escanea un [código QR](https://support.kobotoolbox.org/es/photo_audio_video_file.html) para recolectar información incorporada usando la cámara del dispositivo (cuando se usa la [aplicación KoboCollect](https://support.kobotoolbox.org/es/glossary.html#kobocollect)). |
| <i class="k-icon-qt-file"></i> Archivo | Permite a los encuestados [cargar archivos](https://support.kobotoolbox.org/es/photo_audio_video_file.html), como archivos de texto, hojas de cálculo y archivos PDF. |
| <i class="k-icon-qt-note"></i> Nota | [Proporciona información](https://support.kobotoolbox.org/es/note_questions.html) al encuestado sin requerir ninguna entrada. |
| <i class="k-icon-qt-acknowledge"></i> Consentimiento | Una [casilla de selección única](https://support.kobotoolbox.org/es/select_one_and_select_many.html) que los encuestados pueden marcar para confirmar su acuerdo con una declaración. |
| <i class="k-icon-qt-rating"></i> Calificación | Permite a los encuestados [calificar diferentes elementos](https://support.kobotoolbox.org/es/select_one_and_select_many.html#setting-up-rating-questions) usando una escala común. |
| <i class="k-icon-qt-question-matrix"></i> Matriz de preguntas | Crea un [grupo de preguntas](https://support.kobotoolbox.org/es/matrix_response.html) que se muestran en formato de matriz, donde cada celda dentro de la matriz representa una pregunta independiente. |
| <i class="k-icon-qt-ranking"></i> Clasificación | Permite a los encuestados [ordenar elementos](https://support.kobotoolbox.org/es/select_one_and_select_many.html#setting-up-ranking-questions) según su preferencia. |
| <i class="k-icon-qt-calculate"></i> Cálculo | Realiza automáticamente [cálculos](https://support.kobotoolbox.org/es/calculate_questions.html) dentro de un formulario basándose en las respuestas a preguntas anteriores. |
| <i class="k-icon-qt-hidden"></i> Oculto | Almacena [valores predefinidos](https://support.kobotoolbox.org/es/form_logic.html#storing-constants-in-your-form) que no son visibles para el encuestado. |
| <i class="k-icon-qt-range"></i> Rango | Permite a los encuestados [seleccionar un valor numérico](https://support.kobotoolbox.org/es/number_decimal_range.html#setting-up-range-questions) dentro de un rango especificado. |
| <i class="k-icon-qt-external-xml"></i> XML externo | Conecta el proyecto de KoboToolbox con [otros proyectos](https://support.kobotoolbox.org/es/dynamic_data_attachment_formbuilder.html) para recuperar datos de forma dinámica. |
| <i class="k-icon-qt-select-one-from-file"></i> Seleccionar una de un archivo | Permite a los encuestados seleccionar una opción [de una lista predefinida](https://support.kobotoolbox.org/es/external_file.html) almacenada en un archivo CSV externo. |
| <i class="k-icon-qt-select-many-from-file"></i> Seleccionar varias de un archivo | Permite a los encuestados seleccionar varias opciones [de una lista predefinida](https://support.kobotoolbox.org/es/external_file.html) almacenada en un archivo CSV externo. |

<p class="note">
<strong>Nota:</strong> Los tipos de preguntas Seleccionar una de un archivo y Seleccionar varias de un archivo solo aparecen como opciones en el Formbuilder si se ha <a href="https://support.kobotoolbox.org/es/upload_media.html">cargado</a> un archivo de opciones externo en KoboToolbox.
</p>