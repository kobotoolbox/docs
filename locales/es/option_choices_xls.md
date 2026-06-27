# Administrar opciones de respuesta en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/1b55b2580defd73765e9c2ad608141a3428ee504/source/option_choices_xls.md" class="reference">4 Jan 2026</a>

XLSForm simplifica la creación y el manejo de **listas de opciones de respuesta** para formularios de encuesta. Esto es especialmente útil para listas largas o repetitivas, como nombres de países o ciudades. Las opciones de respuesta se definen para preguntas de tipo `select_one`, `select_multiple` o `rank` [preguntas](https://support.kobotoolbox.org/es/question_types_xls.html#select-question-types).

Este artículo explica cómo definir y administrar opciones de respuesta en XLSForm para formularios complejos, incluyendo las mejores prácticas para definir nombres de opciones.

<p class="note">
Para aprender más sobre la elaboración de formularios en XLSForm, consulta <a href="getting_started_xlsform.html">Crear un XLSForm</a>.
</p>

## Definir opciones de respuesta en XLSForm
Las opciones de respuesta se definen en la **hoja choices** de tu XLSForm. La **hoja choices** incluye tres columnas obligatorias:

| Columna | Descripción |
| :---------  | :--------  |
| `list_name` | Identificador único para una lista de opciones de respuesta, que vincula la pregunta en la **hoja survey** con su lista de opciones en la **hoja choices**. |
| `name` | Nombre corto y único utilizado para identificar cada opción de respuesta. |
| `label` | Texto de la opción tal como se mostrará en el formulario. |

Para definir una lista de opciones de respuesta en XLSForm:

1. En la **hoja choices**, ingresa el **nombre de la lista de opciones** en la columna `list_name`.
2. Ingresa un `name` corto y un `label` para cada opción, usando el mismo `list_name` para todas las opciones de la lista.

**hoja choices**

| list_name | name | label |
| :---------  | :---------  | :---------  |
| marital_options | single | Single |
| marital_options | married | Married |
| marital_options | separated_divorced | Separated/Divorced |
| marital_options | widowed | Widowed |
| choices |

3. En la **hoja survey**, agrega tu pregunta de encuesta. En la columna `type`, ingresa el tipo de pregunta seguido de un espacio y luego el `list_name` de tu lista de opciones.
    - Una lista de opciones puede reutilizarse en múltiples preguntas de la **hoja survey**.

**hoja survey**

| type | name | label |
| :---------  | :---------  | :---------  |
| acknowledge | consent | Do you agree to proceed with the interview? |
| select_one marital_options | marital_status | What is your marital status? |
| survey |

## Mejores prácticas para definir nombres de opciones

Cuando los datos se descargan en [formato de valores y encabezados XML](https://support.kobotoolbox.org/es/export_download.html#value-and-header-format), cada pregunta aparece como su propia variable o columna en el conjunto de datos. Los valores dentro de cada columna son los **nombres de las opciones** definidos en tu **hoja choices**, en lugar de las etiquetas completas que se muestran a los encuestados. Este formato es recomendado para el análisis, ya que proporciona nombres de variables cortos y consistentes, y valores codificados más fáciles de trabajar que las etiquetas completas de preguntas u opciones.

Al definir nombres de opciones:
- Usa solo **letras, números y guiones bajos**. No se permiten espacios ni caracteres especiales.
- Evita cadenas de texto muy largas o complejas, ya que estos valores aparecerán en tu conjunto de datos exportado y pueden usarse en la [lógica del formulario](https://support.kobotoolbox.org/es/form_logic_xls.html).
- Mantén los nombres **consistentes** entre listas para facilitar el análisis de datos.


## Administrar listas de opciones en XLSForm

### Reutilizar listas de opciones
Usar `list_name` en XLSForm te permite **reutilizar listas de opciones** en múltiples preguntas, eliminando la necesidad de ingresarlas manualmente cada vez. Por ejemplo, puedes crear una lista de opciones `yes_no` y aplicarla a todas tus preguntas de Sí/No. Esto ayuda a elaborar formularios de manera más eficiente y consistente.

### Traducir listas de opciones

XLSForm simplifica la traducción de listas de opciones. Puedes agregar múltiples etiquetas para diferentes idiomas, con cada traducción en una columna `label` separada. Los nombres de las opciones subyacentes permanecen iguales, lo que garantiza que el conjunto de datos exportado sea consistente entre traducciones y facilita el análisis.

<p class="note">
Para aprender más sobre cómo agregar traducciones en XLSForm, consulta <a href="language_xls.html">Añadir traducciones en XLSForm</a>.
</p>

### Archivos multimedia como opciones de respuesta

Además de texto, las opciones de respuesta en XLSForm también pueden ser **archivos multimedia**, como imágenes, audio o video. Esto mejora la experiencia de la encuesta al proporcionar indicaciones visuales o auditivas a los encuestados.

<p class="note">
Para aprender más sobre el uso de archivos multimedia como opciones de respuesta, consulta <a href="media.html">Agregar archivos multimedia a un XLSForm</a>.
</p>

### Filtrar listas de opciones

XLSForm te permite filtrar listas de opciones de respuesta según las respuestas a preguntas anteriores. Esta funcionalidad, conocida como **filtros de selección**, puede usarse de diversas maneras. Por ejemplo, puede utilizarse para **preguntas de selección en cascada**, donde la lista de opciones de una pregunta secundaria (p. ej., ciudades) se filtra según la respuesta a una pregunta principal (p. ej., país). También puede usarse para filtrar una pregunta de selección múltiple y mostrar solo las opciones seleccionadas en una pregunta anterior.

<p class="note">
Para aprender más sobre cómo filtrar listas de opciones en XLSForm, consulta <a href="choice_filters_xls.html">Agregar filtros de selección a un XLSForm</a>.
</p>

### Duplicar nombres de opciones

Dentro de una lista de opciones de respuesta, **los nombres de las opciones deben ser únicos**. Sin embargo, el mismo nombre de opción puede reutilizarse en diferentes listas. Por ejemplo, una lista de opciones `yes_no` y una lista `yes_no_maybe` pueden incluir ambas los nombres de opciones `yes` y `no`.

De forma predeterminada, implementar un formulario con nombres de opciones repetidos en la misma lista generará un error. Sin embargo, cuando se usan filtros de selección, es posible que necesites permitir nombres de opciones duplicados dentro de una lista. Para habilitar esto, activa la configuración `allow_choice_duplicates` en tu **hoja settings**.

<p class="note">
Para más información, consulta <a href="form_settings_xls.html">Configuración de formularios en XLSForm</a>.
</p>

### Administrar listas de opciones extensas

Para listas de opciones muy grandes, que contienen cientos o miles de opciones, se recomienda usar los tipos de pregunta `select_one_from_file` o `select_multiple_from_file`, que vinculan una pregunta de encuesta a un **archivo externo** que contiene la lista de opciones. Este enfoque es más eficiente que ingresar las opciones manualmente en el XLSForm, ayuda a evitar tiempos de carga lentos y XLSForms de gran tamaño, y simplifica el manejo o la edición de conjuntos de opciones extensos.

<p class="note">
Para aprender más sobre listas de opciones externas en XLSForm, consulta <a href="select_from_file_xls.html">Seleccionar opciones de un archivo externo en XLSForm</a>.
</p>