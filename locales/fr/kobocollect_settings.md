# Personnalisation des paramètres de KoboCollect
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/5599bf9bc43c6872244104e236df84c6a6ed5f15/source/kobocollect_settings.md" class="reference">19 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/Qeky3aomiWI?si=M1l_jorFQEDacX2A" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect est une application KoboToolbox gratuite et open source conçue pour la collecte de données sur les appareils mobiles Android. Avant de commencer, [installez et configurez](kobocollect_on_android_latest.md) l'application Android KoboCollect. Une fois installée et configurée, vous pouvez personnaliser l'application en fonction de votre projet ou des besoins des utilisatrices et utilisateurs. Les paramètres du projet vous permettent de :

- Ajuster l'**interface utilisateur** (par exemple, la langue, la taille de la police, le thème)
- Configurer les **paramètres de carte** pour les questions basées sur la localisation
- Gérer la façon dont les formulaires sont traités (par exemple, envoi automatique, finalisation, règles de modification)
- Définir l'**identité de l'utilisatrice ou utilisateur et de l'appareil** pour le suivi des soumissions
- Protéger l'accès à l'application et à ses paramètres avec des **mots de passe ou des contrôles administrateur**
  
Pour accéder au menu des paramètres :

1. Appuyez sur l'**icône Projet** dans le coin supérieur droit de votre écran.
2. Appuyez sur **Paramètres**.

<p class="note">
  <strong>Remarque :</strong> Les utilisatrices et utilisateurs n'ont pas besoin d'une connexion Internet pour accéder ou modifier les paramètres du projet dans KoboCollect.
</p>

## Paramètres d'affichage du projet
Dans l'application KoboCollect, vous pouvez [vous connecter à plusieurs comptes KoboToolbox](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html#setting-up-multiple-projects-in-kobocollect). Les comptes utilisateurs sont appelés **Projets** dans KoboCollect. 

Pour personnaliser la façon dont chaque projet est affiché pour une reconnaissance et un changement plus faciles, vous pouvez modifier les paramètres d'**affichage du projet**. Ces modifications n'affectent que la façon dont le projet apparaît dans l'interface de l'appareil et n'affectent pas les données ou les autres appareils.

| **Paramètre**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Nom du projet              | Donnez un nom distinct à votre projet KoboCollect.                                  |
| Icône du projet      | Modifiez la lettre qui apparaît dans le cercle en haut à droite.                                  |
| Couleur du projet           | Modifiez la couleur du cercle en haut à droite.            |

## Paramètres de l'interface utilisateur

Les paramètres de l'interface utilisateur vous permettent d'ajuster l'apparence, la langue et la taille du texte de l'application pour une meilleure lisibilité.

| **Paramètre**    | **Description** |
| :----------------- | :--------------------------------------------- |
| Thème  | Choisissez entre une apparence claire, sombre ou par défaut du système pour l'application. |
| Langue      | Définissez la langue d'affichage de l'interface de l'application. Par défaut, KoboCollect correspond à la langue de l'appareil.|
| Taille de la police de texte           | Ajustez la taille du texte pour une meilleure lisibilité.            |
| Navigation           | Personnalisez la façon dont vous vous déplacez dans les formulaires. Choisissez entre les balayages horizontaux, les boutons avant/arrière ou une disposition combinée. |


<p class="note">
    <strong>Remarque :</strong> Changer la langue définit uniquement la langue de l'interface utilisateur de l'application et non celle du formulaire. Pour les formulaires avec <a href="language_dashboard.html">plusieurs langues</a>, la langue du formulaire est définie lors de la saisie des données.
</p>

## Paramètres des cartes

Les paramètres de carte configurent l'affichage et le comportement des cartes dans l'application pour les questions basées sur la localisation.

| **Paramètre**        | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Source   &emsp;&emsp;&emsp;&emsp;            | Définissez votre source de carte. Choisissez entre Google, OpenStreetMap, USGS ou Carto. |
| Style de carte      | Définissez votre style de carte si vous utilisez Google Maps, USGS ou Carto. |
| Couche           | Sélectionnez une couche hors ligne pour les cartes. Vous pouvez ajouter des options en sélectionnant un fichier MBTiles depuis votre appareil. |

## Paramètres de gestion des formulaires

