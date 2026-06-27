# Añadir lógica de obligación en un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/required_logic_xls.md" class="reference">20 Mar 2026</a>

La lógica de obligación te permite hacer que una pregunta sea obligatoria si se cumplen condiciones específicas. Por ejemplo, puedes requerir una pregunta de número de teléfono solo si los encuestados aceptan ser contactados en el futuro. Esta opción ofrece más control que simplemente marcar una pregunta como siempre obligatoria o siempre opcional.

<p class="note">
  Para obtener más información sobre las preguntas obligatorias y cómo personalizar el mensaje que se muestra a los encuestados cuando dejan una pregunta obligatoria sin responder, consulta <a href="https://support.kobotoolbox.org/es/question_options_xls.html#required-questions">Opciones de preguntas en XLSForm</a>.
</p>

Este artículo explica cómo agregar condiciones de lógica de obligación en XLSForm, incluyendo cómo hacer que una pregunta sea obligatoria según si otra pregunta fue respondida.

<p class="note">
  <strong>Nota:</strong> Este artículo se centra en agregar lógica de obligación en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agregar lógica de obligación en el editor de formularios de KoboToolbox (Formbuilder), consulta <a href="https://support.kobotoolbox.org/es/question_options.html?highlight=custom+logic#mandatory-response">Opciones de preguntas en el Formbuilder</a>.
  <br><br>
  Para practicar con la lógica de obligación en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar condiciones de lógica de obligación

La lógica de obligación usa <a href="https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing">referencias a preguntas</a> para hacer que las preguntas sean obligatorias según las respuestas anteriores. La pregunta utilizada para definir la lógica de obligación se denomina **pregunta de referencia**.

Para agregar lógica de obligación en XLSForm:
1. Añade una columna `required` a la **hoja survey**.
2. En la fila de la pregunta para la que deseas configurar la lógica de obligación, ingresa la condición que debe cumplirse **para que la pregunta sea obligatoria**.

**hoja survey**

| type         | name      | label                                                                     | required           |
|:--------------|:-----------|:--------------------------------------------------------------------------|:------------------|
| select_one yn | recontact  | Do you agree to being contacted again for another study in the future?    |                    |
| text          | email      | What is your email address?                                               | ${recontact} = 'yes' |
| survey | 

Si un encuestado no responde una pregunta obligatoria, no podrá avanzar a la siguiente página del formulario ni enviarlo.

### Formato de las condiciones de lógica de obligación

El formato de la condición de lógica de obligación variará según el **tipo de la pregunta de referencia**, como se detalla en la tabla a continuación.

| Tipo de pregunta de referencia | Condición de lógica de obligación | Ejemplo |
|:-------------------------|:--------------------|:---------|
| select_one | `${reference_question} = 'choice_name'` | `${consent} = 'yes'` |
| select_multiple | `selected(${reference_question}, 'choice_name')` | `selected(${reasons}, 'other')` |
| integer | `${reference_question}` seguido de un operador lógico (>, <, =) y un número (o una referencia a otra pregunta) | `${age} >= 18` |
| date | `${reference_question}` seguido de un operador lógico (>, <, =) y `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
Para obtener más información sobre cómo construir expresiones de lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

## Agregar lógica de obligación según si una pregunta fue respondida

Además de configurar la lógica de obligación para una respuesta específica, también puedes basarla en si una pregunta fue respondida o dejada en blanco. Esto es útil cuando quieres asegurarte de que al menos una de dos preguntas sea obligatoria.

Las preguntas sin responder se tratan como cadenas vacías, representadas como dos apóstrofos simples `''`. Se pueden usar las siguientes condiciones de lógica de obligación:

| Condición de lógica de obligación | Descripción |
|:---------------------------|:-------------|
| `${reference_question} != ''` | Obligatoria solo si `reference_question` tiene respuesta (no está en blanco). |
| `${reference_question} = ''`  | Obligatoria solo si `reference_question` no tiene respuesta (está en blanco). |

**hoja survey**

| type  | name    | label                                               | required     |
|:------|:--------|:----------------------------------------------------|:-------------|
| note  | contact | Please provide your phone number or email address below. |              |
| text  | phone   | Phone number                                        |              |
| text  | email   | Email address                                       | ${phone} = '' |
| survey |