# Añadir lógica de salto a un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/0586118b5f55f20287bc6db496832b14bbfc6239/source/skip_logic_xls.md" class="reference">5 Jun 2026</a>

La lógica de salto, también conocida como lógica de relevancia, te permite **determinar cuándo se mostrará una pregunta o un grupo de preguntas** en el formulario, en función de una pregunta anterior o del resultado de un cálculo. Por ejemplo, puedes usarla para hacer preguntas de seguimiento solo a un subconjunto de encuestados, o para ocultar secciones enteras de un formulario si no son relevantes.

<p class="note">
  Para obtener más información sobre la lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

Este artículo cubre los siguientes temas:
- Agregar lógica de salto a preguntas individuales
- Combinar múltiples condiciones de lógica de salto
- Agregar lógica de salto según si una pregunta fue respondida
- Agregar lógica de salto a grupos de preguntas

<p class="note">
  <strong>Nota:</strong> Este artículo se centra en agregar lógica de salto en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agregar lógica de salto en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/skip_logic.html">Añadir lógica de salto al Formbuilder</a>.
    <br><br>
Para practicar con la lógica de salto en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar condiciones de lógica de salto a preguntas individuales

La lógica de salto utiliza la [referencia a preguntas](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing) para mostrar únicamente las preguntas que son relevantes para el encuestado según sus respuestas anteriores. La pregunta utilizada para definir la lógica de relevancia se denomina **pregunta de referencia**.

Para agregar lógica de salto en XLSForm:
1. Añadir una columna `relevant` a la **hoja survey**.
2. En la fila de la pregunta que deseas mostrar u ocultar, ingresa la condición que debe cumplirse **para que la pregunta se muestre.**

**hoja survey**

| type         | name     | label             | relevant     |
|:--------------|:----------|:------------------|:--------------|
| integer       | age       | ¿Cuántos años tienes?  |               |
| select_one yn | married   | ¿Estás casado/a?  | ${age} > 18   |
| survey |

En el ejemplo anterior, `${age}` es la pregunta de referencia, y la respuesta a `${age}` debe ser mayor que 18 para que se muestre la pregunta "¿Estás casado/a?".

### Formato de las condiciones de lógica de salto

El formato de la condición de lógica de salto variará según el **tipo de la pregunta de referencia**, como se detalla en la tabla a continuación.

| Tipo de pregunta de referencia | Condición de lógica de salto | Ejemplo |
|:-------------------------|:--------------------|:---------|
| select_one | `${pregunta_de_referencia} = 'nombre_de_opción'` | `${consent} = 'yes'` |
| select_multiple | `selected(${pregunta_de_referencia}, 'nombre_de_opción')` | `selected(${reasons}, 'other')` |
| integer | `${pregunta_de_referencia}` seguido de un operador lógico (>, <, =) y un número (o una referencia a otra pregunta) | `${age} >= 18` |
| date | `${pregunta_de_referencia}` seguido de un operador lógico (>, <, =) y `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
  Para obtener más información sobre cómo construir expresiones de lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

## Combinar múltiples condiciones de lógica de salto

Se pueden combinar múltiples condiciones de relevancia en una sola expresión para determinar cuándo se muestra una pregunta en función de una respuesta anterior. Las condiciones se pueden combinar usando los operadores lógicos `and`, `or` y `not`:

- Usa `and` cuando todas las condiciones deben cumplirse para que se muestre una pregunta.
    - Por ejemplo: <code>${age} > 18 <strong>and</strong> ${student} = 'no'</code>
- Usa `or` cuando al menos una condición debe cumplirse para que se muestre una pregunta.
    - Por ejemplo: <code>${age} < 18 <strong>or</strong> ${student} = 'yes'</code>
- Usa `not` para indicar que una condición o conjunto de condiciones no debe cumplirse (por ejemplo, cuando dos condiciones no pueden ser verdaderas al mismo tiempo para que se muestre una pregunta).
    - Por ejemplo: <code><strong>not</strong>(${age} > 18 <strong>and</strong> ${student} = 'yes')</code>

**hoja survey**

| type         | name     | label              | relevant                          |
|:--------------|:----------|:-------------------|:----------------------------------|
| integer       | age       | ¿Cuál es tu edad?  |                                   |
| select_one yn | employed  | ¿Estás empleado/a?  | ${age} >= 16 <strong>and</strong> ${age} <= 75     |
| survey |

## Agregar lógica de salto según si una pregunta fue respondida

Además de agregar lógica de salto basada en una respuesta específica, puedes agregar lógica de salto según si una pregunta fue respondida o dejada en blanco. Esto puede ser útil para agregar preguntas de seguimiento, o cuando usas [preguntas de consentimiento](https://support.kobotoolbox.org/es/select_one_and_select_many.html) en tu formulario.

Las preguntas sin respuesta se tratan como cadenas vacías, representadas como dos apóstrofos simples `''`. Se pueden usar las siguientes condiciones de lógica de salto:

| Condición de lógica de salto | Descripción |
|:---------------------|:-------------|
| `${pregunta_de_referencia} != ''` | Mostrar solo si `pregunta_de_referencia` tiene respuesta (no está en blanco). |
| `${pregunta_de_referencia} = ''` | Mostrar solo si `pregunta_de_referencia` no tiene respuesta (está en blanco). |

**hoja survey**

| type         | name      | label                | relevant             |
|:--------------|:-----------|:---------------------|:---------------------|
| text          | why_joined | ¿Por qué te uniste?    |                      |
| select_one yn | benefits   | ¿Estás viendo beneficios? | ${why_joined} != '' |
| survey |

## Agregar condiciones de lógica de salto a grupos de preguntas

La lógica de salto también se puede aplicar a grupos de preguntas, además de a preguntas individuales. Al aplicar lógica de salto a un grupo, se mostrarán u ocultarán todas las preguntas del grupo en función de las respuestas anteriores.

Para agregar lógica de salto a grupos de preguntas:
1. Añadir una columna `relevant` a la **hoja survey**.
2. En la fila `begin_group` del grupo de preguntas que deseas mostrar u ocultar, ingresa la condición que debe cumplirse **para que el grupo se muestre.**

**hoja survey**

| type         | name        | label                                         | relevant            |
|:-------------|:------------|:---------------------------------------------|:-------------------|
| select_one yn | joined     | ¿Te uniste a la asociación?                |                     |
| begin_group  | association | Participación en la asociación                    | ${joined} = 'yes'  |
| date         | date_joined | ¿Cuándo te uniste a la asociación?           |                     |
| select_one yn | voted      | ¿Has votado alguna vez en alguna elección de la asociación? |                     |
| end_group    |             |                                              |                     |
| survey |

## Resolución de problemas
<details>
<summary><strong>La lógica de salto no funciona como se esperaba con preguntas de opción múltiple</strong></summary>
Al agregar lógica de salto basada en una pregunta de opción múltiple, usar <code>${question} = 'option1'</code> solo funcionará si la Opción 1 es <strong>la única respuesta seleccionada</strong>. Para aplicar lógica de salto cuando se selecciona la Opción 1, independientemente de si también se seleccionan otras opciones, usa la función <code>selected()</code>: <code>selected(${question}, 'option1')</code> <br><br>
Esto es común al agregar una pregunta de texto abierto "Especificar otro" después de una pregunta de opción múltiple. Por ejemplo, si quieres que la pregunta "Especificar otro" aparezca siempre que se seleccione "Otro", usa: <code>selected(${question}, 'other')</code>

</details>