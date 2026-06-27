# Créer un XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/getting_started_xlsform.md" class="reference">23 avr. 2026</a>

<iframe src="https://www.youtube.com/embed/xpeBCy9p1Ys?si=tP_3G2vMnRC1OgWS&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Lorsque vous créez des formulaires d'enquête avec KoboToolbox, vous pouvez construire votre formulaire avec l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** ou en utilisant XLSForm. XLSForm est très efficace pour créer des formulaires de base et avancés dans un format facile à utiliser.

<p class="note">
  Pour plus d'informations sur XLSForm, consultez l'article <a class="reference" href="../fr/edit_forms_excel.html">Introduction à XLSForm</a>. Pour une introduction complète au développement de formulaires avec XLSForm, nous vous recommandons le cours en ligne en autonomie <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

Cet article explique comment configurer un XLSForm à l'aide de Microsoft Excel ou d'autres logiciels de tableur, notamment :

- Configurer la structure de base de votre XLSForm
- Ajouter des questions et des choix de réponse
- Ajouter des paramètres de formulaire et des colonnes optionnelles
- Importer et prévisualiser votre XLSForm dans KoboToolbox

<p class="note">
  <b>Note :</b> Certaines fonctionnalités XLSForm ne sont pas actuellement disponibles dans le Formbuilder, mais les formulaires KoboToolbox peuvent être téléchargés, modifiés dans XLSForm et <a class="reference" href="../fr/xlsform_with_kobotoolbox.html">importés à nouveau dans KoboToolbox</a>.
</p>

## Configurer un XLSForm

Pour configurer la structure de base d'un XLSForm :

1. Ouvrez un nouveau tableur dans votre logiciel de tableur préféré.
2. Créez trois onglets : `survey`, `choices` et `settings`.
   - Les noms des onglets doivent être en lettres minuscules.
3. Dans l'**onglet survey**, créez trois colonnes avec les en-têtes : `type`, `name` et `label`.
4. Dans l'**onglet choices**, créez trois colonnes avec les en-têtes : `list_name`, `name` et `label`.
5. L'**onglet settings** est optionnel. Il peut être utilisé pour inclure des spécifications et des personnalisations supplémentaires du formulaire.
   - Par exemple : `form_title`, `style` et `default_language`.

<p class="note">
Pour commencer avec XLSForm, téléchargez un XLSForm type <a class="reference" href="https://support.kobotoolbox.org/_static/files/getting_started_xlsform/sample_xlsform.xlsx">ici</a>.
</p>

### Colonnes obligatoires dans XLSForm

Les colonnes suivantes sont obligatoires dans XLSForm :

**onglet survey**

| Nom de colonne | Description |
| --- | --- |
| `type` | Définit le type de question (par exemple, text, integer, select_one) |
| `name` | Définit un nom court et unique pour identifier chaque question |
| `label` | Définit le texte de la question tel qu'il sera affiché dans le formulaire |

**onglet choices**

| Nom de colonne | Description |
| --- | --- |
| `list_name` | Définit l'identifiant unique d'une liste de choix de réponse |
| `name` | Définit un nom court et unique pour identifier chaque choix de réponse |
| `label` | Définit le texte du choix tel qu'il sera affiché dans le formulaire |

## Ajouter des questions

Dans XLSForm, les questions sont ajoutées dans l'**onglet survey**. Pour ajouter des questions dans XLSForm :

1. Dans la colonne `type` de l'**onglet survey**, saisissez le [type de question](../fr/question_types_xls.html) de la question que vous souhaitez ajouter.
2. Dans la colonne `name`, saisissez un nom utilisé pour identifier la question.
   - Chaque question doit avoir un nom unique et ne peut pas contenir d'espaces ou de symboles (sauf les tirets bas).
3. Dans la colonne `label`, saisissez le texte de la question tel qu'il doit être affiché dans le formulaire lors de la collecte de données.

**onglet survey**

| type | name | label |
| :--- | :--- | :--- |
| text | yourname | Quel est votre nom ? |
| survey |

4. Si vous ajoutez des **questions à choix multiple** (`select_one`, `select_multiple` ou `rank`) : dans la colonne `type`, après le type de question, ajoutez un espace et saisissez le nom de la liste de choix.
   - Le nom de la liste de choix est ensuite défini dans l'**onglet choices** comme `list_name`.

**onglet survey**

| type | name | label |
| :--- | :--- | :--- |
| select_one sex | baby_sex | Quel est le sexe de votre bébé ? |
| survey |

<p class="note">
Pour en savoir plus sur les types de questions dans XLSForm, consultez l'article <a class="reference" href="../fr/question_types_xls.html">Types de questions dans XLSForm</a>.
</p>

## Ajouter des choix de réponse

Pour les questions à choix multiple, les choix de réponse sont ajoutés dans l'**onglet choices**. Pour ajouter des choix de réponse dans XLSForm :

