# Personnaliser les paramètres KoboCollect
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/b2f0bf10348744a1576080786c7c44eff0dafa1c/source/kobocollect_settings.md" class="reference">24 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/Qeky3aomiWI?si=M1l_jorFQEDacX2A&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect est une application KoboToolbox gratuite et open source conçue pour la collecte de données sur les appareils mobiles Android. Avant de commencer, [installez et configurez](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html) l'application KoboCollect. Une fois installée et configurée, vous pouvez personnaliser l'application en fonction de votre projet ou des besoins des utilisateurs. Les paramètres du projet vous permettent de :

- Ajuster l'**interface utilisateur** (par exemple, la langue, la taille de la police, le thème)
- Configurer les **paramètres de carte** pour les questions basées sur la localisation
- Gérer la façon dont les formulaires sont traités (par exemple, envoi automatique, finalisation, règles de modification)
- Définir l'identité de l'**utilisateur et de l'appareil** pour le suivi des soumissions
- Protéger l'accès à l'application et à ses paramètres avec des **mots de passe ou des contrôles administrateur**

Pour accéder au menu des paramètres :

1. Appuyez sur l'**icône Projet** en haut à droite de votre écran.
2. Appuyez sur **Paramètres**.

<p class="note">
  <strong>Note :</strong> Les utilisateurs n'ont pas besoin d'une connexion Internet pour accéder aux paramètres du projet dans KoboCollect ou les modifier.
</p>

## Paramètres d'affichage du projet
Dans l'application KoboCollect, vous pouvez [vous connecter à plusieurs comptes KoboToolbox](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html#setting-up-multiple-projects-in-kobocollect). Les comptes utilisateurs sont appelés **Projets** dans KoboCollect.

Pour personnaliser l'affichage de chaque projet afin de faciliter sa reconnaissance et le passage d'un projet à l'autre, vous pouvez modifier les paramètres d'**affichage du projet**. Ces modifications n'affectent que la façon dont le projet apparaît dans l'interface de l'appareil et n'ont aucun effet sur les données ni sur les autres appareils.

| **Paramètre**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Nom du projet              | Donnez un nom distinct à votre projet KoboCollect.                                  |
| Icône du projet      | Modifiez la lettre qui apparaît dans le cercle en haut à droite.                                  |
| Couleur du projet           | Modifiez la couleur du cercle en haut à droite.            |

## Paramètres de l'interface utilisateur

Les paramètres de l'interface utilisateur vous permettent d'ajuster l'apparence de l'application, la langue et la taille du texte pour une meilleure lisibilité.

| **Paramètre**    | **Description** |
| :----------------- | :--------------------------------------------- |
| Thème  | Choisissez entre l'apparence claire, sombre ou celle par défaut du système pour l'application. |
| Langue      | Définissez la langue d'affichage de l'interface de l'application. Par défaut, KoboCollect utilise la langue de l'appareil.|
| Taille de la police           | Ajustez la taille du texte pour une meilleure lisibilité.            |
| Navigation           | Personnalisez la façon dont vous naviguez dans les formulaires. Choisissez entre les balayages horizontaux, les boutons suivant/précédent ou une disposition combinée. |


<p class="note">
    <strong>Note :</strong> La modification de la langue ne définit la langue que pour l'interface de l'application et non pour le formulaire. Pour les formulaires disponibles en <a href="https://support.kobotoolbox.org/fr/language_dashboard.html">plusieurs langues</a>, la langue du formulaire est définie lors de la saisie des données.
</p>

## Paramètres de carte

Les paramètres de carte configurent l'affichage et le comportement des cartes dans l'application pour les questions basées sur la localisation.

