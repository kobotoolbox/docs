# Repeat groups in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/repeat_groups_xls.md" class="reference">25 Nov 2025</a>

Repeat groups in XLSForm allow you to ask the same set of questions multiple times within a form. This is especially useful when collecting similar information about several people, items, or events. 

For example, if you're gathering details about each member of a household, you can use a repeat group to ask the same demographic questions for every individual. 

This article covers the following topics:
- Creating a repeat group
- Setting repeat counts to limit the number of repetitions
- Counting the number of repetitions within a repeat group
- Retrieving values from repeat groups 

<p class="note"> 
<strong>Note:</strong> This article focuses on repeating groups in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about repeating groups in the KoboToolbox Formbuilder and to preview repeat groups in action, see <a href="https://support.kobotoolbox.org/group_repeat.html">Grouping questions and repeating groups</a>. 
</p>

## Creating a repeat group

To create a repeat group in XLSForm:

1. In the `type` column of the survey worksheet, enter **begin_repeat** to indicate the start of the repeat group. 
2. In the `name` column of the **begin_repeat** row, enter the unique identifier for the group.
3. In the `label` column, enter the title of the group as you want it displayed in the form. The label is optional and can be left blank.
4. Enter each question of the group in its own row, as you normally would.
5. In a new row after the repeating questions, enter **end_repeat** in the `type` column to indicate the end of the repeat group. 
    - In the **end_repeat** row, leave the `name` and `label` columns blank.
  
**survey worksheet**

| type | name | label |
| :--- | :--- | :--- |
| **begin_repeat** | household_members | Household Members |
| text | name | What is the person's name? |
| integer | age | How old are they? |
| select_one yn | married | Are they married? |
| **end_repeat** | | |
| survey |

Repeat groups function similarly to question groups. With repeat groups, you can:

- Use the **field-list** appearance to [display all questions](https://support.kobotoolbox.org/grouping_questions_xls.html#appearance-settings-for-question-groups) on the same page.
- Add [skip logic](https://support.kobotoolbox.org/grouping_questions_xls.html#applying-skip-logic-to-question-groups) to repeat groups in the **relevance** column.
- Create **nested** repeat groups, where one repeat group is added [inside another](https://support.kobotoolbox.org/grouping_questions_xls.html#nested-groups).

<p class="note">
  <strong>Note:</strong> Adding repeat groups to your form creates a different data structure compared to standard variables or groups. When you download your data in .xlsx format, you will find a separate sheet for each repeat group. For more information on exporting and using repeat group data, see <a href="https://support.kobotoolbox.org/managing_repeat_groups.html">Managing repeat group data</a>.
</p>

## Setting repeat counts

By default, repeat groups can be repeated as many times as needed. To limit the number of times a repeat group is repeated in the form, you can set a repeat count. The **repeat count** can be either a fixed number or dynamically determined based on a previous response.

To set a fixed number of repetitions:

1. Add a **repeat_count** column in the `survey` worksheet. 
2. Input a number in the **repeat_count** column.

**survey worksheet**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| begin_repeat | participant_profile | Participant profile | 3 |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| survey |

To dynamically determine the number of repetitions based on a previous response:

1. Add a **repeat_count** column in the `survey` worksheet.
2. Enter the question reference in the **repeat_count** column. 
    - The referenced question must be an `integer` question type.
  
  **survey worksheet**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| integer | participants | Total number of training participants | |
| begin_repeat | participant_profile | Participant profile | ${participants} |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| survey |

<p class="note">
  <strong>Note:</strong> Inside the <strong>repeat_count</strong> column, you can also include advanced conditional statements to determine if repetitions will continue. For more information, see <a href="https://docs.getodk.org/form-logic/#repeating-as-long-as-a-condition-is-met">ODK documentation</a>. 
</p>

## Counting number of repetitions inside a repeat group

When using repeat groups, you may need a field that counts how many times the group has been repeated. This can be useful for calculations or form logic. For example, you can apply skip logic after a specific repetition or dynamically include the repeat number in a question label (e.g., Child 1, Child 2).

To count how many times a repeat group has been repeated:
1. Add a **calculate** question inside the repeat group.
2. Enter `position(..)` in the **calculation** column. 

This variable stores the current repeat index. You can use it in form logic or to create dynamic question labels.

**survey worksheet**

| type | name | label | calculation | relevance |
| :--- | :--- | :--- | :--- | :--- |
| begin_repeat | profile | Participant profile | | |
| calculate | number | | **position(..)** | |
| note | instructions | Answer the questions below for each participant. | | **${number} = 1** |
| text | name | Name of participant **${number}** | | |
| select_one gender | gender | Gender of participant **${number}** | | |
| integer | age | Age of participant **${number}** | | |
| end_repeat | | | | |
| survey |

## Counting total number of repeat group repetitions

You can also add a separate question outside the repeat group to count the total number of repetitions. This is useful, for example, to confirm the number of participants or children listed in the repeat group.

To count how many times a repeat group was filled in:
1. Add a **calculate** question after the repeat group.
2. In the **calculation** column, enter `count(${repeat_group_name})`, where `repeat_group_name` is the name of the repeat group.

This variable stores the total number of group repetitions. You can use it in calculations or to create dynamic question labels in your form.

**survey worksheet**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Children roster | |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| calculate | count_children | | **count(${children})** |
| acknowledge | confirm_children | Confirm that there are **${count_children}** children in the household. | |
| survey |

## Retrieving values from repeat groups 

Advanced forms often use [question referencing](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) to include responses from earlier questions in question labels, calculations, or skip logic. You can also use question referencing **within repeat groups** or to refer to repeated data elsewhere in your form.

Within a repeat group, you can reference a response from another question in the same repetition using question referencing, as shown below.

**survey worksheet**

type | name | label |
| :--- | :--- | :--- |
| begin_repeat | children | Children roster |
| text | name | What is the child's name? |
| integer | age | How old is ${name}? |
| select_one gender | married | What is ${name}'s gender? |
| end_repeat | | |
| survey |

Outside a repeat group, you can retrieve data from the repeat group for use in form logic or question labels:

1. Add a **calculate** question after your repeat group.
2. Include one of the formulas listed below in the **calculation** column.
3. The **calculate** question stores the retrieved value, which you can then use in form logic or question labels.

**Formulas to retrieve data from repeat groups**

| Formula | Description |
| :--- | :--- |
| `max(${question-name})` | Retrieves the maximum value entered for one question in the repeat group. |
| `min(${question-name})` | Retrieves the minimum value entered for one question in the repeat group. |
| `sum(${question-name})` | Computes the sum of numerical values entered for one question in the repeat group. |
| `join('; ', ${question-name})` | Lists all responses to a given question inside a repeat group, separated by a semi-colon. |
| `indexed-repeat(${question-name}, ${repeat-name}, n)` | Retrieves the value for `${question-name}`, in the repeat group called `${repeat-name}`, in the n<sup>th</sup> repetition. |

**survey worksheet**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Children roster | |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| calculate | max_age | | **max(${age})** |
| acknowledge | confirm_age | Confirm that the oldest child in the household is **${max_age}** years old. | |
| survey |

