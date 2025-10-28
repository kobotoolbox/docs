# Creating Unique Serial Numbers in Forms
<a href="fr/unique_serial_numbers.html">Lire en français</a> | <a href="es/unique_serial_numbers.html">Leer en español</a> | <a href="ar/unique_serial_numbers.html">اقرأ باللغة العربية</a>
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/unique_serial_numbers.md" class="reference">29 Jul 2025</a>

There are times you may want to generate a unique serial number for each and
every form in a project. This article discusses various workarounds on how to
create unique serial numbers using the `calculate` question-type.

## Approach 1: Creating Sequential Unique Serial Numbers Based on Date and Time

This method works best with [Enketo web forms](data_through_webforms.md). It
uses a calculation function to create a unique serial number based on the date
and time to the first millisecond. Although this method may not meet all your
needs, it should give you an illustration of how much you can stretch calculate
functions.

Create a
<a class="reference" href="calculate_questions.html"><code>calculate</code>
question type</a> in either the formbuilder or **XLSForm** and use the formula
below.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  The same formula can work as an <code>integer</code> question when working in
  an <strong>XLSForm</strong>.
</p>

![Calculate example](/images/unique_serial_numbers/calculate_example.png)

In the example, when you preview the deployed form in **Enketo**, you should be
able to see the serial number within the note question as shown in the image
below:

![Preview form](/images/unique_serial_numbers/preview_form.png)

## Approach 2: Creating Unique Serial Numbers from Selected Variables

This example shows how to create unique serial numbers from existing, already
defined variables in your form by using the
[`concat()`](https://docs.getodk.org/form-operators-functions/#concat)
expression in a `calculate` question type. The example is shown as an
**XLSForm**, but can just as easily be done within the formbuilder.

**survey sheet**

| type      | name    | label                                  | calculation                                                           |
| :-------- | :------ | :------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Region Name                            |                                                                       |
| text      | Q2      | District Name                          |                                                                       |
| text      | Q3      | Cluster Name                           |                                                                       |
| text      | Q4      | Village Name                           |                                                                       |
| text      | Q5      | Household Serial Number                |                                                                       |
| calculate | Q1_C    |                                        | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                        | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                        | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                        | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                        | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Your Unique ID for this form is: ${ID} |                                                                       |
| survey |

When you preview the example in **Enketo** web forms, the serial number will be
presented within the note question as shown in the image below:

![Preview unique id](/images/unique_serial_numbers/preview_uniqueid.png)
