# Manually Uploading Submissions
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/488d162653bdaf54b3e1dfe63cd24f8c0c7d133b/source/manual_upload.md" class="reference">24 May 2022</a>

<p class="note">Please note this is still an experimental feature and it does
not prevent you from creating duplicate submissions.</p>

In certain situations, you might not be able to use the standard uploading
option after collecting data with **KoboCollect** or **Enketo Web Forms**. This
may be as a result of issues with your mobile device being partially broken
(e.g. screen is shattered), or due to being in a remote location without
internet access. You may want to download your submissions from the data
collection device to your local computer and then upload them to the server when
you have regained internet connectivity.

## Exporting data from Web Forms

1. In your offline-enabled **Web Form**, open the "Side Panel" by clicking on
   the bracket on the left.

![Side Panel](/images/manual_upload/Side_Panel.png)

2. Click on the **Export** button and ZIP file will be saved to your computer.
   If not, click the **Export** button again. For some browsers this may not
   work and you will need to click the "alternative download - online" link,
   which will require an Internet connection.

![Export](/images/manual_upload/Export.png)

3. Now follow the [instructions outlined below](#importing-a-data-zip-file) for
   importing your submissions.

## Exporting data from KoboCollect

1. Connect the device to your computer through a USB cable.

2. Open the device's internal storage on your computer. (For **Windows**, the
   drivers will install automatically and the device can be opened on **My
   Computer**. On **MacOS** you will need
   [Android File Transfer](https://www.android.com/intl/en_us/filetransfer/)
   from Google to access the device's files.)

3. On your device, navigate to the **KoboCollect** folder (this can be found on
   the path below):

    `Phone\Android\data\org.koboc.collect.android\files\projects`

    You can learn more about the device storage path
    [here](transferring_forms.md).

4. Copy the "instances" folder and paste it somewhere on your computer.

5. If you have more than one device, repeat the above steps and rename each of
   the "instances" folders with a unique name or number.

6. Create a ZIP file of the folder.

7. Now follow the [instructions outlined below](#importing-a-data-zip-file) for
   importing your submissions.

## Importing a data ZIP file

1. Login to your KoboToolbox account, then visit:
   `https://kc-eu.kobotoolbox.org/your_username/bulk-submission-form` OR
   `https://kc.kobotoolbox.org/your_username/bulk-submission-form` (depending on
   where you signed up), and replace `your_username` with **your own username**.

2. Select and upload the ZIP file. All records will be uploaded to the server,
   assuming that they correspond to an existing form.

Once all instances have been uploaded, you will see a confirmation message for
each record. If you see a timeout message, you can try uploading multiple
smaller ZIP files with fewer records. Uploading the same records twice is not an
issue, since duplicate records will be rejected.
