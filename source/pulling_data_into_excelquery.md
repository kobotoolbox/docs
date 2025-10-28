# Connecting KoboToolbox to Microsoft Excel
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c8c238efa59b04f403f13c150b018e1807c66d5c/source/pulling_data_into_excelquery.md" class="reference">28 Oct 2025</a>

<a href="es/pulling_data_into_excelquery.html">Leer en español</a> | <a href="fr/pulling_data_into_excelquery.html">Lire en français</a> | <a href="ar/pulling_data_into_excelquery.html">اقرأ باللغة العربية</a>
such as Microsoft Excel, Power BI or Google Sheets which is made possible
through the Application Programming Interface (API).

This article walks you through the process of connecting your project to Excel.
If you would like to connect to Power BI, refer to the article
[here](pulling_data_into_powerbi.md).

## Step 1: Get the synchronous exports URL

To bring data into Excel, you first need to get the synchronous exports URL
through the KoboToolbox API. The step by step process for doing this is outlined
in the article [here](synchronous_exports.md).

## Step 2: Add the data source

<p class="note">These steps only work in Excel 2016 and later.</p>

- Open Excel and create a blank workbook. You can also work within an existing
  workbook, even if it already has data.
- Click the **Data** tab, choose **Get Data -> From Other Sources -> From Web**.
- Paste the synchronous exports URL you copied and click **OK**.

![Get data](images/pulling_data_excelquery/get_data.gif)

- Within the "Access Web content" dialogue box, click **Basic** for adding your
  authentication details.
- Enter your KoboToolbox username and password and click **CONNECT**.

![Authentication](images/pulling_data_excelquery/authentication.gif)

<p class="note">
  If you made your project's data public, you can connect without authentication
  by choosing "Anonymous" in the "Access Web content" dialogue box. Learn more
  about project permissions
  <a href="managing_permissions.html" class="reference">here</a>.
</p>

A list of the data contained in your project will be displayed in the Navigator.

<p class="note">
  If your form has repeat groups, each group will show up as a separate
  worksheet in the Navigator. Ensure that you use the "data_url_xlsx" link as
  the CSV export <em>does not</em> include repeat groups.
</p>

- Choose the data you would like to import. To import multiple tables at once,
  click "Select multiple items", then choose the items from the list.
- Click **Load** to bring the data in or click **Transform Data** to open the
  Power Query Editor which you can use to clean up and transform the data before
  loading it in.

![Choosing tables](images/pulling_data_excelquery/navigator.gif)

<p class="note">
  You can connect multiple projects in one Excel workbook. Repeat the process
  above for each project, using their synchronous export URL. In most cases
  where you have multiple tables, it may be necessary to set up table
  relationships before you can use the fields to create reports and dashboards.
  Set up relationships by going to
  <strong>Data -> Data Tools -> Relationships</strong>. Learn more about
  creating table relationships
  <a
    href="https://support.microsoft.com/en-us/office/create-a-relationship-between-tables-in-excel-fe1b6be7-1d85-4add-a629-8a3848820be3"
    class="reference"
    >here</a
  >.
</p>

### Using the imported data

Excel gives you several ways to work with the data you have just imported.

#### 1. Create PivotTables and PivotCharts from the Data Model

A PivotTable is a powerful tool used to calculate, summarize, and analyze data -
allowing you to see comparisons, patterns, and trends in the data. Data
summarized in PivotTables can be visualized in a simple manner using
PivotCharts.

- Click the **Insert tab**, then click on the drop-down arrow on PivotTable
- Choose **From Data Model**
- Choose **New Worksheet**
- Click **OK**

![Creating a pivot table](images/pulling_data_excelquery/pivot.gif)

The imported tables will be shown in the **PivotTable Fields** side pane where
you can choose the needed fields.

#### 2. Load data into the worksheet

When you import a single table, such as when your project did not have any
repeating groups, the data is automatically loaded as a table on the worksheet.
However, when your data comes as multiple tables, the tables are listed in the
**Queries & Connections** panel.

To load this data into your worksheet:

- Right-click a table from the **Queries and Connections** pane and choose
  **Load To**. (if you don’t see the pane, go to **Data -> Queries and
  Connections**.
- On the next dialogue box, choose **Table** and click **OK**. You may also
  choose the other available options depending on your need.

![Loading a table in Excel](images/pulling_data_excelquery/load_table.gif)

You can do this for all the tables listed in the **Queries and Connections**
pane.

## Updating the data in your reports

When your project's data is updated on the KoboToolbox server, such as when you
have new submissions, changed validation statuses, edits, or deletions, you will
need to synchronize it with your reports. In Excel:

- Navigate to the **Data** tab
- Under "Queries and connections", click **Refresh**

## Troubleshooting

### Failing to connect to KoboToolbox

Sometimes, even after entering the correct credentials to connect to your
project, you might get an error. This may happen if Excel was configured to
connect to one account before, and you are now trying to connect using a
different account from the same KoboToolbox server, i.e. both from the
Humanitarian server.

To reset authentication settings:

- Go to **Data tab -> Get Data -> Data source settings**. Select the existing
  permissions in the dialogue box and click **Clear Permissions**. Close and try
  adding the new connection again.

![Clearing data source settings](images/pulling_data_excelquery/data_source_settings.gif)

### Failing to refresh data

If you are getting an error when refreshing data, there could be a number of
reasons:

- Your authentication details might have changed. You will need to follow the
  instructions above to change your **Data Source Settings**.
- One or more fields in your form might have been deleted or renamed.
  [You will need to edit the query in Power Query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- There might be a data-type mismatch, especially if you changed the data-type
  of one or more fields in Excel. You can attempt to reset the data-type before
  refreshing the connection.
