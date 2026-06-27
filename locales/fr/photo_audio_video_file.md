# Questions multimédias dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/cfb4a1f8edd217a9c0ed64bd0bfc86e6fda70baa/source/photo_audio_video_file.md" class="reference">6 mai 2026</a>

De nombreux projets de collecte de données nécessitent plus que de simples données quantitatives. KoboToolbox vous permet de recueillir divers fichiers multimédias auprès des répondants, notamment des photos, des enregistrements audio, des vidéos et des fichiers, afin d'apporter des informations qualitatives clés et d'enrichir vos bases de données sur les plans visuel et sonore.

La méthode de capture ou d'importation de fichiers multimédias dépend de l'outil utilisé pour la collecte de données : [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html) ou [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html). Avec KoboCollect ou les formulaires web sur un appareil mobile, vous pouvez capturer des images ou des vidéos directement depuis l'appareil ou importer des fichiers. Avec les formulaires web sur un ordinateur, vous pouvez uniquement importer des images ou des vidéos. Dans tous les cas, vous pouvez enregistrer de l'audio directement dans le formulaire.

Cet article couvre les sujets suivants :
- Types de questions multimédias disponibles dans KoboToolbox
- Ajout de questions multimédias dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**
- Apparences par défaut et avancées des questions multimédias
- Paramètres des questions multimédias

## Types de questions multimédias

Les types de questions multimédias suivants sont disponibles dans le Formbuilder :

| Type de question | Description |
|:-----------------|:------------|
| Photographie | Capturer ou importer une image |
| Audio | Enregistrer ou importer un fichier audio |
| Vidéo | Enregistrer ou importer un fichier vidéo |
| Fichier | Joindre un fichier (ex. : .pdf, .docx) |
| Code-barres / code QR | Scanner des codes-barres et des codes QR à l'aide de l'appareil photo |

<p class="note">
<strong>Note :</strong> KoboToolbox propose également des enregistrements audio d'arrière-plan pour des entretiens complets ou des discussions de groupe. Lorsque l'enregistrement audio d'arrière-plan est actif sur un formulaire, les questions de type <strong>Audio</strong> <strong>dans KoboCollect</strong> sont désactivées, car il n'est pas possible d'enregistrer de l'audio avec les deux fonctionnalités simultanément. Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/recording-interviews.html#recording-interviews-with-background-audio-recordings">Collecter des données qualitatives avec KoboToolbox</a>.
</p>

## Ajout de questions multimédias dans le Formbuilder

Pour ajouter une question multimédia à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ AJOUTER UNE QUESTION.**
4. Choisissez le type de question approprié.

![Ajouter une question multimédia dans le Formbuilder](images/photo_audio_video_file/media.png)

## Apparences des questions multimédias

Les questions multimédias peuvent s'afficher différemment selon que vous utilisez des formulaires web ou KoboCollect. Vous pouvez également modifier l'apparence par défaut des questions multimédias. Cette section décrit comment chaque type de question s'affiche sur les deux plateformes, y compris les options d'apparence par défaut et avancées.

### Apparences par défaut

Le tableau ci-dessous montre comment les questions multimédias s'affichent par défaut dans les formulaires web et dans KoboCollect.

![Apparences par défaut des questions multimédias](images/photo_audio_video_file/table_updated.png)

<p class="note">
<strong>Note :</strong> Les questions de type Code-barres / code QR sont uniquement disponibles dans <a href="https://support.kobotoolbox.org/fr/data_collection_kobocollect.html">KoboCollect</a> sur les appareils mobiles. Lorsqu'un code est scanné à l'aide de l'appareil photo, la valeur encodée dans le code-barres ou le code QR est automatiquement capturée. Dans les <a href="https://support.kobotoolbox.org/fr/data_through_webforms.html">formulaires web</a>, ce type de question s'affiche comme un champ texte standard, dans lequel les répondants doivent saisir la valeur manuellement.
</p>

### Apparences avancées

Vous pouvez appliquer des apparences avancées aux questions de type **Photographie** et **Code-barres / code QR** pour modifier leur affichage et leur comportement dans votre formulaire. Les apparences avancées pour les questions de type **Photographie** permettent aux utilisateurs d'aller au-delà de la simple importation ou capture d'une image : ils peuvent notamment réaliser des croquis, ajouter des signatures, annoter des images et prendre des selfies directement dans le formulaire.

Pour ajouter une apparence avancée :

1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accéderez alors à l'onglet **Options des questions**.
2. Dans **Apparence (avancée)**, choisissez l'apparence souhaitée.

    - Si l'apparence n'est pas répertoriée, sélectionnez **Autre** et saisissez le nom de l'apparence dans la zone de texte, exactement tel qu'il est indiqué ci-dessus.

![Apparences de questions](images/photo_audio_video_file/appearances.png)

Les apparences disponibles pour les questions de type **Photographie** sont les suivantes :

