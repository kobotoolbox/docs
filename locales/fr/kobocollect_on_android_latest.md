# Premiers pas avec KoboCollect
<a href="../kobocollect_on_android_latest.html">Read in English</a> | <a href="../es/kobocollect_on_android_latest.html">Leer en español</a> | <a href="../ar/kobocollect_on_android_latest.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/562abda7896f1c80c1863f158d61432fa915a52f/source/kobocollect_on_android_latest.md" class="reference">19 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/qC2Bz8jZkIM?si=xSyTOxOMR6nE8tum" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect est une application KoboToolbox gratuite et open source conçue pour la collecte de données sur les appareils mobiles Android. Ses capacités hors ligne et sa compatibilité avec la plupart des appareils Android la rendent idéale pour le travail de terrain.

Avant d'utiliser KoboCollect, vous devez [créer un compte KoboToolbox](creating_account.md) sur le site web KoboToolbox et [déployer des formulaires de collecte de données](https://support.kobotoolbox.org/fr/quick_start.html).

<p class="note">
    Cet article explique comment se connecter à KoboCollect pour la collecte de données. Pour en savoir plus sur la configuration des paramètres de KoboCollect et la collecte de données avec l'application, consultez <a href="kobocollect_settings.html">Personnalisation des paramètres de KoboCollect</a> et <a href="data_collection_kobocollect.html">Collecte de données avec KoboCollect</a>.
</p>

## Installation de l'application KoboCollect

L'application KoboCollect peut être téléchargée depuis le [Google Play Store](https://play.google.com/store/apps/details?id=org.koboc.collect.android) pour les appareils Android fonctionnant sous la version 5 ou supérieure.

<p class="note">
    <strong>Remarque :</strong> Nous vous recommandons d'utiliser la dernière version de l'application (v2025.2), car elle inclut des fonctionnalités et des corrections de bugs non disponibles dans les versions antérieures.
</p>

## Configuration de l'application KoboCollect

Pour collecter des données avec KoboCollect, vous devez configurer l'application KoboCollect sur votre appareil mobile pour vous connecter au serveur KoboToolbox. Cela vous permet de télécharger les formulaires déployés depuis KoboToolbox et d'envoyer les données collectées vers le serveur.

Pour connecter KoboCollect au serveur KoboToolbox, vous aurez besoin de votre **URL KoboCollect**, de votre **nom d'utilisateur** et de votre **mot de passe**. Après la configuration manuelle initiale, vous pouvez [générer un code QR](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) pour configurer d'autres appareils.

<p class="note">
    <strong>Remarque :</strong> Dans l'application KoboCollect, les comptes utilisateurs sont appelés <strong>Projets</strong>.
</p>

### Configuration manuelle de KoboCollect
Pour configurer manuellement KoboCollect, vous devrez identifier votre **URL KoboCollect**. Cette URL est spécifique à KoboCollect et diffère de l'URL utilisée pour accéder à votre compte KoboToolbox.

Votre URL KoboCollect dépend du serveur de votre compte :

| **Serveur KoboToolbox**    | **URL KoboCollect**                     |
| :----------------- | :--------------------------------------------- |
| Le serveur KoboToolbox mondial               | https://kc.kobotoolbox.org/ |
| Le serveur KoboToolbox Union européenne      | https://kc-eu.kobotoolbox.org/ |
| Serveur privé           | Unique à chaque organisation            |

Vous pouvez également trouver l'URL KoboCollect sur la plateforme KoboToolbox. Accédez à l'onglet **FORMULAIRE** de votre projet et sélectionnez **Application Android** dans le menu déroulant **Collecter des données**. L'URL KoboCollect sera indiquée à l'étape 3.

![Select Android app in browser](images/kobocollect_on_android_latest/select_android_app_in_browser.png)

Une fois que vous avez identifié votre URL KoboCollect, suivez ces étapes pour configurer la connexion au serveur :

1. Ouvrez l'application KoboCollect.
2. Sélectionnez **Saisir les détails du projet**.
3. Saisissez l'**URL KoboCollect**, votre **nom d'utilisateur** et votre **mot de passe**.
4. Appuyez sur **Ajouter**.
5. Lorsque la configuration est terminée, le menu principal s'affiche.

### Configuration de KoboCollect avec un code QR

