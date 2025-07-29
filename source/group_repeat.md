# Grouping Questions and Repeating Groups
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/52881686dd9222c9f1268bf8d9b80474f8a06438/source/group_repeat.md" class="reference">18 Jun 2025</a>

KoboToolbox supports grouping questions when designing a survey form. Users may
need to group questions due to various reasons:

-   **Make the questionnaire systematic:** You could group your questions that
    have special linkage or attributes as Identifier, Section A, Section I, etc.
-   **Display a set of questions per page:** Grouped questions can be displayed
    on separate pages (or screens) during data collection.
-   **Skip a group of questions:** Rather than adding the same skip logic to
    each individual question, group the questions and add the skip logic to the
    group instead.
-   **Create a roster:** Repeat grouped questions for household surveys, etc.

## Grouping a set of questions

Draft a set of questions that you would wish to group together. Then press the
**CTRL Key** _(It may vary based on the OS used. The instruction here is based
on the Windows OS)_ and select **all the questions** _(with the help of your
mouse)_ that you wish to group. You should see the questions getting highlighted
to blue as shown in the image below:

![image](/images/group_repeat/group.png)

Then press **Create group with selected questions** _(marked under the red box)_
as shown in the image above. You should now be able to see your new group as
shown in the image below. It should be slightly different (enclosed within a
shaded box) then the normal question you generally see.

![image](/images/group_repeat/selected.png)

You can also change the group label. Here I have changed the group label to
**Demographic Characteristics** as shown in the image below:

![image](/images/group_repeat/demographics.png)

## Alternative way of creating a group

Draft a question. Select the question that you have drafted. It highlights to
blue. At the same time the icon (marked under the red box as shown in the image
below) for **Create group with selected questions** also gets activated.

![image](/images/group_repeat/alternative_group.png)

Now click the **Create group with selected questions** (icon) and you should be
able to see the question has been grouped (despite the fact that there is only
one question at the moment).

![image](/images/group_repeat/alternative_selected.png)

Add or modify questions as outlined below.

## Adding questions within a group

Hover your mouse (anywhere inside the group) where you wish to add a new
question. You should see a plus sign (+) under the question. In the image below,
I have hovered my mouse over the last question (Hobby). Press the plus sign that
is inside the group (marked with a red box) to add a new question.

<p class="note">If you press the other plus sign (+) which is located outside the group, you will be adding a question outside the group.</p>

![image](/images/group_repeat/add_questions.png)

You should now be able to see **Add Question** as shown in the image below:

![image](/images/group_repeat/add_questions_2.png)

## Removing questions from a group

Hover your mouse on top of the question you wish to delete. Press the trash
(bin) icon. At this stage, the color of the question box you wish to delete
changes to red. You should also see a text with **Delete Question** on top of
the question that you wish to delete.

![image](/images/group_repeat/delete_questions.png)

Once you click the delete button, you should get a confirmation dialogue box as
shown in the image below. Click **OK**.

![image](/images/group_repeat/confirm_delete.png)

## Re-ordering a question within a group

If you are not satisfied with the ordering of the questions within the group,
you could re-order them by simply selecting a question (that is within a group)
and dragging them to an appropriate place (either up or down as needed).

![image](/images/group_repeat/reorder.png)

If needed, you could also drag them outside the group (to extract a question
from a group).

## Displaying the grouped questions on the same screen

If you wish to display the grouped questions on the same screen, press the gear
like settings icon that has been marked under the red boxed as shown in the
image below. Then select **Show all questions in this group on the same screen**
as shown in the image below:

![image](/images/group_repeat/display.png)

Alternatively, you could also group a set of questions and display them on the
same screen through XLSForm (if you are comfortable with XLSForm) using the
`field-list` option under the `appearance` column:

**survey sheet**

| type           | name  | label                       | appearance |
| :------------- | :---- | :-------------------------- | :--------- |
| begin_group    | DC    | Demographic Characteristics | field-list |
| text           | Name  | Name                        |            |
| integer        | Age   | Age                         |            |
| select_one Sex | Sex   | Sex                         |            |
| text           | Hobby | Hobby                       |            |
| end_group      |       |                             |            |
| survey |

**choices sheet**

