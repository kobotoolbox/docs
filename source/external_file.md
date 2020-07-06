# Select One or Many From External File Question Type

In some cases, it may be desirable to host a list of choice options in an external file, rather than directly in the project XLSForm. For example, a long list of choices (e.g. hundreds or thousands) could slow down the loading and navigation of the form, or adding new choice options after data collection has begun could sometimes be troublesome. 

This article provides a detailed example and method for creating a select one or select many question type with the choice list in a separate external file. 

_Please note: 
* At the moment, this feature is only available using XLSForms and the data can only be entered through Enketo and is not supported by ODK or KoBoCollect. 

_* There is an [outstanding bug](https://github.com/kobotoolbox/kpi/issues/2275) that causes an error when trying to view or download the collected data. For now, you can go around this by using the legacy version of KoBo ([kc.kobotoolbox.org](https://kf.kobotoolbox.org/) or [kc.humanitarianresponse.info](https://kobo.humanitarianresponse.info/)).

**Step 1:**
In the XLSForm, the type should be either `select_one_from_file + (file name with a CSV extension)` or `select_multiple_from_file + (file name with a CSV extension)` as shown in the figure below:

   ![image](/images/external_file/select_file.png) 

_Please note: The fruits.csv is the file name containing the choices for the question “What is your favorite fruit?”._

**Step 2:**
In the choices sheet of the XLSForm, type the name of the variable (i.e. fruits) under list_name and leave the name and label values as just name and label as shown in the figure below:

   ![image](/images/external_file/list_name.png) 
   
**Step 3:**
Create a new csv file and structure it the same as the choices tab in the XLSForm and label the tab the same as the variable you used in the XLSForm. Under the list_name column, type the variable name for each row. Under the name and label columns, create your custom choice options as shown below:

   ![image](/images/external_file/custom_choice.png) 

**Step 4:**
Upload and deploy the XLSForm in KoBoToolbox. 

**Step 5:**
Upload the external csv file the same way you would add a media file to the form: Click the + Add Document button in the Media tab of the project SETTINGS page. After the file is uploaded and shown above, return to the main SETTINGS page and click the Save Changes button. 

   ![image](/images/external_file/upload.jpg) 

_Please note: You are only able to upload the CSV file after you have deployed the form._ 



