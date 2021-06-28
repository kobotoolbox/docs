# Dynamic Data Attachment

This support article illustrates how data from one project can be linked dynamically and referenced by another project(s). It also aims to demonstrate some practical examples that this feature supports.

Now that this feature is available with KoBoToolbox, users can do everything that a [pulldata function](pull_data_kobotoolbox.md) does without having to maintain a separate CSV file. The data stored in the survey project (that the user intends to link) acts as a source file. Users could keep collecting data for their source files and simultaneously use them in another survey project(s). Thus, this feature should help users create and manage a longitudinal survey project _(longitudinal data is collected through a series of repeated observations of the same subjects over a short or long period)_. The best part of this feature is that it also works with a shared project where the project admin could also restrict specific permissions while sharing.

Users can now retrieve any information (such as _text_, _integer_, _decimal_, _select_one response_, _select_multiple response_, _GPS points_) to a child project (aka round 2 project) that has already been collected and stored in a parent project (aka round 1 project). However, media information (such as _image_, _audio_, _video_, _uploaded files_, etc.) cannot be retrieved at the moment.

At the same time, users should also be able to perform various calculations such as counting responses entered and stored in a parent project directly through the child project. Similarly, users are also able to compute the _sum_, _maximum_, or _minimum_ value of a particular variable collected and stored in a parent project directly through a child project.

## Linking a project dynamically through xlsform:

While trying this approach through the xlsform, users will require two xlsform. The first xlsform (also known as <a download href="./_static/files/Round 1.xlsx"> parent form or round 1 form</a>) is generally a normal xlsform that we often design. The second xlsform (also known as <a download href="./_static/files/Round 2.xlsx"> child form or round 2 form</a>) is slightly different from the first xlsform, especially in two aspects, i.e., it has an xml-external question type, and it also has a calculation column that holds the path to the survey project being linked. 

Users could design their parent project as shown in the image below:

<Insert image 1 here>

In the same way, users could design their child project as shown in the image below:

<Insert image 2 here>

__Note:__ The name used for the _xml-external_ question type in the child project is crucial for linking the project with the parent project. In the above example, it was named survey. You can give it a different name as well _(it can only consist of Latin characters and numbers)_. 

## Understanding the syntax used under the calculation column of the child project:

The _survey_ used in all of the syntaxes explained below is the name provided for the _xml-external_ question type as already outlined above. Hence, if you accidentally give a different name (other than _survey_) here, your calculation syntax should be invalid.

__count(instance('survey')/root/data[P_Enumerator]):__ Will return users the total count of what was entered in P_Enumerator (parent project).

__count(instance('survey')/root/data[P_Enumerator = current()/../C_Enumerator]):__ Will return users the total count of what was entered in C_Enumerator (child project) matching/comparing with what was entered in P_Enumerator (parent project).

__instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Name:__ Will return users the name (text value) that was entered in P_Name (parent project) located under the P_Demographic group (parent project) when the value entered in C_SN (child project) matches the value entered in P_SN (parent project). The output of this syntax yields the exact result that a pull data function yields.

__instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Age:__ Will return users the age (integer value) that was entered in P_Age (parent project) located under the P_Demographic group (parent project) when the value entered in C_SN (child project) matches the value entered in P_SN (parent project). The output of this syntax yields the exact result that a pull data function yields.

__instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Sex:__ Will return users the sex (select_one choice) that was entered in P_Sex (parent project) located under the P_Demographic group (parent project) when the value entered in C_SN (child project) matches the value entered in P_SN (parent project). The output of this syntax yields the exact result that a pull data function yields.

__instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Family:__ Will return users the family size (integer value) that was entered in P_Family (parent project) located under the P_Demographic group (parent project) when the value entered in C_SN (child project) matches the value entered in P_SN (parent project). The output of this syntax yields the exact result that a pull data function yields.

__sum(instance('survey')/root/data/P_Demographic/P_Family):__ Will return users the total sum of what was entered in P_Family (parent project) located under the P_Demographic group (parent project).

__max(instance('survey')/root/data/P_Demographic/P_Family):__ Will return users the maximum value of what was entered in P_Family (parent project) located under the P_Demographic group (parent project).

__min(instance('survey')/root/data/P_Demographic/P_Family):__ Will return users the minimum value of what was entered in P_Family (parent project) located under the P_Demographic group (parent project).

__instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Language:__ Will return users the language (select_multiple choice) that was entered in P_Language (parent project) located under the P_Demographic group (parent project) when the value entered in C_SN (child project) matches the value entered in P_SN (parent project). The output of this syntax yields the exact result that a pull data function yields.

__instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Location:__ Will return users the GPS location that was entered in P_Location (parent project) located under the P_Demographic group (parent project) when the value entered in C_SN (child project) matches the value entered in P_SN (parent project). The output of this syntax yields the exact result that a pull data function yields.

