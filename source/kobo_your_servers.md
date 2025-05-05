# Installing KoboToolbox on Your Own Servers
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/8479a024db827ded48ee0596995d14b770823cea/source/kobo_your_servers.md" class="reference">3 Oct 2024</a>

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
only supported on Linux machines. We recommend Ubuntu Server LTS or
similar with at least 4GB RAM and at least 20GB storage. More resources are 
strongly recommended if the server is used for high volume data collection. We recommend
installing the software first on a local machine using the same script since
server installations require additional configurations for domain names and SSL
certificates.

For details about the different components making up KoboToolbox, see
[this post](software_architecture.md).
