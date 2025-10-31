# Advanced options for exporting data
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/b70cdbf084f645b5cefa1a9368456f8f37b7245c/source/advanced_export.md" class="reference">17 Oct 2025</a>


Advanced options provide greater control and flexibility when downloading and exporting your data. This article will guide you through customizing your data exports, from selecting data fields and handling various question types to setting parameters for different analytical needs.

<p class="note">
    To learn more about downloading data, including an overview of export types and available formats, see <a href="https://support.kobotoolbox.org/export_download.html?highlight=export">Exporting and downloading your data.</a>
</p>

## Export options for multiple select questions

The **Export Select Many questions as…** option allows you to choose how to export data from **Select Many** (also called `select_multiple`) questions. You can choose to export them as:

| **Export option**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Single and separate columns &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | This default setting exports one column with all selected options from <strong>Select Many</strong> questions, plus individual columns for each response, as shown below.<br> ![How to select many columns](images/advanced_export/select_many_columns.png) |
| Separate columns  | Each response to <strong>Select Many</strong> questions will be exported into separate columns.|
| Single column   | Responses to <strong>Select Many</strong> questions will be exported into a single column.            |


<p class="note">
  <strong>Note:</strong> In the separate columns, a value of '1' indicates the option was selected, while '0' means the respondent did not choose that option.
</p>

## Selecting data fields for export

Advanced export options allow you to refine your data download by including data from all form versions or selecting specific questions to export.

| **Export setting**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Include data from all […] versions &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | By default, this option is checked. This allows you to download data from all form versions, including deleted questions or choices. If unchecked, only data from the latest deployed form version will be downloaded. |
| Select questions to be exported | To export data from specific questions, enable this option and select the questions to include. |
| Data range | To export data submitted within a specific date range, enable this option and select the start and/or end dates. Date filters are based on submission time and use the UTC time zone. Date submitted on the <strong>start</strong> and <strong>end</strong> dates are included in the exports. |

![How to select data fields](images/advanced_export/select_data_fields.png)

## Additional data format options

KoboToolbox offers additional data format options to further customize your exports, such as including group names in headers, storing date and number responses as text, or including media URLs.

| **Export setting**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Include groups in headers | Choose this option to add group names to each question header, as shown in the example below. ![Include groups in headers](images/advanced_export/group_headers2.png) | 
| Store date and number responses as text &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | By default, <strong>Date, Date & Time, Number,</strong> and <strong>Decimal</strong> questions are saved with their corresponding data types when exported to XLS. Check this option if you prefer to export them as text.<br><br><strong>Note:</strong> Excel time formats do not support timezone data; therefore, any timezone data in the response value will be removed during export. To retain this information, check the option to export dates as text values. |
| Include media URLs | If your form collected media (photos, audio, videos, or files), check this option to ensure your exported file includes links to these media files. |

## Saving export settings

You can save your defined export settings for future use or to generate a [synchronous export](https://support.kobotoolbox.org/synchronous_exports.html) link for software like PowerBI or Excel.

| **Export setting** | **Description**                                |
| :-------------------- | :------------------------------------ |
| Save selection as… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Check this option and enter a name for your export settings. When you click <strong>EXPORT</strong>, these settings will be saved and the name will appear in the <strong>Apply saved export settings</strong> box. | 

To use saved export settings, click on the dropdown menu under **Apply saved export settings** and select the named export settings of your choice.

