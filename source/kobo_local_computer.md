# Installing KoboToolbox on a Local Computer
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/e2788bf7cbca4b5c7245293ad7cb9a94dc2fb55f/source/kobo_local_computer.md" class="reference">11 Sep 2023</a>

The best way to use KoboToolbox is on one of the two public instances -
[kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (used by the majority of our users) and [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (used by organizations that require or prefer data hosting in the European Union).
**There is no software to be installed on your computer when using these free
public servers.** For more help deciding which server to use,
[check this article](creating_account.md).

Installing KoboToolbox on your own computer is **not necessary** and is only
recommended if 1) you are a developer looking to contribute code to our
[open source repositories](https://github.com/kobotoolbox), or 2) if you are an
advanced user and work in an environment with absolutely no Internet access or
if security circumstances prevent using a cloud server. To learn about
installing the software on your own servers, [click here](kobo_your_servers.md).

**Installing KoboToolbox with Docker and kobo-install**

**Warning**: _This requires advanced knowledge of terminal/command line
programming, a good understanding of installing and maintaining server software,
and an ability to self-troubleshoot. Please understand that you shouldn't use
this in a critical environment without having the technical resources in place
to troubleshoot if needed._

KoboToolbox can be installed on Linux or Mac OSX using our own Docker
installation, using the latest code as is available on our public websites. The
detailed instructions and the source repository
[are found on Github](https://github.com/kobotoolbox/kobo-install). For Windows
users we recommend creating a virtual machine running Linux (at least 4GB RAM
and 20GB storage) and following the instructions within this virtual machine.

With Docker, you can run a small "mini server" on your local computer. This
means that the software is still accessed through the browser but from a "local"
address. Note: This requires your computer to be connected to a local network
(WiFi or Ethernet) for the local server to function (and for your mobile devices
to be able to submit data). This local network does not need to be connected to
the Internet.