| list_name | name | label  |
| :-------- | :--- | :----- |
| Sex       | 1    | Male   |
| Sex       | 2    | Female |
| survey |

## Ungrouping a set of questions

If you no longer need a group of questions, you could ungroup or delete the
grouped questions. For this simply click the **Delete** button from the group
header.

![image](/images/group_repeat/ungroup.png)

You should then get a dialogue box confirming if you wish to split apart the
group or delete everything. Press **UNGROUP**.

![image](/images/group_repeat/ungroup_or_delete_confirm.png)

The group disappears but the questions will remain.

![image](/images/group_repeat/ungroup_results.png)

<p class="note">If the <strong>DELETE EVERYTHING</strong> button is pressed, the group and all its questions will be deleted.

## Skipping a group of questions

To skip a group of questions, you should have at least one controlling question
on top of the grouped question. Press the settings icon from the grouped
question as shown in the image below:

![image](/images/group_repeat/skip.png)

Then select **Skip Logic** and configure as shown in the image below:

![image](/images/group_repeat/skip_logic.png)

Alternatively, you could also do this in XLSForm:

**survey sheet**

| type           | name  | label                                                  | relevant    |
| :------------- | :---- | :----------------------------------------------------- | :---------- |
| select_one Q1  | Q1    | Q1. Are the any eligible respondents in the household? |             |
| begin_group    | DC    | Details of eligible respondents                        | ${Q1} = '1' |
| text           | Name  | Name                                                   |             |
| integer        | Age   | Age                                                    |             |
| select_one Sex | Sex   | Sex                                                    |             |
| text           | Hobby | Hobby                                                  |             |
| end_group      |       |                                                        |             |
| survey |

**choices sheet**

| list_name | name | label  |
| :-------- | :--- | :----- |
| Q1        | 1    | Yes    |
| Q1        | 2    | No     |
| Sex       | 1    | Male   |
| Sex       | 2    | Female |
| choices |

## Creating a roster (repeating group of questions)

Questions within a roster can be answered multiple times. For example, in a
household survey you might want to ask the name, age, gender and education
status of every household member.

Create a group of questions following the instructions that has already been
outlined above. Then under the **group settings**, select **Repeat this group if
necessary** (marked under the red box as shown in the image below).

![image](/images/group_repeat/repeat.png)

During an interview the enumerators will be able to enter the details to these
grouped questions as many times as required.

<p class="note">The resulting data structure from a roster is different from the data you normally see with other variables or groups. When downloading your data, you will see a different sheet for each roster (i.e. the number of additional sheets corresponds with the number of repeating groups that you have within your survey form).</p>

## Controlling the loop of repetition in a roster

Sometimes your survey may demand you to control the repeating of questions in a
roster with a value of a certain variable. In this case, you should modify your
survey in XLSForm as the formbuilder does not currently support this feature.

**survey sheet**

| type           | name  | label                                                   | repeat_count |
| :------------- | :---- | :------------------------------------------------------ | :----------- |
| integer        | Q1    | Total number of family members living in this household |              |
| begin_repeat   | DC    | Details of eligible respondents                         | ${Q1}        |
| text           | Name  | Name                                                    |              |
| integer        | Age   | Age                                                     |              |
| select_one Sex | Sex   | Sex                                                     |              |
| text           | Hobby | Hobby                                                   |              |
| end_repeat     |       |                                                         |              |
| survey |

**choices sheet**

| list_name | name | label  |
| :-------- | :--- | :----- |
| Sex       | 1    | Male   |
| Sex       | 2    | Female |
| choices |

<p class="note">Instead of having an indefinite number of repeat group iterations, this method will control the number of iterations based on the value in the <code>repeat_count</code> column.</p>

## Using information to a roster from a preceding roster

