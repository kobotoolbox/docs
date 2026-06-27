# Collecter des données dans plusieurs langues
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/collecting_data_multiple_languages.md" class="reference">23 Apr 2026</a>

KoboToolbox permet de collecter des données dans **autant de langues que nécessaire** au sein d'un même formulaire, y compris les langues utilisant des alphabets non latins. Vous pouvez concevoir votre formulaire avec plusieurs traductions, permettre aux répondants de choisir leur langue préférée pendant la collecte de données, puis afficher ou exporter les données dans n'importe quelle langue du formulaire.

L'ajout de traductions dans un seul formulaire évite de devoir créer des formulaires distincts pour chaque langue, ce qui facilite la gestion des projets multilingues et **garantit la cohérence de vos données entre les langues.** [KoboCollect](../fr/data_collection_kobocollect.html) et les [formulaires web](../fr/data_through_webforms.html) sont tous deux compatibles avec les traductions de formulaires.

Cet article présente les différentes options pour préparer des formulaires avec des traductions, comment collecter des données dans plusieurs langues (y compris la configuration de liens spécifiques à une langue pour les formulaires web), et comment gérer et exporter des données multilingues dans KoboToolbox.

## Configurer vos formulaires avec des traductions

Vous pouvez ajouter des traductions à votre formulaire **directement dans l'interface KoboToolbox** ou en utilisant **XLSForm.** KoboToolbox propose une interface intuitive qui ne nécessite aucune expertise technique et vous permet d'ajouter facilement plusieurs traductions à vos formulaires. Cette approche est utile lorsque vous travaillez avec un petit nombre de questions ou lorsque vous souhaitez effectuer des ajustements rapides.

<p class="note">
  Pour en savoir plus sur la configuration des traductions depuis l'interface KoboToolbox, consultez l'article <a href="../fr/language_dashboard.html">Ajouter des traductions dans KoboToolbox</a>.
</p>

Pour les formulaires multilingues plus volumineux ou plus complexes, XLSForm est souvent l'option la plus efficace. Il vous permet de gérer les traductions en masse, ce qui peut faire gagner du temps lorsque vous travaillez avec de nombreuses questions ou plusieurs langues.

<p class="note">
  Pour en savoir plus sur la configuration des traductions dans XLSForm, consultez l'article <a href="../fr/language_xls.html">Ajouter des traductions dans XLSForm</a>.
</p>

