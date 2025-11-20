# Adding calculations in XLSForm

Calculations can be used inside your form to derive new variables, build advanced form logic, and display results to respondents during data collection.

Calculations are processed within the form, helping save time during data analysis. The results are stored as new columns in the final dataset and can be used throughout the form to apply [skip logic](https://support.kobotoolbox.org/skip_logic_xls.html), set [constraints](https://support.kobotoolbox.org/constraints_xls.html), or display [dynamic content](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) in question labels and notes.

This article explains how to add calculations in XLSForm, covering both basic arithmetic and more advanced expressions.

<p class="note">
<strong>Note:</strong> This article focuses on adding calculations in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about adding calculations in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/calculate_questions.html">Calculate question type</a>.
<br><br>
For hands-on practice with calculations in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Adding calculations in XLSForm

Calculation expressions are constructed using a combination of [question references](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing), [mathematical operators](https://support.kobotoolbox.org/form_logic_xls.html#mathematical-and-comparison-operators), [functions](https://support.kobotoolbox.org/functions_xls.html), and constants.

To add a calculation in your XLSForm:
1. In the `type` column of the `survey` worksheet, enter **calculate** to add a `calculate` question type. 
2. Enter a `name` for the `calculate` question. 
    - Because the calculation is not displayed in the form, the `calculate` question does not require a **label**.
3. Add a **calculation** column in the `survey` worksheet.
4. In the `calculation` column, enter the **calculation expression.** 
    - Calculations can range from [basic arithmetic calculations](https://support.kobotoolbox.org/calculations_xls.html#arithmetic-calculations) to [advanced calculations](https://support.kobotoolbox.org/calculations_xls.html#advanced-calculations) using functions and regular expressions.
  
To refer to the calculation output in the rest of your form (e.g., inside a note question, question label, or form logic), use the [question referencing](https://support.kobotoolbox.org/form_logic_xls.html#question-referencing) format **${question_name}**, where `question_name` is the **name** of the `calculate` question.

**survey worksheet**

| type      | name          | label                          | calculation           |
|:----------|:--------------|:-------------------------------|:----------------------|
| integer   | bags          | Total number of bags sold       |                       |
| decimal   | price         | Price per bag                   |                       |
| calculate | total_amount  |                                | ${bags} * ${price}    |
| note      | display_total | The total is ${total_amount}    |                       |
| survey | 

## Arithmetic calculations

Calculations in XLSForm can range from simple arithmetic calculations to advanced derivation of variables.

Arithmetic calculations allow you to perform basic calculations using the following **operators**:

| Operator | Description |
|:----------|:-------------|
| <strong>+</strong>   | Addition |
| <strong>-</strong>   | Subtraction |
| <strong>*</strong>   | Multiplication |
| <strong>div</strong> | Division |
| <strong>mod</strong> | Modulo (calculates the remainder of a division) |

Calculations in XLSForm follow the **BODMAS** rule for the order of mathematical operations: **B**rackets, **O**rder of powers, **D**ivision, **M**ultiplication, **A**ddition, and **S**ubtraction. This means that calculations within brackets (or parentheses) are performed first, followed by powers, then divisions, multiplications, and so on. Using brackets correctly ensures that your calculations function as expected. 

## Advanced calculations

Advanced calculations in XLSForm often rely on **functions** and **regular expressions** to make calculations more efficient. 
* **Functions** are predefined operations used to automatically perform complex tasks like rounding values, calculating powers, or extracting the current date.
* **Regular expressions (regex)** are search patterns used to match specific characters within a string of text.

<p class="note">
  For a comprehensive list of functions available in XLSForm, see <a href="https://support.kobotoolbox.org/functions_xls.html">Using functions in XLSForm</a>.  To learn more about regular expressions, see <a href="https://support.kobotoolbox.org/restrict_responses.html">Restricting text responses with regular expressions</a>.
</p>

Examples of more advanced calculations include:

| Calculation | Description |
|:-------------|:-------------|
| `int((today()-${DOB}) div 365.25)` | Calculate age from date of birth. |
| `int(today()-${date})` | Calculate days since a date. |
| `format-date(${date}, '%b')` | Return just the month from a date. |
| `concat(${first}, " ", ${middle}, " ", ${last})` | Create a single string with a respondent’s full name. |
| `jr:choice-name(${question1}, '${question1}')` | Return a choice’s label, in the current language, from the choice list. |
| `translate(${full_name}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "abcdefghijklmnopqrstuvwxyz_")` | Convert uppercase letters to lowercase and spaces to underscores. |
| `substr(${question}, 1, 2)` | Keep only the 1st letter or number in a string. |
| `int(random()*10)` | Generate a random number between 0 and 10. |
| `selected-at(${gps}, 0)` | Isolate latitude from GPS coordinates. |
| `selected-at(${gps}, 1)` | Isolate longitude from GPS coordinates. |
| `if(regex(${id}, '^ML-'), 'yes', 'no')` | Create a binary variable that takes `yes` if the respondent ID starts with “ML-”. |

### Setting dynamic default responses

The `calculation` field can also be used to set **dynamic default responses.** Dynamic default responses allow you to display a default response inside a question based on a previous response. 

To set a dynamic default response:
1. In the `calculation` column, enter the **reference to the question** that will dynamically populate the default response. 
2. In the `trigger` column, enter the question that will activate the calculation. 
    - Typically, this would be the same question referenced in the `calculation` column, so that any change to the trigger question will also update the default response.

**survey worksheet**

| type | name       | label                     | calculation | trigger     |
|:------|:-----------|:--------------------------|:-------------|:-------------|
| text  | hh_name    | Name of the head of household |             |              |
| text  | phone      | Household phone number     |              |              |
| text  | phone_name | Name of the phone owner    | ${hh_name}   | ${hh_name}   |
| survey | 

<p class="note">
<strong>Note:</strong> If you want to prevent users from editing the field, set the <code>read_only</code> column to <code>TRUE</code>.
</p>

## Troubleshooting

<details>
  <summary><strong>Troubleshooting recommendations</strong></summary>
  To facilitate troubleshooting, display calculation outputs in a note while developing your form. This helps determine if the calculation is evaluating correctly and makes identifying issues easier. You can also break down long expressions into smaller ones and display the output of each to pinpoint problems. 
</details>

<br>

<details>
  <summary><strong>Calculations not working properly</strong></summary>
  If your calculations are not working, check the following:
  <ul>
  <li><strong>Syntax:</strong> All opened parentheses are closed, straight quotes are used ('), and commas are included where needed.</li>
  <li><strong>References:</strong> Question references correctly match the question name, no spaces or typos, no circular references (i.e., the calculation does not depend on itself).</li>
  <li><strong>Data types:</strong> Numeric and string calculations are not combined within the same question, data types are used correctly.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Dealing with empty fields</strong></summary>
  Unanswered questions are treated as empty strings and will not automatically convert to zero. When an empty value is used in a calculation, it results in "Not a Number" (NaN). To convert empty values to zero for calculations, use the <code>coalesce()</code> or <code>if()</code> <a href="https://support.kobotoolbox.org/functions_xls.html">functions</a>. For example:
  <ul>
  <li><code>coalesce(${potentially_empty_value}, 0)</code></li>
  <li><code>if(${potentially_empty_value}="", 0, ${potentially_empty_value})</code></li>
</ul>
  Another option is to set default values for each of the numeric variables to 0 in the <code>default</code> column.
</details>

<br>

<details>
  <summary><strong>Calculations keep changing in the form</strong></summary>
  Expressions are re-evaluated as an enumerator progresses through a form. This is especially important for <a href="https://support.kobotoolbox.org/functions_xls.html">functions</a> not connected to fields in the form, such as <code>random()</code> or <code>now()</code>, as their values may change under these conditions.
<br><br>
Expressions are re-evaluated when:
  <ul>
  <li>A form is opened</li>
  <li>The value of any question in the calculation changes</li>
  <li>A repeat group is added or deleted</li>
  <li>A form is saved or finalized</li>
</ul>
  To control when an expression is evaluated, set a <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">trigger</a> to evaluate it only when a given question is answered, or the function <code>once()</code> to ensure the expression is only evaluated once (e.g., <code>once(random())</code> or <code>once(today())</code>).
</details>
