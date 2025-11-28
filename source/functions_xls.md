# Using functions in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/580618d986f3783ca933169d5e0ec3108b490e76/source/functions_xls.md" class="reference">25 Nov 2025</a>

Functions are predefined operations used to perform calculations or manipulate data in XLSForm. They are essential for automating tasks and deriving key insights in your forms, allowing you to calculate project indicators, create scoring systems, and manage dates efficiently. 

This article lists common functions used in XLSForm, including functions to manipulate numbers, strings, dates, and GPS points.

<p class="note">
  To learn more about form logic in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>. To learn about functions specifically used in repeat groups, see <a href="https://support.kobotoolbox.org/repeat_groups_xls.html">Repeat groups in XLSForm</a>.
</p>

## Commonly used functions in XLSForm

The following functions are some of the most frequently used in XLSForm. They help control form behavior, manage responses, and perform basic calculations or logical operations across questions. These functions can be applied in calculations, constraints, relevance conditions, and other expressions throughout your form.

| Function | Description |
|:-----------|:-------------|
| `if(expression, then, else)` | If the expression is TRUE, returns `then`. If not, returns `else`. |
| `selected(${question_name}, option_name)` | Used to determine if a specific choice was selected in a `select_multiple` question. |
| `random()` | Returns a random number between 0.0 (inclusive) and 1.0 (exclusive). |
| `count-selected(${question_name})` | Returns the number of options selected in a `select_multiple` question. |
| `coalesce(${question1}, ${question2})` | Returns the first non-empty value of the two arguments. Returns an empty string if both are empty or non-existent. |
| `jr:choice-name(choice_name, '${question_name}')` | Returns the label value, in the active language, associated with the `choice_name` in the list of choices for a select type question. To retrieve the label of whichever response was selected, use `jr:choice-name(${question_name}, '${question_name}')`. |
| `selected-at(${question_name}, n)` | Returns the selected choice in a `select_multiple` question at position **n+1**. For example, `selected-at(${question_name}, 2)` returns the third choice selected in a `select_multiple` question. |
| `once(expression)` | Evaluates an expression only once (e.g., to ensure a random number is only generated once, or to store the first value entered for a question even if the response is changed later). |
| `instance('list_name')/root/item[name = ${question}]/column_name` | Retrieves a value from the choices sheet. Searches the choice list named `list_name`, finds the row where the choice `name` matches the response to `${question}`, and returns the value from the column specified as `column_name`. |

## Functions to manipulate numbers

The following functions are used to perform mathematical operations or transform numeric values in XLSForm. They can help you calculate, round, or convert numbers, as well as apply more advanced mathematical expressions when needed.

| Function | Description |
|:---------|:------------|
| `int(number)` | Transforms a decimal number into an integer without rounding. |
| `round(number, places)` | Rounds a decimal value to a predetermined number of decimal places. |
| `pow(number, power)` | Calculates the power of a number. |
| `number(x)` | Converts x (a string or boolean expression) to a number value. |
| `log(number)` <br> `log10(number)` | Returns the natural log or base-10 log of a number. |
| `abs(number)` | Returns the absolute value of a number. |
| `sin(number)` <br> `asin(number)` <br> `cos(number)` <br> `acos(number)` <br> `tan(number)` <br> `atan(number)` | Returns the sine/arc sine, cosine/arc cosine, or tangent/arc tangent of a number. |
| `sqrt(number)` | Returns the square root of a number. |
| `exp(x)` <br> `exp10(x)` | Returns e^x or 10^x. |
| `pi()` | Returns an approximation of the mathematical constant π. |

<p class="note">
  <strong>Note:</strong> Inside these functions, either constants or <a href="https://support.kobotoolbox.org/form_logic_xls.html#question-referencing">question references</a> can be included.
</p>

## Functions to manipulate strings

The following functions are used to create, modify, or analyze text strings in XLSForm. They are useful for combining text, checking for specific patterns or characters, and cleaning or formatting text inputs.

