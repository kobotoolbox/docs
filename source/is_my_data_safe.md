# KoboToolbox data security measures: Keeping your data safe
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/ede450dc2aabb27eda65076d0334d897949825dd/source/is_my_data_safe.md" class="reference">7 Mar 2023</a>

We take data protection very seriously. Data security means protecting our
users’ data from any threats that may exist. This article summarizes some of our
administrative, physical, organizational, and technical measures for enforcing
data security on the KoboToolbox servers maintained by Kobo, Inc., the
[nonprofit organization behind KoboToolbox](https://www.kobotoolbox.org/kobo/).

We are fully compliant with the European Union’s General Data Protection
Regulation (GDPR). If you are located in the European Union,
[you can sign a data processing agreement (DPA) here](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Confidentiality

**Physical Access Control**

-   Physical access control measures, amongst others, are implemented by Amazon
    Web Services (AWS), which is used to host our KoboToolbox servers. These
    measures include, for example, video surveillance and physical security of
    server and network facilities, maintaining key card access control, limiting
    access to only authorized personnel. For a full list of details about AWS
    technical and organizational measures for physical access control,
    [see this article](https://aws.amazon.com/compliance/data-center/controls/)
    on data center controls provided by AWS.

**Electronic Access Control**

-   All KoboToolbox accounts are password-protected. Users are provided visual
    feedback about the complexity of their password, which encourages them to
    select a stronger password when applicable. Only encrypted password hashes
    are stored on the KoboToolbox server, utilizing the default open-source
    framework provided by Django, which uses the
    [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) algorithm with a SHA256 hash.
    Plain text passwords are never saved on the server.
-   All database content is encrypted at rest (disk-level encryption).
-   Data sent to the server is encrypted in transit using SHA-256 with RSA
    encryption.
-   Users can
    [choose to also enable encryption of their project data (data-level encryption)](encrypting_forms.md)
    which renders it inaccessible at all stages of data processing and requires
    a private key to decrypt it locally.

**Internal Access Control**

-   Only authorized system administrators can access the KoboToolbox Server.
    They may only do so for the express purpose of updating installed software
    or maintaining the server infrastructure.
-   System administrators require additional authentication, including SSH
    Public Key authentication, for accessing the KoboToolbox Server and
    two-factor authentication for accessing control panels provided by AWS.
-   AWS provides a log of actions taken in the AWS Console. For SSH connections
    into the individual KoboToolbox Server instances, Kobo collects "system
    access events" by SSH key, which can then be matched to the authorized
    users.
-   SSH is further protected against brute-force attempts and unauthorized
    access by limiting connections at the firewall level to only a small list of
    explicitly-allowed IP addresses.

**Data Protection by Design and Default**

-   Only limited information is required for creating a KoboToolbox user
    account.
-   Kobo staff are required to abide by the rules set out in Kobo’s privacy
    policies.
-   Data processed on behalf of the user is not accessed by Kobo.
-   Users are provided the option of applying advanced encryption. This ensures
    that data is encrypted using a public key before it is submitted to a
    KoboToolbox Server, and that it can only be decrypted with a private key on
    a local computer. KoboToolbox also offers the possibility of removing
    information in bulk once it has been collected, facilitating the
    pseudonymization of Personal Data (through the removal of identifiers).
-   See above sub-section “Electronic Access Control” for details about visual
    feedback on password complexity.

## Integrity

**Data Transfer Control**

-   All data in transit is protected using SHA-256 with RSA encryption.

**Data Entry Control**

-   Users control who has the permission to enter data based on their
    KoboToolbox permissions. HTTP access logs stored on the server include the
    authenticated user for most requests.

## Availability and Resilience

-   Kobo conducts daily backups of all databases to a separate, remote location.
    In case of a critical outage, all user data will be restored from the most
    recent backup as quickly as possible.
-   Firewalls block all external requests except for SSH connections from a
    small list of explicitly allowed IP addresses. Public HTTP and HTTPS traffic
    cannot connect directly to the KoboToolbox Server, instead it is serviced by
    the AWS load balancer, which then forwards it to Kobo’s front-end servers.
-   KoboToolbox Servers are configured to use multiple concurrently running
    server instances and are set to increase the number of such instances to
    avoid the impact of any localized failures. In case of any other failures
    that threaten continuous operation of critical aspects of the KoboToolbox
    software, system administrators stand by to intervene on short notice to
    restore service.
-   Kobo’s reporting procedures include automated alerts, escalation of
    user-reported issues, and self-noticed problems by staff.
-   Contingency plans include the availability of multiple people in multiple
    geographic locations who can respond to emergencies and restore service.
-   KoboToolbox Servers have the demonstrated ability to continue operating in a
    degraded state, receiving submissions while simultaneously recovering lost
    projects/submissions via to-the-minute point-in-time recovery (PITR).
-   Users found to abuse the use of their accounts by overburdening the
    KoboToolbox Server may be suspended or their account may be restricted.