## Setting up projects for Dynamic Data Attachment:

A project can be dynamically attached in two different scenarios i.e. when _both the projects i.e. parent project, as well as child project, are owned by the same user_ and when _projects are owned by different users_.

### Both Projects Owned by the Same User:

Once a user has finalized their projects in an xlsform, they will need to do the following to set it up so that they could link them dynamically:

__Step 1:__ Upload and deploy the parent project.

<video controls><source src="./_static/files/1. Uploading and deploying xlsform (round 1 survey).mp4" type="video/mp4"></video>

__Step 2:__ Go to the parent project’s __SETTINGS>Connect Projects__. By default, data sharing for a project is disabled. To enable sharing the information with the child project, users will have to toggle the __Data sharing button, changing it to Data Sharing enabled__. Upon pressing the __Data sharing disabled__, users will see a dialogue box. Click __ACKNOWLEDGE AND CONTINUE__. Once the __Data sharing enabled__ button is active, users should be able to __Select specific questions to share__. With this button, users should be able to share or restrict variables with the child project. If you wish to share data from all the variables, you could uncheck __Select specific questions__ to share and proceed. 

<video controls><source src="./_static/files/2. Connect Projects (round 1 survey).mp4" type="video/mp4"></video>

__Step 3:__ Upload and deploy the child project.

<video controls><source src="./_static/files/3. Uploading and deploying xlsform (round 2 survey).mp4" type="video/mp4"></video>

__Step 4:__ Go to the child project’s __SETTINGS>Connect Projects__. Click __Select a different project to import data from__. In the dropdown, you will see the projects that can be linked. __Round 1 Survey__ is listed here because it was made available as outlined in __Step 2__. Once a user selects the available project (_Round 1 Survey_ in my case), a unique name is also provided by the system by default (_round_1_survey_ in my case). Users will now need to be cautious and rename the unique name to the name provided in the _xml-external_ question type while designing the child project. Since I had named it _survey_, I have renamed the unique name from _round_1_survey_ to _survey_. Then press __IMPORT__. Once you press the __IMPORT__ button, you will have an option to share or restrict the variables to your child project. 

<video controls><source src="./_static/files/4. Connect Projects (round 2 survey).mp4" type="video/mp4"></video>

This will now do the magic and link the data from the parent project to the child project. In my case, it will link the data from the _Round 1 Survey_ to the _Round 2 Survey_.

### Projects Owned by Different Users:

Let’s assume a scenario where __userA__ has a parent project which s/he shares with __userB__. Now that this feature is available, __userB__ should be able to upload a child project from his/her user account and link them dynamically with the parent project shared by __userA__. To achieve this at your end, you could follow the steps outlined below: 

__Step 1:__ __userA__ should follow the exact steps as outlined in __Step 1__ and __Step 2__ (__Both Projects Owned by Same User__) to _upload_, _deploy_ and _configure_ the parent project.

__Step 2:__ __userA__ should then share the parent project with userB as outlined in [this support article](managing_permissions.md). While sharing, __userA__ should provide minimum access (_View form_, _Edit form_, _View submissions_, and _Add submissions_) to __userB__ else, __userB__ shall now be able to link the project dynamically as expected.

__Step 3:__ __userB__ will now have to upload, deploy and configure the child project as outlined in __Step 3__ and __Step 4__ (__Both Projects Owned by Same User__). 

## Collecting and managing data with Dynamic Data Attachment:

Both __Collect android app__, and __Enketo__ can be used to collect data for this feature. However, please note that users will need to have at least one submission in the _parent project_ for the _child project_ to function as expected. Similarly, please also be informed that the system takes 5 minutes to sync the parent project's information to the child form. Users if using __Collect android app__ or __Enketo__ (as an offline mode), should frequently download the project to ensure the data is up to date in the _parent project_. If users are using __Collect android app__ and are connected to the internet, the __Collect android app__ could also be configured under the __General Settings>Form management>Blank form update mode>Previously downloaded forms only or Exactly match server__ to automatically update the parent project’s information. This setting could however drain your device’s battery. Hence, be cautious when you are in a situation where you don’t have the option to frequently charge your device.

As a workaround, please see the screenshot of my __DATA>Table__ where I have made some dummy entries to the _parent project_.

<Insert image 3 here>

As I now have some dummy entries for my _parent project_, I am ready to use my _child project_. Please see the screenshot of a survey form (_Round 2 Survey_ in my case) where I am trying to fill it through __Enketo__. Here, you should be able to observe that I am entering only two fields, __Enumerators name__, and __Identification Number__, and the rest is being linked automatically with the parent project.

<Insert image 4 here>
