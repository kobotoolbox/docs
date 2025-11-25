# Form Settings and Metadata
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/e86e7d8a6cc6528808cea9efbb18b772b0c56df4/source/form_meta.md" class="reference">19 Nov 2025</a>


In the formbuilder, there are a number of optional configurations you can set
for your project. You can access these by clicking on the **Layout & Settings**
button.

![Form meta](/images/form_meta/form_meta.png)

## Form style

You can change the way the form appears in Enketo web forms, such as multiple
pages, grid theme, etc., in the **Form Styles** drop-down menu. Learn more about
the different form styles [here](alternative_enketo.md).

## Form metadata

Metadata are hidden questions that can aid data analysis and can be used for
auditing and data integrity purposes. The metadata is captured in the background
during the normal data collection process:

| Metadata         | Description                                                                                                                                                |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Start Time       | Records the exact time and date when a submission is started.                                                                                              |
| End Time         | Records the date and time when a submission is finalized.                                                                                                  |
| Today            | Records the date of the submission.                                                                                                                        |
| Username         | In KoboCollect, records the username saved in the [KoboCollect app settings](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings). If no username is set, it records the one used to sign in to the server. In Enketo, records the account username only if [authentication is required](https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication).<br><br>**Note:** Because the username field can be edited in KoboCollect, it may not match the account used to authenticate to the server. To see which account submitted the data, refer to the automatically generated `_submitted_by` field. |
| Audit            | Captures a detailed log of the interview process, including start time, end time, location, and user actions during the entire data collection process. This metadata question is not supported in Enketo. Learn more about audit logging [here](audit_logging.md)                                             |
| Background Audio | Records [audio in the background](https://support.kobotoolbox.org/recording-interviews.html) while a form is open.                                                                                                                         |
| Device ID        | Records the unique identification of the device or browser used to collect data. The device ID is automatically generated and cannot be modified by users.<br><br>**Note:** In KoboCollect, the device ID is updated whenever the app is reinstalled on a device. In Enketo, the device ID resets any time a new browser window is used.                                                                        |
| Phone Number   | Records the phone number stored in the [KoboCollect app settings](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings). This metadata question is not supported in Enketo.   |

### Adding form metadata in XLSForm

If you are building your form in XLSForm, you can add metadata as follows:

| type             | name             |
| :--------------- | :--------------- |
| start            | start            |
| end              | end              |
| today            | today            |
| username         | username         |
| audit            | audit            |
| background-audio | background_audio |
| deviceid         | deviceid         |
| phonenumber      | phonenumber      |
| survey           |                  |

<p class="note">
  No labels are required as the questions are not visible within the form
  itself during data collection
</p>

## Background audio

When the "Background audio" setting is turned on, audio will be recorded
while the form is open. Learn more about background audio recording
[here](recording-interviews.md).

## Details

When creating a new project, you have the option to set the _description_,
_sector_, and _country_ for your project. You also can opt in to **anonymously**
share the country and sector information with KoboToolbox for the purposes of
improving the platform. You can add or change these details in **Layout &
Settings** pane within the formbuilder or in the **SETTINGS>General** tab.

## Additional settings

Apart from options found in the formbuilder's **Layout & Settings** tab, you can
also change other project-level settings, such as
[sharing](managing_permissions.md),
[connected projects](dynamic_data_attachment.md),
[REST services](rest_services.md) and [media](media.md) and more.

<p class="note">
  You can download an XLSForm with examples from this article
  <a
    download
    class="reference"
    href="./_static/files/form_meta/form_meta.xlsx"
    >here</a
  >.
</p>
