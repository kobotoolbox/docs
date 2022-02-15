# Exporting and Uploading Data to GIS Software
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/886c96185320ca9feab49d06d27145b518db950a/source/upload_to_gis.md" class="reference">26 Jul 2020</a>

**Simple step-by-step process to export and upload your data as a shapefile into GIS software, such as ArcMap.**

There are multiple ways to import location-based data collected through KoboToolbox into GIS software. This article will outline a recommended procedure to download data from KoboToolbox as a CSV file and upload it into ArcMap as a shapefile. While this example uses ArcMap, the process is similar to those in other geospatial softwares, including QGIS (free).

1. In the **Downloads** tab of your project page in KoboToolbox, export and download your data as a CSV file.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    *Note: You can edit the data set once its in the GIS software, however it may be easier to first edit in Excel, or similar program. In Excel, use the [Text to Columns.](https://support.office.com/en-us/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23) function to split your CSV data into individual cells.*


2. Open a new or existing project in ArcMap, go to **Add Data**, and then link the folder where your CSV file is saved on your computer.

    ![image](/images/upload_to_gis/find_file.jpg)


3. Open the **Catalog** window and click on **Folder Connections**. Find your CSV file, right click it, then select **Create Feature Class** > **From XY Table**.


4. In the modal, click the **X Field** drop down and chose your GPS question_Longitude option. Also, be sure to choose your **Coordinate System of Input Coordinates**...(WGS 1984 is a good one, if you're not using one already) and make sure your **Output** is set to the appropriate folder, then click **OK**.

    ![image](/images/upload_to_gis/create_feature.jpg)


5. Back in the **Catalog** window, click and drag your new shapefile into either the **Data View** window or **Table of Contents**.


6.  You should now see your points on the screen and if you open the **Attributes Table**, you'll see all of the associated data with each point. From this point, you can now visualize and run various spatial analyses with your data.

    ![image](/images/upload_to_gis/dataview_table.jpg)
