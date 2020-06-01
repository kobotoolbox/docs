# Collecting Data with KoBoCollect on Android

KoBoCollect is KoBoToolbox's data collection app and can be installed on any Android phone or tablet through the Google Play Store. To install the app on your Android device, [click here](https://play.google.com/store/apps/details?id=org.koboc.collect.android).

To get help troubleshooting common issues, please refer to [this article](https://support.kobotoolbox.org/en/articles/592367-troubleshooting-kobocollect-android-application).

To learn how to get started with KoBoCollect, follow the steps and tips below:

**1. Setup server URL on KoBoCollect**

After installing KoBoCollect, you need to configure it so that it can be used together with your KoBoToolbox account for data collection.

![image](/images/kobocollect_android/server_url.jpg)

1. Open KoBoCollect on your device.

2. Find **General Settings** by clicking on the three dot icon on the upper right side of the screen, then click on Server.

3. In the Server Settings, under URL, enter the server URL https://kc.kobotoolbox.org or https://kc.humanitarianresponse.info (depending on which server you use)

4. Then enter your username and password

.. image:: /images/kobocollect_android/login.jpg

*Note: Sometimes devices will have trouble connecting to the server if the device date and time is not correct.*

**2. Download blank forms from your account**

To download forms from your account and start data collection, follow these steps:

1. Make sure you are connected to the internet on your device and you have deployed at least one project in KoBoToolbox.

2. On the home screen menu of KoBoCollect, select **Get Blank Form**

3. A list of all your forms from your different projects will be shown. Click **Select All** (or select the ones you wish to download), then click **Get Selected**.

.. image:: /images/kobocollect_android/blank_form.jpg

**3. Collect data through filling blank forms**

At this point, you no longer need an internet connection. The blank forms and the following submissions will stay on your device until you regain internet connection and send the data submissions to the server. 

1. Back in the main home screen, select **Fill Blank Form**.

2. Select the form you wish to fill out and enter data. 

3. Now you may go through and start answering all the questions (swiping your finger from right to left)

4. When you reach the end of the form click on **Save Form and Exit** (making sure the form is marked as 'finalized')

.. image:: /images/kobocollect_android/save_exit.jpg

**4. Uploading finalized data to the server**

After you have completed forms, follow these steps to upload the collected data to your KoBoToolbox account and server. 

1. Make sure you are connected to the internet on your device.

2. From the home screen, click on **Send Finalized Form**

3. A list of your most recently collected forms appears.

4. Click **Select All** (or select just the ones you wish to send), then click **Send Selected**.

**Additional Tips:**

**Editing data in KoBoCollect**

Once you have completed filling out forms, its possible to edit and make corrections to the submitted data in KoBoCollect before sending them to the server. 

1. Select **Edit Saved Form** on the home screen of KoBoCollect.

2. You will see a list of Saved Forms. Choose the one that you wish to make corrections to.

3. Make changes as needed and then press **Save Form and Exit**. 

4. Repeat the process if you wish to make corrections to multiple Saved Forms. 

**Deleting Forms in KoBoCollect**

Once you have completed all of your data collection for a specific project and have submitted all the saved forms to your KoBoToolbox server, it's recommend to delete the Blank Forms and Saved Forms from KoBoCollect so that enumerators will not get mixed up when collecting data for other projects. To do this, select **Delete Saved Form** from the home screen. 

**Resetting View Sent Forms in KoBoCollect**

When you've submit completed forms from KoBoCollect to the KoBoToolbox server by clicking **Send Finalized Form**, you should be able to confirm that your submitted forms have reached the server by seeing them in the **View Sent Form** page. It can be nice to have them there until the end of data collection for a specific project, as it gives you the reference of how many data submissions have been sent to the server form that particular device. However, once the data collection for the project is over, it is recommended to reset **View Sent Form** from KoBoCollect as it may create confusion with the total number of completed submissions sent to the server in future projects. 

To reset **View Sent Form** from KoBoCollect follow these steps:

1. Open the **Admin Settings** by clicking on the **three dot icon** on the top right of the screen. 

2. Select **Reset application**... 

3. Check the box for **Saved forms (instances folder,instances database)** and then press **RESET**. When you see **Saved forms::Success**, then press OK.

**Hiding buttons and options within KoBoCollect**

It’s sometimes necessary to hide buttons within KoBoCollect to limit the activity and capabilities of enumerators in the app. You're able to hide many of the buttons available in KoBoCollect through the Admin Settings.

1. On the home screen click the **three dot icon** and select **Admin Settings**

2. At the bottom you will see the **User Access Control** which includes **Main Menu Settings**, **User Settings** and **Form Entry Settings**.

3. Select the buttons you would like to hide from the different screens. If you set an admin password, your enumerators won't be able to access the **Admin Settings** to change access to these buttons.
