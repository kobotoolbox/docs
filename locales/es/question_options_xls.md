# Opciones de preguntas en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/question_options_xls.md" class="reference">23 Apr 2026</a>

Al diseñar un formulario en XLSForm, puedes personalizar las preguntas añadiendo sugerencias, configurando aspectos, haciendo una pregunta obligatoria y más. Para ello, puedes agregar nuevas columnas en la **hoja survey** de tu XLSForm. Estas columnas se pueden añadir en cualquier lugar de la hoja, siempre que el nombre de la columna se escriba exactamente como se requiere.

Este artículo cubre las opciones de preguntas más comunes y cómo añadirlas a tu XLSForm, incluyendo sugerencias de preguntas, preguntas obligatorias, respuestas predeterminadas y parámetros de preguntas.

<p class="note">
  <strong>Nota:</strong> Este artículo se centra en definir opciones de preguntas en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para obtener información sobre las opciones de preguntas en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/question_options.html">Opciones de preguntas en el Formbuilder</a>.
<br><br>
Para practicar con las opciones de preguntas en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Sugerencias de preguntas

Las **sugerencias de preguntas** te permiten añadir instrucciones o información adicional a tu formulario. Hay dos tipos de sugerencias que puedes añadir en XLSForm:
- Las **sugerencias comunes** se usan para proporcionar información adicional a los encuestados o encuestadores directamente en el formulario. Siempre son visibles y se muestran debajo de la etiqueta de la pregunta.
- Las **sugerencias adicionales** se usan para proporcionar información adicional durante el desarrollo del formulario, la capacitación de encuestadores o la recolección de datos. No se muestran de forma predeterminada.

### Añadir sugerencias de preguntas en XLSForm

Para añadir una **sugerencia común** en XLSForm:
1. Añade una columna `hint` a la hoja survey.
2. En la misma fila que tu pregunta, ingresa el texto que debe mostrarse como sugerencia para esa pregunta.

Para añadir una **sugerencia adicional** en XLSForm:
1. Añade una columna `guidance_hint` a la hoja survey.
2. En la misma fila que tu pregunta, ingresa el texto que debe incluirse como orientación adicional.

**hoja survey**

| type | name | label | hint | guidance_hint |
| :--- | :--- | :--- | :--- | :--- |
| integer | height | What is your height? | In centimeters | If the respondent does not know their height, enter 0 |
| survey |

<p class="note">
<strong>Nota:</strong> Las sugerencias de preguntas también se pueden traducir a varios idiomas. Para más información sobre la traducción de formularios, consulta <a class="reference" href="https://support.kobotoolbox.org/es/language_xls.html">Añadir traducciones en XLSForm</a>.
</p>

### Mostrar sugerencias adicionales en KoboCollect

En los formularios web, las sugerencias adicionales aparecen en una sección desplegable **Más detalles**. En KoboCollect, están ocultas de forma predeterminada, pero puedes [cambiar la configuración de tu proyecto](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings) para mostrarlas siempre o en una sección desplegable.

Para mostrar sugerencias adicionales en KoboCollect, sigue los pasos a continuación:
1. Toca el **ícono del proyecto** en la esquina superior derecha de la pantalla.
2. Toca **Ajustes**.
3. En **Manejo de formularios**, selecciona **Mostrar orientación para preguntas**.
4. Elige una opción de visualización: **No**, **Sí - siempre visible** o **Sí - contraída**.

<p class="note">
<strong>Nota:</strong> Las sugerencias adicionales siempre se muestran en los formularios impresos.
</p>

## Preguntas obligatorias

De forma predeterminada, las preguntas de un formulario son opcionales. Configurar una pregunta como **obligatoria** hace que el encuestado deba responderla. Esto puede ser útil para garantizar que los envíos estén completos y evitar datos faltantes.

<p class="note">
<strong>Nota:</strong> Las condiciones de lógica de omisión tienen prioridad sobre la configuración de <strong>obligatorio</strong>, lo que significa que si una pregunta obligatoria está oculta por la lógica de omisión, ya no es obligatorio responderla.
</p>

Para configurar una pregunta como obligatoria en XLSForm:
1. Añade una columna `required` a la hoja survey.
2. En la columna `required`, ingresa cualquiera de los siguientes valores: `TRUE`, `true` o `yes`.
3. Para preguntas opcionales, deja la columna `required` en blanco o ingresa cualquiera de los siguientes valores: `FALSE`, `false` o `no`.

