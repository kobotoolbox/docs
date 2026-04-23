# Data collection with KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/a42f7ff93a1567cc2ac66a749d2a7d5969cfa45a/source/data-collection-tools.md" class="reference">23 Apr 2026</a>

KoboToolbox supports two primary ways to collect data: **web forms**, which run in a browser, and **KoboCollect**, which is the Android app for mobile data collection. Both methods support offline data collection. 

This article explains the two data collection methods available in KoboToolbox, how to choose between them, and how to prepare before launching data collection.

<p class="note">
To learn more about each data collection method, see <a href="https://support.kobotoolbox.org/data_through_webforms.html">Collecting data using web forms</a> and <a href="https://support.kobotoolbox.org/data_collection_kobocollect.html">Collecting data using KoboCollect</a>.
</p>

## Data collection methods

You can collect data with KoboToolbox in two main ways:
- **Web forms** are browser-based forms used to collect data through a web page. They are well suited for self-administered surveys and browser-based data entry.
- **KoboCollect** is an Android app used to collect data on Android devices. It is well suited for field teams with enumerators using Android phones or tablets.

Both methods support [offline data collection](https://support.kobotoolbox.org/data-collection-tools.html#offline-data-collection).

### Choosing a data collection method

The best data collection method depends on how your team will work in practice, and in some cases teams may use both methods within the same project.

The table below summarizes when each method is generally the better fit:

| Web forms | KoboCollect |
| :--- | :--- |
| **Recommended if:** <br> <ul><li>Respondents will submit data directly through a link</li><li>You want a simple way to open and share a form</li><li>Your team is using a mix of device types</li><li>You want to use browser-based data collection without installing an app</li><li>Your form includes features that are only available in web forms, such as the [grid theme](https://support.kobotoolbox.org/alternative_enketo.html) or [question matrices](https://support.kobotoolbox.org/matrix_response.html)</li></ul> | **Recommended if:**<br><ul><li>Much of your data collection is field-based in offline settings</li><li>Data is being collected by a team of enumerators using Android phones or tablets</li><li>Enumerators prefer an app-based workflow (e.g., to save drafts and send finalized submissions later)</li><li>Your project relies on mobile device features such as [barcode scanning or capturing images and videos](https://support.kobotoolbox.org/photo_audio_video_file.html)</li><li>You want more control over form management and automation, such as sending forms, downloading forms, or deleting uploaded data from devices</li></ul> |

When choosing a method, consider how people will access the form, which devices they will use, how often they will need to work offline, and whether your form includes features that are better supported in one method than the other.

<p class="note">
<strong>Note:</strong>
Some features work differently depending on the collection method. Keep this in mind before starting data collection, and always test your form in the method your team will use.
</p>

### Offline data collection

Both web forms and KoboCollect support **offline data collection.**

- When using **web forms**, KoboToolbox can store the form and responses in the browser’s cache so users can continue entering data without an internet connection.
  - Before going offline, you will need to open the form while connected to the internet and wait for it to fully load and be [cached on the device](https://support.kobotoolbox.org/data_through_webforms.html#offline-data-collection).
  - When the device reconnects, saved submissions will upload automatically.
- When using **KoboCollect**, enumerators can download blank forms while online, complete them offline, save drafts, finalize submissions, and send them later when internet access becomes available. 
  - KoboCollect can also be [configured](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) to send finalized forms automatically when connected or only when the user chooses to upload them.

## Preparing for data collection

Before you can collect data, you must **deploy your form** to make it active and available for submissions. If you make changes to the form later, you will need to redeploy it.

<p class="note">
To learn more about deploying your form for data collection, see <a href="https://support.kobotoolbox.org/deploy_form_new_project.html">Deploying forms for data collection</a>.
</p>

Once your form is deployed, make sure your data collection setup is ready before launching data collection: 
- Decide which data collection method(s) to use
- Confirm who can access the form and whether authentication should be required
- Test the project in a scenario similar to your actual data collection, using the same devices and collection method as your respondents or enumerators

Depending on the collection method you choose, we also recommend the following steps:


| Web forms | KoboCollect |
| :--- | :--- |
| <ul><li>Decide whether the form should [require authentication](https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication)</li><li>If your form requires authentication, ensure that data collectors have the right [permissions](https://support.kobotoolbox.org/managing_permissions.html) to access your data collection form</li><li>Decide which [web form mode](https://support.kobotoolbox.org/data_through_webforms.html#data-collection-modes) to use for data collection</li><li>Share the correct form link with data collectors or respondents</li></ul> | <ul><li>Confirm that data collectors have the right [permissions](https://support.kobotoolbox.org/managing_permissions.html) to access your data collection form</li><li>Ensure each data collector has [installed and set up](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) the KoboCollect app</li><li>Confirm each data collector has [downloaded the form(s)](https://support.kobotoolbox.org/data_collection_kobocollect.html#downloading-forms) before starting fieldwork</li></ul> |


<p class="note">
<strong>Note:</strong>
Deployed projects are set to <a href="https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication">require authentication</a> by default, which means users must sign in to access a web form or submit data. To allow <strong>anyone with the form link</strong> to submit data, turn off the authentication requirement for the form. If you keep authentication enabled, <a href="https://support.kobotoolbox.org/managing_permissions.html">share the project</a> with specific KoboToolbox users and give them <strong>Add submissions</strong> permission.
</p>

