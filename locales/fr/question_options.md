# Options de questions dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/9185596568f1a4124aef66d2d51e31fdd8aed0ba/source/question_options.md" class="reference">23 Apr 2026</a>

Après avoir ajouté une question à votre formulaire, vous pouvez personnaliser **son comportement et son apparence en ajustant ses options de question.** Ces paramètres vous permettent de contrôler diverses options, du nom de variable et des réponses obligatoires aux fonctionnalités d'affichage avancées et au balisage HXL.

Cet article explique comment accéder aux options de questions dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, présente les paramètres disponibles et fournit des conseils sur la manière et le moment d'utiliser chaque option efficacement.

## Accéder aux options de questions dans le Formbuilder

Pour accéder aux options de questions dans le Formbuilder :

1. Cliquez sur <i class="k-icon-settings"></i> **Paramètres** dans le menu à droite de la question.
2. L'onglet **Options des questions** s'ouvre, dans lequel vous pouvez configurer des paramètres supplémentaires pour la question sélectionnée.

![Options de questions](images/question_options/options.png)

## Options disponibles dans le Formbuilder

Les options suivantes sont disponibles pour les questions ajoutées dans le Formbuilder :

| Options | Description |
|:---|:---|
| Indice de question | Texte affiché sous le libellé de la question pour fournir des <a href="https://support.kobotoolbox.org/fr/question_options.html#question-hint">instructions supplémentaires</a> ou des précisions aux répondants. |
| Nom du champ | L'<a href="https://support.kobotoolbox.org/fr/question_options.html#data-column-name">identifiant unique</a> d'une question, utilisé dans la logique de formulaire et comme en-tête de colonne dans le jeu de données exporté. |
| Instructions supplémentaires | Des <a href="https://support.kobotoolbox.org/fr/question_options.html#guidance-hint">notes ou instructions</a> supplémentaires destinées aux enquêteurs ou aux concepteurs de formulaires, non affichées par défaut lors de la collecte de données. |
| Réponse obligatoire | Un paramètre qui détermine si une question <a href="https://support.kobotoolbox.org/fr/question_options.html#mandatory-response">doit recevoir une réponse</a> avant que le répondant puisse continuer ou soumettre le formulaire. |
| Réponse par défaut | Une réponse prédéfinie qui <a href="https://support.kobotoolbox.org/fr/question_options.html#default-response">remplit automatiquement</a> une question et peut être modifiée lors de la collecte de données. |
| Apparence (avancée) | Un paramètre optionnel qui modifie la façon dont une question est <a href="https://support.kobotoolbox.org/fr/question_options.html#appearance-advanced">affichée</a> ou se comporte dans le formulaire. |
| HXL | Un hashtag standardisé utilisé pour <a href="https://support.kobotoolbox.org/fr/question_options.html#hxl">baliser les questions</a> selon le cadre du langage d'échange humanitaire (HXL) afin de favoriser l'interopérabilité et le traitement des données. |
| Fichiers acceptés | Spécifie les <a href="https://support.kobotoolbox.org/fr/photo_audio_video_file.html#restricting-accepted-file-types">types de fichiers</a> pouvant être importés pour une question de type **Fichier**, en indiquant les extensions autorisées séparées par des virgules. |
| Paramètres | Paramètres supplémentaires disponibles pour certains types de questions, permettant de personnaliser le comportement, par exemple en <a href="https://support.kobotoolbox.org/fr/select_one_and_select_many.html#randomizing-option-choices">randomisant les choix de réponse</a> ou en limitant la <a href="https://support.kobotoolbox.org/fr/photo_audio_video_file.html#lowering-image-sizes">taille maximale des images</a>. |
| Fichier des choix | Permet aux utilisateurs de sélectionner le <a href="https://support.kobotoolbox.org/fr/external_file.html#setting-up-the-question-in-the-formbuilder">fichier externe</a> qui servira de source d'options pour les questions **Choix unique à partir d'un fichier** et **Sélectionner plusieurs dans le fichier**. |

<p class="note">
<strong>Note :</strong> Pour des options de personnalisation et des paramètres avancés supplémentaires, <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox">téléchargez votre formulaire en tant que XLSForm</a> et ajoutez des <a href="https://support.kobotoolbox.org/fr/question_options_xls.html">options de questions</a> directement dans le tableur.
</p>

