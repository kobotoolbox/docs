# Importer des fichiers multimédias dans un projet
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/d9b44de6b0f7192771a9f7bf86edf271321f398b/source/upload_media.md" class="reference">27 Jan 2026</a>

KoboToolbox vous permet d'importer des fichiers multimédias et des fichiers de données externes à utiliser dans vos formulaires lors de la collecte de données. Cet article décrit les types de fichiers disponibles et explique comment importer des fichiers multimédias et des fichiers de données externes dans votre projet depuis votre appareil ou via une URL.

<p class="note">
  Pour en savoir plus sur les fichiers et les médias de projet, consultez l'article <a href="../fr/project_files_media.html">Introduction aux fichiers et aux médias de projet</a>.
</p>

## Types de fichiers pris en charge

KoboToolbox vous permet d'importer les fichiers suivants :
- **Les fichiers multimédias**, tels que des images, des enregistrements audio et des vidéos, pour aider les répondants à mieux comprendre les questions et enrichir votre formulaire.

<p class="note">
  Pour savoir comment inclure des images, des vidéos ou des enregistrements audio dans un XLSForm, consultez l'article <a href="../fr/media.html">Ajouter des médias à un XLSForm</a>.
</p>

- **Les fichiers de données externes**, tels que des fichiers CSV ou XML, pour gérer de grandes listes de choix ou prendre en charge la logique de formulaire. L'utilisation de fichiers externes facilite la réutilisation et la mise à jour des bases de données sans modifier le formulaire lui-même, ce qui réduit la maintenance continue du formulaire et favorise une collecte de données cohérente et de qualité.

<p class="note">
Pour savoir comment associer des bases de données externes à votre formulaire, consultez les articles <a href="../fr/pull_data_kobotoolbox.html">Extraire des données d'un fichier CSV externe</a> et <a href="../fr/select_from_file_xls.html">Sélectionner des options à partir d'un fichier externe avec XLSForm</a>.
</p>

Les fichiers suivants sont actuellement disponibles pour l'importation dans KoboToolbox :
| Type  | Extensions de fichier |
|:-----|:----------------|
| Image | .jpeg, .png, .svg |
| Audio | .aac, .aacp, .flac, .mp3, .mp4, .mpeg, .ogg, .wav, .webm, .x-m4a, .x-wav |
| Vidéo | .3gpp, .avi, .flv, .mov, .mp4, .ogg, .qtff, .webm, .wmv |
| Fichier  | .csv, .xml, .zip, .geojson |

## Importer des fichiers depuis votre appareil

Après avoir ajouté des références à des médias ou des fichiers externes dans votre formulaire, vous devez importer ces fichiers dans votre projet. Cette opération s'effectue depuis la page **PARAMÈTRES > Média** de votre projet.

Pour importer des fichiers et des médias depuis votre appareil :
1. Connectez-vous à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Ouvrez votre projet et accédez à la page **PARAMÈTRES**.
3. Ouvrez l'onglet <i class="k-icon-file-image"></i> **Média**.
4. Importez les fichiers utilisés par votre formulaire. Les noms de fichiers doivent correspondre exactement aux noms référencés dans le formulaire.
5. Déployez ou redéployez le formulaire pour appliquer les modifications.

![Importer des médias](images/upload_media/upload_media.png)

<p class="note">
<strong>Note :</strong> La taille maximale des fichiers à importer est de 100 Mo. Les fichiers dépassant cette limite doivent être réduits avant l'importation.
</p>

## Importer des fichiers via une URL

<iframe src="https://www.youtube.com/embed/MBU77LUrflA?si=_BRYlIlojJGOqnuT&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Vous pouvez également importer un fichier dans KoboToolbox en fournissant une URL directe vers ce fichier. Cette méthode peut être utile si votre fichier est hébergé en ligne, par exemple un fichier CSV stocké dans un dépôt GitHub.

Pour importer des fichiers et des médias via une URL :
1. Connectez-vous à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Ouvrez votre projet et accédez à la page **PARAMÈTRES**.
3. Ouvrez l'onglet <i class="k-icon-file-image"></i> **Média**.
4. Collez une URL valide sous « Vous pouvez également ajouter des fichiers à l'aide d'une URL » (voir les exigences ci-dessous). Cliquez sur **Ajouter**.
5. Déployez ou redéployez le formulaire pour appliquer les modifications.

![Importer une image via URL](images/upload_media/upload_url.png)

<p class="note">
<strong>Note :</strong> Le nom du fichier à la fin de l'URL doit correspondre exactement au nom du fichier référencé dans le formulaire.
</p>

### Exigences relatives à l'URL

L'URL doit satisfaire les deux exigences suivantes :

- L'URL doit se terminer par une extension de fichier prise en charge (par exemple, `.png`, `.jpg` ou `.csv`).
- L'URL doit ouvrir le fichier directement dans votre navigateur, et non une page web contenant le fichier. L'URL ne fonctionnera pas si elle pointe vers une page d'un service tel que Google Drive, GitHub ou Dropbox.

<p class="note">
<strong>Note :</strong> Si le fichier est ultérieurement dépublié ou supprimé, il cessera de fonctionner dans KoboToolbox.
</p>

### Obtenir une URL directe pour les images

Pour les images, utilisez l'adresse directe de l'image depuis le site source.

Pour obtenir une URL d'image utilisable :
1. Ouvrez la page web contenant l'image.
2. Faites un clic droit sur l'image et sélectionnez **Copier l'adresse de l'image** (ou l'option équivalente dans votre navigateur).
    - Vérifiez que l'URL se termine par une extension d'image (par exemple, `.png` ou `.jpg`).
3. Collez l'URL dans votre navigateur pour confirmer qu'elle ouvre l'image directement.

### Obtenir une URL directe pour les fichiers CSV

Pour les fichiers `.csv`, l'URL doit ouvrir le contenu CSV brut directement dans votre navigateur. Une approche courante consiste à héberger le fichier CSV sur GitHub et à utiliser le lien Raw :

1. Importez ou déposez votre fichier `.csv` dans un dépôt GitHub.
2. Ouvrez le fichier CSV dans GitHub.
3. Cliquez sur **Raw**. Le contenu CSV doit s'afficher directement dans votre navigateur.
4. Copiez l'URL depuis la barre d'adresse de votre navigateur.

<p class="note">
<strong>Note :</strong> La publication d'un fichier Google Sheets au format CSV n'est pas disponible pour ce flux de travail, car KoboToolbox n'accepte pas le format produit par cette méthode.
</p>

Si vous mettez à jour le fichier CSV à la même URL, KoboToolbox **reflétera le fichier mis à jour après un court délai.** Pour récupérer les mises à jour de manière plus fiable, nous vous recommandons de redéployer régulièrement le formulaire.

### Référencer les fichiers importés dans votre formulaire

Une fois le fichier disponible dans KoboToolbox, référencez-le de la même manière que pour les autres médias ou fichiers de choix importés :

- Dans les questions `select_one_from_file` ou `select_multiple_from_file`
- Dans la fonction `pulldata()`
- Dans les colonnes média de votre XLSForm (`image`, `audio`, `video`)

Lorsque vous faites référence aux fichiers importés, utilisez **uniquement le nom du fichier et son extension** à la fin de l'URL (par exemple, `choices.csv` ou `photo.jpg`). N'incluez pas l'URL complète dans ces champs.