# Data Collection on KoBoCollect App - Android Versions 4.1 - 6

__For Android versions 4.1 to 6__

KoBoCollect is an open-source Android app for collecting survey data. It’s one
of two ways that you can collect data through KoBoToolbox (the other way is
through [web forms - Enketo](data_through_webforms.md)). It’s free and users
with Android versions 4.1 to 6 can install an older version of the app through
the [KoBoToolbox GitHub
Repository](https://github.com/kobotoolbox/collect/releases).

If you have Android versions 7 and above, you can download the latest version
of the KoBoCollect App on the [Google Play
Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android)
and refer to our support articles for the latest version of the app: [Basic
Data Collection on the KoBoCollect App](kobocollect_on_android_basic.md) and
[Advanced Functions in the KoBoCollect
App](kobocollect_on_android_advanced.md). We recommend using the latest version
of the app, if possible, as it includes features and bug fixes that may not be
available in older versions.

## Setting Up the Server Connection

The first step after installing __KoBoCollect__ on your device is to set up the
server __URL__, __Username__, and __Password__, which connects your
__KoBoCollect__ app to the __KoBoToolbox__ server. This allows you to download
deployed forms from __KoBoToolbox__ to your mobile device and also send data
collected through the app back to the server.

The server in __KoBoCollect__ can be configured in two different ways: manually
or through a QR code.

### Setting up server connection manually:

- Open __KoBoCollect__.
- Select __Main Settings__ (three vertical dots) > __General Settings__ (this
  may be at the top right, bottom right, or at the bottom in the center of your
  screen depending on your Android version) > __Server__.

![General Settings](/images/kobocollect_android/general_settings.png)

- You will now be asked to input the __URL__, __Username__, and __Password__,
  and then select __Add__. For the URL, you must select from the two
  __KoBoToolbox__ servers. If you created your user account on the general use
  server, the URL is `https://kc.kobotoolbox.org`. If your user account is on
  the Humanitarian server (OCHA), the URL is
  `https://kc.humanitarianresponse.info`.

![Server Settings](/images/kobocollect_android/server_settings.png)

<p class='note'>Despite setting up the server settings correctly, users may
have trouble connecting <strong>KoBoCollect</strong> to the server. This could
be an issue with the device’s incorrect date and time settings. To learn more
about troubleshooting <strong>KoBoCollect</strong>, please read our support
article <a href="troubleshooting_kobocollect.html"
class="reference">Troubleshooting KoBoCollect Android Application</a>.</p>

- After setting up the server, you should now see the following home screen.

![Main Menu](/images/kobocollect_android/main_menu.jpg)

You can use __KoBoCollect__ to get blank forms to your device, collect data
(fill blank forms), store it in your device, edit the filled in forms (edit
saved forms), submit saved forms, and delete filled in forms / blank forms.

### Setting up server connection with a QR code

Oftentimes, users in large projects will need to set up a large number of
devices under the same server settings (__URL__, __Username__, and
__Password__, etc.). Setting up all the devices manually would be
time-consuming and prone to error. To save time, you can configure just one
device manually and then copy the settings through a QR code generated from the
first device.

<p class='note'>To set up a device with a QR Code, you will require at least
one app that has been set up manually.</p>

- Open __KoBoCollect__ to the server that has been configured.
- Select __Main Settings__ (three vertical dots at the top right).
- Select __Configure via QR code__.

![Settings Drop Down](/images/kobocollect_android/settings_drop_down.png)

- Select the __QR CODE__ tab.

![QR Code](/images/kobocollect_android/qr_code.png)

- Now open __KoBoCollect__ in another device that you want to configure and
  navigate to __Main Settings__ > __Configure via QR code__ > __SCAN__.
- Scan the QR code. If successful, you should hear a beep sound and the app
  will be automatically configured.

<p class='note'>You can also copy the QR code and share it by email, Whatsapp,
etc., to set up other devices but be aware that the QR code contains the
password to your account, allowing others to sign into your account. <strong>It
is not recommended to share the QR code through electronic means if the same
account has permissions to view, edit, or delete data</strong>.</p>

## Setting Up Blank Forms in KoBoCollect

Once you have configured the __URL__, __Username__, and __Password__ in the app
correctly, you can send blank forms to your device from the __KoBoToolbox__
server.
- Open __KoBoCollect__.
- Make sure that you have at least one project set up in your __KoBoToolbox__
  user account and that your device is connected to the internet.
- Select __Get Blank Form__ from the home menu.

![Get Blank Form Button](/images/kobocollect_android/get_blank_form_button.png)

- A list of all your deployed survey forms should appear. Press __Select All__
  to have all the survey forms sent to the app or select the ones you wish to
  have by selecting them manually. Then click __Get Selected__.

![Get Blank Form List](/images/kobocollect_android/get_blank_from_list.jpg)

<p class='note'>Users will need an internet connection while sending blank
forms to <strong>KoBoCollect</strong>.</p>

## Collecting Data in KoBoCollect

Once you have blank form(s) in the app, you no longer require an internet
connection to collect data. The blank forms and the filled in forms will stay
on the device until you delete them from the app or submit them to the server.
- Open __KoBoCollect__.
- Select __Fill Blank Form__ from the home menu.
- Select the survey form that you want to use to start collecting data.
- Go through all the questions *by swiping your finger from right to left or by
  selecting the __NEXT__ key after answering the questions.*
- At the end of the survey, select __Save Form and Exit__.

![Finalise Form](/images/kobocollect_android/finalised_form.png)

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

## Editing Data in KoBoCollect

Once you have pressed __Save Form and Exit__, the saved form is automatically
stored under __Edit Saved Form__. If you wish to edit this saved form, you can
follow the steps outlined below.
- Open __KoBoCollect__.
- Select __Edit Saved Form__ from the home menu.
- You will see a list of __Saved Forms__. Choose the one that needs edits or
  updates.
- Make changes as needed, and then select __Save Form and Exit__.
- Repeat the process multiple times if multiple forms need edits or updates.

<p class='note'>Users do not need an internet connection while editing a saved
form in <strong>KoBoCollect</strong>.</p>

## Uploading Finalized Data to the Server

Once you have collected your data, and made any necessary edits, you can upload
the forms to the __KoBoToolbox__ server.
- __Open__ KoBoCollect.
- Make sure the device is securely connected to the internet.
- Select __Send Finalized Form__ from the home screen.
- A list of all the collected forms should appear.
- Press __Select All__ (or select the ones you wish to upload) and then press
  __Send Selected__.
- To ensure the forms were uploaded successfully, select __View Sent Form__.
  You should now be able to view all the submitted forms.

<p class='note'>Users will need an internet connection while submitting data
from <strong>KoBoCollect</strong> to the server.</p>

## Deleting Saved Forms in KoBoCollect

Once you have completed data collection for your survey project and all the
filled in forms have been uploaded to the server, it is recommended to delete
the forms from the __KoBoCollect__ app. Keeping them in the app can confuse
interviewers while collecting data for a different project. Follow the steps
outlined below to delete __Saved Forms__ and __Blank Forms__ from your app.
- Open __KoBoCollect__.
- Select __Delete Saved Form__ from the home screen.
- Users should now see two tabs. The default is __Saved Forms__. These are the
  forms filled in during data collection. Press __Select All__ to delete all
  the __Saved Forms__ from the app and then __Delete Selected__.

![Delete Saved Form](/images/kobocollect_android/delete_saved_forms.png)

- The next tab is the __Blank Forms__. Press __Select All__ to delete all the
  __Blank Forms__ from the app and then __Delete Selected__.

<p class='note'>Users should not require an internet connection to delete saved
forms in <strong>KoBoCollect</strong>.</p>

## Resetting View Sent Form in KoBoCollect

When you submit all the filled forms to the server by pressing __Send Finalized
Form__, the successfully submitted forms can be seen in the __View Sent Form__
section. Data managers generally advise to keep this information until the end
of the project as it always provides a reference for the total number of
collections and submissions.

Once the current project’s data collection is over or if you are planning to
start a new project, it is advised to reset the counter in __View Sent Form__.
This will help to keep track of the data collection for the new project.
- Open __KoBoCollect__
- Select __Main Settings__ (three vertical dots).
- Select __Admin Settings__ (this may be at the top right, bottom right, or at
  the bottom in the center of your screen depending on your android version).
- Select __Reset application__.

![Reset Application](/images/kobocollect_android/reset_application.png)

- Check on __Saved forms (instances folder, instances database)__ and then
  select __RESET__. You should see a small dialogue box with a pop up a message
  "*__Reset results Saved forms: Success__*".
- Select __OK__.

<p class='note'>Users do not need an internet connection to reset <strong>View
Sent Form</strong> in <strong>KoBoCollect</strong>.</p>

## Hiding buttons in KoBoCollect

In some cases, it is recommended to hide certain buttons in the app from
interviewers to prevent them from editing or changing collected data,
decreasing the risk of data loss.
- Open __KoBoCollect__.
- Select __Main Settings__ (three vertical dots).
- Select __Admin Settings__.

![Admin Settings](/images/kobocollect_android/admin_settings.png)

- At the bottom, you should see the __User Access Control__, which includes
  __Main Menu Settings__, __User Settings__, and __Form Entry Settings__.
- Select __Main Menu Settings__ to hide the buttons from the main menu.

![Main Menu Settings](/images/kobocollect_android/main_menu_settings.png)

- Do the same for __User Settings__ and __Form Entry Settings__ to hide buttons
  from those menus as well.

<p class='note'>Users do not need an internet connection to hide buttons in
<strong>KoBoCollect</strong>.</p>

## Locking KoBoCollect with an Admin Password

If needed, you can set up an admin password in the __KoBoCollect__ app,
limiting access to the app’s admin settings to only team members with the admin
password.
- Open __KoBoCollect__.
- Select __Main Settings__ (three vertical dots).
- Select __Admin Settings__.
- Select __Admin Password__.

![Admin Password](/images/kobocollect_android/admin_password.jpg)

- You will be requested to __Enter New Password__. After entering a new
  password, select __OK__.

<p class='note'>Users do not need an internet connection to lock
<strong>KoBoCollect</strong> with an admin password. To remove the admin
password, leave it blank instead of providing a new password.</p>

## Form management settings in KoBoCollect

There are other form management settings available within __KoBoCollect__ which
could assist in managing your data collection project:

__Form update__ provides an option to update the survey form manually or
automatically. If set to automatic, the forms that are redeployed on the
__KoBoToolbox__ server are automatically updated in the app. Note that keeping
this feature active will likely drain your device’s battery more quickly.

__Form submission__ provides an option to send submissions to the server
manually or automatically, with the options of _Wifi only_, _cellular only_,
and _wifi or cellular_. This setting also gives the option to delete finalized
forms and media after being successfully sent to the server.

__Form filling__ provides several options for forms and data collection:
- Option to mark the form as finalized by default.
- Option to configure the constraint processing (_validate upon forward swipe
  or defer validation until finalized_).
- Enable or disable high-resolution video recordings or change the allowed
  image size when taking videos and images through the app.
- _Show guidance for questions_ under the form filling to show or hide guidance
  for questions
- _Use of an external app for audio recording_ could help to set up an external
  app for audio recording while collecting data.

Follow the steps outlined below to access the form management settings:
- Open __KoBoCollect__.
- Select __Main Settings__ (three vertical dots).
- Select __General Settings__.
- Select __Form management__ and select the options relevant for your project.

![Form Management](/images/kobocollect_android/form_management.jpg)

<p class='note'>Users do not need an internet connection to access or change
the form management settings in <strong>KoBoCollect</strong>.</p>

## Setting Up Metadata in KoBoCollect

Users can set up the collection of metadata like _username_, _phone number_ and
_email address_ in __KoBoCollect__, providing additional details on who
submitted the records to the server. These details can be helpful to validate
the quality of the data collected by the team.

<p class='note'>In order to collect metadata, it must be configured in both the
<strong>KoBoCollect</strong> app and on the <strong>KoBoToolbox</strong>
platform for the same project. Please refer to our support article <a
href="form_meta.html" class="reference">Form Settings and Meta Questions</a>
for instructions on how to configure set up in
<strong>KoBoToolbox</strong>.</p>

- Open __KoBoCollect__.
- Select __Main Settings__ (three vertical dots).
- Select __General Settings__.
- Select __User and device identity__.
- Under the __User and device identity__, select __Form metadata__.

![Form Metadata](/images/kobocollect_android/form_metadata.jpg)

- Enter all the metadata like _username_, _phone number_, and _email address_
  that you want to collect.

<p class='note'>Users do not need an internet connection to access the metadata
setting in <strong>KoBoCollect</strong>.</p>

## Differences Between KoBoCollect & ODK Collect

__KoBoCollect__ is a [fork](https://github.com/getodk/collect/network/members)
of __ODK Collect__. As of today, there are no substantive differences between
the two apps. Users are free to use either one for data collection. KoBoToolbox
is fully compatible with both apps.

Please note that it is not recommended to have both apps installed
simultaneously as this could lead to some confusion depending on the Android
settings.

Historically, there were several significant differences between the two. Back
in 2009, __KoBoToolbox__ made several changes to __ODK Collect__, creating
__KoBoCollect__, such as _cascading questions_, hiding _delete_, and _edit_
buttons for field data collection. The __XLSForm__ was not yet an option in
__ODK Collect__ and __KoBoToolbox__ had built a form builder for all question
types and advanced settings, including cascading questions, which were saved
directly as an XML file for the mobile app. These changes were eventually
incorporated into __ODK Collect__, along with many other great features. In
2014, __KoBoToolbox__ decided to fork __ODK Collect__ to create the [new
KoBoCollect](https://github.com/kobotoolbox/collect), with minimal changes,
including the __KoBoToolbox__ server in the configuration dropdown, a reference
back to __ODK Collect__, and the __KoBoToolbox__ logo and name.
