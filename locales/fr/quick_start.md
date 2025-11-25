# Guide de démarrage rapide
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/72921cfe4ac9cd4ad75c1d57664c89478f26c71a/source/quick_start.md" class="reference">30 Sep 2025</a>

Cet article fournit un guide rapide pour débuter avec KoboToolbox. Il explique comment créer un compte, construire et déployer un formulaire, et commencer à collecter des données.

<iframe src="https://www.youtube.com/embed/CYJ-Ob_7Ql8?si=SDjFjZF4zQBE-thP" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



## Créer un compte et se connecter
Pour commencer, rendez-vous sur la [page d'inscription](https://www.kobotoolbox.org/sign-up/) et créez un compte sur l'un de nos serveurs publics. La plupart des utilisatrices et utilisateurs s'inscrivent sur Le serveur KoboToolbox mondial [Global KoboToolbox Server](https://kf.kobotoolbox.org/). Les utilisatrices et utilisateurs ainsi que les organisations qui nécessitent ou préfèrent l'hébergement des données dans l'Union européenne peuvent s'inscrire sur Le serveur KoboToolbox Union européenne [European Union KoboToolbox Server](https://eu.kobotoolbox.org/).

Activez votre compte en utilisant le lien envoyé par e-mail, puis connectez-vous via l'URL du serveur ou la [page d'inscription](https://www.kobotoolbox.org/sign-up/). 

<p class="note">
    Pour plus d'informations sur la création d'un compte, consultez <a href="https://support.kobotoolbox.org/creating_account.html">Créer un compte sur KoboToolbox</a>.
</p>


## Créer votre premier projet

Pour créer votre premier formulaire :
1. Cliquez sur **NOUVEAU**. Vous serez invité à choisir une source de projet.

| Option                    | Description                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| Création de formulaires        | Construisez un formulaire en utilisant l'interface de création de formulaires KoboToolbox <a href="formbuilder.html" class="reference">(KoboToolbox Formbuilder)</a>.                   |
| Utiliser un modèle            | Construisez un formulaire en utilisant un modèle de <a href="question_library.html" class="reference">La bibliothèque de questions</a>.   |
| Importer un XLSForm            | Importez un fichier <a href="edit_forms_excel.html" class="reference">XLSForm</a> dans lequel vous avez défini vos questions.     |
| Importer un XLSForm via une URL | Importez un fichier XLSForm <a href="xls_url.html" class="reference">depuis une source en ligne</a> telle que Google Drive ou Dropbox. |


2. Sélectionnez **Création de formulaires** pour créer un nouveau formulaire en utilisant l'interface de création de formulaires KoboToolbox.
3. Dans la boîte de dialogue **Détails du projet**, saisissez les informations pertinentes concernant votre projet, puis cliquez sur **CRÉER UN PROJET**.

## Construire un formulaire en utilisant l'interface de création de formulaires

1. Une fois dans l'interface de création de formulaires, cliquez sur le bouton <i class="k-icon-plus"></i> pour ajouter votre première question. Saisissez le libellé de la question et choisissez un [type de question](question_types.md).
2. Pour spécifier les paramètres de la question, cliquez sur l'icône <i class="k-icon-settings"></i> **Paramètres**. Par exemple, vous pouvez rendre une question obligatoire, modifier son apparence ou ajouter des conditions de [logique de saut](skip_logic.md).
3. Cliquez sur <i class="k-icon-view"></i> **Aperçu du formulaire** pour visualiser et tester votre formulaire.
4. Pour enregistrer le formulaire, cliquez sur **Enregistrer** dans le coin supérieur droit, puis cliquez sur <i class="k-icon-close"></i> pour fermer le formulaire.

<p class="note">
    Pour en savoir plus sur l'utilisation de l'interface de création de formulaires, consultez <a href="https://support.kobotoolbox.org/formbuilder.html">Débuter avec l'interface de création de formulaires KoboToolbox</a> et <a href="https://support.kobotoolbox.org/question_options.html">Utiliser les options de question</a>.
</p>


## Déployer votre formulaire pour la collecte de données

1. Pour commencer à collecter des données, cliquez sur **DÉPLOYER** dans la page **FORMULAIRE** pour [déployer votre formulaire Brouillon](deploy_form_new_project.md) en tant que nouveau projet de collecte de données.
2. Sous **Collecter des données**, cliquez sur **Copier** pour partager le lien du formulaire pour la saisie de données [depuis un navigateur](data_through_webforms.md) sur n'importe quel appareil (ordinateur, iPhone, Android).
3. Alternativement, téléchargez et configurez l'application Android [KoboCollect](kobocollect_on_android_latest.md) pour la collecte de données mobile.


<p class="note">
    <strong>Remarque :</strong> Pour <a href="project_sharing_settings.html">partager votre formulaire</a> avec toute personne disposant de l'URL du formulaire, activez « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe » dans la page <strong>FORMULAIRE</strong>, sous <strong>Collecter des données</strong>.
</p>


Une fois que vous avez collecté des données, vous pouvez les visualiser, les modifier et les télécharger depuis la page **DONNÉES** de votre projet. Pour en savoir plus sur la gestion de vos données, consultez la section d'assistance [Gestion des projets et des données](https://support.kobotoolbox.org/managing-projects.html).