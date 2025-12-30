# Library locking with XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/2885694527f2b8ce0e6f49925b6b5d3397109769/source/library_locking.md" class="reference">18 Dec 2025</a>

The [KoboToolbox library](https://support.kobotoolbox.org/question_library.html) allows you to store and manage templates, questions, and blocks for reuse across multiple projects. **Form templates in the library** can be shared with team members to ensure consistent form design and reduce duplication of effort.

**Library locking** expands on this by allowing you to control how templates can be edited once they are used to create new projects. With locking, you can specify which questions, groups, or form-level settings can be changed. This is especially useful for large teams working from a shared template, where certain elements need to remain fixed while others can be adapted to local needs.

This article explains how library locking works, the types of restrictions you can apply, how to configure them in XLSForm, and how to upload locked XLSForms to KoboToolbox.

<p class="note">
<strong>Note:</strong> Library locking is not currently supported in the KoboToolbox Formbuilder. To use this feature, you must implement it via XLSForm and then upload your XLSForm to KoboToolbox. 
<br><br>
To learn more about downloading and editing your form as XLSForm, see <a href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Using XLSForm with KoboToolbox</a>.    
</p>

## Introduction to library locking

Library locking controls how much of a form **can be edited** when a project is created from a library template. Restrictions are defined in your XLSForm before uploading the form.

When you create a locked template and share it through your library:
- Users can make local adjustments where restrictions allow.
- Locked elements appear **grayed out** in the Formbuilder.
- A message above the form indicates which restrictions are active.

Library locking is separate from [project permissions](https://support.kobotoolbox.org/managing_permissions.html), which control what different users can do inside a deployed project.

<p class="note">
<strong>Note:</strong> Library locking restrictions apply only in the <strong>Formbuilder</strong> when a project is created from a locked template. If the XLSForm is downloaded and edited in a spreadsheet, the restrictions will not prevent changes. However, incorrect or invalid locking configurations may cause errors when the form is re-uploaded.
</p>

Library locking is configured in three XLSForm worksheets:
- **survey worksheet:** To apply restrictions to specific questions and groups.
- **settings worksheet:** To apply form-level restrictions and set the `kobo--lock_all` option.
- **kobo--locking-profiles worksheet:** To define profiles that group related restrictions. 

Together, these worksheets let you define which parts of a form remain fixed and which parts can be edited when the template is used to create new projects.

## Types of restrictions

Library locking supports restrictions at three levels: **question**, **group**, and **form**. Restrictions define what can and cannot be edited when a project is created from a locked template.

In addition, a global setting (`kobo--lock_all`) can be used to lock the entire form.

### Question-level restrictions

Question-level restrictions apply to individual questions. You can apply the following restrictions to questions in your XLSForm:
| Restriction              | Description                                                                      |
|:------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <code>choice_add</code>                 | Prevents adding new choices to a **select** question.                                                             |
| <code>choice_delete</code>              | Prevents deleting existing choices in a **select** question.                                                      |
| <code>choice_value_edit</code>          | Prevents editing a choice name (or XML value).                                                                |
| <code>choice_label_edit</code>          | Prevents editing a choice label.                                                                              |
| <code>choice_order_edit</code>          | Prevents reordering choices in a **select** question.                                                             |
| <code>question_delete</code>            | Prevents deleting a question.                                                                                 |
| <code>question_label_edit</code>        | Prevents editing a question label or hint.                                                                    |
| <code>question_settings_edit</code>     | Prevents editing question settings, including the question name. This does not include skip logic or validation criteria. |
| <code>question_skip_logic_edit</code>   | Prevents editing skip logic conditions.                                                                       |
| <code>question_validation_edit</code>   | Prevents editing validation criteria.                         |

### Group-level restrictions

Group-level restrictions apply to [question groups](https://support.kobotoolbox.org/grouping_questions_xls.html). You can apply the following restrictions to groups in your XLSForm:

| Name | Description |
|:------|:-------------|
| <code>group_delete</code> | Prevents deleting a group. |
| <code>group_split</code> | Prevents ungrouping questions. |
| <code>group_label_edit</code> | Prevents editing the group label. |
| <code>group_question_add</code> | Prevents adding or cloning questions inside a group. |
| <code>group_question_delete</code> | Prevents deleting questions from within a group. |
| <code>group_question_order_edit</code> | Prevents reordering questions inside a group. |
| <code>group_settings_edit</code> | Prevents editing group settings, including the group name. This does not include skip logic. |
| <code>group_skip_logic_edit</code> | Prevents editing skip logic for a group. |

### Form-level restrictions

Form-level restrictions apply to the whole form. You can apply the following restrictions to your XLSForm:
| Name | Description |
|:------|:-------------|
| <code>form_appearance</code> | Prevents changes to the form [theme](https://support.kobotoolbox.org/form_style_xls.html). |
| <code>form_replace</code> | Prevents replacing the form in KoboToolbox using the <i class="k-icon k-icon-replace"></i> **Replace Form** option. |
| <code>group_add</code> | Prevents creating new groups. |
| <code>question_add</code> | Prevents adding or cloning questions in a group. |
| <code>question_order_edit</code> | Prevents reordering questions. |
| <code>language_edit</code> | Prevents editing translations. |
| <code>form_meta_edit</code> | Prevents editing [metadata](https://support.kobotoolbox.org/metadata_xls.html) questions. |

### Locking an entire form

The `kobo--lock_all` setting can be added to the **settings** worksheet of your XLSForm.
- If set to **TRUE**, the entire form is locked and all granular restrictions become redundant.
- If set to **FALSE** (or omitted), only the restrictions defined in your locking profiles are applied.

**settings worksheet**

|   kobo--lock_all       |
|:----------------- |
|   TRUE  |
| settings | 

## Configuring library locking in XLSForm

### Defining locking profiles

Locking profiles are **sets of restrictions** that can be applied to questions, groups, or the whole form. They are defined in the **kobo--locking-profiles** worksheet of the XLSForm, and then applied in the **survey** and **settings** worksheets. You can create as many profiles as you need.

To define locking profiles in your XLSForm:
1. Create a new worksheet named **kobo--locking-profiles.**
2. Add a **restriction** column, which can include any restrictions from the tables above.
3. Create one column per **profile**  (e.g., `profile_1`, `profile_2`). 
4. In the cell corresponding to a **restriction** and a **profile**, include the keyword `locked` to assign a restriction to a profile.

**kobo--locking-profiles worksheet**

| restriction         | profile_1 | profile_2 | profile_3 |
|:-------------------|:----------|:----------|:----------|
| choice_add          | locked    | locked    |           |
| choice_delete       |           | locked    |           |
| choice_value_edit   | locked    | locked    |           |
| choice_label_edit   |           | locked    |           |
| choice_order_edit   |           | locked    |           |
| question_delete     | locked    | locked    |           |
| form_appearance     |           |           | locked    |

### Applying profiles in the survey worksheet

Once you have defined locking profiles in the **kobo--locking-profiles** worksheet, you can apply these profiles to specific questions and groups. To apply profiles in the `survey` worksheet:

1. Create a column named **kobo--locking-profile** in the `survey` worksheet
2. For each question or group you want to restrict, define the locking profile in the `kobo--locking-profile` column.

**survey worksheet**

| type                     | name    | label              | kobo--locking-profile |
|:-------------------------|:--------|:------------------|:--------------------|
| select_one country        | country | Select your country | profile_1           |
| select_one city           | city    | Select your city   | profile_2           |
| survey | 

### Applying profiles in the settings worksheet

In addition to applying profiles to questions and groups in the `survey` worksheet, you can also apply a profile with form-level restrictions in the `settings` worksheet.

To apply a profile to the `settings` worksheet:
1. Create a **kobo--locking-profile** column in the `settings` worksheet.
2. Specify the profile that you would like to apply.

**settings worksheet**

| kobo--locking-profile |
|:---------------------|
| profile_3            |
| settings | 

<p class="note">
<strong>Note:</strong> Restrictions cannot be applied in the <code>choices</code> worksheet. All choice-related restrictions are defined at the question or group level in the <code>survey</code> worksheet.
</p>

## Using locked templates in KoboToolbox

Once you have created and uploaded a locked XLSForm as a template, you can use it to build new projects in KoboToolbox.

### Importing a locked XLSForm into your library

To import a locked XLSForm into your library:
1. Go to the <i class="k-icon k-icon-library"></i> **Library** from the left menu bar in KoboToolbox.
2. Click **NEW**, then select **Upload**.
3. Upload your XLSForm file, and select **Upload as template.**

![Upload template](images/library_locking/upload_template.png)

The template will appear in your library with a <i class="k-icon k-icon-template-locked"></i> **lock symbol**, showing that it contains restrictions.

### Creating a project from a locked template

1. Go to the **Projects** home page.
2. Click **NEW**, then select **Use a template.**
3. Choose the locked template you want to use.
4. Continue creating your project as usual.

![Use template](images/library_locking/use_template.png)

When you open the project in the Formbuilder:
- A message will appear above the first question summarizing restrictions.
- Locked questions, groups, or form-level settings will appear **grayed out.**
- Each locked question shows which profile has been applied in its **Settings > Locked Features.**

![Locked library](images/library_locking/locked.png)

## Troubleshooting

<details>
  <summary><strong>Troubleshooting recommendations</strong></summary>
  If library locking does not work as expected, try the following:
    <ul>
  <li>Make sure the form was uploaded as a <strong>Template</strong> in the library.</li>
  <li>Check the <strong>settings</strong> worksheet in your XLSForm. If <code>kobo--lock_all</code> is set to <code>true</code>, the whole form will be locked.</li>
  <li>Verify that all restriction names in the <code>kobo--locking-profiles</code> worksheet are valid. Only predefined restriction names are supported.</li>
  <li>Ensure that the column <code>kobo--locking-profile</code> exists in the <strong>survey</strong> or <strong>settings</strong> worksheet and that the profile names match those defined in the <code>kobo--locking-profiles</code> worksheet.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Caveats and limitations</strong></summary>
  <ul>
  <li>Restrictions are enforced only in the <strong>Formbuilder.</strong> If the XLSForm is downloaded and edited directly in a spreadsheet, restrictions do not prevent changes.</li>
  <li>Restrictions apply only to projects created from locked templates. Templates and surveys in the library remain editable.</li>
  <li>Only surveys and templates support locking. If you upload a locked XLSForm as a question or block, the locking is ignored.</li>
  <li>Some spreadsheet editors automatically convert two single dashes <code>--</code> into a long dash (—). Always use two single dashes in names such as <code>kobo--locking-profiles</code>.</li>
</ul>

</details>



