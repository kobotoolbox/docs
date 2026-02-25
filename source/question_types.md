# Adding questions in the Formbuilder
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/3993133bcf0aafda0b0978709534175cb583e049/source/question_types.md" class="reference">28 Oct 2024</a>


The KoboToolbox Formbuilder allows you to easily add questions to your form as you build your survey or questionnaire. 
This article explains how to add questions to your form, define answer choices where applicable, and provides an overview of the available question types in the Formbuilder to support effective form design.

## Adding a question

To add a question to your form:

1. Click the <i class="k-icon-plus"></i> button. 
2. Enter your question label.
3. Click **+ ADD QUESTION.**
4. Choose the [question type](#question-types-in-the-formbuilder). 

![Add a question to the Formbuilder](images/question_types/add_question.png)

<p class="note">
<strong>Note:</strong> Once the question type has been selected, it cannot be changed in the Formbuilder. To change the question type of an existing question, delete the question and create a new question with the same label.
</p>

### Setting data column names

After adding a question to your form, it is strongly recommended to define a **Data Column Name** in the question **Settings.** The data column name is used to identify the question throughout the form logic and in the exported dataset. 

By default, KoboToolbox creates the data column name for you by removing spaces and capital letters from the question label. For example, if the question label is “Respondent name”, the data column name will be `respondent_name`.

<p class="note">
    To learn more about data column names, see <a href="">Question options in the Formbuilder</a>.
</p>

## Adding option choices

When adding Select One or Select Many questions to your form, you will be prompted to enter option choices. 

- You can enter as many option choices as you want. 
- To reorder the list of choices, click and drag an item to the desired position.
- Click the <i class=""></i> trash can icon next to a choice label to delete it.

![Delete choice](images/question_types/delete_choice.png)

<p class="note">
<strong>Note:</strong> Managing long choice lists in the Formbuilder can be time-consuming. If your form includes many options or the same choice list used in multiple questions, it is often easier to create and manage these lists using XLSForm instead. To learn more, see <a href="https://support.kobotoolbox.org/option_choices_xls.html#">Managing option choices in XLSForm</a>.
</p>

### Setting XML values for option choices

Next to each choice option, you will see a field labeled **AUTOMATIC.** This field contains the [XML value](https://support.kobotoolbox.org/glossary.html#xml-value) for that option.

The XML value is a short, internal name that KoboToolbox uses to save and identify the selected option in your data. By default, KoboToolbox creates the XML value for you by removing spaces and capital letters from the option label. For example, if the option label is “Option 1”, the XML value will be `option_1`.

In some cases, you may want to set your own XML value. This can be helpful if the option label is very long or if you want to use a clearer or more consistent name. To do this, click **AUTOMATIC** and replace it with your own custom value.

<p class="note">
<strong>Note:</strong> It is strongly recommended to define XML values for all choices when using non-Latin scripts, such as Chinese, Arabic, or Nepali, to ensure your data is stored and exported correctly.
</p>

## Question types in the Formbuilder

The following question types are available in the Formbuilder:

