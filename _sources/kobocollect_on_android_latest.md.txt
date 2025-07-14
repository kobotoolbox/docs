# Data Collection on KoboCollect App (Latest Version)
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/1c72c9d2c69496381bb948bb554ab64f63df0999/source/kobocollect_on_android_latest.md" class="reference">7 Jul 2025</a>

<p class='note'>The latest version of the KoboCollect App refers to v2021.2.4 and above.</p>

**KoboCollect** is an open-source Android app for collecting survey data. It’s
one of two ways that you can collect data through **KoboToolbox** (the other way
is through [web forms - Enketo](data_through_webforms.md)). It’s free and the
latest version of the app can be accessed in the
[Google Play Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android).

## Setting Up the Server Connection

The first step after installing **KoboCollect** on your device is to set up the
server **URL**, **Username**, and **Password**, which connects your
**KoboCollect** app to the **KoboToolbox** server. This allows you to download
deployed forms from **KoboToolbox** to your mobile device and also send data
collected through the app back to the server.

The server in **KoboCollect** can be configured in two different ways:
_manually_ or through a _QR code_.

### Setting up the server connection _manually_:

-   Open **KoboCollect**.
-   Select **Manually enter project details**.

![Collect Data Anywhere](/images/kobocollect_on_android_latest/collect_data_anywhere.jpg)

-   You will now be asked to input the **URL**, **Username**, and **Password**,
    and then select **Add**. For the URL, you must select from the
    [two KoboToolbox servers](creating_account.md). If you created your user account on
    the Global Server, the URL is `https://kc.kobotoolbox.org`. If your
    user account is on the European Union Server, the URL is
    `https://kc-eu.kobotoolbox.org`.

![Server Settings](/images/kobocollect_on_android_latest/server_settings.png)

<p class='note'>Despite setting up the server settings correctly, users may
have trouble connecting <strong>KoboCollect</strong> to the server. This could
be an issue with the device’s incorrect date and time settings. To learn more
about troubleshooting <strong>KoboCollect</strong>, please read our support
article <a href="troubleshooting_kobocollect.html"
class="reference">Troubleshooting KoboCollect Android Application</a>.</p>

-   After setting up the server, you should now see the following home screen.

![Home Page Comparison](/images/kobocollect_on_android_latest/home_page_comparison.png)

You can use **KoboCollect** to _get blank forms to your device_, _collect data
(fill blank forms)_, _store it in your device_, _edit the filled in forms (edit
saved forms)_, _submit saved forms_, and _delete filled in forms/blank forms_.

### Setting up multiple server connections _manually_

<p class='note'>This feature is only available with the latest version of the app and is relevant if you have multiple
<strong>KoboToolbox</strong> user accounts.</p>

Some users have multiple **KoboToolbox** accounts, either on the same server or
a different server. With the latest version, users can manage all their accounts
in the same app and use them in parallel by switching from one account to
another as needed. Follow the steps outlined below to setup multiple server
connections:

-   After setting up your account in the app (see instructions above), open
    **KoboCollect**.
-   Select the icon (circled in K) that is located at the top right of your
    screen.
-   You should see a dialogue box like the one shown below.

![Project Settings Modal 1](/images/kobocollect_on_android_latest/project_settings_modal_1.jpg)

-   Select **Add project**.
-   Fill in the **URL**, **Username**, and **Password** and then select **Add**.

![Server Settings](/images/kobocollect_on_android_latest/server_settings.png)

-   You should now see the home screen. Once again, select the icon (circled in
    K) at the top right of your screen to ensure your connection was successful.
-   After setting up an additional server, you should see a dialogue box like
    the one shown below.

![Project Settings Modal 2](/images/kobocollect_on_android_latest/project_settings_modal_2.jpg)

Here, you will see two different accounts setup in the app. You can add more
accounts as needed. The account listed first is the active one and you can only
see forms for the active account. You can easily switch to your other accounts,
making them active, by simply selecting them.

### Setting up the server connection with a _QR code_

Oftentimes, users in large projects will need to set up a large number of
devices under the same server settings (**URL**, **Username**, and **Password**,
etc.). Setting up all the devices manually would be time-consuming and prone to
error. To save time, you can set up one device manually and then copy the
settings through a QR code generated from the first device.

