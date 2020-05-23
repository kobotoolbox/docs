# Encrypting Forms

_This procedure is quite technical and is intended for users who are comfortable with advanced technical instructions and requires strict attention to detail._ 

Encrypted forms work by encrypting the data on the phone the moment it is saved. Data sent to KoBoToolbox is encrypted and completely inaccessible to anyone not possessing the private key. In this case, KoBoToolbox serves simply as a storage locker for your encrypted files - a place to upload and then download for later for local decryption ([using ODK Briefcase](http://blog.formhub.org/2013/06/27/formhub-supports-odk-briefcase/)). Since the form submissions are encrypted, it means, however, anything that requires access to the data like the map view or data export won't work within KoBoToolbox. The extra level of security makes using KoBoToolbox in a way to collect sensitive data while meeting certain data protection protocols possible.

### How it Works

KoBoCollect supports the ability to encrypt the content of a form the moment it is marked as completed and ready for submission on the phone. To take advantage of this requires the use of a public encryption key which you include in the XLSForm and a private key (which you never share) that is used by ODK Briefcase to decrypt the data locally after you've downloaded it from KoBoToolbox. The public key is used to encrypt data while the private key decrypts it. Only a person who has the private key, can decrypt the data encrypted with the public key. To understand more about public and private key infrastructure see [here](https://en.wikipedia.org/wiki/Public-key_cryptography).

### How to encrypt XLS forms

1. Create your form in KoBoToolbox as always. Download the form from the drafts list as an XLS file.
2. In the downloaded file go to the 'settings' sheet.
3. Add a column _submission_url_ and type `https://kc.kobotoolbox.org/yourusername/submission` or `https://kc.humanitarianresponse.info/yourusername/submission` (depending upon the server you are using). Please note that yourusername is your KoBoToolbox user account. 
4. Add another column _public_key_ (i.e. base64RsaPublicKey). Paste your compatible public key. 

(Please see image below for reference)

![image](/source/images/encrypting_forms/column.png)

5. Upload the XLS file back to KoBoToolbox. You can either import it back to the Form Drafts list and then deploy it as a new survey project, or import it directly to your deployed Projects list. Once deployed you should see a label with the text "encrypted" next to your form name.

### How to decrypt forms

ODK Briefcase is used to download the encrypted files from KoBoToolbox and decrypt them locally on your computer using a private key ensuring single access to the data. For decryption to be successful with ODK Briefcase make sure you download and install the _Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6_ from the [Java download site](https://www.oracle.com/java/technologies/javase-downloads.html). This is required for decryption to be successful.

**To install the JCE:**

1. Unzip the downloaded zip archive
2. Navigate into the extracted directory tree and copy the local_policy.jar and US_export_policy.jarfiles to the lib\security directory
3. Paste these files inside the installation directory of the Java Runtime Enviornment (JRE) of your computer, replacing earlier versions of these files.

* On **Windows**, the JRE is usually installed here: C:\Program Files\Java\jre7\lib\securityOn OSX the location is /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/security
* On **OSX** the location is /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/security

**To decrypt your forms:**

1. Download and open [ODK Briefcase](https://docs.getodk.org/briefcase-intro/).
2. Specify a **Storage Location** under the **Settings** tab.
3. Open the **Pull** tab and click **Configure**. 

![image](/images/encrypting_forms/configure.png)


