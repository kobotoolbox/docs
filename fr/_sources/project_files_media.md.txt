# Introduction aux fichiers et aux médias de projet
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/project_files_media.md" class="reference">23 Apr 2026</a>

Un projet KoboToolbox peut inclure des fichiers et des médias ajoutés à différentes étapes du processus de collecte de données.

Lors de la création du formulaire, vous pouvez :

- **Joindre des fichiers multimédias** pour enrichir votre formulaire avec des images, des fichiers audio ou des vidéos.
- **Joindre des fichiers de données externes** pour gérer de longues listes de choix ou extraire des données dans votre formulaire.

Lors de la collecte de données, les répondants peuvent **soumettre leurs propres fichiers et médias** dans le cadre de leurs réponses.

Ces deux catégories sont gérées différemment au sein d'un projet.

<p class="note">
<strong>Note :</strong> Seuls les médias et fichiers soumis par les répondants sont comptabilisés dans les limites de stockage de votre plan.
</p>

Cet article présente les sujets suivants :
- Ajouter des fichiers multimédias et des fichiers de données à votre formulaire
- Importer des fichiers et des médias dans KoboToolbox
- Collecter des fichiers et des médias auprès des répondants
- Afficher, télécharger et supprimer les médias soumis par les répondants

## Joindre des fichiers externes et des médias à votre formulaire

KoboToolbox vous permet d'**importer des fichiers multimédias** dans votre formulaire, tels que des images, des enregistrements audio et des vidéos, pour aider les répondants à mieux comprendre les questions et réduire le besoin de clarifications ultérieures.

KoboToolbox vous permet également de **joindre des fichiers CSV externes** à votre formulaire pour gérer de longues listes de choix ou prendre en charge la logique de formulaire. L'utilisation de fichiers externes facilite la réutilisation et la mise à jour des bases de données sans modifier le formulaire lui-même, réduisant ainsi la maintenance continue du formulaire et favorisant une collecte de données cohérente et de qualité.

Les sections ci-dessous présentent ces fonctionnalités et renvoient aux articles d'aide correspondants.

### Ajouter des médias à votre formulaire

Inclure des images, des vidéos ou des enregistrements audio dans les notes, les questions et les choix de votre formulaire peut contribuer à le rendre **plus engageant et accessible.** Cela peut être particulièrement utile pour les utilisateurs ayant des déficiences visuelles ou des difficultés de lecture.

![Formulaire avec médias](images/project_files_media/form.png)

Pour inclure des médias dans votre formulaire, vous devez utiliser XLSForm, puis [importer le XLSForm](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html) dans KoboToolbox. L'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** ne permet pas actuellement d'ajouter des fichiers multimédias directement dans l'éditeur de formulaires.

<p class="note">
  Pour apprendre à inclure des images, des vidéos ou des enregistrements audio dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/media.html">Ajouter des médias à un XLSForm</a>.
</p>

### Joindre des fichiers de données externes à votre formulaire

En plus d'importer des fichiers multimédias, KoboToolbox permet de joindre des fichiers de données externes à vos formulaires afin de récupérer ou de référencer des données externes lors de la collecte de données.

Il existe deux principales façons de connecter votre formulaire à des fichiers externes :

- La fonction `pulldata()` **extrait des informations d'un fichier de données externe** pendant qu'un formulaire est en cours de remplissage. Cela est utile pour référencer des bases de données existantes et réduire la saisie répétée de données par les enquêteurs.

<p class="note">
<strong>Note :</strong> La fonction <code>pulldata()</code> utilise des fichiers externes comme source de données. Si vous souhaitez référencer des données provenant d'un autre projet KoboToolbox plutôt que d'un fichier CSV, vous pouvez utiliser la <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment.html">liaison dynamique de projets</a>.
</p>

- Les types de questions `select_one_from_file` et `select_multiple_from_file` vous permettent de **définir des listes de choix dans un fichier externe** plutôt que directement dans le formulaire. L'utilisation de fichiers externes pour les listes de choix facilite la gestion de longues listes, leur réutilisation dans plusieurs formulaires et leur mise à jour au fil du temps.

Les formats de fichiers disponibles pour ces fonctionnalités sont CSV, XML et GeoJSON.

<p class="note">
  Pour apprendre à joindre des bases de données externes à votre formulaire, consultez les articles <a href="https://support.kobotoolbox.org/fr/pull_data_kobotoolbox.html">Extraire des données d'un fichier CSV externe</a> et <a href="https://support.kobotoolbox.org/fr/external_file.html">Sélectionner des options à partir de fichiers externes dans le Formbuilder</a>.
</p>

### Importer des fichiers et des médias dans KoboToolbox

