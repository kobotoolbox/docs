# Ajouter des traductions dans XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/26219c3ff68ab5e06bc080c11ae388324a894200/source/language_xls.md" class="reference">5 Jun 2026</a>

Ajouter des traductions à un formulaire permet aux utilisateurs de passer à leur langue préférée pendant la collecte de données sans avoir à créer des formulaires distincts. Vous pouvez ajouter autant de traductions que vous le souhaitez. [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html) et les [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html) permettent tous deux les traductions de formulaires.

La plupart des éléments affichés dans le formulaire peuvent être traduits, notamment les **libellés de questions**, les **indices**, les **libellés de choix**, les **messages de contrainte** et les **messages d'obligation**. Les éléments utilisés pour la structure du formulaire, tels que les noms de questions, les noms de choix et les noms de listes, ne peuvent pas être traduits et doivent rester dans la langue utilisée pour le développement du formulaire et l'analyse des données.

<p class="note">
  <strong>Note :</strong> Ajouter des traductions dans XLSForm est plus rapide et plus efficace qu'<a href="https://support.kobotoolbox.org/fr/language_dashboard.html">utiliser l'interface KoboToolbox</a>, en particulier pour les formulaires longs. Pour savoir comment télécharger votre formulaire au format XLSForm afin d'y ajouter des traductions, consultez l'article <a href="../fr/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>.
<br><br>
Pour vous exercer à ajouter des traductions dans XLSForm, consultez le cours <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

Lorsque votre formulaire comprend plusieurs traductions, KoboCollect et les formulaires web affichent un sélecteur de langue **en haut à droite du formulaire**, permettant aux répondants de choisir leur langue préférée.

<p class="note">
    Pour en savoir plus sur la collecte et la gestion des données issues de formulaires traduits, consultez l'article <a href="https://support.kobotoolbox.org/fr/collecting_data_multiple_languages.html">Collecter des données dans plusieurs langues</a>.
</p>

## Codes de langue dans XLSForm

Pour faire référence à différentes langues dans XLSForm, vous devez utiliser le format `langue (code)` dans les en-têtes de colonnes. Par exemple, la référence de langue pour l'anglais est `English (en)` et la référence de langue pour le français est `French (fr)`. Chaque traduction doit utiliser le même nom de langue et le même code de manière cohérente dans tout le formulaire.

Les codes de langue sont disponibles dans le <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">registre IANA des sous-étiquettes de langue</a>. Sur le site de l'IANA, le champ **Description** correspond au nom de la langue et le champ **Subtag** correspond au code de langue (par exemple, **Description :** French, **Subtag :** fr).


## Définir la langue par défaut du formulaire

Pour ajouter des traductions à un XLSForm, commencez par définir la langue par défaut. Il s'agit de la langue dans laquelle le formulaire s'ouvrira par défaut.

Pour définir la langue par défaut de votre formulaire :
1. Dans l'**onglet settings**, ajoutez une colonne `default_language`.
2. Dans la colonne `default_language`, saisissez la langue par défaut en utilisant le format `langue (code)`.
    - Par exemple : `English (en)`.

**onglet settings**

| default_language |
| :---------------- |
| English (en)      |
| settings |

Pour configurer l'**onglet survey** :

1. Renommez la colonne `label` en utilisant le format `label::langue (code)`.
    - Par exemple : `label::English (en)`.
2. Si votre formulaire comprend des colonnes `hint`, `required_message`, `constraint_message` ou `media` dans l'onglet survey, renommez les colonnes existantes en utilisant le format `nom_colonne::langue (code)`.
    - Par exemple : `hint::English (en)`.

**onglet survey**

| type | name | label::English (en) | hint::English (en) |
| :--- | :--- | :------------------ | :----------------- |
| integer | age | How old are you? | In years |
| select_one yn | student | Are you currently a student? | |
| survey |

Enfin, pour configurer l'**onglet choices**, renommez la colonne `label` en utilisant le format `label::langue (code)`.

**onglet choices**

| list_name | name | label::English (en) |
| :--------- | :--- | :------------------ |
| yn | yes | Yes |
| yn | no | No |
| choices |

