# Pulling Data Into Excel Power Query

For seamless data analysis, you can leverage the KoBo API to pull your data into other tools for data analysis. This article covers how to connect to the API to pull your data into Excel Power Query.

## KoBo API

1. Login to your account.

2. Next, go to the API for your account by going to either  [https://kc.humanitarianresponse.info/api/v1](https://kc.humanitarianresponse.info/api/v1) or [https://kc.kobotoolbox.org/api/v1/](https://kc.kobotoolbox.org/api/v1/). Select the URL for the instance in which your account is located.

3. Under the Data heading, click on /api/v1/data

    ![image](/images/pulling_data_excelquery/api_json.jpg)

4. Click on "GET" and select "xls".

    ![image](/images/pulling_data_excelquery/api_datalist.jpg)

5. This action will download a text file to your computer called "data".

6. Next, locate your project's data structure inside the data file. It will be in the following format: description,id,id_string,title,url

    _For example:_

    MIRA_DO,1314,MIRA_DO,MIRA_DO, [https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls](https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls)

7. To pull the data, take the form URL (in bold in the above example) and replace “?format=xls” to “.xls”. For our example, the URL should now be:

   [https://kc.humanitarianresponse.info/api/v1/data/1314.xls](https://kc.humanitarianresponse.info/api/v1/data/1314.xls)


8. Before transitioning over the Excel, make sure that there is a) at least 1 record stored in your data table in KoboToolbox and b) under the Project's settings, set it to "share data publicly".

## Microsoft Excel

9. In Excel, click on Data > From Other Sources > From Web and paste your URL. You should now be able to have your dataset in Microsoft Excel.

    ![image](/images/pulling_data_excelquery/excel.jpg)

## Updating Data in Microsoft Excel

Once you have synced your KoBoToolbox with your Microsoft Excel through Excel Power Query, you should be able to have the dataset in Microsoft Excel. However, when the KoBoToolbox server is updated (i.e. through new submissions, deletion, amendments) your Microsoft Excel dataset does not get updated automatically. You could do this by refreshing the Excel document. For this you will need to click the **Data** and then select **Refresh All**. Any changes made in the KoBoToolbox server will now be manually updated in your Excel dataset. (Please follow this whenever you require an update with your Microsoft Excel dataset)

_**Thanks to Awais Awan for writing the initial draft of this post.**_
