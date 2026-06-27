# Ajouter des médias à un XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/media.md" class="reference">23 Apr 2026</a>

<iframe src="https://www.youtube.com/embed/7TrVmKIuCa8?si=QCr1IzvDXaASEZg7&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


KoboToolbox vous permet d'ajouter des médias, notamment des **images**, des **fichiers audio** et des **vidéos**, aux notes, questions et choix de votre formulaire. L'ajout de médias peut accroître l'engagement des utilisateurs et rendre les formulaires plus accessibles aux personnes malvoyantes ou ayant des difficultés de lecture.

Les médias au sein du formulaire fonctionnent avec [KoboCollect](../fr/data_collection_kobocollect.md) et les [formulaires web](../fr/data_through_webforms.md). Les types de fichiers médias suivants sont actuellement disponibles :

| Média | Fichiers |
| :--- | :--- |
| Image | jpeg, png, svg |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Vidéo | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv |

Cet article couvre les sujets suivants :
- Ajouter des médias aux questions du formulaire
- Ajouter des médias aux choix de réponse
- Ajouter des médias aux traductions du formulaire
- Importer des fichiers médias dans KoboToolbox

<p class="note">
    <strong>Note :</strong> L'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong> ne permet pas d'ajouter des fichiers médias dans vos formulaires. Pour ajouter des médias, vous devez utiliser XLSForm, puis importer votre XLSForm dans KoboToolbox. Pour en savoir plus sur le téléchargement et la modification de votre formulaire en tant que XLSForm, consultez l'article <a href="../fr/xlsform_with_kobotoolbox.md">Utiliser XLSForm avec KoboToolbox</a>.
<br><br>
Pour un apprentissage pratique de l'ajout de fichiers médias dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des médias aux questions dans XLSForm

Pour ajouter des fichiers médias aux questions ou aux notes de votre XLSForm :
1. Ajoutez une nouvelle question dans l'**onglet survey**, en précisant le `type`, le `name` et le `label` (facultatif).
    - Utilisez un type de question `note` si vous souhaitez afficher le fichier média sans collecter de données (par exemple, un logo d'organisation ou une vidéo d'introduction).
    - L'ajout d'un libellé est facultatif lorsqu'un fichier média est inclus.
2. Ajoutez une colonne pour le média que vous souhaitez inclure. Nommez-la `image`, `video` ou `audio`, selon le type de média.
3. Dans la colonne média, sur la ligne de la question que vous avez ajoutée, saisissez le nom exact du fichier média **en incluant l'extension**.
    - Par exemple : `logo.png` ou `intro.mp4`.

**onglet survey**

| type | name | label | image |
| :--- | :--- | :--- | :--- |
| text | Q1 | Dans vos propres mots, comment décririez-vous l'image ci-dessus ? | q1.png |
| survey |

<p class="note">
    <strong>Note :</strong> Auparavant, le format <code>media::file_type</code> était utilisé pour les noms de colonnes médias (par exemple, <code>media::image</code>, <code>media::video</code>, <code>media::audio</code>). Le format simplifié utilisant uniquement le type de média sans le préfixe <code>media::</code> est désormais plus couramment adopté (par exemple, <code>image</code>, <code>video</code>, <code>audio</code>).
</p>

### Importer des fichiers médias dans KoboToolbox

Pour importer les fichiers médias dans KoboToolbox :
1. Connectez-vous à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Dans votre projet KoboToolbox, accédez à **PARAMÈTRES > Média**.
3. Importez les fichiers médias que vous avez ajoutés à votre XLSForm, en vous assurant que le nom du fichier est exactement identique.
4. Déployez ou redéployez votre formulaire pour voir les modifications apportées aux médias.

![Importer des fichiers médias](images/media/upload_media.png)

<p class="note">
    Pour en savoir plus sur l'importation de fichiers médias, consultez l'article <a href="../fr/upload_media.md">Importer des fichiers multimédias dans un projet</a>.
</p>

## Ajouter des médias aux choix de réponse dans XLSForm

