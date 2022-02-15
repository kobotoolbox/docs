# Pulling Data Into Excel Power Query

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/5c33bf8fbd4550f031cd19567502861063b1d88b/source/pulling_data_into_excelquery.md" class="reference">19
Jan 2022</a>

For seamless data analysis, you can leverage the Kobo API to pull your data into
other tools for data analysis. This article covers how to connect to the API to
pull your data into **Excel Power Query**.

## Getting Kobo API for Excel Power Query

-   Login to your account.

-   Next, go to the API for your account by going to either
    [https://kc.humanitarianresponse.info/api/v1](https://kc.humanitarianresponse.info/api/v1)
    or [https://kc.kobotoolbox.org/api/v1/](https://kc.kobotoolbox.org/api/v1/).
    Select the URL for the instance in which your account is located.

-   Under the **Data** heading, click on `/api/v1/data`.

![image](/images/pulling_data_excelquery/api_json.jpg)

-   Click on **GET** and select **xls**.

![image](/images/pulling_data_excelquery/api_datalist.jpg)

-   This action will download a text file to your computer called `data` which
    can be opened/viewed a text editor.

-   Next, locate your project's data structure inside the `data` file you
    downloaded. It will be in the following format: `id`, `id_string`, `title`,
    `description`, `url`.

**For example:**

```
[
    ("id", "1314"),
    ("id_string", "a7tAUbZp9Ad4MkvW7JSrft")("title", "MIRA_DO"),
    ("description", "MIRA_DO"),
    ("url", "https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls"),
]
```

-   To pull the data, take the form URL
    (`https://kc.humanitarianresponse.info/api/v1/data/1314?format=xls`) and
    replace `?format=xls` with `.xls`. For our example, the URL should now be:
    `https://kc.humanitarianresponse.info/api/v1/data/1314.xls`

## Pulling data in Microsoft Excel (by making data public)

Before transitioning over to Excel, ensure that there is _at least one record_
stored in your data table in KoboToolbox _and_ that you have made your data
public by checking **Anyone can view submissions made to this form** from
**SETTINGS>Sharing**. Then click on **Data**, and under **Data**, click on
**From Web**. You should now see a dialogue box to paste your URL and start
pulling data from the server.

![image](/images/pulling_data_excelquery/excel_updated.png)

## Pulling data in Microsoft Excel (without making data public)

Rather than exposing your data publicly, you can use your KoboToolbox login
credentials to authenticate your request:

-   When you get the dialogue box, paste your URL.

![image](/images/pulling_data_excelquery/url.png)

-   You should now see a new dialogue box as shown in the image below:

![image](/images/pulling_data_excelquery/basic_authentication.png)

-   Then select **Basic**. You should be able to see a place where you are able
    to input your login credentials. Use your KoboToolbox credentials and that
    should load your data to Excel.

![image](/images/pulling_data_excelquery/login_credentials.png)

## Troubleshooting

### Reset Excel's Data Source Settings

Sometimes, you may not be able to see the dialogue box to input your login
credentials. In such case, you will have to do the following to reset your
Excel's **Data Source Settings**.

-   Click on **Data** and under **Data** you will need to click on **Get Data**.

![image](/images/pulling_data_excelquery/home.png)

-   Then click on **Data Source Settings**.

![image](/images/pulling_data_excelquery/home_next.png)

-   You will now be able to see a dialogue box, **Data source settings**. Here,
    you will need to press **Clear Permissions**. With this, you should be able
    to see the dialogue box to input your login credentials.

![image](/images/pulling_data_excelquery/data_source_settings.png)

If you wish to learn more on resetting your Excel's **Data Source Settings**
feel free to explore
[here](https://docs.microsoft.com/en-us/power-query/connectorauthentication).

### Updating Data in Microsoft Excel

Once you have synced KoboToolbox with Excel through **Excel Power Query**, you
should have the dataset stored locally. However, when the dataset on the server
updates (i.e. through new submissions, deletions, amendments), your local
dataset does not automatically update. To resync your data, you will need to
click the **Data** button and then **Refresh All**.

_Thanks to Awais Awan for writing the initial draft of this post._
