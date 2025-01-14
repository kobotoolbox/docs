# Text and Note question types
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/4d3ba5b4639335723af5b5a376159a536c904323/source/text_and_note.md" class="reference">9 May 2022</a>

The "Text" question type is best used for questions that require undefined or
open-ended responses, such as names, feedback, explanations or descriptions.

The "Note" question type does not allow for a response value, instead they can
be used to add instructions, or any additional information to make the survey
clearer or easier to navigate. For instance, you can use it to inform the
respondent or enumerator about what the next section of questions contains,
provide background context for why the survey is being done,
[display various kinds of media](media.md), or
[display the results of hidden calculations or responses to previous questions](responses_inside_question.md).

## How to set the questions up

Setting up `text` or `note` questions is very similar:

-   In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to
    add a new question.
-   Type the question text. For example, "What is your name?". Then click **+
    ADD QUESTION** (or press Enter).
-   Choose the question type ("Text" or "Note")

![Setting up text and note questions](images/text_and_note/text_note_setup.gif)

## Appearance in web forms and KoboCollect

### Default appearance

![Default appearance of text and note](images/text_and_note/text_note_default_appearance.png)

<p class="note">
  The default text box in Enketo Webform accepts only one line of text. However,
  in KoboCollect, the text field expands as you type. You can also add line
  breaks to form paragraphs
</p>

### Advanced appearances

You can change the appearance of "Text" questions in its settings.

![Appearance settings](images/text_and_note/text_appearance_settings.png)

![Advanced appearances for text](images/text_and_note/text_advanced_appearance.png)

## Considerations when using "Text" questions

For the sake of data quality, it may be advisable to use
["Select one" or "Select many" question types](select_one_and_select_many.md)
when you are able to predefine a list of the responses. Limiting responses can
streamline data cleaning, processing and analysis.

The use of the "Text" question type is best suited to open-ended questions,
where you are unable to have a predefined list of responses.

## Using question logic

Since the responses to "Text" questions are open-ended, using question logic may
be more challenging and is best facilitated by using "Regular Expressions".

With RegEx, you can implement validation logic, such as limiting the length of
text responses, restricting the characters and sequence (such as a unique ID) or
only allowing responses that are in capital letters.

To learn more about implementing RegEx, read the support article
[Restricting Text Responses With Regular Expressions](restrict_responses.md)
