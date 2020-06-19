# Manually Uploading Submissions

[Warning: This is still an experimental feature, and it does not prevent you from creating duplicate submissions.]

In some situations, you might not be able to use the standard uploading option after collecting data with KoBoCollect or Enketo Web Forms. For example, your mobile device might be partially broken (e.g. screen is shattered), or your devices are in a remote location without Internet access. It is possible to download the submissions to your local computer first and then uploading them to the server. In remote locations, this might be a good option because you may have access to a computer to download the files but need to physically travel to a different location where you can access the Internet.

## Exporting data from Web Forms

1. In your offline-enabled Web Form open the "drawer" by clicking on the bracket on the left.

    ![image](/images/manual_upload/export_data.png)

2. Click on the Export button. A downloadable file has now been prepared and will be saved to your computer immediately, otherwise click the Export button again. For some browsers this may not work and you will need to click the "alternative download - online" link, which will require an Internet connection.

3. Follow the import steps shown below.

## Exporting data from KoBoCollect

1. Connect the device to your computer

2. Open the device's internal storage on your computer. (For Windows the drivers will install automatically and the device can be opened on My Computer. On iOS you will need [Android File Transfer](https://www.android.com/intl/en_us/filetransfer) from Google to access the device's files.

3. On your device open the 'odk' folder.

4. Copy the 'instances' folder and paste it somewhere on your computer.

5. If you have more than one device repeat the above steps and rename each of the 'instances' folders to a unique name or number.

6. Create a ZIP file of the folder.

7. Follow the import steps shown below.

## Importing a data ZIP file to KoBoToolbox

1. Login to your KoBoToolbox account, then visit:

    https://kc.humanitarianresponse.info/your_username/bulk-submission-form *OR*

    https://kc.kobotoolbox.org/your_username/bulk-submission-form

    (depending on where you signed up), and replace 'your_username' with your own username.

2. Select and upload the ZIP file created/downloaded earlier. All records will be parsed and added to the database, assuming that they correspond to an existing form.

    Once all instances have been parsed and added to the database you will see a confirmation message for each record. In the event you are seeing a timeout message, it only means that a large number of records were added; it doesn't mean that the import was unsuccessful. It is advisable in this case to upload multiple smaller ZIP files with fewer records. Uploading the same records twice is not an issue since duplicate records will be rejected.
