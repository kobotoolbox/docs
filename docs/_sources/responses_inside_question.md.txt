# Include Responses Inside Another Question

You can include the response of one question (such as the answer "41" to the question 'How old are you?') inside the label of another question. This can be useful for many reasons in advanced forms. For example, you might want to confirm that a response is really correct.

Referencing other questions in another question requires giving them a fixed name through the question settings, such as income. When referencing other questions always use the unique question name inside the question referencing style:

`${question_name}`

Simply include the reference to the other question among the other words of your label. For example, you can add a new question with the label

`Are you sure you are ${age} years old?` 

and create a skip logic for this question so that it is only asked whenever the age response was lower than 18.

Note that if you reference a question that doesn't exist, it will create an error when you try to deploy your form. Always make sure to reference questions with their exact name, which is also case sensitive. For example, if your question is called `age` you can't use `${Age}`. You can easily try it by clicking on Preview at any point.

Using references is also very useful for creating hidden Calculate questions.
 
If you'd like to reference the response to a Select One question and show the response's label (e.g. "Strongly agree") instead of its encoded value (e.g. "5_s_a"), you can create an intermediate Calculate question entering in something like `jr:choice-name(${q3_village_safe}`, `${q3_village_safe}`)" (without the double quotes, and taking care to include the single quotes) and reference this Calculate question instead of the original question.
