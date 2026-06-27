# Aperçu de l'interface KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/ec2d0081eef81fecd0dc9ee9a6cfdcd53c0f320f/source/kobotoolbox_interface.md" class="reference">5 juin 2026</a>

Cet article présente un aperçu de l'interface KoboToolbox et explique comment naviguer dans les principales pages où vous créez des formulaires, gérez des données et configurez les paramètres de votre projet. Il introduit la **page d'accueil Projets** et les quatre pages principales de chaque projet : **SOMMAIRE**, **FORMULAIRE**, **DONNÉES** et **PARAMÈTRES**.

## Naviguer dans la page d'accueil Projets
Lorsque vous vous connectez à votre compte KoboToolbox, vous arrivez sur la **page d'accueil Projets**. La **page d'accueil Projets** affiche tous les projets que vous possédez ou qui ont été partagés avec votre compte. Depuis cette page, vous pouvez également accéder aux fonctionnalités clés et aux paramètres au niveau du compte.

La **page d'accueil Projets** comprend les éléments suivants :
* Une liste de tous les projets appartenant à votre compte ou partagés avec celui-ci.
* L'accès à la <i class="k-icon-library"></i> **Bibliothèque** depuis le menu de gauche.
* Le bouton **NOUVEAU** pour créer un nouveau projet.
* Des onglets pour afficher les formulaires <i class="k-icon-deploy"></i> **Déployés**, <i class="k-icon-drafts"></i> **Brouillons** ou <i class="k-icon-archived"></i> **Archivés**.
* Une barre de <i class="k-icon-search"></i> **Recherche** pour trouver des projets dans votre liste de projets.
* Une **icône de profil** en haut à droite pour accéder aux [paramètres du compte](../fr/account_settings.html), changer la langue de l'interface ou vous déconnecter de votre compte.

<p class="note">
  <strong>Note :</strong> Depuis n'importe quelle page de votre compte KoboToolbox, cliquez sur <i class="k-icon-help"></i> <strong>Aide</strong> pour accéder rapidement au Centre d'aide, au Forum communautaire, à la KoboToolbox Academy et pour consulter les notifications dans l'application. Cliquez sur <i class="k-icon-logo-github"></i> <strong>Source</strong> pour accéder au code source de KoboToolbox.
</p>

![Projects](images/kobotoolbox_interface/projects.png)


## Travailler dans un projet
Pour ouvrir un projet, cliquez sur son nom dans le tableau **Mes Projets**. Chaque projet contient quatre pages principales : **SOMMAIRE**, **FORMULAIRE**, **DONNÉES** et **PARAMÈTRES**.

### Page SOMMAIRE
La page **SOMMAIRE** fournit un aperçu de votre projet, notamment :
* Les **informations sur le projet** telles que la description, le statut, le propriétaire, ainsi que les dates de dernière modification et de déploiement.
* Les **statistiques de soumissions** pour les sept derniers jours, 31 jours, trois mois, 12 mois, ainsi que le nombre total de soumissions.
* Des **liens rapides** vers les fonctionnalités clés du projet (par exemple, modifier ou prévisualiser le formulaire).
* Les **droits d'accès** et les utilisateurs avec lesquels le projet est partagé.

![Summary](images/kobotoolbox_interface/summary.png)

### Page FORMULAIRE
La page **FORMULAIRE** contient les outils permettant de créer, mettre à jour et déployer votre projet. Elle est divisée en plusieurs sections.

Dans la section **Version actuelle**, vous pouvez :
* <i class="k-icon-view"></i> **Prévisualiser** la version actuelle du formulaire.
* <i class="k-icon-edit"></i> **Modifier** le formulaire dans l'[interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**](../fr/formbuilder.html).
* <i class="k-icon-replace"></i> **Remplacer** le formulaire par un [XLSForm](../fr/getting_started_xlsform.html) ou un [modèle](../fr/question_library.html).
* Ouvrir le menu <i class="k-icon-more"></i> **Plus d'actions** pour télécharger le fichier XLSForm ou XML, [Droits d'accès au niveau de l'utilisateur](../fr/managing_permissions.html), cloner le projet ou créer un modèle.
* <i class="k-icon-language"></i> **Gérer les traductions** pour les formulaires en [plusieurs langues](../fr/language_dashboard.html).
* **DÉPLOYER** ou **REDÉPLOYER** le formulaire.

<p class="note">
  <strong>Note :</strong> Cloner un projet copie uniquement le formulaire. Les soumissions, les fichiers multimédias joints, les droits d'accès, les liaisons dynamiques de projets et les autres paramètres du projet ne sont pas copiés.
</p>


Dans la section **Historique du formulaire**, vous pouvez :
* Consulter chaque version déployée du formulaire et les modifications non déployées, ainsi que la date de dernière modification.
* Cloner des versions ou des modifications antérieures du formulaire.

Dans la section **Collecte de données**, vous pouvez :
* Choisir un [mode de collecte de données](../fr/data_through_webforms.html#data-collection-modes).
* Cliquer sur **Copier** pour copier le lien ou sur **Ouvrir** pour ouvrir le formulaire dans votre navigateur.
* Autoriser les soumissions [sans nom d'utilisateur ni mot de passe](../fr/project_sharing_settings.html#allowing-submissions-without-authentication).

![Form](images/kobotoolbox_interface/form.png)

### Page DONNÉES
La page **DONNÉES** donne accès à toutes les données collectées et comprend un <i class="k-icon-table"></i> **Tableau** de données, des <i class="k-icon-reports"></i> **Rapports** personnalisés, une <i class="k-icon-gallery"></i> **Galerie** photo, un onglet <i class="k-icon-download"></i> **Téléchargements** pour exporter les données, et un mode <i class="k-icon-map-view"></i> **Carte** pour les données GPS.

<p class="note">
  Pour en savoir plus sur la gestion de vos données dans KoboToolbox, consultez les articles <a href="../fr/viewing_validating_data.html">Voir et valider vos données</a> et <a href="../fr/editing_deleting_data.html">Modifier et supprimer vos données</a>.
</p>

![Data](images/kobotoolbox_interface/data.png)


### Page PARAMÈTRES
La page **PARAMÈTRES** contient les options de configuration de votre projet. Elle est divisée en plusieurs onglets :
* <i class="k-icon-settings"></i> **Généralités :** Mettez à jour le nom et la description du projet, [archivez](../fr/managing_projects.html#archiving-and-deleting-projects) ou supprimez le projet.
* <i class="k-icon-gallery"></i> **Médias :** Importez et gérez les [fichiers multimédias du projet](../fr/upload_media.html).
* <i class="k-icon-user-share"></i> **Partage :** Mettez à jour les [Droits d'accès au niveau de l'utilisateur](../fr/managing_permissions.html) pour les autres utilisateurs.
* <i class="k-icon-attach"></i> **Connecter des Projets :** Configurez des connexions pour les [liaisons dynamiques de projets](../fr/dynamic_data_attachment_formbuilder.html).
* <i class="k-icon-data-sync"></i> **Services REST :** Configurez les [services web REST](../fr/rest_services.html) pour envoyer automatiquement les soumissions vers des applications tierces.
* <i class="k-icon-document"></i> **Activité :** Consultez et exportez les [suivis de l'historique du projet](../fr/activity_logs.html#project-history-logs), y compris les modifications apportées par d'autres utilisateurs.

![Settings](images/kobotoolbox_interface/settings.png)

<p class="note">
  Pour en savoir plus sur la gestion de projets, consultez l'article <a href="../fr/managing_projects.html">Gestion de projets dans KoboToolbox</a>.
</p>