Si un encuestado no responde una pregunta obligatoria, no podrá pasar a la siguiente página ni enviar el formulario. Se mostrará el mensaje obligatorio predeterminado "Este campo es obligatorio".

<p class="note">
<strong>Nota:</strong> Solo las preguntas que requieren una entrada deben marcarse como obligatorias en tu XLSForm. Si las preguntas de tipo <code>note</code> se marcan como obligatorias, no podrás continuar ni enviar el formulario.
</p>

### Cambiar el mensaje obligatorio predeterminado

Puedes cambiar el mensaje obligatorio predeterminado en tu XLSForm siguiendo los pasos a continuación:

1. Añade una columna `required_message` a la hoja survey.
2. Ingresa el texto que deseas mostrar cuando los usuarios dejen una pregunta obligatoria en blanco.

**hoja survey**

| type | name | label | required | required_message |
| :--- | :--- | :--- | :--- | :--- |
| select_one education | education_level | What is the highest level of education you have completed? | TRUE | |
| integer | age | What is your age? | TRUE | Please respond to this question before continuing. |
| survey |

<p class="note">
<strong>Nota:</strong> Se puede usar lógica de formulario personalizada para hacer que una pregunta sea obligatoria u opcional según una respuesta anterior. Para obtener más información sobre la lógica de obligación basada en condiciones, consulta <a class="reference" href="https://support.kobotoolbox.org/es/required_logic_xls.html">Añadir lógica de obligación en un XLSForm</a>.
</p>

## Respuestas predeterminadas