## Nom du champ

Le **nom du champ** est l'identifiant unique de chaque question dans votre formulaire. Il sert de nom de variable utilisé dans la [logique de formulaire](https://support.kobotoolbox.org/fr/form_logic.html#question-referencing) et devient l'en-tête de colonne dans votre jeu de données exporté.

Chaque question doit avoir un nom de champ unique. Dans le Formbuilder, il est généré automatiquement à partir du libellé de la question, mais vous pouvez le personnaliser selon vos besoins. Définir des noms clairs et cohérents avant de déployer votre formulaire permet de s'assurer que votre jeu de données suit une convention de nommage logique.

![Nom du champ](images/question_options/data_column_name.png)

### Points importants concernant les noms de champs

Si vous conservez le **nom de champ généré automatiquement**, il se mettra à jour automatiquement chaque fois que vous modifiez le libellé de la question. Cela peut poser des problèmes si vous avez déjà configuré une logique de formulaire dans du code XLSForm en utilisant le nom de champ précédent, ou si vous avez commencé à collecter des données.

Si le nom de champ d'une question change après le début de la collecte de données, KoboToolbox le traitera comme une nouvelle variable. Cela entraînera deux colonnes distinctes dans votre jeu de données.

Pour cette raison, il est recommandé de **définir et finaliser le nom de champ de chaque question avant de déployer votre formulaire** et de collecter des données. Si vous apportez intentionnellement des modifications importantes à une question et souhaitez qu'elle fonctionne comme une nouvelle variable, vous pouvez mettre à jour le nom de champ en conséquence.

Les noms de champs doivent respecter les règles suivantes :

- Utiliser uniquement des lettres, des chiffres et des tirets bas.
- Le premier caractère doit être une lettre.
- Chaque nom doit être unique dans le formulaire.

<p class="note">
<strong>Note :</strong> Les noms de champs sont utilisés pour référencer les réponses dans la <a href="https://support.kobotoolbox.org/fr/form_logic.html#question-referencing">logique de formulaire</a>. Par exemple, vous pouvez inclure une réponse précédente dans le libellé d'une autre question en utilisant le format <code>${data_column_name}</code>. Ce format est utilisé dans les libellés, la logique de saut, les calculs et les validations. Les noms de champs sont sensibles à l'utilisation de majuscules et de minuscules.
</p>

## Indice de question

Les **indices de question** sont utilisés pour fournir des informations supplémentaires aux répondants ou aux enquêteurs directement dans le formulaire. Ils sont toujours visibles et affichés sous le libellé de la question.

![Indice de question](images/question_options/question_hint.png)

## Instructions supplémentaires

Les **instructions supplémentaires** (guidance hint) sont utilisées pour fournir des informations complémentaires lors du développement du formulaire, de la formation des enquêteurs ou de la collecte de données. Elles ne sont pas affichées par défaut.

![Instructions supplémentaires](images/question_options/guidance_hint_new.png)

### Afficher les instructions supplémentaires dans KoboCollect

Dans les formulaires web, les instructions supplémentaires apparaissent dans une section **Plus de détails** réductible. Dans KoboCollect, elles sont masquées par défaut, mais vous pouvez [modifier les paramètres de votre projet](https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings) pour les afficher en permanence ou dans une section réductible.

Pour afficher les instructions supplémentaires dans KoboCollect, suivez les étapes ci-dessous :

1. Appuyez sur l'**icône du projet** en haut à droite de votre écran.
2. Appuyez sur **Paramètres**.
3. Sous **Gestion des formulaires**, sélectionnez **Afficher les instructions pour les questions**.
4. Choisissez une option d'affichage : **Non**, **Oui - toujours affichées** ou **Oui - réduites**.

<p class="note">
<strong>Note :</strong> Les instructions supplémentaires sont toujours affichées dans les formulaires imprimés.
</p>

## Réponse obligatoire

Par défaut, les questions d'un formulaire sont facultatives. Définir la **Réponse obligatoire** sur **Oui** oblige le répondant à répondre à la question. Cela peut être utile pour s'assurer que les soumissions sont complètes et éviter les données manquantes.