Après avoir ajouté des références multimédias ou des fichiers externes à votre formulaire, vous devez importer ces fichiers dans votre projet. Cette opération s'effectue depuis la page **PARAMÈTRES > Média** de votre projet.

<p class="note">
Pour apprendre à importer des fichiers et des médias dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/upload_media.html">Importer des fichiers multimédias dans un projet</a>.
</p>

Les types de fichiers suivants sont actuellement disponibles pour l'importation dans KoboToolbox :

| Média | Types |
|:-----|:------|
| Image | .jpeg, .png, .svg |
| Audio | .aac, .aacp, .flac, .mp3, .mp4, .mpeg, .ogg, .wav, .webm, .x-m4a, .x-wav |
| Vidéo | .3gpp, .avi, .flv, .mov, .mp4, .ogg, .qtff, .webm, .wmv |
| Fichier | .csv, .xml, .zip, .geojson |

<p class="note">
<strong>Note :</strong> La taille maximale des fichiers importés est de 100 Mo. Les fichiers dépassant cette limite doivent être réduits avant l'importation.
</p>

## Collecter des fichiers et des médias auprès des répondants

En plus d'inclure des médias dans votre formulaire, vous pouvez collecter des fichiers et des médias directement auprès des répondants lors de la collecte de données. Cela inclut **des images, des enregistrements audio, des vidéos et d'autres types de fichiers.** La collecte de médias vous permet de recueillir des informations qualitatives qui apportent un contexte visuel ou audio à vos données.

<p class="note">
<strong>Note :</strong> Chaque fichier soumis par un répondant peut avoir une taille maximale de 10 Mo, avec un total maximum de 100 Mo par soumission.
</p>

Les types de questions multimédias suivants sont disponibles dans KoboToolbox :

| Type de question dans le Formbuilder | Type de question XLSForm | Description |
|:-------------------------------------|:-------------------------|:------------|
| Photographie | `image` | Capturer ou importer une image. Peut également être utilisé pour collecter des [dessins, des images annotées et des signatures](https://support.kobotoolbox.org/fr/photo_audio_video_file.html#advanced-appearances). |
| Audio | `audio` | Enregistrer ou importer un fichier audio. |
| Vidéo | `video` | Enregistrer ou importer un fichier vidéo. |
| Fichier | `file` | Joindre un fichier (ex. : .pdf, .docx). |

KoboToolbox permet également l'enregistrement audio d'arrière-plan pour des entretiens complets ou des discussions de groupe.

<p class="note">
  Pour en savoir plus sur la collecte de médias auprès des répondants, consultez l'article <a href="https://support.kobotoolbox.org/fr/photo_audio_video_file.html">Questions multimédias dans KoboToolbox</a>. Pour en savoir plus sur l'enregistrement audio d'arrière-plan, consultez l'article <a href="https://support.kobotoolbox.org/fr/recording-interviews.html#recording-interviews-with-background-audio-recordings">Collecter des données qualitatives avec KoboToolbox</a>.
</p>

### Afficher les fichiers multimédias soumis par les répondants

Tous les fichiers multimédias soumis par les répondants peuvent être consultés depuis le tableau de données. Les images peuvent également être affichées dans la vue **Galerie photo** de votre projet.

<p class="note">
  Pour en savoir plus sur l'affichage des médias soumis par les répondants, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#viewing-media-files">Gérer les réponses média soumises par les répondants</a>.
</p>

### Télécharger les fichiers multimédias soumis par les répondants

Vous pouvez télécharger les fichiers multimédias individuellement depuis le tableau de données, ou en masse depuis la page **Téléchargements**.

Lorsque vous exportez vos données au format CSV ou XLS, le fichier exporté inclut également des hyperliens permettant d'ouvrir les fichiers multimédias associés dans un navigateur web, à condition que l'option par défaut **Inclure les URL des médias** soit sélectionnée.

<p class="note">
  Pour en savoir plus sur l'exportation de vos fichiers multimédias, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#downloading-media-files">Gérer les réponses média soumises par les répondants</a>.
</p>

### Supprimer les fichiers multimédias soumis par les répondants

Enfin, vous pouvez avoir besoin de supprimer des fichiers multimédias pour **gérer le stockage, protéger la confidentialité ou corriger des erreurs de soumission.** Les fichiers multimédias peuvent être supprimés individuellement ou en masse.

Une fois un fichier supprimé, il est marqué comme *Supprimé* dans le tableau de données et ne peut pas être récupéré.

<p class="note">
  Pour en savoir plus sur les différentes méthodes de suppression de fichiers multimédias, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#deleting-media-files">Supprimer vos fichiers multimédias</a>.
</p>