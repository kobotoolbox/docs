# Software Architecture
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/f57c621e04d964a711a55ea6b0969087404e2dd8/source/software_architecture.md" class="reference">21 Sep 2023</a>

KoboToolbox consists of the following components, all of which are open source
(see links for source code):

-   [kpi](https://github.com/kobotoolbox/kpi) - for creating survey forms and
    reusing assets through a question library.
-   [kobocat](https://github.com/kobotoolbox/kobocat) and
    [kobocat-templates](https://github.com/kobotoolbox/kobocat-template) - for
    deploying surveys, collecting, and analyzing data.
-   [enketo-express](https://github.com/kobotoolbox/enketo-express/) - HTML5 Web
    app for collecting data, previewing forms, editing data submissions.
-   [kobocollect](https://play.google.com/store/apps/details?id=org.koboc.collect.android) -
    Android app for collecting data.

KoboToolbox is based on elements from several other open source tools, most
importantly pyxform, formhub/onadata, and the OpenDataKit. As a result, all
forms and collected data are compatible with these tools.

## High-level server-side overview

![image](/images/software_architecture/overview.png)

The best way to use KoboToolbox is on one of the two public instances -
[kf.kobotoolbox.org](https://kf.kobotoolbox.org) and
[eu.kobotoolbox.org](https://eu.kobotoolbox.org) (for organizations that prefer data hosting in the European Union). There is no
software to be installed on your computer. Installing KoboToolbox on your own
computer is not necessary and is only recommended if you work in an environment
with absolutely no Internet access.

For installing KoboToolbox on a local computer or server, visit
[github.com/kobotoolbox/kobo-install](https://github.com/kobotoolbox/kobo-install).
