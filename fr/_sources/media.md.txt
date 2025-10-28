# Ajouter différents types de médias (image, audio, vidéo) à un formulaire
<a href="../media.html">Read in English</a> | <a href="../es/media.html">Leer en español</a> | <a href="../ar/media.html">اقرأ باللغة العربية</a>

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/media.md" class="reference">15
fév. 2022</a>

En plus des questions textuelles et des choix textuels, vous pouvez également ajouter différents types
de médias (tels que _image_, _audio_ et _vidéo_) à vos formulaires. L'ajout de médias dans
un formulaire peut parfois vous aider à exprimer vos questions et choix
de manière bien meilleure.

Les médias dans un formulaire fonctionnent à la fois sur **l'application Android Collect** et les **formulaires Web
(Enketo)**. Voici les fichiers multimédias actuellement pris en charge :

| Média | Fichiers                                                      |
| :---- | :------------------------------------------------------------ |
| Image | jpeg, png, svg                                                |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Vidéo | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv    |

Cet article d'aide vise à illustrer comment créer des formulaires avec médias avec
**KoboToolbox**. Suivez les instructions décrites ci-dessous pour inclure des médias à votre
projet d'enquête.

## Étape 1 : Télécharger le formulaire en tant que XLSForm

Créez un projet d'enquête dans l'interface de création de formulaires, puis téléchargez votre formulaire au format XLS
pour y ajouter des paramètres multimédias. L'interface de création de formulaires ne prend actuellement pas en charge l'ajout
de médias directement au formulaire, vous devrez donc modifier le XLSForm téléchargé pour
effectuer cette action.

<video controls><source src="./_static/files/media/download_xlsform.mp4" type="video/mp4"></video>

## Étape 2 : Ajouter des colonnes de médias à votre XLSForm

<p class='note'>Les noms de fichiers ajoutés au XLSForm doivent correspondre aux noms de fichiers que vous
avez donnés à vos fichiers <em>image</em>, <em>audio</em> et
<em>vidéo</em>.</p>

### Ajout de colonnes de médias image :

Si vous souhaitez ajouter une **image** à une question, tapez `media::image` comme
en-tête de colonne dans l'onglet **survey** de votre XLSForm. Tapez le nom du fichier image
avec son extension pour la question appropriée juste sous l'en-tête de colonne
`media::image`.

De même, si vous souhaitez ajouter une **image** à un choix, tapez
`media::image` comme en-tête de colonne dans l'onglet **choices** de votre XLSForm. Tapez à nouveau le nom du fichier image
avec son extension pour le choix approprié
juste sous l'en-tête de colonne `media::image`.

<video controls><source src="./_static/files/media/adding_media_image.mp4" type="video/mp4"></video>

### Ajout de colonnes de médias audio :

Si vous souhaitez ajouter de l'**audio** à une question, tapez `media::audio` comme en-tête de colonne
dans l'onglet **survey** de votre XLSForm. Tapez le nom du fichier audio avec
son extension pour la question appropriée juste sous l'en-tête de colonne
`media::audio`.

De même, si vous souhaitez ajouter de l'**audio** à un choix, tapez `media::audio` comme
en-tête de colonne dans l'onglet **choices** de votre XLSForm. Tapez à nouveau le nom du
fichier audio avec son extension pour le choix approprié juste sous l'en-tête de colonne
`media::audio`.

<video controls><source src="./_static/files/media/adding_media_audio.mp4" type="video/mp4"></video>

### Ajout de colonnes de médias vidéo :

Si vous souhaitez ajouter une vidéo à une question, tapez `media::video` comme en-tête de colonne
dans l'onglet **survey** de votre XLSForm. Tapez le nom du fichier vidéo avec
son extension pour la question appropriée juste sous l'en-tête de colonne
`media::video`.

De même, si vous souhaitez ajouter une vidéo à un choix, tapez `media::video` comme
en-tête de colonne dans l'onglet **choices** de votre XLSForm. Tapez à nouveau le nom du fichier vidéo
avec son extension pour le choix approprié juste sous l'en-tête de colonne
`media::video`.

<video controls><source src="./_static/files/media/adding_media_video.mp4" type="video/mp4"></video>

## Étape 3 : Gérer les colonnes de médias pour plusieurs langues

<p class='note'>Cette étape concerne celles et ceux qui ont plusieurs langues dans leur projet
d'enquête.</p>

Vous pouvez avoir une enquête avec plusieurs langues et souhaiter ajouter différents types de
médias pertinents pour des langues spécifiques. Dans de tels cas, vous pouvez suivre les
illustrations fournies ci-dessous.

### Gestion de la colonne de médias pour les médias image :

Si vous souhaitez ajouter une image à une question, tapez `media::image` comme en-tête de colonne
dans l'onglet **survey** de votre XLSForm. Tapez le nom du fichier image avec
son extension pour la question appropriée juste sous l'en-tête de colonne
`media::image::Language (code de langue)`.

De même, si vous souhaitez ajouter une image à un choix, tapez
`media::image::Language (code de langue)` comme en-tête de colonne dans l'onglet **choices**
de votre XLSForm. Tapez à nouveau le nom du fichier image avec son extension
pour le choix approprié juste sous l'en-tête de colonne
`media::image::Language (code de langue)`.

<video controls><source src="./_static/files/media/adding_media_image_language.mp4" type="video/mp4"></video>