Una **respuesta predeterminada** rellena una pregunta con una respuesta predefinida basada en una respuesta común o esperada. La respuesta predeterminada puede ser fija o [determinada dinámicamente](https://support.kobotoolbox.org/es/question_options_xls.html#setting-dynamic-default-responses) según la respuesta a una pregunta anterior.

La respuesta predeterminada se registrará como la respuesta final cuando se envíe el formulario, **a menos que el encuestado la modifique** durante la recolección de datos. Para evitar que los encuestados editen una respuesta predeterminada, añade una columna `read_only` y configúrala como `TRUE`.

<p class="note">
<strong>Nota:</strong> Aunque las respuestas predeterminadas pueden hacer que la recolección de datos sea más eficiente al rellenar previamente el formulario con respuestas esperadas o comunes, también pueden introducir sesgos o errores en los datos, y deben usarse con precaución.
</p>

Para configurar una respuesta predeterminada fija en XLSForm:
1. Añade una columna `default` a la hoja survey.
2. Ingresa la respuesta predeterminada siguiendo el [formato apropiado](https://support.kobotoolbox.org/es/question_options_xls.html#default-response-format) para el tipo de pregunta.

**hoja survey**

| type | name | label | default |
| :--- | :--- | :--- | :--- |
| text | name | What is your name? | John Doe |
| integer | age | What is your age? | 50 |
| select_one marital_options | marital_status | What is your marital status? | married |
| select_multiple income_options | income_sources | What are your sources of income? | formal_work farm_business |
| date | dob | When were you born? | 1990-03-25 |
| date | interview_date | When was this interview conducted? | today() |
| survey |

### Formato de la respuesta predeterminada

El formato de la respuesta predeterminada depende del tipo de pregunta y los datos que se recolectan:

| Tipo de pregunta | Formato de la respuesta predeterminada |
| :--- | :--- |
| `integer` | Número |
| `text` | Texto (sin comillas) |
| `select_one` | **Nombre** de la opción (tal como se define en la hoja choices) |
| `select_multiple` | **Nombre(s)** de la(s) opción(es), separados por un **espacio** si hay varios |
| `date` | Fecha en formato YYYY-MM-DD. Si es necesario, añade una comilla simple (') antes de la fecha en Excel para evitar posibles problemas de formato. |

### Configurar respuestas predeterminadas dinámicas

Las respuestas predeterminadas ingresadas en el campo `default` deben ser valores fijos. Para configurar una **respuesta predeterminada dinámica** basada en una respuesta anterior, usa las columnas `calculation` y `trigger` en lugar de la columna `default`:
1. En la columna `calculation`, ingresa la **referencia a la pregunta** que rellenará dinámicamente la respuesta predeterminada.
2. En la columna `trigger`, ingresa la pregunta que activará el cálculo.
    - Normalmente, esta sería la misma pregunta referenciada en la columna `calculation`, de modo que cualquier cambio en la pregunta de activación también actualizará la respuesta predeterminada.

**hoja survey**

| type | name | label | calculation | trigger |
| :--- | :--- | :--- | :--- | :--- |
| text | hh_name | Name of the head of household | | |
| text | phone | Household phone number | | |
| text | phone_name | Name of the phone owner | ${hh_name} | ${hh_name} |
| survey |

## Parámetros de preguntas

Los parámetros de preguntas en XLSForm te permiten ajustar el comportamiento de tus preguntas más allá de la configuración básica.

Para añadir parámetros de preguntas en XLSForm:
1. Añade una columna `parameters` a la hoja survey.
2. Ingresa el [parámetro](https://support.kobotoolbox.org/es/question_options_xls.html#common-question-parameters) apropiado para tu tipo de pregunta.
3. Algunos parámetros se pueden combinar y aplicar a la misma pregunta. Para combinar parámetros, ingrésalos en la misma celda separados por un espacio.

**hoja survey**

| type | name | label | parameters |
| :--- | :--- | :--- | :--- |
| select_one reasons | reasons | Please select all reasons that apply. | randomize=true |
| range | phone | Please select a number between 1 and 5. | start=1 end=5 step=1 |
| survey |

### Parámetros de preguntas más comunes

Los distintos tipos de preguntas en XLSForm tienen diferentes parámetros. Los más comunes son:

| Parámetro | Tipo de pregunta | Descripción |
| :--- | :--- | :--- |
| `randomize=true` | `rank`, `select_one`, `select_multiple` | Aleatoriza el orden de las opciones de respuesta |
| `start=1 end=5 step=1` | `range` | Define el valor mínimo, el valor máximo y el intervalo entre números |
| `capture-accuracy=20` | `geopoint` | Especifica la [precisión GPS](https://support.kobotoolbox.org/es/collect_gps.html#accuracy-of-gps-coordinates) mínima aceptable (en metros) para capturar automáticamente una ubicación. El valor predeterminado es 5 m. |
| `warning-accuracy=50` | `geopoint` | Activa un mensaje de advertencia si la [precisión GPS](https://support.kobotoolbox.org/es/collect_gps.html#accuracy-of-gps-coordinates) (en metros) no está dentro del umbral de precisión especificado. El valor predeterminado es 100 m. |
| `max-pixels=480` | `image` | Limita el máximo de píxeles de una foto para reducir el tamaño del archivo de imagen y mejorar la velocidad de carga |
| `quality=low` | `audio` | Captura una grabación de audio de menor calidad |
| `quality=voice-only` | `audio` | Captura la grabación de audio de la menor calidad posible |

## Opciones de preguntas adicionales

Los XLSForms pueden incluir columnas adicionales en la hoja survey para formularios y funcionalidades más avanzadas. A continuación se enumeran algunas.

| Columna XLSForm | Descripción |
| :--- | :--- |
| `read_only` | Si se ingresa `yes` en el campo `read_only`, el encuestado no puede editar la pregunta. Los campos `read_only` se pueden combinar con los campos `default` o `calculation` para mostrar información al encuestado. |
| `trigger` | La columna trigger se puede usar para ejecutar un cálculo solo cuando cambia la respuesta a otra pregunta visible en el formulario. Para más información, consulta la <a href="https://xlsform.org/en/#trigger">documentación de XLSForm</a>. |
| `body::accept` | Para limitar o ampliar los tipos de archivo aceptados en las preguntas de tipo `file`, especifica las extensiones de archivo en la columna `body::accept`, separadas por una coma (por ejemplo, .pdf, .doc, .png). |
| `hxl` | Para incluir etiquetas del <a href="https://hxlstandard.org">Lenguaje de Intercambio Humanitario</a> (HXL) en tu formulario, especifica la etiqueta (y el atributo opcional) en la columna `hxl`, siguiendo el formato `#etiqueta` o `#etiqueta+atributo`. |

También se pueden añadir otras columnas para incorporar lógica de formulario en tu XLSForm.

<p class="note">
    Para obtener más información sobre cómo añadir lógica de formulario, consulta <a href="https://support.kobotoolbox.org/es/skip_logic_xls.html">Añadir lógica de salto a un XLSForm</a>, <a href="https://support.kobotoolbox.org/es/constraints_xls.html">Agregar restricciones a un XLSForm</a>, <a href="https://support.kobotoolbox.org/es/required_logic_xls.html">Añadir lógica de obligación en un XLSForm</a>, <a href="https://support.kobotoolbox.org/es/choice_filters_xls.html">Agregar filtros de selección a un XLSForm</a> y <a href="https://support.kobotoolbox.org/es/calculations_xls.html">Agregar cálculos a un XLSForm</a>.
</p>