# Preparar tu formulario para el análisis de datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6e9f496956ced232adb4985272fbee0a6465318d/source/preparing_for_analysis.md" class="reference">15 Jun 2026</a>

Muchos problemas de calidad de datos no comienzan durante el análisis, sino durante la recolección de datos. Las decisiones que se toman al elaborar un formulario, como la estructura de las preguntas, los nombres de las opciones de respuesta y el manejo de los datos faltantes, pueden afectar la cantidad de limpieza y preparación que se necesitará más adelante.

KoboToolbox incluye varias herramientas que **apoyan la recolección de datos de alta calidad** y ayudan a preparar tus datos para el análisis a largo plazo.

Este artículo cubre recomendaciones para **diseñar formularios que produzcan datos más limpios y consistentes**, desde el uso de la lógica de formularios y los cálculos hasta la planificación de los nombres de preguntas y opciones de respuesta, y la descarga de tu XLSForm como diccionario de datos.

## Recolectar datos coherentes y consistentes

Una de las formas más efectivas de mejorar tu análisis es prevenir errores durante la recolección de datos. KoboToolbox incluye funcionalidades de lógica de formularios que pueden ayudarte a recolectar respuestas más precisas y consistentes.

### Criterios de validación

Los [criterios de validación](https://support.kobotoolbox.org/es/glossary.html#validation-criteria) ayudan a garantizar que los encuestados proporcionen respuestas válidas. Por ejemplo, puedes usar criterios de validación para:

- Restringir la edad a valores realistas
- Evitar que las fechas de nacimiento se ingresen en el futuro
- Requerir que los números de teléfono sigan un formato específico

Los criterios de validación son especialmente útiles para preguntas cuyas respuestas deben estar dentro de un rango específico o seguir un formato predecible.

### Lógica de omisión

La [lógica de omisión](https://support.kobotoolbox.org/es/glossary.html#skip-logic) ayuda a garantizar que los encuestados solo vean las preguntas que son relevantes para ellos. Por ejemplo, un encuestado que indica que nunca ha estado embarazado no debería ver preguntas sobre embarazos anteriores.

Hacer las preguntas correctas a las personas correctas mejora la calidad de los datos y reduce la carga sobre los encuestados. También reduce la cantidad de limpieza o eliminación de datos que se necesita más adelante.

<p class="note">
  Para obtener más información sobre la lógica de formularios, consulta <a href="https://support.kobotoolbox.org/es/form_logic.html">Introducción a la lógica de formularios en el Formbuilder</a>.
</p>

## Anticipar el formato de tus exportaciones de datos

La forma en que defines los [nombres de las preguntas](https://support.kobotoolbox.org/es/glossary.html#data-column-name) y los [nombres de las opciones de respuesta](https://support.kobotoolbox.org/es/glossary.html#xml-value) afecta la facilidad con la que puedes trabajar con tus datos después de exportarlos. Los **nombres de las preguntas** se convierten en nombres de columnas en tu conjunto de datos exportado, mientras que los **nombres de las opciones de respuesta** representan los valores de respuesta para las preguntas de selección.

Para obtener mejores resultados, sigue las recomendaciones a continuación.

### Usa un formato claro

Usa nombres de preguntas y opciones de respuesta que sean cortos, informativos, únicos y sin espacios ni caracteres especiales (por ejemplo, `age`, `sex` o `district`).

Los nombres claros hacen que tus datos exportados sean más fáciles de leer, procesar y analizar en herramientas externas.

### Mantén los nombres consistentes

Mantén los nombres de preguntas y opciones de respuesta consistentes en todos los formularios siempre que sea posible. Si varias encuestas recolectan la misma información, **usar los mismos nombres de variables** facilita la combinación y comparación de conjuntos de datos.

- Por ejemplo, si un formulario usa `district` y otro usa `location_district` para el mismo tipo de información, es posible que necesites cambiar el nombre de las variables antes de combinar los conjuntos de datos.

Del mismo modo, usar **nombres de opciones de respuesta** estándar facilita el análisis y reduce la necesidad de recodificar datos más adelante.

- Por ejemplo, puedes usar `0` para "No" y `1` para "Sí" en todas las preguntas relevantes de tu formulario.

### Evita cambiar los nombres después de iniciar la recolección de datos

Una vez que la recolección de datos ha comenzado, **evita modificar los nombres de las preguntas o de las opciones de respuesta.** Cambiarlos puede crear inconsistencias entre los envíos existentes y los nuevos.

Si necesitas actualizar las etiquetas que se muestran a los encuestados, edita la etiqueta de la pregunta pero mantén el nombre de la pregunta igual siempre que sea posible.

<p class="note">
  Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/deploy_form_new_project.html#best-practices-for-deploying-and-redeploying-forms">Buenas prácticas para implementar y volver a implementar formularios</a>.
</p>

### Usa prefijos y sufijos

Cuando los formularios contienen variables relacionadas, las convenciones de nomenclatura consistentes pueden ayudar a organizar tus datos. Considera **usar un prefijo o sufijo** para las preguntas u opciones de respuesta relacionadas con el mismo tema o formato.

Por ejemplo:

- Usa `household_` para preguntas relacionadas con el hogar, como `household_size` o `household_income`
- Usa `_other` para preguntas de "Otro, especifica", como `income_source_other`

<p class="note">
<strong>Nota:</strong>
  Los nombres de las preguntas y opciones de respuesta son los mismos en todos los idiomas del formulario. Esto facilita el análisis de datos multilingües después de la exportación.
</p>

## Anticipar las necesidades del análisis

Al diseñar un formulario, piensa en los análisis que podrías querer realizar más adelante. Planificar con anticipación puede reducir la cantidad de procesamiento necesario después de la exportación.

### Usa cálculos para las variables de análisis

Los [cálculos](https://support.kobotoolbox.org/es/glossary.html#calculation) pueden crear variables que de otro modo requerirían procesamiento adicional después de la exportación. Por ejemplo, puedes usar cálculos para crear:

- La edad del encuestado a partir de la fecha de nacimiento
- Totales del tamaño del hogar
- Índice de masa corporal (IMC)
- Puntajes o indicadores basados en varias respuestas

Crear estas variables durante la recolección de datos puede ahorrar tiempo y mejorar la consistencia entre los análisis.

<p class="note">
  Para obtener más información sobre cómo agregar cálculos, consulta <a href="https://support.kobotoolbox.org/es/calculate_questions.html">Agregar cálculos con el Formbuilder</a>.
</p>

### Planifica los datos faltantes

Al analizar datos, es importante saber **por qué falta información.** Una respuesta puede faltar porque la pregunta fue omitida, la información no estaba disponible, no se recordaba, no era aplicable o fue deliberadamente retenida.

Una buena práctica común es [hacer las preguntas obligatorias](https://support.kobotoolbox.org/es/question_options.html#mandatory-response) y al mismo tiempo proporcionar opciones de respuesta explícitas, como:

- Prefiero no responder
- No sé
- No recuerdo
- No aplica

Esto ayuda a reducir los datos faltantes sin explicación y facilita la interpretación de los resultados durante el análisis.

### Minimiza las respuestas de texto abierto

Las **respuestas de texto abierto** suelen ser difíciles de analizar. Cuando sea posible, usa tipos de preguntas estructuradas en su lugar:

- Usa [preguntas de opción múltiple](https://support.kobotoolbox.org/es/select_one_and_select_many.html) cuando las respuestas se puedan estandarizar en opciones predefinidas.
- Usa [preguntas de fecha](https://support.kobotoolbox.org/es/date_time.html) cuando recolectes fechas del calendario.
- Usa [preguntas GPS](https://support.kobotoolbox.org/es/gps_questions.html) o [preguntas de selección en cascada](https://support.kobotoolbox.org/es/cascading_select.html) cuando recolectes información de ubicación.

Reserva las preguntas de texto para información que no pueda estandarizarse de manera razonable.

## Usa tu XLSForm como diccionario de datos

El [XLSForm](https://support.kobotoolbox.org/es/edit_forms_excel.html) de tu formulario KoboToolbox puede servir como diccionario de datos. Documenta la estructura del formulario, los nombres de las preguntas, los nombres de las opciones de respuesta, las etiquetas, las traducciones, los tipos de preguntas y la lógica del formulario.

Para descargar el XLSForm de tu formulario:

1. Abre tu proyecto.
2. Ve a **FORMULARIO.**
3. Haz clic en <i class="k-icon-more"></i> **Otras acciones.**
4. Haz clic en <i class="k-icon-file-xls"></i> **Descargar XLS.**

Cada fila de la hoja `survey` representa una pregunta de tu formulario, y cada columna proporciona información sobre esa pregunta, como el nombre de la pregunta, la etiqueta, el tipo, las traducciones y la lógica del formulario relevante. Para las preguntas de selección, las [opciones de respuesta](https://support.kobotoolbox.org/es/option_choices_xls.html) se encuentran en la hoja `choices`.

Mantener tu XLSForm junto con tu conjunto de datos exportado puede facilitar la interpretación de las variables, la comprensión de los valores de respuesta y la documentación de tu flujo de trabajo de análisis.

<p class="note">
  Para obtener más información sobre XLSForm, consulta <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">Crear un XLSForm</a> y <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html">Usar XLSForm con KoboToolbox</a>.
</p>