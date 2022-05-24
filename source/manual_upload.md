# Manually Uploading Submissions
 
*[Warning: Please note this is still an experimental feature and it does not prevent you from creating duplicate submissions.]*

In certain situations, you might not be able to use the standard uploading option after collecting data with **KoboCollect** or **Enketo Web Forms**. This may be as a result of issues with your mobile device being partially broken (e.g. screen is shattered), or due to being in a remote location without internet access. You may want to download your submissions from the data collection device to your local computer and then upload them to the server when you have regained internet connectivity.

## Exporting data from Web Forms

1. In your offline-enabled **Web Form**, open the “Side Panel” by clicking on the bracket on the left.

![Side Panel](/images/manual_upload/Side_Panel.png)

2. Click on the **Export** button. A downloadable file has now been prepared and will be saved to your computer immediately. If not, click the **Export** button again. For some browsers this may not work and you will need to click the “alternative download - online” link, which will require an Internet connection.

![Export](/images/manual_upload/Export.png)

3. Now follow the instructions outlined below in **Importing a data ZIP file to KoboToolbox**.

## Exporting data from KoboCollect

1. Connect the device to your computer through a USB cable.

2. Open the device’s internal storage on your computer. (For **Windows**, the drivers will install automatically and the device can be opened on **My Computer**. On **iOS** you will need **[Android File Transfer](https://www.android.com/intl/en_us/filetransfer/)** from Google to access the device’s files.)

3. On your device, open the **KoboCollect** folder (this can be found on the path below):

   `Phone\Android\data\org.koboc.collect.android\files\projects`

   You should be able to learn more about the *device storage path* through our support article **[Transferring forms and data manually from one android device to another](https://support.kobotoolbox.org/transferring_forms.html)**.

4. Copy the ‘instances’ folder and paste it somewhere on your computer.

5. If you have more than one device, repeat the above steps and rename each of the ‘instances’ folders with a unique name or number.

6. Create a ZIP file of the folder.

7. Now follow the instructions outlined below in **Importing a data ZIP file to KoboToolbox**.

## Importing a data ZIP file to KoboToolbox

1. Login to your KoboToolbox account, then visit:
`https://kc.humanitarianresponse.info/your_username/bulk-submission-form` OR `https://kc.kobotoolbox.org/your_username/bulk-submission-form` (depending on where you signed up), and replace `your_username` with **your own username**.

2. Select and upload the ZIP file created/downloaded earlier. All records will be parsed and added to the database, assuming that they correspond to an existing form.

Once all instances have been parsed and added to the database you will see a confirmation message for each record. If you see a timeout message, it only means that a large number of records were added; it doesn’t mean that the import was unsuccessful. In this case, we suggest uploading multiple smaller ZIP files with fewer records. Uploading the same records twice is not an issue, since duplicate records will be rejected.
