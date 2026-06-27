# Options de questions dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/question_options_xls.md" class="reference">23 Apr 2026</a>

Lors de la conception d'un formulaire dans XLSForm, vous pouvez personnaliser les questions en ajoutant des indices, en définissant des apparences, en rendant une question obligatoire, et bien plus encore. Pour ce faire, vous pouvez ajouter de nouvelles colonnes dans l'**onglet survey** de votre XLSForm. Ces colonnes peuvent être ajoutées n'importe où dans l'onglet, à condition que le nom de la colonne soit saisi exactement comme requis.

Cet article présente les options de questions les plus courantes et explique comment les ajouter à votre XLSForm, notamment les indices de questions, les questions obligatoires, les réponses par défaut et les paramètres de questions.

<p class="note">
  <strong>Note :</strong> Cet article porte sur la définition des options de questions dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur les options de questions dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_options.html">Options de questions dans le Formbuilder</a>.
<br><br>
Pour un apprentissage pratique des options de questions dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Indices de questions

Les **indices de questions** vous permettent d'ajouter des instructions ou des informations supplémentaires à votre formulaire. Il existe deux types d'indices que vous pouvez ajouter dans XLSForm :
- Les **indices de base** (hint) sont utilisés pour fournir des informations supplémentaires aux répondants ou aux enquêteurs directement dans le formulaire. Ils sont toujours visibles et s'affichent sous le libellé de la question.
- Les **instructions supplémentaires** (guidance hint) sont utilisées pour fournir des informations supplémentaires lors du développement du formulaire, de la formation des enquêteurs ou de la collecte de données. Elles ne sont pas affichées par défaut.

### Ajouter des indices de questions dans XLSForm

Pour ajouter un **indice de base** (hint) dans XLSForm :
1. Ajoutez une colonne `hint` à l'onglet survey.
2. Sur la même ligne que votre question, saisissez le texte qui doit s'afficher comme indice pour cette question.

Pour ajouter des **instructions supplémentaires** (guidance hint) dans XLSForm :
1. Ajoutez une colonne `guidance_hint` à l'onglet survey.
2. Sur la même ligne que votre question, saisissez le texte à inclure comme instructions supplémentaires.

**onglet survey**

| type | name | label | hint | guidance_hint |
| :--- | :--- | :--- | :--- | :--- |
| integer | height | What is your height? | In centimeters | If the respondent does not know their height, enter 0 |
| survey |

<p class="note">
<strong>Note :</strong> Les indices de questions peuvent également être traduits dans plusieurs langues. Pour plus d'informations sur la traduction des formulaires, consultez l'article <a class="reference" href="https://support.kobotoolbox.org/fr/language_xls.html">Ajouter des traductions dans XLSForm</a>.
</p>

### Afficher les instructions supplémentaires dans KoboCollect

Dans les formulaires web, les instructions supplémentaires apparaissent dans une section repliable **Plus de détails**. Dans KoboCollect, elles sont masquées par défaut, mais vous pouvez [modifier les paramètres de votre projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) pour les afficher en permanence ou dans une section repliable.

Pour afficher les instructions supplémentaires dans KoboCollect, suivez les étapes ci-dessous :
1. Appuyez sur l'**icône du projet** en haut à droite de votre écran.
2. Appuyez sur **Paramètres**.
3. Sous **Gestion des formulaires**, sélectionnez **Afficher les instructions pour les questions**.
4. Choisissez une option d'affichage : **Non**, **Oui - toujours affiché**, ou **Oui - réduit**.

<p class="note">
<strong>Note :</strong> Les instructions supplémentaires sont toujours affichées dans les formulaires imprimés.
</p>

## Questions obligatoires

Par défaut, les questions d'un formulaire sont facultatives. Rendre une question **obligatoire** impose au répondant d'y répondre. Cela peut être utile pour s'assurer que les soumissions sont complètes et éviter les données manquantes.

<p class="note">
<strong>Note :</strong> Les conditions de logique de saut ont la priorité sur les paramètres <strong>obligatoires</strong>, ce qui signifie que si une question obligatoire est masquée par la logique de saut, il n'est plus nécessaire d'y répondre.
</p>

Pour rendre une question obligatoire dans XLSForm :
1. Ajoutez une colonne `required` à l'onglet survey.
2. Dans la colonne `required`, saisissez l'une des valeurs suivantes : `TRUE`, `true` ou `yes`.
3. Pour les questions facultatives, laissez la colonne `required` vide ou saisissez l'une des valeurs suivantes : `FALSE`, `false` ou `no`.

