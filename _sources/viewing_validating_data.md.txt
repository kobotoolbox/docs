# Viewing and validating your data
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/d9b44de6b0f7192771a9f7bf86edf271321f398b/source/viewing_validating_data.md" class="reference">27 Jan 2026</a>

<iframe src="https://www.youtube.com/embed/X5W6nv9gYUo?si=n3eniC0Uq_PzFsbT" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

The **Table** view in the **DATA** section of your KoboToolbox project provides a complete and customizable overview of all project submissions. By default, all records are shown, with the most recent submissions listed first. This view is the primary workspace for exploring data, monitoring data quality, validating submissions, and making edits.

This article explains how to:

- Configure the data table in the **Table** view
- Filter and sort your data
- View and validate submissions

<p class="note">
To learn more about making changes to your data, see <a href="https://support.kobotoolbox.org/editing_deleting_data.html">Editing and deleting your data</a>. 
</p>

Project owners can control data access by assigning separate permissions to view, edit, validate, and delete submissions. For example, they can allow some team members to view and validate data while restricting editing and deletion permissions.

<p class="note">
To learn more about user-level permissions for viewing, validating, and editing data, see <a href="https://support.kobotoolbox.org/managing_permissions.html">Sharing projects with user-level permissions</a>.
</p>

## Configuring the data table

The data table in the **Table** view displays all submissions and data fields by default. In many projects, a more focused view is needed. Adjusting what appears in the table helps you work more efficiently, especially for forms with many questions or nested groups. You can choose which fields to display and how data is shown to better match your workflow.

![Choose fields to display in data table](images/viewing_validating_data/table_view.png)

### Customizing the data table

Above the data table, you can configure the following settings:

- **Hide fields:** Click <i class="k-icon-qt-hidden"></i> **hide fields** to view a list of all questions and fields in your form. All fields are selected by default. Clear the checkbox for any field you want to hide, then click Apply to save your changes.
- **Toggle fullscreen:** Click <i class="k-icon-expand"></i> **Toggle fullscreen** to expand the data table to fill the browser window.
- **Display options:** Click <i class="k-icon-settings"></i> **Display options** to control how labels, groups, and HXL tags are shown in the table. The following display options can be configured:

| Display option                 | Description                                                                                  |
|:-------------------------------|:---------------------------------------------------------------------------------------------|
| Display labels or XML values?  | Choose whether to show <a href="https://support.kobotoolbox.org/glossary.html#xml-value">XML values</a> or full question and choice labels in <a href="https://support.kobotoolbox.org/collecting_data_multiple_languages.html">any form language</a> in your table. |
| Show group names in table headers | Decide whether column headers in the table include the name of the question group (e.g., `demographics / age`). |
| Show HXL tags                  | Display <a href="https://support.kobotoolbox.org/hxl.html">Humanitarian Exchange Language</a> (HXL) tags if they were added to your form.           |

Within the data table, you can click a column header and select <i class="k-icon-qt-hidden"></i> **Hide field** to remove fields you do not need, or <i class="k-icon-freeze"></i> **Freeze field** to keep frequently used fields visible while you scroll.

<p class="note">
<strong>Note:</strong> These settings affect the <strong>Table</strong> view for all project users.
</p>

### Navigating the data table

You can change how many rows are shown per page using the dropdown at the bottom of the table. By default, the table displays 30 rows.

<p class="note">
<strong>Note:</strong> Displaying many rows at once can slow down your browser.
</p>

Use the <i class="k-icon-caret-left"></i> **PREV** and **NEXT** <i class="k-icon-caret-right"></i> arrows, or enter a page number, to move through the data table.

## Filtering and sorting your data

By default, submissions in KoboToolbox appear in the data table in submission order, with the most recent entries at the top. In large projects, filtering and sorting are essential for exploring, reviewing, and cleaning data. They help you quickly find specific respondents, examine patterns, and identify records that need attention.

