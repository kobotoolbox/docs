# Incluir respuestas dentro de otra pregunta

Puedes incluir la respuesta de una pregunta (por ejemplo, la respuesta a la pregunta "¿Cuántos años tienes?") dentro de la etiqueta de otra pregunta. Esto puede ser útil por muchas razones en formularios avanzados. Por ejemplo, es posible que quieras confirmar que una respuesta es realmente correcta.

Para referenciar otras preguntas dentro de otra pregunta, es necesario asignarles un nombre fijo a través de la configuración de la pregunta, como `age` o `income`. Al referenciar otras preguntas, usa siempre el nombre único de la pregunta dentro del formato de referencia, como

`${age}` o `${income}`

Simplemente incluye la referencia a la otra pregunta entre las demás palabras de tu etiqueta. Por ejemplo, puedes añadir una nueva pregunta con la etiqueta

`Are you sure you are ${age} years old?`

![image](/images/responses_inside_question/question_name.gif)

También puedes crear una lógica de omisión para esta pregunta, de modo que solo se haga cuando la respuesta de edad sea menor de 18.

Ten en cuenta que si referencias una pregunta que no existe, se generará un error al intentar implementar tu formulario. Asegúrate siempre de referenciar las preguntas con su nombre exacto, que además distingue entre mayúsculas y minúsculas. Por ejemplo, si tu pregunta se llama `age`, no puedes usar `${Age}`. Puedes verificar fácilmente tu formulario haciendo clic en Vista previa en cualquier momento.

![image](/images/responses_inside_question/preview.gif)

**También puedes referenciar la respuesta de una pregunta de tipo Seleccionar una/varias y mostrar la respuesta en lugar del código usando preguntas de Cálculo ocultas**

Si deseas referenciar la respuesta a una pregunta de tipo Seleccionar una/varias y mostrar el texto de la respuesta (por ejemplo, "Totalmente de acuerdo") en lugar de su valor codificado (por ejemplo, "strongly_agr"), puedes:

1. Crear una pregunta de tipo Seleccionar una/varias y asignarle un nombre de referencia fijo a través de la configuración de la pregunta, como `instruction`. Luego, crea una pregunta de Cálculo intermedia e ingresa: `jr:choice-name(${instruction}, '${instruction}')`.

    ![image](/images/responses_inside_question/select_updated.gif)

2. Asigna a esta pregunta de Cálculo un nombre de referencia, como `instruction_calculation`. En tu nueva pregunta, referencia esta pregunta de Cálculo en lugar del nombre asignado a la pregunta de tipo Seleccionar una/varias.

    ![image](/images/responses_inside_question/calculate.gif)

3. Previsualiza y valida el formulario para asegurarte de que todo funciona según lo diseñado.

    ![image](/images/responses_inside_question/preview_calculate.gif)