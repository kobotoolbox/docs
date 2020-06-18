# How to Create Unique Serial Numbers in Forms

There are times you may want to generate a unique serial number for each and every form in a project. This article discusses how to utilize the calculate question-type to do that by either creating sequential unique serial numbers based on date and time or by creating unique serial numbers from selected variables.

## Creating Sequential Unique Serial Numbers Based on Date and Time:

This method works best with Enketo web forms. It uses a calculation function to create a unique serial number based on the date and time to the first millisecond. Although this method may not meet all your needs, it should give you an illustration of how much you can stretch calculate functions to achieve your needs.

1. Create a calculate question type in either the formbuilder or XLSForm and use the formula below. *Please note the same formula can work as an integer question when working in an XLSForm.*

    `concat(substr(today(),0,4),substr(today(),7,5),substr(today(),10,8),
    `substr(now(),13,11),substr(now(),16,14),substr(now(),19,17))`

    Example:

    ![image](/images/unique_serial_numbers/calculate_example.png)

    In the example, when you preview the deployed form in Enketo, you should be able to see the serial number within the note question as shown in the image below:

    ![image](/images/unique_serial_numbers/preview_form.png)

## Creating Unique Serial Numbers from Selected Variables

This example shows how to create unique serial numbers from existing, already defined variables in your form by using the concat expression in a calculate question type. The example is shown as an XLSForm, but can just as easily be done within the formbuilder.

Example:

![image](/images/unique_serial_numbers/xls.jpg)

When you preview the example in Enketo web forms, the serial number will be presented within the note question as shown in the image below:

![image](/images/unique_serial_numbers/preview_uniqueid.png)
