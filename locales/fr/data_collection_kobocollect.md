# Collecte de données avec KoboCollect
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/883b3a06b2cb3ea94f7a7b69c5be2b85953ad453/source/data_collection_kobocollect.md" class="reference">24 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/IEm61fpLoz4?si=TdlWhcVt0OxETlxl&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect est une application KoboToolbox gratuite et open source conçue pour la collecte de données sur appareils mobiles. Elle est particulièrement adaptée aux équipes de terrain composées d'enquêteurs utilisant des téléphones ou tablettes Android, notamment lorsque les données doivent être collectées hors ligne.

Avant de commencer, vous devez [installer et configurer](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html) l'application KoboCollect. Une fois configurée, KoboCollect vous permet de remplir et d'envoyer des formulaires depuis votre appareil mobile, même sans connexion internet.

Cet article explique comment utiliser KoboCollect pour la collecte de données, notamment le téléchargement de formulaires, la saisie et la modification de soumissions, l'envoi de formulaires finalisés, la suppression de formulaires enregistrés ou vierges, ainsi que la résolution des problèmes courants.

<p class="note">
Pour plus d'informations sur l'application KoboCollect et les appareils recommandés, consultez l'article <a href="https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html">Configurer l'application KoboCollect</a>.
</p>

## Télécharger des formulaires

Pour commencer la collecte de données avec KoboCollect, vous devez télécharger le ou les formulaires KoboToolbox sur votre appareil. Avant de télécharger, assurez-vous de disposer des éléments suivants :

