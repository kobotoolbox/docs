# Data Collection on KoboCollect App (Latest Version)
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c2e8c882fdd831549c2f7f4474a9d522bafc181b/source/kobocollect_on_android_latest.md" class="reference">2 Dec 2021</a>

<p class='note'>The latest version of the KoboCollect App refers to v2021.2.4 and above.</p>

__KoboCollect__ is an open-source Android app for collecting survey data. It’s
one of two ways that you can collect data through __KoboToolbox__ (the other
way is through [web forms - Enketo](data_through_webforms.md)). It’s free and
the latest version of the app can be accessed in the [Google Play
Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android)
if you have Android versions 5 and above.

If you have an Android version below 5, you can install an older version of the
app through the [KoboToolbox GitHub
Repository](https://github.com/kobotoolbox/collect/releases). We have a support
article outlining how to collect data in the older version of __KoboCollect__
[here](kobocollect-android.md). We recommend using the latest version of
the app, if possible, as it includes features and bug fixes that may not be
available in older versions.

## Setting Up the Server Connection

The first step after installing __KoboCollect__ on your device is to set up the
server __URL__, __Username__, and __Password__, which connects your
__KoboCollect__ app to the __KoboToolbox__ server. This allows you to download
deployed forms from __KoboToolbox__ to your mobile device and also send data
collected through the app back to the server.

The server in __KoboCollect__ can be configured in two different ways: _manually_
or through a _QR code_.

### Setting up the server connection _manually_:

- Open __KoboCollect__.
- Select __Manually enter project details__.

![Collect Data Anywhere](/images/kobocollect_on_android_latest/collect_data_anywhere.jpg)

- You will now be asked to input the __URL__, __Username__, and __Password__, and
then select __Add__. For the URL, you must select from the [two KoboToolbox
servers](server.md). If you created your user account on the general use
server, the URL is `https://kc.kobotoolbox.org`. If your user account is on the
Humanitarian server (OCHA), the URL is `https://kc.humanitarianresponse.info`.

![Server Settings](/images/kobocollect_on_android_latest/server_settings.png)

<p class='note'>Despite setting up the server settings correctly, users may
have trouble connecting <strong>KoboCollect</strong> to the server. This could
be an issue with the device’s incorrect date and time settings. To learn more
about troubleshooting <strong>KoboCollect</strong>, please read our support
article <a href="troubleshooting_kobocollect.html"
class="reference">Troubleshooting KoboCollect Android Application</a>.</p>

- After setting up the server, you should now see the following home screen.

![Home Page Comparison](/images/kobocollect_on_android_latest/home_page_comparison.png)

You can use __KoboCollect__ to _get blank forms to your device_, _collect data
(fill blank forms)_, _store it in your device_, _edit the filled in forms (edit
saved forms)_, _submit saved forms_, and _delete filled in forms/blank forms_.

### Setting up multiple server connections _manually_

<p class='note'>This feature is only available with the latest version of the app and is relevant if you have multiple
<strong>KoboToolbox</strong> user accounts.</p>

Some users have multiple __KoboToolbox__ accounts, either on the same server or
a different server. With the latest version, users can manage all their
accounts in the same app and use them in parallel by switching from one account
to another as needed. Follow the steps outlined below to setup multiple server
connections:

- After setting up your account in the app (see instructions above), open
  __KoboCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- You should see a dialogue box like the one shown below.

![Project Settings Modal 1](/images/kobocollect_on_android_latest/project_settings_modal_1.jpg)

- Select __Add project__.
- Fill in the __URL__, __Username__, and __Password__ and then select __Add__.

![Server Settings](/images/kobocollect_on_android_latest/server_settings.png)

- You should now see the home screen. Once again, select the icon (circled in
  K) at the top right of your screen to ensure your connection was successful.
- After setting up an additional server, you should see a dialogue box like the
  one shown below.

![Project Settings Modal 2](/images/kobocollect_on_android_latest/project_settings_modal_2.jpg)

Here, you will see two different accounts setup in the app. You can add more
accounts as needed. The account listed first is the active one and you can only
see forms for the active account. You can easily switch to your other accounts,
making them active, by simply selecting them.

### Setting up the server connection with a _QR code_

Oftentimes, users in large projects will need to set up a large number of
devices under the same server settings (__URL__, __Username__, and
__Password__, etc.). Setting up all the devices manually would be
time-consuming and prone to error. To save time, you can set up one device
manually and then copy the settings through a QR code generated from the first
device.

<p class='note'>To set up a device with a QR Code, you will require at least
one app that has been set up manually.</p>

- Open __KoboCollect__ and choose the project that has been set up.
- Select the circle K icon that is located at the top right of your screen.
- Select __Settings__. 

![Project Settings Modal 1](/images/kobocollect_on_android_latest/project_settings_modal_1.jpg)

- Then select __Project Management__.

![Project Settings](/images/kobocollect_on_android_latest/project_settings_list.jpg)

- Select __Reconfigure with QR code__.
- Choose __QR Code__ at the top. A QR code will be displayed that contains all
  of your __KoboCollect__ settings, including the _server URL_, _Username_, and
  _Password_.

![QR Code](/images/kobocollect_on_android_latest/qr_code.jpg)

- Open __KoboCollect__ on another device that you want to set up.
- Select __Configure with QR code__.
- Scan the QR code. If successful, you should hear a beep and the app will be
  automatically configured. Repeat for all other devices you want set up.

<p class='note'>You can also copy the QR code and share it by email, Whatsapp,
etc., to set up other devices but be aware that the QR code contains the
password to your account, allowing others to sign into your account. <strong>It
is not recommended to share the QR code through electronic means if the same
account has permissions to view, edit, or delete data.</strong></p>

## Setting Up Blank Forms in KoboCollect

Once you have configured the __URL__, __Username__, and __Password__ in the app
correctly, you can send blank forms to your device from the __KoboToolbox__
server.

- Open __KoboCollect__.
- Make sure that you have at least one project set up in your __KoboToolbox__
  user account and that your device is connected to the internet.
- Select __Get Blank Form__ from the home menu.

![Get Blank Form Button](/images/kobocollect_on_android_latest/get_blank_form_button.png)

- A list of all your deployed survey forms should appear. Press __Select All__
  to have all the survey forms sent to the app or select the ones you wish to
  have by selecting them manually. Then click __Get Selected__.

![Get Blank Form List](/images/kobocollect_on_android_latest/get_blank_form_list.jpg)

<p class='note'>Users will need an internet connection while sending blank
forms to <strong>KoboCollect</strong>.</p>

## Collecting Data in KoboCollect

Once you have blank form(s) in the app, you will no longer require an internet
connection to collect data. The blank forms and the filled in forms will stay
on the device until you delete them from the app or submit them to the server.

- Open __KoboCollect__.
- Select __Fill Blank__ Form from the home menu.
- Select the survey form that you want to use to start collecting data.
- Go through all the questions *by swiping your finger from right to left or by
  selecting the __NEXT__ key after answering the questions*.
- At the end of the survey, select __Save Form and Exit__.

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

Once you have pressed __Save Form and Exit__, the saved form is automatically
stored under __Edit Saved Form__.

- Open __KoboCollect__.
- Select __Edit Saved Form__ from the home menu.
- You will see a list of __Saved Forms__. Choose the one that needs edits or
  updates.
- Make changes as needed, and then select __Save Form and Exit__.
- Repeat the process multiple times if multiple forms need edits or updates.

<p class='note'>Users do not need an internet connection while editing a saved
form in <strong>KoboCollect</strong>.</p>

## Uploading Finalized Data to the Server

Once you have collected your data, and made any necessary edits, you can upload
the forms to the __KoboToolbox__ server.

- Open __KoboCollect__.
- Make sure the device is securely connected to the internet.
- Select __Send Finalized Form__ from the home screen.
- A list of all the collected forms should appear.
- Press __Select All__ (or select the ones you wish to upload) and then press
  __Send Selected__.
- To ensure the forms were uploaded successfully, select __View Sent Form__.
  You should now be able to view all the submitted forms.

<p class='note'>Users will need an internet connection while submitting data
from <strong>KoboCollect</strong> to the server.</p>

## Deleting Saved Forms in KoboCollect

Once you have completed data collection for your survey project and all the
filled in forms have been uploaded to the server, it is recommended to delete
the forms from the __KoboCollect__ app. Keeping them in the app can confuse
interviewers while collecting data for a different project. Follow the steps
outlined below to delete __Saved Forms__ and __Blank Forms__ from your app.

- Open __KoboCollect__.
- Select __Delete Saved Form__ from the home screen.
- Users should now see two tabs. The default is __Saved Forms__. These are the
  forms that were filled in while collecting data. Press __Select All__ to
  delete all the __Saved Forms__ from the app and then __Delete Selected__.

![Delete Saved Form](/images/kobocollect_on_android_latest/delete_saved_form.png)

- The next tab is the __Blank Forms__. Press __Select All__ to delete all the
  __Blank Forms__ from the app and then __Delete Selected__.

<p class='note'>Users should not require an internet connection to delete saved
forms in <strong>KoboCollect</strong>.</p>

## Resetting View Sent Form in KoboCollect

When you submit all the filled forms to the server by pressing __Send Finalized
Form__, the successfully submitted forms can be seen in the __View Sent Form__
section. Data managers generally advise to keep this information until the end
of the project as it always provides a reference for the total number of
collections and submissions.

Once the current project’s data collection is over or if you are planning to
start a new project, it is advised to reset the counter in __View Sent Form__.
This will help to keep track of the data collection for the new project.

- Open __KoboCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.

![Select Settings](/images/kobocollect_on_android_latest/select_settings.jpg)

- Under __Project settings__, select __Project management__.
- Under __Project management__ select __Reset__.
- Click __Saved forms (instances folder, instances database)__ and then select
  __RESET__.

![Reset](/images/kobocollect_on_android_latest/reset.jpg)

- You should see a small dialogue box with a pop up a message ___"Reset results
  Saved forms: Success"___.
- Select __OK__.

<p class='note'>Users do not need an internet connection to reset <strong>View
Sent Form</strong> in <strong>KoboCollect</strong>.</p>

## Hiding Buttons in KoboCollect

In some cases, it is recommended to hide certain buttons in the app from
interviewers to prevent them from editing or changing collected data,
decreasing the risk of data loss.

- Open __KoboCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.
- Under the __Project settings__, select __Access control__, which includes
  __Main Menu Settings__, __User Settings__, and __Form Entry Settings__.
- Select __Main Menu Settings__ to hide buttons from the main menu.

![Main Menu Settings](/images/kobocollect_on_android_latest/main_menu_settings.jpg)

- Do the same for __User Settings__ and __Form Entry Settings__ to hide buttons
  from those menus as well.

<p class='note'>Users do not need an internet connection to hide buttons in
<strong>KoboCollect</strong>.</p>

## Locking KoboCollect with an Admin Password

If needed, you can set up an admin password in the __KoboCollect__ app,
limiting access to the app’s admin settings to only team members with the admin
password.

- Open __KoboCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.
- Under the __Project settings__, select __Set admin password__.
- You will be requested to __Enter New Password__. After entering a new
  password, select __OK__.

<p class='note'>Users do not need an internet connection to lock
<strong>KoboCollect</strong> with an admin password. To remove the admin
password, leave it blank instead of providing a new password.</p>

## Form Management Settings in KoboCollect

There are other form management settings available within __KoboCollect__ which
could assist in managing your data collection project:

__Form update__ provides an option to update the survey form manually or
automatically. If set to automatic, the forms that are redeployed on the
__KoboToolbox__ server are automatically updated in the app. Note that keeping
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

- Open __KoboCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.
- Under the __Project settings__, select __Form management__ and select the
  options relevant for your project.

![Form Management](/images/kobocollect_on_android_latest/form_management.jpg)

<p class='note'>Users do not need an internet connection to access or change
the form management settings in <strong>KoboCollect</strong>.</p>

## Setting Up Metadata in KoboCollect

Users can set up the collection of metadata like _username_, _phone number_ and
_email address_ in __KoboCollect__, providing additional details on who
submitted the records to the server. These details can be helpful to validate
the quality of the data collected by the team.

<p class='note'>In order to collect metadata, it must be configured in both the
<strong>KoboCollect</strong> app and on the <strong>KoboToolbox</strong>
platform for the same project. Please refer to our support article <a
href="form_meta.html" class="reference">Form Settings and Meta Questions</a> for
instructions on how to configure set up in <strong>KoboToolbox</strong>.</p>

- Open __KoboCollect__.
- Select the icon (circled in K) that is located at the top right of your screen.
- Select __Settings__.
- Under the __Project settings__, select __User and device identity__.
- Under __User and device identity__, select __Form metadata__.

![Form Metadata](/images/kobocollect_on_android_latest/form_metadata.jpg)

- Enter all the metadata like _username_, _phone number_, and _email address_
  that you want to collect.

<p class='note'>Users do not need an internet connection to access the metadata
setting in <strong>KoboCollect</strong>.</p>

## Differences Between KoboCollect & ODK Collect

__KoboCollect__ is a [fork](https://github.com/getodk/collect/network/members)
of __ODK Collect__. As of today, there are no substantive differences between
the two apps. Users are free to use either one for data collection. KoboToolbox
is fully compatible with both apps.

Please note that it is not recommended to have both apps installed
simultaneously as this could lead to some confusion depending on the Android
settings.

Historically, there were several significant differences between the two. Back
in 2009, __KoboToolbox__ made several changes to __ODK Collect__, creating
__KoboCollect__, such as _cascading questions_, hiding _delete_, and _edit_
buttons for field data collection. The __XLSForm__ was not yet an option in
__ODK Collect__ and __KoboToolbox__ had built a formbuilder for all question
types and advanced settings, including cascading questions, which were saved
directly as an XML file for the mobile app. These changes were eventually
incorporated into __ODK Collect__, along with many other great features. In
2014, __KoboToolbox__ decided to fork __ODK Collect__ to create the [new
KoboCollect](https://github.com/kobotoolbox/collect), with minimal changes,
including the __KoboToolbox__ server in the configuration dropdown, a reference
back to __ODK Collect__, and the __KoboToolbox__ logo and name.
