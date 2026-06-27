# Collecter des données avec KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/a42f7ff93a1567cc2ac66a749d2a7d5969cfa45a/source/data-collection-tools.md" class="reference">23 Apr 2026</a>

KoboToolbox propose deux méthodes principales de collecte de données : les **formulaires web**, qui s'exécutent dans un navigateur, et **KoboCollect**, l'application Android dédiée à la collecte mobile de données. Les deux méthodes permettent la collecte de données hors ligne.

Cet article présente les deux méthodes de collecte de données disponibles dans KoboToolbox, comment choisir entre elles et comment se préparer avant de lancer la collecte de données.

<p class="note">
Pour en savoir plus sur chaque méthode de collecte de données, consultez les articles <a href="https://support.kobotoolbox.org/fr/data_through_webforms.html">Collecte de données via des formulaires web</a> et <a href="https://support.kobotoolbox.org/fr/data_collection_kobocollect.html">Collecte de données avec KoboCollect</a>.
</p>

## Méthodes de collecte de données

Vous pouvez collecter des données avec KoboToolbox de deux manières principales :
- Les **formulaires web** sont des formulaires accessibles depuis un navigateur, utilisés pour collecter des données via une page web. Ils sont particulièrement adaptés aux enquêtes auto-administrées et à la saisie de données dans un navigateur.
- **KoboCollect** est une application Android utilisée pour collecter des données sur des appareils Android. Elle est particulièrement adaptée aux équipes de terrain dont les enquêteurs utilisent des téléphones ou des tablettes Android.

