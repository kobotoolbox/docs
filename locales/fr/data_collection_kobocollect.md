# Collecte de données avec KoboCollect
<a href="../data_collection_kobocollect.html">Read in English</a> | <a href="../es/data_collection_kobocollect.html">Leer en español</a> | <a href="../ar/data_collection_kobocollect.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/711a8034f16611e23d4ff78183c4e20825abc818/source/data_collection_kobocollect.md" class="reference">19 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/IEm61fpLoz4?si=TdlWhcVt0OxETlxl" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect est une application KoboToolbox gratuite et open source conçue pour la collecte de données sur les appareils mobiles Android. Avant de commencer, [installez et configurez](kobocollect_on_android_latest.md) l'application Android KoboCollect. 

Une fois configurée, KoboCollect vous permet de remplir et de soumettre des formulaires depuis votre appareil mobile, même hors ligne. Cet article explique comment utiliser l'application pour collecter des données, notamment comment accéder aux formulaires, enregistrer et modifier les réponses, et envoyer les soumissions finalisées.

## Télécharger des formulaires

Pour commencer la collecte de données avec KoboCollect, vous devrez télécharger le ou les formulaires KoboToolbox sur votre appareil. Avant de télécharger, assurez-vous d'avoir :

- Au moins un [formulaire déployé](deploy_form_new_project.md) dans votre compte KoboToolbox (dont vous êtes propriétaire ou qui a été partagé avec vous).
- Un projet (compte) [configuré sur KoboCollect](kobocollect_on_android_latest.md).
- Une connexion Internet sur votre appareil.
  
Pour télécharger des formulaires sur votre appareil :
- Depuis le menu principal, cliquez sur **Télécharger formulaire**.
- Sélectionnez le ou les formulaires que vous souhaitez télécharger individuellement en appuyant sur la case à cocher à côté de chaque formulaire, ou appuyez sur **Tout sélectionner** pour télécharger tous les formulaires déployés.
- Appuyez sur **Télécharger la sélection**.

Les formulaires téléchargés apparaîtront lorsque vous cliquerez sur **Remplir un formulaire** depuis le menu principal de l'application.

<p class="note">
  <strong>Remarque :</strong> Vous devrez répéter ce processus chaque fois qu'une mise à jour est apportée au formulaire ou aux médias du formulaire. Si vous prévoyez des mises à jour fréquentes du formulaire ou si vous utilisez des <a href="dynamic_data_attachment.html">pièces jointes de données dynamiques</a>, nous vous recommandons d'activer les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">téléchargements automatiques de formulaires</a>. 
</p>

## Collecter des données

Une fois les formulaires téléchargés, vous pouvez commencer la collecte de données. Notez qu'une fois que vous avez téléchargé le ou les formulaires dans l'application, vous n'avez pas besoin de connexion Internet pour collecter des données. 

1. Depuis le menu principal, appuyez sur **Remplir un formulaire**.
2. Sélectionnez le formulaire avec lequel vous souhaitez collecter des données.
3. Pour changer la langue du formulaire, appuyez sur l'**icône des trois points** <i class="k-icon-more"></i> dans le coin supérieur droit de l'écran et cliquez sur **Change Language**.
4. Naviguez à travers les questions en balayant vers la gauche ou en cliquant sur **SUIVANT** après avoir répondu.
5. À la fin de l'enquête, vous pouvez choisir de **Sauvegarder le brouillon**, **Finaliser** ou **Envoyer** le formulaire (selon vos [paramètres de projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings)).

| **Option** | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Sauvegarder le brouillon  &emsp;&emsp;&emsp;        | Le formulaire sera enregistré dans **Ébauches** et pourra encore être modifié avant finalisation. |
| Finaliser      | Le formulaire sera enregistré dans **Prêt à envoyer** et ne pourra plus être modifié. Cette option n'apparaît que si le paramètre **Auto send** est défini sur **Off**.                                  |
| Envoyer           | Le formulaire sera envoyé directement au serveur ou mis en file d'attente jusqu'à ce qu'une connexion Internet soit disponible. Il ne pourra plus être modifié. Cette option n'apparaît que si le paramètre **Auto send** est activé.            |

