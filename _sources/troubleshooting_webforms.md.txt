# Troubleshooting Enketo Web Forms
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/e2995378ff58eb4a239119fa45490cccd0bd9c27/source/troubleshooting_webforms.md" class="reference">26 Feb 2021</a>

[Enketo web forms](enketo.md) work on all devices since they open in regular web browsers and allow data collection online or offline. Generally we strongly recommend the latest version of all [modern browsers](https://enke.to/modern-browsers). You could also visit [Enketo's Frequently Asked Questions](https://enketo.org/faq/#browsers) to learn more about *what browsers are supported and recommended* by Enketo.

## Known issues with offline forms on iOS

iOS (running on iPhones and iPads) devices have several known limitations with using offline-enabled forms due to the Apple operating system platform. We strive to have the latest version of iOS fully supported.

* Offline data collection works in any modern browser. On iOS we only recommend Chrome or Safari.
* Version 9.x shows "NotFoundError: DOM IDBDatabase Exception 8". Solution: Close all Enketo tabs in your browser, then reopen the form. The error should now be gone forever.
* Version 9.3.1 shows "Attempted to assign to readonly property" when loading offline form
* Version 8.x shows "undefined is not an object (evaluating 'c.resources')". Solution: Update to latest iOS version

If data collection offline is not required and you are seeing an error on iOS, consider using the _online-only version_ instead of the offline URL.

## Data loss

When collecting data through Enekto, users should never clear the browser's cache (either manually or using some app). Clearing your browser's cache (during data collection) will remove all the information stored in the browser and thus your information will not reach your KoBoToolbox server. This data loss is irreversible. Hence we strongly advise users to clear the browser's cache if and only if you have successfully submitted all your data to your KoBoToolbox server.
