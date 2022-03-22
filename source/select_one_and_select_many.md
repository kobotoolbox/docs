# “Select One” and “Select Many” question types

When you have a categorical question with a list of predefined options (choices)
for respondents to choose from, you have to choose either the “Select One” or
“Select Many” question type in KoboToolbox. A “Select One” question type, also
known as a “single response” question, means a respondent can only select a
single response from the options. Similarly, a “Select Many” question type is
also known as a “multiple response” question where a respondent can select
multiple responses from the options.

“Select One” and “Select Many” question types are better choices for maintaining
quality data when the question has textual responses. This is because, unlike
the open-ended nature of the “Text” question type, the 2 question types limit
the user to the options listed.

## When to use “Select One”, and “Select Many” questions

Use the “Select One” question type when a question has a list of choices, and
the respondent is limited to just a single option from the list. Examples of
select one questions include marital status, sex, or religion.

Use the “Select Many” question type if there is a list of choices and the
respondent may find it appropriate to select more than one choice. Examples of
select many questions include household sources of income and a list of
household assets.

## How to set up a “Select One” or “Select Many” questions

Follow the same steps to setting up either a “Select One” or a “Select Many”
question:

-   In the KoboToolbox formbuilder, click the + button to add a new question.
-   Type the question text. For example, “What is your marital status?”. Then
    click Add Question (or press Enter).
-   Choose the question type (“Select One” or “Select Many”)
-   Type the response labels where there is “Option 1”, “Option 2”. Click “+
    Click to add another response” every time you need additional space for
    another response.

Click the <i class="k-icon k-icon-trash"></i> Delete button next to the option
to remove it.

## XML values for “Select One” and “Select Many” questions

When setting up “Select One” and “Select Many” question responses, you have the
choice to set the XML values or to let KoboToolbox generate them automatically.

XML values are the values that get saved in the database when a user chooses the
response.

Ifyou would like custom values, such as numbers, to be saved in the database
when a response is selected (for example, when a respondent chooses “Married” on
a marital status question, KoboToolbox should save the value 1 in the database).
In that case, you must type the values where it says “AUTOMATIC” as shown below.

![XML Values](/images/select_one_and_select_many/xml_values.png)

<section class="note">
  Note: The predefined choices for a “Select One” and “Select Many” questions
  may sometimes be insufficient in the field while collecting data. Hence, it is
  advised to keep an option where the enumerators should be able to add the
  response provided by the respondents to this category. You could create this
  choice as outlined in our support article [User-Specified “Other” Responses
  for Multiple-Choice Questions](user_specified_other.md).
</section>
	
## How “Select One” and “Select Many” questions are displayed by default on web forms and KoboCollect

![Comparison of select one and select many on Enketo and KoboCollect](/images/select_one_and_select_many/select_one_select_many_comparison.png)

You can see from the display that you can easily differentiate between a “Select
One” and a “Select Many” question in a data entry form. The “Select One”
question has choices with a round button (a dot appears after selecting a
choice) while the “Select Many” question has a choice with a square button
(check marks appear after selecting the choices).

## How data for “Select One” and “Select Many” questions are stored

By default, responses for “Select One” and “Select Many” questions are saved as
text values. You can choose between response labels or XML values when exporting
your data.

When exporting “Select Many” questions, you can choose between exporting all
selected responses in a single column or having the options in separate columns
or both.
[Read more about exporting and downloading data in this support article](https://support.kobotoolbox.org/export_download.html).

## Advanced appearances for “Select One” and “Select Many” questions

When adding “Select One” and “Select Many” questions, you can choose from a wide
range of appearances. Appearances change the way the question is displayed on
web forms or on KoboCollect.

![Appearances](/images/select_one_and_select_many/appearances.png)

The following table shows the appearances and how they are displayed both on web
forms and KoboCollect.

![Appearances](/images/select_one_and_select_many/select_one_select_many_appearances_1.png)
![Appearances](/images/select_one_and_select_many/select_one_select_many_appearances_2.png)
![Appearances](/images/select_one_and_select_many/select_one_select_many_appearances_3.png)

<section class="note">
  <p>
    Note: The option “Other” provides you with a space where you can type a
    different appearance that is not shown on the list.
  </p>

  <p>
    “Quick”, “likert” and “quickcompact” are only applicable to “Select One”
    questions.
  </p>
</section>
