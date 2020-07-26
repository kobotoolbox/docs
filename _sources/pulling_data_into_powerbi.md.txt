# Pulling Data Into PowerBI

## KoBoToolbox

First, you need to find the unique URL that allows you to access your project data via the API. If you already know how to find this, skip to the next section.

1. The unique URL has the following structure: `https://[kobocat-URL]/api/v1/data/[unique-kc-ID]`.

2. To find this URL, go to https://[kobocat-URL/api/v1/data/ and find the project in the list at the bottom, the. copy the value for 'url' (without the quotation marks). For example:

    ![image](/images/pulling_data_into_powerbi/kobo_url.png)

## PowerBI

![image](/images/pulling_data_into_powerbi/powerbi.gif)

1. Open the [Power BI file](https://drive.google.com/file/d/1kYUnVjXIU5zFK-Yn43dPqARy-3L8N7xr/view)

2. Click on **Edit Queries** found under the Home ribbon

    ![image](/images/pulling_data_into_powerbi/edit_queries.jpg)

3. Click on **Edit Credentials**

    ![image](/images/pulling_data_into_powerbi/edit_credentials.jpg)

4. Under the **Basic** tab, enter your KoBo username and password then click connect

    ![image](/images/pulling_data_into_powerbi/login.jpg)

5. A table should load showing you all available forms which you have **enabled data sharing in your KoBoToolbox account** in addition to the languages (labels) you have designed them in. To connect to any of your forms’ data, copy the CSV link found under the CSV column.

    ![image](/images/pulling_data_into_powerbi/csv.jpg)

6. Copy the URL of the dataset you need to connect to, then add it again as a new Web source.

    ![image](/images/pulling_data_into_powerbi/url.gif)


**Thanks to Chris Habib for [writing the initial draft of this post.](https://groups.google.com/forum/#!searchin/kobo-users/Re$3A$20Connecting$20Power$20BI$20to$20KoBo%7Csort:date/kobo-users/K-Iyo7A914E/qy47nkCJCwAJ)**