While working with grouping questions and repeating groups, sometimes you might
need to include certain details to a roster from a preceding roster. Designing
such survey form is possible in KoboToolbox using an
[`indexed-repeat()`](https://docs.getodk.org/form-operators-functions/#indexed-repeat)
function in the XLSForm. For example, you could use the name that has been
recorded in a roster (previously) to link with other repeating group questions
(like education etc.):

**survey sheet**

| type                 | name              | label                                           | calculation                                  | repeat_count    |
| :------------------- | :---------------- | :---------------------------------------------- | :------------------------------------------- | :-------------- |
| begin_repeat         | DC                | Demographic Characteristics                     |                                              |                 |
| text                 | Name              | Name                                            |                                              |                 |
| integer              | Age               | Age                                             |                                              |                 |
| select_one Sex       | Sex               | Sex                                             |                                              |                 |
| text                 | Hobby             | Hobby                                           |                                              |                 |
| end_repeat           |                   |                                                 |                                              |                 |
| calculate            | family_count      |                                                 | count(${DC})                                 |                 |
| note                 | family_count_note | Number of family members: ${family_count}       |                                              |                 |
| begin_repeat         | education         | Education information                           |                                              | ${family_count} |
| calculate            | name_individual   |                                                 | indexed-repeat(${Name}, ${DC}, position(..)) |                 |
| select_one edu_level | edu_level         | What is ${name_individual}'s level of education |                                              |                 |
| end_repeat           |                   |                                                 |                                              |                 |
| survey |

**choices sheet**

| list_name | name | label                    |
| :-------- | :--- | :----------------------- |
| Sex       | 1    | Male                     |
| Sex       | 2    | Female                   |
| edu_level | 1    | Primary                  |
| edu_level | 2    | Secondary                |
| edu_level | 3    | Higher Secondary & Above |
| choices |

Screen seen while [collecting data in Enketo](data_through_webforms.md):

![image](/images/group_repeat/enketo.png)

## Nested Repeat (roster within a roster)

KoboToolbox also supports nested repeat form design. Here you are able to add a
roster within a roster (i.e. a repeat group question within a repeat group
question).

Design a roster (with the group name **Demographic Characteristics**) and then
place another roster (with the group name **List of Hobbies**) within a roster
(**Demographic Characteristics**) by following the steps outlined above under
**Creating a roster (repeating group of questions)**. You should then have a
nested repeat form as shown in the image below:

![image](/images/group_repeat/nested_repeat.png)

Alternatively, you could also do this in XLSForm:

**survey sheet**

| type           | name            | label                               | calculation                                  | repeat_count |
| :------------- | :-------------- | :---------------------------------- | :------------------------------------------- | :----------- |
| begin_repeat   | DC              | Demographic Characteristics         |                                              |              |
| text           | Name            | Name                                |                                              |              |
| integer        | Age             | Age                                 |                                              |              |
| select_one Sex | Sex             | Sex                                 |                                              |              |
| integer        | Hobby           | How many hobbies does ${name} have? |                                              |              |
| calculate      | name_individual |                                     | indexed-repeat(${Name}, ${DC}, position(..)) |              |
| begin_repeat   | LH              | List of Hobbies                     |                                              | ${Hobby}     |
| text           | Hobbies         | Hobbies of ${name_individual}       |                                              |              |
| end_repeat     |                 |                                     |                                              |              |
| end_repeat     |                 |                                     |                                              |              |
| survey |

**choices sheet**

| list_name | name | label  |
| :-------- | :--- | :----- |
| Sex       | 1    | Male   |
| Sex       | 2    | Female |
| choices |

Screen seen while collecting data in Enketo:

![image](/images/group_repeat/nested_repeat_enketo.png)

<p class="note">You are able to collect data using nested repeats in both <a class="reference" href="data_through_webforms.html">Enketo</a> and the <a class="reference" href="kobocollect-android.html">Collect Android app</a>. If you are using Collect, please ensure that you are using the latest version as earlier versions may not support this.</p>

## Downloading Data from Repeat Groups

This section takes you through the process of downloading data from repeat
groups.

Data from repeat groups are downloaded separately from data outside the repeat
groups (primary/parent data). The following diagram illustrates the structure of
how sheets are created in the XLSform.

![Data Structure](/images/group_repeat/data_structure.png)

When you download data from a form (project) with repeat groups included, you
need to use either the **XLS** or **XLS (legacy)** download options. **CSV**
download will only give you data from the Primary/Parent Data.

![XLS Download](/images/group_repeat/xls_download.png)

As previously explained, once you have downloaded the data, check for repeat
group data within the separate sheets. To link the repeat group data to the
parent data, use the index column from the parent sheet and match it to the
parent index column in the repeat group sheet.
