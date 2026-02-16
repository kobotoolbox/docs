# Introduction to form logic in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/form_logic_xls.md" class="reference">25 Nov 2025</a>

Form logic controls the flow and behavior of your form based on responses to previous questions. It allows you to create dynamic forms that adapt to user input. For example, you can use form logic to display specific questions only when relevant, validate responses, or perform calculations automatically.

Key types of form logic include:
- **Skip logic:** Controls when questions are shown or hidden based on previous responses.
- **Constraints:** Validate responses to ensure they meet defined rules or criteria.
- **Choice filters:** Display only relevant answer options based on earlier responses.
- **Calculations:** Automatically generate values using mathematical or logical expressions.
- **Required logic:** Defines when a question must be answered.

Form logic is built using **expressions**, which combine **question references**, **operators**, **functions**, and **constants**. The expression evaluates as TRUE or FALSE to control the form's behavior.

<p class="note">
  This article introduces the basic components of form logic in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>, including question referencing, operators, and functions. To learn more about each type of form logic, see support articles on <a href="https://support.kobotoolbox.org/skip_logic_xls.html">skip logic</a>, <a href="https://support.kobotoolbox.org/required_logic_xls.html">required logic</a>, <a href="https://support.kobotoolbox.org/constraints_xls.html">constraints</a>, <a href="https://support.kobotoolbox.org/choice_filters_xls.html">choice filters</a>, and <a href="https://support.kobotoolbox.org/calculations_xls.html">calculations</a> in XLSForm.
</p>

## Question referencing 

Question referencing allows you to incorporate the answer to a previous question into the label or logic of a subsequent question. Question referencing is frequently used in advanced forms:

- **In question labels or hints:** For example, you can include a respondent’s child’s name in later questions about their child.
- **In form logic:** For example, you can show or hide a question based on a previous response, or validate an answer by comparing it with an earlier one.

Question referencing uses the format **${question_name}**, where 	`question_name` is replaced with the unique name of the referenced question. 

If a question reference includes a spelling error or is otherwise incorrect, an error message will appear when previewing or submitting the form.

<p class="note">
  <strong>Note:</strong> When referencing a question within its own logic (i.e., in its own row), a period <code>.</code> can be used as a shortcut.
</p>

**survey worksheet**

| type     | name            | label                                                                 | constraint              |
|:-----------|:-----------------|:------------------------------------------------------------------------|:--------------------------|
| integer   | household_size  | How many people live in your household?                                |                          |
| integer   | total_under18   | Out of the ${household_size} people, how many are under the age of 18? | . < ${household_size}    |
| survey | 

## Mathematical and comparison operators 

**Mathematical operators** are used to perform arithmetic calculations using numerical values in the form. Mathematical operators in XLSForm include: 

| Operator | Description                     |
|:-----------|:---------------------------------|
| `+`       | Addition                        |
| `-`       | Subtraction                     |
| `*`       | Multiplication                  |
| `div`     | Division                        |
| `mod`     | Modulo (remainder of a division) |

**Comparison operators** are used to compare values. Comparison operators in XLSForm include: 

| Operator | Description                  |
|:-----------|:------------------------------|
| `=`       | Equal to                     |
| `>`       | Greater than                 |
| `<`       | Less than                    |
| `>=`      | Greater than or equal to     |
| `<=`      | Less than or equal to        |
| `!=`      | Not equal to                 |

## Combining conditions using logical operators 

**Logical operators** can be used in XLSForm to combine multiple conditions. Logical operators in XLSForm include:
- **and** (all conditions must be met)
- **or** (at least one of the conditions must be met) 
- **not** (condition(s) must not be met)

**survey worksheet**

| type     | name           | label                                | constraint                         |
|:-----------|:----------------|:--------------------------------------|:------------------------------------|
| integer   | household_size | How many people live in your household? |                                    |
| integer   | total_under18  | How many are under the age of 18?    | . < ${household_size} <strong>and</strong> . >= 0   |
| survey |

## Functions

Functions are predefined operations used to perform calculations or manipulate data in XLSForm. Functions make calculations and form logic more efficient by automatically performing complex tasks like rounding values, calculating powers, or extracting the current date.

<p class="note">
For a comprehensive list of functions in XLSForm, see <a href="https://support.kobotoolbox.org/functions_xls.html">Using functions in XLSForm</a>.
</p>

## Regex

A regular expression (regex) is a search pattern used to match specific characters within a string. It is widely used to validate, search, extract, and restrict text in most programming languages, including in KoboToolbox.

Regex can be used in **constraints** to control the length and characters entered into a question (e.g., limiting phone number entry to exactly 10 digits, controlling the format of ID numbers, or verifying valid email entry). It can also be used in **calculations** and other form logic.

In KoboToolbox, regular expressions are evaluated using the function `regex(., ' ')`, where the regex is entered between apostrophes and the period `.` represents the current question.  `regex(., ' ')` returns TRUE if the regular expression is met, and FALSE otherwise.

<p class="note">
  To learn more about using regex in KoboToolbox, see <a href="https://support.kobotoolbox.org/restrict_responses.html">Introduction to regular expressions</a>.
</p>




