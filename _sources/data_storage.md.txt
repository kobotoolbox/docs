# Data storage
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/b4ed8a99e3db91d492b738ad646871307544f13c/source/data_storage.md" class="reference">6 Nov 2026</a>

KoboToolbox securely stores project data using Amazon Web Services (AWS). Your data is stored in different locations depending on the server you selected when [creating your account](https://support.kobotoolbox.org/creating_account.html#choosing-the-right-server):

| KoboToolbox server                | Data storage location |
| --------------------------------- | --------------------- |
| Global KoboToolbox Server         | United States         |
| European Union KoboToolbox Server | Ireland and Germany   |

Both servers offer the same KoboToolbox features. However, projects and data cannot be transferred or shared between the Global and European Union servers. To collaborate on a project, users must have accounts on the same server.

## What is stored

KoboToolbox stores two main types of project data:
* **Form and submission data,** such as questions and responses, are stored in an AWS database.
* **Files and media submitted by respondents,** such as images, audio recordings, videos, and documents, are stored in Amazon Simple Storage Service (Amazon S3).

Your project data remains stored in KoboToolbox until you delete it. Deleted submissions are **permanently removed** immediately, while deleted projects, accounts, and attachments are retained for up to 30 days before being permanently removed.

<p class="note">
  <strong>Note:</strong> According to KoboToolbox’s Terms of Service, an account is considered inactive if no activity has been recorded for two consecutive years. Under the <a href="https://www.kobotoolbox.org/legal/inactive-accounts/">Inactive Accounts Policy</a>, Kobo reserves the right to delete inactive accounts and all associated projects and data.
</p>

## File storage limits

Your file storage limit depends on your [KoboToolbox plan](https://www.kobotoolbox.org/pricing/):

| Plan              | File storage |
| ----------------- | ------------ |
| Community Plan    | 1 GB         |
| Professional Plan | Unlimited    |
| Teams Plan        | Unlimited    |
| Enterprise Plan   | Unlimited    |

Only **files and media submitted by respondents** count toward your plan’s file storage limit. Files and media attached to a form during form development do not count toward this limit.

You can review your current file storage use and plan limits from the **Usage** page in your [account settings](https://support.kobotoolbox.org/account_settings.html#usage). 

<p class="note">
  <strong>Note:</strong> If your account remains over its <a href="https://support.kobotoolbox.org/account_usage_limits.html">file storage limit</a> for more than 90 days, KoboToolbox will begin deleting media attachments, starting with the oldest files. Submission data will never be deleted.
</p>

To manage your storage use, you can either:
* [Analyse](https://support.kobotoolbox.org/qualitative_analysis.html), [download](https://support.kobotoolbox.org/managing_media_responses.html#downloading-media-files), and [delete](https://support.kobotoolbox.org/managing_media_responses.html#deleting-media-files) media files that you no longer need. 
* Purchase [additional file storage](https://support.kobotoolbox.org/account_settings.html#add-ons) from the **Add-ons** page in your account settings.
* Upgrade to a [paid KoboToolbox plan](https://www.kobotoolbox.org/pricing/).

<p class="note">
  To learn more about monitoring and managing your KoboToolbox file storage, see <a href="https://support.kobotoolbox.org/account_usage_limits.html">Managing account usage limits</a>.
</p>

## Private servers

For organizations with advanced data residency or infrastructure requirements, KoboToolbox also offers [private server deployments](https://www.kobotoolbox.org/enterprise/). These allow you to choose where your data is stored and managed.

Private servers provide the same core KoboToolbox functionality while giving organizations full control over hosting location, compliance requirements, and infrastructure management. Data can be hosted in **28 supported countries** or within your own infrastructure **anywhere in the world.**