<p class='note'>To set up a device with a QR Code, you will require at least
one app that has been set up manually.</p>

-   Open **KoboCollect** and choose the project that has been set up.
-   Select the circle K icon that is located at the top right of your screen.
-   Select **Settings**.

![Project Settings Modal 1](/images/kobocollect_on_android_latest/project_settings_modal_1.jpg)

-   Then select **Project Management**.

![Project Settings](/images/kobocollect_on_android_latest/project_settings_list.jpg)

-   Select **Reconfigure with QR code**.
-   Choose **QR Code** at the top. A QR code will be displayed that contains all
    of your **KoboCollect** settings, including the _server URL_, _Username_,
    and _Password_.

![QR Code](/images/kobocollect_on_android_latest/qr_code.jpg)

-   Open **KoboCollect** on another device that you want to set up.
-   Select **Configure with QR code**.
-   Scan the QR code. If successful, you should hear a beep and the app will be
    automatically configured. Repeat for all other devices you want set up.

<p class='note'>You can also copy the QR code and share it by email, Whatsapp,
etc., to set up other devices but be aware that the QR code contains the
password to your account, allowing others to sign into your account. <strong>It
is not recommended to share the QR code through electronic means if the same
account has permissions to view, edit, or delete data.</strong></p>

## Setting Up Blank Forms in KoboCollect

Once you have configured the **URL**, **Username**, and **Password** in the app
correctly, you can send blank forms to your device from the **KoboToolbox**
server.

-   Open **KoboCollect**.
-   Make sure that you have at least one project set up in your **KoboToolbox**
    user account and that your device is connected to the internet.
-   Select **Get Blank Form** from the home menu.

![Get Blank Form Button](/images/kobocollect_on_android_latest/get_blank_form_button.png)

-   A list of all your deployed survey forms should appear. Press **Select All**
    to have all the survey forms sent to the app or select the ones you wish to
    have by selecting them manually. Then click **Get Selected**.

![Get Blank Form List](/images/kobocollect_on_android_latest/get_blank_form_list.jpg)

<p class='note'>Users will need an internet connection while sending blank
forms to <strong>KoboCollect</strong>.</p>

## Collecting Data in KoboCollect

Once you have blank form(s) in the app, you will no longer require an internet
connection to collect data. The blank forms and the filled in forms will stay on
the device until you delete them from the app or submit them to the server.

-   Open **KoboCollect**.
-   Select **Fill Blank** Form from the home menu.
-   Select the survey form that you want to use to start collecting data.
-   Go through all the questions _by swiping your finger from right to left or
    by selecting the **NEXT** key after answering the questions_.
-   At the end of the survey, select **Save Form and Exit**.

![Finalise Form](/images/kobocollect_on_android_latest/finalise_form.png)

<p class='note'>Make sure the form is marked as "<strong>finalized</strong>".
If this is unchecked but you still select <strong>Save Form and Exit</strong>,
the filled in form goes to <strong>Edit Saved Form</strong> instead of going to
<strong>Send Finalized Form</strong>. If this happens, go back to <strong>Edit
Saved Form</strong>, open the form, and without needing to make any edits, you
can select <strong>Go To End</strong>. Make sure the form is marked as
"<strong>finalized</strong>" and then select <strong>Save Form and
Exit</strong>.<br/>If an interviewer believes that a form has not been
completed, for example, if the head of the household wasn’t there or children
weren’t there but are needed for the data collection, they can rename the form
in order to come back to it more easily. You can change the name of a saved
form to something easy to keep track of, such as "Incomplete" or "Incomplete:
(name of respondent)" under <strong>Name this form</strong>.</p>

## Editing Data in KoboCollect

Once you have pressed **Save Form and Exit**, the saved form is automatically
stored under **Edit Saved Form**.

-   Open **KoboCollect**.
-   Select **Edit Saved Form** from the home menu.
-   You will see a list of **Saved Forms**. Choose the one that needs edits or
    updates.