Pour ajouter des fichiers médias aux choix de réponse de votre XLSForm :
1. Ajoutez une [question à choix multiple](../fr/question_types_xls.md#select-question-types) dans l'**onglet survey**.
2. Dans l'**onglet choices**, ajoutez un `list_name`, un `name` et un `label` (facultatif) pour vos choix.
    - L'ajout d'un libellé est facultatif lorsqu'un fichier média est inclus. Si vous souhaitez utiliser les fichiers médias comme libellé des options, omettez le texte du libellé.
3. Ajoutez une colonne pour le média que vous souhaitez inclure. Nommez-la `image`, `video` ou `audio`, selon le type de média.
4. Dans la colonne média, sur la ligne des choix que vous avez ajoutés, saisissez le nom du fichier média **en incluant l'extension**.
    - Par exemple : `goat.png` ou `fish.png`

**onglet survey**

| name | type | label |
| :--- | :--- | :--- |
| select_one animals | animals | Lequel de ces animaux préférez-vous ? |
| survey |

**onglet choices**

| list_name | name | label | image |
| :--- | :--- | :--- | :--- |
| animals | goats | Chèvres | goat.png |
| animals | cows | Vaches | cow.png |
| animals | chicken | Poulets | chicken.png |
| animals | pigs | Cochons | pig.png |
| animals | fish | Poissons | fish.png |
| choices |

### Importer des fichiers médias dans KoboToolbox

Pour importer les fichiers médias dans KoboToolbox :
1. Connectez-vous à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Dans votre projet KoboToolbox, accédez à **PARAMÈTRES > Média**.
3. Importez les fichiers médias que vous avez ajoutés à votre XLSForm, en vous assurant que le nom du fichier est exactement identique.
4. Déployez ou redéployez votre formulaire pour voir les modifications apportées aux médias.

## Ajouter des médias aux traductions

Dans les XLSForms [traduits en plusieurs langues](../fr/language_xls.md), vous pouvez inclure différents fichiers médias pour chaque langue en ajoutant de nouvelles colonnes `image`, `audio` ou `video`.

Pour ajouter des fichiers médias pour différentes langues dans votre **onglet survey** :

1. Renommez vos colonnes médias en utilisant le format `type_media::langue (code)`, où `type_media` est le type de fichier média et `langue` est la langue par défaut.
    - Par exemple : `image::English (en)`
2. Ajoutez une nouvelle colonne média pour chaque langue de traduction en utilisant le format `type_media::langue (code)`.
    - Par exemple : `audio::Spanish (es)`
3. Dans la colonne média pour chaque langue, saisissez le nom du fichier média que vous souhaitez inclure, en incluant l'extension.
    - Pour utiliser le même fichier média pour chaque langue, saisissez le même nom de fichier que celui figurant dans la colonne de la langue par défaut.

<p class="note">
    <strong>Note :</strong> Si un fichier média n'est pas renseigné dans une colonne de traduction, il ne sera pas affiché pour cette langue.
</p>

**onglet survey**

| type | name | label | video::English (en) | video::Chichewa (ny) |
| :--- | :--- | :--- | :--- | :--- |
| note | intro | Avant de répondre au formulaire, regardez la vidéo ci-dessous : | intro.mp4 | intro_ny.mp4 |
| survey |

### Importer des fichiers médias dans KoboToolbox

Pour importer les fichiers médias traduits dans KoboToolbox :
1. Connectez-vous à votre [compte KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Dans votre projet KoboToolbox, accédez à **PARAMÈTRES > Média**.
3. Importez les fichiers médias que vous avez ajoutés à votre XLSForm, en vous assurant que le nom du fichier est exactement identique.
4. Déployez ou redéployez votre formulaire pour voir les modifications apportées aux médias.

<p class="note">
    Pour en savoir plus sur la gestion des traductions dans XLSForm, consultez l'article <a href="../fr/language_xls.md">Ajouter des traductions dans XLSForm</a>.
</p>

## Résolution de problèmes

<details>
<summary><strong>Erreur lors du déploiement ou de la visualisation du formulaire</strong></summary>
Si vous rencontrez une erreur lors du déploiement ou de la visualisation de votre formulaire, vérifiez les points suivants :
    <ul>
      <li>Le fichier média a été importé dans KoboToolbox via l'onglet <strong>Média</strong> de la page <strong>PARAMÈTRES</strong>.</li>
      <li>Le nom du fichier dans votre XLSForm correspond exactement au nom et à l'extension du fichier média.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Les fichiers médias n'apparaissent pas dans le formulaire déployé</strong></summary>
Si les fichiers médias n'apparaissent pas dans votre formulaire déployé, vérifiez les points suivants :
    <ul>
      <li>Le fichier média a été importé dans KoboToolbox via l'onglet <strong>Média</strong> de la page <strong>PARAMÈTRES</strong>.</li>
      <li>Le nom du fichier dans votre XLSForm correspond exactement au nom et à l'extension du fichier média.</li>
      <li>Le formulaire a été <strong>redéployé</strong> depuis l'importation des fichiers médias.</li>
      <li>Vous avez inclus des fichiers médias pour chaque traduction du formulaire, le cas échéant.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Modifier la taille d'un fichier média</strong></summary>
Pour contrôler la taille des images affichées dans vos questions ou choix, vous devez importer des fichiers médias avec les dimensions souhaitées. Notez que l'utilisation de fichiers très volumineux peut augmenter les temps de chargement dans les formulaires web.
</details>

<br>

<details>
<summary><strong>Le formulaire met longtemps à se charger</strong></summary>
Les formulaires web se chargent lentement si vos fichiers médias sont volumineux. Réduisez la taille des fichiers image, vidéo ou audio avant de les importer sur le serveur afin d'améliorer les temps de chargement.
</details>

<br>

<details>
<summary><strong>Modifier l'alignement des fichiers médias</strong></summary>
Les médias dans les formulaires KoboToolbox sont centrés par défaut, et un alignement personnalisé (à gauche ou à droite) n'est pas possible.
</details>

<br>

<details>
<summary><strong>Les fichiers GIF animés ne sont pas pris en charge</strong></summary>
Les fichiers GIF animés ne fonctionnent actuellement ni avec les formulaires web ni avec l'application Android KoboCollect.
</details>

<br>

<details>
<summary><strong>Impossible d'importer un fichier média</strong></summary>
La taille maximale pour l'importation de médias est de 100 Mo. Les fichiers dépassant cette limite doivent être réduits avant d'être importés.
</details>