# Row-Level Permissions
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/4a1fad39555fe7ad3605100e834bc0cfac85a321/source/row_level_permissions.md" class="reference">3 May 2024</a>

Row-level permissions are an extension of the
[existing permissions feature](managing_permissions.md) in KoboToolbox. This feature allows project
owners to assign eight different levels of permissions for a shared project. There are two types of row-level permissions: **user-based** and **condition-based**.

Row-level permissions allow you to set controls for shared projects to determine which users can access submissions, which submissions they have access to, and if they can view, edit, or delete submissions. User-based permissions can be combined with condition-based permissions for even more control of users’ access to shared projects and data.

## Accessing row-level permissions

To use row-level permissions, go to your project **SETTINGS**, click on the **Sharing** section, and click **Add user**.

![image](/images/row_level_permissions/row-level-options.png)

### Available row-level permissions

| [User-based](#user-based-row-level-permissions) row-level permissions                              | [Condition-based](#condition-based-row-level-permissions) row-level permissions                                                                                                                    |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| View submissions only from specific users     | View data based on a condition                                                                 |
| Edit submissions only from specific users     | Edit submissions based on a condition                                                                 |
| Validate submissions only from specific users   | Validate submissions based on a condition                                                               |
| Delete submissions only from specific users | Delete submissions based on a condition |

<p class="note">
    When certain permissions are granted, other permissions are also automatically granted. For example, if a user is granted <strong>Edit submissions only from specific users</strong>, then the user will also be granted the permission <strong>View submissions only from specific users</strong>.
</p>

## Configure your Project Settings for row level permissions

Before you can set user-based row-level permissions for your project, the setting “Allow submissions to this form without a username and password” must be turned off. Data submissions must be associated with usernames to apply user-based row-level permissions.

Learn more about [requiring passwords for accessing Enketo web forms](https://support.kobotoolbox.org/managing_permissions.html#requiring-passwords-for-accessing-enketo-web-forms).

![image](/images/row_level_permissions/Allow_submissions_without_username_password.gif)

## User-based row-level permissions

User-based row-level permissions allow you to share your project data with another KoboToolbox user and permit them to only view, edit, delete, or validate data submitted by specific users.

This can be useful when you need a user to have access to only the submissions they sent. For example, you may want to allow enumerators access to only their own submissions for verification and/or editing. User-based permissions can also be helpful when you want to share data with specific stakeholders and only allow them to access data submitted by specific users.

| User-based row-level permissions                              | Description                                                                                                                    |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| **View submissions only from specific users**     | Users with this permission can **view data** submitted by specific users                                                                 |
| **Edit submissions only from specific users**     | Users with this permission can **edit data** submitted by specific users                                                                 |
| **Validate submissions only from specific users**   | Users with this permission can <a class="reference" href="record_validation.html"><strong>validate data</strong></a> submitted by specific users                                                               |
| **Delete submissions only from specific users** | Users with this permission can **delete data** submitted by specific users |

### To add user-based row-level permissions:
- Open your project and navigate to the **SETTINGS** tab
- Go to the **Sharing** section
- Click **Add user** and enter the username of the user you would like to share the project with and set permissions for
- Select the user-based permissions you want to allow (view, edit, delete, and/or validate)

![image](/images/row_level_permissions/user-based_row-level.png)

- Below each permission, enter the usernames for the users whose submissions you are granting the user access to
- Click **Grant permissions** to save your row-level permissions settings

Once you have saved your permissions, the user you have shared the project with will be able to view, edit, validate, or delete the project data submitted by the specified usernames, depending on which permissions you selected.

<p class="note">
    To ensure data privacy, please make sure to confirm the username of the user you are granting permissions.
</p>

### User-based row-level permissions example

In the example below, the user **kobocourses** is sharing project data with the user **alex**. User-based permissions have been created so user **alex** can only access project data submitted by **alex** and by the user **mario**. These permissions allow **alex** to view, edit, and validate only the data submitted by **alex** and **mario**.

![image](/images/row_level_permissions/user-based-permission-example.png)

## Condition-based row-level permissions

Condition-based permissions allow you to grant access to project data based on a response to a question on your form. When you create a condition-based permission for a user, they will only have access to specific submissions based on the response to a specific question on the form.

This can be useful for managing access to data in shared projects. A condition-based permission allows you to grant permissions to other users based on the conditional **XML value** response submitted to a specific question. For example, if your form includes a question about marital status, you can create a condition-based permission so that the user you are granting permission to only has access to specific submission data if the response is “married”.

| Condition-based row-level permissions                              | Description                                                                                                                    |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| **View submissions based on a condition**     | Users with this permission can **view data** if the response to a question meets the specified condition                                                                 |
| **Edit submissions based on a condition**     | Users with this permission can **edit data** if the response to a question meets the specified condition                                                                 |
| **Validate submissions based on a condition**   | Users with this permission can <a class="reference" href="record_validation.html"><strong>validate data</strong></a> if the response to a question meets the specified condition                                                               |
| **Delete submissions based on a condition** | Users with this permission can **delete data** if the response to a question meets the specified condition |

<p class="note">
    These condition-based row-level permissions are now available for sharing project data. This new feature adds four new levels of permissions to the existing row-level permissions. Previously, row-level permissions only included user-based permissions.
</p>

### To add condition-based permissions:
- Open your project and navigate to the **SETTINGS** tab
- Go to the **Sharing** section
- Click **Add user** and enter the username of the user you would like to share the project with and set permissions for
- Select the condition-based permissions you want to allow (view, edit, delete, and/or validate)
- Below each permission you have selected, choose the question and enter the response condition that must be met

![image](/images/row_level_permissions/condition-based_row-level.png)

- Open the **Select…** drop-down menu to display the full list of form questions and select the question that should be used to filter which submissions are shared with the user
- On the right-hand side of the **equals sign (=)**, enter the response’s conditional **XML value** for the condition that must be met
- Click **Grant permissions** to save your row-level permissions settings

Once you have saved your permissions, the user you have shared the project with will be able to view, edit, validate, or delete project data submissions that have the required response to the specified question, depending on which permissions you selected.

#### Important note:
- For [Date](date_time.md) questions, the response value must be written in the format `YYYY-MM-DD` (e.g., `1974-12-31`).    
- For [Select One](select_one_and_select_many.md) and [Select Many](select_one_and_select_many.md) questions, the response value must be written using the unique XML value, not the label (e.g., `first_grade` rather than `First grade`).

### Condition-based row-level permissions example

In the example below, the user **kobocourses** is sharing project data with the user **kobosouth**. Condition-based permissions have been created so **kobosouth** only has access to data submissions where the `region` indicated by a respondent is `south`.

![image](/images/row_level_permissions/condition-based-region-example.png)

These permissions allow **kobosouth** to view, edit, delete, and validate only the data submissions where the `region` indicated by the respondent is `south`.

![image](/images/row_level_permissions/condition-based-region-example-full.png)

## Troubleshooting:

1. When submitting data, a dialog box requesting user credentials will appear if the authentication requirement is active and the “Allow submissions to this form without a username and password” setting is turned off.

Enter your KoboToolbox username and password. You will be able to submit data to the server if you have **Add submissions** permission for the project.

![image](/images/row_level_permissions/user_authentication.png)

<p class="note">To ensure data security, it is not advised to share your administrator sign in credentials with other users when managing your project. You can create multiple enumerator accounts and share those credentials with your team.</p>

2. If your user-based permissions are not functioning as expected, confirm that the form authentication requirement is active. To confirm this setting is active, open the project and navigate to the **FORM** tab. Under the **Collect data** section, ensure that the “Allow submissions to this form without a username and password” setting is turned off. User-based permissions will not apply to any submissions collected before the “Allow submissions to this form without a username and password” setting was turned off, because these submissions would not be associated with a username.

<p class="note">By default, project settings now require users to sign in to collect submissions. Learn more about <a class="reference" href="managing_permissions.html#requiring-passwords-for-accessing-enketo-web-forms">requiring passwords for accessing Enketo web forms</a>.</p>