1. Dans la colonne `list_name` de l'**onglet choices**, saisissez le nom de la **liste de choix de réponse**.
   - Le `list_name` est un identifiant unique pour une liste de choix de réponse. Il doit correspondre au nom de liste saisi dans la colonne `type` de l'**onglet survey**.
2. Dans la colonne `name`, ajoutez un nom court pour chaque choix de réponse.
   - Chaque choix au sein d'une liste doit avoir un `name` unique, qui ne peut pas contenir d'espaces ou de symboles (sauf les tirets bas).
3. Dans la colonne `label`, saisissez le texte du choix tel qu'il doit être affiché dans le formulaire lors de la collecte de données.

**onglet choices**

| list_name | name | label |
| :--- | :--- | :--- |
| sex | male | Homme |
| sex | female | Femme |
| choices |

<p class="note">
Pour en savoir plus sur la gestion des choix de réponse dans XLSForm, consultez l'article <a class="reference" href="../fr/option_choices_xls.html">Gérer les choix de réponse dans XLSForm</a>.
</p>

## Ajouter des paramètres

Il existe de nombreux paramètres optionnels qui peuvent être ajoutés à l'**onglet settings** dans XLSForm.

Les paramètres de formulaire courants incluent :

| Paramètre | Description |
| --- | --- |
| `form_title` | Titre affiché en haut du formulaire |
| `default_language` | Langue par défaut du formulaire |
| `style` | Thèmes pour les formulaires web |
| `version` | Identifiant de version du formulaire |

Par exemple, pour ajouter un titre de formulaire :

1. Ajoutez une colonne dans l'**onglet settings** nommée `form_title`.
2. Saisissez le titre du formulaire dans la colonne `form_title`.

<p class="note">
<b>Note :</b> Tous les paramètres de formulaire sont optionnels. Si vous ne définissez pas de titre de formulaire dans votre XLSForm, le nom du fichier Excel sera utilisé comme nom de projet dans KoboToolbox par défaut. Cela peut être modifié dans KoboToolbox.
</p>

**onglet settings**

| form_title |
| :--- |
| Créer un <br> XLSForm |
| settings |

<p class="note">
Pour en savoir plus sur l'onglet settings dans XLSForm, consultez l'article <a class="reference" href="../fr/form_settings_xls.html">Paramètres de formulaires dans XLSForm</a>.
</p>

## Ajouter des colonnes optionnelles à l'onglet survey

Pour personnaliser davantage votre XLSForm, vous pouvez ajouter des colonnes optionnelles pour configurer la logique de formulaire, les options de questions et les paramètres avancés. Les colonnes optionnelles courantes incluent :

| Nom de colonne | Description |
| --- | --- |
| `hint` | Indice de question |
| `guidance_hint` | Instructions supplémentaires (guidance hint) |
| `required` | Rend une question obligatoire |
| `relevant` | Conditions de logique de saut pour la question |
| `constraint` | Critères de validation pour la question |
| `constraint_message` | Message d'erreur lorsque les critères de validation ne sont pas respectés |
| `appearance` | Options pour l'affichage des questions |
| `choice_filter` | Critères pour la sélection en cascade |
| `parameters` | Paramètres pour des types de questions spécifiques |
| `calculation` | Expression mathématique pour une question `calculate` |
| `default` | Réponse par défaut pour une question |

<p class="note">
Pour en savoir plus sur les colonnes optionnelles dans XLSForm, consultez les articles <a class="reference" href="../fr/question_options_xls.html">Options de questions dans XLSForm</a>, <a class="reference" href="../fr/appearances_xls.html">Apparences de questions dans XLSForm</a> et <a class="reference" href="../fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Importer et prévisualiser votre XLSForm dans KoboToolbox

Une fois que vous avez terminé de développer votre XLSForm, vous pouvez l'importer et le prévisualiser dans KoboToolbox :

1. Accédez à la page d'accueil **Projets** dans KoboToolbox et cliquez sur **NOUVEAU**.
2. Sélectionnez **Importer un XLSForm** et importez votre fichier XLSForm.
3. Saisissez les détails du projet et cliquez sur **CRÉER LE PROJET**.
4. Cliquez sur le bouton <i class="k-icon k-icon-view"></i> **Aperçu**.

Si votre XLSForm contient une erreur, un message d'erreur apparaîtra, indiquant généralement la ligne, la question ou l'expression exacte où se trouve le problème. Après avoir corrigé l'erreur dans votre XLSForm, vous devrez importer à nouveau le fichier.

<p class="note">
Pour savoir comment télécharger un XLSForm depuis KoboToolbox, importer votre XLSForm via une URL et utiliser KoboToolbox pour valider et tester votre XLSForm, consultez l'article <a class="reference" href="../fr/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>.
</p>