Les deux méthodes permettent la [collecte de données hors ligne](https://support.kobotoolbox.org/fr/data-collection-tools.html#offline-data-collection).

### Choisir une méthode de collecte de données

La meilleure méthode de collecte de données dépend de la façon dont votre équipe travaillera en pratique. Dans certains cas, les équipes peuvent utiliser les deux méthodes au sein d'un même projet.

Le tableau ci-dessous résume les situations dans lesquelles chaque méthode est généralement la plus adaptée :

| Formulaires web | KoboCollect |
| :--- | :--- |
| **Recommandé si :** <br> <ul><li>Les répondants soumettront leurs données directement via un lien</li><li>Vous souhaitez un moyen simple d'ouvrir et de partager un formulaire</li><li>Votre équipe utilise différents types d'appareils</li><li>Vous souhaitez utiliser la collecte de données dans un navigateur sans installer d'application</li><li>Votre formulaire inclut des fonctionnalités uniquement disponibles dans les formulaires web, telles que le [thème grille](https://support.kobotoolbox.org/fr/alternative_enketo.html) ou les [tableaux de questions](https://support.kobotoolbox.org/fr/matrix_response.html)</li></ul> | **Recommandé si :**<br><ul><li>Une grande partie de votre collecte de données se fait sur le terrain dans des environnements hors ligne</li><li>Les données sont collectées par une équipe d'enquêteurs utilisant des téléphones ou des tablettes Android</li><li>Les enquêteurs préfèrent un flux de travail basé sur une application (par exemple, pour enregistrer des brouillons et envoyer des soumissions finalisées ultérieurement)</li><li>Votre projet repose sur des fonctionnalités propres aux appareils mobiles, telles que la [lecture de codes-barres ou la capture d'images et de vidéos](https://support.kobotoolbox.org/fr/photo_audio_video_file.html)</li><li>Vous souhaitez un meilleur contrôle sur la gestion des formulaires et l'automatisation, comme l'envoi de formulaires, le téléchargement de formulaires ou la suppression des données importées depuis les appareils</li></ul> |

Pour choisir une méthode, tenez compte de la façon dont les personnes accéderont au formulaire, des appareils qu'elles utiliseront, de la fréquence à laquelle elles devront travailler hors ligne, et de si votre formulaire inclut des fonctionnalités mieux disponibles dans l'une ou l'autre des méthodes.

<p class="note">
<strong>Remarque :</strong>
Certaines fonctionnalités se comportent différemment selon la méthode de collecte utilisée. Gardez cela à l'esprit avant de lancer la collecte de données, et testez toujours votre formulaire avec la méthode que votre équipe utilisera.
</p>

### Collecte de données hors ligne

Les formulaires web et KoboCollect permettent tous deux la **collecte de données hors ligne.**

- Avec les **formulaires web**, KoboToolbox peut stocker le formulaire et les réponses dans le cache du navigateur, ce qui permet aux utilisateurs de continuer à saisir des données sans connexion internet.
  - Avant de passer hors ligne, vous devrez ouvrir le formulaire en étant connecté à internet et attendre qu'il soit entièrement chargé et [mis en cache sur l'appareil](https://support.kobotoolbox.org/fr/data_through_webforms.html#offline-data-collection).
  - Lorsque l'appareil se reconnecte, les soumissions enregistrées seront importées automatiquement.
- Avec **KoboCollect**, les enquêteurs peuvent télécharger des formulaires vierges en étant connectés, les remplir hors ligne, enregistrer des brouillons, finaliser des soumissions et les envoyer ultérieurement lorsqu'une connexion internet est disponible.
  - KoboCollect peut également être [configuré](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) pour envoyer automatiquement les formulaires finalisés dès qu'une connexion est disponible, ou uniquement lorsque l'utilisateur choisit de les importer.

## Se préparer pour la collecte de données

Avant de pouvoir collecter des données, vous devez **déployer votre formulaire** pour le rendre actif et disponible pour les soumissions. Si vous apportez des modifications au formulaire ultérieurement, vous devrez le redéployer.

<p class="note">
Pour en savoir plus sur le déploiement de votre formulaire pour la collecte de données, consultez l'article <a href="https://support.kobotoolbox.org/fr/deploy_form_new_project.html">Déployer vos formulaires pour la collecte de données</a>.
</p>

Une fois votre formulaire déployé, assurez-vous que votre configuration de collecte de données est prête avant de lancer la collecte :
- Décidez quelle(s) méthode(s) de collecte de données utiliser
- Confirmez qui peut accéder au formulaire et si une authentification doit être requise
- Testez le projet dans des conditions similaires à votre collecte de données réelle, en utilisant les mêmes appareils et la même méthode de collecte que vos répondants ou enquêteurs

Selon la méthode de collecte choisie, nous recommandons également les étapes suivantes :


| Formulaires web | KoboCollect |
| :--- | :--- |
| <ul><li>Décidez si le formulaire doit [exiger une authentification](https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication)</li><li>Si votre formulaire exige une authentification, assurez-vous que les collecteurs de données disposent des [droits d'accès](https://support.kobotoolbox.org/fr/managing_permissions.html) nécessaires pour accéder à votre formulaire de collecte de données</li><li>Décidez quel [mode de formulaire web](https://support.kobotoolbox.org/fr/data_through_webforms.html#data-collection-modes) utiliser pour la collecte de données</li><li>Partagez le lien correct du formulaire avec les collecteurs de données ou les répondants</li></ul> | <ul><li>Confirmez que les collecteurs de données disposent des [droits d'accès](https://support.kobotoolbox.org/fr/managing_permissions.html) nécessaires pour accéder à votre formulaire de collecte de données</li><li>Assurez-vous que chaque collecteur de données a [installé et configuré](https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html) l'application KoboCollect</li><li>Confirmez que chaque collecteur de données a [téléchargé le ou les formulaires](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html#downloading-forms) avant de commencer le travail de terrain</li></ul> |


<p class="note">
<strong>Remarque :</strong>
Par défaut, les projets déployés sont configurés pour <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">exiger une authentification</a>, ce qui signifie que les utilisateurs doivent se connecter pour accéder à un formulaire web ou soumettre des données. Pour permettre à <strong>toute personne disposant du lien du formulaire</strong> de soumettre des données, désactivez l'exigence d'authentification pour le formulaire. Si vous conservez l'authentification activée, <a href="https://support.kobotoolbox.org/fr/managing_permissions.html">partagez le projet</a> avec des utilisateurs KoboToolbox spécifiques et accordez-leur la permission <strong>Ajouter des soumissions</strong>.
</p>