-   Make changes as needed, and then select **Save Form and Exit**.
-   Repeat the process multiple times if multiple forms need edits or updates.

<p class='note'>Users do not need an internet connection while editing a saved
form in <strong>KoboCollect</strong>.</p>

## Uploading Finalized Data to the Server

Once you have collected your data, and made any necessary edits, you can upload
the forms to the **KoboToolbox** server.

-   Open **KoboCollect**.
-   Make sure the device is securely connected to the internet.
-   Select **Send Finalized Form** from the home screen.
-   A list of all the collected forms should appear.
-   Press **Select All** (or select the ones you wish to upload) and then press
    **Send Selected**.
-   To ensure the forms were uploaded successfully, select **View Sent Form**.
    You should now be able to view all the submitted forms.

<p class='note'>Users will need an internet connection while submitting data
from <strong>KoboCollect</strong> to the server.</p>

## Deleting Saved Forms in KoboCollect

Once you have completed data collection for your survey project and all the
filled in forms have been uploaded to the server, it is recommended to delete
the forms from the **KoboCollect** app. Keeping them in the app can confuse
interviewers while collecting data for a different project. Follow the steps
outlined below to delete **Saved Forms** and **Blank Forms** from your app.

-   Open **KoboCollect**.
-   Select **Delete Saved Form** from the home screen.
-   Users should now see two tabs. The default is **Saved Forms**. These are the
    forms that were filled in while collecting data. Press **Select All** to
    delete all the **Saved Forms** from the app and then **Delete Selected**.

![Delete Saved Form](/images/kobocollect_on_android_latest/delete_saved_form.png)

-   The next tab is the **Blank Forms**. Press **Select All** to delete all the
    **Blank Forms** from the app and then **Delete Selected**.

<p class='note'>Users should not require an internet connection to delete saved
forms in <strong>KoboCollect</strong>.</p>

## Resetting View Sent Form in KoboCollect

When you submit all the filled forms to the server by pressing **Send Finalized
Form**, the successfully submitted forms can be seen in the **View Sent Form**
section. Data managers generally advise to keep this information until the end
of the project as it always provides a reference for the total number of
collections and submissions.

Once the current project’s data collection is over or if you are planning to
start a new project, it is advised to reset the counter in **View Sent Form**.
This will help to keep track of the data collection for the new project.

-   Open **KoboCollect**.
-   Select the icon (circled in K) that is located at the top right of your
    screen.
-   Select **Settings**.

![Select Settings](/images/kobocollect_on_android_latest/select_settings.jpg)

-   Under **Project settings**, select **Project management**.
-   Under **Project management** select **Reset**.
-   Click **Saved forms (instances folder, instances database)** and then select
    **RESET**.

![Reset](/images/kobocollect_on_android_latest/reset.jpg)

-   You should see a small dialogue box with a pop up a message **_"Reset
    results Saved forms: Success"_**.
-   Select **OK**.

<p class='note'>Users do not need an internet connection to reset <strong>View
Sent Form</strong> in <strong>KoboCollect</strong>.</p>

## Hiding Buttons in KoboCollect

In some cases, it is recommended to hide certain buttons in the app from
interviewers to prevent them from editing or changing collected data, decreasing
the risk of data loss.

-   Open **KoboCollect**.
-   Select the icon (circled in K) that is located at the top right of your
    screen.
-   Select **Settings**.
-   Under the **Project settings**, select **Access control**, which includes
    **Main Menu Settings**, **User Settings**, and **Form Entry Settings**.
-   Select **Main Menu Settings** to hide buttons from the main menu.

![Main Menu Settings](/images/kobocollect_on_android_latest/main_menu_settings.jpg)

-   Do the same for **User Settings** and **Form Entry Settings** to hide
    buttons from those menus as well.

<p class='note'>Users do not need an internet connection to hide buttons in
<strong>KoboCollect</strong>.</p>

## Locking KoboCollect with an Admin Password

If needed, you can set up an admin password in the **KoboCollect** app, limiting
access to the app’s admin settings to only team members with the admin password.

-   Open **KoboCollect**.
-   Select the icon (circled in K) that is located at the top right of your
    screen.
