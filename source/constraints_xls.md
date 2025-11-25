# Adding constraints in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/constraints_xls.md" class="reference">25 Nov 2025</a>

Constraints, also known as validation criteria, are a type of form logic used to **restrict the acceptable responses to a question based on a predefined condition**. If the constraint condition is not met, a customizable error message is displayed, prompting the form user to enter a valid response.

<p class="note">
  To learn more about form logic in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

This article covers the following topics:
- Adding constraints to questions in XLSForm
- Combining multiple constraint conditions
- Customizing constraint error messages
- Advanced constraints in XLSForm

<p class="note">
  <strong>Note:</strong> This article focuses on adding constraints in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about adding constraints in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/validation_criteria.html?highlight=limiting">Adding validation criteria in the Formbuilder</a>.
<br><br>
For hands-on practice with adding constraints in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Adding a constraint

Constraints are built using [question references](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing), [comparison operators](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators), and constants. Constraint conditions must be met to validate or submit a form. Otherwise, an **error message** appears, and users are prevented from moving to the next page or submitting the form.

To add constraints in XLSForm:
1. Add a **constraint** column to the `survey` worksheet.
2. In the `constraint` column, define the condition that must be met **for the response to be valid.** 
    - Use a period `.` to reference the question in the row where you are adding a constraint.
    - Use a [comparison operator](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators), followed by a reference value, to build a simple constraint. 
    - For example, `. > 18` restricts an `integer` question to accept only values greater than 18.

**survey worksheet**

| type     | name       | label                                | constraint       |
|:---------|:-----------|:-------------------------------------|:----------------|
| integer  | age        | What is your age?                    | . >= 18         |
| integer  | household  | How many people live in your household? | . <= 30         |
| integer  | income     | Out of those, how many earn income?  | . <= ${household} |
| survey | 

### Formatting reference values
The reference value in a constraint condition must match the **type** of the question for which you are adding a constraint. The reference value formats for main question types are listed below: 

| Question type   | Reference value format                                      | Example                      |
|:----------------|:-----------------------------------------------------------|:------------------------------|
| integer         | Number                                                      | `. > 35`                     |
| select_one      | Choice name (as defined in the choices worksheet) in quotation marks | `. = 'yes'`                  |
| select_multiple | Choice name combined with the `selected()` <a href="https://support.kobotoolbox.org/functions_xls.html">function</a>       | `selected(., 'chair')`       |
| date            | Date in the `date('YYYY-MM-DD')` format                    | `. > date('2021-01-01')`    |
| text            | Text in quotation marks (rarely used for constraints)      | `. != 'Not applicable'`      |

<p class="note">
  To learn more about building form logic expressions in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

## Combining multiple constraint conditions
Multiple constraint conditions can be combined into a single expression to determine whether a response is valid. Conditions can be combined using **and**, **or**, and **not** logical operators:

- Use **and** when all conditions must be met for a response to be valid. 
    - For example: <code>. > 18 <strong>and</strong> . < 65</code>
- Use **or** when at least one condition must be met for a response to be valid.
    - For example: <code>. < 18 <strong>or</strong> ${student} = 'yes'</code>
- Use **not** to indicate that a condition or set of conditions must not be met (e.g., when two conditions cannot be true together for a response to be valid).
    - For example: <code><strong>not</strong>(. < 18 <strong>and</strong> ${household_head} = 'yes')</code>

**survey worksheet**

| type     | name   | label              | hint                                        | constraint                                               |
|:---------|:-------|:------------------|:--------------------------------------------|:---------------------------------------------------------|
| integer  | age    | What is your age? | Must be less than 18 or above 65 to participate | <code>. < 18 <strong>or</strong> . > 65</code>         |
| integer  | weight | How much do you weigh? | Must be between 30 and 200 kg               | <code>. >= 30 <strong>and</strong> . <= 200</code>     |
| survey |


## Customizing constraint error messages

By default, when a response value in the form does not meet the constraint condition, a “Value not allowed” error message appears. It is recommended to customize this message to inform users why the value is invalid, allowing them to correct their input.

To customize the constraint error message:
1. Add a **constraint_message** column to the `survey` worksheet.
2. In the `constraint_message` column, enter the text you wish to display as the error message when the constraint conditions are not met.

**survey worksheet**

| type    | name | label           | constraint | constraint_message     |
|:--------|:-----|:----------------|:-----------|:----------------------|
| integer | age  | What is your age? | . >= 18   | Must be older than 18. |

## Advanced constraints in XLSForm

Beyond basic constraints, you can customize conditions to ensure data quality and adapt to many data collection scenarios. To build more advanced constraint conditions in XLSForm:

- Use parentheses to combine more than two conditions
- Use [functions](https://support.kobotoolbox.org/functions_xls.html) for increased flexibility 
- Use [regular expressions](https://support.kobotoolbox.org/restrict_responses.html) to restrict text responses
  
Examples of more advanced validation criteria include:

| Criteria | Description |
|:---------|:------------|
| <code>(. >= 18 and . < 130) or (. = 999)</code> | The response must be between 17 and 130 or be equal to 999 (often used for non-response) |
| <code>not(${in_university} = 'yes' and . < 16)</code> | If the answer to `in_university` is ‘yes’, the current response must be greater than 16. |
| <code>not(selected(., 'none') and count-selected(.)>1)</code> | The ‘none’ option cannot be selected if any other response in a `select_multiple` question is selected. |
| <code>. < today()</code> | The date entered must be before today’s date. |
| <code>regex(., '^\d{2}$')</code> | The input is restricted to two numbers (using <a href="https://support.kobotoolbox.org/restrict_responses.html">regular expressions</a>). |


