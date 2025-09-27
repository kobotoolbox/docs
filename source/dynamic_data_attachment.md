# Dynamic Data Attachments

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/1d7f77a9494f8bbbc0728a28c2e7af03c98f3f7b/source/dynamic_data_attachment.md" class="reference">5
Aug 2021</a>

This article explains how to dynamically link data between KoboToolbox projects. Dynamic linking allows you to use data from a **parent project** within **child projects**, simplifying the management of longitudinal data collection. 

<p class="note">
    <strong>Note:</strong> Dynamic data attachments function similarly to the <a href="https://support.kobotoolbox.org/pull_data_kobotoolbox.html">`pulldata()`</a> function but eliminate the need for separate CSV files, since the data from a linked parent project serves as the data source.
</p>

You can retrieve various non-media responses from a parent project and perform calculations on this linked data in a child project. This can be useful for retrieving baseline data, contact information, or health records in cohort studies, or for confirming or verifying previously collected data. 

We recommend using [XLSForm](https://support.kobotoolbox.org/edit_forms_excel.html) to set up dynamic data attachments. For examples of parent and child projects, download sample files [here](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/Round_1.xlsx) and [here](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/Round_2.xlsx).

## Dynamically linking projects in XLSForm

Dynamically linking projects requires a **parent project** and at least one **child project**. The **parent project** requires no modification from a normal XLSForm. However, setting up the **child project(s)** involves the following steps:
1. Add a row at the beginning of your XLSForm and set the question type to `xml-external`.
2. In the `name` column, provide a short name for the parent form. This name can consist of Latin alphabet characters, underscores, and numbers.

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. Throughout the form, you can retrieve values from the parent project by creating a new question and including the [appropriate expression](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments) in the `calculation` column (see table [below](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). You can use the following question types to retrieve data:
    - Use a **calculate** question type to retrieve and store values for future use within the form or dataset (e.g., for calculations or dynamic question labels).
    - Use **text**, **integer**, **decimal**, **select_one**, or **select_multiple** question types to include retrieved values as default responses in editable fields. Data edited in the child project will not change the original data in the parent project.
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | What is the participant's ID? |  |
| integer | age | Confirm the participant's age | instance('parent')/root/data[enrollment_id =current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Note:</strong> 
    To display linked data without allowing users to edit the field, use a <strong>calculate</strong> question followed by a <strong>note</strong> question that displays the calculated value. Alternatively, use <strong>text</strong>, <strong>integer</strong>, <strong>decimal</strong>, <strong>select_one</strong>, or <strong>select_multiple</strong> questions with the `read_only` column set to `TRUE`.
</p>

## Calculation syntax for dynamic data attachments

In the **calculation** column of the row where linked data will be retrieved, include one of the expressions in the table below. These expressions are called **XPaths**. 

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
| `count(instance('parent')/root/data[parent_question])`      | Returns the total number of rows in the parent project where `parent_question` is not empty. |
| `count(instance('parent')/root/data[parent_question =current()/../child_question])` | Returns the total count of instances where the value of `parent_question` in the parent project is equal to the value of `child_question` in the child project. |
| `instance('parent')/root/data[parent_index_group/parent_index_question =current()/../child_index_question]/parent_group/parent_question` | Returns the value of `parent_question` (in `parent_group`) from the parent project where `child_index_question` in the child project is equal to `parent_index_question` in the parent project. |
| `instance('parent')/root/data[parent_index_group/parent_index_question =current()/../child_index_question][position()=1]/parent_group/parent_question` | Same as above, but specifies that only data from the first instance of `parent_index_question` should be returned, using the `[position()=1]` argument. Used in case of possible duplicates in the parent form. |
| `sum(instance('parent')/root/data/parent_group/parent_question)` | Returns the sum of values from `parent_question` (in `parent_group`) from the parent project. Note that `parent_question must be numeric` |
| `max(instance('parent')/root/data/parent_group/parent_question)`         | Returns the maximum value entered in `parent_questio`n (in parent_group) from the parent project. Note that `parent_question` must be numeric.     |
| `min(instance('parent')/root/data/parent_group/parent_question)`      | Returns the minimum value entered in `parent_question` (in `parent_group`) from the parent project. Note that `parent_question` must be numeric.     |

## Setting up projects for dynamic linking

Once your XLSForms are set up, log into your KoboToolbox account and follow these steps:
Upload and deploy the parent project, if not already deployed. Ensure the parent project has at least one submission.
Enable data sharing: 
In the parent project’s SETTINGS > Connect Projects tab, toggle the Data Sharing switch (disabled by default) and click ACKNOWLEDGE AND CONTINUE in the confirmation window. 
All data is shared by default, but you can restrict specific variables to share with child projects by clicking “Select specific questions to share”.


<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