| Function | Description |
|:---------|:------------|
| `concat()` | Concatenates one or more arguments (separated by commas) into a single string. |
| `regex(string, expression)` | Returns `TRUE` if the string is an exact and complete match for a <a href="https://support.kobotoolbox.org/restrict_responses.html">regular expression</a>. |
| `contains(string, substring)` | Returns `TRUE` if the string contains the substring. |
| `starts-with(string, substring)` | Returns `TRUE` if the string begins with the substring. |
| `ends-with(string, substring)` | Returns `TRUE` if the string ends with the substring. |
| `substr(string, start[, end])` | Returns the substring of `string` beginning at the index start and extending to (but not including) index end (or to the termination of `string`, if end is not provided). |
| `substring-before(string, target)` | Returns the substring of `string` before the first occurrence of the target substring. If the target is not found, or `string` begins with the target substring, then this will return an empty string. |
| `substring-after(string, target)` | Returns the substring of `string` after the first occurrence of the target substring. If the target is not found this will return an empty string. |
| `translate(string, fromchars, tochars)` | Returns a copy of string, where every occurrence of a character in `fromchars` is replaced by the corresponding character in `tochars` (e.g., replacing all lowercase letters with uppercase letters). <br><br> <strong>Note:</strong> If `fromchars` is longer than `tochars`, every occurrence of a character in `fromchars` that does not have a corresponding character in `tochars` will be removed. |
| `string-length(string)` | Returns the number of characters in `string` (e.g., to add a word limit to a text question). |
| `normalize-space(string)` | Returns a string in which any leading and trailing whitespaces in the string are removed, and sequences of whitespaces are replaced with a single space. |

## Functions to manipulate dates

The following functions are used to record, format, and calculate date and time values in XLSForm. They can help capture the current date or time, convert text into date format, or display dates and times in a specific format.

| Function | Description |
|:---------|:------------|
| `today()` | Returns the current date without a time component. |
| `now()` | Returns the current date and time in ISO 8601 format, including the timezone. |
| `date('YYYY-MM-DD')` | Forces dates into the correct date format (especially for dates before 1970). |
| `format-date(date, format)` | Returns `date` as a string formatted as defined by <code>format</code>. Common formats include: <ul><li><code>%Y</code>: 4-digit year</li><li><code>%y</code>: 2-digit year</li><li><code>%m</code>: 0-padded month</li><li><code>%n</code>: numeric month</li><li><code>%b</code>: short text month (Jan, Feb, Mar…)</li><li><code>%d</code>: 0-padded day of month</li><li><code>%e</code>: day of month</li><li><code>%a</code>: short text day (Sun, Mon, Tue…).</li></ul> |
| `format-date-time(datetime, format)` | Returns `datetime` as a string formatted as defined by <code>format</code>. Common formats include: <ul><li><code>%H</code>: 0-padded hour (24-hr time)</li><li><code>%h</code>: hour (24-hr time)</li><li><code>%M</code>: 0-padded minute</li><li><code>%S</code>: 0-padded second</li><li><code>%3</code>: 0-padded millisecond ticks.</li></ul> |


## Functions to manipulate GPS data

The following functions are used to work with geographic data collected through GPS questions in XLSForm. They can calculate distances, perimeters, or areas based on geopoint, geotrace, or geoshape responses.

| Function | Description |
|:---------|:------------|
| `area(${geoshape})` | Returns the area, in square meters, of a `geoshape` value. |
| `distance(geo)` | Returns the distance, in meters, of either: <ul><li>the perimeter of a `geoshape` value</li><li>the length of a `geotrace` value</li><li>a list of geopoints either specified as strings or references to other fields (including from repeat groups), separated by commas</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Returns `TRUE` if the specified `${geopoint}` is inside the specified `${geoshape}`, `FALSE` otherwise. Supported only in KoboCollect. |

