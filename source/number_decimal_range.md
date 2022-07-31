# Number, Decimal and Range Question Types
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/52e6493336639f134f77fb4aff35a0a83a1d1365/source/number_decimal_range.md" class="reference">31 Jul 2022</a>

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

## Setting up in formbuilder

To set up the "Number" and "Decimal" question types:

- In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to add
  a new question.
- Type the question’s label. For example, "How many people live in this
  household?". Then click "+ ADD QUESTION" (or press Enter).
- Choose the question type ("Number" or "Decimal").

![Setting up number questions](/images/number_decimal_range/setup_number_question.gif)

To add a "Range" question type:

- In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to add
  a new question.
- Type the question text. For example, "Rate the effectiveness of the project
  from 1 to 5 (5 being most effective)". Then click
  "<i class="k-icon k-icon-plus"></i> ADD QUESTION" (or press Enter).
- Choose the "Range" question type.
- Type the `start` value (in this example, 1).
- Type the `end` value (in this example, 5).
- Type in the `step`, the number of steps from one value to the next. (In this
  example, 1, meaning the options on the sliding scale are 1, 2, 3, 4, 5).

![Setting up range questions](/images/number_decimal_range/setup_range_question.gif)

<p class="note">
  It is strongly recommended that you specify names for
  <strong>all questions</strong> before deploying your form,
  <em>especially</em> if the labels are non-Latin character languages such as
  Chinese, Arabic or Nepali.
</p>

## Setting up in XLSForm

In XLSForm, you can add "Number", "Decimal" and "Range" questions by using
`integer`, `decimal` and `range` question types respectively:

| type    | name     | label                                             | parameters           |
| :------ | :------- | :------------------------------------------------ | :------------------- |
| integer | hhsize   | How many people live in this household?           |                      |
| decimal | landsize | How big is your land? (in hectares)               |                      |
| range   | rating   | Rate the effectiveness of the project from 1 to 5 | start=1 end=5 step=1 |
| survey  |

<p class="note">
  When adding a <code>range</code> question to an XLSForm, the
  <code>start</code>, <code>end</code> and <code>step</code> parameters are
  added in the <code>parameters</code> column.
</p>

## Translating question labels

For translating question labels into other languages through the KoboToolbox UI,
refer to the support article, [here](language_dashboard.md), or
[here](language_xls.md) if you are creating your form using XLSForm.

## Default appearance in web forms and KoboCollect

![Number, Decimal and Range questions](/images/number_decimal_range/number_decimal_range_default.png)

## Advanced appearances

![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_advanced_appearance.png)

![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_advanced.png)

### Advanced appearances in XLSForm

You can specify advanced appearances of "Number", "Decimal" and "Range"
questions in XLSForm under the appearances column as in the following examples:

| type    | name            | label                                                    | appearance    | parameters           |
| :------ | :-------------- | :------------------------------------------------------- | :------------ | :------------------- |
| integer | income          | What was the total income you got in the last 12 months? | thousands-sep |                      |
| decimal | bearing         | Capture bearing                                          | bearing       |                      |
| range   | vertical_rating | Rate the effectiveness of the project from 1 to 5        | vertical      | start=1 end=5 step=1 |
| range   | picker_rating   | Rate the effectiveness of the project from 1 to 5        | picker        | start=1 end=5 step=1 |
| range   | star_rating     | Rate the effectiveness of the project from 1 to 5        | rating        | start=1 end=5 step=1 |
| survey  |

## Limits on "Number" and "Decimal" questions

### KoboCollect

The "Number" question type is limited to a maximum of 9 characters and the
"Decimal" question type is limited to a maximum of 15 characters.

<p class="note">
  Negative signs and decimal points count towards the character limit.
</p>

### Enketo

Both "Number" and "Decimal" question types are limited to a maximum of 16
significant figures.

If a positive or negative integer of 22 significant figures is entered, the form
will record a 16 digit number with scientific notation. For example, the number
`±9845284926482357445633` would be recorded as `±9.845284926482358e+21`.

If a positive or negative decimal of 22 significant figures is entered, the form
will record a truncated 16 digit number, rounded to the 16th digit. For example,
the number `±9845284926.482357445633` will be recorded as `±9845284926.482357`.

### Text question type as number

If your survey requires numeric responses that will exceed 15 digits, you can
use a workaround with the "Text" question type:

- Add a "Text" question to your form.
- Go to the **Appearance** setting and select "numbers". A digit keyboard will
  now appear when filling in this question.
- Finally, a [`regex()` constraint](restrict_responses.md) can be included to
  further restrict the input if necessary.

Here is an XLSForm example to illustrate this:

| type   | name   | label               | appearance | constraint            | constraint_message     |
| ------ | ------ | ------------------- | ---------- | --------------------- | ---------------------- |
| text   | number | Enter a long number | numbers    | regex(., '^[0-9]\*$') | Value must be a number |
| survey |

<p class="note">
  You can download an XLSForm with examples from this article
  <a
    download
    class="reference"
    href="./_static/files/number_decimal_range/number_decimal_range_question_types.xlsx"
    >here</a
  >.
</p>
