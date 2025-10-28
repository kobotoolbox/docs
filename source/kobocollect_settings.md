# Customizing KoboCollect settings
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c8c238efa59b04f403f13c150b018e1807c66d5c/source/kobocollect_settings.md" class="reference">28 Oct 2025</a>

<a href="es/kobocollect_settings.html">Leer en español</a> | <a href="fr/kobocollect_settings.html">Lire en français</a> | <a href="ar/kobocollect_settings.html">اقرأ باللغة العربية</a>

<iframe src="https://www.youtube.com/embed/Qeky3aomiWI?si=M1l_jorFQEDacX2A" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect is a free, open-source KoboToolbox app designed for data collection on Android mobile devices. Before you get started, [install and configure](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) the KoboCollect app. Once installed and configured, you can customize the app based on your project or user needs. Project settings allow you to:

- Adjust the **user interface** (e.g., language, font size, theme)
- Configure **map settings** for location-based questions
- Manage how forms are handled (e.g., auto-send, finalize, editing rules)
- Set the **user and device** identity for tracking submissions
- Protect access to the app and its settings with **passwords or admin controls**
  
To access the settings menu:

1. Tap the **Project icon** in the top right corner of your screen.
2. Tap **Settings**.

<p class="note">
  <strong>Note:</strong> Users do not need an internet connection to access or change project settings in KoboCollect.
</p>