| Apparence | Description |
|:----------|:------------|
| `signature` | Permet à l'utilisateur de capturer une signature en signant directement sur l'écran de l'appareil (ex. : pour les formulaires nécessitant une signature numérique à des fins de vérification). |
| `draw` | Permet aux utilisateurs de réaliser des croquis ou des dessins directement sur l'écran de l'appareil (ex. : pour capturer des illustrations ou des cartes dessinées à la main). |
| `annotate` | Permet à l'utilisateur d'annoter une image en y dessinant ou en y écrivant. |
| `new` (autre) | Invite l'utilisateur à prendre une nouvelle photo à l'aide de l'appareil photo de l'appareil (disponible uniquement avec KoboCollect). |
| `new-front` (autre) | Invite l'utilisateur à prendre une nouvelle photo à l'aide de l'appareil photo frontal de l'appareil (disponible uniquement avec KoboCollect). |

Pour les questions de type **Code-barres / code QR**, une seule apparence avancée est disponible :

| Apparence | Description |
|:----------|:------------|
| `front` | Bascule de l'appareil photo arrière par défaut vers l'appareil photo frontal. |

## Paramètres des questions multimédias

Au-delà de leur fonction de base, les questions multimédias offrent également des paramètres avancés permettant de gérer la taille des fichiers et de restreindre les types de fichiers acceptés.

<p class="note">
<strong>Note :</strong> Chaque fichier importé par un répondant peut avoir une taille maximale de 10 Mo, avec un total maximum de 100 Mo par soumission.
</p>

### Réduction de la taille des images

Si votre projet implique la collecte d'un volume important de fichiers multimédias, vous pourriez rencontrer des difficultés pour importer des fichiers dans KoboToolbox, selon votre débit internet. Les utilisateurs du [plan Community](https://www.kobotoolbox.org/pricing/) sont également limités à 1 Go de stockage de fichiers gratuit. Il est donc conseillé de gérer la taille des fichiers multimédias que vous collectez.

Pour définir la taille maximale des images collectées à l'aide du type de question **Photographie** :

1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accéderez alors à l'onglet **Options des questions**.
2. Définissez le paramètre **max-pixels** sur la valeur de votre choix (ex. : 1000).

![image](images/photo_audio_video_file/parameters.png)

<p class="note">
<strong>Note :</strong> Vous pouvez également configurer la résolution vidéo et la taille des images dans les <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">paramètres KoboCollect</a>.
</p>

### Restriction des types de fichiers acceptés

Par défaut, le type de question **Fichier** accepte tous les types de fichiers. Pour restreindre les types de fichiers acceptés par cette question :

1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accéderez alors à l'onglet **Options des questions**.
2. Dans la zone de texte **Fichiers acceptés**, listez les extensions de fichiers que vous souhaitez autoriser, séparées par une virgule (ex. : .doc, .pdf, .xlsx).

![image](images/photo_audio_video_file/files.png)

## Résolution de problèmes

<details>
  <summary><strong>Collecter plusieurs images ou fichiers multimédias</strong></summary>
  Les types de questions multimédias ne permettent l'importation que d'un seul fichier à la fois. Pour permettre aux utilisateurs d'importer plusieurs fichiers, vous pouvez placer la question multimédia dans un groupe répété, ou dupliquer la question multimédia dans le formulaire autant de fois que nécessaire. Vous pouvez utiliser la <a href="https://support.kobotoolbox.org/fr/skip_logic.html">logique de saut</a> pour afficher les questions multimédias suivantes uniquement si la précédente n'est pas vide.
</details>

<br>

<details>
  <summary><strong>L'enregistrement audio dans un formulaire web bloque l'accès aux autres questions</strong></summary>
  Lorsqu'un utilisateur enregistre une réponse à une question audio dans un formulaire web, les autres questions sont verrouillées jusqu'à la fin de l'enregistrement. Cela garantit que l'audio est entièrement capturé avant que l'utilisateur ne poursuive le reste du formulaire.
</details>

<br>

<details>
  <summary><strong>Collecter des données EXIF à partir d'images importées</strong></summary>
  Lorsque des images sont importées via des formulaires web ou KoboToolbox, les données EXIF ne sont pas conservées par défaut. Pour conserver les données EXIF, utilisez un type de question <strong>Fichier</strong> et définissez le paramètre <strong>Fichiers acceptés</strong> (<code>body::accept</code> dans XLSForm) sur <code>.jpg, .jpeg, .png</code>.
</details>

<br>

<details>
  <summary><strong>Formats de codes-barres / codes QR pris en charge</strong></summary>
KoboCollect fonctionne avec un large éventail de formats de codes-barres et de codes QR, notamment UPC-A, UPC-E, EAN-8, EAN-13, Code 39, Code 93, Code 128, Codabar, ITF, RSS-14, RSS-Expanded, QR Code, Data Matrix, Aztec, PDF 417 et MaxiCode. Si un code-barres ne peut pas être scanné, vérifiez qu'il utilise l'un de ces formats compatibles.
</details>