<p class="note">
<strong>Note:</strong> The <strong>Table</strong> view in KoboToolbox provides basic filtering and sorting for data monitoring and editing. For more advanced data analysis, including filtering with multiple conditions, we recommend <a href="https://support.kobotoolbox.org/export_download.html">exporting your dataset</a> and using spreadsheet or analysis software.
</p>

For each column in the data table, you can use the following features:

- **Search:** Use the search bar above text, number, and date fields to filter results. For example, you can search for a unique ID or filter by a specific age.
- **Filter:** For fields based on select type questions, click **Show all** in the column header to open a list of answer options. Select an option to filter the responses.
- **Sort:** Click a column header and choose Sort **A → Z** or **Sort Z → A** to change the order of submissions.

<p class="note">
<strong>Note:</strong> Sorting the table applies to all users and persists after you leave the <strong>Table</strong> view. Searching and filtering applies only to you while you are in the <strong>Table</strong> view and automatically resets when you leave it.
</p>

## Viewing individual submissions

Opening an individual submission lets you review all data from a single respondent. The single submission view includes tools for examining and managing an individual record.

To open a submission, click <i class="k-icon-view"></i> **View** in the corresponding row. 

![Open submission details](images/viewing_validating_data/open_submission.png)

The submission window displays all responses and includes the following options:

- View data in [any form language](https://support.kobotoolbox.org/collecting_data_multiple_languages.html).
- Display [XML values](https://support.kobotoolbox.org/glossary.html#xml-value) next to each question.
- **View** and **Edit** the submission [in Enketo](https://support.kobotoolbox.org/editing_deleting_data.html).
- **Duplicate** the submission.
- <i class="k-icon-print"></i> **Print** the submission.
- <i class="k-icon-trash"></i> **Delete** the submission.
- Assign a **validation status.**

![View submission window](images/viewing_validating_data/view_submission.png)

Within the single submission view, navigate through submissions using **< Previous** and **Next >**.

## Validating your data

Record validation helps project teams maintain data quality, track review status, and flag issues that require follow-up. Validation status appears as a dedicated column in the **Table** view, and users with appropriate permissions can update them for individual or multiple submissions.

The available statuses are:

- **Approved:** The submission has been reviewed and confirmed to be complete, accurate, and suitable for use in analysis.
- **Not approved:** The submission does not meet data quality requirements and should be excluded from analysis or removed from the dataset.
- **On hold:** The submission requires review. Additional verification or follow-up is needed before the data can be accepted or rejected.

Validation supports structured data review in collaborative teams. For example, reviewers can filter the table to show only submissions that require review.

<p class="note">
<strong>Note:</strong> A project owner can grant <strong>Validate submissions</strong> <a href="https://support.kobotoolbox.org/managing_permissions.html#setting-user-level-permissions">permission</a> to other users separately from the <strong>Edit submissions</strong> permission.
</p>

### Updating validation status in bulk

Validation status can be applied to multiple submissions at once, which is useful for large-scale reviews or quality checks.

To validate submissions in bulk:

1. Select the submissions using the checkboxes.
2. Click **Change status.**
3. Choose a validation status.

<p class="note">
<strong>Note:</strong> You can select all submissions on the current page by clicking the checkbox in the table header. To select all submissions in the project across all pages, click the arrow next to the checkbox and choose <strong>Select all results.</strong>
</p>

![Select submissions](images/viewing_validating_data/select.png)

## Troubleshooting

<details>
  <summary><strong>Fields or questions not appearing in the data table</strong></summary>
If you added new questions after data collection began, the fields may remain hidden if table visibility was previously configured. Click <i class="k-icon-qt-hidden"></i> <strong>hide fields</strong>, locate and select the new question, then click <strong>Apply.</strong>
</details>

<br>

<details>
  <summary><strong>Search functionality for Hidden question types</strong></summary>
  The <strong>Search</strong> feature is not currently supported for <strong>Hidden</strong> question types. To locate a specific value in a <strong>Hidden</strong> field, sort the table by that field and scroll to the value in alphabetical or numerical order.
</details>

<br>
