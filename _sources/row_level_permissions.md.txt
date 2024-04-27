# Row-Level Permissions

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/row_level_permissions.md" class="reference">15
Feb 2022</a>

Row-level permissions are an extension of the
[existing permissions feature](managing_permissions.md) in KoboToolbox. The feature allows project
owners to create four different levels of permissions for a shared project. To
find this functionality, simply go to project **SETTINGS** and click on the
**Sharing** section. You will see a screen as shown below.

![image](/images/row_level_permissions/row-level-options.png)

As of August 2021, the management of project permissions has been extended to
allow for a total of four **row-level** access permissions that include:

| Row-level permission                              | Description                                                                                                                    |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| **View submissions only from specific users**     | _View data_ submitted by a subset of defined data entry users.                                                                 |
| **Edit submissions only from specific users**     | _Edit data_ submitted by a subset of defined data entry users.                                                                 |
| **Delete submissions only from specific users**   | _Delete data_ submitted by a subset of defined data entry users.                                                               |
| **Validate submissions only from specific users** | <a class="reference" href="record_validation.html"><i>Validate data</i></a> submitted by a subset of defined data entry users. |

<p class="note">
    Please note that some permissions imply others. For example, if <i>Alice</i> has <strong>Edit submissions only from specific users</strong> only for <i>Bob</i>, then this implies that <i>Alice</i> also has <strong>View submissions only from specific users</strong> for <i>Bob</i>.
</p>

## Configure your Account Settings:

By default, users must be authenticated by entering their KoboToolbox username and password before they can submit data to a deployed form. This is important for row-level permissions to work correctly. To confirm that the form authentication requirement is active, open the project and navigate to the **FORM** tab. Under the **Collect data** section, ensure that the “Allow submissions to this form without a username and password” setting is turned off.

![image](/images/row_level_permissions/Accounts_Settings.png)

## Managing Row Level Permissions:

In this example, three user accounts are presented to demonstrate how the
feature works. _kalyan1_ represents the _admin_ or _owner_ of the survey project
(as seen in the previous images). _kalyan2_ and _kalyan3_ represent different
users receiving permissions. **Require authentication to see forms and submitted
data** has been checked for _kalyan1_.

### View submissions only from specific users:

_kalyan1_ can share row-level permissions with _kalyan2_, where they can _view_
submissions made from _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/1_View_submissions_1.mp4" type="video/mp4"></video>

Row-level permissions can also be set for _kalyan3_ such that they can only
_view_ submissions made by _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/2_View_submissions_2.mp4" type="video/mp4"></video>

### Edit submissions only from specific users:

In this case, _kalyan1_ can share row-level permissions with _kalyan2_, where
they can _view_ and _edit_ submissions made from _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/3_Edit_Submission_1.mp4" type="video/mp4"></video>

As with view permissions, the same can be done for _kalyan3_ to only _view_ and
_edit_ submissions from _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/4_Edit_Submission_2.mp4" type="video/mp4"></video>

### Delete submissions only from specific users:

In this case, _kalyan1_ can share row-level permissions with _kalyan2_, where
they can _view_ and _delete_ submissions made from _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/5_Delete_Submissions_1.mp4" type="video/mp4"></video>

The same can be done for _kalyan3_ to only _view_ and _delete_ submissions from
_kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/6_Delete_Submissions_2.mp4" type="video/mp4"></video>

### Validate submissions only from specific users:

In this case, _kalyan1_ can share row-level permissions with _kalyan2_ where
they can _view_ and _validate_ submissions made from _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/7_Validate_Submissions_1.mp4" type="video/mp4"></video>

The same can be done for _kalyan3_ to only _view_ and _validate_ submissions
from _kalyan2_.

<video controls><source src="./_static/files/row_level_permissions/8_Validate_Submissions_2.mp4" type="video/mp4"></video>

## Troubleshooting:

### Scenario 1:

You may come across this dialogue box _(as shown in the image below)_ when
submitting data with the **Require authentication to see forms and submitted
data** option checked in KoboToolbox.

![image](/images/row_level_permissions/Login.png)

Enter your KoboToolbox login credentials and, if the account has **Add
submissions** permission, you will be able to submit data to the server.

<p class="note">Note that it’s advised not to share your admin login credentials when managing your project for data security. You can create multiple enumerator accounts and share those credentials with your team.</p>

### Scenario 2:

To set the _view_, _edit_, _delete_ and _validate_ row-level permissions
correctly on submissions from a subset of users, the **Require authentication to
see forms and submitted data** option must be checked _before_ data is
collected. Otherwise only data collected after this option is checked will be
restricted as expected.
