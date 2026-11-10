# Connecting KoboToolbox data to Google Sheets and Data Studio

KoboToolbox allows you to connect project data to **Google Sheets** and **Data Studio** using the KoboToolbox [Application Programming Interface (API)](https://support.kobotoolbox.org/api.html). These connections allow you to retrieve updated submissions for analysis, reports, and dashboards without manually downloading new data files.

**Google Sheets** is a spreadsheet application for organizing and analyzing data, while **Data Studio** (formerly Looker Studio) is a reporting tool for creating interactive dashboards and visualizations.

You can connect KoboToolbox to Google Sheets using a [synchronous export link](https://support.kobotoolbox.org/synchronous_exports.html), then use the connected spreadsheet as a data source in Data Studio.

This article covers connecting KoboToolbox data to Google Sheets and Data Studio, refreshing the data, and troubleshooting common issues.

<p class="note">
  <strong>Note:</strong> The Google Sheets method described below uses a public synchronous export link and does not support authentication. It is only suitable for projects where submission data can be made public. For private projects, use an authenticated connection, such as a custom Google Apps Script, instead.
</p>

## Preparing to connect KoboToolbox to Google Sheets

Before connecting KoboToolbox to Google Sheets, you need to retrieve your project's synchronous export link and enable public access to submissions.

### Enabling public access to submissions

Google Sheets data import does not support authentication, so you must allow public access to your KoboToolbox project submissions.

To enable public access:
1. Open your KoboToolbox project and go to **SETTINGS > Sharing.**
2. Enable **Anyone can view submissions made to this form.**

This allows Google Sheets to access the synchronous export link without requiring your KoboToolbox credentials.

<p class="note">
  <strong>Note:</strong> Enabling this setting makes your project submissions publicly accessible, including to people outside your organization. Only use this method if your data is intended to be public. For more information, see <a href="https://support.kobotoolbox.org/project_sharing_settings.html">Sharing projects with project-level settings</a>.
</p>

### Retrieving your synchronous export link

A synchronous export link allows external applications to retrieve project data in CSV or XLSX format using saved export settings. The link remains the same, but the data is updated when the external application refreshes its connection.

<p class="note">
  To generate and retrieve your link, follow the instructions in <a href="https://support.kobotoolbox.org/synchronous_exports.html">Using the API for synchronous exports</a>.
</p>

For Google Sheets, use the CSV link, which provides your project data in CSV format.

<p class="note">
  <strong>Note:</strong> CSV exports do not include repeat group data. If your project contains repeat groups, you will need to use an XLSX export and a different import method to include those records.
</p>

## Connecting KoboToolbox to Google Sheets

Google Sheets provides an `IMPORTDATA()` function that retrieves data from a publicly accessible CSV file. You can use this function with your synchronous export link to import KoboToolbox submissions into a spreadsheet.

### Importing project data into Google Sheets

To import your publicly accessible KoboToolbox data: 
1. Open [Google Sheets](https://sheets.google.com/) and create a new spreadsheet, or add a new sheet to an existing spreadsheet.
2. Select cell **A1**.
3. Enter the following formula, replacing `YOUR_EXPORT_URL` with your synchronous export link: `=IMPORTDATA("YOUR_EXPORT_URL")`
4. Press **Enter**.
5. If you see the warning message “Warning: Some formulas are trying to send and receive data from external parties,” click **Allow access**.

<p class="note">
  <strong>Note:</strong> If the data is not imported correctly into separate columns, you may need to specify a semicolon as the delimiter: <code>=IMPORTDATA("YOUR_EXPORT_URL", ";")</code>
</p>

Google Sheets will retrieve the CSV data from KoboToolbox and populate the spreadsheet with your project submissions.

You can then use Google Sheets to filter, summarize, and analyze your data or create charts.

<p class="note">
  <strong>Note:</strong> Keep the cells populated by <code>IMPORTDATA()</code> clear of other content. If existing values block the imported data, Google Sheets may display an error.
</p>

## Connecting Google Sheets to Data Studio

Once your KoboToolbox data is available in Google Sheets, you can connect the spreadsheet to **Data Studio** to create interactive reports and dashboards.

Data Studio uses the Google Sheets connector to retrieve data from your spreadsheet. You do not need to configure a separate connection to KoboToolbox.

### Adding Google Sheets as a data source

To connect your spreadsheet to Data Studio:
1. Open [Data Studio](https://datastudio.google.com/) and create a new report.
2. In the **Add data to report** window, select **Google Sheets**.
3. Authorize access to your Google account if prompted.
4. Select the spreadsheet containing your KoboToolbox data.
5. Choose the worksheet containing the imported submissions.
6. Ensure **Use first row as headers** is selected.
7. Click **Add** or **Connect**, depending on the interface, and add the data source to your report.

Your KoboToolbox submission fields will now be available for creating charts, tables, filters, and other visualizations.

### Creating reports and dashboards
Once connected, you can use Data Studio to create visualizations based on your KoboToolbox data.

For example, you can:
* Create charts showing trends in data collection.
* Display summary statistics from your submissions.
* Add filters to explore data by location, date, or other variables.
* Combine data from multiple sources in a single report.

You can customize your report and share it with other users according to your organization's requirements.

<p class="note">
  <strong>Note:</strong> Data Studio reads data from the connected Google Sheet. If you add, remove, or rename columns in your spreadsheet, you may need to refresh the data source fields in Data Studio.
</p>

## Refreshing your data

When new submissions are received or existing records are edited or deleted in KoboToolbox, the changes must be retrieved by Google Sheets before they can appear in Data Studio.

### Refreshing data in Google Sheets

Google Sheets automatically checks for updates to `IMPORTDATA()` approximately every hour while the spreadsheet is open.

To manually trigger a refresh:
1. Select the cell containing the `IMPORTDATA()` formula.
2. Delete the formula.
3. Reenter the same formula and press **Enter**.

Google Sheets will request the data again from KoboToolbox.

<p class="note">
  <strong>Note:</strong> KoboToolbox synchronous exports are cached for up to five minutes, so recent submissions may not appear immediately after refreshing.
</p>

## Refreshing data in Data Studio

Data Studio periodically retrieves data from your connected Google Sheet according to its data freshness settings.

To review these settings:
1. Open your report in Data Studio.
2. Select **Resource > Manage added data sources**.
3. Edit the Google Sheets data source.
4. Open the **Data freshness** settings and select your preferred refresh interval.

You can also manually refresh your report using the refresh option in Data Studio.

<p class="note">
  <strong>Note:</strong> Refreshing Data Studio does not force Google Sheets to retrieve new data from KoboToolbox. The report can only display the data currently available in the connected spreadsheet.
</p>

## Connecting private KoboToolbox projects

If your project contains sensitive or private data, you should not enable public access solely to connect it to Google Sheets.

The `IMPORTDATA()` function does not support the authentication headers required to access private KoboToolbox API endpoints.

For private projects, you can use **Google Apps Script** or another application that supports authenticated API requests. These tools can retrieve data using your KoboToolbox API key and write the results to Google Sheets.

Once the data is available in a private Google Sheet, you can connect it to Data Studio using the same steps described above.

<p class="note">
  For more information about API authentication and retrieving project submissions, see <a href="https://support.kobotoolbox.org/api.html">Getting started with the API</a> and <a href="https://support.kobotoolbox.org/data_endpoint.html">Using the API data endpoint</a>.
</p>



## Troubleshooting

<details>
  <summary><strong>Google Sheets cannot import the data</strong></summary>
  <p>If Google Sheets displays an error when using <code>IMPORTDATA()</code>, check that:</p>
  <ul>
    <li>You are using the CSV synchronous export link.</li>
    <li>Your project allows public access to submissions.</li>
    <li>The export link is correct and accessible.</li>
    <li>The cells where the imported data should appear are empty.</li>
  </ul>
  <p>Large datasets may also exceed Google Sheets import or processing limits.</p>
</details>

<br>

<details>
  <summary><strong>New submissions do not appear</strong></summary>
  <p>If your spreadsheet does not show recent submissions:</p>
  <ol>
    <li>Confirm that the submissions are visible in your KoboToolbox project.</li>
    <li>Check whether your saved export settings include filters that exclude the submissions.</li>
    <li>Allow time for the synchronous export cache and Google Sheets import function to update.</li>
    <li>Reenter the <code>IMPORTDATA()</code> formula to request the data again.</li>
  </ol>
</details>

<br>

<details>
  <summary><strong>Data Studio is not showing updated data</strong></summary>
  <p>If your Google Sheet contains updated submissions but Data Studio does not:</p>
  <ol>
    <li>Check the data freshness settings in Data Studio.</li>
    <li>Manually refresh the report.</li>
    <li>Confirm that the correct spreadsheet and worksheet are connected.</li>
    <li>If the structure of your spreadsheet has changed, refresh the data source fields.</li>
  </ol>
</details>

<br>

<details>
  <summary><strong>Some fields are missing or incorrectly formatted</strong></summary>
  <p>Check your saved export settings in KoboToolbox to ensure the required questions are included.</p>
  <p>Google Sheets and Data Studio may also interpret some fields, such as dates or numeric values, differently. Review the column formatting in Google Sheets and field types in Data Studio.</p>
</details>

<br>