Si un répondant ne répond pas à une question obligatoire, il ne pourra pas passer à la page suivante ni soumettre le formulaire. Le message d'obligation par défaut « This field is required » s'affichera.

<p class="note">
<strong>Note :</strong> Seules les questions nécessitant une saisie doivent être marquées comme obligatoires dans votre XLSForm. Si des questions de type <code>note</code> sont marquées comme obligatoires, vous ne pourrez pas continuer ni soumettre le formulaire.
</p>

### Modifier le message d'obligation par défaut

Vous pouvez modifier le message d'obligation par défaut dans votre XLSForm en suivant les étapes ci-dessous :

1. Ajoutez une colonne `required_message` à l'onglet survey.
2. Saisissez le texte à afficher lorsque les utilisateurs laissent une question obligatoire sans réponse.

**onglet survey**

| type | name | label | required | required_message |
| :--- | :--- | :--- | :--- | :--- |
| select_one education | education_level | What is the highest level of education you have completed? | TRUE | |
| integer | age | What is your age? | TRUE | Please respond to this question before continuing. |
| survey |

<p class="note">
<strong>Note :</strong> Une logique de formulaire personnalisée peut être utilisée pour rendre une question obligatoire ou facultative en fonction d'une réponse précédente. Pour en savoir plus sur la logique d'obligation conditionnelle, consultez l'article <a class="reference" href="https://support.kobotoolbox.org/fr/required_logic_xls.html">Ajouter une logique d'obligation conditionnelle dans XLSForm</a>.
</p>

## Réponses par défaut