## Project display settings
In the KoboCollect app, you can [connect to multiple KoboToolbox accounts](https://support.kobotoolbox.org/kobocollect_on_android_latest.html#setting-up-multiple-projects-in-kobocollect). User accounts are called **Projects** in KoboCollect. 

To customize how each project is displayed for easier recognition and switching, you can edit the **project display** settings. These changes only affect how the project appears in the device’s interface and do not affect the data or other devices.

| **Setting**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Project name              | Give a distinct name to your KoboCollect project.                                  |
| Project icon      | Change the letter that appears in the top right circle.                                  |
| Project color           | Change the color of the top right circle.            |

## User interface settings

User interface settings allow you to adjust the app's appearance, language, and text size for better readability.

| **Setting**    | **Description** |
| :----------------- | :--------------------------------------------- |
| Theme  | Choose between light, dark, or system default appearance for the app. |
| Language      | Set the language for the app interface display. By default, KoboCollect matches the device language.|
| Text font size           | Adjust the text size for better readability.            |
| Navigation           | Customize how you move through forms. Choose between horizontal swipes, forward/back buttons, or a combined layout. |


<p class="note">
    <strong>Note:</strong> Changing the language only sets the language for the app user interface and not for the form. For forms with <a href="https://support.kobotoolbox.org/language_dashboard.html">multiple languages</a>, the form language is set during data entry.
</p>

## Maps settings

Map settings configure the display and behavior of maps within the app for location-based questions.

| **Setting**        | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Source   &emsp;&emsp;&emsp;&emsp;            | Define your map source. Choose between Google, OpenStreetMap, USGS or Carto. |
| Map style      | Define your map style if using Google Maps, USGS, or Carto. |
| Layer           | Select an offline layer for the maps. You can add options by selecting an MBTiles file from your device. |

## Form management settings

Form management settings control how forms are handled within the app, including form version updates, submissions, and data entry behaviors. 

| **Setting** | **Description**                  |
| :----------------- | :--------------------------------------------- |
| Blank form update mode &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Define if you want new versions of the forms to be updated automatically or manually. Options include: <ul><li><strong>Manual</strong>: The default mode, in which enumerators manually manage updating forms.</li><li><strong>Previously downloaded forms only</strong>: Enumerators receive a notification when one or more forms previously downloaded to the device have an update available.</li><li><strong>Exactly match server</strong>: All forms shared with the account are automatically downloaded and updated based on changes to the server.</li></ul> |
| Automatic update frequency      | Specifies how frequently KoboCollect should check for updates to forms on the server when using **Previously downloaded forms only** or **Exactly match server**. |
| Automatic download | When **Previously downloaded forms only** is selected, you can choose whether forms are updated automatically. Otherwise, users will only be notified of available updates.<br><br>This setting is automatically enabled when **Exactly matching form version** is selected.  |
| Hide old form versions           | If there are multiple versions of the same form, only the most recently downloaded will be displayed when starting a new form. |
| Auto send           | When enabled, forms are sent to the server immediately when they are finalized, if the device can connect to the Internet. If an Internet connection is not available at the time of finalization, your finalized forms will be queued to send as soon as connectivity is established. You can specify whether to send over WiFi, cellular data, or both. |
| Delete after send         | Delete finalized forms and media from the device after sending them successfully to the server. |
| Constraint processing | When your forms include constraints (validation criteria), choose between validating responses when moving to the next page or at the end of the form. |
| High res video        | Enable or disable high-resolution video recordings when taking videos through the app. |
| Image size      | Define the preferred image size, from very small to large. This can help conserve storage space on the server. |
| Show guidance for questions         | Define how [guidance hints](https://support.kobotoolbox.org/question_options.html?highlight=guidance+hint#guidance-hint-optional) should be displayed within your form. |
| Use external app for audio recording        | By default, an internal recorder is used for audio recording. Enable this setting to use an external audio application instead. |
| Finalize forms on import            | When enabled, forms that are brought into KoboCollect from outside the app (e.g. copied from device storage or SD card) are automatically marked as <strong>Finalized</strong>, so they are ready to send without requiring manual finalization. |


<p class="note">
    <strong>Note:</strong> Configuring projects for <strong>automatic form updates</strong> is recommended in projects with frequent form edits or <a href="https://support.kobotoolbox.org/dynamic_data_attachment.html">dynamic data attachments</a>. This removes the need to manually download form updates. However, more frequent automatic updates will drain your device’s battery more quickly.
</p>

## User and device identity settings

User and device identity settings allow you to set device metadata for tracking submissions.

| **Setting**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Form metadata  &emsp;&emsp;             | Enter a <strong>username</strong>, <strong>phone number</strong>, and <strong>email address</strong>, and view <strong>device id</strong> (defined automatically) to provide additional details on who submitted the records to the server. These details can help validate the quality of the data collected by the team. |
| Collect anonymous usage data      | Allow the KoboToolbox team to collect anonymous usage data to help us prioritize fixes and features. |

## Set admin password

Set an admin password in the KoboCollect app, limiting access to the **Protected** settings menu to only team members with the admin password. This can help prevent data collectors from modifying settings in the field.

To remove the admin password, click **Set admin password**, leave the field blank, and click **OK**. 

## Project management

Project management settings provide tools to manage and reset project-related settings on your device, including reconfiguring settings, resetting specific data, or deleting all project data.

| **Setting**&emsp;&emsp;&emsp;    | **Description**                                |
| :----------------- | :--------------------------------------------- |
|Reconfigure with QR code &emsp;&emsp; | Reconfigure your KoboCollect settings by scanning a QR code from another project. Note that this approach will replace the current project with the new one. This is also where you can find the QR code to [set up another device](https://support.kobotoolbox.org/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) with the same settings. |
| Reset | Reset specific settings, such as clearing saved forms, cached data, or map layers, without affecting other parts of the app. |
| Delete | Delete all data related to the project from the device, including blank forms, submitted data, and settings, which can be helpful when retiring a device or preparing it for a new user. |

<p class="note"> 
    <strong>Note:</strong> Use these options with caution, especially when deleting data, as some actions cannot be undone. Deleting data from the device does not affect the overall KoboToolbox project and does not delete data from the server.
</p>

## Access control

This menu lets you hide or restrict parts of the app interface, helping you customize the app based on the user’s role (e.g., enumerator vs. supervisor). This helps simplify the app and prevents unauthorized changes.

| **Setting**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Main Menu Settings | Hide or show main menu options (e.g., **Download form** or **Delete form**). |
| User Settings | Hide or show general settings (e.g., changing server or user identity). |
| Form Entry Settings | Hide or show form entry settings (e.g., allowing backward navigation, editing saved forms). |

Use the checkboxes to enable or disable specific buttons and settings. Once set up, adding an [admin password](#set-admin-password) can prevent unauthorized changes.

