# How to Use the Calculate Question Type

Some advanced forms may require an internal calculation to take place as part of the form (rather than afterwards during the analysis). This can be done by adding a Calculation and writing the mathematical expression into the question label field.  

![image](/images/calculate_questions/calculation.gif)  

A mathematical expression could be as simple as `5 + 1`, but most likely it would include reference to another question.

Referencing other questions in your calculation requires giving them a fixed name through the question settings, such as income. When referencing other questions always use the unique question name (not label) inside the question referencing style: `${question_name}`

If for example, you wanted to convert the answer to a question about someone's income into another currency (such as Rwandan Francs to US Dollars), you would write `${income} / 688`

You can now use the answer to this Calculate question for other purposes, such as building your skip logic (for example only ask a follow-up question above a certain income threshold) or by displaying it inside a Note ([see here](responses_inside_question.md) for help on how to display the response to one question in the label of another question).

**List of available functions**

There are a lot of different options available, such as the round() function (e.g. `round(${int_1} div ${int_2}, 1`) will round the result of a division to a single decimal). For a list of some of the many mathematical expressions that can be used in this field, please see [XForm specifications on calculation functions](https://docs.getodk.org/form-operators-functions/) for the technical background of all the functions available in KoBoToolbox and XLSForms. For advance use of calculations in KoBoToolbox, please refer to this article.

**List of available calculation operators**

![image](/images/calculate_questions/operator.png)  
