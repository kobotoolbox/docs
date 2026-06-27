# Types de questions dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/question_types_xls.md" class="reference">23 avr. 2026</a>

Lorsque vous ajoutez des questions à un XLSForm, vous devez choisir le **type de question** approprié. Le type de question dépendra du type d'information que vous souhaitez collecter : certains types de questions sont plus adaptés au texte, d'autres aux chiffres, aux dates ou aux choix multiples.

Le type de question dans XLSForm est saisi dans la colonne `type` de l'**onglet survey**. Utilisez toujours l'orthographe exacte et respectez les majuscules et minuscules. Vous pouvez ajouter des [apparences](https://support.kobotoolbox.org/fr/appearances_xls.html) supplémentaires à la plupart des types de questions pour modifier leur affichage ou leur fonctionnalité.

<p class="note">
<strong>Note :</strong> Bien que XLSForm soit entièrement intégré dans KoboToolbox, certains types de questions ont des noms et des fonctionnalités différents dans l'<a href="https://support.kobotoolbox.org/fr/formbuilder.html">interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)</a> que dans XLSForm.
</p>

Cet article couvre les types de questions disponibles dans XLSForm, y compris leurs descriptions et leurs équivalents dans le Formbuilder. Des liens sont fournis à la fin de chaque section pour plus d'informations sur les fonctionnalités des types de questions et les apparences lors de la collecte de données.

<p class="note">
Pour en savoir plus sur la création de formulaires dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">Créer un XLSForm</a>.
</p>

### Questions à choix multiple

Les questions à choix multiple permettent aux répondants de choisir parmi des options prédéfinies. Pour les questions `select_one`, `select_multiple` et `rank`, les [choix de réponse](https://support.kobotoolbox.org/fr/option_choices_xls.html) sont définis dans l'**onglet choices** de l'XLSForm.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `select_one` | Permet aux répondants de sélectionner une option parmi une liste prédéfinie. | Choix unique |
| `select_multiple` | Permet aux répondants de sélectionner plusieurs options parmi une liste prédéfinie. | Choix multiple |
| `rank` | Permet aux répondants de classer des éléments ou des options dans une liste de choix. | Classement |
| `acknowledge` | Une case à cocher unique que les répondants peuvent sélectionner pour confirmer leur accord avec une déclaration. | Consentement |
| `select_one_from_file` | Permet aux répondants de sélectionner une option parmi une liste prédéfinie, stockée dans un fichier CSV externe. | Choix unique à partir d'un fichier |
| `select_multiple_from_file` | Permet aux répondants de sélectionner plusieurs options parmi une liste prédéfinie, stockée dans un fichier CSV externe. | Choix multiple à partir d'un fichier |


<p class="note">
Pour en savoir plus sur les questions à choix multiple dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/select_one_and_select_many.html">Questions à choix multiple dans KoboToolbox</a>.
</p>


### Questions numériques

Les questions numériques sont utilisées pour collecter des nombres entiers, des nombres décimaux ou des valeurs dans une plage spécifiée.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `integer` | Permet aux répondants de saisir des nombres entiers. | Chiffre |
| `decimal` | Permet aux répondants de saisir des nombres pouvant contenir des décimales. | Décimale |
| `range` | Permet aux répondants de sélectionner une valeur numérique dans une plage spécifiée, limitée par des valeurs minimales et maximales, <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#question-parameters">configurées</a> dans la colonne `parameters`. | Intervalle |


<p class="note">
Pour en savoir plus sur les questions numériques dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/number_decimal_range.html">Questions numériques dans KoboToolbox</a>.
</p>


### Questions de type texte et note

Les questions de type texte sont utilisées pour collecter des réponses ouvertes, tandis que les questions de type note fournissent des informations ou donnent des instructions aux répondants.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `text` | Fournit une zone de texte pour collecter des réponses ouvertes lorsque les choix ne peuvent pas être facilement prédéfinis, comme des noms, des opinions ou des descriptions détaillées. | Texte |
| `note` | Fournit des informations au répondant sans nécessiter de saisie, comme des instructions ou des explications. | Note |


<p class="note">
Pour en savoir plus sur les questions de type texte et note dans KoboToolbox, consultez les articles <a href="https://support.kobotoolbox.org/fr/text_questions.html">Questions de type texte dans KoboToolbox</a> et <a href="https://support.kobotoolbox.org/fr/note_questions.html">Questions de type note dans KoboToolbox</a>.
</p>

### Questions de type média

Les questions de type média permettent aux répondants de télécharger ou d'enregistrer des images, des fichiers audio et vidéo, ou de scanner des codes-barres directement dans leurs formulaires.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `image` | Permet aux répondants de télécharger des images ou de prendre des photos lors de l'utilisation de l'application KoboCollect. La qualité des fichiers image peut être <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#question-parameters">ajustée</a> dans la colonne `parameters`. | Photographie |
| `audio` | Permet aux répondants de télécharger un fichier audio ou d'enregistrer de l'audio en réponse à une question spécifique. La qualité des fichiers audio peut être <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#question-parameters">ajustée</a> dans la colonne `parameters`. | Audio |
| `video` | Permet aux répondants de télécharger des vidéos ou d'enregistrer des vidéos lors de l'utilisation de l'application KoboCollect. | Vidéo |
| `file` | Permet aux répondants de télécharger des fichiers, tels que des fichiers texte, des tableurs et des fichiers PDF. Les types de fichiers acceptés peuvent être <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#additional-question-options">restreints</a> en spécifiant les extensions de fichiers dans la colonne `body::accept` (par exemple, `.pdf, .docx`). | Fichier |
| `barcode` | Scanne un code QR pour collecter les informations intégrées à l'aide de la caméra de l'appareil dans KoboCollect. | Code-barres / code QR |
| `background-audio` | Collecte de l'audio en continu pendant que le formulaire est ouvert. L'enregistrement audio commence lorsque le formulaire est ouvert et se poursuit jusqu'à ce que le formulaire soit fermé. | Enregistrement audio d'arrière-plan |


<p class="note">
Pour en savoir plus sur les questions de type média dans KoboToolbox, consultez les articles <a href="https://support.kobotoolbox.org/fr/photo_audio_video_file.html">Questions multimédias dans KoboToolbox</a> et <a href="https://support.kobotoolbox.org/fr/recording-interviews.html#recording-interviews-with-background-audio-recordings">Collecter des données qualitatives avec KoboToolbox</a>.
</p>

### Questions de type GPS

Les questions de type GPS sont utilisées pour capturer les coordonnées géographiques d'un lieu, d'un chemin ou d'une zone directement dans vos formulaires.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `geopoint` | Collecte un emplacement géographique unique, tel que les coordonnées d'une école, d'une clinique ou d'une maison spécifique. La précision par défaut et la précision d'avertissement peuvent être <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#question-parameters">configurées</a> dans la colonne `parameters`. | Position |
| `geotrace` | Enregistre plusieurs points GPS qui forment une ligne, par exemple pour suivre un chemin, tracer un itinéraire ou cartographier un drain. | Ligne |
| `geoshape` | Collecte des points qui forment une zone fermée, comme une parcelle de terrain ou un champ. | Zone |


<p class="note">
Pour en savoir plus sur les questions de type GPS dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/gps_questions.html">Questions GPS dans KoboToolbox</a>.
</p>

### Questions de type date et heure

Les questions de type date et heure sont utilisées pour capturer des dates de calendrier spécifiques, des heures ou les deux dans une seule réponse.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `date` | Capture une date de calendrier spécifique, généralement au format jour, mois et année. | Date |
| `time` | Capture une heure spécifique en heures et minutes. | Heure |
| `datetime` | Capture à la fois une date et une heure dans une seule réponse combinée. | Date et heure |


<p class="note">
Pour en savoir plus sur les questions de type date et heure dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/date_time.html">Questions de type date et heure dans KoboToolbox</a>.
</p>

### Questions de type calcul et caché

Les questions de type calcul et caché sont utilisées pour effectuer des calculs automatiques dans un formulaire en fonction des réponses précédentes ou pour stocker des valeurs prédéfinies.

| Type XLSForm | Description | Équivalent Formbuilder |
| :--- | :--- | :--- |
| `calculate` | Effectue automatiquement des calculs dans un formulaire en fonction des réponses aux questions précédentes. | Calcul |
| `hidden` | Stocke des valeurs prédéfinies qui ne sont pas visibles pour le répondant. La valeur est <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#default-responses">stockée</a> dans la colonne `default`. | Caché |

Pour en savoir plus sur les calculs dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/calculations_xls.html">Ajouter des calculs dans XLSForm</a>.

<p class="note">
Pour une pratique concrète avec différents types de questions dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals de la KoboToolbox Academy</a>.
</p>