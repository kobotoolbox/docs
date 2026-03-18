# Using regular expressions in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/restrict_responses.md" class="reference">29 Jul 2025</a>

A **regular expression**, or regex, is a search pattern used to match specific characters or character ranges within text. Regular expressions are commonly used to validate, search, extract, or restrict text input.

In KoboToolbox, regular expressions are typically used to control how users enter data. For example, you can restrict a mobile number to exactly 10 digits, enforce a specific ID format, or limit text to uppercase letters only.

This article provides an overview of common regular expression components and practical examples you can use to validate and restrict text input in your forms.

<p class="note">
   To learn more about using regular expressions in your forms, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a> and <a href="https://support.kobotoolbox.org/form_logic.html">Introduction to form logic in the Formbuilder</a>. 
</p>

## Common regex components

Regular expressions in KoboToolbox are written inside the `regex()` function. For example, `regex(., '^[0-9]{10}$')` restricts an input to exactly 10 digits.

The following tables describe commonly used regex elements.

### Anchors and grouping

| Regex | Description |
|:---|:---|
| <code>^</code> | Matches the start of a string |
| <code>$</code> | Matches the end of a string |
| <code>( )</code> | Groups characters together |
| <code>\|</code> | Matches one pattern or another (logical OR) |

### Character classes

| Regex | Description |
|:---|:---|
| <code>[abc]</code> | Matches a, b, or c |
| <code>[a-z]</code> | Matches any lowercase letter |
| <code>[A-Z]</code> | Matches any uppercase letter |
| <code>[0-9]</code> | Matches any digit from 0 to 9 |
| <code>[a-zA-Z0-9]</code> | Matches letters or digits |
| <code>[^abc]</code> | Matches any character except a, b, or c |
| <code>[^A-Z]</code> | Matches any character except uppercase letters |

### Special character shortcuts

| Regex | Description |
|:---|:---|
| <code>\d</code> | Matches any digit (same as [0-9]) |
| <code>\D</code> | Matches any non-digit |
| <code>\w</code> | Matches any word character (letters, digits, _) |
| <code>\W</code> | Matches any non-word character |
| <code>\s</code> | Matches a space or tab |
| <code>\b</code> | Matches a word boundary |
| <code>\.</code> | Matches a literal dot (<code>.</code>) |
| <code>\@</code> | Matches a literal <code>@</code> |
| <code>\$</code> | Matches a literal <code>$</code> |
| `\\` | Matches a literal backslash (<code>\\</code>) |
| <code>\number</code> | Refers to a previously matched group |

### Quantifiers

| Regex | Description |
|:---|:---|
| <code>?</code> | Matches zero or one occurrence |
| <code>*</code> | Matches zero or more occurrences |
| <code>+</code> | Matches one or more occurrences |
| <code>{x}</code> | Matches exactly x occurrences |
| <code>{x,}</code> | Matches at least x occurrences |
| <code>{x,y}</code> | Matches between x and y occurrences |

## Common examples

The following examples can be used as [constraints](https://support.kobotoolbox.org/constraints_xls.html) or [validation criteria](https://support.kobotoolbox.org/validation_criteria.html).

### Common regex expressions with numbers

| Regex | Description |
|:---|:---|
| <code>regex(., '^\d+$')</code> | Limit input to numbers |
| <code>regex(., '^\d{2}$')</code> | Limit input to 2 digits |
| <code>regex(., '^\d{2,4}$')</code> | Limit input to 2-4 digits |
| <code>regex(., '^\d{10}$')</code> | Limit input to 10 digits |
| <code>regex(., '^[1-9][0-9]?$&#124;^100$')</code> | Limit input to a number between 1 and 100 (e.g., for a percentage) |
| <code>regex(., '^[1-9][0-9]{8}$')</code> | Limit input to 9 digits, first digit cannot be 0 |
| <code>regex(., '^\d{2}\.\d{3}$')</code> | Limit input to number formatted as 12.345 |
| <code>regex(., '^(\d{10}&#124;\d{13}&#124;\d{17})$')</code> | Limit input to 10, 13, or 17 digits |
| <code>regex(., '^(12&#124;345)$')</code> | Input must be 12 or 345 |

### Common regex expressions with letters

| Regex | Description |
|:---|:---|
| <code>regex(., '^\D*$')</code> | Limit input to letters, spaces, and symbols (no numbers) |
| <code>regex(., '^[A-Za-z]+$')</code> | Limit input to letters |
| <code>regex(., '^[A-Za-z\s]+$')</code> | Limit input to letters and spaces |
| <code>regex(., '^[a-z]{1,6}$')</code> | Limit input to 1–6 lowercase letters |
| <code>regex(., '^[A-Z]{1,10}$')</code> | Limit input to 1–10 uppercase letters |
| <code>regex(., '^(Apple&#124;Orange&#124;Banana)$')</code> | Input must match one word from the list |
| <code>regex(., '^colou?r$')</code> | Allows color or colour |
| <code>regex(., '^[A-Z\s]+$')</code> | Limit input to uppercase letters and spaces only |
| <code>regex(., '^[a-z_]+$')</code> | Limit input to lowercase letters and underscores (<code>_</code>) |

### Common regex expressions with letters and numbers

| Regex | Description |
|:---|:---|
| <code>regex(., '^\w{3}$')</code> | Limit input to exactly 3 letters, digits, or underscores (<code>_</code>) |
| <code>regex(., '^[A-Z]{1}[0-9]{8}$')</code> | Limit input to one letter and eight numbers |
| <code>regex(., '^CAR-PRC-2020-\d{4}$')</code> | Limit input to a specific ID format |
| <code>regex(., '^\W*(\w+\b\W*){3}$')</code> | Limit input to exactly 3 words |
| <code>regex(., '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*(\.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)*\.[a-zA-Z]{2,}$')</code> | Limit input to common email format |

<p class="note">
  For additional help building and testing patterns, visit: <a href="http://www.regexr.com/">http://www.regexr.com/</a>  
</p>


