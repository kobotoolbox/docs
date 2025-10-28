# Types de questions « Sélectionner une réponse » et « Sélectionner plusieurs réponses »
<a href="../select_one_and_select_many.html">Read in English</a> | <a href="../es/select_one_and_select_many.html">Leer en español</a> | <a href="../ar/select_one_and_select_many.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/0d49d3448e1794b63e051d20df2421b33f5274fc/source/select_one_and_select_many.md" class="reference">28 mars 2022</a>

Lorsque vous avez une question catégorielle avec une liste d'options prédéfinies parmi lesquelles les répondantes et répondants peuvent choisir, vous devez choisir soit le type de question « Sélectionner une réponse » soit « Sélectionner plusieurs réponses » dans KoboToolbox. Un type de question « Sélectionner une réponse », également connu sous le nom de question à « réponse unique », signifie qu'une répondante ou un répondant ne peut sélectionner qu'une seule réponse dans une liste d'options. De même, un type de question « Sélectionner plusieurs réponses » est également connu sous le nom de question à « réponses multiples » où une répondante ou un répondant peut sélectionner plusieurs réponses dans une liste d'options.

Les types de questions « Sélectionner une réponse » et « Sélectionner plusieurs réponses » peuvent être de meilleurs choix pour maintenir la qualité des données lorsque la question a une portée étroite et définie. En effet, contrairement à la nature ouverte du type de question « Texte », les deux types de questions de sélection limitent l'utilisatrice ou l'utilisateur aux options listées.

## Quand les utiliser

Utilisez le type de question « Sélectionner une réponse » lorsqu'une question comporte une liste de choix et que la répondante ou le répondant est limité à une seule option de la liste. Les exemples incluent le statut matrimonial, le sexe ou la religion.

Utilisez le type de question « Sélectionner plusieurs réponses » s'il existe une liste de choix et que la répondante ou le répondant peut trouver approprié de sélectionner plus d'un choix. Les exemples incluent les sources de revenus du ménage ou une liste des biens du ménage.

## Configuration de la question et des choix

Suivez les mêmes étapes pour configurer une question « Sélectionner une réponse » ou « Sélectionner plusieurs réponses » :

-   Dans l'interface de création de formulaires, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> pour ajouter une nouvelle question.
-   Saisissez le libellé de la question, par exemple, « Quel est votre statut matrimonial ? ». Ensuite, cliquez sur **+ Ajouter une question** (ou appuyez sur **Entrée**).
-   Choisissez le type de question (« Sélectionner une réponse » ou « Sélectionner plusieurs réponses »)
-   Saisissez les libellés de réponse là où il y a « Option 1 », « Option 2 ». Ajoutez plus de choix si nécessaire.

<p class="note">
  Vous pouvez réorganiser votre liste de choix en cliquant et en faisant glisser chaque élément vers une nouvelle position dans la liste.
</p>

Cliquez sur l'icône de corbeille <i class="k-icon k-icon-trash"></i> à gauche du libellé de l'option pour la supprimer.

## Traduction des libellés de questions et de choix

Pour traduire les questions de type sélection et leurs libellés dans d'autres langues via l'interface utilisateur de KoboToolbox, consultez l'article d'assistance [Ajouter une autre langue dans le tableau de bord du projet](language_dashboard.md), ou [ici](language_xls.md) si vous créez votre formulaire en utilisant XLSForm.

## Valeurs XML

Lors de la configuration des réponses aux questions « Sélectionner une réponse » et « Sélectionner plusieurs réponses », vous avez le choix de spécifier les valeurs XML ou de laisser KoboToolbox les générer automatiquement.

<p class="note">
  Il est fortement recommandé de spécifier les valeurs XML pour <strong>toutes les questions et tous les choix</strong> avant de déployer votre formulaire, <em>en particulier</em> si les libellés sont dans des langues à caractères non latins telles que le chinois, l'arabe ou le népalais.
</p>

Les valeurs XML sont les valeurs qui sont enregistrées dans la soumission lorsqu'une utilisatrice ou un utilisateur choisit la réponse, et non le libellé. Dans l'interface de création de formulaires, saisissez les valeurs là où il est indiqué « AUTOMATIQUE » comme illustré ci-dessous.

![Valeurs XML](/images/select_one_and_select_many/xml_values.png)

Les choix prédéfinis pour les questions « Sélectionner une réponse » et « Sélectionner plusieurs réponses » peuvent parfois être insuffisants lors de la collecte de données. Il est possible d'inclure l'option d'une réponse textuelle dans ce cas, comme décrit dans notre article d'assistance [Réponses « Autre » spécifiées par l'utilisatrice ou l'utilisateur pour les questions à choix multiples](user_specified_other.md).

## Comment elles sont affichées par défaut sur les formulaires web et KoboCollect

![Comparaison de sélectionner une réponse et sélectionner plusieurs réponses sur Enketo et KoboCollect](/images/select_one_and_select_many/select_one_select_many_comparison.png)

Vous pouvez facilement différencier une question « Sélectionner une réponse » d'une question « Sélectionner plusieurs réponses » dans un formulaire de saisie de données. La question « Sélectionner une réponse » a des choix avec un bouton radio (un point plein apparaît après la sélection d'un élément) tandis que la question « Sélectionner plusieurs réponses » a des choix avec une case à cocher carrée (des coches apparaissent après la sélection d'éléments).

## Options d'export

Lors de l'export de questions « Sélectionner plusieurs réponses », vous pouvez choisir entre exporter toutes les réponses sélectionnées dans une seule colonne ou avoir les options dans des colonnes séparées ou les deux. Pour en savoir plus sur l'export et le téléchargement des données, consultez [cet article d'assistance](export_download.md).

## Apparences avancées

Lors de l'ajout de questions « Sélectionner une réponse » et « Sélectionner plusieurs réponses », vous pouvez choisir parmi une large gamme d'apparences. Les apparences modifient la façon dont la question est affichée dans les formulaires web ou KoboCollect.

![Apparences](/images/select_one_and_select_many/appearances.png)

<p class="note">
  L'option « autre » vous fournit un espace où vous pouvez saisir une apparence différente qui n'est pas affichée dans la liste.
</p>

Le tableau suivant montre les différentes apparences disponibles et comment elles sont affichées à la fois dans les formulaires web et KoboCollect.

![Apparences](/images/select_one_and_select_many/select_one_select_many_table.png)

<p class="note">
  Les apparences « quick », « likert » et « quickcompact » ne sont applicables qu'aux questions « Sélectionner une réponse ».
</p>