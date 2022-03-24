# "Select One" and "Select Many" question types

When you have a categorical question with a list of predefined options for
respondents to choose from, you have to choose either the "Select One" or
"Select Many" question type in KoboToolbox. A "Select One" question type, also
known as a "single response" question, means a respondent can only select a
single response from a list of options. Similarly, a "Select Many" question type
is also known as a "multiple response" question where a respondent can select
multiple responses from a list of options.

"Select One" and "Select Many" question types can be better choices for
maintaining quality data when the question has a narrow and defined scope. This
is because, unlike the open-ended nature of the "Text" question type, the two
select question types limit the user to the options listed.

## When to use them

Use the "Select One" question type when a question has a list of choices, and
the respondent is limited to just a single option from the list. Examples
include marital status, sex, or religion.

Use the "Select Many" question type if there is a list of choices and the
respondent may find it appropriate to select more than one choice. Examples
include household sources of income or a list of household assets.

## Setting up the question and choices

Follow the same steps for setting up either a "Select One" or a "Select Many"
question:

-   In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to
    add a new question.
-   Type the question label, for example, "What is your marital status?". Then
    click **+ Add Question** (or press **Enter**).
-   Choose the question type ("Select One" or "Select Many")
-   Type the response labels where there is "Option 1", "Option 2". Add more
    choices if necessary.

<p class="note">
  You can reorder your list of choices by clicking and dragging each item to a
  new position in the list.
</p>

Click the <i class="k-icon k-icon-trash"></i> trash can icon to the left of the
option's label to remove it.

## Translating question and choice labels

For translating select type questions and their labels into other languages
through the KoboToolbox UI, refer to the support article,
[Adding Another Language in the Project Dashboard](language_dashboard.md), or
[here](language_xls.md) if you are creating your form using XLSForm.

## XML values

When setting up "Select One" and "Select Many" question responses, you have the
choice to specify the XML values or to let KoboToolbox generate them
automatically.

<p class="note">
  It is strongly recommended that you specify XML values for
  <strong>all questions and choices</strong> before deploying your form,
  <em>especially</em> if the labels are non-Latin character languages such as
  Chinese, Arabic or Nepali.
</p>

XML values are the values that get saved in the submission when a user chooses
the response, not the label. In the formbuilder, type the values where it says
"AUTOMATIC" as shown below.

![XML Values](/images/select_one_and_select_many/xml_values.png)

The predefined choices for a "Select One" and "Select Many" questions may
sometimes be insufficient while collecting data. It is possible to include the
option for a text response in that case, as outlined in our support article,
[User-Specified "Other" Responses for Multiple-Choice Questions](user_specified_other.md).

## How they are displayed by default on web forms and KoboCollect

![Comparison of select one and select many on Enketo and KoboCollect](/images/select_one_and_select_many/select_one_select_many_comparison.png)

You can easily differentiate between a "Select One" and a "Select Many" question
in a data entry form. The "Select One" question has choices with a radio button
(a solid dot appears after selecting an item) while the "Select Many" question
has choices with a square checkbox (check marks appear after selecting items).

## Export options

When exporting "Select Many" questions, you can choose between exporting all
selected responses in a single column or having the options in separate columns
or both. Read more about exporting and downloading data in
[this support article](export_download.md).

## Advanced appearances

When adding "Select One" and "Select Many" questions, you can choose from a wide
range of appearances. Appearances change the way the question is displayed in
the web forms or KoboCollect.

![Appearances](/images/select_one_and_select_many/appearances.png)

<p class="note">
  The option "other" provides you with a space where you can type a different
  appearance that is not shown on the list.
</p>

The following table shows the different available appearances and how they are
displayed both in the web forms and KoboCollect.

![Appearances](/images/select_one_and_select_many/select_one_select_many_appearances_1.png)
![Appearances](/images/select_one_and_select_many/select_one_select_many_appearances_2.png)
![Appearances](/images/select_one_and_select_many/select_one_select_many_appearances_3.png)

<p class="note">
  The appearances "quick", "likert" and "quickcompact" are only applicable to
  "Select One" questions.
</p>
