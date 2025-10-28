# Débuter avec XLSForm
<a href="../getting_started_xlsform.html">Read in English</a> | <a href="../es/getting_started_xlsform.html">Leer en español</a> | <a href="../ar/getting_started_xlsform.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/8d0c50778ae17aa78829bafa85b7bf16ef00c45c/source/getting_started_xlsform.md" class="reference">10 juin 2025</a>

Lorsque vous créez des formulaires d'enquête pour KoboToolbox, vous pouvez construire votre formulaire avec l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder) ou en XLSForm. XLSForm est très efficace pour créer des formulaires de base et avancés dans un format facile à utiliser.

Cet article explique comment :

-   Configurer un XLSForm en utilisant Microsoft Excel
-   Importer et prévisualiser un XLSForm dans KoboToolbox
-   Télécharger un formulaire créé avec l'interface de création de formulaires KoboToolbox en tant qu'XLSForm

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_xlsform_v2.mp4"
    type="video/mp4"
  />
</video>

<br/>

<p class="note">
  <b>Remarque :</b> Certaines fonctionnalités XLSForm ne sont actuellement pas disponibles dans l'interface de création de formulaires, mais elles peuvent être utilisées pour la construction de formulaires en XLSForm puis importées dans KoboToolbox. Cela peut être particulièrement utile pour les formulaires complexes.
</p>

## Qu'est-ce que XLSForm

XLSForm est un format standardisé pour développer des formulaires en utilisant Microsoft Excel et d'autres logiciels de tableur. Les XLSForms peuvent ensuite être importés dans KoboToolbox pour générer un formulaire de collecte de données.

Il existe de nombreux avantages à utiliser XLSForm, en particulier pour construire des formulaires complexes avec des fonctionnalités plus avancées, notamment les conditions de pertinence, les calculs et les contraintes. XLSForm vous permet également de collaborer sur la construction de formulaires en utilisant le même fichier Excel ou en temps réel en utilisant Google Sheets.

<p class="note">
  <b>Remarque :</b> Pour une introduction complète au développement de formulaires en utilisant XLSForm, nous recommandons le <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">Cours XLSForm Fundamentals</a> en ligne à votre rythme de KoboToolbox Academy.
</p>

## Configurer un XLSForm

Pour configurer la structure de base d'un XLSForm :

1. Créez un classeur dans Microsoft Excel ou Google Sheets.
2. Créez trois feuilles de calcul : **survey**, **choices** et **settings**.
   - Les noms des feuilles de calcul doivent être en lettres minuscules.
3. Dans la feuille de calcul **survey**, créez trois colonnes avec les en-têtes : `type`,
   `name` et `label`.
4. Dans la feuille de calcul **choices**, créez trois colonnes avec les en-têtes :
   `list_name`, `name` et `label`.
5. La feuille de calcul **settings** est facultative. Elle peut être utilisée pour inclure des spécifications et des personnalisations de formulaire supplémentaires.
   - Par exemple : `form_title`, `style` et `default_language`.

### Colonnes obligatoires dans XLSForm

#### Feuille de calcul survey

| Nom de colonne | Description |
| :--- | :--- |
| type | Définit le type de question (par exemple, text, integer, select_one) |
| name | Définit un nom court et unique pour faire référence à chaque question |
| label | Définit le texte de la question tel qu'il sera affiché dans le formulaire |

#### Feuille de calcul choices

| Nom de colonne | Description |
| :--- | :--- |
| list_name | Définit l'identifiant unique pour une liste d'options de choix |
| name | Définit un nom court et unique pour faire référence à chaque option de choix |
| label | Définit le texte du choix tel qu'il sera affiché dans le formulaire |

## Ajouter des questions

Dans XLSForm, les questions sont ajoutées dans la feuille de calcul **survey**. Le processus étape par étape ci-dessous explique comment ajouter les exemples de questions suivants : **Quel est votre nom ?**, **Quel est le sexe de votre bébé ?** et **Quel âge avez-vous ?**

