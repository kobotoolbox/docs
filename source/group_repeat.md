# Grouping questions and repeating groups
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/01270a828ec846731411368326ba58114adda98e/source/group_repeat.md" class="reference">28 Oct 2025</a>


<iframe src="https://www.youtube.com/embed/nmPACLvYnUI?si=mkUi9RBLNHObj9ei" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Grouping questions helps organize related questions into sections, adds structure to your form, and makes it easier to navigate. For example, all demographic questions can be grouped together in one section of the form.

Users may need to group questions for various reasons:
-   **Structuring the questionnaire:** Questions with common themes or attributes can be grouped together in a single section.
-   **Displaying a set of questions per page:** Grouped questions can be displayed on separate pages or screens during data collection.
-   **Skipping a group of questions:** Skip logic can be added to the whole group instead of adding it to each individual question.
-   **Create a roster:** Question groups can be repeated, for example for household surveys or indicator tracking.

This article covers how to create and manage question groups and [repeat groups](#repeating-a-question-group) in the KoboToolbox Formbuilder.

## Creating and managing question groups

The Formbuilder makes it easy to group questions, add questions to groups, remove questions from groups, and re-order questions within a group.

### Grouping a set of questions

To create a question group, follow the steps below:

1. Draft a set of questions that you would like to group together.
2. Select the questions using the **CTRL** key (Windows) or the **Command** key (Mac).
3. Click on <i class="k-icon-group"></i> **Create group with selected questions** in the top left menu bar.

![image](/images/group_repeat/grouping_questions.png)

Your new group will appear enclosed within a shaded box, distinguishing it from standard questions. You can also change the group label, which will display at the top of the group in the form.

<p class="note">
    <b>Note:</b> Alternatively, you can create a single question, select the question, and click on <b>Create group</b>. Then, you can add more questions within the group, as outlined below.
</p>

### Adding questions within a group

Hover your mouse anywhere inside the group where you want to add a new question. Click on a <i class="k-icon-plus"></i> **sign** inside the group to add a new question.

<p class="note">
    <b>Note:</b> If you click the <i class="k-icon-plus"> </i><b>sign</b> that is located outside the group, you will be adding a question outside the group.
</p>

You also drag and drop any existing question into a question group.

### Removing questions from a group

To remove a question from a group but keep it in the form, select the question and drag it outside of the group.

To permanently delete a question from the form, click <i class="k-icon-trash"></i> **Delete Question** from the question menu on the right, then click **OK**.

### Re-ordering a question within a group

You can reorder questions within a group by selecting the question and dragging it to the desired position (up or down).

### Removing a question group 
If you no longer need a group of questions, you can either ungroup them or delete the entire group. To do this, click the <i class="k-icon-trash"></i> **Delete** button from the group header.

A dialog box will appear asking you to confirm if you wish to split apart the group or delete everything.

- Click **UNGROUP** to remove the group while keeping the questions in the form.
- Click **DELETE EVERYTHING** to delete both the group and all its questions.

### Nested groups

A group of questions can be created or placed inside another group. This is known as **nested groups**. [Repeat groups](#repeating-a-question-group) can also be nested. 

---

## Question group settings

After creating a question group, you can customize its behavior and appearance. For example, you can display all questions in the group on the same screen, apply skip logic to the entire group, or set the group to repeat.

### Displaying grouped questions on the same screen

In KoboCollect, questions appear one at a time by default. In Enketo web forms, all questions appear on the same screen.

To display questions by group on the same screen during data collection, click the <i class="k-icon-settings"></i> **Settings** icon to the right of the group name. Then, under **Appearance (Advanced)**, select **field-list** (Show all questions in this group on the same screen).

<p class="note">
    <b>Note:</b> If you plan to collect data using Enketo web forms, you will also need to enable the <b>Multiple pages</b> theme in the <b>Form style</b> menu (<b>Layout & Settings</b>). For more information on Enketo web form styles, see <a href="https://support.kobotoolbox.org/alternative_enketo.html">Using alternative Enketo web form styles</a>.
</p>

### Skipping a question group
To skip a group of questions, ensure you have at least one controlling question positioned before the grouped questions. Click the <i class="k-icon-settings"></i> **Settings** icon for the grouped question, then select **Skip Logic** and configure the skip logic conditions as you would for an individual question.

<p class="note">
    To learn more about adding skip logic conditions, see <a href="https://support.kobotoolbox.org/skip_logic.html">Adding skip logic in the Formbuilder</a>.
</p>

### Repeating a question group
A repeat group allows a set of questions to be answered multiple times within a form. For example, in a household survey, you could use a repeat group to collect the name, age, gender, and education status for every household member. 

To create a question group:
1. Create all the questions you wish to include, then group them.
2. In the group <i class="k-icon-settings"></i> **Settings**, turn on the option to **Repeat this group if necessary**.

![image](/images/group_repeat/repeating_groups.png)

During data collection, enumerators will be able to enter responses for these grouped questions as many times as needed.

<p class="note">
    <b>Note:</b> Adding repeat groups to your form creates a different data structure compared to standard variables or groups. When you download your data in .xlsx format, you will find a separate sheet for each repeat group. For more information on exporting and using repeat group data, see <a href="https://support.kobotoolbox.org/managing_repeat_groups.html">Managing repeat group data</a>.
</p>

### Advanced settings for repeat groups
Additional settings and functionalities for repeat groups are available through XLSForm, but not directly within the Formbuilder. These include setting a fixed or dynamic number of repetitions, and using information from repeat groups elsewhere in your form.

<p class="note">
    For more information about advanced settings for repeat groups, see <a href="https://docs.getodk.org/form-logic/#controlling-the-number-of-repetitions">XLSForm documentation</a>.  
</p>

