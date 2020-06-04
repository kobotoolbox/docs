# Question Options

The Question Options screen contains some very useful features to get the most out of your form.

![image](/images/question_options/options.png)

**Name**

The **Name** is the unique identifier (ID) of your question.

This field is mandatory for every question. Only letters, numbers, and underscores are allowed in this field, and the field must start with a letter or an underscore. KoBoToolbox will automatically give every questions a default name to begin with (such as `how_old_are_you`), but you can change it to anything you like, such as `age` or `A01`.

The name (ID) is important because it is used in the column headers of tables and spreadsheets after your data has been collected. If you want your spreadsheet to follow a specific naming convention, you should specify the name for each of your questions before deploying the form as a data collection project.

Note that the automatic naming of questions is based on Latin characters only. If your question labels don't use any Latin characters, your automatic names would be just underscores and numbers.

**Hint (optional)**

**Hints** are help texts that will be displayed underneath your questions on the form.

Hints are optional. The hint text is often used to provide additional instructions to your interviewer staff. For example, your question label might be `How old are you?` and your hint might be `If respondent doesn't know, enter 999`.

**Required**

If a question is **required**, the interviewer needs to provide an answer in order to finalize the form.

'Read a Note' questions can't be made required because the interviewer can't actually give a response to it (notes only consist of a label - see Response Options.

**Default (optional)**

This allows specifying a default response that the interviewer can accept or change.

In most studies this would not be recommended as it might create an accidental bias, but it may be useful for date or time questions where the responses tend to be around a certain known point. For date questions, the default response needs to be written in the format `YYYY-MM-DD` e.g. `1974-12-31`). For Select One or Select Many questions the response needs to be written using the unique Value - not the label (e.g. `first_grade` rather than `First grade`).

**Appearance (optional)**

This advanced setting allows displaying the question in a modified way. Certain appearance options will only be available depending on the [Question Type](question_types.html). 

For a full list of appearance values, visit [ODK's appearance documentation](http://xlsform.org/en/#appearance).

![image](/images/question_options/appearance.png)
