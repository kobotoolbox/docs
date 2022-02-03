# Is My Data Safe on Your Server?
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/b12b2b3dce2d89fca8bd8d64219c682eb2bbae1a/source/is_my_data_safe.md" class="reference">19 Jul 2020</a>

Most users use one of the two server instances that we support: [KoBoToolbox by OCHA](https://kobo.humanitarianresponse.info/accounts/login/?next=/#/) (for humanitarian workers) and [KoBoToolbox by HHI](https://kf.kobotoolbox.org/accounts/login/?next=/#/) (for everyone else). KoBoToolbox can also be installed on local computers or your own web servers. This article is about the security of your data on one of the two supported servers hosted by HHI and OCHA.
 
We take the protection of collected data very seriously. Data from both servers is hosted by Amazon Web Services (AWS). Both servers are administered using best practice tools and mechanisms to keep data safe from intrusion or loss. 

The instance hosted by HHI ([kf.kobotoolbox.org](https://kf.kobotoolbox.org)) is physically located in the United States of America. **The humanitarian instance financed by OCHA, is hosted at a data center in Ireland.**

AWS security information can be found on [this page](https://aws.amazon.com/security/). In addition, we do regular database backups to protect against any eventuality. The privacy policy and terms of use are both linked here.
 
Once your data is received on the server it is stored in accounts protected by usernames and passwords. However, unless it was encrypted on the handset [(see this article)](encrypting_forms.md), it will be stored 'in the clear' on the server filesystem or within its database, which means that our server administrators could potentially access it. 

For [kobo.humanitarianresponse.info](https://kobo.humanitarianresponse.info/accounts/login/?next=/#/) and [kc.humanitarianresponse.info](https://kobo.humanitarianresponse.info/accounts/login/?next=/kobocat/#/) only the server administrator has technical access to the database, and we will never access your data unless you have given us explicit access to it. However, to have complete control and ownership of your data, you are also free to install an instance of KoBoToolbox on your own server.

All user passwords are only stored fully encrypted on the KoBoToolbox server, using the default open source framework provided by Django, which we use for our backend. Django uses the [PBKDF2 algorithm](https://en.wikipedia.org/wiki/PBKDF2) with a [SHA256 hash](https://en.wikipedia.org/wiki/SHA-2). This approach is considered very secure as such encrypted passwords require enormous amounts of computing power and time to break. Read more about Django's password encryption process [here](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/).
