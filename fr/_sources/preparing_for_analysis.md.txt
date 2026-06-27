# Préparer votre formulaire pour l'analyse des données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6e9f496956ced232adb4985272fbee0a6465318d/source/preparing_for_analysis.md" class="reference">15 Jun 2026</a>

De nombreux problèmes de qualité des données ne surviennent pas lors de l'analyse, mais pendant la collecte de données. Les décisions prises lors de la création d'un formulaire — telles que la structure des questions, la dénomination des choix de réponse et la gestion des données manquantes — peuvent influer sur la quantité de nettoyage et de préparation nécessaires par la suite.

KoboToolbox propose plusieurs outils qui **favorisent une collecte de données de qualité** et vous aident à préparer vos données pour l'analyse sur le long terme.

Cet article présente des recommandations pour **concevoir des formulaires produisant des données plus propres et plus cohérentes**, depuis l'utilisation de la logique de formulaire et des calculs jusqu'à la planification des noms de questions et de choix, en passant par le téléchargement de votre XLSForm en tant que dictionnaire de données.

## Collecter des données cohérentes et homogènes

L'un des moyens les plus efficaces d'améliorer votre analyse est de prévenir les erreurs lors de la collecte de données. KoboToolbox propose des fonctionnalités de logique de formulaire qui peuvent vous aider à collecter des réponses plus précises et plus cohérentes.

### Critères de validation

