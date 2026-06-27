# Apparences de questions dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/9c69366d98a834d18d0284e5cc12bafde903278f/source/appearances_xls.md" class="reference">6 mai 2026</a>

Les apparences de questions vous permettent de personnaliser l'affichage des questions dans le formulaire et le type de réponses collectées. Cet article explique comment ajouter des apparences de questions dans un XLSForm et liste les apparences courantes par type de question.

Il est important de noter que certaines apparences ne fonctionnent qu'avec les [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html), tandis que d'autres sont uniquement disponibles dans [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html). Tenez compte de votre méthode de collecte de données lors du choix des apparences.

<p class="note">
  <b>Note :</b> Cet article porte sur la configuration des apparences de questions dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur la configuration des apparences dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** <b>(KoboToolbox Formbuilder)</b>, consultez la documentation <a href="https://support.kobotoolbox.org/fr/using-formbuilder.html">Utiliser le Formbuilder</a>.
<br><br>
Pour vous exercer à configurer des apparences de questions dans un XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des apparences de questions

Pour ajouter des apparences de questions dans un XLSForm :
1. Dans l'**onglet survey**, ajoutez une colonne `appearance`.
2. Saisissez le nom de l'apparence dans la colonne `appearance`. Veillez à respecter exactement l'orthographe et la ponctuation du nom de l'apparence.
3. Certaines apparences peuvent être combinées et appliquées à la même question. Pour combiner des apparences, saisissez-les dans la même cellule en les séparant par un espace.

**onglet survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| text | description | Describe the project. | multiline |
| select_one country_list | country | Which country is this project taking place in? | autocomplete minimal |
| survey |


## Apparences de questions disponibles dans XLSForm
Les tableaux ci-dessous listent les apparences de questions courantes par type de question et indiquent celles qui sont disponibles dans les formulaires web et dans KoboCollect.

### Types de questions à choix multiple
Les questions à choix multiple permettent aux répondants de [choisir parmi des options prédéfinies](https://support.kobotoolbox.org/fr/question_types_xls.html#select-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `minimal` | Affiche les choix dans un menu déroulant. | Formulaires web et KoboCollect |
| `compact` | Affiche les choix côte à côte avec un espacement minimal et sans cases de sélection. | Formulaires web et KoboCollect |
| `label` | Affiche les libellés des choix sans les cases de sélection. | Formulaires web et KoboCollect |
| `list-nolabel` | Affiche les cases de sélection des choix sans les libellés. | Formulaires web et KoboCollect |
| `autocomplete` | Ajoute une barre de recherche en haut de la liste d'options. | Formulaires web et KoboCollect (à combiner avec l'apparence `minimal`) |
| `likert` | Affiche les choix de réponse sous forme d'échelle de Likert (uniquement pour `select_one`). | Formulaires web et KoboCollect |
| `horizontal` | Affiche les choix en colonnes de taille égale, avec le même nombre de choix par ligne. | Formulaires web uniquement. Utilisez `columns` pour une compatibilité avec KoboCollect. |
| `columns` | Affiche les choix en colonnes de taille égale, avec le même nombre de choix par ligne. | Formulaires web et KoboCollect |
| `horizontal-compact` | Affiche les choix en colonnes avec des cases de sélection visibles. Le nombre de colonnes peut varier selon la ligne, en fonction de la longueur de chaque libellé d'option. | Formulaires web uniquement. Utilisez `columns-pack` pour une compatibilité avec KoboCollect. |
| `columns-pack` | Affiche les choix en colonnes avec des cases de sélection visibles. Le nombre de colonnes peut varier selon la ligne, en fonction de la longueur de chaque libellé d'option. | Formulaires web et KoboCollect |
| `columns-n` | Affiche les choix disponibles dans le nombre (n) de colonnes spécifié. | Formulaires web et KoboCollect |
| `quick` | Fait avancer automatiquement le formulaire à la question suivante après la sélection d'une réponse (uniquement pour `select_one`). | KoboCollect uniquement |
| `quickcompact` | Affiche les choix côte à côte avec un espacement minimal et sans cases de sélection, et fait avancer automatiquement le formulaire à la question suivante après la sélection d'une réponse (uniquement pour `select_one`). | KoboCollect uniquement |
| `map` | Affiche une carte pour sélectionner des options. Nécessite de <a href="https://support.kobotoolbox.org/fr/select_from_map_xls.html">définir des coordonnées GPS</a> dans l'onglet `choices` (uniquement pour `select_one`). | KoboCollect uniquement |
| `quick map` | Affiche une carte pour sélectionner des options et enregistre automatiquement le premier emplacement sélectionné sans afficher d'informations supplémentaires. Nécessite de <a href="https://support.kobotoolbox.org/fr/select_from_map_xls.html">définir des coordonnées GPS</a> dans l'onglet `choices` (uniquement pour `select_one`). | KoboCollect uniquement |

<p class="note">
  <b>Note :</b> Les apparences pour les questions <code>select_one</code> et <code>select_multiple</code> peuvent également être utilisées pour les questions de type <a href="https://support.kobotoolbox.org/fr/select_from_file_xls.html">sélection à partir d'un fichier</a>.
</p>

