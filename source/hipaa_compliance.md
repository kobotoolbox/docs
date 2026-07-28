# Compliance with HIPAA
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/713766f1e5111103d023ea41c43d44fac7c1a23d/source/hipaa_compliance.md" class="reference">28 Jul 2026</a>

The Health Insurance Portability and Accountability Act (HIPAA) is a United States law that establishes requirements for protecting certain health information. HIPAA may apply to covered entities, business associates, and other organizations that handle protected health information (PHI). PHI can include information about a person’s health, healthcare, or payment for healthcare.

This article explains the limitations of using KoboToolbox for projects that are subject to HIPAA.

## Public KoboToolbox servers

The public KoboToolbox servers are not designed to meet the specific requirements of HIPAA. While KoboToolbox includes security features such as [account permissions](https://support.kobotoolbox.org/managing_permissions.html), [two-factor authentication](https://support.kobotoolbox.org/two_factor_authentication.html), [activity logs](https://support.kobotoolbox.org/activity_logs.html), and [form encryption](https://support.kobotoolbox.org/encrypting_forms.html), these measures alone do not make the public servers HIPAA-compliant.

Organizations should not collect, store, or process PHI on the public KoboToolbox servers when HIPAA compliance is required.

## Private KoboToolbox deployments

Organizations that need to use KoboToolbox for a HIPAA-regulated project can consider operating a [private KoboToolbox deployment](https://github.com/kobotoolbox/kobo-install) with a hosting provider that supports HIPAA compliance.

A private deployment is not automatically HIPAA-compliant. The organization is responsible for ensuring that the hosting environment, KoboToolbox configuration, policies, procedures, agreements, and day-to-day operations meet all applicable requirements.

Organizations may also need to enter into business associate agreements with hosting providers and other service providers that create, receive, maintain, or transmit electronic PHI.

Before using KoboToolbox to collect health information, consult your organization’s privacy, security, or legal team to determine whether HIPAA applies and what safeguards are required.
