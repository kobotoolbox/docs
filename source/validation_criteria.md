# Adding validation criteria in the Formbuilder
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/9c216c0650cac549ce4c2836cb5b8a588a47357a/source/validation_criteria.md" class="reference">2 Oct 2025</a>


<iframe src="https://www.youtube.com/embed/ya9usVpEo9Q?si=-rDzXcCRazcY0Bws" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Validation logic, also known as validation criteria or constraints, defines conditions for an acceptable response to a question. This feature helps ensure high-quality data by preventing accidental or invalid answers.

Validation criteria can be applied to any question type. For example, you can use it to ensure that a participant is above a certain age, that a date is within a specific range, or that a text entry matches a certain pattern. 

There are two methods for adding validation criteria in the Formbuilder: adding a condition via the **validation criteria builder**, or manually entering validation logic in **XLSForm code.**


## Adding a condition

The validation criteria builder allows you to add conditions for **Text**, **Number**, **Decimal**, and **Date** questions. It is not compatible with **Select One** or **Select Many** questions. To use the builder:
1. Open the <i class="k-icon-settings"></i> **Settings** in the right side menu of the question.
2. Select **Validation Criteria**, and click **Add a condition.**
3. Choose the appropriate logic operator for your condition (e.g., >, =, !=). 
4. In the **response value** field, select or type in the value that is required for the response to be valid. 

<p class="note">
    <strong>Note:</strong> To add validation criteria to <strong>Date</strong> questions, the response value must be in <code>YYYY-MM-DD</code> format. For example, to set a validation criteria for a date to be before January 1, 2021, use <code>< 2021-01-01</code>.
</p>

To add multiple conditions (e.g., a minimum and a maximum value), add your first condition, then click **Add another condition.** When using multiple conditions, specify whether at least one of these conditions must be met or all of them. You can delete conditions by clicking on the <i class="k-icon-trash"></i> trash can.

If the validation conditions are not met, the input will not be accepted during data collection. An [error message](#error-message) will be displayed.


## Manually entering validation logic in XLSForm code
For advanced users and for **Select One** or **Select Many** questions, validation criteria can be entered directly in XLSForm code. 

To manually enter validation logic in XLSForm code, follow these steps:
1. Open the <i class="k-icon-settings"></i> **Settings** in the right side menu of the question.
2. Select **Validation Criteria**, and click **Manually enter your validation logic in XLSForm code.**
3. Enter the criteria in XLSForm code.

In XLSForm syntax, a dot `.` is used to refer to the current question, and `${question_name}` is used to refer to other questions. You will also need to include the relevant logic operator and response value. 

### Example Validation Criteria

| Criteria             | Description                                  |
| :------------------- | :------------------------------------------- |
| `. > 17`             | Response must be greater than 17             |
| `. >= 17 and . <= 130` | Response must be equal to or between 17 and 130          |
| `not(${in_university} = 'yes' and . < 16)` | Cannot provide a response below 16 if the response to `in_university` is “Yes”|
| `not(selected(., ’none’) and count-selected(.)>1)`| Cannot select “None” and other options in a Select Many question |


<p class="note">
    For more information on XLSForm code and operators, see <a href="https://support.kobotoolbox.org/form_logic_xls.html">Introduction to form logic in XLSForm</a>.
</p>

## Error message
The **error message** is an optional message that the interviewer or respondent will see when an invalid response is entered. It can be set using both the **validation criteria builder** approach and the **XLSForm code** approach, at the bottom of the box. 

If no error message is specified, the default message is “Value not allowed”. Custom error messages typically specify the validation criteria to help the respondent correct their answer (e.g., “Age must be greater than 18”).
