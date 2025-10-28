# Overview on Data Collection Tools
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/01270a828ec846731411368326ba58114adda98e/source/data-collection-tools.md" class="reference">28 Oct 2025</a>

<a href="es/data-collection-tools.html">Leer en español</a> | <a href="fr/data-collection-tools.html">Lire en français</a> | <a href="ar/data-collection-tools.html">اقرأ باللغة العربية</a>

KoboToolbox allows data collection in multiple ways. Because KoboToolbox is
built on the [Xform/ODK standards](https://xlsform.org), our forms are
compatible with
[a number of different tools](https://xlsform.org/en/#tools-that-support-xlsforms)
that can be used for data collection.

For Android devices, we recommend using
[Collect Andoid app](https://play.google.com/store/apps/details?id=org.koboc.collect.android&hl=en_US)
app, which can be downloaded from the Google Play Store and installed on any
standard Android phone or tablet.

For any other devices (including iPhones, iPads, or any laptop or computer), we
recommend using the webform [for collecting data](data_through_webforms.md).

## A quick rundown on the differences between the two options

| &nbsp;                                                                         | Webforms                                    | KoboCollect                                            |
| :----------------------------------------------------------------------------- | :------------------------------------------ | :----------------------------------------------------- |
| Devices                                                                        | Any mobile device or computer               | Android only                                           |
| Runs in...                                                                     | Browser                                     | Native Android application                             |
| Configurable                                                                   | Server-wide                                 | On each device                                         |
| Default form display                                                           | All questions on the same screen            | One question per screen                                |
| Data upload                                                                    | Automatically when connection available     | On user request or immediately if connection available |
| Phone-specific meta-questions (`subscriberid`, `simserial`, `phonenumber`)     | No                                          | Yes                                                    |
| `barcode` question type                                                        | No (except manual entry)                    | Yes                                                    |
| Different form styles                                                          | Yes                                         | No                                                     |
| Encryption                                                                     | Not for storage, but always during transfer | Can be enabled on-device, always during transfer       |
| `hide-input` appearance for maps to hide manual GPS inputs                     | Yes                                         | No                                                     |
| Advanced map appearance options (`streets`, `terrain`, `satellite`, `[other]`) | Yes                                         | No                                                     |
| Text formatting in notes and labels (bold, italics, links)                     | Yes                                         | No                                                     |
| Combine subsequent notes into a single note on the screen                      | Yes                                         | No                                                     |
| `multiline` appearance for `text` questions                                    | Yes                                         | Yes                                                     |
| `horizontal-compact` appearance for select-type questions                      | Yes                                         | No                                                     |
| `likert` scale appearance for select-type questions                            | Yes                                         | Yes                                                     |
| `compact-2` appearance for select-type questions                               | No                                          | Yes                                                    |
| `no-calendar` appearance                                                       | No                                          | Yes                                                    |
| Advanced image appearances (`annotate`, `draw`, `signature`)                   | Yes                                         | Yes                                                    |
| Calculation command `repeat_count()`                                           | Set a minimum number of repeat groups       | Set an exact number of repeat groups                   |

### Collecting data using KoboCollect

After deploying a project, you can go to **Form - Collect data**, and then
select the Android application.

![image](/images/data_collection_tool/KoboCollect.gif)

For details on how to set up KoboCollect on any Android devices,
[read this article](kobocollect_on_android_latest.md).

### Collecting Data using the Enketo Webform

To [use the webform](data_through_webforms.md), after deploying a project, you
can go to **Form - Collect data**, multiple options (online or offline, single
or multiple submissions) are available. The default option is **Online-Offline
(multiple submission)**.

![image](/images/data_collection_tool/Webform.gif)
