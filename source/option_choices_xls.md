# Managing option choices in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/90ffcfbf27679c7831416efd108d4519cdaa668c/source/option_choices_xls.md" class="reference">25 Nov 2025</a>

XLSForm simplifies the creation and management of **option choice lists** for survey forms. This is particularly useful for long or repetitive lists, such as country or city names. Option choices are defined for `select_one`, `select_multiple`, or `rank` [questions](https://support.kobotoolbox.org/question_types_xls.html#select-question-types). 

This article details how to define and manage option choices in XLSForm for complex forms, including best practices for defining choice names.

<p class="note">
To learn more about building forms in XLSForm, see <a href="getting_started_xlsform.html">Getting started with XLSForm</a>.
</p>

## Defining option choices in XLSForm
Option choices are defined in the `choices` worksheet of your XLSForm. The `choices` worksheet includes three mandatory columns:

| Column | Description |
| :---------  | :--------  |
| `list_name` | Unique identifier for a list of option choices, which links the question in the `survey` worksheet to its choice list in the `choices` worksheet. |
| `name` | Short, unique name used to refer to each option choice. |
| `label` | Choice text as it will be displayed in the form. |

To define a list of option choices in XLSForm:

1.  In the `choices` worksheet, enter the **name of the list of choices** in the `list_name` column. 
2.  Enter a short `name` and a `label` for each option, using the same `list_name` for all options in the list.

**choices worksheet**

| list_name | name | label |
| :---------  | :---------  | :---------  |
| marital_options | single | Single |
| marital_options | married | Married |
| marital_options | separated_divorced | Separated/Divorced |
| marital_options | widowed | Widowed |
| choices |

3.  In the `survey` worksheet, add your survey question. In the `type` column, enter the question type followed by a single space and then the `list_name` for your list of choices.
    - A list of choices can be reused across multiple questions in the `survey` worksheet.

**survey worksheet**

| type | name | label |
| :---------  | :---------  | :---------  |
| acknowledge | consent | Do you agree to proceed with the interview? |
| select_one marital_options | marital_status | What is your marital status? |
| survey |

 
## Best practices for defining choice names

When data is downloaded in [XML values and headers format](https://support.kobotoolbox.org/export_download.html#value-and-header-format), each question appears as its own variable or column in the dataset. The values inside each column are the **choice names** defined in your `choices` worksheet, rather than the full labels shown to respondents. This format is recommended for analysis, since it provides short, consistent variable names and coded values that are easier to work with than full question or option labels.

When defining choice names:
- Use only **letters, numbers, and underscores**. Spaces and special characters are not allowed.
- Avoid very long or complex strings of text, as these values will appear in your exported dataset and may be used in [form logic](https://support.kobotoolbox.org/form_logic_xls.html).
- Keep names **consistent** across lists to facilitate data analysis.
 

## Managing choice lists in XLSForm

### Reusing choice lists
Using `list_name` in XLSForm allows you to easily **reuse choice lists** across multiple questions, eliminating the need for manual re-entry. For example, you can create a `yes_no` choice list and apply it to all your Yes/No questions. This helps build forms more efficiently and consistently.

### Translating choice lists

XLSForm simplifies the translation of choice lists. You can add multiple labels for different languages, with each translation in a separate `label` column. The underlying choice names remain the same, which ensures the exported dataset is consistent across translations and facilitates analysis.

<p class="note">
To learn more about adding translations in XLSForm, see <a href="language_xls.html">Adding translations in XLSForm</a>.
</p>

### Media files as option choices

In addition to text, option choices in XLSForm can also be **media files**, such as images, audio, or video. This enhances the survey experience by providing visual or auditory cues to respondents.

<p class="note">
To learn more about using media files as option choices, see <a href="media.html">Adding media to an XLSForm</a>.
</p>

### Filtering choice lists

XLSForm allows you to filter option choice lists based on responses to previous questions. This feature, known as **choice filters**, can be used in various ways. For example, they can be used for **cascading select questions**, where the choice list for a child question (e.g., cities) is filtered based on the response to a parent question (e.g., country). They can also be used for filtering a multiple choice question to display only options selected in a previous question.

<p class="note">
To learn more about filtering choice lists in XLSForm, see <a href="choice_filters_xls.html">Adding choice filters in XLSForm</a>.
</p>

### Duplicating choice names

Within a given list of option choices, **choice names must be unique**. However, the same choice name can be reused across different lists. For instance, a `yes_no` choice list and a `yes_no_maybe` choice list can both include `yes` and `no` choice names.

By default, deploying a form with repeated choice names in the same list will result in an error. However, when using choice filters, you may need to allow duplicate choice names within a list. To enable this, activate the `allow_choice_duplicates` setting in your `settings` worksheet.

<p class="note">
For more information, see <a href="form_settings_xls.html">Form settings in XLSForm</a>.
</p>

### Managing long choice lists

For very large choice lists, containing hundreds or thousands of options, it is recommended to use `select_one_from_file` or `select_multiple_from_file` question types, which link a survey question to an **external file** containing the list of choices. This approach is more efficient than manually entering choices inside the XLSForm, helps avoid slow loading times and large XLSForms, and simplifies managing or editing extensive option sets.

<p class="note">
To learn more about external choice lists in XLSForm, see <a href="select_from_file_xls.html">Selecting options from an external file</a>.
</p>

