# Form metadata in XLSForm 
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/af653bb67285d52f37e1e9c1518021e00c014b4e/source/metadata_xls.md" class="reference">4 Jan 2026</a>

Metadata questions automatically gather information about the data collection process, such as the date, time, and device used, without requiring input from the respondent. 

Metadata questions are hidden from respondents, and metadata fields cannot be edited in the KoboToolbox data table. This background information supports auditing, helps maintain data integrity, and can be used in data analysis.

<p class="note">
<strong>Note:</strong> This article focuses on adding metadata questions in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about adding metadata questions in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/form_meta.html">Adding form metadata in the Formbuilder</a>.
</p>

## Adding metadata questions in XLSForm

Metadata questions are added to XLSForm in the same way as any other question types:

1. Enter the metadata question `type` in a new row, using the exact name shown [in the table below](https://support.kobotoolbox.org/metadata_xls.html#available-metadata-questions-in-xlsform).
2. Include a question `name`. 
3. Question labels are not required, as they are not displayed in the form.

**survey worksheet**

| type | name       | label        |
|:-----|:-----------|:-------------|
| start | start_time |              |
| end   | end_time   |              |
| survey | 

## Available metadata questions in XLSForm

Available metadata questions in XLSForm include:

| Type       | Description |
|:--------------------|:-------------|
| `start` | Records the exact time and date when a submission is started. |
| `end` | Records the date and time when a submission is finalized. |
| `today` | Records the date of the submission. |
| `deviceid` | Records the unique identification of the device or browser used to collect data. The <code>deviceid</code> is automatically generated and cannot be modified by users.<br><br>**Note:** In KoboCollect, the <code>deviceid</code> is updated whenever the app is reinstalled on a device. In Enketo, the <code>deviceid</code> resets any time a new browser window is used. |
| `username` | In KoboCollect, records the username saved in the <a href="https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings">KoboCollect app settings</a>. If no username is set, it records the one used to sign in to the server.<br>In Enketo, records the account username only if <a href="https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication">authentication is required</a>.<br><br>**Note:** Because the `username` field can be edited in KoboCollect, it may not match the account used to authenticate to the server. To see which account submitted the data, refer to the automatically generated `_submitted_by` field.|
| `phonenumber` | Records the phone number stored in the <a href="https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings">KoboCollect app settings</a>. This metadata question is not supported in Enketo. |
| `email` | Records the email address from the <a href="https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings">KoboCollect app settings</a>. This metadata question is not supported in Enketo. |
| `start-geopoint` | Captures GPS coordinates when the form is first opened. Can be used to warm up the device GPS so that later GPS questions can reach accurate readings more quickly. |
| `background-geopoint` | Captures GPS coordinates when a specific question is answered. The question must be specified in the <code>trigger</code> column of the <code>background-geopoint</code> question. |
| `background-audio` | Records audio in the background while a form is open. To learn more about this feature, see <a href="https://support.kobotoolbox.org/recording-interviews.html">Recording interviews with background audio recording</a>. | 
| `audit` | Captures a detailed log of the interview process, including start time, end time, location, and user actions during the entire data collection process. This metadata question is not supported in Enketo.<br><br>To learn more about using the audit question for audit logs and configuring settings, see <a href="https://docs.getodk.org/form-audit-log/">Form Audit Log (ODK)</a>. |

## Configuring metadata in KoboCollect 

The user’s default email, phone number, and username can be [configured](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings) and modified in the KoboCollect app:
1. Open the KoboCollect app.
2. Tap the **Project icon** in the top right corner of your screen.
3. Tap **Settings**.
4. Scroll down to **User and device identity**, then **Form metadata**. 
5. Enter the username, phone number, and/or email address. You can also view the current device ID.

