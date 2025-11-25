# Selecting options from an external file
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/select_from_file_xls.md" class="reference">25 Nov 2025</a>

**Select from file** questions allow you to use a list of choice options stored in an external file instead of defining them directly in your form. There are two types: `select_one_from_file` for selecting a **single choice**, and `select_multiple_from_file` for selecting **multiple choices**. 

Using a separate file for your choice list makes it easier to manage long lists, reuse them across multiple forms, and update options when needed. Supported file formats include CSV, XML, and GeoJSON.

This article explains how to format your external file, set up your XLSForm to use **select from file** questions, and upload your external file to KoboToolbox.

<p class="note">
<strong>Note:</strong> This article focuses on adding select from file questions in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about adding select from file questions in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/external_file.html">Select One or Many From External File Question Type</a>.
<br><br>
  For hands-on practice with select from file questions in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Formatting external choice lists

To get started, create your list of choices in a separate external file. The required structure of this file depends on the format you choose (CSV, XML, or GeoJSON). Use a separate file for each choice list.

<p class="note">
  To learn more about formatting XML or GeoJSON files, see <a href="https://xlsform.org/en/#multiple-choice-from-file">XLSForm</a> and <a href="https://docs.getodk.org/form-datasets/#building-selects-from-geojson-files">ODK documentation</a>. GeoJSON files are primarily used for <a href="https://support.kobotoolbox.org/select_from_map_xls.html">selecting options from a map</a>.
</p>

For CSV files, the structure is similar to the choices worksheet in an XLSForm. It should include the `name` and `label` columns, but the `list_name` column is not needed. 

**External CSV file**

| name    | label     |
|:--------|:----------|
| option1 | Option 1  |
| option2 | Option 2  |
| option3 | Option 3  |

If your file uses different names for the choice name and label, you can specify this in your XLSForm (see instructions [below](https://support.kobotoolbox.org/select_from_file_xls.html#configuring-choice-name-and-label-columns)).

<p class="note">
<strong>Note:</strong> Use short, simple file names for your external files, avoiding spaces or special characters. The file name will be used in your XLSForm to link questions to their choice lists. If you use multiple external files, make sure each one has a unique name, even if they use different file types.
</p>

## Setting up your XLSForm

To add a select from file question to your XLSForm:
1. In the `type` column of the `survey` worksheet, enter the select from file question type (`select_one_from_file` or `select_multiple_from_file`).
2. In the same cell, instead of the choices `list_name`, add a single space and the name of the external file, including the file extension. 
    - For example: `select_one_from_file households.csv`

**survey worksheet**

| type                     | name | label           |
|:-------------------------|:-----|:----------------|
| select_one_from_file households.csv | hh   | Select household |
| survey |

### Configuring choice name and label columns

If your external file uses different column names instead of `name` and `label`:
1. Add a **parameters** column to the `survey` worksheet 
2. In the select from file question row, specify the custom names with the `value` and `label` parameters.
    - `value` represents the choice **name**.
    - `label` represents the choice **label**.

**survey worksheet**

| type                     | name | label            | parameters                   |
|:-------------------------|:-----|:-----------------|:-----------------------------|
| select_one_from_file households.csv | hh   | Select household | value=housenum label=housename |
| survey | 

## Uploading the external file to KoboToolbox

When uploading your XLSForm to KoboToolbox, you must also upload the external file that contains your list of choices:
1. In KoboToolbox, navigate to the project **SETTINGS** page.
2. In the **Media** tab, upload the external file. Ensure the file name matches exactly the file name specified in the XLSForm.

To update your list of choices, edit the external file as needed, re-upload it to KoboToolbox, and redeploy your form.

![Upload media](images/select_from_file_xls/upload_media.png) 

## Troubleshooting

<details>
  <summary><strong>Translated choice lists</strong></summary>
  Select from file questions do not currently support <a href="https://support.kobotoolbox.org/language_xls.html">translated choice lists</a>. Your external choice file can include only a single <code>label</code> column. Any additional translated <code>label</code> columns will be ignored in Enketo or will cause an error in KoboCollect. For forms that include translations, use internal choice lists instead, or set up multiple <strong>select from file</strong> questions using skip logic to pull from different files depending on the form language.
</details>



