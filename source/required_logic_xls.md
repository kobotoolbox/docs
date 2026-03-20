# Adding required logic in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/5c9f0c5e963d76d2f81701257272894d4f3f9405/source/required_logic_xls.md" class="reference">12 Jan 2026</a>

Required logic allows you to make a question mandatory if specific conditions are met. For example, you can require a phone number question only if respondents agree to be contacted in the future. This option provides more control than simply marking a question as always required or always optional.

<p class="note">
  To learn more about required questions and how to customize the message shown to respondents when they leave a required question unanswered, see <a href="https://support.kobotoolbox.org/question_options_xls.html#required-questions">Question options in XLSForm</a>.
</p>

This article explains how to add required logic conditions in XLSForm, including making a question required based on whether another question was answered. 

<p class="note">
  <strong>Note:</strong> This article focuses on adding required logic in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about adding required logic in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/question_options.html?highlight=custom+logic#mandatory-response">Question options in the Formbuilder</a>.
  <br><br>
  For hands-on practice with required logic in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Adding required logic conditions

Required logic uses <a href="https://support.kobotoolbox.org/form_logic_xls.html#question-referencing">question referencing</a> to make questions required based on previous answers. The question used to define the required logic is referred to as the **reference question.**

To add required logic in XLSForm:
1. Add a `required` column to the survey worksheet. 
2. In the row of the question you wish to set the required logic for, enter the condition that must be met in order **for the question to be mandatory.**

**survey worksheet**

| type         | name      | label                                                                     | required           |
|:--------------|:-----------|:--------------------------------------------------------------------------|:------------------|
| select_one yn | recontact  | Do you agree to being contacted again for another study in the future?    |                    |
| text          | email      | What is your email address?                                               | ${recontact} = 'yes' |
| survey | 

If a respondent does not answer a required question, they will not be able to proceed to the next page of the form or submit it. 

### Formatting required logic conditions

The format of the required logic condition will differ according to the **type of the reference question**, as detailed in the table below.

| Reference question type | Required logic condition | Example |
|:-------------------------|:--------------------|:---------|
| select_one | `${reference_question} = 'choice_name'` | `${consent} = 'yes'` |
| select_multiple | `selected(${reference_question}, 'choice_name')` | `selected(${reasons}, 'other')` |
| integer | `${reference_question}` followed by a logical operator (>, <, =) and a number (or a reference to another question) | `${age} >= 18` |
| date | `${reference_question}` followed by a logical operator (>, <, =) and `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
To learn more about building form logic expressions in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

## Adding required logic based on whether a question was answered

In addition to setting required logic for a specific response, you can also base it on whether a question was answered or left blank. This is useful when you want to ensure that at least one of two questions is required.

Unanswered questions are treated as empty strings, noted as two single apostrophes `''`. The following required logic conditions can be used:

| Required logic condition | Description |
|:---------------------------|:-------------|
| `${reference_question} != ''` | Require only if `reference_question` is answered (not blank). |
| `${reference_question} = ''`  | Require only if `reference_question` is unanswered (blank). |

**survey worksheet**

| type  | name    | label                                               | required     |
|:------|:--------|:----------------------------------------------------|:-------------|
| note  | contact | Please provide your phone number or email address below. |              |
| text  | phone   | Phone number                                        |              |
| text  | email   | Email address                                       | ${phone} = '' |
| survey | 
