# Data collection using KoboCollect
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/data_collection_kobocollect.md" class="reference">31 Oct 2025</a>


<iframe src="https://www.youtube.com/embed/IEm61fpLoz4?si=TdlWhcVt0OxETlxl" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect is a free, open-source KoboToolbox app designed for data collection on Android mobile devices. Before you get started, [install and configure](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) the KoboCollect app. 

Once set up, KoboCollect allows you to fill and submit forms from your mobile device, even offline. This article explains how to use the app to collect data, including accessing forms, saving and editing responses, and sending finalized submissions.

## Downloading forms

To begin data collection with KoboCollect, you will need to download the KoboToolbox form(s) to your device. Before downloading, ensure you have:

- At least one [deployed form](https://support.kobotoolbox.org/deploy_form_new_project.html) in your KoboToolbox account (either owned by or shared with you).
- A project (account) [set up on KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html).
- An internet connection on your device.
  
To download forms to your device:
- From the main menu, click **Download form**.
- Select the form(s) you wish to download individually by tapping the checkbox next to each form, or tap **Select All** to download all deployed forms.
- Tap **Get Selected**.

Downloaded forms will appear when you click on **Start new form** from the app main menu.

<p class="note">
  <strong>Note:</strong> You will need to repeat this process any time an update is made to the form or form media. If you anticipate frequent form updates or are using <a href="https://support.kobotoolbox.org/dynamic_data_attachment.html">dynamic data attachments</a>, we recommend enabling <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">automatic form downloads</a>. 
</p>

## Collecting data

Once forms are downloaded, you can begin data collection. Note that once you have downloaded the form(s) in the app, you do not need an internet connection to collect data. 

1. From the main menu, tap **Start new form**.
2. Select the form you wish to collect data with.
3. To change the form language, tap the <i class="k-icon-more"></i> **three dots icon** in the top right corner of the screen and click **Change Language**.
4. Navigate through questions by swiping left or clicking **NEXT** after answering.
5. At the end of the survey, you can choose to **Save as draft**, **Finalize**, or **Send** the form (depending on your [project settings](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings)).

| **Option** | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Save as draft  &emsp;&emsp;&emsp;        | The form will be saved to **Drafts** and can still be edited before finalizing. |
| Finalize      | The form will be saved to **Ready to send** and can no longer be edited. This option appears only if the **Auto send** setting is set to **Off**.                                  |
| Send           | The form will be sent to the server directly or queued until an internet connection is available. It can no longer be edited. This option appears only if the **Auto send** setting is enabled.            |

By default, forms and data remain on the device until manually deleted. If you enable **Delete after send** in the [project settings](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings), forms will be deleted automatically once they have been submitted to the server.

## Editing drafts

If you saved a survey as a draft, you can edit it before sending it to the server:

1. From the main menu, select **Drafts**.
2. A list of saved draft forms will appear. Select the one you want to edit.
3. Make the necessary changes, then tap **Finalize** or **Send**, depending on your workflow.

<p class="note">
  <strong>Note:</strong> You do not need an internet connection to edit a saved form in KoboCollect.
</p>

## Sending finalized forms to the server

After finalizing your forms, you must upload them to the KoboToolbox server. Forms are often completed and finalized offline, then uploaded in bulk once an internet connection is available. To send your forms to the KoboToolbox server:

1. Ensure the device has a secure internet connection.
2. From the main menu, tap **Ready to send**. A list of finalized forms will appear.
3. Tap **Select All**, or manually select the forms you want to upload by ticking the checkbox.
4. Tap **Send Selected** to submit the forms to the server.

To verify successful upload, go to the main menu and select **Sent**. You will see all forms sent to the server, along with their synchronization date.

<p class="note">
  <strong>Note:</strong> If your project is <strong>set to automatically send finalized forms</strong>, the <strong>Ready to send</strong> page will not appear in the main menu, and you can skip these steps. For more information on project settings in KoboCollect, see <a href="https://support.kobotoolbox.org/kobocollect_settings.html">Customizing KoboCollect settings</a>.
</p>

## Deleting saved forms and blank forms

After finalizing data collection and uploading all completed forms to the server, you may want to delete remaining form data from the KoboCollect app, unless automatic deletion is [already enabled](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) for your device. This helps protect data privacy and prevents confusion when collecting data for a new project.

There are two types of forms that can be deleted:

- **Saved Forms**: These are forms for which data has been filled in, including drafts, finalized forms, and forms that have been sent to the server.
- **Blank Forms**: These are empty data collection forms that have downloaded to the device from the **Download form** page. Only delete these forms once data collection for them has ended.
  
To delete forms:
1. From the main menu, tap **Delete form**. You will see two tabs.
2. Under **Saved Forms**:
    - Tap **Select All** to delete all saved forms, or select individual forms.
    - Tap **Delete Selected**.
3. Under **Blank Forms**:
    - Tap **Select All** to delete all blank forms, or select individual forms.
    - Tap **Delete Selected**.

<p class="note">
  <strong>Note:</strong> You do not need an internet connection to delete saved forms in KoboCollect. However, if blank forms are accidentally deleted offline, an internet connection is required to recover them for continued data collection. To prevent accidental deletion, you can set access controls in the <a href="https://support.kobotoolbox.org/kobocollect_settings.html#access-control">project settings</a>.
</p>


