# Ajouter des questions avec le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/35c2ef4865450c612c41e9e784bd674a9f99756a/source/question_types.md" class="reference">20 Mar 2026</a>

L'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** vous permet d'ajouter facilement des questions à votre formulaire au fur et à mesure que vous construisez votre enquête ou questionnaire.

Cet article explique comment ajouter des questions à votre formulaire, définir des choix de réponse le cas échéant, et présente un aperçu des types de questions disponibles dans le Formbuilder pour vous aider à concevoir des formulaires efficaces.

## Ajouter une question

Pour ajouter une question à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ ADD QUESTION.**
4. Choisissez le [type de question](#types-de-questions-dans-le-formbuilder).

![Ajouter une question dans le Formbuilder](images/question_types/add_question.png)

<p class="note">
<strong>Note :</strong> Une fois le type de question sélectionné, il ne peut pas être modifié dans le Formbuilder. Pour changer le type d'une question existante, supprimez la question et créez-en une nouvelle avec le même libellé.
</p>

### Définir les noms de champs

Après avoir ajouté une question à votre formulaire, il est fortement recommandé de définir un **nom du champ** dans les **Paramètres** de la question. Le nom du champ est utilisé pour identifier la question dans la logique du formulaire et dans le jeu de données exporté.

Par défaut, KoboToolbox crée le nom du champ automatiquement en supprimant les espaces et les majuscules du libellé de la question. Par exemple, si le libellé de la question est « Nom du répondant », le nom du champ sera `respondent_name`.

<p class="note">
    Pour en savoir plus sur les noms de champs, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_options.html#data-column-name">Options de questions dans le Formbuilder</a>.
</p>

## Ajouter des choix de réponse

Lorsque vous ajoutez des questions de type Choix unique ou Choix multiple à votre formulaire, vous serez invité à saisir des choix de réponse.

- Vous pouvez saisir autant de choix de réponse que vous le souhaitez.
- Pour réorganiser la liste des choix, cliquez sur un élément et faites-le glisser vers la position souhaitée.
- Cliquez sur l'icône de corbeille <i class="k-icon-trash"></i> à côté d'un libellé de choix pour le supprimer.

![Supprimer un choix](images/question_types/delete_choice.png)

<p class="note">
<strong>Note :</strong> La gestion de longues listes de choix dans le Formbuilder peut prendre beaucoup de temps. Si votre formulaire comprend de nombreuses options ou si la même liste de choix est utilisée dans plusieurs questions, il est souvent plus simple de créer et de gérer ces listes avec XLSForm. Pour en savoir plus, consultez l'article <a href="https://support.kobotoolbox.org/fr/option_choices_xls.html#">Gérer les choix de réponse dans XLSForm</a>.
</p>

### Définir les valeurs XML des choix de réponse

À côté de chaque choix de réponse, vous verrez un champ intitulé **AUTOMATIC.** Ce champ contient la [valeur XML](https://support.kobotoolbox.org/fr/glossary.html#xml-value) de cette option.

La valeur XML est un nom interne court que KoboToolbox utilise pour enregistrer et identifier l'option sélectionnée dans vos données. Par défaut, KoboToolbox crée la valeur XML automatiquement en supprimant les espaces et les majuscules du libellé de l'option. Par exemple, si le libellé de l'option est « Option 1 », la valeur XML sera `option_1`.

Dans certains cas, vous pouvez souhaiter définir votre propre valeur XML. Cela peut être utile si le libellé de l'option est très long ou si vous souhaitez utiliser un nom plus clair ou plus cohérent. Pour ce faire, cliquez sur **AUTOMATIC** et remplacez-le par votre propre valeur personnalisée.

<p class="note">
<strong>Note :</strong> Il est fortement recommandé de définir des valeurs XML pour tous les choix lorsque vous utilisez des scripts non latins, tels que le chinois, l'arabe ou le népalais, afin de garantir que vos données sont correctement enregistrées et exportées.
</p>

## Types de questions dans le Formbuilder

Les types de questions suivants sont disponibles dans le Formbuilder :

| Type de question | Description |
|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| <i class="k-icon-qt-select-one"></i> Choix unique | Permet aux répondants de [sélectionner une option](https://support.kobotoolbox.org/fr/select_one_and_select_many.html) dans une liste prédéfinie. |
| <i class="k-icon-qt-select-many"></i> Choix multiple | Permet aux répondants de [sélectionner plusieurs options](https://support.kobotoolbox.org/fr/select_one_and_select_many.html) dans une liste prédéfinie. |
| <i class="k-icon-qt-text"></i> Texte | Fournit une [zone de texte](https://support.kobotoolbox.org/fr/text_questions.html) pour recueillir des réponses ouvertes. |
| <i class="k-icon-qt-number"></i> Chiffre | Permet aux répondants de saisir des [nombres entiers](https://support.kobotoolbox.org/fr/number_decimal_range.html). |
| <i class="k-icon-qt-decimal"></i> Décimale | Permet aux répondants de [saisir des nombres](https://support.kobotoolbox.org/fr/number_decimal_range.html) pouvant contenir des décimales. |
| <i class="k-icon-qt-date"></i> Date | Capture une [date calendaire](https://support.kobotoolbox.org/fr/date_time.html) précise, incluant l'année, le mois et le jour. |
| <i class="k-icon-qt-time"></i> Heure | Capture une [heure précise](https://support.kobotoolbox.org/fr/date_time.html) en heures et minutes. |
| <i class="k-icon-qt-date-time"></i> Date et heure | Capture à la fois [une date et une heure](https://support.kobotoolbox.org/fr/date_time.html) dans une réponse combinée. |
| <i class="k-icon-qt-point"></i> Position | Enregistre une [localisation GPS unique](https://support.kobotoolbox.org/fr/gps_questions.html). |
| <i class="k-icon-qt-line"></i> Ligne | Enregistre [plusieurs points GPS](https://support.kobotoolbox.org/fr/gps_questions.html) formant une ligne. |
| <i class="k-icon-qt-area"></i> Zone | Enregistre [plusieurs points GPS](https://support.kobotoolbox.org/fr/gps_questions.html) formant une zone délimitée. |
| <i class="k-icon-qt-photo"></i> Photographie | Permet aux répondants d'[importer des images](https://support.kobotoolbox.org/fr/photo_audio_video_file.html) ou de prendre des photos (lors de l'utilisation de l'[application KoboCollect](https://support.kobotoolbox.org/fr/glossary.html#kobocollect)). |
| <i class="k-icon-qt-audio"></i> Audio | Permet aux répondants d'[importer un fichier audio](https://support.kobotoolbox.org/fr/photo_audio_video_file.html) ou d'enregistrer un audio. |
| <i class="k-icon-qt-video"></i> Vidéo | Permet aux répondants d'[importer des vidéos](https://support.kobotoolbox.org/fr/photo_audio_video_file.html) ou d'enregistrer des vidéos (lors de l'utilisation de l'[application KoboCollect](https://support.kobotoolbox.org/fr/glossary.html#kobocollect)). |
| <i class="k-icon-qt-barcode"></i> Code-barres / code QR | Scanne un [code QR](https://support.kobotoolbox.org/fr/photo_audio_video_file.html) pour collecter les informations intégrées à l'aide de la caméra de l'appareil (lors de l'utilisation de l'[application KoboCollect](https://support.kobotoolbox.org/fr/glossary.html#kobocollect)). |
| <i class="k-icon-qt-file"></i> Fichier | Permet aux répondants d'[importer des fichiers](https://support.kobotoolbox.org/fr/photo_audio_video_file.html), tels que des fichiers texte, des tableurs et des fichiers PDF. |
| <i class="k-icon-qt-note"></i> Note | [Fournit des informations](https://support.kobotoolbox.org/fr/note_questions.html) au répondant sans nécessiter de saisie. |
| <i class="k-icon-qt-acknowledge"></i> Consentement | Une [case à cocher unique](https://support.kobotoolbox.org/fr/select_one_and_select_many.html) que les répondants peuvent sélectionner pour confirmer leur accord avec une déclaration. |
| <i class="k-icon-qt-rating"></i> Notation | Permet aux répondants d'[évaluer différents éléments](https://support.kobotoolbox.org/fr/select_one_and_select_many.html#setting-up-rating-questions) à l'aide d'une échelle commune. |
| <i class="k-icon-qt-question-matrix"></i> Tableau de questions | Crée un [groupe de questions](https://support.kobotoolbox.org/fr/matrix_response.html) affichées dans un format de tableau, où chaque cellule représente une question distincte. |
| <i class="k-icon-qt-ranking"></i> Classement | Permet aux répondants de [classer des éléments](https://support.kobotoolbox.org/fr/select_one_and_select_many.html#setting-up-ranking-questions) par ordre de préférence. |
| <i class="k-icon-qt-calculate"></i> Calcul | Effectue automatiquement des [calculs](https://support.kobotoolbox.org/fr/calculate_questions.html) dans un formulaire en fonction des réponses aux questions précédentes. |
| <i class="k-icon-qt-hidden"></i> Caché | Stocke des [valeurs prédéfinies](https://support.kobotoolbox.org/fr/form_logic.html#storing-constants-in-your-form) qui ne sont pas visibles par le répondant. |
| <i class="k-icon-qt-range"></i> Intervalle | Permet aux répondants de [sélectionner une valeur numérique](https://support.kobotoolbox.org/fr/number_decimal_range.html#setting-up-range-questions) dans une plage définie. |
| <i class="k-icon-qt-external-xml"></i> XML externe | Connecte le projet KoboToolbox à [d'autres projets](https://support.kobotoolbox.org/fr/dynamic_data_attachment_formbuilder.html) afin de récupérer des données de manière dynamique. |
| <i class="k-icon-qt-select-one-from-file"></i> Choix unique à partir d'un fichier | Permet aux répondants de sélectionner une option [dans une liste prédéfinie](https://support.kobotoolbox.org/fr/external_file.html) stockée dans un fichier CSV externe. |
| <i class="k-icon-qt-select-many-from-file"></i> Sélectionner plusieurs dans le fichier | Permet aux répondants de sélectionner plusieurs options [dans une liste prédéfinie](https://support.kobotoolbox.org/fr/external_file.html) stockée dans un fichier CSV externe. |

<p class="note">
<strong>Note :</strong> Les types de questions Choix unique à partir d'un fichier et Sélectionner plusieurs dans le fichier n'apparaissent comme options dans le Formbuilder que si un fichier de choix externe a été <a href="https://support.kobotoolbox.org/fr/upload_media.html">importé</a> dans KoboToolbox.
</p>