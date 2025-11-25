# Grouping questions in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/51a5c6e3324893d6fe857b201d4219be3e9cb7eb/source/grouping_questions_xls.md" class="reference">25 Nov 2025</a>

Grouping questions in XLSForm helps organize related content into clear, structured sections, improving form layout and navigation. For example, you can group all demographic questions into one section.

XLSForm makes it easy to create groups and [nested groups](https://support.kobotoolbox.org/grouping_questions_xls.html#nested-groups), and to apply [skip logic](https://support.kobotoolbox.org/grouping_questions_xls.html#applying-skip-logic-to-question-groups) to entire question groups. Group-level skip logic streamlines the respondent's experience by showing only relevant sections based on previous answers.

This article covers the following topics:

- Creating question groups and nested groups in XLSForm
- Displaying all grouped questions on a single page
- Adding skip logic to question groups

<p class="note">
<strong>Note:</strong> This article focuses on grouping questions in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about grouping questions in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/group_repeat.html">Grouping questions and repeating groups</a>.
</p>

## Creating a question group

To create a question group in XLSForm:

1.  In the `type` column of the `survey` worksheet, enter **begin_group** to indicate the start of the group.
2.  In the `name` column of the **begin_group** row, enter the unique identifier for the group.
3.  In the `label` column, enter the title of the group as you want it displayed in the form. The label is optional and can be left blank.
4.  Enter each question of the group in its own row, as you normally would.
5.  In a new row after the grouped questions, enter **end_group** in the `type` column to indicate the end of the group.
    - In the **end_group** row, leave the `name` and `label` columns blank.

**survey worksheet**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Section A: Personal Information |
| text | name | What is your name? |
| integer | age | How old are you? |
| select_one yn | married | Are you married? |
| **end_group** | | |
| survey |

### Nested groups

Nested groups are groups of questions inside another group of questions. Nested groups can be used to create a hierarchical structure within your XLSForm. For example, you can include a group of questions about a child inside a larger group of questions about the household.

When creating multiple groups, ensure that each `begin_group` row has a corresponding `end_group` row. If the number of `begin_group` rows does not match the number of `end_group` rows, the form will generate an error, preventing it from functioning properly during preview or deployment.

**survey worksheet**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Section A: Personal Information |
| text | name | What is your name? |
| integer | age | How old are you? |
| select_one yn | married | Are you married? |
| **begin_group** | education | Education |
| select_one yn | student | Are you currently a student? |
| select_one edu | education_level | What is the highest level of education you have completed? |
| **end_group** | | |
| **end_group** | | |
| survey |

### Repeat groups

In XLSForm, question groups can be repeated to collect the same set of responses multiple times within a form. This is useful when gathering similar information about multiple people, items, or events. Repeated groups are called **repeat groups**.

<p class="note">
  To learn more about setting up repeating groups of questions in XLSForm, see <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">Repeat groups in XLSForm</a>.
</p>

## Appearance settings for question groups

A common reason to group questions is to display them together on a single page. You can adjust the group's appearance settings to control how grouped questions are shown during data collection. The steps vary depending on whether you are using [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) or [Enketo](https://support.kobotoolbox.org/enketo.html).

<p class="note">
<strong>Note:</strong> Appearance settings to display groups on a single page work both for question groups and <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">repeat groups</a>.
</p>

### Using KoboCollect to collect data

By default, KoboCollect displays each question on a separate screen. Users must move manually from one question to the next.

To **display all grouped questions on the same screen** in KoboCollect:
1.  In the `survey` worksheet, add an **appearance** column.
2.  In the `appearance` column, enter **field-list** in the `begin_group` row.
    * Each question group will now appear on its own page.

**survey worksheet**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Section A: Personal Information | **field-list** |
| text | name | What is your name? | |
| integer | age | How old are you? | |
| select_one yn | married | Are you married? | |
| end_group | | | |
| survey |

### Using Enketo web forms to collect data

By default, Enketo web forms display all questions on a single page.

To display each group of questions on its own page in Enketo web forms:
1.  In the `settings` worksheet, add a **style** column.
2.  In the second cell of the `style` column, enter **pages**.
    * This applies the **pages** [theme](https://support.kobotoolbox.org/form_style_xls.html) to your Enketo web form, dividing it into separate pages similar to KoboCollect. 

**settings worksheet**

| style |
| :--- |
| pages |
| settings |

3.  In the `survey` worksheet, add an **appearance** column.
4.  In the `appearance` column, enter **field-list** in the `begin_group` row.
    * Each question group will now appear on its own page.

**survey worksheet**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Section A: Personal Information | **field-list** |
| text | name | What is your name? | |
| integer | age | How old are you? | |
| select_one yn | married | Are you married? | |
| end_group | | | |
| survey |


## Applying skip logic to question groups

Applying skip logic to question groups ensures that only relevant sections appear based on earlier responses. For example, in a household survey, you can use skip logic to show a group of questions for the head of household only when a previous question identifies the respondent as such. This makes the form easier to navigate and more responsive to user input.

To [apply skip logic](https://support.kobotoolbox.org/skip_logic_xls.html) to question groups in XLSForm, use the same approach as you would for individual questions:
1.  Add a **relevant** column to your `survey` worksheet.
2.  In the `relevant` column for the `begin_group` row, enter the condition that determines when the group should be shown.
3.  If the condition is met, the entire group will be displayed. If not, the group will be hidden.

This helps control the flow of your form so that only relevant sections appear based on earlier responses, making the form more streamlined and responsive to user input.

<p class="note">
<strong>Note:</strong> Skip logic can be applied both for question groups and <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">repeat groups</a>. To learn more about skip logic in XLSForm, see <a href="https://support.kobotoolbox.org/skip_logic_xls.html">Adding skip logic in XLSForm</a>.
</p>
