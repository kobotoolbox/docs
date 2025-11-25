# Configuration de l'authentification à deux facteurs dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/3c86f234242bee25d3d6f91bffee5cb93d808344/source/two_factor_authentication.md" class="reference">5 septembre 2025</a>

<iframe src="https://www.youtube.com/embed/4BhF0eva_d4?si=Ha6XbjiSjfPEL-CX" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br>

KoboToolbox prend en charge **l'authentification à deux facteurs (2FA)** pour améliorer la sécurité des comptes. Avec la 2FA, vous devrez saisir le mot de passe de votre compte et un code provenant d'une application pour smartphone pour accéder à votre compte KoboToolbox.

La 2FA minimise les risques liés à un mot de passe compromis. Même si votre mot de passe est piraté, hameçonné ou deviné, la 2FA empêche l'accès non autorisé à votre compte en ajoutant une couche de sécurité supplémentaire au-delà de **l'authentification à facteur unique (SFA)**.

<p class="note">
    <strong>Remarque :</strong> Une application d'authentification compatible sur votre appareil mobile est nécessaire pour configurer la 2FA pour votre compte KoboToolbox. Cet article utilise Google Authenticator, disponible sur le <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2">Google Play Store</a> et l'<a href="https://apps.apple.com/fr/app/google-authenticator/id388497605?l=en-GB">Apple App Store</a>, mais d'autres applications d'authentification peuvent également fonctionner.
</p>

Cet article couvre les sujets suivants :

- Configuration de la 2FA avec un code QR ou une clé manuelle
- Désactivation et reconfiguration de la 2FA
- Utilisation de KoboCollect lorsque la 2FA est activée

## Configuration de la 2FA dans KoboToolbox

La 2FA dans KoboToolbox peut être configurée selon deux approches différentes : l'approche par **code QR** et l'approche par **clé manuelle**. Pour commencer avec l'une ou l'autre approche :

1. Connectez-vous à votre compte KoboToolbox.
2. Cliquez sur votre icône de profil dans le coin supérieur droit.
3. Sélectionnez **PARAMÈTRES DU COMPTE**.
4. Accédez à l'onglet **Sécurité**.
5. Dans la section **Authentification à deux facteurs**, activez la 2FA en basculant le bouton **Désactivé**.
6. Ouvrez votre application d'authentification et suivez les étapes de l'une des deux approches ci-dessous.

### Configuration de la 2FA avec un code QR

La première méthode est l'approche par **code QR**, qui utilise l'appareil photo de votre appareil pour scanner un code QR afin de configurer la 2FA pour votre compte.

<p class="note">
  <b>Remarque :</b> Les étapes ci-dessous décrivent le processus en utilisant l'application Google Authenticator. Le processus devrait être similaire avec d'autres applications d'authentification, mais il peut y avoir quelques différences.
</p>

Pour configurer la 2FA avec un code QR :

1. Ouvrez votre application d'authentification et appuyez sur **Commencer**.
2. Sélectionnez **Scanner un code QR**. L'appareil photo de votre appareil devrait maintenant être actif.
3. Scannez le code QR visible sur votre écran.
4. Saisissez le code PIN à 6 chiffres de l'application d'authentification dans votre compte KoboToolbox pour configurer la 2FA, puis appuyez sur **Suivant**.
5. Des codes de récupération seront affichés pour vous aider à accéder à votre compte si votre application d'authentification échoue. Téléchargez les codes en sélectionnant **Télécharger les codes** et conservez-les dans un endroit sûr.
6. Continuez en sélectionnant **J'ai enregistré mes codes**.

Vous avez maintenant configuré avec succès la 2FA dans votre compte KoboToolbox via l'**approche par code QR**.

### Configuration de la 2FA avec une clé manuelle

La deuxième approche est l'**approche par clé manuelle**, qui ne nécessite pas l'appareil photo de votre appareil pour configurer la 2FA pour votre compte KoboToolbox.

Pour configurer la 2FA avec une clé manuelle :

1. En bas de la fenêtre 2FA dans KoboToolbox, cliquez sur **Pas de code QR ? Saisir la clé manuellement**. Une clé de 32 caractères sera affichée.
2. Ouvrez votre application d'authentification et appuyez sur **Commencer**.
3. Sélectionnez **Saisir une clé de configuration**.
4. Saisissez le nom du compte (par exemple, « KoboToolbox ») et la clé de 32 caractères dans l'application, puis appuyez sur **Ajouter**.
5. Saisissez le code PIN à 6 chiffres de votre application d'authentification dans votre compte KoboToolbox pour configurer la 2FA, puis appuyez sur **Suivant**.
6. Des codes de récupération seront affichés pour vous aider à accéder à votre compte si votre application d'authentification échoue. **Téléchargez les codes** en sélectionnant Télécharger les codes et conservez-les dans un endroit sûr.
7. Continuez en sélectionnant **J'ai enregistré mes codes**.

