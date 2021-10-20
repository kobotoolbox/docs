# Advanced Functions on KoBoCollect App

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

To review basic functions on the latest version of the app, see our support
article [Basic Data Collection on KoBoCollect
app](kobocollect_on_android_basic.md).

## Resetting View Sent Form in KoBoCollect

When you submit all the filled forms to the server by pressing **Send Finalized
Form**, the successfully submitted forms can be seen in the **View Sent Form**
section. Data managers generally advise to keep this information until the end
of the project as it always provides a reference for the total number of
collections and submissions.

Once the current project’s data collection is over or if you are planning to
start a new project, it is advised to reset the counter in **View Sent Form**.
This will help to keep track of the data collection for the new project.
- Open __KoBoCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.

![Select Settings](/images/kobocollect_on_android_advanced/select_settings.jpg)

- Under **Project settings**, select **Project management**.
- Under **Project management** select __Reset__.
- Click **Saved forms (instances folder, instances database)** and then select
  __RESET__.

![Reset](/images/kobocollect_on_android_advanced/reset.jpg)

- You should see a small dialogue box with a pop up a message ***"Reset results
  Saved forms: Success"***.
- Select __OK__.

<p class='note'>Users do not need an internet connection to reset <strong>View
Sent Form</strong> in <strong>KoBoCollect</strong>.</p>

## Hiding Buttons in KoBoCollect

In some cases, it is recommended to hide certain buttons in the app from
interviewers to prevent them from editing or changing collected data,
decreasing the risk of data loss.
- Open __KoBoCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.
- Under the **Project settings**, select **Access control**, which includes
  **Main Menu Settings**, **User Settings**, and **Form Entry Settings**.
- Select **Main Menu Settings** to hide buttons from the main menu.

![Main Menu Settings](/images/kobocollect_on_android_advanced/main_menu_settings.jpg)

- Do the same for **User Settings** and **Form Entry Settings** to hide buttons
  from those menus as well.

<p class='note'>Users do not need an internet connection to hide buttons in
<strong>KoBoCollect</strong>.</p>

## Locking KoBoCollect with an Admin Password

If needed, you can set up an admin password in the __KoBoCollect__ app,
limiting access to the app’s admin settings to only team members with the admin
password.
- Open __KoBoCollect__.
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.
- Under the **Project settings**, select **Set admin password**.
- You will be requested to **Enter New Password**. After entering a new
  password, select __OK__.

<p class='note'>Users do not need an internet connection to lock
<strong>KoBoCollect</strong> with an admin password. To remove the admin
password, leave it blank instead of providing a new password.</p>

## Form Management Settings in KoBoCollect

There are other form management settings available within __KoBoCollect__ which
could assist in managing your data collection project:

**Form update** provides an option to update the survey form manually or
automatically. If set to automatic, the forms that are redeployed on the
__KoBoToolbox__ server are automatically updated in the app. Note that keeping
this feature active will likely drain your device’s battery more quickly.

**Form submission** provides an option to send submissions to the server
manually or automatically, with the options of _Wifi only_, _cellular only_,
and _wifi or cellular_. This setting also gives the option to delete finalized
forms and media after being successfully sent to the server.

**Form filling** provides several options for forms and data collection:
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
- Select the icon (circled in K) that is located at the top right of your
  screen.
- Select __Settings__.
- Under the __Project settings__, select __Form management__ and select the
  options relevant for your project.

![Form Management](/images/kobocollect_on_android_advanced/form_management.jpg)

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
href="form_meta.html" class="reference">Form Settings and Meta Questions</a> for
instructions on how to configure set up in <strong>KoBoToolbox</strong>.</p>

- Open __KoBoCollect__.
- Select the icon (circled in K) that is located at the top right of your screen.
- Select __Settings__.
- Under the __Project settings__, select __User and device identity__.
- Under __User and device identity__, select __Form metadata__.

![Form Metadata](/images/kobocollect_on_android_advanced/form_metadata.jpg)

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
2014, __KoBoToolbox__ decided to fork __ODK Collect__ to create the new
__KoBoCollect__, with minimal changes, including the __KoBoToolbox__ server in
the configuration dropdown, a reference back to __ODK Collect__, and the
__KoBoToolbox__ logo and name.
