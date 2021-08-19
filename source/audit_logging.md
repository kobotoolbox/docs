# Audit Logging Meta Question Type

Audit Logging can be a useful tool to monitor enumerator behavior and discover which questions are taking longer to answer, better understand how the enumerators are navigating a certain form, and see which enumerators are generally taking longer periods of time to submit answers.

<p class="note">This feature requires manually analyzing CSV files.</p>

The audit log meta question is a question type that is only supported by using the [Collect Android app](kobocollect-android.md).

To add an `audit` meta question type to a form and view the finalized data, please follow the steps below:

1. In an XLSForm file, add `audit` in the same fashion as you would any other meta questions. Then upload the form file to your project and deploy the form.

__survey__

| type  | name  | label                  |
| ---   | ---   | ---                    |
| start | start |                        |
| end   | end   |                        |
| audit | audit |                        |
| text  | Q1    | Q1. What is your name? |

2. Collect data using the [Collect Andoid app](kobocollect-android.md) and send the finalized forms back to the server. Collect saves the audit logs for each submission in a CSV file that are saved and uploaded to the server just as an attached photo would be.

3. After the data has been submitted, open your project in the browser and go to __DATA__, then __Downloads__. Select __Media Attachments (ZIP)__ as the export type and then click on __New Export__. Once the download is done pending, click on the file to download it to your computer.

![image](/images/audit_logging/zip_export.png)

4. Once the ZIP file has been extracted and opened, click on the file labeled 'audit.csv' to view the audit logs. It's important to note that the CSV uses [Unix Epoch](https://www.unixtimestamp.com/index.php) time so the logs are recorded in milliseconds.

5. Because timestamps are saved for each individual submission, you will probably need to copy the values into a new spreadsheet to do further analysis across all submissions (e.g. by enumerator or by question). Collating many different CSV files into can be done by [many free tools or by writing a script](https://www.google.com/search?q=merge+many+CSV). To read more detailed information regarding log structure and event types, please visit ODK's great documentation on [Logging Enumerator Behavior](https://docs.getodk.org/form-audit-log/#).

Please feel free post on our [community forum](https://community.kobotoolbox.org/) to share your favorite approach or script to use this feature so others can learn from your example.
