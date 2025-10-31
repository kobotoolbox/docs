# Using the Question Library
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/01270a828ec846731411368326ba58114adda98e/source/question_library.md" class="reference">28 Oct 2025</a>


## Adding Questions to your Library

Questions that have previously been added to your library can be added to any other form by drag-and-dropping them from the Question Library sidebar within the formbuilder.

To access the Question Library sidebar, click the **Add from Library** button in the top right corner of the formbuilder toolbar.

![image](/images/question_library/library.jpg)

If necessary, you can search for the question you are looking for by using the Search function to search by keyword or tag.

To add the question to your form, **drag-and-drop** it to the desired position. A question can be added multiple times if necessary, for example when reusing a specific scale for different questions.

## Managing Questions in your Library

The question library allows you to save and reuse frequently used questions.

To manage the Question Library click on the library menu button in the top left sidebar. By default the library will display all your questions. You can **view** or edit each individual question by clicking on collection label.

To **clone** or **download** the collection, hover the mouse over the collection label and the icons will appear on the right side.

You can also **add new questions** from within the library. Just click on **New** and you will be able to create a new question that is saved in the library.

To **delete questions** in your library, simply click **Delete** after clicking on the **More Actions** icon.

![image](/images/question_library/delete.jpg)

## Importing Collections

In addition to creating Collections in the interface, you can also import large sets of questions and blocks from Excel, based on the XLSForm standard. Advanced users will find it more practical to start from existing XLSForms than copying existing question content into the tool one by one.

![image](/images/question_library/import_collection.png)

By default, each XLS file will import as a new Collection. If your file only contains one question or one block, it will import just that one question or one block instead of creating a Collection. The name of the Collection is taken from the file name (duplicates of existing Collections are allowed). But it's easy to rename the Collection after importing it - just click on the Collection name in the left sidebar, then click the settings icon.

Use <a download class="reference" href="./_static/files/question_library/collection_import_sample.xlsx">this Excel file as a template</a>.
The file generally follows the XLSForm format. There a few differences:

* The main sheet containing the questions should be named **library** when uploading multiple blocks.
* (Optional) Question blocks should be defined in the additional column called **block**, writing the same block title in each row of the table that should be included in the block. The block label has no limitations in terms of characters, but it needs to be the exact same spelling to avoid breaking the block up ('Household questions' is different from 'household questions'). Use a block title that makes it easy to identify the contents later on.
* Any row in the template sheet that doesn't have a value in the block column will be imported as a separate question.
* (Optional) Define any tags for the question or block by adding a column **tag:[your tag name]** for each tag, then writing '1' in each row that should use the tag. In the case of blocks, it's enough to write '1' in any of the rows in the block regardless which one. It's enough to mark one of the questions in the block, though it doesn't matter if several questions are tagged.

Some other suggestions:

* You can include groups in blocks. Just ensure that the 'begin group' line has a unique 'name' ID (as in all XLSForms) and that the opening (begin group) and closing (end group) are included in the block. Add the block name as the group label might be a good idea so that you see the block label after importing it to the formbuilder.
* You can include skip logic and validation rules within blocks that you import. That's very useful when importing entire blocks of questions into new form drafts without having to rebuild these advanced settings.
* You can add multiple languages to question and response labels with the usual XLSForm syntax (label::English (en), label::Español (es), etc.)
