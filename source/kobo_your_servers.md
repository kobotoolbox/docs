# Installing KoboToolbox on Your Own Servers

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/c4236e20933ea5350c1822f820a8ee0882344920/source/kobo_your_servers.md" class="reference">26
Jul 2020</a>

**Warning:** _Installing KoboToolbox on your own server requires advanced server
administration and programming skills. Please understand that you shouldn't use
this in a critical environment without having the technical resources in place
to troubleshoot if needed. Consider installing Kobo on your local computer
instead with [these instructions](kobo_local_computer.md)._

All of the components of KoboToolbox can be installed on your own servers.
KoboToolbox is free and open source, and our code can be found on
[GitHub](https://github.com/kobotoolbox).

We have created a simplified process using Docker called kobo-install, which can
be found [here](https://github.com/kobotoolbox/kobo-install). This is currently
only supported on Linux machines (we recommend Ubuntu Server 18.04.3 LTS or
similar with at least 4GB RAM and at least 20GB storage). We recommend
installing the software first on a local machine using the same script since
server installations require additional configurations for domain names and SSL
certificates.

For details about the different components making up KoboToolbox, see
[this post](software_architecture.md).
