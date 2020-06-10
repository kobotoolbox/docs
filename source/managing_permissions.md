# Managing permissions

**Learn how to grant various permissions for other users to collaborate on your projects**

KoBoToolbox allows giving different permission levels to a data collection project. While most users may only use a single user to manage, access, and enter data for a given project, sometimes more complex scenarios require different levels of access.

**Requiring passwords for accessing forms**

By default KoBoToolbox only requires a username and password for accessing data and managing your projects. Forms can be accessed by anyone who knows the respective URL. To require users to log in to access your forms, go to Settings inside your online account and check the '**Require authentication to see forms and submit data**' box. (*Note: currently requiring authentication can only be set globally for all the projects in your account and not just for individual projects.*)


![image](/images/managing_permissions/account_settings.jpg)

![image](/images/managing_permissions/user_permissions.jpg)


**Setting project-specific user permissions**

![image](/images/managing_permissions/proj_permissions.jpg)

To control project sharing permissions go to the *Sharing* tab in the *Settings* page in your data collection project, enter the username of the user who should get new permissions, select the permission level checkbox, then click GRANT PERMISSIONS. The available permissions are: 

* View Form 
* Edit Form 
* View submissions
* Add Submissions
* Edit and Delete Submissions
* Validate Submissions

Some permissions automatically grant other permissions. Example: If a user is granted 'Add Submissions' they will also be able to 'View Form'. 

To copy a team and their associated permissions from another project, click on the link at the bottom of the page. Clicking the link will overwrite any existing settings already defined in the current project. 

**Assigning 'Add Submissions' rights for specific users**

You might want to use one or more users other than your own account to collect data. For example, you created a form and project but have three enumerators in the field, who should only be able to submit data but not access the collected information. Assuming you created your data collection project with username1 and want to share it with username2, username3, and username4:

**In the online platform:**

* Sign up with the separate users needed for the field, i.e. username2, username3, and username4. Each one needs to be activated but can all point to the same email address.
* Sign back in to your own account (username1). Go to the Project that you want to allow others to submit to.
* Open the Settings page, and under ADD USER type in 'username2', then select 'Add Submissions' and click GRANT PERMISSIONS.
* Repeat the last step for each user.

**In KoBoCollect:**

* Under General Settings in the URL field enter [https://kc.kobotoolbox.org](https://kc.kobotoolbox.org) or [https://kc.humanitarianresponse.info](https://kc.humanitarianresponse.info) as applicable (don't include the username)
* Then enter the username and password for the user who will use the handset (e.g. username1).

**Advanced View Submissions permission settings**

To set permissions for a user to view only data submitted by a subset of specified users or view data submitted only by themselves, please visit our [Row-Level Permissions](https://support.kobotoolbox.org/en/articles/3345421-row-level-permissions) article to learn more. 

**A Project owner can give a “Validate Submissions” permission to other users.**

Users with this permission can view a record, edit it if necessary, and assign a status to the record in question. Assigning a status to a particular record/submission raises data collection standards for teams with more than one enumerator.

* The validation status labels available include:
    * On Hold: Record is under review.
    * Approved: The data within this record is accurate.
    * Flagged for Removal: The data within this record should be removed from the data set.

More on "Validate Submissions" can be [found here](record_validation.md).
