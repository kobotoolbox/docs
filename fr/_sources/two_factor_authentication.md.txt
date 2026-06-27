# Configuration de l'authentification à deux facteurs dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/two_factor_authentication.md" class="reference">23 Apr 2026</a>


<iframe src="https://www.youtube.com/embed/4BhF0eva_d4?si=Ha6XbjiSjfPEL-CX&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br>

KoboToolbox propose l'**authentification à deux facteurs (2FA)** pour renforcer la sécurité des comptes. Avec la 2FA, vous devrez saisir votre mot de passe ainsi qu'un code généré par une application sur votre smartphone pour accéder à votre compte KoboToolbox.

La 2FA réduit les risques liés à un mot de passe compromis. Même si votre mot de passe est piraté, hameçonné ou deviné, la 2FA empêche tout accès non autorisé à votre compte en ajoutant une couche de sécurité supplémentaire au-delà de l'**authentification à facteur unique (SFA)**.

<p class="note">
    <strong>Note :</strong> Une application d'authentification compatible sur votre appareil mobile est requise pour configurer la 2FA sur votre compte KoboToolbox. Cet article utilise Google Authenticator, disponible sur le <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2">Google Play Store</a> et l'<a href="https://apps.apple.com/fr/app/google-authenticator/id388497605?l=en-GB">Apple App Store</a>, mais d'autres applications d'authentification peuvent également fonctionner.
</p>

Cet article couvre les sujets suivants :

- Configurer la 2FA avec un code QR ou une clé manuelle
- Désactiver et reconfigurer la 2FA
- Utiliser KoboCollect lorsque la 2FA est activée

## Configurer la 2FA dans KoboToolbox

La 2FA dans KoboToolbox peut être configurée selon deux approches différentes : l'approche par **code QR** et l'approche par **clé manuelle**. Pour commencer avec l'une ou l'autre de ces approches :

1. Connectez-vous à votre compte KoboToolbox.
2. Cliquez sur l'icône de votre profil en haut à droite.
3. Sélectionnez **COMPTE**.
4. Accédez à l'onglet **Sécurité**.
5. Dans la section **Authentification à deux facteurs**, activez la 2FA en basculant le bouton **Désactivé**.
6. Ouvrez votre application d'authentification et suivez les étapes correspondant à l'une des deux approches ci-dessous.

### Configurer la 2FA avec un code QR

La première méthode est l'approche par **code QR**, qui utilise l'appareil photo de votre appareil pour scanner un code QR afin de configurer la 2FA pour votre compte.

<p class="note">
  <b>Note :</b> Les étapes ci-dessous décrivent le processus avec l'application Google Authenticator. Le processus devrait être similaire avec d'autres applications d'authentification, mais il peut y avoir quelques différences.
</p>

Pour configurer la 2FA avec un code QR :

1. Ouvrez votre application d'authentification et appuyez sur **Get started**.
2. Sélectionnez **Scan a QR code**. L'appareil photo de votre appareil devrait maintenant être actif.
3. Scannez le code QR visible sur votre écran.
4. Saisissez le code PIN à 6 chiffres de l'application d'authentification dans votre compte KoboToolbox pour configurer la 2FA, puis appuyez sur **Next**.
5. Des codes de récupération s'afficheront pour vous aider à accéder à votre compte si votre application d'authentification ne fonctionne plus. Téléchargez les codes en sélectionnant **Codes de téléchargement** et conservez-les en lieu sûr.
6. Continuez en sélectionnant **J'ai enregistré mes codes**.

Vous avez maintenant configuré avec succès la 2FA dans votre compte KoboToolbox via l'**approche par code QR**.

### Configurer la 2FA avec une clé manuelle

La deuxième approche est l'**approche par clé manuelle**, qui ne nécessite pas l'appareil photo de votre appareil pour configurer la 2FA sur votre compte KoboToolbox.

Pour configurer la 2FA avec une clé manuelle :

1. En bas de la fenêtre 2FA dans KoboToolbox, cliquez sur **Pas de code QR ? Saisir la clé manuellement**. Une clé de 32 caractères s'affichera.
2. Ouvrez votre application d'authentification et appuyez sur **Get started**.
3. Sélectionnez **Enter a setup key**.
4. Saisissez le nom du compte (par exemple, « KoboToolbox ») et la clé de 32 caractères dans l'application, puis appuyez sur **Add**.
5. Saisissez le code PIN à 6 chiffres de votre application d'authentification dans votre compte KoboToolbox pour configurer la 2FA, puis appuyez sur **Next**.
6. Des codes de récupération s'afficheront pour vous aider à accéder à votre compte si votre application d'authentification ne fonctionne plus. **Téléchargez les codes** en sélectionnant Codes de téléchargement et conservez-les en lieu sûr.
7. Continuez en sélectionnant **J'ai enregistré mes codes**.