Les [critères de validation](https://support.kobotoolbox.org/fr/glossary.html#validation-criteria) permettent de s'assurer que les répondants fournissent des réponses valides. Par exemple, vous pouvez utiliser des critères de validation pour :

- Limiter l'âge à des valeurs réalistes
- Empêcher la saisie de dates de naissance dans le futur
- Exiger que les numéros de téléphone respectent un format spécifique

Les critères de validation sont particulièrement utiles pour les questions dont les réponses doivent se situer dans une plage spécifique ou suivre un format prévisible.

### Logique de saut

La [logique de saut](https://support.kobotoolbox.org/fr/glossary.html#skip-logic) permet de s'assurer que les répondants ne voient que les questions qui les concernent. Par exemple, un répondant qui déclare n'avoir jamais été enceinte ne devrait pas se voir poser de questions sur des grossesses antérieures.

Poser les bonnes questions aux bonnes personnes améliore la qualité des données et réduit la charge pesant sur les répondants. Cela réduit également la quantité de nettoyage ou de suppression de données nécessaires par la suite.

<p class="note">
  Pour en savoir plus sur la logique de formulaire, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic.html">Introduction à la logique de formulaire dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)</a>.
</p>

## Anticiper le format de vos exports de données

La façon dont vous définissez les [noms de questions](https://support.kobotoolbox.org/fr/glossary.html#data-column-name) et les [noms de choix](https://support.kobotoolbox.org/fr/glossary.html#xml-value) influe sur la facilité avec laquelle vous pourrez travailler avec vos données après l'export. Les **noms de questions** deviennent des noms de colonnes dans votre base de données exportée, tandis que les **noms de choix** représentent les valeurs de réponse pour les questions à choix multiple.

Pour de meilleurs résultats, suivez les recommandations ci-dessous.

### Utiliser un formatage clair

Utilisez des noms de questions et de choix courts, informatifs, uniques et sans espaces ni caractères spéciaux (par exemple, `age`, `sex` ou `district`).

Des noms clairs rendent vos données exportées plus faciles à lire, à traiter et à analyser dans des outils externes.

### Maintenir la cohérence des noms

Maintenez la cohérence des noms de questions et de choix d'un formulaire à l'autre dans la mesure du possible. Si plusieurs enquêtes collectent les mêmes informations, **l'utilisation des mêmes noms de variables** facilite la combinaison et la comparaison des bases de données.

- Par exemple, si un formulaire utilise `district` et qu'un autre utilise `location_district` pour le même type d'information, vous devrez peut-être renommer les variables avant de combiner les bases de données.

De même, l'utilisation de **noms de choix** standardisés facilite l'analyse et réduit la nécessité de recoder les données par la suite.

- Par exemple, vous pouvez utiliser `0` pour « Non » et `1` pour « Oui » pour toutes les questions pertinentes de votre formulaire.

### Éviter de modifier les noms après le début de la collecte de données

Une fois la collecte de données commencée, **évitez de modifier les noms de questions ou de choix.** Les modifier peut créer des incohérences entre les soumissions existantes et les nouvelles soumissions.

Si vous devez mettre à jour les libellés affichés aux répondants, modifiez le libellé de la question tout en conservant le même nom de question dans la mesure du possible.

<p class="note">
  Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/deploy_form_new_project.html#best-practices-for-deploying-and-redeploying-forms">Déployer vos formulaires pour la collecte de données</a>.
</p>

### Utiliser des préfixes et des suffixes

Lorsque les formulaires contiennent des variables liées entre elles, des conventions de nommage cohérentes peuvent contribuer à organiser vos données. Envisagez **d'utiliser un préfixe ou un suffixe** pour les questions ou les choix liés au même sujet ou au même format.

Par exemple :

- Utilisez `household_` pour les questions relatives au ménage, telles que `household_size` ou `household_income`
- Utilisez `_other` pour les questions « Autre, précisez », telles que `income_source_other`

<p class="note">
<strong>Note :</strong>
  Les noms de questions et de choix restent identiques quelle que soit la langue du formulaire. Cela facilite l'analyse des données multilingues après l'export.
</p>

## Anticiper les besoins en matière d'analyse

Lors de la conception d'un formulaire, réfléchissez aux analyses que vous pourriez souhaiter effectuer par la suite. Planifier à l'avance peut réduire la quantité de traitement nécessaire après l'export.

### Utiliser des calculs pour les variables d'analyse

Les [calculs](https://support.kobotoolbox.org/fr/glossary.html#calculation) permettent de créer des variables qui nécessiteraient autrement un traitement supplémentaire après l'export. Par exemple, vous pouvez utiliser des calculs pour créer :

- L'âge du répondant à partir de sa date de naissance
- Les totaux de la taille du ménage
- L'indice de masse corporelle (IMC)
- Des scores ou des indicateurs basés sur plusieurs réponses

Créer ces variables lors de la collecte de données peut faire gagner du temps et améliorer la cohérence des analyses.

<p class="note">
  Pour en savoir plus sur l'ajout de calculs, consultez l'article <a href="https://support.kobotoolbox.org/fr/calculate_questions.html">Ajouter des calculs avec le Formbuilder</a>.
</p>

### Planifier la gestion des données manquantes

Lors de l'analyse des données, il est important de savoir **pourquoi des informations sont manquantes.** Une réponse peut être absente parce que la question a été ignorée, que l'information était indisponible, non mémorisée, non applicable ou délibérément non communiquée.

Une bonne pratique courante consiste à [rendre les questions obligatoires](https://support.kobotoolbox.org/fr/question_options.html#mandatory-response) tout en proposant des options de réponse explicites, telles que :

- Préfère ne pas répondre
- Ne sait pas
- Ne se souvient pas
- Sans objet

Cela contribue à réduire les données manquantes inexpliquées et facilite l'interprétation des résultats lors de l'analyse.

### Limiter les réponses en texte libre

Les **réponses en texte libre** sont souvent difficiles à analyser. Dans la mesure du possible, utilisez plutôt des types de questions structurées :

- Utilisez des [questions à choix multiple](https://support.kobotoolbox.org/fr/select_one_and_select_many.html) lorsque les réponses peuvent être standardisées en options prédéfinies.
- Utilisez des [questions de type date](https://support.kobotoolbox.org/fr/date_time.html) pour collecter des dates du calendrier.
- Utilisez des [questions GPS](https://support.kobotoolbox.org/fr/gps_questions.html) ou des [questions à sélection en cascade](https://support.kobotoolbox.org/fr/cascading_select.html) pour collecter des informations de localisation.

Réservez les questions de type texte aux informations qui ne peuvent raisonnablement pas être standardisées.

## Utiliser votre XLSForm comme dictionnaire de données

Le [XLSForm](https://support.kobotoolbox.org/fr/edit_forms_excel.html) qui sous-tend votre formulaire KoboToolbox peut servir de dictionnaire de données. Il documente la structure de votre formulaire, les noms de questions, les noms de choix, les libellés, les traductions, les types de questions et la logique de formulaire.

Pour télécharger le XLSForm de votre formulaire :

1. Ouvrez votre projet.
2. Accédez à **FORMULAIRE.**
3. Cliquez sur <i class="k-icon-more"></i> **Plus d'actions.**
4. Cliquez sur <i class="k-icon-file-xls"></i> **Télécharger XLS.**

Chaque ligne de l'**onglet survey** représente une question de votre formulaire, et chaque colonne fournit des informations sur cette question, telles que le nom de la question, le libellé, le type, les traductions et la logique de formulaire associée. Pour les questions à choix multiple, les [choix de réponse](https://support.kobotoolbox.org/fr/option_choices_xls.html) sont répertoriés dans l'**onglet choices**.

Conserver votre XLSForm avec votre base de données exportée peut faciliter l'interprétation des variables, la compréhension des valeurs de réponse et la documentation de votre processus d'analyse.

<p class="note">
  Pour en savoir plus sur XLSForm, consultez les articles <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">Créer un XLSForm</a> et <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>.
</p>