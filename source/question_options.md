# Using the Question Options
<a href="fr/question_options.html">Lire en français</a> | <a href="es/question_options.html">Leer en español</a> | <a href="ar/question_options.html">اقرأ باللغة العربية</a>
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/43a3384fad535287d1c7820457ab2d25a86877fc/source/question_options.md" class="reference">24 Sep 2025</a>

After adding a question, there are many different customizations you can make to
it using the question options. To get to the question options screen of a
question, click its <i class="k-icon k-icon-settings"></i> Settings button.

![Question options](/images/question_options/options2.png)

## Data Column Name

The **Data Column Name** is the unique identifier (ID) of your question.

This field is mandatory for every question. Only letters, numbers, and
underscores are allowed in this field, and the field must start with a letter or
an underscore. You can input anything you like, such as `what_is_your_name` or
`age`.

The Data Column Name is important because it is used in the column headers of
tables and spreadsheets after your data has been collected. If you want your
spreadsheet to follow a specific naming convention, you should specify the name
for each of your questions before deploying the form as a data collection
project.

## Guidance Hint (optional)

**Guidance Hints** are extra instructions that you can add to your questions as
notes. By default in Enketo web forms, the guidance hints are displayed under an
accordion which can be expanded and collapsed as shown below.

![Guidance hint in Enketo Web forms](/images/question_options/guidance_hint_enketo.gif)

In [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html), guidance hints are not displayed by default. You can [choose how
guidance hints should be displayed](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) in your forms by going to Settings -> Form
Management -> Show guidance for questions. Here you have 3 choices: No, Yes -
always shown and Yes - always collapsed.

![Guidance hint in KoboCollect](/images/question_options/guidance_hint_kobocollect.gif)

Guidance hints can be used as internal notes when collaborating with others in
developing the form. You can also show them on printouts or extra instructions
during training for enumerators.

## Mandatory Response

This settings allows you to specify whether the question must be responded to at
all times or not. In XLSForm, this is called `required`.

In KoboToolbox, there are three options for mandatory response:

1. Yes - The question must be answered at all times. If a response is not
   provided, the user will not be able to move to the next question or save the
   form.
2. No - The question is not mandatory and hence can be manually skipped.
3. Custom logic - You can define logic using XLSForm code which will define when
   the question will be mandatory. For example, if you set the following custom
   logic `${age} > 18`, the question will be mandatory when a preceding question
   with the data column name `age` is greater than 18.

## Default Response (optional)

This allows specifying a default response that the interviewer can accept or
change.

In most studies this would not be recommended as it might create an accidental
bias, but it may be useful for date or time questions where the responses tend
to be around a certain known point.

For <i class="k-icon k-icon-qt-date"></i> Date questions, the default response
needs to be written in the format `YYYY-MM-DD` e.g. `1974-12-31`).

For <i class="k-icon k-icon-qt-select-one"></i> Select One or
<i class="k-icon k-icon-qt-select-many"></i> Select Many questions the response
needs to be written using the unique Value (xml value) - not the label (e.g.
`first_grade` rather than `First grade`).

## Appearance (optional)

This advanced setting allows displaying the question in a modified way. Certain
appearance options will only be available depending on the
[Question Type](question_types.md).

For a full list of appearance values, visit
[ODK's appearance documentation](http://xlsform.org/en/#appearance).

![Question appearance oprions](/images/question_options/appearance.png)
