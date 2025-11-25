# Types de questions « Photo », « Audio », « Vidéo » et « Fichier »
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/27c3e37a283d79de0cbecebbf3a41d5b6ba6d7df/source/photo_audio_video_file.md" class="reference">11 Sep 2023</a>

Avec KoboToolbox, vous pouvez collecter différents types de médias dans le cadre de votre projet de collecte de données.

Lorsque vous souhaitez capturer des images dans vos soumissions, utilisez le type de question « Photo ».

Si une question nécessite que vous enregistriez ou joigniez un fichier audio, par exemple lorsqu'une longue explication est attendue de la part du répondant ou de la répondante, utilisez le type de question « Audio ». La dernière version de KoboCollect vous permet d'enregistrer de l'audio directement dans l'application sans ouvrir une application distincte.

Avec le type de question « Vidéo », vous pourrez enregistrer une vidéo à l'aide de la caméra de l'appareil ou joindre un fichier vidéo.

Si une question nécessite que vous joigniez un fichier tel qu'un PDF, vous pouvez utiliser le type de question « Fichier ».

## Comment configurer les types de questions « Photo », « Audio », « Vidéo » et « Fichier »

### Configuration dans l'interface de création de formulaires

Ajouter des questions média est simple :

- Cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question
- Saisissez le texte de la question, par exemple « Prenez une photo de l'unité d'habitation », puis cliquez sur **AJOUTER UNE QUESTION** ou appuyez sur ENTRÉE sur votre clavier
- Choisissez le type de question

![Adding media question](images/photo_audio_video_file/add.gif)

### Configuration dans XLSForm

Pour ajouter des questions média dans XLSForm, utilisez les types de questions `image`, `audio`, `video` ou `file` comme indiqué dans l'exemple suivant :

| type   | name        | label                                                                | hint                    |
| :----- | :---------- | :------------------------------------------------------------------- | :---------------------- |
| image  | house_photo | Prenez une photo de l'unité d'habitation                             |                         |
| audio  | impact      | Quel a été l'impact du projet sur votre ménage ?                     | Enregistrer comme audio |
| video  | preparation | Enregistrez une vidéo du répondant pendant qu'il prépare le VitaMeal |                         |
| file   | CV          | Joignez votre CV                                                     |                         |
| survey |

## Apparence des types de questions « Photo », « Audio », « Vidéo » et « Fichier »

### Apparence par défaut

![Default appearances](images/photo_audio_video_file/default_appearances.png)

### Apparences avancées pour le type de question « Photo »

Lors de l'ajout du type de question « Photo », vous pouvez choisir parmi plusieurs apparences (dans les paramètres de la question). Les apparences modifient la façon dont la question est affichée dans les formulaires web et KoboCollect.

![Advanced appearances for photo question type](images/photo_audio_video_file/advanced_appearances_photo.png)

![Advanced appearances](images/photo_audio_video_file/advanced_appearances.png)

### Ajout d'apparences avancées dans XLSForm

Vous pouvez spécifier les apparences avancées de la question « Photo » dans XLSForm sous la colonne appearance comme indiqué dans l'exemple suivant :

| type   | name       | label                         | appearance |
| :----- | :--------- | :---------------------------- | :--------- |
| image  | sign       | Signez ici                    | signature  |
| image  | drawing    | Dessinez ici                  | draw       |
| image  | annotation | Prenez une image et annotez-la | annotate   |
| survey |

## Enregistrement audio en arrière-plan

Vous pouvez enregistrer de l'audio en arrière-plan lorsque vous ouvrez le formulaire dans KoboCollect. Cela peut être utile dans plusieurs scénarios de collecte de données, notamment les discussions de groupe et les entretiens avec des informateurs et informatrices clés.

Activez l'enregistrement audio en arrière-plan dans l'interface de création de formulaires en cliquant sur **Mise en page et paramètres** et en activant la fonctionnalité.

![Background audio](images/photo_audio_video_file/background_audio.png)

<p class="note">
  L'enregistrement audio en arrière-plan est uniquement disponible dans KoboCollect et <strong>non</strong> dans les formulaires web Enketo.
</p>

Dans XLSForm, vous pouvez activer l'enregistrement en arrière-plan avec le type de question `background-audio`. Il s'agit d'un type de question « méta » et par conséquent aucun `label` n'est requis, seulement un `name`. La qualité audio peut être configurée dans la colonne `parameters`, comme expliqué [ici](recording-interviews.md).

| type             | name             | label |
| :--------------- | :--------------- | :---- |
| background-audio | background_audio |       |
| survey           |

<p class="note">
  Il n'est pas possible d'enregistrer de l'audio en utilisant le type de question « Audio » pendant qu'un enregistrement audio en arrière-plan est en cours sur le formulaire. Lorsque l'enregistrement audio en arrière-plan est activé, tous les types de questions « Audio » sont désactivés.
</p>

Vous pouvez en savoir plus sur l'enregistrement audio en arrière-plan [ici](recording-interviews.md).

## Réduire la taille des fichiers média collectés

Si vous collectez beaucoup de médias dans votre projet, vous pourriez rencontrer des difficultés pour les importer dans KoboToolbox en fonction de la vitesse de votre connexion Internet. Si vous utilisez Le serveur KoboToolbox mondial ou Le serveur KoboToolbox Union européenne, vous êtes également limité à seulement 1 Go de stockage gratuit. Il est judicieux de gérer la taille des fichiers média collectés tels que les images, l'audio et les vidéos.

Vous pouvez définir la taille maximale des images que vous collectez en utilisant le type de question « Photo » en accédant aux paramètres de la question et en définissant le paramètre « max-pixels » dans l'interface de création de formulaires.

![Max pixels](images/photo_audio_video_file/max-pixels.png)

Dans XLSForm, vous pouvez faire de même en ajoutant « max-pixels » dans la colonne `parameters` comme suit :

| type   | name  | label           | parameters     |
| :----- | :---- | :-------------- | :------------- |
| image  | photo | Capturer photo  | max-pixels=480 |
| survey |

Dans KoboCollect, vous pouvez également choisir la qualité vidéo et la taille des photos via la section Gestion des formulaires des paramètres du projet.

Vous pouvez en savoir plus sur la façon de réduire la taille des fichiers [ici](lower_file_size.md).

## Limiter les types de fichiers acceptés pour le type de question « Fichier »

Tous les types de fichiers sont acceptés par défaut pour le type de question « Fichier ». Dans l'interface de création de formulaires, vous pouvez restreindre cela en procédant comme suit :

- Accédez aux paramètres de la question « Fichier »
- Dans la case « Fichiers acceptés », saisissez les extensions de fichiers que vous souhaitez autoriser, séparées par une virgule, par exemple « .doc, .pdf, .xlsx »

![File types](images/photo_audio_video_file/file_types.png)

Dans XLSForm, vous pouvez limiter les types de fichiers acceptés en spécifiant les extensions de fichiers dans la colonne `body::accept` comme suit :

| type   | name | label          | body::accept |
| :----- | :--- | :------------- | :----------- |
| file   | CV   | Joignez votre CV | .pdf, .doc   |
| survey |

<p class="note">
  Téléchargez un XLSForm avec des exemples de cet article <a download class="reference" href="./_static/files/photo_audio_video_file/media_question_types.xlsx">ici</a>.
</p>