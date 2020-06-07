# Software Architecture

KoBoToolbox consists of the following components, all of which are open source (see links for source code):

   * [kpi](https://github.com/kobotoolbox/kpi) - for creating survey forms and reusing assets through a question library.
   * [kobocat](https://github.com/kobotoolbox/kobocat) and [kobocat-templates](https://github.com/kobotoolbox/kobocat-template) - for deploying surveys, collecting, and analyzing data.
   * [enketo-express](https://github.com/kobotoolbox/enketo-express/) - HTML5 Web app for collecting data, previewing forms, editing data submissions.
   * [kobocollect](https://play.google.com/store/apps/details?id=org.koboc.collect.android) - Android app for collecting data.

KoBoToolbox is based on elements from several other open source tools, most importantly pyxform, formhub/onadata, and the OpenDataKit. As a result, all forms and collected data are compatible with these tools. 

**High-level server-side overview**

![image](/images/software_architecture/overview.png)

The best way to use KoBoToolbox is on one of the two public instances - [kobo.humanitarianresponse.info](http://kobo.humanitarianresponse.info) (if you work for a humanitarian organization) and [kf.kobotoolbox.org](http://kf.kobotoolbox.org) (non-humanitarians). There is no software to be installed on your computer. Installing KoBoToolbox on your own computer is not necessary and is only recommended if you work in an environment with absolutely no Internet access.

For installing KoBoToolbox on a local computer or server, visit [github.com/kobotoolbox/kobo-install](https://github.com/kobotoolbox/kobo-install).
