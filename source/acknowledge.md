# Acknowledge question type
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/acknowledge.md" class="reference">31 Oct 2025</a>


The "Acknowledge" question type displays a single option, to select "OK" on the
form.

You can use the "Acknowledge" type for questions that require only 2 states of
response: answered and not answered, or accepted and not accepted. You could use
this question type with an informed consent in your survey form, or as a way of
ensuring the interviewee has read through and agrees to the terms, usually
outlined using a ["Note" question type](question_types.md).

## How to set up the question

1. In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to
   add a new question.
2. Type the question text. For example, "If you agree to continue with the
   survey, click OK."
3. Click "<i class="k-icon k-icon-plus"></i> ADD QUESTION" (or press the Enter
   key on the keyboard).
4. Choose the "<i class="k-icon k-icon-qt-acknowledge"></i> Acknowledge"
   question type.

![Adding the acknowledge question](images/acknowledge/acknowledge_adding.gif)

## How it is displayed in web forms and KoboCollect

The "Acknowledge" question displays a single radio button with the label "OK" as
shown below:

![Acknowledge questions in KoboCollect and Enketo](images/acknowledge/acknowledge.png)

## Using skip logic and validation criteria

An "Acknowledge" question has only 2 states of response: one where the question
is answered, and one where it is not, i.e. the response value is either "OK" or
_blank_.

![Acknowledge questions in Skip logic](images/acknowledge/acknowledge_skip.gif)

In the above example, the group "Survey" will only be displayed if the
"Acknowledge" question was answered (the user clicked OK).

Below is the equivalent form logic in XLSForm syntax:

**survey sheet**

| type        | name    | label                                              | relevant          |
| :---------- | :------ | :------------------------------------------------- | :---------------- |
| acknowledge | consent | If you agree to continue with the survey, click OK |                   |
| begin_group | survey  | Survey                                             | ${consent} = "OK" |
| text        | name    | What is your name?                                 |                   |
| integer     | age     | How old are you?                                   |                   |
| end_group   |         |                                                    |                   |
| survey |

<p class="note">
  You can download the example XLSForm
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >here <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>