L'utilisation d'un code QR permet de configurer efficacement KoboCollect sur plusieurs appareils avec les **mêmes paramètres de serveur** (URL KoboCollect, nom d'utilisateur, mot de passe et <a href="kobocollect_settings.html">paramètres de configuration du projet</a>). Cela peut être utile pour éviter de répéter les étapes manuelles ou pour configurer les appareils des enquêteurs sans partager les mots de passe du compte.

<p class="note">
    <strong>Remarque :</strong> Pour utiliser la méthode du code QR, vous devez d'abord configurer manuellement un appareil, puis copier le code QR généré sur les autres appareils.
</p>

Pour accéder à votre code QR :

1. Accédez au menu **Projets** et sélectionnez le projet que vous souhaitez copier.
2. Appuyez sur **Paramètres**.
3. Sélectionnez **Gestion du projet**.
4. Appuyez sur **Reconfigurer avec un code QR**.
5. Choisissez **Code QR**. Votre code QR apparaîtra à l'écran.
6. **Prenez une capture d'écran** du code QR pour le partager afin de configurer d'autres appareils. Vous pouvez également revenir à ce menu à tout moment pour accéder à nouveau au code QR.

Pour configurer d'autres appareils à l'aide du code QR :

1. Ouvrez **KoboCollect** sur l'appareil que vous souhaitez configurer.
2. Appuyez sur **Configurer avec un code QR**.
3. Scannez un code QR avec l'appareil photo de l'appareil, ou appuyez sur les <i class="k-icon-more"></i> **trois points** dans le coin supérieur droit et sélectionnez **Importer un code QR** pour utiliser une capture d'écran enregistrée sur votre appareil.

Si la configuration réussit, l'application sera configurée automatiquement.

<p class="note">
    <strong>Remarque :</strong> Le code QR contient vos identifiants de compte, y compris votre mot de passe. Toute personne qui le scanne aura les mêmes autorisations d'accès que le compte à partir duquel il a été généré. Si vous souhaitez uniquement que quelqu'un collecte des données (par exemple, un enquêteur), <strong>assurez-vous que le compte utilisé pour générer le code QR n'a pas les autorisations de consulter, modifier ou supprimer des données.</strong> Pour protéger vos données, évitez de partager des codes QR provenant de comptes disposant d'un accès complet.
</p>

### Configuration de plusieurs projets dans KoboCollect

Les utilisatrices et utilisateurs peuvent connecter plusieurs comptes KoboToolbox et basculer facilement entre différents projets au sein de la même application KoboCollect, qu'ils se trouvent sur le même serveur ou sur des serveurs différents.

Pour configurer des projets supplémentaires dans KoboCollect :

1. Appuyez sur l'**icône Projet** située dans le coin supérieur droit.
2. Dans le menu **Projets**, appuyez sur **Ajouter un projet**.
3. Configurez un nouveau projet en utilisant l'approche manuelle ou en scannant un code QR.
4. Lorsque la configuration est terminée, le menu principal s'affiche.
5. Appuyez sur l'**icône Projet** pour ouvrir le menu. Les deux projets devraient maintenant être visibles.

Des projets supplémentaires peuvent être ajoutés en répétant le même processus. Le projet actif sera listé en premier dans le menu **Projets**. Pour basculer vers un autre projet, appuyez simplement sur son icône.

<p class="note">
    Pour en savoir plus sur la modification de l'affichage des projets pour faciliter leur reconnaissance et leur basculement, consultez <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#project-display-settings">Paramètres d'affichage du projet</a>.
</p>

### Configuration d'un projet dans KoboCollect sans authentification

Il est également possible d'accéder aux projets dans KoboCollect sans mot de passe. Cela est utile pour les projets avec de nombreux enquêteurs, car cela évite d'avoir à créer des comptes individuels ou à partager des identifiants.

<p class="note">
    <strong>Remarque :</strong> Cette approche nécessite d'activer « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe » pour vos formulaires. Pour en savoir plus sur les paramètres de partage au niveau du projet, consultez <a href="project_sharing_settings.html">Partage de projets avec des paramètres au niveau du projet</a>.
</p>

Pour vous connecter à KoboCollect sans authentification :
1. Activez « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe » pour vos formulaires.
2. [Facultatif] Créez un compte KoboToolbox dédié pour les collecteurs de données et [partagez vos formulaires](managing_permissions.md) avec ce compte.
3. Connectez-vous à KoboCollect en utilisant les identifiants suivants :
    - **URL** : URL KoboCollect suivie du nom d'utilisateur du compte (`https://[kobocollect_url]/[username]`)
    - **Nom d'utilisateur** : (Laisser vide)
    - **Mot de passe** : (Laisser vide)

Cette approche permet aux utilisatrices et utilisateurs de télécharger et de soumettre des données à tous les formulaires partagés avec `username` qui ne [nécessitent pas d'authentification](project_sharing_settings.md).

Pour différencier les enquêteurs et suivre les soumissions, vous pouvez demander aux enquêteurs de saisir un nom d'utilisateur personnalisé, un numéro de téléphone et une adresse e-mail dans les [Paramètres d'identité de l'utilisateur et de l'appareil](https://support.kobotoolbox.org/fr/kobocollect_settings.html#user-and-device-identity-settings).

<p class="note">
    <strong>Remarque :</strong> Cette approche peut être utile lorsque votre compte utilise l'<a href="two_factor_authentication.html">authentification à deux facteurs</a>, car vous ne pourrez pas télécharger de formulaires ni soumettre de données en utilisant l'approche normale.
</p>