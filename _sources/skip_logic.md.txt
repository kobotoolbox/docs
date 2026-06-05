# Adding skip logic in the Formbuilder
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/9f9bb8dabfcd58f2bc08a4c6c0158d65262e935d/source/skip_logic.md" class="reference">5 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/uLSnoG0mqV4?si=63o4YeQUZWOsZmfF" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Skip logic, also known as branching or relevance conditions, controls which questions are displayed in a form. By default, all questions are visible. Skip logic determines under which condition(s) a question should appear. Skip logic conditions are always applied to the question or group that should be conditionally visible.

<p class="note">
    <strong>Note:</strong> You can apply skip logic to entire <a href="group_repeat.html">question groups</a> as well as individual questions. This can simplify form logic and make it easier to manage complex questionnaires.
</p>

There are two methods for adding skip logic in the Formbuilder: adding a condition via the **skip logic builder**, or manually entering skip logic in **XLSForm code**.

## Adding a condition

This first method allows you to use the skip logic builder to add your conditions. It is recommended for beginners. To add a skip logic condition, follow these steps:

1. Open the <i class="k-icon-settings"></i> **Settings** in the right side menu of the question or group to be conditionally displayed.
2. Select **Skip Logic**, and click **Add a condition**.
3. Select the question in the form that will determine whether the current question is displayed or not. 
4. Choose the appropriate logic operator for your condition (e.g., >, =, !=). 
5. In the **response value** field, select or type in the response that is required for the condition to be met. 

The question will be displayed only when the specified condition is met.

To add multiple conditions, add your first condition, then click the **Add another condition** button. When using multiple conditions, specify whether at least one of these conditions must be met or all of them.

<p class="note">
    <strong>Note:</strong> You can delete skip logic conditions by clicking on the <i class="k-icon-trash"></i> trash can.
</p>

## Manually entering skip logic in XLSForm code
For advanced users, skip logic can be entered directly in XLSForm code. The basic structure of the conditions remains unchanged: you will need to identify the controlling question, choose a logic operator, and type in the required response value. 

To manually enter skip logic in XLSForm code, follow these steps:
1. Open the <i class="k-icon-settings"></i> **Settings** in the right side menu of the question or group to be conditionally displayed.
2. Select **Skip Logic**, and click **Manually enter your skip logic in XLSForm code**.
3. Enter the condition in XLSForm code.

In XLSForm code, questions are referred to by their **question name** (Data Column Name) using the format `${question_name}`. For example, if Q2 should be asked only if the answer to Q1 is "Yes", the skip logic condition for Q2 would be `${Q1} = ‘yes’`.

<p class="note">
    For more information on XLSForm code and operators, see <a href="https://support.kobotoolbox.org/form_logic.html">Introduction to form logic in the Formbuilder</a>.
</p>

## Troubleshooting
<details>
<summary><strong>Skip logic does not work as expected with multiple choice questions</strong></summary>
When adding skip logic based on a multiple choice question, using <code>${question} = 'option1'</code> will only work if Option 1 is <strong>the only selected response</strong>. To apply skip logic when Option 1 is selected, regardless of whether other options are also selected, use the <code>selected()</code> function: <code>selected(${question}, 'option1')</code> <br><br>
This is common when adding an open text “Specify other” question after a multiple choice question. For example, if you want the “Specify other” question to appear whenever “Other” is selected, use: <code>selected(${question}, 'other')</code>

</details>
