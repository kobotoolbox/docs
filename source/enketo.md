# What Are Enketo Web Forms?

According to [Enketo.org](https://enketo.org), **Enketo** is the name of an open-source project as well as the name of an open-source web application that uses a popular open-source form format. 

Enketo was developed as a follow-up to a 2009 Masters Dissertation at the University of Liverpool on the 'Applicability of [Offline-capable Web Technologies](https://blog.enketo.org/offline-capable-web-applications/) for Information Management in Humanitarian Aid'.

After a year of initial development, it was adopted by [a lab at Columbia University](https://qsel.columbia.edu/products-tools/) and [first launched](https://blog.enketo.org/enketo-is-now-open-source-and-will-be-used-in-formhub/) in 2012. This was the start of a cascade of [adoption](https://enketo.org/about/adoption/) by companies and organizations across the world.

### What Ecosystem does Enketo use?

Enketo is part of the OpenRosa/ODK ecosystem which means:

1. Enketo can be combined with other tools to flexibly create a full-fledged information management system. This has resulted in the adoption of Enketo into KoBoToolBox. It also means that the Enketo Project can focus on just data collection and do this in the best way possible.
2. Enketo does not require a long-term commitment by the user.
 
### What are the general features?

Surveys deployed with Enketo:
* work offline
* have beautiful themes and widgets
* are printer-friendly
* can use very powerful skip and validation logic
* run on any device, mobile or desktop, as long as it has a fairly [modern browser](https://enke.to/modern-browsers)

### How can I access Enketo when on KoBoToolbox? 

Whenever you open a form on the webform version within KoBoToolbox, you are actually using Enketo. For details, please visit our support article [Collecting Data through Web Forms] (data_through_webforms.md).

### How do I troubleshoot Enketo?
Enketo web forms work on all devices since they open in regular web browsers and allow data collection online or offline. Generally we strongly recommend the latest version of all modern browsers; [see here for more details on browsers working with Enketo](https://enketo.org/faq/#browsers).  

**Known issues with offline forms on iOS**

iOS (running on iPhones and iPads) devices have several known limitations with using offline-enabled forms due to the Apple operating system platform. We strive to have the latest version of iOS fully supported.

* Offline data collection works in any modern browser. On iOS we only recommend Chrome or Safari.
* Version 9.x shows "NotFoundError: DOM IDBDatabase Exception 8". Solution: Close all Enketo tabs in your browser, then reopen the form. The error should now be gone forever.
* Version 9.3.1 shows "Attempted to assign to readonly property" when loading offline form
* Version 8.x shows "undefined is not an object (evaluating 'c.resources')". Solution: Update to latest iOS version

If data collection offline is not required and you are seeing an error on iOS, consider using the [online-only version](https://ee.kobotoolbox.org/::ABCD) instead of the offline URL. 

For details on troubleshooting, please visit our support article [Troubleshooting Enketo Web Forms](troubleshooting_webforms.md).
