# Collecting Data Offline
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/b70cdbf084f645b5cefa1a9368456f8f37b7245c/source/data-offline.md" class="reference">17 Oct 2025</a>


**All data collection can take place offline, both with KoboCollect and with Web
Forms.**

When a user enters data it is stored first on the device. KoboCollect [can be set](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) to attempt sending the information through a network connection immediately or
only at a later stage when the interviewer or supervisor wants to upload
finalized forms. Web Forms will always attempt to upload data immediately and
will retry until a connection has been established again.

All synchronization is proofed even against poor Internet connection quality.
Should a connection time out or be interrupted while a specific form is being
transferred, it will be resent with the next upload attempt. The server will not
integrate half received data in this case. Only when a record has been uploaded
successfully and the server confirms receipt will the survey data be removed
from the upload queue.

Web Forms uses the browser's HTML5 offline storage to store survey responses as
well as the form itself. It is important to wait for the small confirmation
message in the top-right on the form, which will show a green checkmark once the
form has been cached. After this the form can be accessed and data can be
entered even without any connection. It is recommended to create a bookmark on
the device to easily access specific forms

## What do I do if I have NO access to the internet?

If it is not possible to connect a handset to the Internet at all (the
interviewers can't move into an area where a connection is available), then it
is also possible to transfer survey data from KoboCollect through an external
tool [ODK Briefcase](https://docs.getodk.org/briefcase-intro)) and by connecting
the mobile devices by USB cable to a local computer. For more details about how
to use ODK Briefcase to transfer data,
[read this post](https://blog.cartong.org/2016/03/11/migration-odk-platforms).
After this is it possible to upload the survey data from a centralized computer
to the KoboToolbox server, using the same tool.

Finally, it is also possible to install KoboToolbox on a local computer, e.g. a
laptop, and then connect local mobile devices through a local WiFi to the
computer. This WiFi does not need to be connected to the Internet as there would
be a direct connection between the mobile devices and the local computer.
[See here](https://github.com/kobotoolbox/kobo-install) to find out how to install KoboToolbox on
your computer.
