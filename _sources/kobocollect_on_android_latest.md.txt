# Getting started with KoboCollect
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/ff350995fdbf546a9f306c1128351d40aaf9a258/source/kobocollect_on_android_latest.md" class="reference">30 Dec 2025</a>


<iframe src="https://www.youtube.com/embed/qC2Bz8jZkIM?si=xSyTOxOMR6nE8tum" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect is a free, open-source KoboToolbox app designed for data collection on Android mobile devices. Its offline capabilities and compatibility with most Android devices make it ideal for fieldwork. 

Before using KoboCollect, you must [set up a KoboToolbox account](https://support.kobotoolbox.org/creating_account.html) on the KoboToolbox website and [deploy data collection forms](https://support.kobotoolbox.org/quick_start.html). 

<p class="note">
    This article covers how to connect to KoboCollect for data collection. To learn more about configuring KoboCollect settings and collecting data with the app, see <a href="https://support.kobotoolbox.org/kobocollect_settings.html">Customizing KoboCollect settings</a> and <a href="https://support.kobotoolbox.org/data_collection_kobocollect.html">Data collection using KoboCollect</a>.
</p>

## Installing the KoboCollect app

The KoboCollect app can be downloaded from the [Google Play Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android) for Android devices running version 5 or above. 

<p class="note">
    <strong>Note:</strong> We recommend using the latest version of the app (v2025.3.3), as it includes features and bug fixes not available in older versions.
</p>

## Setting up the KoboCollect app

To collect data with KoboCollect, you must configure the KoboCollect app on your mobile device to connect to the KoboToolbox server. This enables you to download deployed forms from KoboToolbox and send collected data back to the server.

To connect KoboCollect to the KoboToolbox server, you will need your **KoboCollect URL**, your **username**, and your **password**. After the initial manual setup, you can [generate a QR code](https://support.kobotoolbox.org/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) to configure other devices. 

<p class="note">
    <strong>Note:</strong> In the KoboCollect app, user accounts are called <strong>Projects</strong>.
</p>

### Setting up KoboCollect manually 
To manually set up KoboCollect, you will need to identify your **KoboCollect URL**. This URL is specific to KoboCollect and differs from the URL used to access your KoboToolbox account. 

Your KoboCollect URL depends on your account’s server:

| **KoboToolbox Server**    | **KoboCollect URL**                     |
| :----------------- | :--------------------------------------------- |
| Global KoboToolbox Server               | https://kc.kobotoolbox.org/ |
| European Union KoboToolbox Server      | https://kc-eu.kobotoolbox.org/ |
| Private Server           | Unique to each organization            |

You can also find the KoboCollect URL on the KoboToolbox platform. Go to the **FORM** tab of your project and select **Android application** from the **Collect data** drop-down menu. The KoboCollect URL will be listed in step 3.

![Select Android app in browser](images/kobocollect_on_android_latest/select_android_app_in_browser.png)

Once you have identified your KoboCollect URL, follow these steps to set up the server connection:

1. Open the KoboCollect app.
2. Select **Manually enter project details**.
3. Enter the **KoboCollect URL**, your **username**, and **password**.
4. Tap **Add**. 
5. When configuration is complete, the main menu will be displayed.

### Setting up KoboCollect with a QR code

Using a QR code efficiently configures KoboCollect on multiple devices with the **same server settings** (KoboCollect URL, username, password, and <a href="https://support.kobotoolbox.org/kobocollect_settings.html">project configuration settings</a>). This can be useful to avoid repeating manual steps or to configure enumerator devices without sharing account passwords.

<p class="note">
    <strong>Note:</strong> In order to use the QR code method, you must first manually configure one device and then copy the generated QR code to the other devices. 
</p>

To access your QR code:

1. Go to the **Projects** menu and select the project you want to copy.
2. Tap **Settings**.
3. Select **Project Management**.
4. Tap **Reconfigure with QR Code**.
5. Choose **QR Code**. Your QR code will appear on the screen.
6. **Take a screenshot** of the QR code to share it for setting up other devices. You can also return to this menu anytime to access the QR code again.
   
To configure other devices using the QR code:

1. Open **KoboCollect** on the device you want to set up.
2. Tap **Configure with QR Code**.
3. Scan a QR code with the device's camera, or tap the <i class="k-icon-more"></i> **three dots** in the top right corner and select **Import QR code** to use a screenshot saved to your device.

If the setup is successful, the app will be configured automatically.

<p class="note">
    <strong>Note:</strong> The QR code contains your account credentials, including your password. Anyone who scans it will have the same access permissions as the account it was generated from. If you only want someone to collect data (e.g., an enumerator), <strong>make sure the account used to generate the QR code does not have permissions to view, edit, or delete data.</strong> To keep your data safe, avoid sharing QR codes from accounts with full access.
</p>

### Setting up multiple projects in KoboCollect

Users can connect multiple KoboToolbox accounts and easily switch between different projects within the same KoboCollect app, regardless of whether they are on the same or different servers.

To set up additional projects in KoboCollect:

1. Tap the **Project icon** located in the top right corner.
2. In the **Projects** menu, tap **Add project**.
3. Set up a new project using the manual approach or by scanning a QR code.
4. When configuration is complete, the main menu will be displayed.
5. Tap the **Project icon** to open the menu. Both projects should now be visible.

Additional projects can be added by repeating the same process. The active project will be listed first in the **Projects** menu. To switch to a different project, simply tap its icon. 

<p class="note">
    To learn more about changing how projects are displayed for easier recognition and switching, see <a href="https://support.kobotoolbox.org/kobocollect_settings.html#project-display-settings">Project display settings</a>.
</p>

### Setting up a project in KoboCollect without authentication

It is also possible to access projects in KoboCollect without a password. This is useful for projects with many enumerators, as it avoids the need to create individual accounts or share credentials.

<p class="note">
    <strong>Note:</strong> This approach requires enabling “Allow submissions to this form without a username and password” for your forms. To learn more about project-level sharing settings, see <a href="https://support.kobotoolbox.org/project_sharing_settings.html">Sharing projects with project-level settings</a>.
</p>

To connect to KoboCollect without authentication:
1. Enable “Allow submissions to this form without a username and password” for your forms.
2. [Optional] Create a dedicated KoboToolbox account for data collectors and [share your forms](https://support.kobotoolbox.org/managing_permissions.html) with this account. 
3. Connect to KoboCollect using the following credentials:
    - **URL**: KoboCollect URL followed by the account username (`https://[kobocollect_url]/[username]`)
    - **Username**: (Leave blank)
    - **Password**: (Leave blank)

This approach allows users to download and submit data to any forms shared with `username` that do not [require authentication](https://support.kobotoolbox.org/project_sharing_settings.html).

To differentiate enumerators and track submissions, you can ask enumerators to enter a custom username, phone number, and email address in the [User and device identity settings](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings).

<p class="note">
    <strong>Note:</strong> This approach can be useful when your account uses <a href="https://support.kobotoolbox.org/two_factor_authentication.html">two-factor authentication</a>, as you will not be able to download forms or submit data using the normal approach.
</p>
