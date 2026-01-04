# Using question options in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/73c93af0ec1e54a26a64da395d94fffcc924344f/source/question_options_xls.md" class="reference">25 Nov 2025</a>

When designing a form in XLSForm, you can customize questions by adding hints, setting appearances, making a question mandatory, and more. To do this, you can add new columns in the `survey` worksheet of your XLSForm. These columns can be added anywhere in the worksheet, as long as the column name is typed exactly as required. 

This article covers the most common question options and how to add them to your XLSForm, including question hints, required questions, default responses, and question parameters.

<p class="note">
  <strong>Note:</strong> This article focuses on defining question options in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about question options in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/question_options.html">Using the question options</a>.
<br><br>
For hands-on practice with question options in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Question hints

**Question hints** allow you to add instructions or additional information to your form. There are two types of hints that you can add in XLSForm: 
- **Regular hints** are used to provide additional information for respondents or enumerators directly in the form. They are always visible and displayed below the question label.
- **Guidance hints** are used to provide additional information during form development, enumerator training, or data collection. They are not displayed by default.

### Adding question hints in XLSForm

To add a **regular hint** in XLSForm:
1. Add a `hint` column to the survey worksheet.
2. In the same row as your question, enter the text that should be displayed as a hint for that question.

To add a **guidance hint** in XLSForm:
1. Add a `guidance_hint` column to the survey worksheet.
2. In the same row as your question, enter the text that should be included as additional guidance.

**survey worksheet**

| type | name | label | hint | guidance_hint |
| :--- | :--- | :--- | :--- | :--- |
| integer | height | What is your height? | In centimeters | If the respondent does not know their height, enter 0 |
| survey |

<p class="note">
<strong>Note:</strong> Question hints can also be translated into multiple languages. For more information on translating forms, see <a class="reference" href="https://support.kobotoolbox.org/language_xls.html">Adding translations in XLSForm</a>. 
</p>

### Displaying guidance hints in KoboCollect 

In Enketo web forms, guidance hints appear in a collapsible **More Details** section. In KoboCollect, they are hidden by default, but you can [change your project settings](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) to always display them or show them in a collapsible section. 

To display guidance hints in KoboCollect, follow the steps below:
1. Tap the **Project icon** in the top right corner of your screen. 
2. Tap **Settings**. 
3. Under **Form management**, select **Show guidance for questions**. 
4. Choose a display option: **No**, **Yes - always shown**, or **Yes - collapsed**.

<p class="note">
<strong>Note:</strong> Guidance hints are always displayed in printed forms. 
</p>

## Required questions

By default, questions in a form are optional. Setting a question as **required** makes it mandatory for the respondent to answer. This can be useful for ensuring submissions are complete and avoiding missing data. 

<p class="note">
<strong>Note:</strong> Skip logic conditions take precedence over <strong>required</strong> settings, meaning that if a required question is hidden by skip logic, it is no longer mandatory to answer. 
</p>

To set a question as required in XLSForm: 
1. Add a `required` column to the survey worksheet. 
2. In the `required` column, enter any of the following: `TRUE`, `true`, or `yes`. 
3. For optional questions, leave the `required` column blank or enter any of the following: `FALSE`, `false`, or `no`.

If a respondent does not answer a required question, they will not be able to proceed to the next page or submit the form. The default required message "This field is required" will be displayed. 

<p class="note">
<strong>Note:</strong> Only questions that require an input should be marked as required in your XLSForm. If <code>note</code> questions are marked as required, you will not be able to continue or submit the form. 
</p>

### Changing the default required message 

You can change the default required message in your XLSForm by following the steps below:

1. Add a `required_message` column to the survey worksheet. 
2. Enter the text you wish to display when users leave a required question blank.

**survey worksheet**

| type | name | label | required | required_message |
| :--- | :--- | :--- | :--- | :--- |
| select_one education | education_level | What is the highest level of education you have completed? | TRUE | |
| integer | age | What is your age? | TRUE | Please respond to this question before continuing. |
| survey | 

<p class="note">
<strong>Note:</strong> Custom form logic can be used to make a question required or optional based on a previous response. To learn more about condition-based required logic, see <a class="reference" href="https://support.kobotoolbox.org/required_logic_xls.html">Adding required logic in XLSForm</a>. 
</p>

## Default responses

