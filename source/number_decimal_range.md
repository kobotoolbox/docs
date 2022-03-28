# Number, Decimal and Range Question Types

When creating questions with numeric responses, you can choose between the
“Number”, “Decimal” and “Range” question types in KoboToolbox.

This article describes these question types and how to use them.

## When to use them

**Number:** The “Number” question type in the formbuilder is equivalent to the
`integer` question type in XLSForm. Use the “Number” question type when
responses to a question will be in the form of whole numbers, such as number of
children (1, 3, 5, etc.).

**Decimal:** Use the “Decimal” question type when a question’s response will be
in the form of decimal numbers, such as monthly income (1.2, 34.5, 42.42, etc.).

**Range:** The “Range” question type can collect both integer and decimal
values. By default, the “Range” question type displays a sliding scale that
allows users to pick a number. When setting it up, you must define the start and
end values of the range as well as the step between them.

## How to set them up

To set up the “Number” and “Decimal” question types:

-   In the KoboToolbox Formbuilder, click the <i class="k-icon k-icon-plus"></i>
    button to add a new question.
-   Type the question text. For example, “How many people live in this
    household?”. Then click “<i class="k-icon k-icon-plus"></i> ADD QUESTION”
    (or press Enter).
-   Choose the question type (“Number” or “Decimal”).

![Setting up number questions](/images/number_decimal_range/setup_number_question.gif)

To add a “Range” question type:

-   In the KoboToolbox Formbuilder, click the <i class="k-icon k-icon-plus"></i>
    button to add a new question.
-   Type the question text. For example, “Rate the effectiveness of the project
    from 1 to 5 (5 being most effective)”. Then click
    “<i class="k-icon k-icon-plus"></i> ADD QUESTION” (or press Enter).
-   Choose the “Range” question type.
-   Type the start value (in this example, 1).
-   Type the end value (in this example, 5).
-   Type in the number of steps from one value to the next. (In this example, 1,
    meaning the options on the sliding scale are 1, 2, 3, 4, 5).

![Setting up range questions](/images/number_decimal_range/setup_range_question.gif)

## How they are displayed by default on web forms and KoboCollect

![Number, Decimal and Range questions](/images/number_decimal_range/number_decimal_range.png)

## Data storage

Data for “Number” questions are stored as integers (whole numbers), while for
“Decimal” question types, values are stored as decimals.

In the case of the “Range” question type, the values stored will depend on the
parameter values specified. If all the parameters are whole numbers, the values
that will be shown and saved in the database will be whole numbers (integers).
On the other hand, if one of the parameters is a decimal, the range bar will
show decimals (and the numbers that will be saved will be in decimal format).

## Advanced appearances

![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_appearances_1.png)
![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_appearances_2.png)
![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_appearances_3.png)
![Number, Decimal and Range advanced appearances](/images/number_decimal_range/number_decimal_range_appearances_4.png)
