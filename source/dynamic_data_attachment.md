# Dynamic Data Attachments

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/1d7f77a9494f8bbbc0728a28c2e7af03c98f3f7b/source/dynamic_data_attachment.md" class="reference">5
Aug 2021</a>

This article explains how to dynamically link data between KoboToolbox projects. Dynamic linking allows you to use data from a **parent project** within **child projects**, simplifying the management of longitudinal data collection. 

<p class="note">
    <strong>Note:</strong> Dynamic data attachments function similarly to the `pulldata()` function but eliminate the need for separate CSV files, since the data from a linked parent project serves as the data source.
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


3. Throughout the form, you can retrieve values from the parent project by creating a new question and including the [appropriate expression](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments) in the `calculation` column (see table [below](https://support.kobotoolbox.org/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). You can use the following question types to retrieve data:
    - Use a calculate question type to retrieve and store values for future use within the form or dataset (e.g., for calculations or dynamic question labels).
    - Use text, integer, decimal, select_one, or select_multiple question types to include retrieved values as default responses in editable fields. Data edited in the child project will not change the original data in the parent project.

FOR LATER!!!
<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