1. Dans la colonne `type` de la feuille de calcul survey, tapez **text**. C'est le type de question pour la première question, **Quel est votre nom ?**
2. Dans la colonne `name`, tapez **yourname**. Ce sera le nom unique utilisé pour identifier la première question. Chaque question doit avoir un nom unique et ne peut pas contenir d'espaces ou de symboles (sauf le trait de soulignement).
3. Dans la colonne `label`, tapez **Quel est votre nom ?**. Cette étiquette sera affichée comme texte de question sur le formulaire pendant la collecte de données.

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | Quel est votre nom ? |
| survey |

4. Pour la deuxième question, **Quel est le sexe de votre bébé ?**, entrez **select_one sex** dans la colonne `type` de la feuille de calcul survey.
   - **select_one** est le type de question qui permet aux utilisatrices et utilisateurs de sélectionner un seul choix parmi une liste d'options de réponse.
   - **sex** est le nom de la liste d'options de réponse, qui est défini dans la feuille de calcul choices (voir [Ajouter des options de réponse](https://support.kobotoolbox.org/getting_started_xlsform.html#adding-response-choices)).
5. Dans la colonne `name`, tapez **baby_sex**.
6. Dans la colonne `label`, tapez **Quel est le sexe de votre bébé ?**

| type           | name     | label                    |
| :------------- | :------- | :----------------------- |
| select_one sex | baby_sex | Quel est le sexe de votre bébé ? |
| survey |


7. Pour la question **Quel âge avez-vous ?**, suivez le même processus en utilisant **integer** comme type de question dans la colonne `type`.

| type    | name | label            |
| :------ | :--- | :--------------- |
| integer | age  | Quel âge avez-vous ? |
| survey |

<p class="note">
  <b>Remarque :</b> Pour en savoir plus sur les types de questions dans XLSForm, consultez <a class="reference external" href="https://xlsform.org/en/#question-types">Question types (XLSForm.org)</a>.
</p>

## Ajouter des options de réponse

Pour les questions de type select (**select_one** et **select_multiple**), les options de choix de réponse sont ajoutées dans la feuille de calcul **choices**. Le processus étape par étape ci-dessous explique comment ajouter les choix pour l'exemple de question : **Quel est le sexe de votre bébé ?**

1. Dans la colonne `list_name` de la feuille de calcul choices, entrez le list_name **sex**.
   - C'est le list_name précédemment défini pour la question **baby_sex** dans la feuille de calcul survey.
   - Le list_name est l'identifiant unique pour la liste d'options de choix de réponse.
2. Dans la colonne name, ajoutez le nom de choix **male**.
   - Le nom de choix est l'identifiant unique pour chaque option de choix.
3. Dans la colonne label, entrez l'étiquette de choix **Masculin**.
   - L'étiquette de choix est affichée sur le formulaire pendant la collecte de données.
4. Pour ajouter la deuxième option de choix pour la question **baby_sex**, entrez **sex** dans la colonne `list_name`. Entrez **female** comme nom de choix et **Féminin** comme étiquette de choix.

| list_name | name   | label  |
| :-------- | :----- | :----- |
| sex       | male   | Masculin   |
| sex       | female | Féminin |
| choices |

## Ajouter des paramètres

Il existe de nombreux paramètres facultatifs qui peuvent être ajoutés à la feuille de calcul **settings** dans XLSForm.

Les paramètres de formulaire courants incluent :

| Paramètre de formulaire     | Description                            |
| :--------------- | :------------------------------------- |
| form_title       | Titre affiché en haut du formulaire |
| default_language | Langue par défaut du formulaire                  |
| style            | Thèmes pour les formulaires web Enketo            |
| version          | ID de version du formulaire                        |
| settings |

Par exemple, pour ajouter un titre de formulaire :

1. Ajoutez une colonne dans la feuille de calcul settings nommée `form_title`.
2. Entrez le titre du formulaire dans la colonne `form_title`.
   - Si vous ne définissez pas de titre de formulaire dans votre XLSForm, par défaut le nom du fichier Excel sera utilisé comme nom de projet dans KoboToolbox. Cela peut être modifié dans KoboToolbox.

<p class="note">
  <b>Remarque :</b> Pour en savoir plus sur la feuille de calcul settings dans XLSForm, consultez <a class="reference external" href="https://xlsform.org/en/#settings-worksheet">Settings worksheet (XLSForm.org)</a>.
</p>

## Ajouter des colonnes facultatives à la feuille de calcul survey