-   Select **Settings**.
-   Under the **Project settings**, select **Set admin password**.
-   You will be requested to **Enter New Password**. After entering a new
    password, select **OK**.

<p class='note'>Users do not need an internet connection to lock
<strong>KoboCollect</strong> with an admin password. To remove the admin
password, leave it blank instead of providing a new password.</p>

## Form Management Settings in KoboCollect

There are other form management settings available within **KoboCollect** which
could assist in managing your data collection project:

**Form update** provides an option to update the survey form manually or
automatically. If set to automatic, the forms that are redeployed on the
**KoboToolbox** server are automatically updated in the app. Note that keeping
this feature active will likely drain your device’s battery more quickly.

**Form submission** provides an option to send submissions to the server
manually or automatically, with the options of _Wifi only_, _cellular only_, and
_wifi or cellular_. This setting also gives the option to delete finalized forms
and media after being successfully sent to the server.

**Form filling** provides several options for forms and data collection:

-   Option to mark the form as finalized by default.
-   Option to configure the constraint processing (_validate upon forward swipe
    or defer validation until finalized_).
-   Enable or disable high-resolution video recordings or change the allowed
    image size when taking videos and images through the app.
-   _Show guidance for questions_ under the form filling to show or hide
    guidance for questions
-   _Use of an external app for audio recording_ could help to set up an
    external app for audio recording while collecting data.

Follow the steps outlined below to access the form management settings:

-   Open **KoboCollect**.
-   Select the icon (circled in K) that is located at the top right of your
    screen.
-   Select **Settings**.
-   Under the **Project settings**, select **Form management** and select the
    options relevant for your project.

![Form Management](/images/kobocollect_on_android_latest/form_management.jpg)

<p class='note'>Users do not need an internet connection to access or change
the form management settings in <strong>KoboCollect</strong>.</p>

## Setting Up Metadata in KoboCollect

Users can set up the collection of metadata like _username_, _phone number_ and
_email address_ in **KoboCollect**, providing additional details on who
submitted the records to the server. These details can be helpful to validate
the quality of the data collected by the team.

<p class='note'>In order to collect metadata, it must be configured in both the
<strong>KoboCollect</strong> app and on the <strong>KoboToolbox</strong>
platform for the same project. Please refer to our support article <a
href="form_meta.html" class="reference">Form Settings and Meta Questions</a> for
instructions on how to configure set up in <strong>KoboToolbox</strong>.</p>

-   Open **KoboCollect**.
-   Select the icon (circled in K) that is located at the top right of your
    screen.
-   Select **Settings**.
-   Under the **Project settings**, select **User and device identity**.
-   Under **User and device identity**, select **Form metadata**.

![Form Metadata](/images/kobocollect_on_android_latest/form_metadata.jpg)

-   Enter all the metadata like _username_, _phone number_, and _email address_
    that you want to collect.

<p class='note'>Users do not need an internet connection to access the metadata
setting in <strong>KoboCollect</strong>.</p>

## Differences Between KoboCollect & ODK Collect

**KoboCollect** is a [fork](https://github.com/getodk/collect/network/members)
of **ODK Collect**. As of today, there are no substantive differences between
the two apps. Users are free to use either one for data collection. KoboToolbox
is fully compatible with both apps.

Please note that it is not recommended to have both apps installed
simultaneously as this could lead to some confusion depending on the Android
settings.

Historically, there were several significant differences between the two. Back
in 2009, **KoboToolbox** made several changes to **ODK Collect**, creating
**KoboCollect**, such as _cascading questions_, hiding _delete_, and _edit_
buttons for field data collection. The **XLSForm** was not yet an option in
**ODK Collect** and **KoboToolbox** had built a formbuilder for all question
types and advanced settings, including cascading questions, which were saved
directly as an XML file for the mobile app. These changes were eventually
incorporated into **ODK Collect**, along with many other great features. In
2014, **KoboToolbox** decided to fork **ODK Collect** to create the
[new KoboCollect](https://github.com/kobotoolbox/collect), with minimal changes,
including the **KoboToolbox** server in the configuration dropdown, a reference
back to **ODK Collect**, and the **KoboToolbox** logo and name.
