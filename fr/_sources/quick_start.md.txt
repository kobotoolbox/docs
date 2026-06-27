# Guide de démarrage rapide
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/5224e960558832c7d31889fafa6cdfba84b58126/source/quick_start.md" class="reference">23 mars 2026</a>

<iframe src="https://www.youtube.com/embed/CYJ-Ob_7Ql8?si=SDjFjZF4zQBE-thP&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Cet article fournit un guide rapide pour débuter avec KoboToolbox. Il explique comment créer un compte, construire et déployer un formulaire, et commencer à collecter des données.


<p class="note">
    Pour une introduction complète au développement de formulaires avec KoboToolbox, nous recommandons le <a href="https://academy.kobotoolbox.org/courses/initiation">Cours d'initiation à KoboToolbox</a> en ligne en autonomie de la KoboToolbox Academy.
</p>


## Créer un compte et se connecter
Pour commencer, rendez-vous sur la [page d'inscription](https://www.kobotoolbox.org/sign-up/) et créez un compte sur l'un de nos serveurs publics. La plupart des utilisateurs s'inscrivent sur notre [serveur KoboToolbox mondial](https://kf.kobotoolbox.org/). Les utilisateurs et organisations qui nécessitent ou préfèrent l'hébergement de données dans l'Union européenne peuvent s'inscrire sur le [serveur KoboToolbox Union européenne](https://eu.kobotoolbox.org/).

Activez votre compte en utilisant le lien envoyé par email, puis connectez-vous via l'URL du serveur ou la [page d'inscription](https://www.kobotoolbox.org/sign-up/).

<p class="note">
    Pour plus d'informations sur la création d'un compte, consultez l'article <a href="creating_account.html">Créer un compte KoboToolbox</a>.
</p>


## Créer votre premier projet

Pour créer votre premier formulaire :
1. Cliquez sur **NOUVEAU**. Vous serez invité à choisir une source de projet.

| Option                    | Description                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| Création de formulaires        | Créez un formulaire en utilisant l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**.                   |
| Utiliser un modèle            | Créez un formulaire en utilisant un modèle de la <a href="question_library.html" class="reference">bibliothèque de questions</a>.   |
| Importer un XLSForm            | Importez un fichier <a href="edit_forms_excel.html" class="reference">XLSForm</a> dans lequel vous avez défini vos questions.     |
| Importer un XLSForm via URL | Importez un fichier XLSForm <a href="xlsform_with_kobotoolbox.html#importing-an-xlsform-via-url" class="reference">depuis une source en ligne</a> telle que Google Drive ou Dropbox. |


2. Sélectionnez **Création de formulaires** pour créer un nouveau formulaire en utilisant le Formbuilder de KoboToolbox.
3. Dans la boîte de dialogue **Informations sur le projet**, saisissez les informations pertinentes sur votre projet, puis cliquez sur **CRÉER LE PROJET**.

## Créer un formulaire avec le Formbuilder

1. Une fois dans le Formbuilder, cliquez sur le bouton <i class="k-icon-plus"></i> pour ajouter votre première question. Saisissez le libellé de la question et choisissez un [type de question](question_types.md).
2. Pour spécifier les paramètres de la question, cliquez sur l'icône <i class="k-icon-settings"></i> **Paramètres**. Par exemple, vous pouvez rendre une question obligatoire, modifier son apparence ou ajouter des conditions de [branchement conditionnel](skip_logic.md).
3. Cliquez sur <i class="k-icon-view"></i> **Aperçu du formulaire** pour visualiser et tester votre formulaire.
4. Pour sauvegarder le formulaire, cliquez sur **Sauvegarder** en haut à droite, puis cliquez sur <i class="k-icon-close"></i> pour fermer le formulaire.

<p class="note">
    Pour en savoir plus sur l'utilisation du Formbuilder, consultez les articles <a href="formbuilder.html">Découvrir l'interface de création de formulaires</a> et <a href="question_options.html">Options de questions dans le Formbuilder</a>.
</p>


## Déployer votre formulaire pour la collecte de données

1. Pour commencer à collecter des données, cliquez sur **DÉPLOYER** dans la page **FORMULAIRE** pour [déployer votre brouillon de formulaire](deploy_form_new_project.md) en tant que nouveau projet de collecte de données.
2. Sous **Collecter des données**, cliquez sur **Copier** pour partager le lien du formulaire pour la saisie de données [depuis un navigateur](data_through_webforms.md) sur n'importe quel appareil (ordinateur, iPhone, Android).
3. Alternativement, téléchargez et configurez l'application Android [KoboCollect](kobocollect_on_android_latest.md) pour la collecte de données mobile.


<p class="note">
    <strong>Note :</strong> Pour <a href="project_sharing_settings.html">partager votre formulaire</a> avec toute personne disposant de l'URL du formulaire, activez « Autoriser les soumissions sans nom d'utilisateur ni mot de passe pour ce formulaire » dans la page <strong>FORMULAIRE</strong>, sous <strong>Collecter des données</strong>.
</p>


Une fois que vous avez collecté des données, vous pouvez les visualiser, les modifier et les télécharger depuis la page **DONNÉES** de votre projet. Pour en savoir plus sur la gestion de vos données, consultez l'article [Gestion de projets dans KoboToolbox](managing_projects.html).