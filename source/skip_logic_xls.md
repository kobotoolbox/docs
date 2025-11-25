# Adding skip logic in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/skip_logic_xls.md" class="reference">25 Nov 2025</a>

Skip logic, also known as relevance logic, allows you to **determine when a question or group of questions will be displayed** in the form based on a previous question or the result of a calculation. For example, you can use it to ask follow-up questions only to a subset of respondents, or to hide entire sections of a form if they are not relevant.

<p class="note">
  To learn more about form logic in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

This article covers the following topics: 
- Adding skip logic to individual questions 
- Combining multiple skip logic conditions 
- Adding skip logic based on whether a question was answered
- Adding skip logic to question groups

<p class="note">
  <strong>Note:</strong> This article focuses on adding skip logic in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about adding skip logic in the KoboToolbox Formbuilder, see <a href=https://support.kobotoolbox.org/skip_logic.html">Adding skip logic in the Formbuilder</a>.
<br><br>
For hands-on practice with skip logic in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Adding skip logic conditions to individual questions

Skip logic uses [question referencing](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) to only display questions that are relevant to the respondent based on previous answers. The question used to define the relevance logic is referred to as the **reference question**.

To add skip logic in XLSForm:
1. Add a **relevant** column to the `survey` worksheet. 
2. In the row of the question you wish to display or hide, enter the condition that must be met **for the question to be displayed.**

**survey worksheet**

| type         | name     | label             | relevant     |
|:--------------|:----------|:------------------|:--------------|
| integer       | age       | How old are you?  |               |
| select_one yn | married   | Are you married?  | ${age} > 18   |
| survey |

In the example above, `${age}` is the reference question, and the answer to `${age}` must be greater than 18 for the “Are you married?” question to be displayed.

### Formatting skip logic conditions

The format of the skip logic condition will differ according to the **type** of the reference question, as detailed in the table below.

| Reference question type | Skip logic condition | Example |
|:-------------------------|:--------------------|:---------|
| select_one | `${reference_question} = 'choice_name'` | `${consent} = 'yes'` |
| select_multiple | `selected(${reference_question}, 'choice_name')` | `selected(${reasons}, 'other')` |
| integer | `${reference_question}` followed by a logical operator (>, <, =) and a number (or a reference to another question) | `${age} >= 18` |
| date | `${reference_question}` followed by a logical operator (>, <, =) and `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
  To learn more about building form logic expressions in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

## Combining multiple skip logic conditions

Multiple relevance conditions can be combined into a single expression to determine when a question is displayed based on a previous response. Conditions can be combined using **and**, **or**, and **not** logical operators:

- Use **and** when all conditions must be met for a question to be displayed. 
    - For example: <code>${age} > 18 <strong>and</strong> ${student} = ‘no’</code>
- Use **or** when at least one condition must be met for a question to be displayed.
    - For example: <code>${age} < 18 <strong>or</strong> ${student} = ‘yes’</code>
- Use **not** to indicate that a condition or set of conditions must not be met (e.g., when two conditions cannot be true together for a question to be displayed).
    - For example: <code><strong>not</strong>(${age} > 18 <strong>and</strong> ${student} = ‘yes’)</code>

**survey worksheet**

| type         | name     | label              | relevant                          |
|:--------------|:----------|:-------------------|:----------------------------------|
| integer       | age       | What is your age?  |                                   |
| select_one yn | employed  | Are you employed?  | ${age} >= 16 <strong>and</strong> ${age} <= 75     |
| survey | 

## Adding skip logic based on whether a question was answered

In addition to adding skip logic based on a specific response, you can add skip logic based on whether a question was answered or left blank. This can be useful to add follow-up questions, or when using [acknowledge questions](https://support.kobotoolbox.org/acknowledge.html) in your form.

Unanswered questions are treated as empty strings, noted as two single apostrophes `''`. The following skip logic conditions can be used:

| Skip logic condition | Description |
|:---------------------|:-------------|
| `${reference_question} != ''` | Display only if `reference_question` is answered (not blank). |
| `${reference_question} = ''` | Display only if `reference_question` is unanswered (blank). |

**survey worksheet**

| type         | name      | label                | relevant             |
|:--------------|:-----------|:---------------------|:---------------------|
| text          | why_joined | Why did you join?    |                      |
| select_one yn | benefits   | Are you seeing benefits? | ${why_joined} != '' |
| survey | 

## Adding skip logic conditions to question groups

Skip logic can be applied to question groups as well as individual questions. Applying skip logic to a group will show or hide all questions within that group based on previous responses. 

To add skip logic to question groups:
1. Add a **relevant** column to the `survey` worksheet. 
2. In the **begin_group** row of the question group you wish to display or hide, enter the condition that must be met **for the group to be displayed.**

**survey worksheet**

| type         | name        | label                                         | relevant            |
|:-------------|:------------|:---------------------------------------------|:-------------------|
| select_one yn | joined     | Did you join the association?                |                     |
| begin_group  | association | Association participation                    | ${joined} = 'yes'  |
| date         | date_joined | When did you join the association?           |                     |
| select_one yn | voted      | Have you ever voted in any election for the association? |                     |
| end_group    |             |                                              |                     |
| survey | 