Vous avez maintenant configuré avec succès la 2FA dans votre compte KoboToolbox via l'**approche par clé manuelle**.

## Désactivation de la 2FA

Pour désactiver la 2FA de votre compte KoboToolbox :

1. Cliquez sur votre icône de profil dans le coin supérieur droit.
2. Sélectionnez **PARAMÈTRES DU COMPTE**.
3. Accédez à l'onglet **Sécurité**.
4. Dans la section **Authentification à deux facteurs**, désactivez la 2FA en basculant le bouton **Activé**.
5. Ouvrez l'application d'authentification sur votre smartphone, obtenez le code à 6 chiffres et saisissez-le. Appuyez sur **Suivant**.
6. Après avoir saisi le code à 6 chiffres, le système désactivera la 2FA de votre compte.

![image](/images/two_factor_authentication/Deactivate_2FA.png)

## Reconfiguration de la 2FA

Pour reconfigurer la 2FA pour votre compte KoboToolbox (par exemple, pour configurer un nouveau smartphone) :

1. Cliquez sur votre icône de profil dans le coin supérieur droit.
2. Sélectionnez **PARAMÈTRES DU COMPTE**.
3. Accédez à l'onglet **Sécurité**.
4. Dans la section **Authentification à deux facteurs**, à côté d'**Application d'authentification**, appuyez sur le bouton **Reconfigurer** pour commencer à reconfigurer la 2FA. Ce processus suit les mêmes étapes que la configuration de la 2FA.

Lorsque vous reconfigurez la 2FA pour votre compte, la configuration précédente sera automatiquement supprimée. Tous les jetons ou codes de récupération de l'ancienne configuration ne seront plus valides. Après la désactivation de votre 2FA actuelle, vous serez invité à la configurer à nouveau. Si vous ne pouvez pas terminer le processus, la 2FA restera désactivée pour votre compte. Dans ce cas, vous pouvez l'activer à nouveau à tout moment via le processus habituel, comme indiqué ci-dessus.

## Utilisation de KoboCollect avec la 2FA

L'authentification à deux facteurs ajoute une couche de protection aux comptes contenant des données sensibles. L'utilisation de ces comptes pour la collecte de données pourrait poser des risques importants. Par conséquent, lors de l'activation de la 2FA pour votre compte, vous ne pouvez plus télécharger de formulaires ni soumettre de données à [KoboCollect](kobocollect_on_android_latest.md) depuis ce compte. Vous recevrez un message d'erreur lors de la tentative de téléchargement de nouveaux formulaires dans l'application, tel que « Le serveur nécessite une authentification : Nom d'utilisateur ou mot de passe invalide pour le serveur. »

Pour collecter des données avec KoboCollect lorsque la 2FA est active, nous recommandons l'une des approches suivantes :

1. Créez un compte KoboToolbox distinct pour la collecte de données et les tests de formulaires à utiliser avec KoboCollect. Partagez votre ou vos formulaires avec ce nouveau compte et limitez ses [permissions](managing_permissions.md) à **Ajouter des soumissions** pour une sécurité maximale.
2. [Activez](https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication) « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe » pour vos formulaires, et [connectez-vous à KoboCollect](kobocollect_on_android_latest.md) en utilisant les identifiants suivants :
    - **URL** : `https://[kobocollect_url]/[username]`
    - **Nom d'utilisateur** : (vide)
    - **Mot de passe** : (vide)

La deuxième approche permet aux utilisatrices et utilisateurs de télécharger et de soumettre des données à tous les formulaires partagés avec `username` qui ne [nécessitent pas d'authentification](https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication).

## Dépannage
<details>
<summary><b>Génération de nouveaux codes de récupération</b></summary>
Si vous avez égaré vos codes de récupération ou pensez qu'ils ont été compromis, vous pouvez générer de nouveaux codes de récupération pour la 2FA en appuyant sur le bouton <b>Générer de nouveaux</b> à côté de <b>Codes de récupération</b>.
</details>

<br>

<details>
<summary><b>Impossible d'accéder au compte KoboToolbox</b></summary>
Si vous ne parvenez pas à accéder à votre compte KoboToolbox avec la 2FA activée (par exemple, si vous avez réinitialisé votre smartphone et désinstallé l'application d'authentification, ou si vous avez égaré vos codes de récupération), vous pouvez contacter <a class="reference external" href="support@kobotoolbox.org">support@kobotoolbox.org</a>. Veuillez utiliser l'adresse e-mail enregistrée sur votre compte pour demander la désactivation de la 2FA.
</details>

<br>

<details>
<summary><b>Fonctionnalité non disponible</b></summary>
Cette fonctionnalité est actuellement indisponible pour les utilisatrices et utilisateurs du plan Community. Cependant, la 2FA sera étendue à toutes les utilisatrices et tous les utilisateurs dans les prochains mois, quel que soit leur plan.
</details>