Une **réponse par défaut** prérenseigne une question avec une réponse prédéfinie basée sur une réponse courante ou attendue. La réponse par défaut peut être fixe ou [déterminée dynamiquement](https://support.kobotoolbox.org/fr/question_options_xls.html#setting-dynamic-default-responses) en fonction de la réponse à une question précédente.

La réponse par défaut sera enregistrée comme réponse finale lors de la soumission du formulaire, **sauf si elle est modifiée par le répondant** pendant la collecte de données. Pour empêcher les répondants de modifier une réponse par défaut, ajoutez une colonne `read_only` et définissez-la comme `TRUE`.

<p class="note">
<strong>Note :</strong> Bien que les réponses par défaut puissent rendre la collecte de données plus efficace en prérenseignant le formulaire avec des réponses attendues ou courantes, elles risquent également d'introduire des biais ou des erreurs dans les données, et doivent être utilisées avec précaution.
</p>

Pour définir une réponse par défaut fixe dans XLSForm :
1. Ajoutez une colonne `default` à l'onglet survey.
2. Saisissez la réponse par défaut en respectant le [format approprié](https://support.kobotoolbox.org/fr/question_options_xls.html#default-response-format) pour le type de question.

**onglet survey**

| type | name | label | default |
| :--- | :--- | :--- | :--- |
| text | name | What is your name? | John Doe |
| integer | age | What is your age? | 50 |
| select_one marital_options | marital_status | What is your marital status? | married |
| select_multiple income_options | income_sources | What are your sources of income? | formal_work farm_business |
| date | dob | When were you born? | 1990-03-25 |
| date | interview_date | When was this interview conducted? | today() |
| survey |

### Format des réponses par défaut

Le format de la réponse par défaut dépend du type de question et des données collectées :

| Type de question | Format de la réponse par défaut |
| :--- | :--- |
| `integer` | Nombre |
| `text` | Texte (sans guillemets) |
| `select_one` | **Nom** du choix (tel que défini dans l'onglet choices) |
| `select_multiple` | **Nom(s)** du ou des choix, séparés par un **espace** s'il y en a plusieurs |
| `date` | Date au format AAAA-MM-JJ. Si nécessaire, faites précéder la date d'une apostrophe (') dans Excel pour éviter d'éventuels problèmes de mise en forme. |

### Définir des réponses par défaut dynamiques

Les réponses par défaut saisies dans le champ `default` doivent être des valeurs fixes. Pour définir une **réponse par défaut dynamique** basée sur une réponse précédente, utilisez les colonnes `calculation` et `trigger` à la place de la colonne `default` :
1. Dans la colonne `calculation`, saisissez la **référence à la question** qui alimentera dynamiquement la réponse par défaut.
2. Dans la colonne `trigger`, saisissez la question qui déclenchera le calcul.
    - En général, il s'agit de la même question que celle référencée dans la colonne `calculation`, de sorte que toute modification de la question déclencheur mettra également à jour la réponse par défaut.

**onglet survey**

| type | name | label | calculation | trigger |
| :--- | :--- | :--- | :--- | :--- |
| text | hh_name | Name of the head of household | | |
| text | phone | Household phone number | | |
| text | phone_name | Name of the phone owner | ${hh_name} | ${hh_name} |
| survey |

## Paramètres de questions

Les paramètres de questions dans XLSForm vous permettent d'affiner le comportement de vos questions au-delà des paramètres de base.

Pour ajouter des paramètres de questions dans XLSForm :
1. Ajoutez une colonne `parameters` à l'onglet survey.
2. Saisissez le [paramètre](https://support.kobotoolbox.org/fr/question_options_xls.html#common-question-parameters) approprié pour votre type de question.
3. Certains paramètres peuvent être combinés et appliqués à la même question. Pour combiner des paramètres, saisissez-les dans la même cellule en les séparant par un espace.

**onglet survey**

| type | name | label | parameters |
| :--- | :--- | :--- | :--- |
| select_one reasons | reasons | Please select all reasons that apply. | randomize=true |
| range | phone | Please select a number between 1 and 5. | start=1 end=5 step=1 |
| survey |

### Paramètres de questions courants

Les différents types de questions dans XLSForm disposent de paramètres différents. Les paramètres les plus courants sont :

| Paramètre | Type de question | Description |
| :--- | :--- | :--- |
| `randomize=true` | `rank`, `select_one`, `select_multiple` | Randomise l'ordre des choix de réponse |
| `start=1 end=5 step=1` | `range` | Définit la valeur minimale, la valeur maximale et l'écart entre les nombres |
| `capture-accuracy=20` | `geopoint` | Spécifie la [précision GPS](https://support.kobotoolbox.org/fr/collect_gps.html#accuracy-of-gps-coordinates) minimale acceptable (en mètres) pour la capture automatique d'une position. La valeur par défaut est 5 m. |
| `warning-accuracy=50` | `geopoint` | Déclenche un message d'avertissement si la [précision GPS](https://support.kobotoolbox.org/fr/collect_gps.html#accuracy-of-gps-coordinates) (en mètres) n'est pas dans le seuil de précision spécifié. La valeur par défaut est 100 m. |
| `max-pixels=480` | `image` | Limite le nombre maximum de pixels d'une photo, afin de réduire la taille du fichier image et d'améliorer la vitesse d'importation |
| `quality=low` | `audio` | Capture un enregistrement audio de qualité inférieure |
| `quality=voice-only` | `audio` | Capture un enregistrement audio de la qualité la plus basse |

## Options de questions supplémentaires

Les XLSForms peuvent inclure des colonnes supplémentaires dans l'onglet survey pour des formulaires et des fonctionnalités plus avancés. En voici quelques-unes.

| Colonne XLSForm | Description |
| :--- | :--- |
| `read_only` | Si `yes` est saisi dans le champ `read_only`, la question ne peut pas être modifiée par le répondant. Les champs `read_only` peuvent être combinés avec les champs `default` ou `calculation` pour afficher des informations au répondant. |
| `trigger` | La colonne trigger peut être utilisée pour exécuter un calcul uniquement lorsque la réponse à une autre question visible dans le formulaire est modifiée. Pour plus d'informations, consultez la <a href="https://xlsform.org/en/#trigger">documentation XLSForm</a>. |
| `body::accept` | Pour limiter ou élargir les types de fichiers acceptés pour les questions de type `file`, spécifiez les extensions de fichiers dans la colonne `body::accept`, séparées par une virgule (par exemple, .pdf, .doc, .png). |
| `hxl` | Pour inclure des balises <a href="https://hxlstandard.org">Humanitarian Exchange Language</a> (HXL) dans votre formulaire, spécifiez la balise (et l'attribut facultatif) dans la colonne `hxl`, en respectant le format `#tag` ou `#tag+attribute`. |

D'autres colonnes peuvent également être ajoutées pour intégrer une logique de formulaire dans votre XLSForm.

<p class="note">
    Pour en savoir plus sur l'ajout d'une logique de formulaire, consultez les articles <a href="https://support.kobotoolbox.org/fr/skip_logic_xls.html">Ajouter une logique de saut dans XLSForm</a>, <a href="https://support.kobotoolbox.org/fr/constraints_xls.html">Ajouter des contraintes dans XLSForm</a>, <a href="https://support.kobotoolbox.org/fr/required_logic_xls.html">Ajouter une logique d'obligation conditionnelle dans XLSForm</a>, <a href="https://support.kobotoolbox.org/fr/choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a> et <a href="https://support.kobotoolbox.org/fr/calculations_xls.html">Ajouter des calculs dans XLSForm</a>.
</p>