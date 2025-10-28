# Managing repeat group data
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/050dcc9c8bfb4c528208bbe886979999037f1554/source/managing_repeat_groups.md" class="reference">28 Oct 2025</a>

<a href="es/managing_repeat_groups.html">Leer en español</a> | <a href="fr/managing_repeat_groups.html">Lire en français</a> | <a href="ar/managing_repeat_groups.html">اقرأ باللغة العربية</a>

<p class="note">
  To learn more about setting up repeat groups in your forms, see <a     href="https://support.kobotoolbox.org/group_repeat.html">Grouping questions and repeating groups</a>.
</p>

## Viewing and editing repeat group data
You can view repeated data in the data table, which you can find in the **Table** view of the **DATA** tab in the KoboToolbox project interface. Responses to repeated questions appear in a single column per question, with responses separated by a comma, as shown below. 

 ![image](/images/managing_repeat_groups/data_table.png) 

You can also view the complete data for any given submission, including each repetition of repeat groups, by clicking the <i class="k-icon-view"></i>**Open** button to the left of each submission.

To edit repeat group data, click the <i class="k-icon-edit"></i>**Edit** button. This will open up the form and allow you to [edit the form data](https://support.kobotoolbox.org/howto_edit_single_submissions.html) before resubmitting. [Bulk editing](https://support.kobotoolbox.org/howto_edit_multiple_submissions.html) repeat group data is not currently supported.

<p class="note">
  <b>Note</b>: Repeat group data cannot be displayed in the <b>Reports</b> or <b>Map</b> views due to the data structure of repeat groups.
</p>

## Exporting repeat group data
To export data from a form with repeat groups, you must download your data in **XLS format**. Each repeat group will be exported **as a separate sheet** in the exported file. CSV download will only provide data from the primary data.

![image](/images/managing_repeat_groups/download.png)

<p class="note"> 
    To learn more about exporting your data, see <a href="https://support.kobotoolbox.org/export_download.html">Exporting and downloading your data</a>.
</p>

## Linking repeat group data
In exported XLS files, repeat group data is stored **in a separate sheet**. The first sheet of the XLS file contains the main response data, and each repeat group's data is stored in its own sheet. Nested repeat groups are also stored in separate sheets. 

Data from repeat groups can be linked to the main data using the **_index** column from the main data sheet and the **_parent_index** column from the repeat group data sheet.

In the example below, the first sheet includes an **_index** column, in green, which identifies the first submission. The second sheet, shown in the second image, contains a **_parent_index** column, also highlighted in green, which links back to the first sheet. In this example, both rows from the repeated data come from the first data submission.

![image](/images/managing_repeat_groups/main_data.png)

![image](/images/managing_repeat_groups/repeat_group_data.png)

<p class="note">
  <b>Note</b>: The repeat group data sheet also includes an <b>_index column</b>. This column is used to link to <b>nested repeat groups</b>, following the same setup as described above, with the repeat group as the main data and the nested repeat group as the linked data.
</p>

Repeat group data can be merged with the main data using different tools for data analysis. For example, in Excel and Power BI, you can use [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) or [VLOOKUP()](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1) to merge data. In SQL, R, SAS, and other database management languages, you can combine the datasets using a [left join](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17).

<p class="note">
  To learn more about merging repeat group data using Power Query, see <a href="https://support.kobotoolbox.org/merging_dataset_excel_power_query.html?highlight=power+query">Merging Individual Data with Roster Data through Power Query in Excel</a>.<br><br>To learn more about combining datasets in R, see <a href="https://dplyr.tidyverse.org/reference/mutate-joins.html">Mutating joins</a>.
</p>





