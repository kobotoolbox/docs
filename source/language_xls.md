# Adding translations in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/e1bfb2942ae7721c6ebe1a23aa74295ca0ac2bb1/source/language_xls.md" class="reference">30 Dec 2025</a>

Adding translations to a form allows users to switch to their preferred language during data collection without creating separate forms. Any number of translations can be added. Both [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) and [Enketo web forms](https://support.kobotoolbox.org/enketo.html) support form translations.

Most elements displayed in the form can be translated, such as **question labels**, **hints**, **choice labels**, **constraint messages**, and **required messages**. Elements used for form structure, like question names, choice names, and list names, cannot be translated and should remain in the language used for form development and data analysis.

When your form includes multiple translations, KoboCollect and Enketo will display a language selector in the **top right corner of the form**, allowing respondents to choose their preferred language.

<p class="note">
  <strong>Note:</strong> Adding translations in XLSForm is faster and more efficient than <a href="https://support.kobotoolbox.org/language_dashboard.html">using the Formbuilder</a>, especially for longer forms. To learn how to download your form in XLSForm to add translations, see <a href="xlsform_with_kobotoolbox.html">Using XLSForm with KoboToolbox</a>.
<br><br>
For hands-on practice with adding translations in XLSForm, see KoboToolbox Academy's <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Language codes in XLSForm

When referring to different languages in XLSForm, you will need to use the format `language (code)` in your column headers. For example, the language reference for English is `English (en)` and the language reference for French is `French (fr)`. Each translation must use the same language name and code consistently throughout your form. 

Language codes can be found in the <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">IANA language subtag registry</a>. On the IANA website, the **Description** refers to the language name, and the **Subtag** refers to the language code (e.g., **Description:** French, **Subtag:** fr).


## Setting the default form language

To add translations to an XLSForm, first define the default language. This is the language the form will open to by default.

To define the default language of your form:
1. In the `settings` worksheet, add a `default_language` column.
2. In the `default_language` column, enter the default language using the `language (code)` format.
    - For example: `English (en)`.

**settings worksheet**

| default_language |
| :---------------- |
| English (en)      |
| settings |

To set up the `survey` worksheet:

1. Rename the `label` column using the format `label::language (code)`.
    - For example: `label::English (en)`.
2. If your form includes `hint`, `required_message`, `constraint_message`, or `media` columns in the `survey` worksheet, rename the existing columns using the format `column_name::language (code)`.
    - For example: `hint::English (en)`.

**survey worksheet**

| type | name | label::English (en) | hint::English (en) |
| :--- | :--- | :------------------ | :----------------- |
| integer | age | How old are you? | In years |
| select_one yn | student | Are you currently a student? | |
| survey |

Finally, to set up the `choices` worksheet, rename the `label` column using the format `label::language (code)`.

**choices worksheet**

| list_name | name | label::English (en) |
| :--------- | :--- | :------------------ |
| yn | yes | Yes |
| yn | no | No |
| choices |

## Adding translations

Once you have defined your default language, you can add translations for each visible element of your form. You can add as many translation columns as you like.

<p class="note">
  <strong>Note:</strong> If you omit text for a translated element, it will appear as a blank field on the form.
</p>

To add translations to the `survey` worksheet:
1. Add a new `label` column for each translation language using the format `label::language (code)`.
    - For example: `label::Spanish (es)`.
2. If your form includes `hint`, `required_message`, `constraint_message`, or `media` columns in the `survey` worksheet, set up the corresponding translation columns using the `column_name::language (code)` format.
    - For example: `hint::French (fr)` or `required_message::Chichewa (ny)`.
3. Enter the translations for all form elements in the relevant columns.

<p class="note">
  To learn more about managing media files in translated forms, see <a href="https://support.kobotoolbox.org/media.html#adding-media-to-translations">Adding media to translations</a>.
</p>

**survey worksheet**

| type | name | label::English (en) | label::Chichewa (ny) | hint::English (en) | hint::Chichewa (ny) |
| :--- | :--- | :------------------ | :------------------- | :----------------- | :------------------ |
| integer | age | How old are you? | Muli ndi zaka zingati? | In years | M'zaka |
| select_one yn | student | Are you currently a student? | Kodi panopa ndinu wophunzira? | | |
| survey |

To add translations to the `choices` worksheet:
1. Add a new `label` column for each translation language using the format `label::language (code)`.
    - For example: `label::Spanish (es)`.
2. Enter the translation for each choice label in the relevant translation column.
3. If your `choices` worksheet includes media columns, set up the corresponding translation columns using the `column_name::language (code)` format.

<p class="note">
  <strong>Note:</strong> To learn more about managing media files in translated forms, see <a href="https://support.kobotoolbox.org/media.html#adding-media-to-translations">Adding media to translations</a>.
</p>

**choices worksheet**

| list_name | name | label::English (en) | label::Chichewa (ny) |
| :--------- | :--- | :------------------ | :------------------- |
| yn | yes | Yes | Inde |
| yn | no | No | Ayi |
| choices |


## Guidelines for translations

### Using spreadsheet features for bulk translations

XLSForm makes it easy to translate form elements in bulk, instead of entering translations one by one. For example, you can copy an entire column into a translation system for bulk translation, and paste the column back into your XLSForm. If you are using Google Sheets to build your XLSForm, you can use the `GOOGLETRANSLATE()` formula to automate the translation process.

Machine translations should always be reviewed and validated by a fluent speaker to ensure accuracy, cultural appropriateness, and proper context. This step helps maintain the quality and reliability of your translated content.

### Translating to non-Latin scripts

Non-Latin scripts such as Arabic, Cyrillic, Tamil, Nepali, or Hindi are fully supported in KoboToolbox and can be used for default languages or translations.

<p class="note">
  <strong>Note:</strong> It is recommended to use only Latin characters for question and choice <strong>names</strong>, because non-Latin scripts may cause errors or compatibility issues when exporting data or working with XLSForm, but question and choice <strong>labels</strong> can safely use any script.
</p>

When adding translations in non-Latin scripts, it is essential to **use proper Unicode characters**. Unicode ensures that text is correctly displayed and understood across all devices and platforms.

To enter Unicode text, you do not need to install any special fonts. Instead, set your system keyboard to the appropriate language or script and type as you normally would. Avoid using pseudo fonts (i.e., special fonts that visually mimic non-Latin scripts by reassigning Latin characters), as these are not compatible with KoboToolbox and can cause serious display and data integrity issues. If you are using Windows and need help setting up your system keyboard, refer to [Microsoft documentation](https://support.microsoft.com/en-us/windows/manage-the-language-and-keyboard-input-layout-settings-in-windows-12a10cb4-8626-9b77-0ccb-5013e0c7c7a2).

### Translating right-to-left scripts

When adding a language that uses a right-to-left (RTL) script, such as Arabic, Hebrew, or Urdu, it is important to **use the correct language code** and to ensure the **first visible text in the translation** (e.g., a question label, hint, or note) is written in the RTL language. This will ensure that the form's layout does not default to left-to-right (LTR) formatting.

Additionally, when incorporating question references within question labels using RTL scripts, please note that the question reference syntax is reversed (i.e., `{question_name}$`).

**survey worksheet**

| type | name | label::English (en) | label::Arabic (ar) |
| :--- | :--- | :------------------ | :----------------- |
| begin\_group | profile | Respondent profile | ملف المستجيب |
| text | name | Respondent's name | اسم المدعى عليه |
| integer | age | How old is ${name}? | ؟{name}$ كم عمرك |
| end\_group | | | |
| survey |
