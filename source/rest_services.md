# REST Services
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/rest_services.md" class="reference">15 Feb 2022</a>

**How to link your data to other servers or services using REST Services**

KoboToolbox has a number of advanced features built in based on our open source
libraries, which include useful add-ons for advanced use cases.

You can link your data collected with KoboToolbox to other servers or services
you might own through REST Services. REST Services supports JSON or XML formats,
and basic authentication. Moreover it’s possible to send only a subset of
fields.

In case of a failure, the background task will retry 3 times to send the data
(first time after 60 seconds, second time after 600 seconds, and third time
after 6,000 seconds). Email notifications can be enabled to receive a failure
report.

Note that your data is sent to the external server only on creation. Nothing is
sent when data is edited.

Here are some tutorial videos for using REST Services:

1. Creation

    [![Creation](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Creation")

2. Subset of fields (Fields are added by pressing “Enter” or “Tab”)

    [![Subset of fields](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Subset of fields")

3. Failure/Retry

    [![Failure / Retry](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Failure / Retry")

4. Custom Wrapper (Only available with JSON format)

    [![Custom Wrapper](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Custom Wrapper")