| **Paramètre**        | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Source   &emsp;&emsp;&emsp;&emsp;            | Définissez votre source de carte. Choisissez entre Google, OpenStreetMap, USGS ou Carto. |
| Style de carte      | Définissez le style de votre carte si vous utilisez Google Maps, USGS ou Carto. |
| Couche           | Sélectionnez une [couche hors ligne](https://docs.getodk.org/collect-offline-maps/) pour les cartes. Vous pouvez ajouter des options en sélectionnant un fichier MBTiles depuis votre appareil. |

## Paramètres de gestion des formulaires

Les paramètres de gestion des formulaires contrôlent la façon dont les formulaires sont traités dans l'application, notamment les mises à jour de versions, les soumissions et les comportements lors de la saisie des données.

| **Paramètre** | **Description**                  |
| :----------------- | :--------------------------------------------- |
| Mode de mise à jour des formulaires vierges &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Définissez si vous souhaitez que les nouvelles versions des formulaires soient mises à jour automatiquement ou manuellement. Les options disponibles sont : <ul><li><strong>Manuel</strong> : Le mode par défaut, dans lequel les enquêteurs gèrent manuellement la mise à jour des formulaires.</li><li><strong>Formulaires antérieurement téléchargés uniquement</strong> : Lorsqu'une mise à jour est disponible pour un ou plusieurs formulaires précédemment téléchargés sur l'appareil, ils sont soit mis à jour automatiquement (si le **Téléchargement automatique** est activé), soit les utilisateurs sont notifiés des mises à jour disponibles.</li><li><strong>Copie exacte du serveur</strong> : Tous les formulaires partagés avec le compte sont automatiquement téléchargés et mis à jour en fonction des modifications apportées au serveur.</li></ul> |
| Fréquence de mise à jour automatique      | Spécifie la fréquence à laquelle KoboCollect doit vérifier les mises à jour des formulaires sur le serveur lors de l'utilisation de **Formulaires antérieurement téléchargés uniquement** ou de **Copie exacte du serveur**. |
| Téléchargement automatique | Lorsque **Formulaires antérieurement téléchargés uniquement** est sélectionné, vous pouvez choisir si les formulaires sont mis à jour automatiquement. Sinon, les utilisateurs seront uniquement notifiés des mises à jour disponibles.<br><br>Ce paramètre est automatiquement activé lorsque **Copie exacte du serveur** est sélectionné.  |
| Masquer les anciennes versions de formulaires           | S'il existe plusieurs versions d'un même formulaire, seule la version la plus récemment téléchargée sera affichée lors du démarrage d'un nouveau formulaire. |
| Envoi automatique           | Lorsque cette option est activée, les formulaires sont envoyés au serveur dès qu'ils sont finalisés, si l'appareil peut se connecter à Internet. Si aucune connexion Internet n'est disponible au moment de la finalisation, vos formulaires finalisés seront mis en file d'attente pour être envoyés dès qu'une connexion sera établie. Vous pouvez spécifier si l'envoi doit se faire via le WiFi, les données mobiles, ou les deux. |
| Supprimer après envoi         | Supprime les formulaires finalisés et les fichiers média de l'appareil après leur envoi réussi au serveur. |
| Traitement des contraintes | Lorsque vos formulaires incluent des contraintes (critères de validation), choisissez entre valider les réponses lors du passage à la page suivante ou à la fin du formulaire. |
| Vidéo haute résolution        | Activez ou désactivez les enregistrements vidéo haute résolution lors de la prise de vidéos via l'application. |
| Taille des images      | Définissez la taille d'image préférée, de très petite à grande. Cela peut aider à économiser l'espace de stockage sur le serveur. |
| Afficher les instructions supplémentaires pour les questions         | Définissez comment les [instructions supplémentaires (guidance hints)](https://support.kobotoolbox.org/fr/question_options.html#guidance-hint) doivent être affichées dans votre formulaire. |
| Utiliser une application externe pour l'enregistrement audio        | Par défaut, un enregistreur interne est utilisé pour l'enregistrement audio. Activez ce paramètre pour utiliser une application audio externe à la place. |
| Finaliser les formulaires à l'importation            | Lorsque cette option est activée, les formulaires importés dans KoboCollect depuis l'extérieur de l'application (par exemple, copiés depuis le stockage de l'appareil ou une carte SD) sont automatiquement marqués comme <strong>Finalisés</strong>, afin qu'ils soient prêts à être envoyés sans nécessiter de finalisation manuelle. |


<p class="note">
    <strong>Note :</strong> La configuration de projets avec des <strong>mises à jour automatiques de formulaires</strong> est recommandée pour les projets avec des modifications fréquentes de formulaires ou des <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment_formbuilder.html">liaisons dynamiques de projets</a>. Cela supprime la nécessité de télécharger manuellement les mises à jour de formulaires. Cependant, des mises à jour automatiques plus fréquentes déchargeront plus rapidement la batterie de votre appareil.
</p>

## Paramètres d'identité de l'utilisateur et de l'appareil

Les paramètres d'identité de l'utilisateur et de l'appareil vous permettent de définir les métadonnées de l'appareil pour le suivi des soumissions.

| **Paramètre**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Métadonnées du formulaire  &emsp;&emsp;             | Saisissez un <strong>nom d'utilisateur</strong>, un <strong>numéro de téléphone</strong> et une <strong>adresse email</strong>, et consultez l'<strong>identifiant de l'appareil</strong> (défini automatiquement) pour fournir des informations supplémentaires sur la personne qui a soumis les enregistrements au serveur. Ces informations peuvent aider à valider la qualité des données collectées par l'équipe. |
| Collecter des données d'utilisation anonymes      | Autorisez l'équipe KoboToolbox à collecter des données d'utilisation anonymes pour nous aider à prioriser les corrections et les fonctionnalités. |

## Définir un mot de passe administrateur

Définissez un mot de passe administrateur dans l'application KoboCollect pour limiter l'accès au menu des paramètres **Protégés** aux seuls membres de l'équipe disposant du mot de passe administrateur. Cela peut aider à empêcher les agents de collecte de données de modifier les paramètres sur le terrain.

Pour supprimer le mot de passe administrateur, cliquez sur **Définir un mot de passe administrateur**, laissez le champ vide et cliquez sur **OK**.

## Gestion du projet

Les paramètres de gestion du projet fournissent des outils pour gérer et réinitialiser les paramètres liés au projet sur votre appareil, notamment la reconfiguration des paramètres, la réinitialisation de données spécifiques ou la suppression de toutes les données du projet.

| **Paramètre**&emsp;&emsp;&emsp;    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Reconfigurer avec un code QR &emsp;&emsp; | Reconfigurez vos paramètres KoboCollect en scannant un code QR d'un autre projet. Notez que cette approche remplacera le projet actuel par le nouveau. C'est également ici que vous pouvez trouver le code QR pour [configurer un autre appareil](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) avec les mêmes paramètres. |
| Réinitialiser | Réinitialisez des paramètres spécifiques, tels que l'effacement des [formulaires sauvegardés](https://support.kobotoolbox.org/fr/glossary.html#saved-forms-kobocollect), des données en cache ou des couches de carte, sans affecter les autres parties de l'application. |
| Supprimer | Supprimez le projet et toutes les données liées au projet de l'appareil, y compris les [formulaires vierges](https://support.kobotoolbox.org/fr/glossary.html#blank-forms-kobocollect), les formulaires soumis, les formulaires finalisés et les brouillons, ce qui peut être utile lors de la mise hors service d'un appareil ou de sa préparation pour un nouvel utilisateur. |

<p class="note">
    <strong>Note :</strong> Utilisez ces options avec précaution, en particulier lors de la suppression de données, car certaines actions sont irréversibles. La suppression de données de l'appareil n'affecte pas le projet KoboToolbox global et <strong>ne supprime pas les données déjà soumises au serveur</strong>, mais supprime les soumissions non envoyées ou en brouillon.
</p>

## Contrôle d'accès

Ce menu vous permet de masquer ou de restreindre certaines parties de l'interface de l'application, vous aidant à personnaliser l'application en fonction du rôle de l'utilisateur (par exemple, enquêteur ou superviseur). Cela permet de simplifier l'application et d'empêcher les modifications non autorisées.

| **Paramètre**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Paramètres du menu principal | Masquez ou affichez les options du menu principal (par exemple, **Télécharger formulaire** ou **Supprimer formulaire**). |
| Paramètres utilisateur | Masquez ou affichez les paramètres généraux (par exemple, la modification du serveur ou de l'identité de l'utilisateur). |
| Paramètres de saisie du formulaire | Masquez ou affichez les paramètres de saisie du formulaire (par exemple, autoriser la navigation en arrière, modifier les formulaires sauvegardés). |

Utilisez les cases à cocher pour activer ou désactiver des boutons et des paramètres spécifiques. Une fois configuré, l'ajout d'un [mot de passe administrateur](#set-admin-password) peut empêcher les modifications non autorisées.