# Getting started with XLSForm

<iframe src="https://www.youtube.com/embed/xpeBCy9p1Ys?si=tP_3G2vMnRC1OgWS" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


When creating survey forms with KoboToolbox, you can build your form with the [KoboToolbox Formbuilder](https://support.kobotoolbox.org/formbuilder.html) or using XLSForm. XLSForm is very effective for creating both basic and advanced forms in a user-friendly format.

<p class="note">
  For more information about XLSForm, see <a class="reference" href="https://support.kobotoolbox.org/edit_forms_excel.html">Introduction to XLSForm</a>. For a comprehensive introduction to form development using XLSForm, we recommend <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">KoboToolbox Academy’s self-paced online XLSForm Fundamentals Course</a>.
</p>

This article explains how to set up an XLSForm using Microsoft Excel or other spreadsheet programs, including:

- Setting up the basic structure of your XLSForm
- Adding questions and option choices
- Adding form settings and optional columns
- Uploading and previewing your XLSForm in KoboToolbox

<p class="note">
  <b>Note:</b> Some XLSForm features are not currently available in the Formbuilder, but KoboToolbox forms can be downloaded, modified in XLSForm, and <a class="reference" href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">uploaded back to KoboToolbox</a>.
</p>


## Setting up an XLSForm

To set up the basic structure of an XLSForm:

1. Create a workbook in your preferred spreadsheet software.
2. Create three worksheets: **survey**, **choices**, and **settings**.
   - Worksheet names must be all lowercase letters.
3. In the **survey** worksheet, create three columns with the headings: `type`, `name`, and `label`.
4. In the **choices** worksheet, create three columns with the headings: `list_name`, `name`, and `label`.
5. The **settings** worksheet is optional. It can be used to include additional form specifications and customizations.
   - For example: `form_title`, `style`, and `default_language`.

<p class="note">
To get started with XLSForm, download a sample XLSForm <a class="reference" href="https://support.kobotoolbox.org/_static/files/getting_started_xlsform/sample_xlsform.xlsx">here</a>.
</p>

### Mandatory columns in XLSForm

The following columns are mandatory in XLSForm:

**survey worksheet**

| Column name | Description |
| --- | --- |
| type | Defines the question type (e.g., text, integer, select_one) |
| name | Defines a short, unique name to refer to each question |
| label | Defines the question text as it will be displayed in the form |

**choices worksheet**

| Column name | Description |
| --- | --- |
| list_name | Defines the unique identifier for a list of option choices |
| name | Defines a short, unique name to refer to each option choice |
| label | Defines the choice text as it will be displayed in the form |

## Adding questions

In XLSForm, questions are added in the **survey** worksheet. To add questions in XLSForm:

1. In the `type` column of the `survey` worksheet, enter the [question type](https://support.kobotoolbox.org/question_types_xls.html) of the question you want to add.
2. In the `name` column, enter a name used to identify the question.
   - Each question must have a unique name and cannot contain spaces or symbols (except underscores).
3. In the `label` column, enter the question text as it should be displayed in the form during data collection.

**survey worksheet**

| type | name | label |
| :--- | :--- | :--- |
| text | yourname | What is your name? |
| survey |

4. If you are adding **select type questions** (`select_one`, `select_multiple`, or `rank`): in the `type` column, after the question type, add a space and enter the name of the list of choices.
   - The name of the list of choices is later defined in the `choices` worksheet as the `list_name`.

**survey worksheet**

| type | name | label |
| :--- | :--- | :--- |
| select_one sex | baby_sex | What is your baby’s sex? |
| survey |

<p class="note">
To learn more about question types in XLSForm, see <a class="reference" href="https://support.kobotoolbox.org/question_types_xls.html">Question types in XLSForm</a>.
</p>

## Adding option choices

For select type questions, option choices are added in the **choices** worksheet. To add option choices in XLSForm:

1. In the `list_name` column of the `choices` worksheet, enter the name of the **list of option choices**.
   - The `list_name` is a unique identifier for a list of option choices. It must match the list name entered in the `type` column of the `survey` worksheet.
2. In the `name` column, add a short name for each option choice.
   - Each choice within a list must have a unique `name`, which cannot contain spaces or symbols (except underscores).
3. In the `label` column, enter the choice text as it should be displayed in the form during data collection.

**choices worksheet**

| list_name | name | label |
| :--- | :--- | :--- |
| sex | male | Male |
| sex | female | Female |
| choices |

<p class="note">
To learn more about managing option choices in XLSForm, see <a class="reference" href="https://support.kobotoolbox.org/option_choices_xls.html">Managing option choices in XLSForm</a>.
</p>

## Adding settings

There are many optional settings that can be added to the **settings** worksheet in XLSForm.

Common form settings include:

| Setting | Description |
| --- | --- |
| form_title | Title displayed at the top of the form |
| default_language | Default form language |
| style | Themes for Enketo web forms |
| version | Form version ID |

For example, to add a form title:

1. Add a column in the settings worksheet named `form_title`.
2. Enter the form title in the `form_title` column.

<p class="note">
<b>Note:</b> All form settings are optional. If you do not define a form title in your XLSForm, the Excel file name will be used as the project name in KoboToolbox by default. This can be edited in KoboToolbox.
</p>

**settings worksheet**

| form_title |
| :--- |
| Getting started with <br> XLSForm |
| settings |

<p class="note">
To learn more about the settings worksheet in XLSForm, see <a class="reference" href="https://support.kobotoolbox.org/form_settings_xls.html">Form settings in XLSForm</a>.
</p>

## Adding optional columns to the survey worksheet

To further customize your XLSForm, you can add optional columns to configure form logic, question options, and advanced settings. Common optional columns include:

| Column name | Description |
| --- | --- |
| hint | Question hint |
| guidance_hint | Guidance hint |
| required | Option to make a question mandatory |
| relevant | Skip logic conditions for the question |
| constraint | Validation criteria for the question |
| constraint_message | Error message when validation criteria are not met |
| appearance | Options for how questions are displayed |
| choice_filter | Criteria for cascading select |
| parameters | Settings for specific question types |
| calculation | Mathematical expression for calculate question |
| default | Default response for a question |

<p class="note">
To learn more about optional columns in XLSForm, see <a class="reference" href="https://support.kobotoolbox.org/question_options_xls.html">Using question options in XLSForm</a>, <a class="reference" href="https://support.kobotoolbox.org/appearances_xls.html">Question appearances in XLSForm</a>, and <a class="reference" href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

## Uploading and previewing your XLSForm in KoboToolbox

Once you have finished developing your XLSForm, you can upload and preview it in KoboToolbox:

1. Go to the **Project** home page in KoboToolbox and click **NEW**.
2. Select **Upload an XLSForm** and upload your XLSForm file.
3. Enter the project details and click **CREATE PROJECT**.
4. Click the <class="k-icon k-icon-view"> **Preview** button.

If your XLSForm contains an error, an error message will appear, usually indicating the exact row, question, or expression where the issue is located. After correcting the error in your XLSForm, you will need to upload the file again.

<p class="note">
To learn how to download an XLSForm from KoboToolbox, import your XLSForm via URL, and use KoboToolbox to validate and test your XLSForm, see <a class="reference" href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Using XLSForm with KoboToolbox</a>.
</p>

