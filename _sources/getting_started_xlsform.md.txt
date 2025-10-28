# Getting started with XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c8c238efa59b04f403f13c150b018e1807c66d5c/source/getting_started_xlsform.md" class="reference">28 Oct 2025</a>

<a href="es/getting_started_xlsform.html">Leer en español</a> | <a href="fr/getting_started_xlsform.html">Lire en français</a> | <a href="ar/getting_started_xlsform.html">اقرأ باللغة العربية</a>

This article explains how to:

-   Set up an XLSForm using Microsoft Excel
-   Upload and preview an XLSForm in KoboToolbox
-   Download a form created with the KoboToolbox Formbuilder as an XLSForm

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_xlsform_v2.mp4"
    type="video/mp4"
  />
</video>

<br/>

<p class="note">
  <b>Note:</b> Some XLSForm features are not currently available in the Formbuilder, but they can be used for form building in XLSForm and then uploaded to KoboToolbox. This can be especially useful for complex forms.
</p>

## What is XLSForm

XLSForm is a standard for developing forms using Microsoft Excel and other spreadsheet software. XLSForms can then be uploaded to KoboToolbox to generate a data collection form.

There are many advantages to using XLSForm, especially for building complex forms with more advanced functionalities, including relevance conditions, calculations, and constraints. XLSForm also enables you to collaborate on form building using the same Excel file or in real time using Google Sheets.

<p class="note">
  <b>Note:</b> For a comprehensive introduction to form development using XLSForm, we recommend KoboToolbox Academy’s self-paced online <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

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

### Mandatory columns in XLSForm

#### Survey worksheet

| Column name | Description |
| :--- | :--- |
| type | Defines the question type (e.g., text, integer, select_one) |
| name | Defines a short, unique name to refer to each question |
| label | Defines the question text as it will be displayed in the form |

#### Choices worksheet

| Column name | Description |
| :--- | :--- |
| list_name | Defines the unique identifier for a list of option choices |
| name | Defines a short, unique name to refer to each option choice |
| label | Defines the choice text as it will be displayed in the form |

## Adding questions

In XLSForm, questions are added in the **survey** worksheet. The step-by-step process below explains how to add the following example questions: **What is your name?**, **What is your baby’s sex?**, and **How old are you?**

1. In the `type` column of the survey worksheet, type **text**. This is the question type for the first question, **What is your name?**
2. In the `name` column, type **yourname**. This will be the unique name used to identify the first question. Each question must have a unique name and cannot contain spaces or symbols (except the underscore).
3. In the `label` column, type **What is your name?**. This label will be displayed as the question text on the form during data collection.

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | What is your name? |
| survey |

4. For the second question, **What is your baby’s sex?**, enter **select_one sex** in the `type` column of the survey worksheet.
   - **select_one** is the question type that allows users to select only one choice from a list of response choices.
   - **sex** is the name of the list of response choices, which is defined in the choices worksheet (see [Adding response choices](https://support.kobotoolbox.org/getting_started_xlsform.html#adding-response-choices)).
5. In the `name` column, type **baby_sex**.
6. In the `label` column, type **What is your baby’s sex?**

| type           | name     | label                    |
| :------------- | :------- | :----------------------- |
| select_one sex | baby_sex | What is your baby’s sex? |
| survey |


7. For the question **How old are you?**, follow the same process using **integer** as the question type in the `type` column.

| type    | name | label            |
| :------ | :--- | :--------------- |
| integer | age  | How old are you? |
| survey |

<p class="note">
  <b>Note:</b> To learn more about question types in XLSForm, see <a class="reference external" href="https://xlsform.org/en/#question-types">Question types (XLSForm.org)</a>.
</p>

## Adding response choices

For select type questions (**select_one** and **select_multiple**), response choice options are added in the **choices** worksheet. The step-by-step process below explains how to add the choices for the example question: **What is your baby’s sex?**

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
| choices |

## Adding settings

There are many optional settings that can be added to the **settings** worksheet in XLSForm.

Common form settings include:

| Form setting     | Description                            |
| :--------------- | :------------------------------------- |
| form_title       | Title displayed at the top of the form |
| default_language | Default form language                  |
| style            | Themes for Enketo web forms            |
| version          | Form version ID                        |
| settings |

For example, to add a form title:

1. Add a column in the settings worksheet named `form_title`.
2. Enter the form title in the `form_title` column.
   - If you do not define a form title in your XLSForm, by default the Excel file name will be used as the project name in KoboToolbox. This can be edited in KoboToolbox.

<p class="note">
  <b>Note:</b> To learn more about the settings worksheet in XLSForm, see <a class="reference external" href="https://xlsform.org/en/#settings-worksheet">Settings worksheet (XLSForm.org)</a>.
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

To upload and preview your XLSForm in KoboToolbox:

1. Go to the **Project List** view in KoboToolbox and click **NEW**.
2. Select **Upload an XLSForm** and upload your **Excel** file.
   - If you created your XLSForm in **Google Sheets**, you will need to download the file before uploading it to KoboToolbox. In the Google Sheets menu, click File > Download > Microsoft Excel.
3. Enter the project details and click **CREATE PROJECT**.
4. Click the <i class="k-icon k-icon-view"></i> **Preview** button.

<p class="note">
  <b>Note:</b> To learn how to import your XLSForm via URL, see the support article <a class="reference" href="https://support.kobotoolbox.org/xls_url.html">Importing an XLSForm via URL</a>.
</p>

## Downloading an XLSForm from KoboToolbox

Forms created using the KoboToolbox Formbuilder can be easily downloaded as an XLSForm file.

1. Go to the **FORM** tab of your project in KoboToolbox.
2. Click the <i class="k-icon k-icon-more"></i> **More actions** icon.
3. Click <i class="k-icon k-icon-xls-file"></i>**Download XLS**.

Downloading your KoboToolbox form as an XLSForm file can be very useful for many reasons, including:

-   Adding advanced features to your form that are not currently supported in the Formbuilder.
-   Making changes to the form that are more efficient to do in XLSForm (e.g., duplicating a large number of questions or adding translations).
-   Avoiding slow computer or internet speeds that can affect form building in the Formbuilder (e.g., limited RAM, poor internet connectivity).
-   Sharing the form as an Excel file for collaboration with team members and managing form versions.
-   Sharing the form to request assistance from the KoboToolbox support team or in the Community Forum.

## Replacing a form with an XLSForm file

You can replace an existing form in the Formbuilder with a new version using an XLSForm. For example, after editing the form in Excel, you must upload the updated file to KoboToolbox.

1. Go to the **FORM** tab of your project in KoboToolbox.
2. Click the <i class="k-icon k-icon-more"></i> **More actions** icon.
3. Click <i class="k-icon k-icon-replace"></i> **Replace form**.
4. Choose the file you wish to upload.

## More XLSForm resources

For more information about using XLSForm, see the following resources:

-   [Official XLSForm documentation at XLSForm.org](https://xlsform.org)
-   [Form building documentation from ODK](https://docs.getodk.org/)
