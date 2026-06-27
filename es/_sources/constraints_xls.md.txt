# Agregar restricciones a un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/c6f58131d275f1d56d26e1aaa599c31a3f1b53d5/source/constraints_xls.md" class="reference">24 Jun 2026</a>

Las restricciones, también conocidas como criterios de validación, son un tipo de lógica de formulario que se utiliza para **limitar las respuestas aceptables a una pregunta en función de una condición predefinida**. Si no se cumple la condición de restricción, se muestra un mensaje de error personalizable que indica al usuario del formulario que ingrese una respuesta válida.

<p class="note">
  Para obtener más información sobre la lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

Este artículo cubre los siguientes temas:
- Agregar restricciones a preguntas en XLSForm
- Combinar múltiples condiciones de restricción
- Personalizar los mensajes de error de restricción
- Restricciones avanzadas en XLSForm

<p class="note">
  <strong>Nota:</strong> Este artículo se centra en agregar restricciones en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para obtener información sobre cómo agregar restricciones en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/validation_criteria.html?highlight=limiting">Añadir criterios de validación en el Formbuilder</a>.
<br><br>
Para practicar con la adición de restricciones en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar una restricción

Las restricciones se construyen utilizando [referencias a preguntas](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing), [operadores de comparación](https://support.kobotoolbox.org/es/form_logic_xls.html#mathematical-and-comparison-operators) y constantes. Las condiciones de restricción deben cumplirse para validar o enviar un formulario. De lo contrario, aparece un **mensaje de error** y se impide que los usuarios avancen a la siguiente página o envíen el formulario.

Para agregar restricciones en XLSForm:
1. Añade una columna `constraint` a la **hoja survey**.
2. En la columna `constraint`, define la condición que debe cumplirse **para que la respuesta sea válida.**
    - Usa un punto `.` para hacer referencia a la pregunta en la fila donde estás agregando una restricción.
    - Usa un [operador de comparación](https://support.kobotoolbox.org/es/form_logic_xls.html#mathematical-and-comparison-operators), seguido de un valor de referencia, para construir una restricción simple.
    - Por ejemplo, `. > 18` restringe una pregunta de tipo `integer` para aceptar únicamente valores mayores que 18.

**hoja survey**

| type     | name       | label                                | constraint       |
|:---------|:-----------|:-------------------------------------|:----------------|
| integer  | age        | What is your age?                    | . >= 18         |
| integer  | household  | How many people live in your household? | . <= 30         |
| integer  | income     | Out of those, how many earn income?  | . <= ${household} |
| survey |

### Formato de los valores de referencia
El valor de referencia en una condición de restricción debe coincidir con el `type` de la pregunta para la que estás agregando una restricción. A continuación se indican los formatos de los valores de referencia para los principales tipos de preguntas:

| Tipo de pregunta | Formato del valor de referencia                                      | Ejemplo                      |
|:----------------|:-----------------------------------------------------------|:------------------------------|
| integer         | Número                                                      | `. > 35`                     |
| select_one      | Nombre de la opción (tal como se define en la hoja choices) entre comillas | `. = 'yes'`                  |
| select_multiple | Nombre de la opción combinado con la <a href="https://support.kobotoolbox.org/es/functions_xls.html">función</a> `selected()`       | `selected(., 'chair')`       |
| date            | Fecha en el formato `date('YYYY-MM-DD')`                    | `. > date('2021-01-01')`    |
| text            | Texto entre comillas (raramente utilizado para restricciones)      | `. != 'Not applicable'`      |

<p class="note">
  Para obtener más información sobre cómo construir expresiones de lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

## Combinar múltiples condiciones de restricción
Es posible combinar varias condiciones de restricción en una sola expresión para determinar si una respuesta es válida. Las condiciones se pueden combinar usando los operadores lógicos `and`, `or` y `not`:

- Usa `and` cuando todas las condiciones deben cumplirse para que una respuesta sea válida.
    - Por ejemplo: <code>. > 18 <strong>and</strong> . < 65</code>
- Usa `or` cuando al menos una condición debe cumplirse para que una respuesta sea válida.
    - Por ejemplo: <code>. < 18 <strong>or</strong> ${student} = 'yes'</code>
- Usa `not` para indicar que una condición o conjunto de condiciones no debe cumplirse (por ejemplo, cuando dos condiciones no pueden ser verdaderas al mismo tiempo para que una respuesta sea válida).
    - Por ejemplo: <code><strong>not</strong>(. < 18 <strong>and</strong> ${household_head} = 'yes')</code>

**hoja survey**

| type     | name   | label              | hint                                        | constraint                                               |
|:---------|:-------|:------------------|:--------------------------------------------|:---------------------------------------------------------|
| integer  | age    | What is your age? | Must be less than 18 or above 65 to participate | <code>. < 18 <strong>or</strong> . > 65</code>         |
| integer  | weight | How much do you weigh? | Must be between 30 and 200 kg               | <code>. >= 30 <strong>and</strong> . <= 200</code>     |
| survey |


## Personalizar los mensajes de error de restricción

De forma predeterminada, cuando el valor de una respuesta en el formulario no cumple la condición de restricción, aparece el mensaje de error "Value not allowed". Se recomienda personalizar este mensaje para informar a los usuarios por qué el valor no es válido, permitiéndoles corregir su entrada.

Para personalizar el mensaje de error de restricción:
1. Añade una columna `constraint_message` a la **hoja survey**.
2. En la columna `constraint_message`, ingresa el texto que deseas mostrar como mensaje de error cuando no se cumplan las condiciones de restricción.

**hoja survey**

| type    | name | label           | constraint | constraint_message     |
|:--------|:-----|:----------------|:-----------|:----------------------|
| integer | age  | What is your age? | . >= 18   | Must be older than 18. |

## Restricciones avanzadas en XLSForm

Más allá de las restricciones básicas, puedes personalizar las condiciones para garantizar la calidad de los datos y adaptarte a muchos escenarios de recolección de datos. Para construir condiciones de restricción más avanzadas en XLSForm:

- Usa paréntesis para combinar más de dos condiciones
- Usa [funciones](https://support.kobotoolbox.org/es/functions_xls.html) para mayor flexibilidad
- Usa [expresiones regulares](https://support.kobotoolbox.org/es/restrict_responses.html) para restringir las respuestas de texto

Algunos ejemplos de criterios de validación más avanzados incluyen:

| Criterio | Descripción |
|:---------|:------------|
| <code>(. >= 18 and . < 130) or (. = 999)</code> | La respuesta debe estar entre 17 y 130 o ser igual a 999 (utilizado frecuentemente para no-respuesta). |
| <code>count-selected(.)<=3</code> | Limita la selección múltiple a un máximo de tres opciones. |
| <code>not(${in_university} = 'yes' and . < 16)</code> | Si la respuesta a `in_university` es 'yes', la respuesta actual debe ser mayor que 16. |
| <code>not(selected(., 'none') and count-selected(.)>1)</code> | La opción 'none' no puede seleccionarse si se ha seleccionado cualquier otra respuesta en una pregunta de tipo `select_multiple`. |
| <code>. < today()</code> | La fecha ingresada debe ser anterior a la fecha de hoy. |
| <code>regex(., '^\d{2}$')</code> | La entrada se restringe a dos números (usando <a href="https://support.kobotoolbox.org/es/restrict_responses.html">expresiones regulares</a>). |
| <code>decimal-time(.)>=0.5</code> | La hora ingresada debe ser a las 12 p.m. o después. |