# Pulling data from an external CSV 
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/bdf046e95ac9a5302be29803281c48f39e961b0c/source/pull_data_kobotoolbox.md" class="reference">8 Dec 2025</a>

The `pulldata()` function in XLSForm lets you dynamically retrieve information from an external CSV file while completing a form. This allows you to reference existing datasets and automatically pull in related details, avoiding the need for enumerators to re-enter the same information.

For example, you can use `pulldata()` to:
- **Auto-fill related information:** When an ID, code, or key is entered, automatically retrieve linked details such as a name, category, or description.
- **Preload background data:** Load information from external files so enumerators only need to collect new or updated data.

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

| ID           | status          | 
|:-----------  |:----------------|
| AH784N       | eligible        |
| DB839K       | ineligible      | 
| SH849T       | eligible        |

## Setting up your XLSForm

Once you have set up your external CSV, configure your XLSForm in the following way:

1. Ensure your XLSForm includes a question that serves as the **index variable**.
2. Add a `calculate` field to your survey. Give the field a `name`.
3. In the `calculation` column, use the **pulldata()** function to specify which field in the CSV to pull from. Use the following syntax: `pulldata('csv','pull_from', 'csv_index', '${survey_index}')`.	
    - `csv` is the name of the CSV file, without the extension.
    - `pull_from` refers to the column in your CSV file that contains the data you want to import into your form.
    - `csv_index` is the column in your CSV file that contains the **index variable.**
    - `survey_index` is the name of the question in your survey that contains the **index variable.**
  
  **survey worksheet**

  | type      | name               | label                                      | calculation |
|:-----------|:------------------|:-------------------------------------------|:-------------|
| text       | respondent_id      | Respondent ID                              |              |
| calculate  | eligibility_status |                                            | pulldata('eligibility', 'status', 'ID', 'respondent_id') |
| note       | eligibility_note    | Respondent is ${eligibility_status} for the study. |              |
| survey | 

In the example above, the calculation retrieves the value from the `status` column of the `eligibility.csv` file, in the row where the `ID` in the CSV matches the ID entered in the `respondent_id` question of your form.

<p class="note">
<strong>Note:</strong> After using the <code>pulldata()</code> function to retrieve external CSV data, you can reference that field in subsequent skip logic conditions, constraints, and labels, just like any other field or calculation.
</p>

## Uploading your external CSV to KoboToolbox

The final step in linking your external CSV file to your form is uploading the file to KoboToolbox. To do this:
1. Navigate to your project **SETTINGS**, and open the **Media** tab.
2. Upload the CSV file(s) with the exact name you have used in your XLSForm.
3. Deploy or redeploy the form.

![Upload media](images/pull_data_kobotoolbox/upload_media.png) 

## Troubleshooting

<details>
  <summary><strong>Non-English fonts or special characters are not displaying correctly</strong></summary>
  Save your CSV file in <strong>UTF-8 format</strong>. This ensures that Android devices can render non-English text or special characters properly.
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

