# Pulling Data Into Excel Power Query

For seamless data analysis, you can leverage the KoBo API to pull your data into other tools for data analysis. This article covers how to connect to the API to pull your data into __Excel Power Query__.

## Getting KoBo API for Excel Power Query

* Login to your account.

* Next, go to the API for your account by going to either [https://kc.humanitarianresponse.info/api/v1](https://kc.humanitarianresponse.info/api/v1) or [https://kc.kobotoolbox.org/api/v1/](https://kc.kobotoolbox.org/api/v1/). Select the URL for the instance in which your account is located.

* Under the __Data__ heading, click on `/api/v1/data`.

![image](/images/pulling_data_excelquery/api_json.jpg)

* Click on __GET__ and select __xls__.

![image](/images/pulling_data_excelquery/api_datalist.jpg)

* This action will download a text file to your computer called __data__. You could open this file with a __Notepad__.

* Next, locate your project's data structure inside the `data` file you downloaded. It will be in the following format: `id`, `id_string`, `title`, `description`, `url`. _For example:_

[(`'id'`, `1314`), (`'id_string'`, `'a7tAUbZp9Ad4MkvW7JSrft'`) (`'title'`, `'MIRA_DO'`), (`'description'`, `'MIRA_DO'`), (`'url'`, `'https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls'`)]

* To pull the data, take the form URL (`https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls`) and replace `?format=xls` to `.xls`. For our example, the URL should now be: [https://kc.humanitarianresponse.info/api/v1/data/1314.xls](https://kc.humanitarianresponse.info/api/v1/data/1314.xls)

## Pulling data in Microsoft Excel (by making data public)

Before transitioning over the Excel, make sure that there is at least 1 record stored in your data table in KoboToolbox. Once this is ensured, you could click on **Data** and under **Data** you will need to click on **From Web**. You should now get a dialogue box where you could paste your URL. With this, you should be able to have your data in Microsoft Excel (if you have made your data publicly by checking `Anyone can view submissions made to this form` from **SETTINGS>Sharing**).

![image](/images/pulling_data_excelquery/excel_updated.png)

## Pulling data in Microsoft Excel (without making data public)

There are times when you do not wish to make your data public, instead you wish to use your login credentials to pull your data to Excel. If this is how you wish to pull your data into Excel, you could do the following:

* When you get the dialogue box, paste your URL.

![image](/images/pulling_data_excelquery/url.png)

* You should now see a new dialogue box as shown in the image below:

![image](/images/pulling_data_excelquery/basic_authentication.png)

* Then select `Basic`. You should be able to see a place where you are able to input your login credentials. Use your KoBoToolbox credentials and that should load your data to Excel.

![image](/images/pulling_data_excelquery/login_credentials.png)

## Troubleshooting

### Reset Excel's Data Source Settings

Sometimes, you may not be able to see the dialogue box to input your login credentials. In such case, you will have to do the following to reset your Excel's `Data Source Settings`.

* Click on **Data** and under **Data** you will need to click on **Get Data**. 

![image](/images/pulling_data_excelquery/home.png)

* Then click on `Data Source Settings`.

![image](/images/pulling_data_excelquery/home_next.png)

* You will now be able to see a dialogue box, `Data source settings`. Here, you will need to press `Clear Permissions`. With this, you should be able to see the dialogue box to input your login credentials.

![image](/images/pulling_data_excelquery/data_source_settings.png)

If you wish to learn more on resetting your Excel's `Data Source Settings` feel free to explore [here](https://docs.microsoft.com/en-us/power-query/connectorauthentication).

### Updating Data in Microsoft Excel

Once you have synced your KoBoToolbox with your Microsoft Excel through __Excel Power Query__, you should be able to have the dataset in Microsoft Excel. However, when the KoBoToolbox server is updated (i.e. through new submissions, deletion, amendments) your Microsoft Excel dataset does not get updated automatically. You could do this by refreshing the Excel document. For this you will need to click the **Data** and then select **Refresh All**. Any changes made in the KoBoToolbox server will now be manually updated in your Excel dataset. (Please follow this whenever you require an update with your Microsoft Excel dataset)

_**Thanks to Awais Awan for writing the initial draft of this post.**_