A **default response** populates a question with a predefined answer based on a common or expected response. The default response can be fixed or [dynamically determined](https://support.kobotoolbox.org/question_options_xls.html#setting-dynamic-default-responses) based on the response to a previous question. 

The default response will be recorded as the final answer when the form is submitted **unless modified by the respondent** during data collection.  To prevent respondents from editing a default response, add a `read-only` column and set it to `TRUE`. 

<p class="note">
<strong>Note:</strong> Although default responses can make data collection more efficient by prepopulating the form with expected or common responses, they also risk introducing bias or errors in the data, and should be used with caution. 
</p>

To set a fixed default response in XLSForm: 
1. Add a `default` column to the survey worksheet. 
2. Enter the default response, following the [appropriate format](https://support.kobotoolbox.org/question_options_xls.html#default-response-format) for the question type.

**survey worksheet**

| type | name | label | default |
| :--- | :--- | :--- | :--- |
| text | name | What is your name? | John Doe |
| integer | age | What is your age? | 50 |
| select_one marital_options | marital_status | What is your marital status? | married |
| select_multiple income_options | income_sources | What are your sources of income? | formal_work farm_business |
| date | dob | When were you born? | 1990-03-25 |
| date | interview_date | When was this interview conducted? | today() |
| survey |

### Default response format

The format of the default response depends on the question type and the data being collected: 

| Question type | Default response format |
| :--- | :--- |
| integer | Number |
| text | Text (without quotation marks) |
| select_one | Choice **name** (as defined in the choices worksheet) |
| select_multiple | Choice **name(s)**, separated by a **space** if there are multiple |
| date | Date in the YYYY-MM-DD format. If needed, prefix the date with a single quote (') in Excel to avoid potential formatting issues. | 

### Setting dynamic default responses

Default responses entered in the `default` field must be fixed values. To set a **dynamic default response** based on a previous answer, use the `calculation` and `trigger` columns instead of the `default` column: 
1. In the `calculation` column, enter the **reference to the question** that will dynamically populate the default response. 
2. In the `trigger` column, enter the question that will activate the calculation. 
    - Typically, this would be the same question referenced in the `calculation` column, so that any change to the trigger question will also update the default response. 

**survey worksheet**

| type | name | label | calculation | trigger |
| :--- | :--- | :--- | :--- | :--- |
| text | hh_name | Name of the head of household | | |
| text | phone | Household phone number | | |
| text | phone_name | Name of the phone owner | ${hh_name} | ${hh_name} |
| survey | 


## Question parameters

Question parameters in XLSForm allow you to fine-tune how your questions behave beyond basic settings. 

To add question parameters in XLSForm: 
1. Add a `parameters` column to the survey worksheet.
2. Enter the appropriate [parameter](https://support.kobotoolbox.org/question_options_xls.html#common-question-parameters) for your question type. 
3. Some parameters can be combined and applied to the same question. Combine parameters by entering them in the same cell and separating them with a space.

**survey worksheet**

| type | name | label | parameters |
| :--- | :--- | :--- | :--- |
| select_one reasons | reasons | Please select all reasons that apply. | randomize=true |
| range | phone | Please select a number between 1 and 5. | start=1 end=5 step=1 |
| survey | 

### Common question parameters

Different question types in XLSForm have different parameters. The most common parameters are: 

| Parameter | Question type | Description |
| :--- | :--- | :--- |
| randomize=true | rank, select_one, select_multiple | Randomizes the order of option choices |
| start=1 end=5 step=1 | range | Defines the minimum value, maximum value, and interval between numbers |
| capture-accuracy=20 | geopoint | Specifies the minimum acceptable GPS accuracy (in meters) for automatically capturing a location |
| warning-accuracy=50 | geopoint | Triggers a warning message if the GPS accuracy is not within the specified accuracy threshold |
| max-pixels=480 | image | Limits the maximum pixels for a photo, to reduce the image file size and improve upload speed |
| quality=low | audio | Captures a lower quality audio recording |
| quality=voice-only | audio | Captures the lowest quality audio recording |

## Additional question options

XLSForms can include additional columns in the survey worksheet for more advanced forms and functionalities. A few are listed below.

| XLSForm column | Description |
| :--- | :--- |
| read_only | If `yes` is entered in the `read_only` field, the question cannot be edited by the respondent. `read_only` fields can be combined with `default` or `calculation` fields to display information to the respondent. | 
| trigger | The trigger column can be used to run a calculation only when the response to another visible question in the form is changed. For more information, see <a href="https://xlsform.org/en/#trigger">XLSForm documentation</a>. | 
| body::accept | To limit the accepted file types for `file` questions, specify file extensions in the `body::accept` column, separated by a comma (e.g., .pdf, .doc). | 

Other columns can also be added to incorporate form logic into your XLSForm. 

<p class="note">
    To learn more about adding form logic, see <a href="https://support.kobotoolbox.org/skip_logic_xls.html">Adding skip logic in XLSForm</a>, <a href="https://support.kobotoolbox.org/constraints_xls.html">Adding constraints in XLSForm</a>, <a href="https://support.kobotoolbox.org/required_logic_xls.html">Adding required logic in XLSForm</a>, <a href="https://support.kobotoolbox.org/choice_filters_xls.html">Adding choice filters in XLSForm</a>, and <a href="https://support.kobotoolbox.org/calculations_xls.html">Adding calculations in XLSForm</a>.
</p>