### Gestion de la colonne de médias pour les médias audio :

Si vous souhaitez ajouter de l'audio à une question, tapez
`media::audio::Language (code de langue)` comme en-tête de colonne dans l'onglet **survey**
de votre XLSForm. Tapez le nom du fichier audio avec son extension pour la
question appropriée juste sous l'en-tête de colonne
`media::audio::Language (code de langue)`.

De même, si vous souhaitez ajouter de l'audio à un choix, tapez
`media::audio::Language (code de langue)` comme en-tête de colonne dans l'onglet **choices**
de votre XLSForm. Tapez à nouveau le nom du fichier audio avec son extension
pour le choix approprié juste sous l'en-tête de colonne
`media::audio::Language (code de langue)`.

<video controls><source src="./_static/files/media/adding_media_audio_language.mp4" type="video/mp4"></video>

### Gestion de la colonne de médias pour les médias vidéo :

Si vous souhaitez ajouter une vidéo à une question, tapez
`media::video::Language (code de langue)` comme en-tête de colonne dans l'onglet **survey**
de votre XLSForm. Tapez le nom du fichier vidéo avec son extension pour la
question appropriée juste sous l'en-tête de colonne
`media::video::Language (code de langue)`.

De même, si vous souhaitez ajouter une vidéo à un choix, tapez
`media::video::Language (code de langue)` comme en-tête de colonne dans l'onglet **choices**
de votre XLSForm. Tapez à nouveau le nom du fichier vidéo avec son extension
pour le choix approprié juste sous l'en-tête de colonne
`media::video::Language (code de langue)`.

<video controls><source src="./_static/files/media/adding_media_video_language.mp4" type="video/mp4"></video>

## Étape 4 : Remplacer le XLSForm

Importez et remplacez votre XLSForm dans le projet existant ou créez un nouveau
projet.

<video controls><source src="./_static/files/media/replacing_xlsform.mp4" type="video/mp4"></video>

## Étape 5 : Importer les fichiers multimédias

Allez dans **PARAMÈTRES>Médias**. Importez tous les fichiers multimédias qui ont été référencés dans
votre formulaire.

<video controls><source src="./_static/files/media/uploading_media.mp4" type="video/mp4"></video>

<p class='note'><strong>Astuce :</strong> Rassemblez tous les fichiers multimédias que vous inclurez dans votre projet
d'enquête. Donnez un nom de fichier court à chacun des médias. Les noms de fichiers
avec un espace (par exemple, « red book ») ne sont pas pris en charge par le système. Par conséquent,
vous devrez soit supprimer l'espace entre les noms (par exemple,
« redbook »), soit utiliser « _ » pour un espace (par exemple, « red_book »).</p>

## Étape 6 : Déployer le formulaire

Une fois que vous avez remplacé le XLSForm puis importé tous les fichiers multimédias, vous
devrez déployer votre enquête.

<video controls><source src="./_static/files/media/deploying_form.mp4" type="video/mp4"></video>

<p class='note'>Chaque fois que de nouveaux fichiers multimédias sont ajoutés ou modifiés, vous devez
<strong>redéployer</strong> votre projet pour que la modification prenne effet.
Vous pouvez voir vos nouveaux médias lors de la prévisualisation de votre formulaire
<em>avant</em> le redéploiement.</p>

## Étape 7 : Collecter des données

Vous pouvez maintenant retourner dans **Formulaire>Collecter des données**, puis cliquer sur **Ouvrir** pour vérifier
si les médias sont correctement affichés.

<video controls><source src="./_static/files/media/collecting_data.mp4" type="video/mp4"></video>

<p class='note'>Les fichiers GIF animés ne sont actuellement pas pris en charge par Enketo ou
l'application Android Collect. L'alignement des médias à un emplacement souhaité du formulaire (alignement à gauche,
alignement au centre ou alignement à droite) n'est pas non plus
possible.</p>

## Trucs et astuces

### Identifier le nom de fichier, l'extension et la taille d'un fichier multimédia sur Windows

-   Sélectionnez un fichier multimédia (image, audio ou vidéo).
-   Faites un clic droit avec votre souris lorsque le fichier multimédia est toujours sélectionné.

![Dropdown select properties](images/media/dropdown_select_properties.png)

-   Puis sélectionnez **Propriétés**.
-   Vous devriez maintenant pouvoir voir le *nom de fichier* et l'*extension* du fichier
    multimédia sous l'onglet **Général**.

![Image properties](images/media/image_properties.png)

-   Vous devriez également pouvoir identifier les dimensions et la taille du média sous l'onglet
    **Détails**. Si vous souhaitez avoir de petites images dans votre question ou
    vos choix, vous devrez importer des médias avec une dimension plus petite, ou
    vice-versa.

<p class='note'>Les médias dans un formulaire Enketo prendront plus de temps à se charger si vous
avez des fichiers volumineux. Essayez de réduire la taille des fichiers image, vidéo ou audio
avant de les importer sur le serveur.</p>

![Image details](images/media/image_details.png)

<p class='note'>Vous pouvez accéder au XLSForm <a download class='reference'
href='./_static/files/media/xlsform-example.xls'>ici</a> et aux fichiers multimédias <a
download class='reference'
href='./_static/files/media/xlsform-example-media.zip'>ici</a> qui ont été utilisés
dans cet article.</p>