# Adding a custom submission message

Custom submission messages allow you to display a tailored message after a respondent successfully submits a form.

Custom submission messages can be used to:

- **Confirm event registrations:** For example, to confirm registration, provide event details, and include a calendar download link.
- **Provide conditional incentives:** To display a message based on a respondent’s eligibility, such as a coupon code or thank you message.
- **Support follow-up workflows:** To display a ticket number, a summary of submitted data, or a link to the next step in a process.

This feature must be configured in [XLSForm](https://support.kobotoolbox.org/getting_started_xlsform.html).

## Configuring a custom submission message

To set up a custom submission message in XLSForm:

1. In the `settings` sheet, add three columns: `name`, `namespaces`, and `attribute::kobo:submitMessage` 
    - In the `name` column, enter `data`
    - In the `namespaces` column, enter `kobo="http://kobotoolbox.org/xforms"`
    - In the `attribute::kobo:submitMessage` column, enter `/data/submitMessage`.

**settings sheet**

| name | namespaces     | attribute::kobo:submitMessage              |
| :--- | :------- | :----------------- |
| text | kobo="http://kobotoolbox.org/xforms" | /data/submitMessage |
| settings |

2. In the `survey` sheet, create a `calculate` question. 
    - In the `name` column, enter `submitMessage`
    - In the `calculation` column, enter the confirmation message you wish to use.

**survey sheet**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- |:------------|
| calculate | submitMessage |  | `“Thank you for registering. Click [here](http://kobotoolbox.org) for more information about the event.”` |
| survey |

<p class="note">
  For an example of this feature in practice, download a sample XLSForm <a href="https://docs.google.com/spreadsheets/d/1CgjrpJcDX1pLmf-B-PUZ4-KFs2pPuntD/edit?usp=sharing&ouid=104272235398180261217&rtpof=true&sd=true">here</a>.
</p>

## Customizing the submission message

You can use functions and Markdown in the `calculation` column to customize the message.

### Using conditional statements

Use `if()` to display different messages based on form responses.

For example: `if(${eligible} = 'yes', 'You are eligible.', 'You are not eligible.')`

### Displaying choice labels

Use `jr:choice-name()` to display the [label](https://support.kobotoolbox.org/glossary.html#label) of a selected choice instead of its [choice name](https://support.kobotoolbox.org/glossary.html#choice-name).

For example: `concat('You are registered for ', jr:choice-name(${event}, '${event}'))`

### Formatting the submission message

Use Markdown to add formatting to the submission message, such as hyperlinks, bold text, italic text, or lists.

For example: `'**Congratulations!** You are eligible. Click [here](http://kobotoolbox.org) for more information.'`

<p class="note">
  For more information on formatting text using Markdown, see <a href="https://support.kobotoolbox.org/form_style_xls.html#styling-text">Styling your forms using XLSForm</a>.
</p>

## Creating submission messages in multiple languages

For multilingual forms, you can display the submission message in the language selected by the respondent.

To configure multilingual submission messages:

1. In the `survey` sheet, create a `select_one` question to store the message.
2. Enter `false` in the `relevant` column to hide the question in the form.
3. In the `choices` sheet, add the submission message as a choice.
4. [Translate](https://support.kobotoolbox.org/language_xls.html) the choice label into each form language.
5. In the `calculation` column of the `submitMessage` row, enter: `jr:choice-name('choice_name', '${question_name}')`
    - `choice_name` is the name of the choice where your message is stored
    - `question_name` is the name of the `select_one` question created above

The submission message will appear in the language selected at the top of the form.

<p class="note">
  For an example of a form that displays a submission message in multiple languages, download a sample XLSForm <a href="https://docs.google.com/spreadsheets/d/1NXwXbG6PaSFX1HZGEDMdji6XiUIHfkHG/edit?usp=sharing&rtpof=true&sd=true">here</a>.
</p>

## Compatibility

Custom submission messages are intended for use with [web forms](https://support.kobotoolbox.org/data_through_webforms.html). They work only with the following [data collection modes](https://support.kobotoolbox.org/data_through_webforms.html#data-collection-modes):

- Online-Only (single submission)
- Online-Only (once per respondent)

They may also appear in [KoboCollect](https://support.kobotoolbox.org/data_collection_kobocollect.html), but KoboCollect treats the message as plain text, so Markdown formatting and links are not rendered. Consider your data collection method and test the message before collecting data with your form.



