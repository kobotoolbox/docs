# Editing and deleting your data

Editing and deleting data helps **maintain data quality** after submissions are collected. You may need to correct individual responses, update multiple records at once, duplicate a submission, or remove records that are no longer needed. KoboToolbox offers several ways to manage these tasks, including **editing submissions in Enketo**, **editing raw data directly**, and **applying bulk updates.** This article explains each method and when to use it.

<p class="note">
<strong>Note:</strong> Submissions collected with the <a href="https://support.kobotoolbox.org/kobocollect_on_android_latest.html">KoboCollect app</a> cannot be edited or deleted <strong>in KoboCollect</strong> after they are submitted. All post-submission changes must be made in KoboToolbox.
</p>

Project owners can control data access by assigning separate permissions to view, edit, validate, and delete submissions. For example, they can allow some team members to edit data while restricting deletion permissions.

<p class="note">
To learn more about user-level permissions for editing and deleting data, see <a href="https://support.kobotoolbox.org/managing_permissions.html">Sharing projects with user-level permissions</a>. 
</p>

## Editing individual submissions

KoboToolbox offers two editing approaches, each designed for different use cases. Understanding how they differ helps you choose the safest and most appropriate method for updating data.

The two methods for editing submissions in KoboToolbox are:

- **Editing submissions in Enketo:** Opens the submission in Enketo so you can correct responses and resubmit the form. This method is recommended when form logic needs to be applied.
- **Editing raw data directly in KoboToolbox:** Opens a data editor that lets you modify specific responses directly. This method is recommended when you need precise control over edits and do not need form logic to apply.

Each method comes with its advantages and limitations:

| Editing method      | Advantages                                                                                                                                   | Limitations                                                                                                                                                                                                                   |
|:--------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Editing in Enketo &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  | <ul><li><strong>Maintains form logic</strong>: calculations and skip logic are automatically re-evaluated.</li><li><strong>Provides a more intuitive, form-based editing experience</strong>: the submission opens in the same layout and flow used during data collection.</li><li><strong>Minimizes data entry errors</strong> by enforcing choice lists, required questions, and validation rules during editing.</li></ul> | <br><ul><li>Reopening the form can <strong>unintentionally modify other responses</strong> because all form logic and calculations run again.</li><li><strong>Skip logic may hide or delete existing answers</strong> if they no longer meet the relevance conditions defined in the updated form.</li><li>May require entering responses for newly added questions, and may delete responses to questions that have been removed from the form.</li></ul> |
| Editing raw data    |<ul><li><strong>Allows targeted edits</strong> to specific fields without reopening the form.</li><li><strong>Preserves the rest of the submission unchanged</strong>, since no form logic, calculations, or constraints are triggered.</li><li>Allows entering values <strong>not included in choice lists</strong> or <strong>supported by question type</strong> as well as deleting required responses.</li><li>Allows for <strong>editing multiple submissions</strong> in bulk.</li></ul> | <br><ul><li><strong>Skip logic and validation rules are ignored</strong>, which may lead to inconsistent values.</li><li><strong>Question types and option choices</strong> are not enforced.</li><li>Cannot edit <strong>calculation</strong> results or <strong>metadata.</strong></li><li>Not currently supported for editing questions inside <strong>repeating groups.</strong></li><li>Must manually enter correct XML values for select questions.</li><li>Incorrect response type, choice name, or GPS coordinate formatting can lead to issues in reports or during analysis.</li></ul> <br> |

<p class="note">
<strong>Note:</strong> When editing data using either method, the `_uuid` metadata field is updated each time a change is saved. When editing in Enketo, the `end` field is also updated. All other metadata fields remain unchanged, including `_id`, `start`, `today`, `_submission_time`, and `_submitted_by`.
</p>

### Editing submissions in Enketo

This method opens a submission in Enketo so you can correct responses.

To edit a submission in Enketo:


