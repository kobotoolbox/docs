# Using the API

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/api.md" class="reference">15
Feb 2022</a>

KoboToolbox has a number of advanced features built in based on our open source
libraries, which include useful add-ons for advanced use cases. There are many
ways to use our API. For some hands-on examples,
[see this post](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).

KoboToolbox has two APIs for its primary tools, kpi and kc. Originally kc was
the only api for deploying forms and retrieving data. Now, kpi is the primary
API that should be used.

The base URL depends on the server you are using: for most users it is
[kf.kobotoolbox.org](https://kf.kobotoolbox.org) or
[kobo.humanitarianresponse.info](https://kobo.humanitarianresponse.info). Below
we only use [kpi-url] to refer to this base URL.

## Getting your API Token:

There are different ways to get your API Token.

**Method 1:**

To find your API token go to
[https://[kpi-url]/token/?format=json](https://[kpi-url]/token/?format=json)

![image](/images/api/token.png)

**Method 2:**

-   Select ACCOUNT SETTINGS (from where you normally log out) as shown in the
    image below:

    ![image](/images/api/token1.png)

-   Then press the eye like button to view your Token as shown in the image
    below:

    ![image](/images/api/token2.png)

**Method 3:**

You could use the following curl command:

`curl -u username:password "https:/[kpi-url]/token/?format=json"`

## Testing your API:

To test it use this command:

`curl -X GET https://[kpi-url]/api/v2/assets.json -H "Authorization: Token [your_token_goes_here]"`

You can also use tools like Postman to build and test your API snippets:

![image](/images/api/test.png)

For more details on using the API follow these endpoints (selection only):

[https://[kpi-url]/api/v2/assets/](https://[kpi-url]/api/v2/assets/) (list of
all assets, including forms/projects, questions, blocks, templates, collections;
for each asset there are several additional sub-endpoints)
[https://[kpi-url]/api/v2/assets/{asset_uid}/data/](https://[kpi-url]/api/v2/assets/{asset_uid}/data/)
(access submitted data) [https://[kpi-url]/exports/](https://[kpi-url]/exports/)
(create or view data exports)

You can find more examples
[in this forum post](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).