Pour personnaliser davantage votre XLSForm, vous pouvez ajouter des colonnes facultatives qui incluent la logique de formulaire, les options de question et les paramètres avancés.

| **Nom de colonne**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| hint               | Indice de question                                  |
| guidance_hint      | Indice d'orientation                                  |
| required           | Option pour rendre une question obligatoire            |
| relevant           | Conditions de logique de saut pour la question         |
| constraint         | Critères de validation pour la question           |
| constraint_message | Message d'erreur lorsque les critères de validation ne sont pas respectés |
| appearance         | Options pour l'affichage des questions        |
| choice_filter      | Critères pour la sélection en cascade                  |
| parameters         | Paramètres pour des types de questions spécifiques           |
| calculation        | Expression mathématique pour la question de calcul |
| default            | Réponse par défaut pour une question                |

## Importer et prévisualiser l'XLSForm dans KoboToolbox

Pour importer et prévisualiser votre XLSForm dans KoboToolbox :

1. Allez dans la vue **Liste de projets** dans KoboToolbox et cliquez sur **NOUVEAU**.
2. Sélectionnez **Importer un XLSForm** et importez votre fichier **Excel**.
   - Si vous avez créé votre XLSForm dans **Google Sheets**, vous devrez télécharger le fichier avant de l'importer dans KoboToolbox. Dans le menu Google Sheets, cliquez sur Fichier > Télécharger > Microsoft Excel.
3. Entrez les détails du projet et cliquez sur **CRÉER UN PROJET**.
4. Cliquez sur le bouton <i class="k-icon k-icon-view"></i> **Aperçu**.

<p class="note">
  <b>Remarque :</b> Pour apprendre comment importer votre XLSForm via URL, consultez l'article d'assistance <a class="reference" href="https://support.kobotoolbox.org/xls_url.html">Importer un XLSForm via URL</a>.
</p>

## Télécharger un XLSForm depuis KoboToolbox

Les formulaires créés avec l'interface de création de formulaires KoboToolbox peuvent être facilement téléchargés sous forme de fichier XLSForm.

1. Allez dans l'onglet **FORMULAIRE** de votre projet dans KoboToolbox.
2. Cliquez sur l'icône <i class="k-icon k-icon-more"></i> **Plus d'actions**.
3. Cliquez sur <i class="k-icon k-icon-xls-file"></i>**Télécharger XLS**.

Télécharger votre formulaire KoboToolbox sous forme de fichier XLSForm peut être très utile pour de nombreuses raisons, notamment :

-   Ajouter des fonctionnalités avancées à votre formulaire qui ne sont actuellement pas prises en charge dans l'interface de création de formulaires.
-   Apporter des modifications au formulaire qui sont plus efficaces à faire en XLSForm (par exemple, dupliquer un grand nombre de questions ou ajouter des traductions).
-   Éviter les vitesses d'ordinateur ou d'internet lentes qui peuvent affecter la construction de formulaires dans l'interface de création de formulaires (par exemple, RAM limitée, mauvaise connectivité internet).
-   Partager le formulaire sous forme de fichier Excel pour la collaboration avec les membres de l'équipe et la gestion des versions de formulaire.
-   Partager le formulaire pour demander de l'aide à l'équipe d'assistance KoboToolbox ou sur le Forum communautaire.

## Remplacer un formulaire par un fichier XLSForm

Vous pouvez remplacer un formulaire existant dans l'interface de création de formulaires par une nouvelle version en utilisant un XLSForm. Par exemple, après avoir modifié le formulaire dans Excel, vous devez importer le fichier mis à jour dans KoboToolbox.

1. Allez dans l'onglet **FORMULAIRE** de votre projet dans KoboToolbox.
2. Cliquez sur l'icône <i class="k-icon k-icon-more"></i> **Plus d'actions**.
3. Cliquez sur <i class="k-icon k-icon-replace"></i> **Remplacer le formulaire**.
4. Choisissez le fichier que vous souhaitez importer.

## Plus de ressources XLSForm

Pour plus d'informations sur l'utilisation de XLSForm, consultez les ressources suivantes :

-   [Documentation officielle XLSForm sur XLSForm.org](https://xlsform.org)
-   [Documentation de construction de formulaires d'ODK](https://docs.getodk.org/)