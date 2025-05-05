# Encrypting Forms
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/179faeb3c5a17b69406b0243ab9c22f7ca86aa44/source/encrypting_forms.md" class="reference">4 Nov 2024</a>

_This procedure is quite technical and is intended for users who are comfortable
with advanced technical instructions and requires strict attention to detail._

Encrypted forms work by encrypting the data on the phone the moment it is saved.
Data sent to KoboToolbox is encrypted and completely inaccessible to anyone not
possessing the private key. In this case, KoboToolbox serves simply as a storage
locker for your encrypted files - a place to upload and then download for later
for local decryption
([using ODK Briefcase](http://blog.formhub.org/2013/06/27/formhub-supports-odk-briefcase/)).
Since the form submissions are encrypted, it means, however, anything that
requires access to the data like the map view or data export won't work within
KoboToolbox. The extra level of security makes using KoboToolbox in a way to
collect sensitive data while meeting certain data protection protocols possible.

## How it Works

KoboCollect supports the ability to encrypt the content of a form the moment it
is marked as completed and ready for submission on the phone. To take advantage
of this requires the use of a public encryption key which you include in the
XLSForm and a private key (which you never share) that is used by ODK Briefcase
to decrypt the data locally after you've downloaded it from KoboToolbox. The
public key is used to encrypt data while the private key decrypts it. Only a
person who has the private key, can decrypt the data encrypted with the public
key. To understand more about public and private key infrastructure
[see here](https://en.wikipedia.org/wiki/Public-key_cryptography).

## How to encrypt XLS forms

1. Create your form in KoboToolbox as always. Download the form from the drafts
   list as an XLS file.

2. In the downloaded file go to the 'settings' sheet.

3. Add a column _submission_url_ and type
   `https://kc.kobotoolbox.org/submission` or
   `https://kc-eu.kobotoolbox.org/submission` (depending
   upon the server you are using).

5. Add another column _public_key_ (i.e. base64RsaPublicKey). Paste your
   compatible public key.

    (Please see image below for reference)

    ![image](/images/encrypting_forms/column.png)

6. Upload the XLS file back to KoboToolbox. You can either import it back to the
   Form Drafts list and then deploy it as a new survey project, or import it
   directly to your deployed Projects list. Once deployed you should see a label
   with the text "encrypted" next to your form name.

<p class="note">
  Please note that the URL for an authenticated user no longer includes **yourusername** per recent updates. 
</p>

## How to decrypt forms

ODK Briefcase is used to download the encrypted files from KoboToolbox and
decrypt them locally on your computer using a private key ensuring single access
to the data. For decryption to be successful with ODK Briefcase make sure you
download and install the _Java Cryptography Extension (JCE) Unlimited Strength
Jurisdiction Policy Files 6_ from the
[Java download site](https://www.oracle.com/java/technologies/javase-jce-all-downloads.html).
This is required for decryption to be successful.

### To install the JCE:

1. Unzip the downloaded zip archive

2. Navigate into the extracted directory tree and copy the local_policy.jar and
   US_export_policy.jarfiles to the lib\security directory

3. Paste these files inside the installation directory of the Java Runtime
   Enviornment (JRE) of your computer, replacing earlier versions of these
   files.
    - On **Windows**, the JRE is usually installed here: C:\Program
      Files\Java\jre7\lib\security
    - On **OSX** the location is /Library/Internet
      Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/security

### To decrypt your forms:

1. Download and open [ODK Briefcase](https://docs.getodk.org/briefcase-intro/).

2. Specify a **Storage Location** under the **Settings** tab.

3. Open the **Pull** tab and click **Configure**.  
   ![image](/images/encrypting_forms/configure.png)

4. Then enter the following:

    - `https://kc.kobotoolbox.org` OR
      `https://kc-eu.kobotoolbox.org`(depending on which
      server you use)
    - Your username
    - Your password
    - Press **Connect** when done  
      ![image](/images/encrypting_forms/connect.png)

<p class="note">
  Please note that the server URLs above no longer need to include **yourusername** per recent updates. 
</p>

5. A list of projects is displayed. Select a project that you wish to pull and
   press **Pull**. You will receive a message **Success** under the **Pull
   Status**.

6. Now go to **Export** tab.

7. Press the **Edit Default Configuration** to ensure that you have the **PEM
   private key** at the **PEM file location**.  
   ![image](/images/encrypting_forms/private_key.png)  
   If it’s not there, select the **PEM private key** from the folder you had
   secured safely. (_Note: You will also see all the projects here that has been
   successfully pulled._)

8. Now check the project that you would wish to export and press **Export**.

9. Data is exported as a CSV file, you can now view the unencrypted data.

## Generating RSA Encryption Keys

To generate the RSA public-private key pairs you can use the OpenSSL software
package, which is pre-installed on OSX and Linux. On Windows you have to
download and install the OpenSSL software package from
[this site](http://slproweb.com/products/Win32OpenSSL.md). (_Note: install the
Win64 OpenSSL v1.1.1c in **C**: rather than the default location **C:\Program
Files**_)

### How to generate RSA key for use with encrypted forms on KoboToolbox

_Note: We strongly recommend using OpenSSL as documented below for creating your
public/private key pair as other methods may not be supported by the software._

1. Open a Windows 'cmd' window.

2. Type the following command: `cd C:\OpenSSL-Win32\bin` to change to the /bin
   directory in the OpenSSL directory.

    ![image](/images/encrypting_forms/openssl_1.png)

3. Create a 2048-bit private key and write it to the **MyPrivateKey.pem** file
   by typing the following command, then press **Enter**:
   `openssl genpkey -out MyPrivateKey.pem -outform PEM -algorithm RSA -pkeyopt rsa_keygen_bits:2048`

    ![image](/images/encrypting_forms/openssl_2.png)

4. Then, extract the public key for the above private key. Type the following
   command then press **Enter**:
   `openssl rsa -in MyPrivateKey.pem -inform PEM -out MyPublicKey.pem -outform PEM -pubout`

    ![image](/images/encrypting_forms/openssl_3.png)

5. You have now generated two files that is:

    - **MyPrivateKey.pem** - your private key that you need to move to a secure
      location.
    - **MyPublicKey.pem** - your public key, that you can share with anyone you
      want to share information securely

6. Open the **MyPublicKey.pem** with Notepad or another text edit, your public
   key is the uninterrupted very long string of characters,

`e.g.:Tjhfur1K9+BRQ2USezIPbtyahbfuNqviI5Suhm8maA3JoELRHj9psjf/oNWoG87aFtKNbLrRaCEDP oFMDC9NEzWlv5L49BygeieMu/wg/rtMT0M0kgDbKxw5weJJgyb9P41aMsrqAAAAB3NzaC1yc2EAAAADAQAB AAABAQDfNoFX7bh3bfdW6lGfDht1Ea8PUBLKYjugbHN5jS7j5fHV6dexM+kzvITVgoyjhhKPXeCbaT62vD/ saTqJFXJzlysnZ24fqxNkjreO5K5EQ9c3ggwqML06+AKrFUSP5jpnyJJH8btNwKl6D5pG4ZseHwDUKzZtae xtPTNQz67kdYIKdtCkCsQHVsy4xvy/A0jzfK3xyOkG6j+L`

This string is what you will need to paste under the public_key field in your
settings sheet on your XLS file.

**IMPORTANT**: make sure that you paste only the public key string and no blank
spaces or line breaks!

**MyPrivateKey.pem** is the file you will use when exporting the submissions
using ODK Briefcase.

Note: When trying to edit a form that has been encrypted, you receive a message
“This form cannot be edited once it has been marked as finalized. It may by
encrypted”.