### Types de questions chiffre (integer et decimal)
Les questions numériques permettent de [collecter des nombres entiers ou décimaux](https://support.kobotoolbox.org/fr/question_types_xls.html#numeric-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `thousands-sep` | Formate les grands nombres en utilisant une virgule comme séparateur des milliers. | Formulaires web et KoboCollect |
| `bearing` | Enregistre une mesure de boussole en degrés (uniquement pour `decimal`), si l'appareil est équipé d'un accéléromètre ou d'un capteur de champ magnétique. | KoboCollect uniquement |
| `counter` | Affiche des boutons pour augmenter ou diminuer les chiffres (uniquement pour `integer`). | KoboCollect uniquement |


### Type de question intervalle (range)
Les questions de type intervalle permettent de [sélectionner des valeurs dans une plage définie](https://support.kobotoolbox.org/fr/question_types_xls.html#numeric-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `vertical` | Change l'orientation de la ligne numérique en ligne verticale. | Formulaires web et KoboCollect |
| `picker` | Dans KoboCollect, affiche un sélecteur contextuel pour choisir des valeurs. Dans les formulaires web, affiche un menu déroulant. | Formulaires web et KoboCollect |
| `rating` | Affiche des étoiles à la place de la ligne numérique. | Formulaires web et KoboCollect |
| `distress` | Affiche un thermomètre à la place de la ligne numérique. | Formulaires web uniquement |


### Type de question texte
Les questions de type texte permettent aux utilisateurs de [collecter des réponses ouvertes](https://support.kobotoolbox.org/fr/question_types_xls.html#text-and-note-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `numbers` | Affiche un clavier numérique à la place du clavier de texte (par exemple, pour collecter des numéros de téléphone). | KoboCollect uniquement |
| `multiline` | Affiche une zone de texte plus grande pour les réponses textuelles longues. | Formulaires web et KoboCollect |
| `url` | Affiche une URL cliquable sous le texte de la question et rend la question en lecture seule. Nécessite de saisir une URL dans la colonne `default` de la question, ou dans la colonne `calculation` si l'URL contient des valeurs dynamiques. Fonctionne également avec les questions de type `note`. | Formulaires web et KoboCollect |
| `masked` | Masque le texte saisi par le répondant (par exemple, un mot de passe ou des informations confidentielles). | KoboCollect uniquement |


### Type de question date
Les questions de type date permettent de [capturer des dates calendaires précises](https://support.kobotoolbox.org/fr/question_types_xls.html#date-and-time-question-types).

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `month-year` | Capture un mois et une année. | Formulaires web et KoboCollect |
| `year` | Capture uniquement une année. | Formulaires web et KoboCollect |
| `no-calendar` | Affiche un sélecteur pour choisir le jour, le mois et l'année, à la place du sélecteur de calendrier par défaut. | KoboCollect uniquement |
| `coptic` | Affiche le calendrier copte. | KoboCollect uniquement |
| `ethiopian` | Affiche le calendrier éthiopien. | KoboCollect uniquement |
| `islamic` | Affiche le calendrier islamique. | KoboCollect uniquement |
| `bikram-sambat` | Affiche le calendrier Bikram Sambat. | KoboCollect uniquement |
| `myanmar` | Affiche le calendrier birman. | KoboCollect uniquement |
| `persian` | Affiche le calendrier persan. | KoboCollect uniquement |
| `buddhist` | Affiche le calendrier bouddhiste. | KoboCollect uniquement |


### Types de questions GPS
Les questions GPS permettent de [capturer les coordonnées géographiques](https://support.kobotoolbox.org/fr/question_types_xls.html#gps-question-types) d'un emplacement, d'un itinéraire ou d'une zone directement dans vos formulaires.

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `maps` | Affiche une carte permettant aux utilisateurs de visualiser l'emplacement en cours d'enregistrement automatique (uniquement pour `geopoint`). | KoboCollect uniquement (inclus dans l'apparence par défaut des formulaires web) |
| `placement-map` | Permet la sélection manuelle d'un emplacement sur une carte (uniquement pour `geopoint`). | KoboCollect uniquement (inclus dans l'apparence par défaut des formulaires web) |
| `hide-input` | Affiche une carte plus grande et masque les autres champs de saisie (latitude, longitude, altitude, précision). | Formulaires web uniquement |


### Type de question image
Les questions de type image permettent aux utilisateurs d'[importer ou de prendre des photos](https://support.kobotoolbox.org/fr/question_types_xls.html#media-question-types) directement dans leurs formulaires.

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `signature` | Permet aux utilisateurs de dessiner leur signature. | Formulaires web et KoboCollect |
| `draw` | Permet aux utilisateurs de faire des croquis ou des dessins. | Formulaires web et KoboCollect |
| `annotate` | Permet aux utilisateurs d'annoter une image en dessinant ou en écrivant dessus. Les utilisateurs peuvent importer leur propre image, ou vous pouvez définir une image par défaut à annoter en saisissant le nom du fichier image dans la colonne `default` et en [important](https://support.kobotoolbox.org/fr/upload_media.html) le fichier dans votre projet KoboToolbox. | Formulaires web et KoboCollect |
| `new` | Invite les utilisateurs à prendre une nouvelle photo avec l'appareil photo de l'appareil (sans import de fichier). | KoboCollect uniquement |
| `new-front` | Invite les utilisateurs à prendre une nouvelle photo avec la caméra frontale de l'appareil. | KoboCollect uniquement |


### Type de question code-barres (barcode)
Les questions de type code-barres permettent aux utilisateurs de [scanner un code QR](https://support.kobotoolbox.org/fr/question_types_xls.html#media-question-types) à l'aide de l'appareil photo de l'appareil dans KoboCollect.

| Apparence | Description | Compatibilité |
| :--- | :--- | :--- |
| `hidden-answer` | Masque la valeur du code-barres scanné. | KoboCollect uniquement |