- Au moins un [formulaire déployé](https://support.kobotoolbox.org/fr/deploy_form_new_project.html) dans votre compte KoboToolbox (dont vous êtes propriétaire ou qui a été partagé avec vous).
- Un projet (compte) [configuré dans KoboCollect](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html).
- Une connexion internet sur votre appareil.

Pour télécharger des formulaires sur votre appareil :
- Depuis le menu principal, appuyez sur **Download form**.
- Sélectionnez le ou les formulaires à télécharger individuellement en appuyant sur la case à cocher à côté de chaque formulaire, ou appuyez sur **Select all** pour télécharger tous les formulaires déployés.
- Appuyez sur **Get Selected**.

Les formulaires téléchargés apparaîtront lorsque vous appuierez sur **Start new form** depuis le menu principal de l'application.

<p class="note">
  <strong>Note :</strong>
Si votre projet a été configuré pour le <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">téléchargement automatique des formulaires</a> avec l'option <strong>Exactly match server</strong>, tous les formulaires partagés avec le compte sont automatiquement téléchargés sur l'appareil, ce qui rend l'étape précédente inutile.
</p>

## Récupérer les mises à jour des formulaires

Lorsque des modifications sont apportées à un formulaire de collecte de données, vous devez récupérer les mises à jour dans KoboCollect **tout en étant connecté à internet.** La méthode de récupération des mises à jour dépend des [paramètres du projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings).

| Paramètres | Récupération des mises à jour |
|:---|:---|
| Paramètres par défaut | Téléchargez les nouvelles versions d'un formulaire en appuyant sur **Download form**, en sélectionnant le ou les formulaires à mettre à jour, puis en appuyant sur **Get Selected.** |
| Previously downloaded forms only | Les mises à jour se téléchargent automatiquement à la fréquence configurée dans les paramètres du projet.<br><br>Pour forcer une mise à jour et vous assurer d'utiliser la dernière version, appuyez sur **Download form**, sélectionnez le ou les formulaires à mettre à jour, puis appuyez sur **Get Selected.** |
| Exactly match server | Les mises à jour se téléchargent automatiquement à la fréquence configurée dans les paramètres du projet.<br><br>Pour forcer une mise à jour et vous assurer d'utiliser la dernière version, appuyez sur **Start new form**, puis appuyez sur le bouton Rafraîchir en haut à droite. |

<p class="note">
  <strong>Note :</strong>
Si vous anticipez des mises à jour fréquentes de formulaires ou si vous utilisez des <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment.html">liaisons dynamiques de projets</a>, qui nécessitent des mises à jour régulières pour récupérer les données du formulaire principal, nous vous recommandons d'activer le <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">téléchargement automatique des formulaires</a>.
</p>

## Collecter des données

Une fois les formulaires téléchargés, vous pouvez commencer la collecte de données. Notez qu'une fois le ou les formulaires téléchargés dans l'application, vous n'avez pas besoin d'une connexion internet pour collecter des données.

1. Depuis le menu principal, appuyez sur **Start new form**.
2. Sélectionnez le formulaire avec lequel vous souhaitez collecter des données.
3. Pour changer la langue du formulaire, appuyez sur l'icône <i class="k-icon-more"></i> **trois points** dans le coin supérieur droit de l'écran, puis appuyez sur **Change Language**.
4. Naviguez entre les questions en faisant glisser vers la gauche ou en appuyant sur **NEXT** après avoir répondu.
5. À la fin du questionnaire, vous pouvez choisir de **Save as draft**, **Finalize** ou **Send** le formulaire (selon vos [paramètres du projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings)).

| **Option** | **Description** |
| :----------------- | :--------------------------------------------- |
| Save as draft &emsp;&emsp;&emsp; | Le formulaire sera enregistré dans **Drafts** et pourra encore être modifié avant d'être finalisé. |
| Finalize | Le formulaire sera enregistré dans **Ready to send** et ne pourra plus être modifié. Cette option n'apparaît que si le paramètre **Auto send** est défini sur **Off**. |
| Send | Le formulaire sera envoyé directement au serveur ou mis en file d'attente jusqu'à ce qu'une connexion internet soit disponible. Il ne pourra plus être modifié. Cette option n'apparaît que si le paramètre **Auto send** est activé. |

Par défaut, les formulaires et les données restent sur l'appareil jusqu'à leur suppression manuelle. Si vous activez **Delete after send** dans les [paramètres du projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings), les formulaires seront automatiquement supprimés une fois envoyés au serveur.

## Modifier des brouillons

Si vous avez enregistré un questionnaire comme brouillon, vous pouvez le modifier avant de l'envoyer au serveur :

1. Depuis le menu principal, sélectionnez **Drafts**.
2. Une liste des formulaires enregistrés comme brouillons apparaîtra. Sélectionnez celui que vous souhaitez modifier.
3. Apportez les modifications nécessaires, puis appuyez sur **Finalize** ou **Send**, selon votre flux de travail.

<p class="note">
  <strong>Note :</strong> Vous n'avez pas besoin d'une connexion internet pour modifier un formulaire enregistré dans KoboCollect.
</p>

## Envoyer les formulaires finalisés au serveur

Après avoir finalisé vos formulaires, vous devez les importer sur le serveur KoboToolbox. Les formulaires sont souvent remplis et finalisés hors ligne, puis envoyés en lot une fois qu'une connexion internet est disponible. Pour envoyer vos formulaires au serveur KoboToolbox :

1. Assurez-vous que l'appareil dispose d'une connexion internet sécurisée.
2. Depuis le menu principal, appuyez sur **Ready to send**. Une liste des formulaires finalisés apparaîtra.
3. Appuyez sur **Select All**, ou sélectionnez manuellement les formulaires à envoyer en cochant la case correspondante.
4. Appuyez sur **Send Selected** pour envoyer les formulaires au serveur.

Pour vérifier que l'envoi a réussi, accédez au menu principal et sélectionnez **Sent**. Vous verrez tous les formulaires envoyés au serveur, ainsi que leur date de synchronisation.

<p class="note">
  <strong>Note :</strong> Si votre projet est <strong>configuré pour envoyer automatiquement les formulaires finalisés</strong>, la page <strong>Ready to send</strong> n'apparaîtra pas dans le menu principal et vous pouvez ignorer ces étapes. Pour plus d'informations sur les paramètres du projet dans KoboCollect, consultez l'article <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html">Personnaliser les paramètres KoboCollect</a>.
</p>

## Supprimer des formulaires enregistrés et des formulaires vierges

Après avoir finalisé la collecte de données et importé tous les formulaires complétés sur le serveur, vous souhaiterez peut-être supprimer les données de formulaires restantes de l'application KoboCollect, sauf si la suppression automatique est [déjà activée](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) sur votre appareil. Cela contribue à protéger la confidentialité des données et à éviter toute confusion lors de la collecte de données pour un nouveau projet.

Il existe deux types de formulaires pouvant être supprimés :

- **Saved Forms** : Ce sont des [formulaires pour lesquels des données ont été saisies](https://support.kobotoolbox.org/fr/glossary.html#saved-forms-kobocollect), notamment les brouillons, les formulaires finalisés et les formulaires déjà envoyés au serveur.
- **Blank Forms** : Ce sont des [formulaires de collecte de données vierges](https://support.kobotoolbox.org/fr/glossary.html#blank-forms-kobocollect) téléchargés sur l'appareil depuis la page **Download form**. Ne supprimez ces formulaires qu'une fois la collecte de données terminée.

Pour supprimer des formulaires :
1. Depuis le menu principal, appuyez sur **Delete form**. Deux onglets apparaîtront.
2. Sous **Saved Forms** :
    - Appuyez sur **Select All** pour supprimer tous les formulaires enregistrés, ou sélectionnez des formulaires individuels.
    - Appuyez sur **Delete Selected**.
3. Sous **Blank Forms** :
    - Appuyez sur **Select All** pour supprimer tous les formulaires vierges, ou sélectionnez des formulaires individuels.
    - Appuyez sur **Delete Selected**.

<p class="note">
  <strong>Note :</strong> Vous n'avez pas besoin d'une connexion internet pour supprimer des formulaires dans KoboCollect. Cependant, si des formulaires vierges sont accidentellement supprimés hors ligne, une connexion internet est nécessaire pour les récupérer et poursuivre la collecte de données. Pour éviter toute suppression accidentelle, vous pouvez définir des contrôles d'accès dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#access-control">paramètres du projet</a>.
</p>

## Résolution de problèmes

<details>
<summary><strong>Le chargement de la page Download form prend trop de temps</strong></summary>
Si la page <strong>Download form</strong> met longtemps à se connecter au serveur ou à charger les formulaires disponibles, votre compte KoboToolbox contient peut-être trop de formulaires actifs, ou votre connexion internet est faible.
<br><br>
Essayez les solutions suivantes :
<br>
<ul>
<li>Archivez les formulaires qui ne sont plus utilisés afin de réduire le nombre de formulaires que KoboCollect doit charger.</li>
<li>Vérifiez que votre connexion internet est stable, puis réessayez.</li>
</ul>
</details>

<br>

<details>
<summary><strong>KoboCollect affiche une ancienne version du formulaire</strong></summary>
Si KoboCollect affiche une version plus ancienne de votre formulaire, téléchargez à nouveau le formulaire pour obtenir la dernière version déployée. Vous pouvez également activer les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">mises à jour automatiques des formulaires</a> dans KoboCollect afin que l'application vérifie l'existence de versions plus récentes lors de la connexion au serveur.
</details>

<br>

<details>
<summary><strong>Error evaluating field […] XPath evaluation: type mismatch. This field is repeated</strong></summary>
Cette erreur signifie que votre formulaire utilise des <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment.html">liaisons dynamiques de projets</a> et que le champ utilisé pour relier les données du formulaire principal et du formulaire secondaire contient des valeurs en double dans les données du formulaire principal. Le champ de liaison doit contenir uniquement des valeurs uniques.
<br><br>
Pour corriger ce problème, supprimez ou corrigez les valeurs en double dans le champ de liaison des données du formulaire principal, ou utilisez l'argument <code>[position() = 1]</code> dans votre calcul.
</details>

<br>

<details>
<summary><strong>Repeats in 'field-list' groups are not supported</strong></summary>
Cette erreur se produit dans KoboCollect lorsqu'un groupe répété est imbriqué dans un groupe plus large utilisant l'apparence <code>field-list</code>. KoboCollect ne permet pas les groupes répétés à l'intérieur de groupes <code>field-list</code>. Les groupes répétés doivent apparaître sur leur propre page.
<br><br>
Pour résoudre ce problème, déplacez le groupe répété en dehors du groupe principal, ou supprimez l'apparence <code>field-list</code> du groupe principal.
</details>

<br>

<details>
<summary><strong>Error getting form list</strong></summary>
Si vous voyez "Error getting form list" après avoir ouvert <strong>Download form</strong>, vérifiez d'abord que l'URL du serveur KoboToolbox dans KoboCollect est correcte. Une faute de frappe dans l'URL est une cause fréquente de cette erreur.
<br><br>
Assurez-vous également que l'appareil est connecté à internet. Dans certains cas, l'appareil peut sembler connecté à un réseau Wi-Fi mais nécessiter une connexion via un navigateur avant que l'accès à internet soit disponible.
</details>

<br>

<details>
<summary><strong>Erreurs de connexion sécurisée</strong></summary>
Vous pouvez voir une erreur telle que "Generic Exception: No peer certificate", "Form listing failed", ou <code>SSLPeerUnverifiedException</code> lorsque KoboCollect ne parvient pas à établir une connexion sécurisée au serveur.
<br><br>
La cause la plus fréquente est que la date de l'appareil est incorrecte. Vérifiez les paramètres de date et d'heure du téléphone ou de la tablette, puis réessayez. Cela peut se produire si la batterie de l'appareil s'est complètement déchargée et que la date a été réinitialisée.
<br><br>
Cette erreur peut également apparaître lors de l'utilisation d'un réseau Wi-Fi ou d'un point d'accès qui nécessite une connexion via un navigateur avant d'autoriser l'accès à internet.
</details>

<br>

<details>
<summary><strong>Unable to edit this blank form because the corresponding blank form is not present or was deleted</strong></summary>
Cette erreur apparaît lorsque vous essayez de modifier un <a href="https://support.kobotoolbox.org/fr/glossary.html#saved-forms-kobocollect">formulaire enregistré</a>, mais que le <a href="https://support.kobotoolbox.org/fr/glossary.html#blank-forms-kobocollect">formulaire vierge</a> d'origine n'est plus disponible sur l'appareil.
<br><br>
Pour corriger ce problème, téléchargez à nouveau le formulaire vierge. Vous devriez ensuite pouvoir rouvrir et continuer à modifier le formulaire enregistré.
</details>

<br>

<details>
<summary><strong>Aucun accès à internet</strong></summary>
Si les appareils de terrain ne peuvent accéder à internet à aucun moment, les soumissions KoboCollect peuvent tout de même être transférées manuellement de l'appareil vers un ordinateur à l'aide d'<a href="https://docs.getodk.org/briefcase-intro">outils externes</a> et d'une connexion USB. Dans des configurations plus avancées, il est également possible de <a href="https://github.com/kobotoolbox/kobo-install">faire fonctionner KoboToolbox localement</a> sur un ordinateur et de connecter des appareils via un réseau local sans accès à internet.
<br><br>
Ces approches sont moins courantes et nécessitent une configuration supplémentaire ; elles conviennent donc généralement mieux aux flux de travail spécialisés.
</details>