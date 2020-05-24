# Audit Logging Meta Question Type
## Using the audit meta question type to log enumerator behavior

Audit Logging can be a useful tool to monitor enumerator behavior and discover which questions are taking longer to answer, better understand how the enumerators are navigating a certain form, and see which enumerators are generally taking quicker or longer periods of time to submit answers. This feature requires manually analyzing CSV files and is only meant for advanced users. This feature is also not supported in the Form Builder and requires you to use an [XLSForm](https://support.kobotoolbox.org/en/articles/592430-editing-forms-in-excel-using-xlsform). 

The audit log meta question is a question type that is only supported by using the [KoBoCollect](data_through_webforms.html) app. 

To add an audit meta question type to a form and view the finalized data, please follow the steps below: 

1. In an XLSForm file, add 'audit' in the same fashion as you would any other meta questions. Then upload the form file to your project and deploy the form. 

    ![image](/images/audit_logging/xls.png)  

2. Collect data using the [KoBoCollect app](data_through_webforms.html) and send the finalized forms back to the server. Collect saves the audit logs for each submission in a CSV file that are saved and uploaded to the server just as an attached photo would be.  

3. After the data has been submitted, open your project in the browser and go to _DATA_, then _Downloads_. Select Media Attachments (ZIP) as the export type and then click on New Export. Once the download is done pending, click on the file to download it to your computer. 

    ![image](/images/audit_logging/zip_export.png)  

4. Once the ZIP file has been extracted and opened, click on the file labeled 'audit.csv' to view the audit logs. It's important to note that the CSV uses [Unix Epoch](https://www.unixtimestamp.com/index.php) time so the logs are recorded in milliseconds.  

5. Because timestamps are saved for each individual submission, you will probably need to copy the values into a new spreadsheet to do further analysis across all submissions (e.g. by enumerator or by question). Collating many different CSV files into can be done by [many free tools or by writing a script](https://www.google.com/search?q=merge+many+CSV). To read more detailed information regarding log structure and event types, please visit ODK's great documentation on [Logging Enumerator Behavior](https://docs.getodk.org/form-audit-log/#).

Please feel free post on our [community forum](https://community.kobotoolbox.org/) to share your favorite approach or script to use this new feature so others can learn from your example.  
