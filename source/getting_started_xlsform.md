# Getting started with XLSForm

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/495951b94c328bc1ae7d6e429c30aac371acec18/source/getting_started_xlsform.md" class="reference">19
Dec 2024</a>

When creating survey forms for KoboToolbox, you can build your form with the KoboToolbox Formbuilder or in XLSForm. XLSForm is very effective for creating both basic and advanced forms in a user-friendly format.

This article explains how to:

-   Set up an XLSForm using Microsoft Excel
-   Upload and preview an XLSForm in KoboToolbox
-   Download a form created with the KoboToolbox Formbuilder as an XLSForm

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_with_xlsform.mp4"
    type="video/mp4"
  />
</video>

<br/>

<p class="note">
  Note: Some XLSForm features are not currently available in the Formbuilder, but they can be used for form building in XLSForm and then uploaded to KoboToolbox. This can be especially useful for complex forms.
</p>

## What is XLSForm

XLSForm is a standard for developing forms using Microsoft Excel and other spreadsheet software. XLSForms can then be uploaded to KoboToolbox to generate a data collection form.

There are many advantages to using XLSForm, especially for building complex forms with more advanced functionalities, including relevance conditions, calculations, and constraints. XLSForm also enables you to collaborate on form building using the same Excel file or in real time using Google Sheets.

## Setting up an XLSForm

To set up the basic structure of an XLSForm:

1. Create a workbook in Microsoft Excel or Google Sheets.
2. Create three worksheets: **survey**, **choices**, and **settings**.
   - Worksheet names must be all lowercase letters.
3. In the **survey** worksheet, create three columns with the headings: `type`,
   `name`, and `label`.
4. In the **choices** worksheet, create three columns with the headings:
   `list_name`, `name`, and `label`.
5. The **settings** worksheet is optional. It can be used to include additional form specifications and customizations.
   - For example: `form_title`, `style`, and `default_language`.

## Adding questions

In XLSForm, questions are added in the **survey** worksheet. The step-by-step process below explains how to add the following example questions: **What is your name?**, **What is your baby’s sex?**, and **How old are you?**.

1. In the `type` column of the survey worksheet, type **text**. This is the question type for the first question, **What is your name?**.
2. In the `name` column, type **yourname**. This will be the unique name used to identify the first question. Each question must have a unique name and cannot contain spaces or symbols (except the underscore).
3. In the `label` column, type **What is your name?**. This label will be displayed as the question text on the form during data collection.

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | What is your name? |
4. For the second question, **What is your baby’s sex?**, enter **select_one sex** in the `type` column of the survey worksheet.
   - **select_one** is the question type that allows users to select only one choice from a list of response choices.
   - **sex** is the name of the list of response choices, which is defined in the choices worksheet (see [Adding response choices](https://support.kobotoolbox.org/getting_started_xlsform.html#adding-choices)).
5. In the `name` column, type **baby_sex**.
6. In the `label` column, type **What is your baby’s sex?**

| type           | name     | label                    |
| :------------- | :------- | :----------------------- |
| select_one sex | baby_sex | What is your baby’s sex? |
7. For the question **How old are you?**, follow the same process using **integer** as the question type in the `type` column.

| type    | name | label            |
| :------ | :--- | :--------------- |
| integer | age  | How old are you? |

<p class="note">
  Note: To learn more about question types in XLSForm, see [Question types (XLSForm.org)](https://xlsform.org/en/#question-types).
</p>

## Adding response choices

For select type questions (**select_one** and **select_multiple**), response choice options are added in the **choices** worksheet. The step-by-step process below explains how to add the choices for the example question: **What is your baby’s sex?**.

1. In the `list_name` column in the choices worksheet, enter the list_name **sex**.
   - This is the list_name previously defined for the **baby_sex** question in the survey worksheet.
   - The list_name is the unique identifier for the list of response choice options.
2. In the name column, add the choice name **male**.
   - The choice name is the unique identifier for each choice option.
3. In the label column, enter the choice label **Male**.
   - The choice label is displayed on the form during data collection.
4. To add the second choice option for the **baby_sex** question, enter **sex** in the `list_name` column. Enter **female** as the choice name and **Female** as the choice label.
   
| list_name | name   | label  |
| :-------- | :----- | :----- |
| sex       | male   | Male   |
| sex       | female | Female |

## Adding settings

There are many optional settings that can be added to the settings worksheet in XLSForm.

Common form settings include:

| Form setting     | Description                            |
| :--------------- | :------------------------------------- |
| form_title       | Title displayed at the top of the form |
| default_language | Default form language                  |
| style            | Themes for Enketo web forms            |
| version          | Form version ID                        |

For example, to add a form title:

1. Add a column in the **settings** worksheet named `form_title`.
2. Enter the form title in the `form_title` column.
   - If you do not define a form title in your XLSForm, by default the Excel file name will be used as the project name in KoboToolbox. This can be edited in KoboToolbox.

<p class="note">
  Note: To learn more about the settings worksheet in XLSForm, see [Settings worksheet (XLSForm.org)](https://xlsform.org/en/#settings-worksheet).
</p>

## Adding optional columns to the survey worksheet

To further customize your XLSForm, you can add optional columns that include form logic, question options, and advanced settings.

| **Column name**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| hint               | Question hint                                  |
| guidance_hint      | Guidance hint                                  |
| required           | Option to make a question mandatory            |
| relevant           | Skip logic conditions for the question         |
| constraint         | Validation criteria for the question           |
| constraint_message | Error message when validation criteria not met |
| appearance         | Options for how questions are displayed        |
| choice_filter      | Criteria for cascading select                  |
| parameters         | Settings for specific question types           |
| calculation        | Mathematical expression for calculate question |
| default            | Default response for a question                |

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
