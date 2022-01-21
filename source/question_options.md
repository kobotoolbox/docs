# Using the Question Options

The Question Options screen contains some very useful features to get the most out of your form. You can click the <i class="k-icon k-icon-settings"></i> Settings button to access the Question Options screen.

![image](/images/question_options/options2.png)

## Data Column Name

The **Data Column Name** is the unique identifier (ID) of your question.

This field is mandatory for every question. Only letters, numbers, and underscores are allowed in this field, and the field must start with a letter or an underscore. You can input anything you like, such as `what_is_your_name` or `age`. 

The Data Column Name (ID) is important because it is used in the column headers of tables and spreadsheets after your data has been collected. If you want your spreadsheet to follow a specific naming convention, you should specify the name for each of your questions before deploying the form as a data collection project.

## Guidance Hint (optional)

**Guidance Hints** are extra instructions that you can add to your questions as notes. These notes are not normally shown on the form by default.

Guidance hints can be used as internal notes when collaborating with others in developing the form. You can also show them on printouts or during training for enumerators.

## Mandatory Response

This settings allows you to specify whether the question must be responded to at all times or not.

Three options are available:

1. Yes - The question must be answered at all times. If the user does not provide a response, he/she will not be able to move to the next question or save the form.
2. No - The question is not mandatory and hence can be manually skipped
3. Custom logic - You can define logic using XLSForm code which will define when the question will be mandatory. For example, if you set the following custom logic `age > 18`, the question will be mandatory when a preceding question with the data column name `age` is greater than 18

## Default Response (optional)

This allows specifying a default response that the interviewer can accept or change.

In most studies this would not be recommended as it might create an accidental bias, but it may be useful for date or time questions where the responses tend to be around a certain known point. For <i class="k-icon k-icon-qt-date"></i> Date questions, the default response needs to be written in the format `YYYY-MM-DD` e.g. `1974-12-31`). For <i class="k-icon k-icon-qt-select-one"></i> Select One or <i class="k-icon k-icon-qt-select-many"></i> Select Many questions the response needs to be written using the unique Value (xml value) - not the label (e.g. `first_grade` rather than `First grade`).

## Appearance (optional)

This advanced setting allows displaying the question in a modified way. Certain appearance options will only be available depending on the [Question Type](question_types.md).

For a full list of appearance values, visit [ODK's appearance documentation](http://xlsform.org/en/#appearance).

![image](/images/question_options/appearance.png)