# Getting started with XLSForm

This article will show you how to:

-   Set up an XLSForm using Microsoft Excel.
-   Upload and preview the XLSForm in KoboToolbox.
-   Download a form you have been creating using the KoboToolbox formbuilder as
    an XLSForm.

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_with_xlsform.mp4"
    type="video/mp4"
  />
</video>

<br/>

When building forms for KoboToolbox, there are two main methods you can use. One
is by using the KoboToolbox formbuilder, and the other is using XLSForm.

XLSForm is a standard for creating forms in Microsoft Excel and makes it
possible to create basic and advanced forms in a user-friendly format.

<p class="note">
  There are a number of XLSForm features that are not yet supported by the
  formbuilder and therefore a knowledge of XLSForm can be important for more
  complex forms.
</p>

## What is XLSForm

An XLSForm is simply an Excel file structured in a standardized format that can
be uploaded to KoboToolbox to generate a data collection form.

Not only does using XLSForm offer enhanced functionalities, but it can also make
collaborating on form building easier in some case. For example, members of your
team can work on building the form in Google Sheets, allowing for real time
collaboration.

## How to set up XLSForm

To get started with XLSForm, do the following:

1. Create a workbook (either in Microsoft Excel or Google Sheets).
2. Create three worksheets: **survey**, **choices**, and **settings**
   respectively (sheet names must all be in lowercase).
3. In the **survey** worksheet, create three columns with headings: `type`,
   `name`, and `label`.
4. In the **choices** worksheet, create three columns with headings:
   `list_name`, `name`, `label`.
5. In the **settings** worksheet, create a column named `form_title` (the
   **settings** sheet is optional)

## Adding questions

Questions in XLSForm go in the **survey** sheet. We will practice adding a few
questions: _What is your name_, _Sex_ and _How old are you?_

1. In the **survey** sheet, under the `type` column, type "text". This is the
   question type for our first question. To learn more about question types in
   XLSForm, [read this article](https://xlsform.org/en/#question-types).
2. Under the `name` column, type "yourname". This will be the variable name of
   our first question. The variable name uniquely identifies each question in
   the form. It’s also the name of the question in the database when we start
   collecting data. Each question must have a unique name and cannot contain
   spaces or symbols (except the underscore).
3. Under the `label` column, type "What is your name". This label will be shown
   as the question text on the form when we collect data.

For our second question:

1. Still in the **survey** sheet, type `select_one gender` in the `type` column
   below the previous question (make sure to put a space between the 2 words).
   `select_one` is the question type that allows us to specify a list of choices
   where a user will only be allowed to pick one choice. (If a user can select
   several choices, this would be specified by the `select_multiple` question
   type.) "sex" is the name of the list of choices which we have to define in
   the **choices** sheet.
2. Type the `name` and `label` of the question as "sex" and "Sex" respectively.

Add the final question as follows:

| type    | name | label            |
| ------- | ---- | ---------------- |
| integer | age  | How old are you? |

## Adding choices

Regardless of the type of multiple choice question (`select_one` or
`select_multiple`), the next step will be to define the list of choices in the
**choices** sheet. Each list of choices must have the same `list_name`.

Since we defined one question that has a list of choices ("sex") in the previous
step, we need to add this list in the **choices** sheet as follows:

1. Switch to the **choices** sheet so that you can add your list of choices for
   the "Sex" question.
2. In the cell below `list_name`, type "sex". This is the list name we defined
   for the "Sex" question in the **survey** sheet. In the cell below `name`,
   type "male". This is the value that will be stored when the user chooses the
   option "Male". Under `label`, type "Male". This is what will be shown for
   this option in the survey.
3. For the second choice, type "sex" as `list_name`, "female” as the `name`, and
   "Female" as the `label`.

## Adding settings

It is not mandatory to include the **settings** sheet in the XLSForm - any form
will work just fine without it. However, at minimum, you can define the
`form_title`.

<p class="note">
  Without the <code>form_title</code> in the <strong>settings</strong> sheet,
  KoboToolbox will, by default, use the file name as the name of the project
  when you import the XLSForm.
</p>

Below the `form_title` column, type "Practice form" as the title of the form we
are creating in this article.

## Uploading and previewing the XLSForm in KoboToolbox

Once you have finished creating the XLSForm you must upload it to KoboToolbox in
order to preview it.

1. While you are on the Project List view (the first screen after you have just
   logged in to KoboToolbox), click **NEW**.
2. Click **Upload an XLSForm** (if you were creating the form using Google
   Sheets, you can either download the file as an Excel file, or
   [follow the instructions in the linked article](xls_url.md) to import it via
   a URL).
3. Choose the Excel file you just created and wait until it uploads.
4. Confirm the project details and click **CREATE PROJECT**.
5. You can then click the <i class="k-icon k-icon-view"></i> _Preview form_
   button to preview your form.

## Downloading an XLSForm from KoboToolbox

KoboToolbox allows you to download a form you have been creating using the
formbuilder as an XLSForm file. This might be useful for several reasons such
as:

-   You need to add some advanced features that are not yet supported in the
    formbuilder.
-   You would like to make changes to the form that might be easier through
    XLSForm (such as quickly duplicating a large number of questions).
-   Your computer resources such as your browser or internet connection.
-   You would like to collaborate on the form with members of your team and you
    prefer sharing the XLSForm.
-   Manage versioning of your form outside of the KoboToolbox platform.
-   You are needing assistance from the support team and need to share your form
    with us.

To download the XLSForm while you are on the Project List view:

1. Hover your mouse over the name of the project.
2. Click the <i class="k-icon k-icon-more"></i> _More actions_ icon.
3. Click <i class="k-icon k-icon-xls-file"></i> _Download XLS_.
4. Save the file.

## Replacing a form with an XLSForm file

You can replace an existing form with a new version using an XLSForm (for
example, after having edited the form in Excel). To do this while you are on the
Project List view:

1. Hover your mouse over the name of the project.
2. Click the <i class="k-icon k-icon-more"></i> _More actions_ icon.
3. Click <i class="k-icon k-icon-replace"></i> _Replace form_.
4. Choose the file.

## More XLSForm learning resources

Go to the following links to learn more about XLSForm:

-   [Official XLSForm documentation at XLSForm.org](https://xlsform.org)
-   [Detailed form building documentation from ODK](https://docs.getodk.org/)