Par défaut, les formulaires et les données restent sur l'appareil jusqu'à leur suppression manuelle. Si vous activez **Delete after send** dans les [paramètres de projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings), les formulaires seront supprimés automatiquement une fois qu'ils auront été soumis au serveur.

## Modifier les brouillons

Si vous avez enregistré une enquête comme brouillon, vous pouvez la modifier avant de l'envoyer au serveur :

1. Depuis le menu principal, sélectionnez **Ébauches**.
2. Une liste des formulaires brouillons enregistrés apparaîtra. Sélectionnez celui que vous souhaitez modifier.
3. Apportez les modifications nécessaires, puis appuyez sur **Finaliser** ou **Envoyer**, selon votre flux de travail.

<p class="note">
  <strong>Remarque :</strong> Vous n'avez pas besoin de connexion Internet pour modifier un formulaire enregistré dans KoboCollect.
</p>

## Envoyer les formulaires finalisés au serveur

Après avoir finalisé vos formulaires, vous devez les importer sur le serveur KoboToolbox. Les formulaires sont souvent complétés et finalisés hors ligne, puis importés en masse une fois qu'une connexion Internet est disponible. Pour envoyer vos formulaires au serveur KoboToolbox :

1. Assurez-vous que l'appareil dispose d'une connexion Internet sécurisée.
2. Depuis le menu principal, appuyez sur **Prêt à envoyer**. Une liste des formulaires finalisés apparaîtra.
3. Appuyez sur **Tout sélectionner**, ou sélectionnez manuellement les formulaires que vous souhaitez importer en cochant la case.
4. Appuyez sur **Envoyer éléments sélectionnés** pour soumettre les formulaires au serveur.

Pour vérifier la réussite de l'importation, allez dans le menu principal et sélectionnez **Envoyé**. Vous verrez tous les formulaires envoyés au serveur, ainsi que leur date de synchronisation.

<p class="note">
  <strong>Remarque :</strong> Si votre projet est <strong>configuré pour envoyer automatiquement les formulaires finalisés</strong>, la page <strong>Prêt à envoyer</strong> n'apparaîtra pas dans le menu principal, et vous pouvez ignorer ces étapes. Pour plus d'informations sur les paramètres de projet dans KoboCollect, consultez <a href="kobocollect_settings.html">Personnaliser les paramètres de KoboCollect</a>.
</p>

## Supprimer les formulaires enregistrés et les formulaires vierges

Après avoir finalisé la collecte de données et importé tous les formulaires complétés sur le serveur, vous souhaiterez peut-être supprimer les données de formulaire restantes de l'application KoboCollect, à moins que la suppression automatique ne soit [déjà activée](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) pour votre appareil. Cela permet de protéger la confidentialité des données et d'éviter toute confusion lors de la collecte de données pour un nouveau projet.

Il existe deux types de formulaires qui peuvent être supprimés :

- **Formulaires enregistrés** : Ce sont des formulaires pour lesquels des données ont été renseignées, y compris les brouillons, les formulaires finalisés et les formulaires qui ont été envoyés au serveur.
- **Formulaires vierges** : Ce sont des formulaires de collecte de données vides qui ont été téléchargés sur l'appareil depuis la page **Télécharger formulaire**. Ne supprimez ces formulaires qu'une fois la collecte de données terminée pour ceux-ci.
  
Pour supprimer des formulaires :
1. Depuis le menu principal, appuyez sur **Supprimer formulaire**. Vous verrez deux onglets.
2. Sous **Formulaires enregistrés** :
    - Appuyez sur **Tout sélectionner** pour supprimer tous les formulaires enregistrés, ou sélectionnez des formulaires individuels.
    - Appuyez sur **Supprimer la sélection**.
3. Sous **Formulaires vierges** :
    - Appuyez sur **Tout sélectionner** pour supprimer tous les formulaires vierges, ou sélectionnez des formulaires individuels.
    - Appuyez sur **Supprimer la sélection**.

<p class="note">
  <strong>Remarque :</strong> Vous n'avez pas besoin de connexion Internet pour supprimer des formulaires enregistrés dans KoboCollect. Cependant, si des formulaires vierges sont accidentellement supprimés hors ligne, une connexion Internet est nécessaire pour les récupérer afin de poursuivre la collecte de données. Pour éviter toute suppression accidentelle, vous pouvez définir des contrôles d'accès dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#access-control">paramètres de projet</a>.
</p>