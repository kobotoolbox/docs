# Introducción a la lógica de formularios en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/form_logic_xls.md" class="reference">20 mar 2026</a>

La lógica de formularios controla el flujo y el comportamiento de tu formulario en función de las respuestas a preguntas anteriores. Te permite crear formularios dinámicos que se adaptan a la información ingresada por los usuarios. Por ejemplo, puedes usar la lógica de formularios para mostrar preguntas específicas solo cuando sean relevantes, validar respuestas o realizar cálculos automáticamente.

Los principales tipos de lógica de formularios son:
- **Lógica de omisión:** Controla cuándo se muestran u ocultan las preguntas en función de respuestas anteriores.
- **Restricciones:** Validan las respuestas para asegurarse de que cumplan con las reglas o criterios definidos.
- **Filtros de selección:** Muestran solo las opciones de respuesta relevantes en función de respuestas anteriores.
- **Cálculos:** Generan valores automáticamente mediante expresiones matemáticas o lógicas.
- **Lógica requerida:** Define cuándo una pregunta debe ser respondida obligatoriamente.

La lógica de formularios se construye usando **expresiones**, que combinan **referencias a preguntas**, **operadores**, **funciones** y **constantes**. La expresión se evalúa como TRUE o FALSE para controlar el comportamiento del formulario.

<p class="note">
  Este artículo presenta los componentes básicos de la lógica de formularios en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>, incluyendo la referencia a preguntas, los operadores y las funciones. Para obtener más información sobre cada tipo de lógica de formularios, consulta los artículos de ayuda sobre <a href="https://support.kobotoolbox.org/es/skip_logic_xls.html">lógica de omisión</a>, <a href="https://support.kobotoolbox.org/es/required_logic_xls.html">lógica requerida</a>, <a href="https://support.kobotoolbox.org/es/constraints_xls.html">restricciones</a>, <a href="https://support.kobotoolbox.org/es/choice_filters_xls.html">filtros de selección</a> y <a href="https://support.kobotoolbox.org/es/calculations_xls.html">cálculos</a> en XLSForm.
</p>

## Referencia a preguntas

La referencia a preguntas te permite incorporar la respuesta a una pregunta anterior en la etiqueta o la lógica de una pregunta posterior. La referencia a preguntas se usa con frecuencia en formularios avanzados:

- **En etiquetas o sugerencias de preguntas:** Por ejemplo, puedes incluir el nombre del hijo de un encuestado en preguntas posteriores sobre ese hijo.
- **En la lógica de formularios:** Por ejemplo, puedes mostrar u ocultar una pregunta en función de una respuesta anterior, o validar una respuesta comparándola con una anterior.

La referencia a preguntas usa el formato **${question_name}**, donde `question_name` se reemplaza con el nombre único de la pregunta referenciada.

Si una referencia a una pregunta contiene un error ortográfico o es incorrecta, aparecerá un mensaje de error al previsualizar o enviar el formulario.

<p class="note">
  <strong>Nota:</strong> Al referenciar una pregunta dentro de su propia lógica (es decir, en su propia fila), se puede usar un punto <code>.</code> como atajo.
</p>

**hoja survey**

| type     | name            | label                                                                 | constraint              |
|:-----------|:-----------------|:------------------------------------------------------------------------|:--------------------------|
| integer   | household_size  | How many people live in your household?                                |                          |
| integer   | total_under18   | Out of the ${household_size} people, how many are under the age of 18? | . < ${household_size}    |
| survey | 

## Operadores matemáticos y de comparación

Los **operadores matemáticos** se usan para realizar cálculos aritméticos con valores numéricos en el formulario. Los operadores matemáticos en XLSForm incluyen:

| Operador | Descripción                          |
|:-----------|:--------------------------------------|
| `+`       | Suma                                 |
| `-`       | Resta                                |
| `*`       | Multiplicación                       |
| `div`     | División                             |
| `mod`     | Módulo (resto de una división)       |

Los **operadores de comparación** se usan para comparar valores. Los operadores de comparación en XLSForm incluyen:

| Operador | Descripción                        |
|:-----------|:------------------------------------|
| `=`       | Igual a                            |
| `>`       | Mayor que                          |
| `<`       | Menor que                          |
| `>=`      | Mayor o igual que                  |
| `<=`      | Menor o igual que                  |
| `!=`      | Distinto de                        |

## Combinar condiciones con operadores lógicos

Los **operadores lógicos** se pueden usar en XLSForm para combinar múltiples condiciones. Los operadores lógicos en XLSForm incluyen:
- **and** (todas las condiciones deben cumplirse)
- **or** (al menos una de las condiciones debe cumplirse)
- **not** (las condiciones no deben cumplirse)

**hoja survey**

| type     | name           | label                                | constraint                         |
|:-----------|:----------------|:--------------------------------------|:------------------------------------|
| integer   | household_size | How many people live in your household? |                                    |
| integer   | total_under18  | How many are under the age of 18?    | . < ${household_size} <strong>and</strong> . >= 0   |
| survey |

## Funciones

Las funciones son operaciones predefinidas que se usan para realizar cálculos o manipular datos en XLSForm. Las funciones hacen que los cálculos y la lógica de formularios sean más eficientes al realizar automáticamente tareas complejas, como redondear valores, calcular potencias o extraer la fecha actual.

<p class="note">
Para consultar una lista completa de funciones en XLSForm, ver <a href="https://support.kobotoolbox.org/es/functions_xls.html">Usar funciones en XLSForm</a>.
</p>

## Regex

Una expresión regular (regex) es un patrón de búsqueda que se usa para identificar caracteres específicos dentro de una cadena de texto. Se usa ampliamente para validar, buscar, extraer y restringir texto en la mayoría de los lenguajes de programación, incluyendo en KoboToolbox.

Las expresiones regulares se pueden usar en **restricciones** para controlar la longitud y los caracteres ingresados en una pregunta (por ejemplo, limitar la entrada de un número de teléfono a exactamente 10 dígitos, controlar el formato de números de identificación o verificar que una dirección de correo electrónico sea válida). También se pueden usar en **cálculos** y en otros tipos de lógica de formularios.

En KoboToolbox, las expresiones regulares se evalúan con la función `regex(., ' ')`, donde la expresión regular se ingresa entre apóstrofos y el punto `.` representa la pregunta actual. `regex(., ' ')` devuelve TRUE si se cumple la expresión regular, y FALSE en caso contrario.

<p class="note">
  Para obtener más información sobre el uso de expresiones regulares en KoboToolbox, ver <a href="https://support.kobotoolbox.org/es/restrict_responses.html">Usar expresiones regulares en XLSForm</a>.
</p>