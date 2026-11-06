# Data security and protection in KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/4b23386a4f434718a2d9d1c203661406b44dbba0/source/is_my_data_safe.md" class="reference">8 Sep 2026</a>

KoboToolbox uses administrative, physical, organizational, and technical security measures to protect user data. This article provides an overview of the security measures implemented on the KoboToolbox servers managed by [Kobo, Inc.](https://www.kobo.ngo/about), the nonprofit organization behind KoboToolbox.

KoboToolbox [complies](https://support.kobotoolbox.org/gdpr.html) with the European Union's General Data Protection Regulation (GDPR). Users in the European Union can also sign a [Data Processing Agreement (DPA)](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Data confidentiality

KoboToolbox uses several security measures to prevent unauthorized access to user data.

### Physical access controls

KoboToolbox servers are hosted by Amazon Web Services (AWS), which implements physical security measures to protect its data centers. These include video surveillance, controlled access to server facilities, and restricted access to authorized personnel.

<p class="note">
For more information, see <a href="https://aws.amazon.com/compliance/data-center/controls/">AWS Data Center Controls</a>.
</p>


### Account security and data encryption

KoboToolbox uses the following measures to protect user accounts and data:

* **Password protection:** All KoboToolbox accounts are password-protected. Users receive feedback on password strength to help them create secure passwords.
* **Two-factor authentication (2FA):** All KoboToolbox users can [enable two-factor authentication](https://support.kobotoolbox.org/two_factor_authentication.html) to add an extra layer of security to their accounts.
* **Secure password storage:** Passwords are stored as encrypted password hashes using Django's password-hashing framework, which uses the PBKDF2 algorithm with SHA-256. Plain-text passwords are never stored on the server.
* **Encryption at rest:** All database content is encrypted at rest using disk-level encryption.
* **Encryption in transit:** Data transmitted to KoboToolbox servers is encrypted to protect it during transfer.
* **Advanced data encryption:** Users can [enable project-level encryption](https://support.kobotoolbox.org/encrypting_forms.html) to encrypt form submissions before they reach the server. Encrypted data can only be decrypted locally using the corresponding private key.

### Internal access controls

Access to KoboToolbox servers is restricted to authorized system administrators for software updates and server maintenance.

Additional security measures include:
* **Authentication:** System administrators must use SSH public key authentication to access servers and two-factor authentication to access AWS management consoles.
* **Access logging:** AWS records actions performed in its management console. Kobo also records SSH access events, which can be linked to authorized users through their SSH keys.
* **Network restrictions:** Firewalls restrict SSH connections to a limited list of authorized IP addresses, helping prevent unauthorized access and brute-force attacks.


### Data protection by design and default

KoboToolbox incorporates data protection measures into its platform design and default settings:

* Only limited personal information is required to create a KoboToolbox account.
* Kobo staff must follow the organization's privacy policies.
* Kobo does not access data processed on behalf of users.
* Users can enable advanced encryption to protect submissions before they reach KoboToolbox servers.
* Users can remove identifying information from collected data in bulk to support pseudonymization.

## Data integrity

KoboToolbox implements measures to protect data during transmission and control who can submit data.

### Data transfer controls

Data transmitted between users and KoboToolbox servers is encrypted to protect it during transfer.

### Data entry controls

Project owners can manage who is allowed to submit data using KoboToolbox's permission settings.

Server access logs also record authenticated usernames for most HTTP requests, helping track user activity.

## Data availability and resilience

KoboToolbox uses backup, monitoring, and infrastructure measures to maintain service availability and support recovery in case of system failures.

### Data backups and recovery

* Kobo performs daily backups of all databases to a separate, remote location.
* In the event of a critical outage, Kobo works to restore user data from the most recent backup as quickly as possible.
* KoboToolbox supports point-in-time recovery (PITR), allowing data to be restored to a specific point in time. The platform can continue receiving submissions in a reduced-capacity state while recovery is underway.

### Server infrastructure and availability

* **Network protection:** Firewalls restrict external connections. Public HTTP and HTTPS traffic is routed through AWS load balancers rather than connecting directly to KoboToolbox servers.
* **Redundant infrastructure:** KoboToolbox uses multiple server instances running simultaneously. Additional instances can be added to reduce the impact of localized failures.
* **System monitoring:** Automated alerts, user reports, and staff monitoring help identify and address technical issues.
* **Incident response:** System administrators are available to respond to critical failures. Kobo also maintains contingency plans involving staff in multiple geographic locations to support service recovery.

### Preventing service disruptions
To maintain platform availability, Kobo may restrict or suspend accounts that place excessive demands on KoboToolbox servers or otherwise abuse the service.

<p class="note">
To learn more about KoboToolbox's security and data protection practices, visit the <a href="https://trust.kobotoolbox.org">KoboToolbox Trust Center</a>.
</p>
