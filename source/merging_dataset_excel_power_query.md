# Merging Individual Data with Roster Data through Power Query in Excel

As illustrated in the support article, [Grouping Questions and Repeating
Groups](group_repeat.md), you can use repeating groups to fulfil certain survey requirements. You may also need to analyze data from the repeat groups that were collected. When [downloading the data from the server (in XLS format)](export_download.md), you should see the data in the following structure:

![Dataset Sheets](/images/merging_dataset_excel_power_query/Dataset_Sheets.png)

The first sheet with the sheet name **Repeat Group (Merge)** seen in the image above holds the *individual data* from the survey while the second sheet with the sheet name **CR** holds the *roster data*. 

<p class='note'>For downloaded datasets, you should have one sheet more than the number of <em>repeat groups</em>. For example, if you had one <em>repeat groups</em> included in the survey form, you should have two sheets in your dataset.</p>

This support article will also illustrate the difference between *individual data* and *roster data*. It will then show the steps for how to merge them into a single dataset through **Power Query** in **Excel**.

Merging *individual data* and *roster data* through the system is currently not available but it is possible through **Power Query** in **Excel**. Excel was chosen over other software because it is a widely used spreadsheet and available to almost all the PCs. It is also relatively easy-to-use.

## Differences between individual data and roster data:

*Individual data* are information that are generally captured only once in an interview. *Roster data*, on the other hand, are captured more than once *(e.g., details of all family members living within a household)* from within the same individual in an interview. The number of cases in an *individual data* may equal to *roster data* but can never exceed it, while the number of cases in *roster data* generally exceeds the *individual data* but sometimes may be equal (but never less).

A filled-up survey form, as shown below, should show in a picture the differences between an *individual data* and *roster data*. *Please note, all data used in this support article are hypothetical*.

![Form](/images/merging_dataset_excel_power_query/Form.png)

<p class='note'>Any data that is collected outside the repeat group is an <em>individual data</em> and any data that is collected inside a repeat group is <em>roster data</em>.</p>

Data downloaded in XLS format should also show the difference between an *individual data* and *roster data* in a picture. 

Each record *(as shown in the image below)*, under **Name of the household head**, **Sex of the household head**, **Total family members in the household**, and **Total school going children (aged 6-16 years) in the household** from the first sheet **Repeat Group (Merge)** is an *individual data*. 

![Individual Data](/images/merging_dataset_excel_power_query/Individual_Data.png)

This example dataset has a total of 7 interviews as its *individual data*. 

Similarly, each record *(as shown in the image below)*, under **Name of child**, **Age of child**, and **Sex of child** from the second sheet **CR** is a *roster data*. 

![Roster Data](/images/merging_dataset_excel_power_query/Roster_Data.png)

So, this example sample dataset has a total of 12 records as its *roster data*. 

<p class='note'><strong>Note:</strong> While downloading a dataset from the server, you should also be able to see other variables (metadata variables) if they have not been filtered out. They have been removed from this example dataset for simplicity.</p>

## Merging individual data with roster data:

If you look closely at the images shared above, you can see `_index` column
*with value 1* in the first sheet **Repeat Group (Merge)**. Similarly, there is
also a `_parent_index` column *with value 1* in the second sheet **CR**.
`_index` and `_parent_index` are additional variables created by the system to manage repeat groups. They are matching variables needed to merge **individual data** and **roster data** together into one. 

There are basically two approaches to merge *individual data* and *roster data* into a single dataset through **Power Query** in **Excel**. You can use any of the following approaches: 

### First approach: Merging individual data with roster data (when the dataset is already open)

For the first approach, you must have opened your XLS dataset. For details, please see the video below:

<video controls><source src="./_static/files/merging_dataset_excel_power_query/XLS_Dataset_Open.mp4" type="video/mp4"></video>

* Open the dataset that has both the *individual data* and *roster data*.

* Select all data from the first sheet *(individual data)*.

* Under the **Data** tab, select **From Table/Range**.

* A dialogue box **(Create Table)** will pop-up. Select **OK**.

* Select the **Close & Load** icon that is located at the top left corner of the screen. You should now see two dropdown options: **Close & Load** and **Close & Load To …**. 

