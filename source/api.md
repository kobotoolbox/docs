# Using the API

KoBoToolbox has a number of advanced features built in based on our open source libraries, which include useful add-ons for advanced use cases. There are many ways to use our API. For some hands-on examples, [see this post](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).

KoBoToolbox has two APIs for its primary tools, kpi and kc. Originally kc was the only api for deploying forms and retrieving data. Now, kpi is the primary API that should be used. 

The base URL depends on the server you are using: for most users it is [kf.kobotoolbox.org](https://kf.kobotoolbox.org) or [kobo.humanitarianresponse.info](https://kobo.humanitarianresponse.info). Below we only use [kpi-url] to refer to this base URL.

**API Token:**
To find your API token go to [https://[kpi-url]/token/?format=json](https://[kpi-url]/token/?format=json)

   ![image](/images/api/token.png)  
   
To test it use this command:

curl -X GET https://[kpi-url]/api/v2/assets.json -H "Authorization: Token [your_token_goes_here]"

You can also use tools like Postman to build and test your API snippets:

   ![image](/images/api/test.png)  

For more details on using the API follow these endpoints (selection only): 

[https://[kpi-url]/api/v2/assets/](https://[kpi-url]/api/v2/assets/) (list of all assets, including forms/projects, questions, blocks, templates, collections; for each asset there are several additional sub-endpoints)
[https://[kpi-url]/api/v2/{asset_uid}/data/](https://[kpi-url]/api/v2/{asset_uid}/data/) (access submitted data)
[https://[kpi-url]/exports/](https://[kpi-url]/exports/) (create or view data exports)

You can find more examples [in this forum post](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).

