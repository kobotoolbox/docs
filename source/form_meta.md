# Form Settings and Metadata
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/form_meta.md" class="reference">31 Oct 2025</a>


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
| Start Time       | Date and time when opening the form (timestamp)                                                                                                            |
| End Time         | Date and time when finishing the form ("Submit" button pressed)                                                                                            |
| Today            | The date of the form's submission                                                                                                                          |
| Username         | The username of the enumerator if [authentication is used](managing_permissions.md#requiring-passwords-for-accessing-enketo-web-forms) for data collection |
| Audit            | Record an audit log while the form is being completed. Learn more about audit logging [here](audit_logging.md)                                             |
| Background Audio | Record audio in the background                                                                                             |
| Device ID        | IMEI (International Mobile Equipment Identity)                                                                                                             |
| Phone Number\*   | The cellphone number of the data collection device                                                                                                         |

<p class="note">
  The Phone Number meta question is only captured on mobile devices that have a
  SIM card.
</p>

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