## Ajouter des traductions

Une fois la langue par défaut définie, vous pouvez ajouter des traductions pour chaque élément visible de votre formulaire. Vous pouvez ajouter autant de colonnes de traduction que vous le souhaitez.

<p class="note">
  <strong>Note :</strong> Si vous omettez le texte d'un élément traduit, celui-ci apparaîtra comme un champ vide dans le formulaire.
</p>

Pour ajouter des traductions dans l'onglet survey :
1. Ajoutez une nouvelle colonne `label` pour chaque langue de traduction en utilisant le format `label::langue (code)`.
    - Par exemple : `label::Spanish (es)`.
2. Si votre formulaire comprend des colonnes `hint`, `required_message`, `constraint_message` ou `media` dans l'onglet survey, créez les colonnes de traduction correspondantes en utilisant le format `nom_colonne::langue (code)`.
    - Par exemple : `hint::French (fr)` ou `required_message::Chichewa (ny)`.
3. Saisissez les traductions de tous les éléments du formulaire dans les colonnes correspondantes.

<p class="note">
  Pour en savoir plus sur la gestion des fichiers média dans les formulaires traduits, consultez l'article <a href="https://support.kobotoolbox.org/fr/media.html#adding-media-to-translations">Ajouter des médias à un XLSForm</a>.
</p>

**onglet survey**

| type | name | label::English (en) | label::Chichewa (ny) | hint::English (en) | hint::Chichewa (ny) |
| :--- | :--- | :------------------ | :------------------- | :----------------- | :------------------ |
| integer | age | How old are you? | Muli ndi zaka zingati? | In years | M'zaka |
| select_one yn | student | Are you currently a student? | Kodi panopa ndinu wophunzira? | | |
| survey |

Pour ajouter des traductions dans l'onglet choices :
1. Ajoutez une nouvelle colonne `label` pour chaque langue de traduction en utilisant le format `label::langue (code)`.
    - Par exemple : `label::Spanish (es)`.
2. Saisissez la traduction de chaque libellé de choix dans la colonne de traduction correspondante.
3. Si votre onglet choices comprend des colonnes média, créez les colonnes de traduction correspondantes en utilisant le format `nom_colonne::langue (code)`.

<p class="note">
  <strong>Note :</strong> Pour en savoir plus sur la gestion des fichiers média dans les formulaires traduits, consultez l'article <a href="https://support.kobotoolbox.org/fr/media.html#adding-media-to-translations">Ajouter des médias à un XLSForm</a>.
</p>

**onglet choices**

| list_name | name | label::English (en) | label::Chichewa (ny) |
| :--------- | :--- | :------------------ | :------------------- |
| yn | yes | Yes | Inde |
| yn | no | No | Ayi |
| choices |


## Recommandations pour les traductions

### Utiliser les fonctionnalités du tableur pour les traductions en masse

XLSForm facilite la traduction des éléments du formulaire en masse, plutôt que de saisir les traductions une par une. Par exemple, vous pouvez copier une colonne entière dans un outil de traduction pour une traduction en masse, puis coller la colonne dans votre XLSForm. Si vous utilisez Google Sheets pour créer votre XLSForm, vous pouvez utiliser la formule `GOOGLETRANSLATE()` pour automatiser le processus de traduction.

Les traductions automatiques doivent toujours être relues et validées par un locuteur natif afin de garantir leur exactitude, leur adéquation culturelle et leur pertinence contextuelle. Cette étape contribue à maintenir la qualité et la fiabilité de votre contenu traduit.

### Traduire vers des scripts non latins

Les scripts non latins tels que l'arabe, le cyrillique, le tamoul, le népalais ou le hindi sont entièrement pris en charge dans KoboToolbox et peuvent être utilisés comme langues par défaut ou comme traductions.

<p class="note">
  <strong>Note :</strong> Il est recommandé d'utiliser uniquement des caractères latins pour les <strong>noms</strong> de questions et de choix, car les scripts non latins peuvent provoquer des erreurs ou des problèmes de compatibilité lors de l'export des données ou de l'utilisation de XLSForm. En revanche, les <strong>libellés</strong> de questions et de choix peuvent utiliser n'importe quel script sans risque.