* Select **Close & Load To …**.

* A dialogue box **(Import Data)** will pop-up. Select **Only Create Connection** and then press **OK**.

* You have now created a query table for the *(individual data)*.

* You can now go to the second sheet, *(roster data)*, and follow the exact steps you have performed above.

* With this you have created a query table for the *(roster data)*.

* Under the **Data** tab, select **Get Data**. From there, select **Combine Queries** and then **Merge**.

* A dialogue box **Merge** is seen.

* Load both the query tables. Once both the tables are loaded, select the
  matching variable `_index` from the first table. Similarly, select the
  matching variable `_parent_index` from the second table. As soon as you select both the matching variables you should be able to see **The selection matches … of … rows from the first table**. The query table should now be merged. 

* To expand the merged table, check all the variables that you wish to have in the merged dataset. You can also uncheck **Use original column name as prefix** to have the original variable name in the merged dataset. When everything is done, select **OK**.

* You should now have the final merged dataset.

* Once again, select the **Close & Load** icon that is located at the top left corner of the screen. You should see two dropdown options: **Close & Load** and **Close & Load To …**.

* Select **Close & Load**. With this final click you have merged your *individual data* and *roster data* into a single dataset.

### Second approach: Merging individual data with roster data (when the dataset is not yet open)

Use the second approach when you have not yet opened your XLS dataset and only have opened your new Excel workbook. For details, please see the video below:

<video controls><source src="./_static/files/merging_dataset_excel_power_query/New_Excel_Workbook.mp4" type="video/mp4"></video>

* Open a new Excel workbook.

* Under the **Data** tab, select **Get Data**. From there select **From File** and then **From Workbook**.

* Search the file from your PC. Once you see it, select the file and then press **Import**.

* A dialogue box **Navigator** is seen. Here, check **Select multiple items** and the sheet names **CR** and **Repeat Group (Merge)** that are visible. Once they are checked the **Load** button at the bottom of the dialogue box gets activated. 

* Select the **Load** button. You should see two dropdown options: **Load** and **Load To …**. Select **Load**. 

* With this, you have created query tables for the *(individual data)* and the *(roster data)*. 

* Under the **Data** tab, select **Get Data**. From there, select **Combine Queries** and then select **Merge**.

* A dialogue box **Merge** is seen.

* Load both the query tables. Once both the tables are loaded, select the
  matching variable `_index` from the first table. Similarly, select the
  matching variable `_parent_index` from the second table. As soon as you select both the matching variables you should be able to see **The selection matches … of … rows from the first table**. The query table should now be merged. 

* To expand the merged table, check all the variables that you wish to have in the merged dataset. You can also uncheck **Use original column name as prefix** to have the original variable name in the merged dataset. When everything is done, select **OK**.

* You should now have the final merged dataset.

* Once again, select the **Close & Load** icon that is located at the top left corner of the screen. You should see two dropdown options: **Close & Load** and **Close & Load To …**.

* Select **Close & Load**. With this final click you have merged your *individual data* and *roster data* into a single dataset.

<p class='note'>The differences in the two approaches are with loading the query table. Once the query tables are loaded, you will need to follow the same steps to merge the <em>individual data</em> and <em>roster data</em>.</p>

## Troubleshooting:

* Managing *repeat group* at the moment is not supported in CSV format. You will need to download the data in XLS format.

* Microsoft Power Query for Excel is an Excel add-on. You can download it through this **[Microsoft download site](https://www.microsoft.com/en-us/download/details.aspx?id=39379)**. It should work best on *Excel for Microsoft 365* or *Excel 2021*, *Excel 2019*, *Excel 2016*, *Excel 2013*, and *Excel 2010*. For more details, please check out the **[Microsoft support site](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a)**.

<p class='note'>For practice, you can access the XLSForm <strong><a download class='reference'
href='./_static/files/merging_dataset_excel_power_query/Repeat_Group_(Merge).xls'>here</a></strong> and the example sample dataset <strong><a download class='reference'
href='./_static/files/merging_dataset_excel_power_query/Repeat_Group_(Merge)_Dataset.xls'>here</a></strong> that were used in this article.</p>
