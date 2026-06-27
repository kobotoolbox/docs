# Crear un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/getting_started_xlsform.md" class="reference">23 abr 2026</a>

<iframe src="https://www.youtube.com/embed/xpeBCy9p1Ys?si=tP_3G2vMnRC1OgWS&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Al crear formularios de encuesta con KoboToolbox, puedes crear tu formulario con el [editor de formularios de KoboToolbox (Formbuilder)](https://support.kobotoolbox.org/es/formbuilder.html) o usando XLSForm. XLSForm es muy efectivo para crear formularios básicos y avanzados en un formato fácil de usar.

<p class="note">
  Para obtener más información sobre XLSForm, consulta <a class="reference" href="https://support.kobotoolbox.org/es/edit_forms_excel.html">Introducción a XLSForm</a>. Para una introducción completa al desarrollo de formularios usando XLSForm, recomendamos el <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> en línea de aprendizaje autónomo de KoboToolbox Academy.
</p>

Este artículo explica cómo configurar un XLSForm usando Microsoft Excel u otros programas de hojas de cálculo, incluyendo:

- Configurar la estructura básica de tu XLSForm
- Agregar preguntas y opciones de respuesta
- Agregar configuración del formulario y columnas opcionales
- Cargar y previsualizar tu XLSForm en KoboToolbox

<p class="note">
  <b>Nota:</b> Algunas funcionalidades de XLSForm no están disponibles actualmente en el Formbuilder, pero los formularios de KoboToolbox se pueden descargar, modificar en XLSForm y <a class="reference" href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html">cargar de nuevo a KoboToolbox</a>.
</p>

## Configurar un XLSForm

Para configurar la estructura básica de un XLSForm:

1. Abre una nueva hoja de cálculo en tu programa de hojas de cálculo preferido.
2. Crea tres hojas de trabajo: `survey`, `choices` y `settings`.
   - Los nombres de las hojas de trabajo deben estar en minúsculas.
3. En la **hoja survey**, crea tres columnas con los encabezados: `type`, `name` y `label`.
4. En la **hoja choices**, crea tres columnas con los encabezados: `list_name`, `name` y `label`.
5. La **hoja settings** es opcional. Se puede usar para incluir especificaciones y personalizaciones adicionales del formulario.
   - Por ejemplo: `form_title`, `style` y `default_language`.

<p class="note">
Para comenzar con XLSForm, descarga un XLSForm de ejemplo <a class="reference" href="https://support.kobotoolbox.org/_static/files/getting_started_xlsform/sample_xlsform.xlsx">aquí</a>.
</p>

### Columnas obligatorias en XLSForm

Las siguientes columnas son obligatorias en XLSForm:

**hoja survey**

| Nombre de columna | Descripción |
| --- | --- |
| `type` | Define el tipo de pregunta (ej., text, integer, select_one) |
| `name` | Define un nombre corto y único para referirse a cada pregunta |
| `label` | Define el texto de la pregunta tal como se mostrará en el formulario |

**hoja choices**

| Nombre de columna | Descripción |
| --- | --- |
| `list_name` | Define el identificador único para una lista de opciones de respuesta |
| `name` | Define un nombre corto y único para referirse a cada opción de respuesta |
| `label` | Define el texto de la opción tal como se mostrará en el formulario |

## Agregar preguntas

En XLSForm, las preguntas se agregan en la **hoja survey**. Para agregar preguntas en XLSForm:

