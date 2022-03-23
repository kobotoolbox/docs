# KoboToolbox data security measures

We take protecting our users’ data very seriously. This article summarizes some of our administrative, physical, organizational, and technical measures for enforcing data security on our KoboToolbox servers (kobo.humanitarianresponse.info and kf.kobotoolbox.org).

1. Confidentiality
   - Physical Access Control
Physical access control measures, amongst others, are implemented by Amazon Web Services, which is used to host our KoboToolbox servers. For details about AWS technical and organizational measures for physical access control, see this article on data center controls. 

   - Electronic Access Control

     - All KoboToolbox accounts are password-protected. Users are provided visual feedback about the complexity of their password, which encourages them to select a stronger password when applicable. Passwords are stored fully encrypted on the KoboToolbox Server, utilizing the default open-source framework provided by Django, which uses the PBKDF2 algorithm with a SHA256 hash.
     - All database content is encrypted at rest (database-level encryption).
     - Users can choose to enable encryption of their project data[b] (data-level encryption) which renders it inaccessible at all stages of data processing and requires a private key to decrypt it locally.
     - Users found to abuse the use of their API keys by overburdening the KoboToolbox Server may be suspended or their account may be restricted.
   - Internal Access Control
     - Only authorized system administrators can access the KoboToolbox Server. They may only do so for the express purpose of updating installed software or maintaining the server infrastructure.
     - System administrators require additional authentication, including SSH Public Key authentication, for accessing the KoboToolbox Server and two-factor authentication for accessing control panels provided by Sub-Processor.
     - Sub-Processor provides a log of actions taken in the AWS Console. For SSH connections into the individual KoboToolbox Server instances, Kobo collects "system access events" by SSH key, which can then be matched to the authorized users.
     - Only explicitly listed IP addresses are allowed to connect to production servers.
   - Data Protection by Design and Default
     - Only limited information is required for creating a KoboToolbox user account.
     - Kobo staff are required to abide by the rules set out in Kobo’s privacy policies.
     - Data processed on behalf of the user is not accessed by Kobo.
     - Users are provided the option of applying advanced encryption. This ensures that data is encrypted using a public key before it is submitted to a KoboToolbox Server, and that it can only be decrypted with a private key on a local computer. KoboToolbox also offers the possibility of removing information in bulk once it has been collected, facilitating the pseudonymization of Personal Data (through the removal of identifiers).
     - See above sub-section “Electronic Access Control” for details about visual feedback on password complexity.
2. Integrity
   - Data Transfer Control
All data in transit is protected using SHA-256 with RSA encryption.
   - Data Entry Control
For using the Services, personal data is entered by the user. HTTP access logs include the authenticated user for most requests.
3. Availability and Resilience
    - Kobo conducts daily backups of all databases to a separate, remote location. In case of a critical outage, all user data will be restored from the most recent backup as quickly as possible.
    - Firewalls block all external requests except for SSH connections from a small list of explicitly allowed IP addresses. Public HTTP and HTTPS traffic cannot connect directly to the KoboToolbox Server, instead it is serviced by the Sub-Processor’s load balancer, which then forwards it to Kobo’s front-end servers.
    - KoboToolbox Servers are configured to use multiple concurrently running server instances and are set to increase the number of such instances to avoid the impact of any localized failures. In case of any other failures that threaten continuous operation of critical aspects of the KoboToolbox software, system administrators stand by to intervene on short notice to restore service.
    - Kobo’s reporting procedures include automated alerts, escalation of user-reported issues, and self-noticed problems by staff.
    - Contingency plans include the availability of multiple people in multiple geographic locations who can respond to emergencies and restore service.
    - KoboToolbox Servers have the demonstrated ability to continue operating in a degraded state, receiving submissions while simultaneously recovering lost projects/submissions via to-the-minute point-in-time recovery (PITR).