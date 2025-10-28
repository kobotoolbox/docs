# Incluir respuestas dentro de otra pregunta
<a href="../responses_inside_question.html">Read in English</a> | <a href="../fr/responses_inside_question.html">Lire en français</a> | <a href="../ar/responses_inside_question.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/aca19282c9a46e952209d16a75fce9e800f6ea1c/source/responses_inside_question.md" class="reference">5 Oct 2020</a>

Puedes incluir la respuesta de una pregunta (como incluir la respuesta de la pregunta '¿Cuántos años tienes?') dentro de la etiqueta de otra pregunta. Esto puede ser útil por muchas razones en formularios avanzados. Por ejemplo, es posible que desees confirmar que una respuesta es realmente correcta.

Hacer referencia a otras preguntas en otra pregunta requiere darles un nombre fijo a través de la configuración de la pregunta, como `age` o `income`. Al hacer referencia a otras preguntas, siempre usa el nombre único de la pregunta dentro del estilo de referencia de pregunta, como

`${age}` o `${income}`

Simplemente incluye la referencia a la otra pregunta entre las demás palabras de tu etiqueta. Por ejemplo, puedes agregar una nueva pregunta con la etiqueta

`¿Estás seguro/a de que tienes ${age} años?`

![image](/images/responses_inside_question/question_name.gif)

Y también puedes crear una lógica de salto para esta pregunta de modo que solo se pregunte cuando la respuesta de edad sea menor de 18.

Ten en cuenta que si haces referencia a una pregunta que no existe, se creará un error cuando intentes desplegar tu formulario. Siempre asegúrate de hacer referencia a las preguntas con su nombre exacto, que también distingue entre mayúsculas y minúsculas. Por ejemplo, si tu pregunta se llama `age` no puedes usar `${Age}`. Puedes verificar fácilmente tu formulario haciendo clic en Vista previa en cualquier momento.

![image](/images/responses_inside_question/preview.gif)

**También puedes hacer referencia a la respuesta de una pregunta de Selección Única/Múltiple y mostrar la respuesta en lugar del código usando preguntas de Cálculo ocultas**

Si deseas hacer referencia a la respuesta de una pregunta de Selección Única/Múltiple y mostrar la respuesta de la respuesta (por ejemplo, "Totalmente de acuerdo") en lugar de su valor codificado (por ejemplo, "strongly_agr"), puedes:

1. Crear una pregunta de Selección Única/Múltiple y darle a la pregunta un nombre de referencia fijo a través de la configuración de la pregunta, como `instruction`. Y crear una pregunta de Cálculo intermedia e ingresar: `jr:choice-name(${instruction}, '${instruction}')`.

    ![image](/images/responses_inside_question/select_updated.gif)

2. Darle a esta pregunta de Cálculo un nombre de referencia, como `instruction_calculation`. En tu nueva pregunta, haz referencia a esta pregunta de Cálculo en lugar del nombre dado a la pregunta de Selección Única/Múltiple.

    ![image](/images/responses_inside_question/calculate.gif)

3. Previsualizar y validar el formulario para asegurarte de que todo funcione según lo diseñado.

    ![image](/images/responses_inside_question/preview_calculate.gif)