1. En la columna `type` de la **hoja survey**, ingresa el [tipo de pregunta](https://support.kobotoolbox.org/es/question_types_xls.html) de la pregunta que deseas agregar.
2. En la columna `name`, ingresa un nombre usado para identificar la pregunta.
   - Cada pregunta debe tener un nombre único y no puede contener espacios ni símbolos (excepto guiones bajos).
3. En la columna `label`, ingresa el texto de la pregunta tal como debe mostrarse en el formulario durante la recolección de datos.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| text | yourname | ¿Cuál es tu nombre? |
| survey |

4. Si estás agregando **preguntas de tipo selección** (`select_one`, `select_multiple` o `rank`): en la columna `type`, después del tipo de pregunta, agrega un espacio e ingresa el nombre de la lista de opciones.
   - El nombre de la lista de opciones se define más adelante en la **hoja choices** como `list_name`.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| select_one sex | baby_sex | ¿Cuál es el sexo de tu bebé? |
| survey |

<p class="note">
Para obtener más información sobre los tipos de pregunta en XLSForm, consulta <a class="reference" href="https://support.kobotoolbox.org/es/question_types_xls.html">Tipos de preguntas en XLSForm</a>.
</p>

## Agregar opciones de respuesta

Para preguntas de tipo selección, las opciones de respuesta se agregan en la **hoja choices**. Para agregar opciones de respuesta en XLSForm:

1. En la columna `list_name` de la **hoja choices**, ingresa el nombre de la **lista de opciones de respuesta**.
   - El `list_name` es un identificador único para una lista de opciones de respuesta. Debe coincidir con el nombre de lista ingresado en la columna `type` de la **hoja survey**.
2. En la columna `name`, agrega un nombre corto para cada opción de respuesta.
   - Cada opción dentro de una lista debe tener un `name` único, que no puede contener espacios ni símbolos (excepto guiones bajos).
3. En la columna `label`, ingresa el texto de la opción tal como debe mostrarse en el formulario durante la recolección de datos.

**hoja choices**

| list_name | name | label |
| :--- | :--- | :--- |
| sex | male | Masculino |
| sex | female | Femenino |
| choices |

<p class="note">
Para obtener más información sobre la administración de opciones de respuesta en XLSForm, consulta <a class="reference" href="https://support.kobotoolbox.org/es/option_choices_xls.html">Administrar opciones de respuesta en XLSForm</a>.
</p>

## Agregar configuraciones

Hay muchas configuraciones opcionales que se pueden agregar a la **hoja settings** en XLSForm.

Las configuraciones comunes del formulario incluyen:

| Configuración | Descripción |
| --- | --- |
| `form_title` | Título que se muestra en la parte superior del formulario |
| `default_language` | Idioma predeterminado del formulario |
| `style` | Temas para formularios web |
| `version` | ID de versión del formulario |

Por ejemplo, para agregar un título de formulario:

1. Agrega una columna en la **hoja settings** llamada `form_title`.
2. Ingresa el título del formulario en la columna `form_title`.

<p class="note">
<b>Nota:</b> Todas las configuraciones del formulario son opcionales. Si no defines un título de formulario en tu XLSForm, el nombre del archivo de Excel se usará como el nombre del proyecto en KoboToolbox de forma predeterminada. Esto se puede editar en KoboToolbox.
</p>

**hoja settings**

| form_title |
| :--- |
| Comenzar con <br> XLSForm |
| settings |

<p class="note">
Para obtener más información sobre la hoja de configuraciones en XLSForm, consulta <a class="reference" href="https://support.kobotoolbox.org/es/form_settings_xls.html">Configuración de formularios en XLSForm</a>.
</p>

## Agregar columnas opcionales a la hoja survey

Para personalizar aún más tu XLSForm, puedes agregar columnas opcionales para configurar la lógica del formulario, opciones de preguntas y configuraciones avanzadas. Las columnas opcionales comunes incluyen:

| Nombre de columna | Descripción |
| --- | --- |
| `hint` | Sugerencia de pregunta |
| `guidance_hint` | Sugerencia adicional |
| `required` | Hace que una pregunta sea obligatoria |
| `relevant` | Condiciones de lógica de omisión para la pregunta |
| `constraint` | Criterios de validación para la pregunta |
| `constraint_message` | Mensaje de error cuando no se cumplen los criterios de validación |
| `appearance` | Opciones para cómo se muestran las preguntas |
| `choice_filter` | Criterios para selección en cascada |
| `parameters` | Configuraciones para tipos de pregunta específicos |
| `calculation` | Expresión matemática para pregunta `calculate` |
| `default` | Respuesta predeterminada para una pregunta |

<p class="note">
Para obtener más información sobre las columnas opcionales en XLSForm, consulta <a class="reference" href="https://support.kobotoolbox.org/es/question_options_xls.html">Opciones de preguntas en XLSForm</a>, <a class="reference" href="https://support.kobotoolbox.org/es/appearances_xls.html">Apariencia de preguntas en XLSForm</a> y <a class="reference" href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

## Cargar y previsualizar tu XLSForm en KoboToolbox

Una vez que hayas terminado de desarrollar tu XLSForm, puedes cargarlo y previsualizarlo en KoboToolbox:

1. Ve a la página de inicio de **Proyecto** en KoboToolbox y haz clic en **NUEVO**.
2. Selecciona **Cargar un XLSForm** y carga tu archivo XLSForm.
3. Ingresa los detalles del proyecto y haz clic en **CREAR PROYECTO**.
4. Haz clic en el botón <i class="k-icon k-icon-view"></i> **Previsualizar**.

Si tu XLSForm contiene un error, aparecerá un mensaje de error, generalmente indicando la fila, pregunta o expresión exacta donde se encuentra el problema. Después de corregir el error en tu XLSForm, deberás cargar el archivo nuevamente.

<p class="note">
Para aprender cómo descargar un XLSForm de KoboToolbox, importar tu XLSForm a través de URL y usar KoboToolbox para validar y probar tu XLSForm, consulta <a class="reference" href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html">Usar XLSForm con KoboToolbox</a>.
</p>