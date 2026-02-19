# Pulling data from an external CSV 
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/d9b44de6b0f7192771a9f7bf86edf271321f398b/source/pull_data_kobotoolbox.md" class="reference">27 Jan 2026</a>

The `pulldata()` function in XLSForm lets you dynamically retrieve information from an external CSV file while completing a form. This allows you to reference existing datasets and automatically pull in related details, avoiding the need for enumerators to re-enter the same information.

For example, you can use `pulldata()` to:
- **Auto-fill related information:** When an ID, code, or key is entered, automatically retrieve linked details such as a name, category, or description.
- **Preload background data:** Load information from external files so enumerators only need to collect new or updated data.

<p class="note">
    <strong>Note:</strong> The <code>pulldata()</code> function uses external CSV files as its data source. If you want to reference data from another KoboToolbox project instead of a CSV file, you can use <a href="https://support.kobotoolbox.org/dynamic_data_attachment.html">dynamic data attachments</a>.
</p>

Using `pulldata()` helps reduce errors, saves time during data collection, and ensures that forms remain consistent with external reference datasets. This function is supported in both the <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">KoboCollect Android app</a> and <a href="https://support.kobotoolbox.org/enketo.html">Enketo web forms</a>. We recommend using <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a> to set up the `pulldata()` function.

This article covers the following steps for pulling data from an external CSV:
- Setting up your external CSV
- Setting up your XLSForm
- Uploading your external CSV to KoboToolbox

## Setting up your external CSV

To use `pulldata()`, first prepare an external CSV file containing the reference data you want to retrieve. Each row should represent a unique record (for example, a participant, location, or item) and the file should include at least two columns. One column must contain the **index variable** that matches the values entered in your form.

The **index variable** acts as the [primary key](https://en.wikipedia.org/wiki/Primary_key) that links your XLSForm to the external CSV. It should be a unique identifier that exists in both files, such as a participant ID, a district name, or another matching code.

The remaining columns can include any additional details you want to retrieve, such as names, categories, or descriptions. Ensure the CSV file is clean, consistently formatted, and saved with the `.csv` extension.

**Example: eligibility.csv**

| ID           | status          | age             | 
|:-----------  |:----------------|:----------------|
| AH784N       | eligible        | 19              |
| DB839K       | ineligible      | 37              |
| SH849T       | eligible        | 42              |

<p class="note">
<strong>Note:</strong> To use <code>pulldata()</code> with <code>select_one</code> or <code>select_multiple</code> questions, the value in the external file must match the <strong>choice name</strong>, not the choice label. For <code>select_multiple</code> questions, list multiple choice names separated by a space.
</p>

## Setting up your XLSForm

Once you have set up your external CSV, configure your XLSForm in the following way:

1. Ensure your XLSForm includes a question that serves as the **index variable**.
2. Add a new question to your form to retrieve data from the external file, using one of the two approaches below:
    * Add a `calculate` question to retrieve and store values for later use in the form or dataset. For example, you can use it to display a value in a note or question label, or to use the value in calculations and skip logic.
    * Add a `text`, `integer`, `decimal`, `date`, `select_one`, or `select_multiple` question to include retrieved values as default responses in editable fields.
3. In the `calculation` column of your new question, use the **pulldata()** function to specify which field in the CSV to pull from. Use the following syntax: `pulldata('csv','pull_from', 'csv_index', ${survey_index})`.	
    - `csv` is the name of the CSV file, without the extension.
    - `pull_from` refers to the column in your CSV file that contains the data you want to import into your form.
    - `csv_index` is the column in your CSV file that contains the **index variable.**
    - `survey_index` is the name of the question in your survey that contains the **index variable.**
  
  **survey worksheet**

  | type      | name               | label                                      | calculation |
|:-----------|:------------------|:-------------------------------------------|:-------------|
| text       | respondent_id      | Respondent ID                              |              |
| calculate  | eligibility_status |                                            | pulldata('eligibility', 'status', 'ID', ${respondent_id}) |
| note       | eligibility_note   | Respondent is ${eligibility_status} for the study. |              |
| integer    | respondent_age     | Respondent age | pulldata('eligibility', 'age', 'ID', ${respondent_id}) |
| survey | 

In the example above, the calculation retrieves the value from the `status` column of the `eligibility.csv` file, in the row where the `ID` in the CSV matches the ID entered in the `respondent_id` question of your form. Then, it retrieves and displays the respondent’s age from the `age` column of the `eligibility.csv` file.

<p class="note">
<strong>Note:</strong> After using the <code>pulldata()</code> function to retrieve external CSV data, you can reference that field in subsequent skip logic conditions, constraints, and labels, just like any other field or calculation.
</p>

## Uploading your external CSV to KoboToolbox

The final step in linking your external CSV file to your form is uploading the file to KoboToolbox. To do this:
1. Navigate to your project **SETTINGS**, and open the **Media** tab.
2. Upload the CSV file(s) with the exact name you have used in your XLSForm.
3. Deploy or redeploy the form.

![Upload media](images/pull_data_kobotoolbox/upload_media.png) 

<p class="note">
    To learn more about uploading media files, see <a href="https://support.kobotoolbox.org/upload_media.html">Uploading media files to a project</a>.
</p>

## Troubleshooting

<details>
  <summary><strong>Non-Latin fonts or special characters are not displaying correctly</strong></summary>
  Save your CSV file in <strong>UTF-8 format</strong>. This ensures that Android devices can render non-Latin text or special characters properly.
</details>

<br>

<details>
  <summary><strong>Numeric values are not working as expected</strong></summary>
  All data pulled from a CSV file is treated as text. To use these values as numbers, apply the <code>int()</code> or <code>number()</code> <a href="https://support.kobotoolbox.org/functions_xls.html">functions</a> to the retrieved value in your XLSForm.
</details>

<br>

<details>
  <summary><strong>Protecting sensitive data</strong></summary>
  If your CSV contains sensitive information that you do not want uploaded to the server, upload a blank CSV file with your form. Then manually replace it on each device with the real CSV file. This approach only works with the KoboCollect app.
</details>

<br>

<details>
  <summary><strong>Slow form loading with large files</strong></summary>
  If you are using very large CSV files, you may experience slow form loading in KoboCollect. To resolve this, we recommend using the <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">trigger</a> column to pull data from the external file once, rather than recurrently in the background.
</details>

<br>

<details>
  <summary><strong>Pulling dates from external CSV files</strong></summary>
  If you are storing dates in an external CSV file and want to pull them into a form, ensure they are in the format YYYY-MM-DD. If you are editing your CSV in Excel, add a single quote <code>'</code> in front of the date to avoid automatic date formatting in Excel.
</details>

<br>

<details>
  <summary><strong>Pull data not working properly</strong></summary>
  If the pulldata() functionality is not working properly, try the following:
  <ul>
  <li>Rename your CSV file to remove underscores or special symbols.</li>
  <li>Check that your CSV file is adequately set up with one variable per column (see <a href="https://community.kobotoolbox.org/t/pulldata-is-not-working-on-kobocollect-android/6462/39">Community Forum</a> post).</li>
  <li>Check that you are using the exact spelling for file names and column names.</li>
  <li>Check that the cells in your CSV file do not include extra spaces before or after the value.</li>
</ul>
</details>

<br>

