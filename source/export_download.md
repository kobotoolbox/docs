# Exporting and Downloading Your Data

KoboToolbox allows you to download the data you have collected in several
different formats. There are a number of customizations you can make to your
export settings.

To download your data:

- Open your project and navigate to **DATA -> Downloads**.

![Navigating to the Dowloads screen](images/export_download/data_downloads.gif)

- Choose your export settings (described further in the sections below).
- Click **EXPORT**. This will generate an export which will be shown in a table
  below.
- Click **DOWNLOAD** to download the exported file.

![Download screen](images/export_download/download.png)

<section class="note">

Each new export can take between a few seconds and several minutes to be created
(depending on the size of the file) and will be shown below in the **Exports**
section of the page.

Each export is retained as a unique snapshot in the system and shows the date
and time each export was originally created, so it is possible to go back to
previous non-deleted exports.

</section>

## Export types

You can choose from one of the following export types:

- **XLS** - Microsoft Excel file
- **CSV** - Comma Separated Values file. This file type is great for importing
  into almost any data management software, such as databases
- **GeoJSON** - Open standard geospatial data interchange format best for
  integrating with GIS software, such as ArcGIS
- **SPSS Labels** - Generates SPSS syntax file which will apply question labels
  and value labels to variables of KoboToolbox data imported into SPSS when run.
  Learn more about importing data into SPSS (and STATA)
  [here](https://support.kobotoolbox.org/converting_to_spss_and_stata.md)
- **CSV (legacy)** - Generates a CSV file using a legacy interface of
  KoboToolbox
- **GPS Coordinates (KML)** - Generates a KML file which can be used to work
  with your data in GIS software, such as Google Earth
- **XLS (legacy)** - Generates an XLSX (Microsoft Excel) file using a legacy
  interface of KoboToolbox
- **Media Attachments (ZIP)** - Downloads a ZIP file with all the media
  collected through the form

<p class="note">If your form has repeat groups, each repeat group will be exported as a separate
sheet in the exported file. Only the XLSX format supports having multiple
sheets. Hence, it is recommended to export your data as XLSX if your form has
repeat groups. If you need to merge the repeat data with the main survey data,
follow the instructions in the article
<a href="https://support.kobotoolbox.org/merging_dataset_excel_power_query.html">here</a>.</p>

## Value and header format

When you choose the non-legacy export formats (XLS, CSV, GeoJSON and SPSS
Labels), you also have the option to choose the format of the data values and
headers. Here the options are:

- **Labels (default)** - The exported file will use the question labels
  (question text) as column headers and value labels for the responses (in the
  case of “Select One” and “Select Many” questions)
- **XML values and headers** - The exported file will use the “Data Column
  Names” (variable names) as column headers and XML values for the responses (in
  the case of “Select One” and “Select Many” questions)

## Advanced options

Aside from being able to customize the value and header format, non-legacy
formats also allow you to customize other aspects of the exported file. You can
find these options when you click **Advanced Options**.

![Download Settings](images/export_download/download_settings.png)

- **Export Select Many questions as**: This option allows you to choose how you
  want “Select Many” questions to be exported. You can choose to export them as:

  - _Single and separate columns_ : This is the default settings that will
    export a column with all the selected options in the “Select Many” question,
    as well as separate columns for each response, as shown below.

    ![Download Settings](images/export_download/select_many_options.png)

In the separate columns, the value 1 means the option was selected, while 0
means the respondent did not pick the option.

- _Separate columns_: Each response in the “Select Many” question will be
  exported into separate columns.
- _Single column_: Selected responses in the “Select Many” question will be
  exported into a single column.
- **Include groups in headers**: Choose this option when you want the group
  names to be added to each question header, as shown in the example below.

  ![Download Settings](images/export_download/group_headers.png)

- **Store date and number responses as text**: By default, “Date”, “Date &
  Time”, “Number” and “Decimal” questions are saved in their corresponding data
  type. If you instead want to export them as text, turn on this option.
- **Include data from all … versions**: By default, this option is checked. When
  selected, this option allows you to download the data from all your form
  versions. When unchecked, you will only be able to download the data from the
  latest deployed form version.
- **Include media URLs**: If your form collected media such as _photos_,
  _audios_, _videos_ and _files_, you can turn this option **ON** to ensure that
  your exported file includes links to the files in KoboToolbox.
- **Select questions to be exported**: If you want to export data from a few
  questions, you can turn this option **ON** and uncheck the questions you don’t
  want to export.
- **Save selection as…**: After defining your export settings, you can turn
  **ON** this option and enter a name for the export settings. When you click
  the **EXPORT** button, the export settings will be saved and the name will
  appear in the “Apply saved export settings” box. This is helpful for when you
  want to use the same settings to export another file later. It is also useful
  when you are
  **[generating a synchronous exports link you can later use to pull your data into software such as PowerBI or Excel](synchronous_exports.md)**.

## Solving exports stuck in pending state

If you have XLS exports stuck in the pending state:

- Remove the stuck exports by clicking on the red trash can icon for each one.
- Retry the exports by clicking the **EXPORT** button again.
- Please note that any export stuck in the "Pending" state for longer than an
  hour will likely never succeed; if you encounter such an export, please feel
  free to delete it and create a new export.

You should not have any trouble creating new exports from this point forward,
but if you do, please don't hesitate to let us know on the
**[community forum](https://community.kobotoolbox.org/)**.