![Réponse obligatoire](images/question_options/mandatory.png)

Si un répondant ne répond pas à une question obligatoire, il ne pourra pas passer à la page suivante ni soumettre le formulaire. Le message d'obligation par défaut "This field is required" sera affiché.

<p class="note">
<strong>Note :</strong> Les conditions de logique de saut ont la priorité sur les paramètres de <strong>Réponse obligatoire</strong>, ce qui signifie que si une question obligatoire est masquée par la logique de saut, il n'est plus nécessaire d'y répondre.
</p>

### Définir une logique personnalisée pour les réponses obligatoires

Une logique de formulaire personnalisée peut être utilisée pour rendre une question obligatoire ou facultative en fonction d'une réponse précédente. Pour mettre en œuvre une logique personnalisée pour les réponses obligatoires :

1. Sélectionnez **Logique personnalisée** à côté de **Réponse obligatoire**.
2. Dans la zone de texte, saisissez la formule XLSForm qui détermine si la question sera obligatoire ou non.

![Logique personnalisée](images/question_options/custom_mandatory.png)

<p class="note">
    Pour en savoir plus sur la logique d'obligation conditionnelle, consultez l'article <a href="https://support.kobotoolbox.org/fr/required_logic_xls.html">Ajouter une logique d'obligation conditionnelle dans XLSForm</a>.
</p>

## Réponse par défaut

Une **réponse par défaut** remplit une question avec une réponse prédéfinie basée sur une réponse courante ou attendue. La réponse par défaut sera enregistrée comme réponse finale lors de la soumission du formulaire, **sauf si elle est modifiée par le répondant** lors de la collecte de données.

![Réponse par défaut](images/question_options/default_response.png)

<p class="note">
<strong>Note :</strong> Bien que les réponses par défaut puissent rendre la collecte de données plus efficace en préremplissant le formulaire avec des réponses attendues ou courantes, elles risquent également d'introduire des biais ou des erreurs dans les données, et doivent être utilisées avec précaution.
</p>

### Format de la réponse par défaut

Le format de la réponse par défaut dépend du type de question et des données collectées :

| Type de question | Format de la réponse par défaut |
|:---|:---|
| Chiffre | Nombre |
| Texte | Texte (sans guillemets) |
| Choix unique | <a href="https://support.kobotoolbox.org/fr/question_types.html#setting-xml-values-for-option-choices">Valeur XML</a> du choix |
| Choix multiple | <a href="https://support.kobotoolbox.org/fr/question_types.html#setting-xml-values-for-option-choices">Valeurs XML</a> des choix, séparées par un espace s'il y en a plusieurs |
| Date | Date au format YYYY-MM-DD. |

## Apparence (avancée)

Les apparences de questions vous permettent de modifier la façon dont une question est affichée et, dans certains cas, la manière dont les répondants interagissent avec elle. Certaines apparences sont uniquement disponibles dans les formulaires web, tandis que d'autres fonctionnent uniquement dans KoboCollect.

![Apparence avancée](images/question_options/appearance.png)

Les apparences disponibles varient selon le type de question. Consultez l'article d'aide correspondant à chaque type de question pour voir toutes les apparences disponibles.

## HXL

HXL, ou **langage d'échange humanitaire** (Humanitarian Exchange Language), est un [système standardisé](https://hxlstandard.org/) permettant de baliser les données à l'aide de hashtags (#). Il est largement utilisé par les organisations pour améliorer le partage d'informations lors de réponses humanitaires et d'autres situations de crise.

L'application de balises HXL à vos questions contribue à rendre vos données plus interopérables entre les systèmes et les organisations. Elle favorise également un traitement et une analyse des données plus efficaces.

Dans KoboToolbox, vous pouvez attribuer une balise HXL par question et inclure des attributs de manière optionnelle. Lorsque vous exportez vos données sous forme de fichier XLS avec les valeurs et en-têtes XML sélectionnés, une ligne supplémentaire contenant les balises HXL apparaîtra directement sous les noms de variables dans votre jeu de données.

L'utilisation de balises HXL est particulièrement utile lorsque vos données seront partagées avec des partenaires ou intégrées dans d'autres systèmes de données humanitaires.

![HXL](images/question_options/hxl.png)