La plupart des éléments affichés aux répondants peuvent être traduits. Il s'agit notamment des **libellés de questions, des indices, des libellés de choix, des messages de contrainte** et des **messages d'obligation.** Les éléments qui définissent la structure du formulaire, tels que les [noms de champs](../fr/glossary.html#data-column-name) et les [valeurs XML](../fr/glossary.html#xml-value), ne peuvent pas être traduits et doivent rester dans la langue utilisée pour le développement du formulaire et l'analyse des données.

<p class="note">
  <strong>Note :</strong> XLSForm facilite l'ajout de traductions en masse à l'aide d'outils de traduction automatique ou en ligne. Les traductions automatiques doivent toujours être vérifiées par un locuteur courant pour garantir leur exactitude, leur adéquation culturelle et leur contexte approprié. Cela contribue à maintenir la qualité et la fiabilité de votre contenu traduit.
</p>

## Collecter des données dans plusieurs langues

<iframe src="https://www.youtube.com/embed/MWLlWtXYHig?si=nGuOVpt0tVR_ip7l&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Lorsque votre formulaire contient des traductions, les répondants peuvent choisir leur langue préférée pendant la collecte de données et changer de langue à tout moment avant de soumettre leurs réponses.

Pour changer la langue du formulaire dans les formulaires web :

1. Ouvrez le formulaire dans votre navigateur.
2. En haut à droite du formulaire, un menu déroulant **Choose Language** s'affiche (uniquement dans les formulaires comportant plusieurs langues).
3. Ouvrez le menu déroulant et choisissez parmi la liste des traductions disponibles.

Pour changer la langue du formulaire dans KoboCollect :

1. Ouvrez le formulaire sur votre appareil.
2. Appuyez sur le bouton <i class="k-icon-more-vertical"></i> **More options** en haut à droite de l'écran.
3. Sélectionnez <i class="k-icon-language"></i> **Change Language.**
4. Choisissez parmi la liste des traductions disponibles.

### URL du formulaire spécifique à une langue

Par défaut, les liens de formulaires copiés depuis KoboToolbox s'ouvrent dans la langue par défaut du formulaire. Pour partager un lien qui s'ouvre dans une autre langue du formulaire, ajoutez le paramètre `lang` à la fin de l'URL du formulaire :

1. Copiez le lien de votre formulaire dans **FORMULAIRE > Collect data.**
2. Ajoutez `?lang=[code_langue]` à la fin de l'URL.
    - Par exemple : `https://ee.kobotoolbox.org/x/[form_id]?lang=fr`.
3. Partagez l'URL spécifique à la langue avec les répondants.

<p class="note">
  <strong>Note :</strong> Cela remplace à la fois le paramètre de langue du navigateur et la langue par défaut du formulaire. Cette fonctionnalité s'applique uniquement aux formulaires web, et non à KoboCollect.
</p>

## Gérer les données dans plusieurs langues

Après avoir collecté des données dans plusieurs langues, KoboToolbox vous permet d'afficher et d'exporter vos données dans n'importe quelle langue incluse dans votre formulaire.

<p class="note">
<p>
  <strong>Note :</strong> Si vous collectez des réponses audio dans plusieurs langues, vous pouvez transcrire et traduire ces réponses à l'aide des fonctionnalités de transcription et de traduction automatiques de KoboToolbox. Pour en savoir plus, consultez l'article <a href="../fr/transcription-translation.html">Transcription et traduction de réponses audio</a>.
</p>

### Afficher les données dans différentes langues en mode Tableau

Dans la vue **DONNÉES > Tableau**, vous pouvez changer la langue utilisée pour les libellés des questions et des choix.

Pour afficher votre tableau de données dans une autre langue :

1. Dans votre projet, accédez à **DONNÉES > Tableau.**
2. Dans le coin supérieur droit, cliquez sur <i class="k-icon-settings"></i> **Options d'affichage.**
3. Sous **Afficher les libellés ou des valeurs XML ?**, sélectionnez la langue que vous souhaitez utiliser.

![Options d'affichage en mode Tableau](images/collecting_data_multiple_languages/table_view.png)

<p class="note">
<strong>Note :</strong> Toutes les données du formulaire sont affichées dans la langue sélectionnée, quelle que soit la langue utilisée lors de la collecte de données, à l'exception des réponses en texte libre.
</p>

### Afficher les données dans différentes langues en mode Rapports

Dans la vue **DONNÉES > Rapports**, vous pouvez également changer la langue du rapport.

Pour afficher votre rapport de données dans une autre langue :

1. Dans votre projet, accédez à **DONNÉES > Rapports.**
2. Cliquez sur <i class="k-icon-settings"></i> **Modifier le style du rapport.**
3. Accédez à l'onglet **TRANSLATION.**
4. Sélectionnez la langue que vous souhaitez afficher dans le rapport.

![Modifier le style du rapport](images/collecting_data_multiple_languages/reports.png)

<p class="note">
<strong>Note :</strong> Toutes les données du formulaire sont affichées dans la langue sélectionnée, quelle que soit la langue utilisée lors de la collecte de données, à l'exception des réponses en texte libre.
</p>

### Sélectionner une langue lors de l'export des données

Dans la section **DONNÉES > Téléchargements**, vous pouvez choisir la langue utilisée dans votre jeu de données exporté.

Pour exporter votre rapport de données dans une autre langue :

1. Dans votre projet, accédez à **DONNÉES > Téléchargements.**
2. Cliquez sur le menu déroulant sous **Format pour les valeurs et l'en-tête.**
3. Sélectionnez la langue dans laquelle vous souhaitez exporter vos données.
4. Cliquez sur **Exporter**, puis téléchargez le fichier exporté.

![Sélectionner la langue d'export](images/collecting_data_multiple_languages/exports.png)

<p class="note">
  <strong>Note :</strong> Toutes les données du formulaire sont exportées dans la langue sélectionnée, quelle que soit la langue utilisée lors de la collecte de données, à l'exception des réponses en texte libre.
</p>

Vous pouvez également afficher ou exporter vos données en utilisant les [valeurs XML](../fr/glossary.html#xml-value). **Les valeurs XML ne sont pas traduites** et sont généralement générées dans la langue utilisée lors du développement du formulaire.

L'utilisation des valeurs XML est recommandée pour l'analyse, car elles fournissent des noms de variables courts et cohérents ainsi que des valeurs codées qui **restent identiques quelle que soit la traduction**, indépendamment de la langue utilisée par les répondants.