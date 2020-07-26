# Including Responses Inside Another Question

You can include the response of one question (such as include the answer of the question 'How old are you?') inside the label of another question. This can be useful for many reasons in advanced forms. For example, you might want to confirm that a response is really correct.

Referencing other questions in another question requires giving them a fixed name through the question settings, such as `age` or `income`. When referencing other questions always use the unique question name inside the question referencing style, such as 

`${age}` or `${income}`

Simply include the reference to the other question among the other words of your label. For example, you can add a new question with the label

`Are you sure you are ${age} years old?` 

![image](/images/responses_inside_question/question_name.gif)

And you can also create a skip logic for this question so that it is only asked whenever the age response is lower than 18.

Note that if you reference a question that doesn't exist, it will create an error when you try to deploy your form. Always make sure to reference questions with their exact name, which is also case sensitive. For example, if your question is called `age` you can't use `${Age}`. You can easily check your form by clicking on Preview at any point.

![image](/images/responses_inside_question/preview.gif)

**You can also reference the response from a Select One/Many question and display the answer instead of the code using hidden Calculate questions**
 
If you'd like to reference the response to a Select One/Many question and show the response's answer (e.g. "Strongly Agree") instead of its encoded value (e.g. "strongly_agr"), you can:

1. Create a Select One/Many question, and give the question a fixed reference name through the question settings, such as `instruction`. And create an intermediate Calculate question and enter: `jr:choice-name(${instruction}, ${instruction})`. 

    ![image](/images/responses_inside_question/select.gif)

2. Give this Calculate question a reference name, such as `instruction_calculation`. In your new question, reference this Calculate question instead of the name given to the Select One/Many question. 

    ![image](/images/responses_inside_question/calculate.gif)
    
3. Preview and validate the form to make sure everything works as designed.

    ![image](/images/responses_inside_question/preview_calculate.gif)

