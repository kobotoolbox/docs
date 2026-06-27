# Gestion de projets dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/d66c12822969e6fa3db776489f574522bf03eebb/source/managing_projects.md" class="reference">19 fév. 2026</a>

Un **projet** dans KoboToolbox correspond à un formulaire, ses paramètres et toutes les données soumises à ce formulaire. La gestion des projets commence sur la **page d'accueil Projets**, où vous pouvez visualiser, trier, filtrer et organiser vos projets. Vous pouvez également créer de nouveaux projets, mettre à jour des projets existants et gérer la façon dont ils sont partagés avec vos collaborateurs.

Cet article explique comment visualiser et gérer des projets, créer de nouveaux projets, travailler avec les paramètres et les données d'un projet, et archiver ou supprimer des projets qui ne sont plus utilisés.

## Aperçu des projets existants
La **page d'accueil Projets** répertorie tous les projets que vous possédez ou qui ont été partagés avec vous. Le tableau **Mes Projets** affiche des informations clés telles que le nom du projet, le propriétaire, le statut et le nombre de soumissions.

Les projets existent dans trois états :
* **Déployés :** Projets qui ont été publiés et sont prêts pour la collecte de données, permettant aux utilisateurs d'ouvrir le formulaire et de soumettre des réponses.
* **Brouillons :** Projets qui sont encore en cours de développement ou de modification et qui ne sont pas encore déployés, et ne peuvent donc pas recevoir de soumissions.
* **Archivés :** Projets qui ont été retirés de la liste des projets actifs et n'acceptent plus de nouvelles soumissions, mais sont conservés à titre de référence ou pour la tenue de registres.

Vous pouvez gérer vos projets à l'aide des outils disponibles sur cette page :
* **Filtrer :** Cliquez sur <i class="k-icon-filter"></i> **filter** pour filtrer les projets par nom, description, statut, propriétaire, date de dernière modification, date de dernière modification, date de dernier déploiement, secteur, pays et langues.
* **Sélectionner les champs :** Cliquez sur <i class="k-icon-spreadsheet"></i> **fields** pour choisir les champs affichés dans le tableau **Mes Projets**.
* **Trier :** Cliquez sur un en-tête de colonne pour trier selon ce champ.
* **Plus d'actions :** Cochez la case à côté d'un projet pour effectuer une action sur celui-ci.
    * En haut à droite, vous pouvez <i class="k-icon-archived"></i> **archiver** un projet ou mettre à jour ses <i class="k-icon-user-share"></i> **droits d'accès**.
    * Vous pouvez également <i class="k-icon-trash"></i> **supprimer** plusieurs projets à la fois.

![Projects](images/kobotoolbox_interface/projects.png)

