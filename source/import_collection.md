# Importing library collections using XLSForm

A **collection** is a group of related questions, question blocks, and templates organized in your [KoboToolbox library](https://support.kobotoolbox.org/question_library.html). Collections help you manage reusable content by project, theme, country, or organization.

You can import multiple questions or question blocks at once as a collection using an [XLSForm](https://support.kobotoolbox.org/getting_started_xlsform.html). This approach is useful when preparing standardized question sets outside the [Formbuilder](https://support.kobotoolbox.org/formbuilder.html) or migrating existing XLSForm content into your library.

This article explains how to structure and upload an XLSForm so it is imported as a collection.

## Setting up your XLSForm

To import successfully into your KoboToolbox question library, your XLSForm must follow a specific structure. Once you have a [working XLSForm](https://support.kobotoolbox.org/getting_started_xlsform.html), you can adapt it to function as a collection by modifying its structure:

1. **Rename the main worksheet:** Replace the standard `survey` worksheet with a worksheet named `library`.
    - This sheet should contain the same columns you would normally include in a survey sheet, such as `type`, `name`, `label`, [translated label columns](https://support.kobotoolbox.org/language_xls.html), and any relevant [question options](https://support.kobotoolbox.org/question_options_xls.html).
2. **Include individual questions or question groups:** You may include standalone questions or full question groups in the `library` worksheet.
3. **Define question blocks using a `block` column:** Add a column named `block` to group related questions into a question block.
    - Enter the same block title in each row that belongs to that block.
    - Any row without a value in the `block` column will be imported as an individual question.
4. **Add tags (optional):** To assign tags to a question or block, add a column using the format `tag:[tag name]` (e.g., `tag:wash`).
    - Enter 1 in each row that should receive the tag.
    - For blocks, it is sufficient to mark one row within the block, though marking multiple rows will not cause issues.

<p class="note">
  For an example of the required structure, see this <a href="https://support.kobotoolbox.org/_static/files/question_library/collection_import_sample.xlsx"> sample XLSForm</a>.
</p>

## Uploading your XLSForm

Once your XLSForm is structured correctly as a collection, you can upload it to your KoboToolbox library.

To upload your XLSForm:

1. Log in to your KoboToolbox account.
2. Click <i class="k-icon-library"></i> **Library** in the left-side menu to open the library.
3. Click **NEW** in the top left corner.
4. Select <i class="k-icon-upload"></i> **Upload** and import your XLSForm. Click **Upload.**

The file will be imported as a collection in your question library.

<p class="note">
  To learn more about the KoboToolbox library, see Using the <a href="https://support.kobotoolbox.org/question_library.html">KoboToolbox question library</a>.
</p>

## Additional considerations

### Groups within blocks

You may include `begin_group` and `end_group` rows inside a block. Ensure that the `begin_group` row has a unique `name` value, as required in standard XLSForm structure. The opening and closing group rows must both be included within the same block. 

Using the block name as the group label can help maintain clarity after import.

<p class="note">
  To learn more about question groups in XLSForm, see <a href="https://support.kobotoolbox.org/grouping_questions_xls.html">Grouping questions in XLSForm</a>.
</p>

### Skip logic and validation rules 

You can include relevance logic, constraints, and other form logic in your XLSForm. These settings will be preserved during import, which is useful when reusing complex question blocks without rebuilding advanced logic.

<p class="note">
  To learn more about form logic in XLSForm, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

### Multiple languages 

You can include translations using standard XLSForm syntax, such as `label::English (en)` or `label::Español (es)`. Translated labels and choice labels will be imported with the block.

<p class="note">
  To learn more about adding translations in XLSForm, see <a href="https://support.kobotoolbox.org/language_xls.html#">Adding translations in XLSForm</a>.
</p>
