# Collecting Data with KoBoCollect on Android

Data for KoBoToolbox can be collected using two different approaches, viz. [_collecting data through web forms (Enketo)_](data_through_webforms.md) and _collecting data through KoBoCollect_. This article describes collecting data with KoBoCollect Android App.

Any modern Android device should support KoBoCollect. It is free, and the latest version of the app can be installed directly through [Google Play Store]( https://play.google.com/store/apps/details?id=org.koboc.collect.android). Alternatively, an appropriate version can be installed compatible with the device's operating system through our [GitHub repository] (https://github.com/kobotoolbox/collect/releases). We, however, strongly recommend users install the latest version of the app as it should be bugs-free and should also support the latest features compatible with KoBoToolbox. 

#### Setup Server URL on KoBoCollect

After installing the app on the device, users will need to configure it with the user's KoBoToolbox account. 

* Open __KoBoCollect__.
* Open __General Settings__ (this may be at the top right of your screen, the bottom right, or at the button in the center, depending on your Android version). Then select __Server__.
![image](/images/kobocollect_android/kobocollect_android_1.png)
* Users are now able to configure the __URL__, __Username__, and __Password__ from the __Server Settings__. Under __URL__, enter the server `https://kc.kobotoolbox.org` or `https://kc.humanitarianresponse.info` _(depending upon the used server)_. Under the __Username__, _enter account username_ and under the __Password__, _enter account password_.
![image](/images/kobocollect_android/kobocollect_android_2.png)
__Note:__ A device may sometimes have trouble connecting to the server if the device date and time are incorrect. To learn more about troubleshooting, please feel free to go through our support article [Troubleshooting KoBoCollect Android Application]( troubleshooting_kobocollect.md).

#### Getting Blank Forms in KoBoCollect

Follow the steps mentioned below to get blank survey forms to the app. 

* Make sure that users have successfully deployed at least one project through the user's KoBoToolbox account.
* Make sure that users have set up the URL as mentioned above.
* Make sure that the device is connected to the internet securely.
* Select __Get Blank Form__ from the home menu.
![image](/images/kobocollect_android/kobocollect_android_3.jpg)
* A list of all the deployed survey forms should appear. Press __Select All__ to have all the survey forms to the app or select the ones manually and then press __Select All__. Then press __Get Selected__.
![image](/images/kobocollect_android/kobocollect_android_4.jpg)

#### Collecting Data in KoBoCollect

Once the blank forms are in the app, users no longer require an internet connection to collect data. The blank forms and the filled-up forms should stay on the device until they are deleted or submitted to the server. 

Follow the steps mentioned below to start collecting data using the app. 

* Press __Fill Blank Form__ from the home menu.
* Select the survey form to start collecting data.
* Go through all the questions (swiping your finger from right to left).
* At the end of the survey, press __Save Form and Exit__. _Make sure the form is marked as **'finalized'**. If this is unchecked and still press Save Form and Exit, the filled-up form goes to **Edit Saved Form** while it does not go to **Send Finalized Form**. In such a scenario, go back to **Edit Saved Form**, open the form and then press **Go To End** and press **Save Form and Exit**, making sure the form is marked as **'finalized'**. Generally, when finished collecting data and when the form is marked as **'finalized'** and pressed **Save Form and Exit**, the saved form simultaneously goes to **Edit Saved Form** and **Send Finalized Form**._ 
![image](/images/kobocollect_android/kobocollect_android_5.png)
Users could also change the name of the saved form to the desired name under __Name this form__ if they think data collection has not been completed and requires another visit with the respondent. Changing the completed form's name would make the enumerator easy to spot which form to edit from the __Edit Saved Form__.

#### Editing Data in KoBoCollect

Once users have completed collecting data by pressing __Save Form and Exit__, the saved form automatically goes to __Edit Saved Form__. If users need to edit this saved form, follow the steps outlined below. 

* Press __Edit Saved Form__ from the home menu.
* Users should see a list of __Saved Forms__. Choose the one that needs correction. 
* Make changes as needed, and then press __Save Form and Exit__. 
* Repeat the process multiple times if more corrections are required.

#### Uploading Finalized Data to the Server

Users should now need an internet connection at this phase to upload their finalized forms to the server. Follow the steps mentioned below to upload the collected data to the KoBoToolbox server (your KoBoToolbox account).

* Ensure the device with the completed forms is securely connected to the internet.
* From the home screen, press on __Send Finalized Form__.
* A list of all the collected forms should appear.
* Press __Select All__ (or select the ones you wish to upload) and then press __Send Selected__.
* To ensure the forms were uploaded successfully, press __View Sent Form__. Users should be able to view all the submitted forms.

#### Deleting Saved Forms in KoBoCollect

Once all the filled-up forms are submitted, users could delete __Saved Forms__ and __Blank Forms__ from the app to not mix up with other ongoing projects or future projects. Follow the steps outlined to delete these forms from the app. 

* From the home screen, press on __Delete Saved Form__.
* Users should now see two tabs. The default is __Saved Forms__. These are the forms that were filled-up while collecting data. Press __Select All__ to delete all the __Saved Forms__ from the app and then press __Delete Selected__. 
![image](/images/kobocollect_android/kobocollect_android_6.png)
* The next tab is the __Blank Forms__. These are the blank questionnaire or, in other words, the questionnaire to the survey project that a user deployed through their KoBoToolbox account. Press __Select All__ to delete all the __Blank Forms__ from the app and then press __Delete Selected__.

#### Resetting View Sent Form from KoBoCollect

When a user submits all the filled-up forms to the server by pressing __Send Finalized Form__, the user should be able to confirm that the submitted forms have reached the server if they see them in the __View Sent Form__ (i.e., once you submit them, they are also seen in the __View Sent Form__). Data managers generally advise users to keep this information until the end of the project as it always provides the user with reference on the total number of collections and submissions. 

However, once the project's data collection is over, it is advised to reset __View Sent Form__ from the app as it may create confusion with the total number of completed cases sent to the server. Hence, to avoid this confusion, please follow the steps to reset __View Sent Form__ from the app as follows:

* Open the __Admin Settings__ (this may be on the top right, the bottom right, or in the bottom center of your screen, depending on your Android version).
![image](/images/kobocollect_android/kobocollect_android_7.png)
* Select __Reset application__.
* Check on __Saved forms (instances folder, instances database)__ and then press __RESET__. Users should further see a small dialogue box pop up __Reset results Saved forms::Success__. Then press __OK__.

#### Hiding Buttons in KoBoCollect

It is sometimes necessary to hide some buttons so that enumerators do not manipulate the collected data or play around, which increases the risk of data loss. Hence, to avoid this pitfall follow the instructions outlined below.

* Open the __Admin Settings__ (this may be on the top right, the bottom right, or in the bottom center of your screen, depending on your Android version).
* At the bottom, users should see the __User Access Control__, which includes __Main Menu Settings__, __User Settings__, and __Form Entry Settings__.
* Select __Main Menu Settings__ to hide the button from the main menu.
![image](/images/kobocollect_android/kobocollect_android_8.png)
* Select __User Settings__ to hide the button from the user settings menu.
![image](/images/kobocollect_android/kobocollect_android_9.png)
* Select __Form Entry Settings__ to hide the button from the form menu.
![image](/images/kobocollect_android/kobocollect_android_10.png)
* After making changes, do not forget to set an __Admin Password__ so that enumerators would not access the __Admin Settings__.
![image](/images/kobocollect_android/kobocollect_android_11.jpg)

#### Differences Between KoBoCollect & ODK Collect

__KoBoCollect__ is a fork of the excellent __ODK Collect__. As of today, there are no substantive differences between the two apps. Users are free to use either one for their data collection. KoBoToolbox's online features are fully compatible with both apps. So technically, there should be no advantage of one over the other. 

We, however, do not recommend having both apps installed concurrently. Installing both apps on the same device could lead to some confusion depending on the Android settings. 

Historically there used to be some significant differences between the two. Back in 2009, KoBoToolbox made several significant changes to __ODK Collect__ that became __KoBoCollect__. That included _cascading questions_, _hiding delete and edit buttons_ for field data collection, and other changes. That was in part because XLSForm was not yet an option, and KoBoToolbox built a form builder for all question types and advanced settings, including cascading questions, which were saved directly as an XML file for the mobile app. These changes were eventually added to __ODK Collect__ over the years, along with many other great features. So, in 2014, KoBoToolbox decided to re-fork __KoBoCollect__ off __ODK Collect__, keeping only minimal changes. Today these include the _KoBoToolbox server in the configuration dropdown_, a reference back to __ODK Collect__, and the _KoBoToolbox logo and name_. 

KoBoToolbox updates __KoBoCollect__ periodically. Interested users could find the source code [here]( https://github.com/kobotoolbox/collect/releases). There are tens of thousands of __KoBoCollect__ users worldwide; hence, KoBoToolbox has not planned to discontinue __KoBoCollect__ at this point. Nevertheless, if a user is starting a new project, one could very well start with __ODK Collect__. One advantage in starting with __ODK Collect__ is that the app is updated more frequently than __KoBoCollect__ hence receiving bug fixes more quickly.
