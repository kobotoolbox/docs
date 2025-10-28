# Setting up two-factor authentication in KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/050dcc9c8bfb4c528208bbe886979999037f1554/source/two_factor_authentication.md" class="reference">28 Oct 2025</a>

<br>

KoboToolbox supports **Two-Factor Authentication (2FA)** to improve account security. With 2FA, you will need to enter your account password and a code from a smartphone app to access your KoboToolbox account.

2FA minimizes the risks of a compromised password. Even if your password is hacked, phished, or guessed, 2FA prevents unauthorized access to your account by adding an additional layer of security beyond **Single-Factor Authentication (SFA)**.

<p class="note">
    <strong>Note:</strong> A compatible authenticator app on your mobile device is required to set up 2FA for your KoboToolbox account. This article uses Google Authenticator, available on the <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2">Google Play Store</a> and <a href="https://apps.apple.com/fr/app/google-authenticator/id388497605?l=en-GB">Apple App Store</a>, but other authenticator apps can also work.
</p>

This article covers the following topics:

- Setting up 2FA with a QR code or manual key
- Disabling and reconfiguring 2FA
- Using KoboCollect when 2FA is enabled

## Setting up 2FA in KoboToolbox

2FA in KoboToolbox can be configured using two different approaches: the **QR code** approach and the **manual key** approach. To get started with either approach:

1. Log in to your KoboToolbox account.
2. Click your profile icon in the top right corner.
3. Select **ACCOUNT SETTINGS**.
4. Go to the **Security** tab.
5. In the **Two-factor authentication section**, enable 2FA by toggling the **Disabled** button.
6. Open your authenticator app and follow the steps for one of the two approaches below.

### Setting up 2FA with a QR code

The first method is the **QR code** approach, which uses your device's camera to scan a QR code to configure 2FA for your account. 

<p class="note">
  <b>Note:</b> The steps below describe the process using the Google Authenticator app. The process should be similar with other authenticator apps, but there may be some differences.
</p>

To set up 2FA with a QR code:

1. Open your authenticator app and press **Get started**.
2. Select **Scan a QR code**. Your device’s camera should now be active.
3. Scan the QR code visible on your monitor.
4. Enter the 6-digit PIN from the authenticator app into your KoboToolbox account to configure 2FA, then press **Next**.
5. Recovery codes will be displayed to help you access your account if your authenticator app fails. Download the codes by selecting **Download codes** and store them in a safe place.
6. Proceed by selecting **I saved my codes**.

You have now successfully configured 2FA in your KoboToolbox account via the **QR code approach**. 

### Setting up 2FA with a manual key

The second approach is the **manual key approach**, which does not require your device’s camera to configure 2FA for your KoboToolbox account.

To set up 2FA with a manual key:

1. At the bottom of the 2FA window in KoboToolbox, click **No QR code? Enter key manually**. A 32-character key will be displayed.
2. Open your authenticator app and press **Get started**.
3. Select **Enter a setup key**.
4. Enter the Account name (e.g., "KoboToolbox") and the 32-character key in the app, then press **Add**. 
5. Enter the 6-digit PIN from your authenticator app into your KoboToolbox account to configure 2FA, then press **Next**.
6. Recovery codes will be displayed to help you access your account if your authenticator app fails. **Download the codes** by selecting Download codes and store them in a safe place.
7. Proceed by selecting **I saved my codes**.

You have now successfully configured 2FA in your KoboToolbox account via the **manual key approach**.

## Disabling 2FA

To disable 2FA from your KoboToolbox account:

1. Click your profile icon in the top right corner.
2. Select **ACCOUNT SETTINGS**.
3. Go to the **Security** tab.
4. In the **Two-factor authentication section**, disable 2FA by toggling the **Enabled** button.
5. Open the authenticator app on your smartphone, get the 6-digit code, and enter it. Press **Next**.
6. After entering the 6-digit code, the system will disable 2FA from your account. 

![image](/images/two_factor_authentication/Deactivate_2FA.png) 

## Reconfiguring 2FA

To reconfigure 2FA for your KoboToolbox account (e.g., to configure a new smartphone):

1. Click your profile icon in the top right corner.
2. Select **ACCOUNT SETTINGS**.
3. Go to the **Security tab**.
4. In the **Two-factor authentication section**, next to **Authenticator app**, press the **Reconfigure** button to begin reconfiguring 2FA. This process follows the same steps as setting up 2FA.
   
When you reconfigure 2FA for your account, the previous setup will be automatically deleted. Any tokens or recovery codes from the old setup will no longer be valid. After your current 2FA has been deactivated, you will be prompted to configure it again. If you cannot complete the process, 2FA will remain disabled for your account. In this case, you can enable it again at any time through the usual process, as shared above.

## Using KoboCollect with 2FA

Two-factor authentication adds a layer of protection to accounts with sensitive data. Using these accounts for data collection could pose significant risks. Therefore, when activating 2FA for your account, you can no longer download forms or submit data to [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) from this account. You will receive an error message when attempting to download new forms inside the app, such as “Server Requires Authentication: Invalid username or password for server.” 

To collect data with KoboCollect when 2FA is active, we recommend either of the following approaches:

1. Create a separate KoboToolbox account for data collection and form testing to use with KoboCollect. Share your form(s) with this new account and restrict its [permissions](https://support.kobotoolbox.org/managing_permissions.html) to **Add submissions** for maximum security.
2. [Enable](https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication) “Allow submissions to this form without a username and password” for your forms, and [connect to KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) using the following credentials:
    - **URL**: `https://[kobocollect_url]/[username]` 
    - **Username**: (blank)
    - **Password**: (blank)

The second approach allows users to download and submit data to any forms shared with `username` that do not [require authentication](https://support.kobotoolbox.org/project_sharing_settings.html#allowing-submissions-without-authentication).

## Troubleshooting
<details>
<summary><b>Generating new recovery codes</b></summary>
If you have misplaced your recovery codes or believe they have been compromised, you can generate new recovery codes for 2FA by pressing the <b>Generate new</b> button next to <b>Recovery codes</b>.
</details>

<br>

<details>
<summary><b>Unable to access KoboToolbox account</b></summary>
If you are unable to access your KoboToolbox account with 2FA enabled (for example, if you reset your smartphone and uninstalled the authenticator app, or you misplaced your recovery codes), you can contact <a class="reference external" href="support@kobotoolbox.org">support@kobotoolbox.org</a>. Please use the email address registered to your account to request that 2FA be disabled.
</details>

<br>

<details>
<summary><b>Feature not available</b></summary>
This feature is currently unavailable for users on the Community Plan. However, 2FA will be extended to all users in the coming months, regardless of their plan.
</details>
