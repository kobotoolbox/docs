# Dynamic data attachments
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/a3cacecb4631b200222c9c43250fdfb191a78633/source/dynamic_data_attachment.md" class="reference">19 Feb 2026</a>


Dynamic linking allows you to use data from a **parent project** within **child projects**, simplifying the management of longitudinal data collection. This article explains how to dynamically link data between KoboToolbox projects.

<p class="note">
    <strong>Note:</strong> Dynamic data attachments function similarly to the <a href="https://support.kobotoolbox.org/pull_data_kobotoolbox.html"><code>pulldata()</code></a> function but eliminate the need for separate CSV files, since the data from a linked parent project serves as the data source.
</p>

You can retrieve various **non-media responses** from a parent project and perform calculations on this linked data in a child project. This can be useful for retrieving baseline data, contact information, or health records in cohort studies, or for confirming or verifying previously collected data. 

We recommend using [XLSForm](https://support.kobotoolbox.org/edit_forms_excel.html) to set up dynamic data attachments. For examples of parent and child projects, download sample files [here](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) and [here](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx).

## Dynamically linking projects in XLSForm

Dynamically linking projects requires a **parent project** and at least one **child project**. The **parent project** requires no modification from a normal XLSForm. However, setting up the **child project(s)** involves the following steps:
1. In the `survey` worksheet of your XLSForm, add a row and set the question type to `xml-external`.
2. In the `name` column, provide a short name for the parent form. This name can consist of Latin alphabet characters, underscores, and numbers.

**survey worksheet**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. Throughout the form, you can retrieve values from the parent project by creating a new question and including the appropriate expression in the `calculation` column (see table [below](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). You can use the following question types to retrieve data:
    - Use a `calculate` question type to retrieve and store values for future use within the form or dataset (e.g., for calculations or dynamic question labels).
    - Use `text`, `integer`, `decimal`, `date`, `select_one`, or `select_multiple` question types to include retrieved values as default responses in editable fields. Data edited in the child project will not change the original data in the parent project.
  
**survey worksheet**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | What is the participant's ID? |  |
| integer | age | Confirm the participant's age | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Note:</strong> 
    To display linked data without allowing users to edit the field, use a <code>calculate</code> question followed by a <code>note</code> question that displays the calculated value. Alternatively, use <code>text</code>, <code>integer</code>, <code>decimal</code>, <code>select_one</code>, or <code>select_multiple</code> questions with the <code>read_only</code> column set to <code>TRUE</code>.
</p>

## Calculation syntax for dynamic data attachments

In the `calculation` column of the row where linked data will be retrieved, include one of the expressions in the table below. These expressions are called **XPaths**. 

For each expression in the table below:

- `parent` is the unique name assigned to the **parent form** (e.g., in the `xml-external` question of the **child form**).
- `parent_question` refers to the `name` of a question from the **parent form**.
- `child_question` refers to the `name` of a question from the **child form**.
- `parent_index_question` is the identifying question from the **parent form** that links it to the **child form** (e.g., unique ID, organization name).
- `child_index_question` is the identifying question from the **child form** that links it to the **parent form** (e.g., unique ID, organization name).
- `parent_group` refers to the `name` of the group in the **parent form** in which the `parent_question` is located.
- `parent_index_group` refers to the `name` of the group in the **parent form** in which the `parent_index_question` is located.

| **XPath**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Returns the total number of rows in the parent project. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Returns the total number of rows in the parent project where `parent_question`  (in `parent_group`) is not empty. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question])` | Returns the total count of instances where the value of `parent_question`  (in `parent_group`) in the parent project is equal to the value of `child_question` in the child project. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Returns the value of `parent_question` (in `parent_group`) from the parent project where `child_index_question` in the child project is equal to `parent_index_question` in the parent project. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Same as above, but specifies that only data from the first instance of `parent_index_question` should be returned, using the `[position() = 1]` argument. Used in case of possible duplicates in the parent form. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Returns the sum of values from `parent_question` (in `parent_group`) from the parent project. Note that `parent_question must be numeric` |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Returns the maximum value entered in `parent_questio`n (in parent_group) from the parent project. Note that `parent_question` must be numeric.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Returns the minimum value entered in `parent_question` (in `parent_group`) from the parent project. Note that `parent_question` must be numeric.     |   


<p class="note">
    <strong>Note:</strong> If the parent question is not included in any group, omit <code>parent_group</code> from the expression
</p>

## Setting up projects for dynamic linking

Once your XLSForms are set up, log into your KoboToolbox account and follow these steps:

1. Create and deploy the **parent project**, if not already deployed. 
2. Enable data sharing for the parent project: 
    - In the **SETTINGS > Connect Projects** tab of the parent project, toggle the **Data sharing** switch (disabled by default) and click **ACKNOWLEDGE AND CONTINUE** in the confirmation window. 
    - All data is shared by default, but you can restrict specific variables to share with child projects by clicking "Select specific questions to share".

<p class="note">
    <strong>Note:</strong> If projects have different owners, the parent project owner must <a href="https://support.kobotoolbox.org/managing_permissions.html">share the project</a> with the child project owner. The minimum permissions required for dynamic data attachments to work are <strong>View form</strong> and <strong>View submissions</strong>. Note that this allows child project administrators to view all parent project data.
</p>

3. Create and deploy the **child project**.
4. Connect the child project to the parent project: 
    - In the **SETTINGS > Connect Projects** tab of the child project, click the "Select a different project to import data from." A dropdown menu will allow you to select a parent project to link. 
    - Rename the linked parent project to the `xml-external` question name defined in the XLSForm and click **IMPORT**. 
    - You can then select specific questions from the parent project to share with the child project (recommended), or select all questions.
5. If you add new fields to the parent form and wish to use them in the child project, re-import the parent project in the child project settings.

<p class="note">
    <strong>Note:</strong> Forms can only be linked together if they are on the same KoboToolbox server.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Dynamically linking a form to itself

It is possible for a parent and child project to be the same project. The steps are the same as those described above. Examples of use cases include: 

- **Daily monitoring**: If a form is used to survey the same person over time, you can link it to itself to count previous submissions. This can allow you to display a message (e.g., "monitoring is complete") after a certain number of entries or to inform the enumerator of the number of forms submitted, as shown in the example below.

**survey worksheet**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | What is the participant's ID? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | This participant has been surveyed ${count} times. | |
| survey | 

- **Registration form**: By linking a registration form to itself, you can check whether a user has already been registered. This can allow you to generate an error message or add a constraint if they are already registered, preventing duplicate registrations, as shown in the example below.

**survey worksheet**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | What is the customer's ID number? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | This customer is already registered. Please close this form. | | ${count} > 0 |
| survey | 

## Collecting and managing data with dynamic linking

Data for dynamically linked projects can be collected using the [KoboCollect Android app](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) or [Enketo web forms](https://support.kobotoolbox.org/data_through_webforms.html).

When collecting data, note the following:

- The parent project must have at least one submission for the child project to function correctly.
- When collecting data online, there is a five-minute delay in syncing new parent project data with the child project.
- In offline mode, frequently download the child project to ensure data synchronization with the parent project.

<p class="note">
    <strong>Note:</strong> You can <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">configure the KoboCollect Android app</a> to automatically update the parent project's data when an internet connection is available. Go to <strong>Settings > Form management > Blank form update mode</strong> and select either <strong>Previously downloaded forms only</strong> or <strong>Exactly match server</strong>. You can set the automatic download frequency to occur every 15 minutes, every hour, every six hours, or every 24 hours. Note that enabling this setting may increase battery consumption.
</p>

## Troubleshooting

<details>
  <summary><strong>Error or crash when linking forms</strong></summary>
If the user interface crashes when you attempt to link forms, check the following:
  <ul>
    <li>Your XLSForm does not include duplicate question or group names in the <code>name</code> column of the <code>survey</code> worksheet.</li>
    <li>Your parent project has at least one submission.</li>
  </ul>
If the user interface is still crashing, select only the questions you need to connect the forms, instead of clicking <strong>Select all</strong>.
</details>

<br>

<details>
<summary><strong>Parent data not showing in the child form</strong></summary>
Check that the calculation syntax in the child form is correct and that the relevant questions are shared in both projects. If your parent question is in a question group, be sure to include the group name in the XPath expression. Note that new parent project data takes up to five minutes to sync when you are online. If you add new fields to the parent form and want to use them in the child project, open the child project settings, re-import the parent project, and redeploy.
</details>

<br>

<details>
<summary><strong>Child form loads slowly</strong></summary>
Large dynamic data attachments can slow down form loading. Share only the questions the child form needs instead of the full list of questions, then redeploy and try again.
</details>

<br>

<details>
<summary><strong>Dynamic data not refreshing in KoboCollect</strong></summary>
If you are using KoboCollect and collecting data offline, data must first be submitted to the parent project and then downloaded to your data collection device for the dynamic data attachment to work. Both steps require an internet connection. Downloading parent data is similar to downloading a new version of a form, and the KoboCollect app can be configured to <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">automatically download new data</a> at a set frequency. It is not recommended to rely on dynamic data attachments for data collected offline within a short period of time.
</details>

<br>

<details>
<summary><strong>Dynamic data attachment not working inside question groups</strong></summary>
To pull dynamic data from a parent form into a child form with question groups, ensure the index question (e.g., the identification number) in the child form is in the same group as the calculation for the dynamic data. See sample files <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> and <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> for an example of dynamic data attachments within groups.
</details>

<br>

<details>
<summary><strong>Error evaluation fields in KoboCollect</strong></summary>
If your parent form contains duplicate submissions, you may receive an error message in KoboCollect stating “Error evaluating field / XPath evaluation: type mismatch /This field is repeated.” To solve this issue and pull data only from the first submission containing a specific index value, use the <code>[position()=1]</code> argument, as below:
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>

