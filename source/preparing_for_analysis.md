# Preparing your form for data analysis
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/9751288d763fc7db0fce24b02e91750f51ea710f/source/preparing_for_analysis.md" class="reference">17 Jul 2026</a>

Many data quality problems do not begin during analysis, but during data collection. Decisions made when building a form, such as how questions are structured, how option choices are named, and how missing data is handled, can affect how much cleaning and preparation is required later.

KoboToolbox includes several tools that **support high quality data collection** and help prepare your data for analysis in the long run. 

This article covers recommendations for **designing forms that produce cleaner, more consistent data**, from using form logic and calculations to planning question and choice names, and downloading your XLSForm as a data dictionary.

## Collecting coherent and consistent data

One of the most effective ways to improve your analysis is to prevent errors during data collection. KoboToolbox includes form logic functionalities that can help you collect more accurate and consistent responses.

### Validation criteria

[Validation criteria](https://support.kobotoolbox.org/glossary.html#validation-criteria) help ensure that respondents provide valid answers. For example, you can use validation criteria to:

- Restrict age to realistic values
- Prevent dates of birth from being entered in the future
- Require phone numbers to follow a specific format

Validation criteria are especially useful for questions where answers must fall within a specific range or follow a predictable format.

### Skip logic

[Skip logic](https://support.kobotoolbox.org/glossary.html#skip-logic) helps ensure that respondents only see questions that are relevant to them. For example, a respondent who reports never being pregnant should not be asked questions about previous pregnancies.

Asking the right questions to the right people improves data quality and reduces the burden on respondents. It also reduces the amount of cleaning or data removal required later.

<p class="note">
  To learn more about form logic, see <a href="https://support.kobotoolbox.org/form_logic.html">Introduction to form logic in the Formbuilder</a>.
</p>

## Anticipating the format of your data exports

The way you define [question names](https://support.kobotoolbox.org/glossary.html#question-name) and [choice names](https://support.kobotoolbox.org/glossary.html#choice-name) affects how easy your data is to work with after export. **Question names** become column names in your exported dataset, while **choice names** represent response values for select questions.

For best results, follow the recommendations below.

### Use clear formatting

Use question and choice names that are short, informative, unique, and free of spaces and special characters (e.g., `age`, `sex`, or `district`).

Clear names make your exported data easier to read, process, and analyze in external tools.

### Keep names consistent

Keep question and choice names consistent across forms whenever possible. If multiple surveys collect the same information, **using the same variable names** makes it easier to combine and compare datasets.

- For example, if one form uses `district` and another form uses `location_district` for the same type of information, you may need to rename variables before combining the datasets.

Similarly, using standard **choice names** makes analysis easier and reduces the need for recoding data later. 

- For example, you can use `0` for “No” and `1` for “Yes” across all relevant questions in your form.

### Avoid changing names after data collection starts

Once data collection has started, **avoid modifying question names or choice names.** Changing them can create inconsistencies between existing and new submissions.

If you need to update labels shown to respondents, edit the question label but keep the question name the same whenever possible.

<p class="note">
  For more information, see <a href="https://support.kobotoolbox.org/deploy_form_new_project.html#best-practices-for-deploying-and-redeploying-forms">Best practices for deploying and redeploying forms</a>.
</p>

### Use prefixes and suffixes

When forms contain related variables, consistent naming conventions can help organize your data. Consider **using a prefix or suffix** for questions or choices related to the same topic or format.

For example:

- Use `household_` for household-related questions, such as `household_size` or `household_income`
- Use `_other` for “Other, specify” questions, such as `income_source_other`

<p class="note">
<strong>Note:</strong>
  Question and choice names remain the same across form languages. This makes multilingual data easier to analyze after export.
</p>

## Anticipate analysis needs

When designing a form, think about the analyses you may want to perform later. Planning ahead can reduce the amount of processing required after export.

### Use calculations for analysis variables

[Calculations](https://support.kobotoolbox.org/glossary.html#calculation) can create variables that would otherwise require additional processing after export. For example, you can use calculations to create:

- Respondent age based on date of birth
- Household size totals
- Body mass index (BMI)
- Scores or indicators based on several responses

Creating these variables during data collection can save time and improve consistency across analyses.

<p class="note">
  To learn more about adding calculations, see <a href="https://support.kobotoolbox.org/calculate_questions.html">Adding calculations in the Formbuilder</a>.
</p>

### Plan for missing data

When analyzing data, it is important to know **why information is missing.** A response may be missing because the question was skipped, unavailable, not remembered, not applicable, or deliberately withheld.

A common best practice is to [make questions required](https://support.kobotoolbox.org/question_options.html#mandatory-response) while providing explicit response options, such as:

- Prefer not to say
- Don’t know
- Don’t remember
- Not applicable

This helps reduce unexplained missing data and makes results easier to interpret during analysis.

### Choose appropriate question types

Use **open-ended questions** when you need detailed, descriptive, or qualitative information that cannot be captured through predefined options. [Text](https://support.kobotoolbox.org/text_questions.html) and [audio](https://support.kobotoolbox.org/photo_audio_video_file.html) questions can be especially useful for collecting explanations, experiences, opinions, and other contextual information.

Use **structured question types** rather than open-ended questions when responses can be standardized:

- Use [multiple choice questions](https://support.kobotoolbox.org/select_one_and_select_many.html) when responses can fit into predefined options. 
- Use [date questions](https://support.kobotoolbox.org/date_time.html) when collecting calendar dates. 
- Use [GPS questions](https://support.kobotoolbox.org/gps_questions.html) or [cascading select questions](https://support.kobotoolbox.org/cascading_select.html) when collecting location information.

Choose the question type based on the information you need and how you plan to analyze it.

## Use your XLSForm as a data dictionary

The [XLSForm](https://support.kobotoolbox.org/edit_forms_excel.html) behind your KoboToolbox form can serve as a data dictionary. It documents your form structure, question names, choice names, labels, translations, question types, and form logic.

To download your form’s XLSForm:

1. Open your project.
2. Go to **FORM.**
3. Click <i class="k-icon-more"></i> **More actions.**
4. Click <i class="k-icon-file-xls"></i> **Download XLS.**

Each row in the `survey` tab represents a question in your form, and each column provides information about that question, such as the question name, label, type, translations, and relevant form logic. For select questions, [option choices](https://support.kobotoolbox.org/option_choices_xls.html) are listed in the `choices` tab.

Keeping your XLSForm with your exported dataset can make it easier to interpret variables, understand response values, and document your analysis workflow.

<p class="note">
  To learn more about XLSForm, see <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">Getting started with XLSForm</a> and <a href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Using XLSForm with KoboToolbox</a>.
</p>

