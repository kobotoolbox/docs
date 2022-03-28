# Number, Decimal and Range Question Types
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/bee2f6203c95d0a965438b4ad7f173902c608dca/source/number_decimal_range.md" class="reference">28 Mar 2022</a>

When creating questions with numeric responses, you can choose between the
"Number", "Decimal" and "Range" question types in KoboToolbox.

This article describes these question types and how to use them.

## When to use them

**Number:** The "Number" question type in the formbuilder is equivalent to the
`integer` question type in XLSForm. Use the "Number" question type when
responses to a question will be in the form of whole numbers, such as number of
children (1, 3, 5, etc.).

**Decimal:** Use the "Decimal" question type when a question’s response will be
in the form of decimal numbers, such as monthly income (1.2, 34.5, 42.42, etc.).

**Range:** The "Range" question type can collect both integer and decimal
values. By default, the "Range" question type displays a sliding scale that
allows users to pick a number. When setting it up, you must define the `start`
and `end` values of the range as well as the `step` between them.

## How to set them up

To set up the "Number" and "Decimal" question types:

-   In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to
    add a new question.
-   Type the question text. For example, "How many people live in this
    household?". Then click "<i class="k-icon k-icon-plus"></i> ADD QUESTION"
    (or press Enter).
-   Choose the question type ("Number" or "Decimal").

![Setting up number questions](/images/number_decimal_range/setup_number_question.gif)

To add a "Range" question type:

-   In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to
    add a new question.
-   Type the question text. For example, "Rate the effectiveness of the project
    from 1 to 5 (5 being most effective)". Then click
    "<i class="k-icon k-icon-plus"></i> ADD QUESTION" (or press Enter).
-   Choose the "Range" question type.
-   Type the `start` value (in this example, 1).
-   Type the `end` value (in this example, 5).
-   Type in the `step`, the number of steps from one value to the next. (In this
    example, 1, meaning the options on the sliding scale are 1, 2, 3, 4, 5).

![Setting up range questions](/images/number_decimal_range/setup_range_question.gif)

<p class="note">
  It is strongly recommended that you specify names for
  <strong>all questions</strong> before deploying your form,
  <em>especially</em> if the labels are non-Latin character languages such as
  Chinese, Arabic or Nepali.
</p>

## Translating question labels

For translating question labels into other languages through the KoboToolbox UI,
refer to the support article,
[Adding Another Language in the Project Dashboard](language_dashboard.md), or
[here](language_xls.md) if you are creating your form using XLSForm.

## How they are displayed by default on web forms and KoboCollect

![Number, Decimal and Range questions](/images/number_decimal_range/number_decimal_range_default.png)

## Advanced appearances

![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_advanced.png)
