# Connecting KoboToolbox to Power BI
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/ae9e699afd6c0ed484945430ba6722b974b99b49/source/pulling_data_into_powerbi.md" class="reference">22 Aug 2022</a>

The KoboToolbox API allows you to connect your project with other data analysis
tools such as Power BI, Excel and Google Sheets. Data you collect is shared with
the external application which can then be used for analysis and visualizations
and dashboards.

One of the most popular data analysis and visualization programs you can connect
to is [Microsoft Power BI](https://powerbi.microsoft.com).

This article walks you through the steps of connecting your project with Power
BI. If you would like to connect to Excel, refer to the article
[here](pulling_data_into_excelquery.md).

## Step 1: Get the synchronous exports URL

The first step in bringing data into Power BI is to get the synchronous exports
URL through the KoboToolbox API. A detailed process for doing this is outlined
in the article [here](synchronous_exports.md).

## Step 2: Add the data source

Once you have your URL, you can proceed with the steps below in Power BI:

- Click the drop-down arrow on the "Get Data" button
- Choose "Web"
- Paste the synchronous export URL you copied and click **OK**
- Click **Basic** for adding your authentication details
- Type your KoboToolbox username and password and click **CONNECT**

<p class="note">
  If you made your project's data public, you can connect without the need for
  authentication by choosing "Anonymous" in the "Access Web content" dialogue
  box. Learn more about project permissions
  <a href="managing_permissions.html" class="reference">here</a>.
</p>

A list of the data contained in your project will be displayed in the Navigator.

- Choose the data you would like to import.
- Click **Load** to bring the data in or click **Transform Data** to open the
  Power Query Editor, which you can use to clean up and transform the data
  before loading it.

![Get data and Authentication](images/pulling_data_into_powerbi/get_data_auth.gif)

The tables will be shown in the **Fields** panel where you can develop your
dashboards and reports.

<p class="note">
  In Power BI you can connect multiple projects. Repeat the process above for
  each project, using their synchronous export URL. In the case where you have
  multiple tables (for example if you had repeat groups), you might also need to
  set up table relationships. This is done in the <strong>Model View</strong>.
  Learn more about how to create table relationships
  <a
    href="https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships"
    class="reference"
    >here</a
  >.
</p>

## Updating the data in your reports

When your project's data is updated on the KoboToolbox server, such as when you
have new submissions, changed validation statuses, edits, or deletions, you will
need to synchronize it with your reports.

To do this, click **Refresh** in the "Home" tab.

## Troubleshooting

### Failing to connect to KoboToolbox

Sometimes, even after entering the correct credentials to connect to your
project, you might see an error. This may happen if Power BI was configured to
connect to one account before, and you are now trying to connect using a
different account from the same KoboToolbox server.

To reset authentication settings:

- Go to **File -> Options and Settings -> Data Source Settings**. Select the
  existing permissions in the dialogue box and click **Clear Permissions**.
  Close and try adding the new connection again.

![Clear Permissions](images/pulling_data_into_powerbi/data_source_settings.gif)

### Failing to refresh data

If you are getting an error when your refreshing data, there could be a number
of reasons:

- Your authentication details might have changed. You will need to follow the
  instructions above to change your **Data Source Settings**.
- One or more fields in your form might have been deleted or renamed. You will
  need to
  [edit the query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- There might be a data-type mismatch, especially if you changed the data-type
  of one or more fields in Power BI. You can attempt to reset the data-type
  before refreshing the connection.
