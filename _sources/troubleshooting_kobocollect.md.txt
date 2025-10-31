# Troubleshooting KoboCollect Android Application
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/troubleshooting_kobocollect.md" class="reference">31 Oct 2025</a>


**-- Kindly report any uncovered issue on our
[community forum](https://community.kobotoolbox.org/)--**

<p class="note">
    To learn more about connecting KoboCollect to your KoboToolbox account, configuring KoboCollect settings, and collecting data with the app, see <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">Getting started with KoboCollect</a>, <a href="https://support.kobotoolbox.org/kobocollect_settings.html">Customizing KoboCollect settings</a> and <a href="https://support.kobotoolbox.org/data_collection_kobocollect.html">Data collection using KoboCollect</a>.
</p>


_Common error messages with troubleshooting guides:_

**Error: Message 'Error getting form list' after selecting 'Download form'**

**Troubleshooting:** The most likely solutions for this problem is either

1. Check your URL, you most likely have a small typo in the URL you entered into
   the settings. Refer to [this article](kobocollect_on_android_latest.md) on setting up
   your android phone/tablet for data collection.

2. Another possible explanation is that your phone wasn't connected to the
   Internet when you selected **Download form**, for example when you are
   connected to a WiFi network in a public place that requires you to sign in
   through your browser. [This article](kobocollect_on_android_latest.md) discusses in
   greater detail how to connect your device with your account.

**Error: Generic Exception: No peer certificate or Form listing failed. Error:
javx.net.ssl.SSLPeerUnverifiedException...**

This error appears when KoboCollect tries to communicate with the server but
can't establish a secure (SSL/HTTPS) connection.

**Troubleshooting:**

1. Highly likely your device is using the wrong date. Check that the date is
   correct, then try again. _Please refer to your phone/tablet manual on how to
   set the date._ Android devices reset their dates to 2000 or another year if
   ever the battery goes to 0%, which is why this error can appear frequently if
   your team has a tendency to drain the battery all the way.

2. You may also see this error message if you are using a WiFi hotspot that
   requires you to sign in after connecting.

**Error: KoboCollect has crashed**

**Troubleshooting:**

1. If this **occurs** while you are trying to **upload submissions or download a
   new form**, then your device has a significant interruption in its Internet
   connection. Although it sounds alarming, it is harmless: Simply repeat the
   upload or download process.

2. If this **occurs** while you are trying to **open a new form** in your phone,
   then the following possible reasons could help you resolve:

    - The form you are trying to open has errors either in the calculate,
      constraints or skip routines. This is rare since the system would have
      already checked for the errors.
    - The form your are trying to open is either too large or has numerous
      actions (calculations, large list of responses or other complex
      procedures) which cannot be handled by the memory capacity of your device.
      Kindly refer to [this article](devices_for_data_collection.md) on
      recommended devices.

**Error: Unable to edit this blank form because the corresponding blank form is
not present or was deleted**

**Troubleshooting:**

This type of error message occurs when you try to edit your saved form when the
corresponding blank form is not present or was deleted.

If this occurs, retrieve the corresponding blank form from your KoboToolbox
account by clicking **Download form** on the home screen and then select the
particular form which requires amendments.

**Error: Unable to install KoboCollect android app in a device. Shows the
following error message (can’t create directory/storage/sdcard0/odk)**

**Troubleshooting:**

You see this error message when your device is out of storage space. To overcome
this issue, free your device by uninstalling some unnecessary app and then try
installing KoboCollect.
