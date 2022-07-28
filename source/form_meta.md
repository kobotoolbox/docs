# Form Settings and Metadata

In the formbuilder, there are a number of optional configurations you can set
for your project. You can access these by clicking on the **Layout & Settings**
button.

![Form meta](/images/form_meta/form_meta.png)

## Form Style

You can change the way the form appears in Enketo Web Forms by changing the
**Form Styles**. Learn more about form styles [here](alternative_enketo.md).

## Form Metadata

Metadata are hidden questions that can help you with your analysis later on.
They are typically captured automatically as data collection progresses. In
detail, here is what they stand for:

| Metadata       | Description                                                                                                          |
| :------------- | :------------------------------------------------------------------------------------------------------------------- |
| Start Time     | Exact start date and time when starting the interview (timestamp)                                                    |
| End Time       | Exact end date and time when finishing the interview                                                                 |
| Today          | Day the interview is conducted                                                                                       |
| Username       | The username of the enumerator if authentication is used for data collection                                         |
| Audit          | Record an audit log while the survey is being completed. Learn more about the Audit Logging [here](audit_logging.md) |
| Device ID      | IMEI (International Mobile Equipment Identity)                                                                       |
| Phone Number\* | The cell phone number                                                                                                |

<p class="note">
Note: The Phone Number is only captured on mobile phones that have a SIM card.
</p>

### Adding Form Metadata in XLSForm

If you are building your form in XLSForm, you can add metadata as follows:

| type        | name        |
| :---------- | :---------- |
| start       | start       |
| end         | end         |
| today       | today       |
| username    | username    |
| audit       | audit       |
| deviceid    | deviceid    |
| phonenumber | phonenumber |
| survey      |

## Background audio

When the background audio setting is turned on, KoboCollect will be recording
the audio of the interview everytime you open the form. Learn more about
background audio recording [here](recording-interviews.md).

## Details

When creating a new project, you have the option to set the description, sector,
and country for your project. You also can opt in to anonymously share the
country and sector information with KoboToolbox for the purposes of using the
data to improve the platform. You can add or change these details from this
section of the **Layout & Settings** pane.

## More settings

Apart from the form settings found under **Layout & Settings** in the
formbuilder, you can also change other settings that have to do with the project
as a whole, such as [sharing settings](managing_permissions.md),
[connected projects](dynamic_data_attachment.md),
[REST services](rest_services.md) and [project media](media.md). You can learn
more about these settings by clicking on the linked articles.

<p class="note">
  Download an XLSForm with examples from this article
  <a
    download
    class="reference"
    href="./_static/files/form_meta/form_meta.xlsx"
    >here</a
  >.
</p>