Les paramètres de gestion des formulaires contrôlent la façon dont les formulaires sont traités dans l'application, y compris les mises à jour de version de formulaire, les soumissions et les comportements de saisie de données. 

| **Paramètre** | **Description**                  |
| :----------------- | :--------------------------------------------- |
| Mode de mise à jour des formulaires vierges &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Définissez si vous souhaitez que les nouvelles versions des formulaires soient mises à jour automatiquement ou manuellement. Les options incluent : <ul><li><strong>Manuel</strong> : Le mode par défaut, dans lequel les enquêtrices et enquêteurs gèrent manuellement la mise à jour des formulaires.</li><li><strong>Formulaires précédemment téléchargés uniquement</strong> : Les enquêtrices et enquêteurs reçoivent une notification lorsqu'un ou plusieurs formulaires précédemment téléchargés sur l'appareil ont une mise à jour disponible.</li><li><strong>Correspondre exactement au serveur</strong> : Tous les formulaires partagés avec le compte sont automatiquement téléchargés et mis à jour en fonction des modifications apportées au serveur.</li></ul> |
| Fréquence de mise à jour automatique      | Spécifie la fréquence à laquelle KoboCollect doit vérifier les mises à jour des formulaires sur le serveur lors de l'utilisation de **Formulaires précédemment téléchargés uniquement** ou **Correspondre exactement au serveur**. |
| Téléchargement automatique | Lorsque **Formulaires précédemment téléchargés uniquement** est sélectionné, vous pouvez choisir si les formulaires sont mis à jour automatiquement. Sinon, les utilisatrices et utilisateurs seront uniquement informés des mises à jour disponibles.<br><br>Ce paramètre est automatiquement activé lorsque **Correspondre exactement à la version du formulaire** est sélectionné.  |
| Masquer les anciennes versions de formulaire           | S'il existe plusieurs versions du même formulaire, seule la version la plus récemment téléchargée sera affichée lors du démarrage d'un nouveau formulaire. |
| Envoi automatique           | Lorsqu'il est activé, les formulaires sont envoyés au serveur immédiatement lorsqu'ils sont finalisés, si l'appareil peut se connecter à Internet. Si une connexion Internet n'est pas disponible au moment de la finalisation, vos formulaires finalisés seront mis en file d'attente pour être envoyés dès que la connectivité sera établie. Vous pouvez spécifier s'il faut envoyer via WiFi, données cellulaires ou les deux. |
| Supprimer après envoi         | Supprimez les formulaires finalisés et les médias de l'appareil après les avoir envoyés avec succès au serveur. |
| Traitement des contraintes | Lorsque vos formulaires incluent des contraintes (critères de validation), choisissez entre valider les réponses lors du passage à la page suivante ou à la fin du formulaire. |
| Vidéo haute résolution        | Activez ou désactivez les enregistrements vidéo haute résolution lors de la prise de vidéos via l'application. |
| Taille de l'image      | Définissez la taille d'image préférée, de très petite à grande. Cela peut aider à économiser l'espace de stockage sur le serveur. |
| Afficher les conseils pour les questions         | Définissez comment les [conseils d'orientation](https://support.kobotoolbox.org/fr/question_options.html?highlight=guidance+hint#guidance-hint-optional) doivent être affichés dans votre formulaire. |
| Utiliser une application externe pour l'enregistrement audio        | Par défaut, un enregistreur interne est utilisé pour l'enregistrement audio. Activez ce paramètre pour utiliser une application audio externe à la place. |
| Finaliser les formulaires lors de l'importation            | Lorsqu'il est activé, les formulaires qui sont importés dans KoboCollect depuis l'extérieur de l'application (par exemple, copiés depuis le stockage de l'appareil ou la carte SD) sont automatiquement marqués comme <strong>Finalisés</strong>, de sorte qu'ils sont prêts à être envoyés sans nécessiter de finalisation manuelle. |


<p class="note">
    <strong>Remarque :</strong> La configuration de projets pour les <strong>mises à jour automatiques de formulaires</strong> est recommandée dans les projets avec des modifications fréquentes de formulaires ou des <a href="dynamic_data_attachment.html">pièces jointes de données dynamiques</a>. Cela supprime le besoin de télécharger manuellement les mises à jour de formulaires. Cependant, des mises à jour automatiques plus fréquentes épuiseront la batterie de votre appareil plus rapidement.
</p>

## Paramètres d'identité de l'utilisatrice ou utilisateur et de l'appareil

Les paramètres d'identité de l'utilisatrice ou utilisateur et de l'appareil vous permettent de définir les métadonnées de l'appareil pour le suivi des soumissions.

| **Paramètre**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Métadonnées du formulaire  &emsp;&emsp;             | Saisissez un <strong>nom d'utilisatrice ou utilisateur</strong>, un <strong>numéro de téléphone</strong> et une <strong>adresse e-mail</strong>, et consultez l'<strong>identifiant de l'appareil</strong> (défini automatiquement) pour fournir des détails supplémentaires sur qui a soumis les enregistrements au serveur. Ces détails peuvent aider à valider la qualité des données collectées par l'équipe. |
| Collecter des données d'utilisation anonymes      | Autorisez l'équipe KoboToolbox à collecter des données d'utilisation anonymes pour nous aider à prioriser les corrections et les fonctionnalités. |

## Définir le mot de passe administrateur

Définissez un mot de passe administrateur dans l'application KoboCollect, limitant l'accès au menu des paramètres **Protégés** uniquement aux membres de l'équipe disposant du mot de passe administrateur. Cela peut aider à empêcher les collectrices et collecteurs de données de modifier les paramètres sur le terrain.

Pour supprimer le mot de passe administrateur, cliquez sur **Définir le mot de passe administrateur**, laissez le champ vide et cliquez sur **OK**. 

## Gestion du projet

Les paramètres de gestion du projet fournissent des outils pour gérer et réinitialiser les paramètres liés au projet sur votre appareil, y compris la reconfiguration des paramètres, la réinitialisation de données spécifiques ou la suppression de toutes les données du projet.

| **Paramètre**&emsp;&emsp;&emsp;    | **Description**                                |
| :----------------- | :--------------------------------------------- |
|Reconfigurer avec un code QR &emsp;&emsp; | Reconfigurez vos paramètres KoboCollect en scannant un code QR d'un autre projet. Notez que cette approche remplacera le projet actuel par le nouveau. C'est également ici que vous pouvez trouver le code QR pour [configurer un autre appareil](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) avec les mêmes paramètres. |
| Réinitialiser | Réinitialisez des paramètres spécifiques, tels que l'effacement des formulaires enregistrés, des données en cache ou des couches de carte, sans affecter d'autres parties de l'application. |
| Supprimer | Supprimez toutes les données liées au projet de l'appareil, y compris les formulaires vierges, les données soumises et les paramètres, ce qui peut être utile lors de la mise hors service d'un appareil ou de sa préparation pour une nouvelle utilisatrice ou un nouvel utilisateur. |

<p class="note"> 
    <strong>Remarque :</strong> Utilisez ces options avec prudence, en particulier lors de la suppression de données, car certaines actions ne peuvent pas être annulées. La suppression de données de l'appareil n'affecte pas le projet KoboToolbox global et ne supprime pas les données du serveur.
</p>

## Contrôle d'accès

Ce menu vous permet de masquer ou de restreindre des parties de l'interface de l'application, vous aidant à personnaliser l'application en fonction du rôle de l'utilisatrice ou utilisateur (par exemple, enquêtrice ou enquêteur vs superviseure ou superviseur). Cela aide à simplifier l'application et empêche les modifications non autorisées.

| **Paramètre**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Paramètres du menu principal | Masquez ou affichez les options du menu principal (par exemple, **Télécharger formulaire** ou **Supprimer formulaire**). |
| Paramètres utilisateur | Masquez ou affichez les paramètres généraux (par exemple, modification du serveur ou de l'identité de l'utilisatrice ou utilisateur). |
| Paramètres de saisie de formulaire | Masquez ou affichez les paramètres de saisie de formulaire (par exemple, autoriser la navigation vers l'arrière, modifier les formulaires enregistrés). |

Utilisez les cases à cocher pour activer ou désactiver des boutons et des paramètres spécifiques. Une fois configuré, l'ajout d'un [mot de passe administrateur](#définir-le-mot-de-passe-administrateur) peut empêcher les modifications non autorisées.