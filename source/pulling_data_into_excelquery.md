# Pulling Data Into Excel Power Query

For seamless data analysis, you can leverage the KoBo API to pull your data into other tools for data analysis. This article covers how to connect to the API to pull your data into __Excel Power Query__.

## Getting KoBo API for Excel Power Query

* Login to your account.

* Next, go to the API for your account by going to either [https://kc.humanitarianresponse.info/api/v1](https://kc.humanitarianresponse.info/api/v1) or [https://kc.kobotoolbox.org/api/v1/](https://kc.kobotoolbox.org/api/v1/). Select the URL for the instance in which your account is located.

* Under the __Data__ heading, click on `/api/v1/data`.

![image](/images/pulling_data_excelquery/api_json.jpg)

* Click on __GET__ and select __xls__.

![image](/images/pulling_data_excelquery/api_datalist.jpg)

* This action will download a text file to your computer called `data` which can be opened/viewed a text editor.

* Next, locate your project's data structure inside the `data` file you downloaded. It will be in the following format: `id`, `id_string`, `title`, `description`, `url`.

__For example:__

```
[
    ("id", "1314"),
    ("id_string", "a7tAUbZp9Ad4MkvW7JSrft")("title", "MIRA_DO"),
    ("description", "MIRA_DO"),
    ("url", "https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls"),
]
```

* To pull the data, take the form URL (`https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls`) and replace `?format=xls` with `.xls`. For our example, the URL should now be: `https://kc.humanitarianresponse.info/api/v1/data/1314.xls`

## Pulling data in Microsoft Excel (by making data public)

Before transitioning over to Excel, ensure that there is _at least one record_ stored in your data table in KoboToolbox _and_ that you have made your data public by checking __Anyone can view submissions made to this form__ from __SETTINGS>Sharing__. Then click on __Data__, and under __Data__, click on __From Web__. You should now see a dialogue box to paste your URL and start pulling data from the server.

![image](/images/pulling_data_excelquery/excel_updated.png)

## Pulling data in Microsoft Excel (without making data public)

Rather than exposing your data publicly, you can use your KoBoToolbox login credentials to authenticate your request:

* When you get the dialogue box, paste your URL.

![image](/images/pulling_data_excelquery/url.png)

* You should now see a new dialogue box as shown in the image below:

![image](/images/pulling_data_excelquery/basic_authentication.png)

* Then select __Basic__. You should be able to see a place where you are able to input your login credentials. Use your KoBoToolbox credentials and that should load your data to Excel.

![image](/images/pulling_data_excelquery/login_credentials.png)

## Troubleshooting

### Reset Excel's Data Source Settings

Sometimes, you may not be able to see the dialogue box to input your login credentials. In such case, you will have to do the following to reset your Excel's __Data Source Settings__.

* Click on __Data__ and under __Data__ you will need to click on __Get Data__.

![image](/images/pulling_data_excelquery/home.png)

* Then click on __Data Source Settings__.

![image](/images/pulling_data_excelquery/home_next.png)

* You will now be able to see a dialogue box, __Data source settings__. Here, you will need to press __Clear Permissions__. With this, you should be able to see the dialogue box to input your login credentials.

![image](/images/pulling_data_excelquery/data_source_settings.png)

If you wish to learn more on resetting your Excel's __Data Source Settings__ feel free to explore [here](https://docs.microsoft.com/en-us/power-query/connectorauthentication).

### Updating Data in Microsoft Excel

Once you have synced KoBoToolbox with Excel through __Excel Power Query__, you should have the dataset stored locally. However, when the dataset on the server updates (i.e. through new submissions, deletions, amendments), your local dataset does not automatically update. To resync your data, you will need to click the __Data__ button and then __Refresh All__.

_Thanks to Awais Awan for writing the initial draft of this post._