</p>

Lorsque vous ajoutez des traductions en scripts non latins, il est essentiel d'**utiliser des caractères Unicode appropriés**. Unicode garantit que le texte est correctement affiché et interprété sur tous les appareils et plateformes.

Pour saisir du texte Unicode, il n'est pas nécessaire d'installer des polices spéciales. Il suffit de configurer le clavier de votre système dans la langue ou le script approprié et de taper normalement. Évitez d'utiliser des pseudo-polices (c'est-à-dire des polices spéciales qui imitent visuellement des scripts non latins en réaffectant des caractères latins), car elles ne sont pas compatibles avec KoboToolbox et peuvent entraîner de graves problèmes d'affichage et d'intégrité des données. Si vous utilisez Windows et avez besoin d'aide pour configurer le clavier de votre système, consultez la [documentation Microsoft](https://support.microsoft.com/en-us/windows/manage-the-language-and-keyboard-input-layout-settings-in-windows-12a10cb4-8626-9b77-0ccb-5013e0c7c7a2).

### Traduire vers des scripts de droite à gauche

Lorsque vous ajoutez une langue utilisant un script de droite à gauche (RTL), comme l'arabe, l'hébreu ou l'ourdou, il est important d'**utiliser le code de langue correct** et de veiller à ce que le **premier texte visible de la traduction** (par exemple, un libellé de question, un indice ou une note) soit rédigé dans la langue RTL. Cela garantit que la mise en page du formulaire ne bascule pas par défaut vers un formatage de gauche à droite (LTR).

De plus, lorsque vous intégrez des références à des questions dans des libellés de questions en scripts RTL, notez que la syntaxe de référencement des questions est inversée (c'est-à-dire `{question_name}$`).

**onglet survey**

| type | name | label::English (en) | label::Arabic (ar) |
| :--- | :--- | :------------------ | :----------------- |
| begin\_group | profile | Respondent profile | ملف المستجيب |
| text | name | Respondent's name | اسم المدعى عليه |
| integer | age | How old is ${name}? | ؟{name}$ كم عمرك |
| end\_group | | | |
| survey |



## Résolution de problèmes

<details>
<summary><b>Une langue sans nom apparaît après l'importation d'un XLSForm</b></summary>
Une langue sans nom peut apparaître si votre XLSForm ne contient pas de colonnes de traduction pour les éléments visibles par les répondants, tels que les colonnes <code>hint</code>, <code>guidance_hint</code>, média, <code>constraint_messages</code> ou <code>required_message</code>. Tant que ce problème n'est pas corrigé, le texte de ces colonnes apparaîtra vide pour toutes les langues autres que la langue par défaut.<br><br>Une langue sans nom peut également apparaître si vous avez défini un <code>default_language</code> dans l'onglet <code>settings</code>, par exemple <code>English (en)</code>, mais que votre formulaire ne comporte qu'une seule langue et utilise <code>label</code> au lieu de <code>label::English (en)</code>. Pour corriger ce problème, supprimez le paramètre de langue par défaut dans l'onglet <code>settings</code>.<br><br>Enfin, une langue sans nom peut apparaître si vous importez un XLSForm dans un projet qui avait auparavant plusieurs langues, mais qui n'en a plus qu'une seule non spécifiée. Si votre formulaire ne comporte désormais qu'une seule langue, ouvrez l'<a class="reference external" href="https://support.kobotoolbox.org/fr/language_dashboard.html">interface de traductions</a>, définissez la langue sans nom comme langue par défaut, puis supprimez les autres langues.
</details>

<br>

<details>
<summary><b>Des langues supplémentaires ou inutiles persistent après l'importation d'un XLSForm</b></summary>
   Si vous importez un XLSForm comportant moins de langues qu'une version antérieure du même projet, KoboToolbox peut continuer à afficher les langues de la version précédente. Pour supprimer les langues inutiles, ouvrez l'<a class="reference external" href="https://support.kobotoolbox.org/fr/language_dashboard.html">interface de traductions</a> dans KoboToolbox et supprimez les langues qui ne sont plus utilisées.
</details>