Vous avez maintenant configuré avec succès la 2FA dans votre compte KoboToolbox via l'**approche par clé manuelle**.

## Désactiver la 2FA

Pour désactiver la 2FA de votre compte KoboToolbox :

1. Cliquez sur l'icône de votre profil dans le coin supérieur droit.
2. Sélectionnez **COMPTE**.
3. Accédez à l'onglet **Sécurité**.
4. Dans la section **Authentification à deux facteurs**, désactivez la 2FA en basculant le bouton **Activé**.
5. Ouvrez l'application d'authentification sur votre smartphone, récupérez le code à 6 chiffres et saisissez-le. Appuyez sur **Next**.
6. Après avoir saisi le code à 6 chiffres, le système désactivera la 2FA de votre compte.

![image](/images/two_factor_authentication/Deactivate_2FA.png)

## Reconfigurer la 2FA

Pour reconfigurer la 2FA pour votre compte KoboToolbox (par exemple, pour configurer un nouveau smartphone) :

1. Cliquez sur l'icône de votre profil dans le coin supérieur droit.
2. Sélectionnez **COMPTE**.
3. Accédez à l'onglet **Sécurité**.
4. Dans la section **Authentification à deux facteurs**, à côté de **Application d'authentification**, appuyez sur le bouton **Reconfigurer** pour commencer à reconfigurer la 2FA. Ce processus suit les mêmes étapes que la configuration initiale de la 2FA.

Lorsque vous reconfigurez la 2FA pour votre compte, la configuration précédente est automatiquement supprimée. Les jetons ou codes de récupération de l'ancienne configuration ne seront plus valides. Une fois votre 2FA actuelle désactivée, vous serez invité à la reconfigurer. Si vous ne pouvez pas terminer le processus, la 2FA restera désactivée pour votre compte. Dans ce cas, vous pouvez la réactiver à tout moment en suivant la procédure habituelle décrite ci-dessus.

## Utiliser KoboCollect avec la 2FA

L'authentification à deux facteurs ajoute une couche de protection aux comptes contenant des données sensibles. L'utilisation de ces comptes pour la collecte de données pourrait présenter des risques importants. Par conséquent, lorsque vous activez la 2FA pour votre compte, vous ne pouvez plus télécharger des formulaires ni soumettre des données vers [KoboCollect](../fr/data_collection_kobocollect.md) depuis ce compte. Vous recevrez un message d'erreur lorsque vous tenterez de télécharger de nouveaux formulaires dans l'application, tel que "Server Requires Authentication: Invalid username or password for server."

Pour collecter des données avec KoboCollect lorsque la 2FA est active, nous recommandons l'une des approches suivantes :

1. Créez un compte KoboToolbox distinct pour la collecte de données et les tests de formulaires à utiliser avec KoboCollect. Partagez votre ou vos formulaires avec ce nouveau compte et limitez ses [droits d'accès](../fr/managing_permissions.md) à **Ajouter des soumissions** pour une sécurité maximale.
2. [Activez](../fr/project_sharing_settings.md#allowing-submissions-without-authentication) l'option « Autoriser les soumissions sans nom d'utilisateur ni mot de passe pour ce formulaire » pour vos formulaires, et [connectez-vous à KoboCollect](../fr/kobocollect_on_android_latest.md) en utilisant les identifiants suivants :
    - **URL** : `https://[kobocollect_url]/[username]`
- **Nom d'utilisateur** : (vide)
    - **Mot de passe** : (vide)

La deuxième approche permet aux utilisateurs de télécharger et de soumettre des données vers tous les formulaires partagés avec `username` qui ne [requièrent pas d'authentification](../fr/project_sharing_settings.md#allowing-submissions-without-authentication).

## Résolution de problèmes
<details>
<summary><b>Générer de nouveaux codes de récupération</b></summary>
Si vous avez égaré vos codes de récupération ou pensez qu'ils ont été compromis, vous pouvez générer de nouveaux codes de récupération pour la 2FA en appuyant sur le bouton <b>Générer de nouveau</b> à côté de <b>Codes de récupération</b>.
</details>

<br>

<details>
<summary><b>Impossible d'accéder à votre compte KoboToolbox</b></summary>
Si vous ne pouvez pas accéder à votre compte KoboToolbox avec la 2FA activée (par exemple, si vous avez réinitialisé votre smartphone et désinstallé l'application d'authentification, ou si vous avez égaré vos codes de récupération), vous pouvez contacter <a class="reference external" href="support@kobotoolbox.org">support@kobotoolbox.org</a>. Veuillez utiliser l'adresse email associée à votre compte pour demander la désactivation de la 2FA.
</details>