## Créer un projet
Pour créer un nouveau projet dans KoboToolbox :
1. Cliquez sur **NEW** depuis la **page d'accueil Projets**.
2. Choisissez l'une des options suivantes :
    - <i class="k-icon-edit"></i> **Build from scratch** pour créer un formulaire à l'aide de l'[interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**](https://support.kobotoolbox.org/fr/formbuilder.html).
    - <i class="k-icon-template"></i> **Use a template** pour sélectionner un modèle de formulaire depuis la [bibliothèque de questions](https://support.kobotoolbox.org/fr/question_library.html).
    - <i class="k-icon-upload"></i> **Upload an XLSForm** pour importer un [XLSForm](https://support.kobotoolbox.org/fr/getting_started_xlsform.html) existant.
    - <i class="k-icon-link"></i> **Import an XLSForm via URL** pour créer un lien vers un XLSForm [hébergé en ligne](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#importing-an-xlsform-via-url).
3. Créez, testez et prévisualisez votre formulaire.
4. Cliquez sur **DEPLOY** depuis la page **FORM** de votre projet pour mettre le formulaire en ligne pour la collecte de données.

![Create](images/managing_projects/create.png)

## Gérer un projet existant
Lorsque vous ouvrez un projet, vous pouvez le gérer via les onglets en haut de la page :
* **SUMMARY :** Aperçu des métadonnées du projet et des soumissions.
* **FORM :** Modifier le formulaire, déployer les modifications et copier le lien du formulaire.
* **DATA :** Visualiser les données soumises dans différents formats, générer des rapports et exporter des données.
* **SETTINGS :** Mettre à jour les paramètres du projet, notamment les [Droits d'accès au niveau de l'utilisateur](https://support.kobotoolbox.org/fr/managing_permissions.html), les [médias au sein du formulaire](https://support.kobotoolbox.org/fr/upload_media.html) et la configuration générale.

<p class="note">
  Pour en savoir plus sur la gestion de vos données dans KoboToolbox, consultez les articles <a href="https://support.kobotoolbox.org/fr/viewing_validating_data.html">Voir et valider vos données</a> et <a href="https://support.kobotoolbox.org/fr/editing_deleting_data.html">Modifier et supprimer vos données</a>.
</p>


## Archiver et supprimer des projets
Lorsque des projets deviennent obsolètes ou ne sont plus nécessaires, vous pouvez les retirer de l'utilisation active en les **archivant** ou en les **supprimant**. L'archivage empêche de nouvelles soumissions tout en conservant le formulaire et les données existantes. La suppression retire définitivement le projet et toutes ses données de votre compte.

<p class="note">
  <strong>Remarque :</strong> Les projets supprimés ne pouvant pas être récupérés, ne supprimez un projet que lorsque vous êtes certain que ni le formulaire ni ses données ne seront nécessaires. Avant de supprimer un projet, nous vous recommandons de <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox">télécharger le formulaire</a> en tant que XLSForm et d'<a href="https://support.kobotoolbox.org/fr/export_download.html">exporter</a> toutes les données du projet.
</p>

### Archiver des projets
L'archivage est recommandé pour les formulaires qui ne doivent plus accepter de soumissions mais qui doivent rester disponibles à titre de référence.

Il existe deux façons d'archiver un projet. Pour archiver un projet depuis la **page d'accueil Projets** :
1. Sur la **page d'accueil Projets**, cochez la case du projet.
2. Cliquez sur <i class="k-icon-archived"></i> **Archive project** en haut à droite.
3. Il vous sera demandé de confirmer que votre formulaire n'acceptera pas de soumissions tant qu'il est archivé. Cliquez sur **ARCHIVE** pour confirmer.

![Archive](images/managing_projects/archive_home.png)

Pour archiver un projet depuis la page **SETTINGS** du projet :
1. Ouvrez le projet et accédez à la page **SETTINGS**.
2. Dans l'onglet <i class="k-icon-settings"></i> **General**, cliquez sur **Archive Project**.
3. Il vous sera demandé de confirmer que votre formulaire n'acceptera pas de soumissions tant qu'il est archivé. Cliquez sur **ARCHIVE** pour confirmer.

![Archive](images/managing_projects/archive_settings.png)

Pour désarchiver un projet, suivez les mêmes étapes et cliquez sur **Unarchive Project**.

### Supprimer des projets
La suppression d'un projet retire définitivement le formulaire et toutes les données associées. Cette action est irréversible.

Il existe deux façons de supprimer un projet. Pour supprimer un projet depuis la **page d'accueil Projets** :
1. Sur la **page d'accueil Projets**, cochez la case à côté du projet.
2. Cliquez sur <i class="k-icon-trash"></i> **Delete 1 project** dans le coin supérieur droit.
3. Une boîte de dialogue de confirmation vous demandera d'accepter les points suivants :
    * Vous êtes en train de supprimer définitivement ce formulaire.
    * Toutes les données recueillies pour ce formulaire seront supprimées.
    * Le formulaire associé à ce projet sera supprimé.

![Delete](images/managing_projects/delete_home.png)

Pour supprimer un projet depuis la page **SETTINGS** du projet :
1. Ouvrez le projet et accédez à la page **SETTINGS**.
2. Dans l'onglet <i class="k-icon-settings"></i> **General**, cliquez sur **Delete Project and Data**.
3. Une boîte de dialogue de confirmation vous demandera d'accepter les points suivants :
    * Vous êtes en train de supprimer définitivement ce formulaire.
    * Toutes les données recueillies pour ce formulaire seront supprimées.
    * Le formulaire associé à ce projet sera supprimé.

![Delete](images/managing_projects/delete_settings.png)