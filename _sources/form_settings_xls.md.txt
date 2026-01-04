# Form settings in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/1b55b2580defd73765e9c2ad608141a3428ee504/source/form_settings_xls.md" class="reference">4 Jan 2026</a>

XLSForm allows you to configure settings for your forms using the `settings` worksheet. For example, you can specify a form title, set a default language, or track version numbers. 

This article covers how to add and utilize the available form settings in XLSForm.

<p class="note">
<strong>Note:</strong> This article focuses on form settings forms in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about configuring form settings in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/form_meta.html">Form settings and metadata</a>.
</p>

## Adding form settings in XLSForm

To add form settings in XLSForm:
1. Add a `settings` worksheet to your XLSForm. 
2. Create a new column for each setting, using the exact column name shown [in the table below](https://support.kobotoolbox.org/form_settings_xls.html#available-form-settings-in-xlsform).
3. Under each setting, specify the relevant value (see example below).

**settings worksheet**

| form_title            | version | default_language | style |
|:----------------------|:--------|:----------------|:------|
| Form settings in XLSForm | v3     | English (en)    | pages |
| settings | 

## Available form settings in XLSForm

Available form settings in XLSForm include:

| Form setting               | Description |
|:----------------------------|:------------|
| <code>form_title</code>     | Specifies the title of the form that is shown to users. This can also be set and managed in KoboToolbox when the form is uploaded. |
| <code>version</code>        | Includes a string that represents the current version of the XLSForm (e.g., v1 or YYYYMMDD). Useful for tracking form versions for collaboration. |
| <code>instance_name</code>  | Specifies a unique name for each form submission using fields filled in by the user during the survey. Appears in the data table for each submission. Can be used to create custom participant or submission IDs.<br><br>For example, <code>concat(${lname}, '-', ${fname}, '-', today())</code> returns <code>lastname-firstname-date</code>. |
| <code>default_language</code> | Sets the default language in <a href="https://support.kobotoolbox.org/language_xls.html">translated forms</a>. The <code>language (code)</code> format is used, as defined in the <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">IANA language registry website</a>. |
| <code>style</code>          | Specifies an <a href="https://support.kobotoolbox.org/form_style_xls.html">alternative theme for Enketo web forms</a>. |
| <code>allow_choice_duplicates</code> | Allows an XLSForm to reuse duplicated option names <strong>within</strong> a choice list (e.g., when using choice filters where choice names are duplicated). |
| <code>public_key</code>     | Specifies the public key for <a href="https://support.kobotoolbox.org/encrypting_forms.html?highlight=encryption">encryption-enabled forms</a>. |

