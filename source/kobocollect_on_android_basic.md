# Basic Data Collection on KoBoCollect App

**For Android versions 7 and above**

__KoBoCollect__ is an open-source Android app for collecting survey data. It’s
one of two ways that you can collect data through __KoBoToolbox__ (the other
way is through [web forms - Enketo](data_through_webforms.md)). It’s free and
the latest version of the app can be accessed in the [Google Play
Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android)
if you have Android versions 7 and above.

If you have Android versions 4.1 to 6, you can install an older version of the
app through the [KoBoToolbox GitHub
Repository](https://github.com/kobotoolbox/collect/releases). We have a support
article outlining how to collect data in the older version of __KoBoCollect__
[here](kobocollect_on_android_old.md). We recommend using the latest version of
the app, if possible, as it includes features and bug fixes that may not be
available in older versions.

To review advanced functions on the latest version of the app, see our support
article [Advanced Functions on KoBoCollect
app](kobocollect_on_android_advanced.md).

## Setting Up the Server Connection

The first step after installing __KoBoCollect__ on your device is to set up the
server __URL__, __Username__, and __Password__, which connects your
__KoBoCollect__ app to the __KoBoToolbox__ server. This allows you to download
deployed forms from __KoBoToolbox__ to your mobile device and also send data
collected through the app back to the server.

The server in __KoBoCollect__ can be configured in two different ways: manually or through a QR code.

### Setting up the server connection manually:

- Open __KoBoCollect__.
- Select __Manually enter project details__.

![Collect Data Anywhere](/images/kobocollect_on_android_basic/collect_data_anywhere.jpg)

You will now be asked to input the __URL__, __Username__, and __Password__, and
then select __Add__. For the URL, you must select from the [two KoBoToolbox
servers](server.md). If you created your user account on the general use
server, the URL is `https://kc.kobotoolbox.org`. If your user account is on the
Humanitarian server (OCHA), the URL is `https://kc.humanitarianresponse.info`.

![Server Settings](/images/kobocollect_on_android_basic/server_settings.png)

<p class='note'>Despite setting up the server settings correctly, users may
have trouble connecting <strong>KoBoCollect</strong> to the server. This could be an issue with
the device’s incorrect date and time settings. To learn more about
troubleshooting <strong>KoBoCollect</strong>, please read our support article <a
href="troubleshooting_kobocollect.html" class="reference">Troubleshooting
KoBoCollect Android Application</a>.</p>

- After setting up the server, you should now see the following home screen.

![Home Page Comparison](/images/kobocollect_on_android_basic/home_page_comparison.png)

You can use __KoBoCollect__ to get blank forms to your device, collect data
(fill blank forms), store it in your device, edit the filled in forms (edit
saved forms), submit saved forms, and delete filled in forms/blank forms.

### Setting up multiple server connections manually

<p class='note'>This section is only relevant if you have multiple
<strong>KoBoToolbox</strong> user accounts.</p>

Some users have multiple __KoBoToolbox__ accounts, either on the same server or
a different server. With the latest version, users can manage all their
accounts in the same app and use them in parallel by switching from one account
to another as needed. Follow the steps outlined below to setup multiple server
connections:
- After setting up your account in the app (see instructions above), open
  __KoBoCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- You should see a dialogue box like the one shown below.

![Project Settings Modal 1](/images/kobocollect_on_android_basic/project_settings_modal_1.jpg)

- Select __Add project__.
- Fill in the __URL__, __Username__, and __Password__ and then select __Add__.

![Server Settings](/images/kobocollect_on_android_basic/server_settings.png)

- You should now see the home screen. Once again, select the icon (circled in
  K) at the top right of your screen to ensure your connection was successful.
- After setting up an additional server, you should see a dialogue box like the
  one shown below.

![Project Settings Modal 2](/images/kobocollect_on_android_basic/project_settings_modal_2.jpg)

Here, you will see two different accounts setup in the app. You can add more
accounts as needed. The account listed first is the active one and you can only
see forms for the active account. You can easily switch to your other accounts,
making them active, by simply selecting them.

### Setting up the server connection with a QR code

Oftentimes, users in large projects will need to set up a large number of
devices under the same server settings (__URL__, __Username__, and
__Password__, etc.). Setting up all the devices manually would be
time-consuming and prone to error. To save time, you can set up one device
manually and then copy the settings through a QR code generated from the first
device.

<p class='note'>To set up a device with a QR Code, you will require at least
one app that has been set up manually.</p>

- Open __KoBoCollect__ and choose the project that has been set up.
- Select the circle K icon that is located at the top right of your screen.
- Select __Settings__, then __Project Management__.

![Project Settings Modal 1](/images/kobocollect_on_android_basic/project_settings_modal_1.jpg)
![Project Settings](/images/kobocollect_on_android_basic/project_settings_list.jpg)

- Select __Reconfigure with QR code__.
- Choose __QR Code__ at the top. A QR code will be displayed that contains all
  of your __KoBoCollect__ settings, including the _server URL_, _username_, and
  _password_.

![QR Code](/images/kobocollect_on_android_basic/qr_code.jpg)

- Open __KoBoCollect__ on another device that you want to set up.
- Select __Configure with QR code__.
- Scan the QR code. If successful, you should hear a beep and the app will be
  automatically configured. Repeat for all other devices you want set up.

<p class='note'>You can also copy the QR code and share it by email, Whatsapp,
etc., to set up other devices but be aware that the QR code contains the
password to your account, allowing others to sign into your account. <strong>It
is not recommended to share the QR code through electronic means if the same
account has permissions to view, edit, or delete data.</strong></p>

## Setting Up Blank Forms in KoBoCollect

Once you have configured the __URL__, __Username__, and __Password__ in the app
correctly, you can send blank forms to your device from the __KoBoToolbox__
server.
- Open __KoBoCollect__.
- Make sure that you have at least one project set up in your __KoBoToolbox__
  user account and that your device is connected to the internet.
- Select __Get Blank Form__ from the home menu.

![Get Blank Form Button](/images/kobocollect_on_android_basic/get_blank_form_button.png)

- A list of all your deployed survey forms should appear. Press __Select All__ to
have all the survey forms sent to the app or select the ones you wish to have
by selecting them manually. Then click __Get Selected__.

![Get Blank Form List](/images/kobocollect_on_android_basic/get_blank_form_list.jpg)

<p class='note'>Users will need an internet connection while sending blank
forms to <strong>KoBoCollect</strong>.</p>

## Collecting Data in KoBoCollect

Once you have blank form(s) in the app, you will no longer require an internet connection to collect data. The blank forms and the filled in forms will stay on the device until you delete them from the app or submit them to the server.
- Open __KoBoCollect__.
- Select __Fill Blank__ Form from the home menu.
- Select the survey form that you want to use to start collecting data.
- Go through all the questions *by swiping your finger from right to left or by selecting the __NEXT__ key after answering the questions*.
- At the end of the survey, select __Save Form and Exit__.

![Finalise Form](/images/kobocollect_on_android_basic/finalise_form.png)

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

Once you have pressed __Save Form and Exit__, the saved form is automatically stored under __Edit Saved Form__.
- Open __KoBoCollect__.
- Select __Edit Saved Form__ from the home menu.
- You will see a list of __Saved Forms__. Choose the one that needs edits or updates.
- Make changes as needed, and then select __Save Form and Exit__.
- Repeat the process multiple times if multiple forms need edits or updates.

<p class='note'>Users do not need an internet connection while editing a saved form in <strong>KoBoCollect</strong>.</p>

## Uploading Finalized Data to the Server

Once you have collected your data, and made any necessary edits, you can upload
the forms to the __KoBoToolbox__ server.
- Open __KoBoCollect__.
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
  forms that were filled in while collecting data. Press __Select All__ to
  delete all the __Saved Forms__ from the app and then __Delete Selected__.

![Delete Saved Form](/images/kobocollect_on_android_basic/delete_saved_form.png)

- The next tab is the __Blank Forms__. Press __Select All__ to delete all the
  __Blank Forms__ from the app and then __Delete Selected__.

<p class='note'>Users should not require an internet connection to delete saved
forms in <strong>KoBoCollect</strong>.</p>

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
