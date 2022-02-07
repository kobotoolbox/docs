# Using the Question Options
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/e341c15a1e4d5391551a195acd36ecec7124062d/source/question_options.md" class="reference">25 Jul 2020</a>

The Question Options screen contains some very useful features to get the most out of your form. You can click Setting to access the Question Options screen.

![image](/images/question_options/options.png)

## Data Column Name

The **Data Column Name** is the unique identifier (ID) of your question.

This field is mandatory for every question. Only letters, numbers, and underscores are allowed in this field, and the field must start with a letter or an underscore. You can input anything you like, such as `what_is_your_name` or `age`.

The Data Column Name (ID) is important because it is used in the column headers of tables and spreadsheets after your data has been collected. If you want your spreadsheet to follow a specific naming convention, you should specify the name for each of your questions before deploying the form as a data collection project.

## Guidance Hint (optional)

**Guidance Hint** are help texts that will be displayed underneath your questions on the form.

Hints are optional. The hint text is often used to provide additional instructions to your interviewer staff. For example, your question label might be `How old are you?` and your hint might be `If respondent doesn't know, enter 999`.

## Mandatory Response

If a question is **mandatory**, the interviewer needs to provide an answer in order to finalize the form.

## Default Response (optional)

This allows specifying a default response that the interviewer can accept or change.

In most studies this would not be recommended as it might create an accidental bias, but it may be useful for date or time questions where the responses tend to be around a certain known point. For date questions, the default response needs to be written in the format `YYYY-MM-DD` e.g. `1974-12-31`). For Select One or Select Many questions the response needs to be written using the unique Value - not the label (e.g. `first_grade` rather than `First grade`).

## Appearance (optional)

This advanced setting allows displaying the question in a modified way. Certain appearance options will only be available depending on the [Question Type](question_types.md).

For a full list of appearance values, visit [ODK's appearance documentation](http://xlsform.org/en/#appearance).

![image](/images/question_options/appearance.png)
