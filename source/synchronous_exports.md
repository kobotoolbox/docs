# Connecting to your data using synchronous exports
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/a41c940878a7d7b76a9f915ce3005dd9fb4d0a0a/source/synchronous_exports.md" class="reference">7 Jul 2022</a>

In this article, we'll explore how to use the synchronous exports feature to
connect your project data to programs such as Microsoft PowerBI, Excel, Google
Sheets, Tableau and others.

Using the KoboToolbox interface, in the **DATA>Downloads** tab of your project,
is [the standard method for exporting your data](export_download.md) into
multiple different formats. These exports are created in an "asynchronous"
fashion, meaning they are created in the background and you will see a
"Processing…" item in your downloads list until complete. This will generate a
"snapshot" of your data at the time of exporting. You can then download the
completed export for analysis outside the application.

There is also a [REST API](api.md) where project data can be queried in JSON or
XML format depending on your purposes, such as for automated scripts or
connecting with other applications. However, there are important advantages to
using the asynchronous exports over the REST API, such as specifying labels,
languages, filtering by question names, etc., which the JSON and XML formats do
not provide. This is particularly useful when creating dashboards in an external
application. The "synchronous exports" feature aims to make it easier to
seamlessly connect your data with an external application using the same export
settings in standard downloads. An API endpoint can be queried by an external
application allowing for a dashboard to automatically update with the latest
data.

## Steps to using the synchronous export feature

### Step 1: Generate a named export

- Within your KoboToolbox project, go to the **DATA>Downloads** tab.
- You can change different settings of your export, such as the "Value and
  Header format".
- Click "Advanced options" to customize the data that will be exported. For
  example, you can choose:
  - Which questions to export;
  - How "Select Many" questions will be exported;
  - Form versions from which the data will be exported: either all versions or
    just the latest one;
  - Whether to include groups in headers, and so on.
- Choose "Save selection as…" and enter a name for the export.
- Click **Export** to save the settings.

![Create export settings](/images/synchronous_exports/create-export-settings.gif)

### Step 2: Retrieve the synchronous export link

- Note the asset UID of your project. The asset UID is a unique ID assigned to
  each project in KoboToolbox and you can find it on the URL when you open the
  project. For example, in this URL:
  `https://kf.kobotoolbox.org/#/forms/arHt74WLoe2eQW4G7Zsqvy/data/table`, the
  asset UID is `arHt74WLoe2eQW4G7Zsqvy`.

![Asset UID](/images/synchronous_exports/asset-uid.png)

- Open a new tab in your browser and paste the following URL
  `https://{kf_url}/api/v2/assets/{asset_uid}/export-settings/`. Replace
  `{asset_uid}` with your project's asset UID and `{kf_url}` with the KPI URL of
  [the server you are using](server.md) (`kf.kobotoolbox.org` for the
  non-humanitarian server or `kobo.humanitarianresponse.info` for the
  humanitarian server).

![Export settings](/images/synchronous_exports/export-settings-url.png)

- Locate the name of the export setting you created in the interface. The two
  URLs, `data_url_csv` and `data_url_xlsx`, are your project's synchronous
  export links, one for a CSV file and the other for an Excel file.You can
  experiment with each to see which is best suited to your requirements.

![Export URL](/images/synchronous_exports/export-url.png)

- Copy the link for the data type you want to use.

Repeat groups in forms are exported as separate sheets in the Excel file and are
not included in the CSV export. Therefore if your project contains repeat
groups, you should use the `data_url_xlsx` link.

### Step 3: Connecting your data to an external application

There are many external applications that can connect to external data sources,
generally pulling data in regular intervals. However, not all applications
support authenticated requests, so your use-case and access to software licenses
will determine which is best suited for you. For the purposes of this article,
we will use the example of connecting your data to Google Sheets, without
authentication.

- Ensure that your project has the setting "Anyone can view submissions made to
  this form" checked in **SETTINGS>Sharing**.

![Sharing](/images/synchronous_exports/sharing.png)

- Create a new workbook in Google Sheets or open a new tab in an existing
  workbook.
- Paste the formula `=IMPORTDATA("{export_url}", ";")` in cell `A1`, replacing
  `{export_url}` with your `data_url_csv` URL and press ENTER. Your export will
  initiate and the cells will populate once complete.

![Google Sheets](/images/synchronous_exports/google-sheets.png)

- If you would like to refresh the data more regularly than Google does
  automatically, you can delete cell `A1` and then click the undo button. This
  will force Google Sheets to fetch the data again.

## Authentication

For projects that contain sensitive or private data it is important that the
option "Anyone can view submissions made to this form" is unchecked in
**SETTINGS>Sharing**. When using an application that can make authenticated
requests such as Power BI, token or basic authentication with your username and
password will be used to access the data. You can find your API token in your
**ACCOUNT SETTINGS**:

![Token](/images/synchronous_exports/token.png)

If you would like to test that you are able to successfully pull data from your
project using authenticated requests before integrating with another
application, you can use either of the following commands in a terminal or
alternatively with a REST client such as Postman (replacing the variables within
curly braces):

```bash
TOKEN=your-secret-token

# Using curl:
curl -L https://{kf_url}/api/v2/assets/{asset_uid}/export-settings/{export_settings_uid}/data.csv \
  -H "Authorization: Token $TOKEN" \
  -o data.csv

# Using wget:
wget https://{kf_url}/api/v2/assets/{asset_uid}/export-settings/{export_settings_uid}/data.csv \
  –header "Authorization: Token $TOKEN" \
  -O data.csv
```

For more information on connecting to PowerBI or Excel with Power Query,
continue reading [here](pulling_data_into_excelquery.md).

## Limitations

In order to protect the reliability of the server, there are some limitations
that have been placed on the synchronous export feature:

- Exported data is only refreshed every **5 minutes**. Therefore if you or your
  external application makes a request to the URL in less than 5 minutes after
  your last request, you will be served a cached copy of your last export, even
  if submissions have changed in the project during that time.
- Exports must complete within **120 seconds** otherwise they will fail. This
  means that projects with many submissions or projects with many questions will
  need to add a query constraint in the export settings to limit the number of
  submissions included in the synchronous export or filter out questions that
  aren't needed. If this is the case for you, please refer to the
  [forum thread here](https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4).
