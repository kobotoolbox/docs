# Gestion des données de groupes répétés
<a href="../managing_repeat_groups.html">Read in English</a> | <a href="../es/managing_repeat_groups.html">Leer en español</a> | <a href="../ar/managing_repeat_groups.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/cb137e68b19147fcd0331a6f7919f5563dcebeca/source/managing_repeat_groups.md" class="reference">21 août 2025</a>

KoboToolbox vous permet de collecter des données répétées au sein d'un formulaire, par exemple lors de la réalisation d'une enquête auprès des ménages où les mêmes questions sont posées à tous les membres. Cet article explique comment visualiser, modifier et exporter les données de groupes répétés, et comment lier les données de groupes répétés aux données principales.

<p class="note">
  Pour en savoir plus sur la configuration des groupes répétés dans vos formulaires, consultez <a href="group_repeat.html">Regroupement de questions et groupes répétés</a>.
</p>

## Visualisation et modification des données de groupes répétés
Vous pouvez visualiser les données répétées dans le tableau de données, que vous trouverez dans le mode **Tableau** de l'onglet **DONNÉES** de l'interface du projet KoboToolbox. Les réponses aux questions répétées apparaissent dans une seule colonne par question, avec les réponses séparées par une virgule, comme illustré ci-dessous.

 ![image](/images/managing_repeat_groups/data_table.png) 

Vous pouvez également visualiser les données complètes de toute soumission donnée, y compris chaque répétition des groupes répétés, en cliquant sur le bouton <i class="k-icon-view"></i>**Ouvrir** à gauche de chaque soumission.

Pour modifier les données de groupes répétés, cliquez sur le bouton <i class="k-icon-edit"></i>**Modifier**. Cela ouvrira le formulaire et vous permettra de [modifier les données du formulaire](howto_edit_single_submissions.md) avant de le soumettre à nouveau. La [modification en masse](howto_edit_multiple_submissions.md) des données de groupes répétés n'est actuellement pas prise en charge.

<p class="note">
  <b>Remarque</b> : Les données de groupes répétés ne peuvent pas être affichées dans les modes <b>Rapports</b> ou <b>Carte</b> en raison de la structure des données des groupes répétés.
</p>

## Exportation des données de groupes répétés
Pour exporter les données d'un formulaire avec des groupes répétés, vous devez télécharger vos données au **format XLS**. Chaque groupe répété sera exporté **sous forme de feuille distincte** dans le fichier exporté. Le téléchargement CSV ne fournira que les données des données principales.

![image](/images/managing_repeat_groups/download.png)

<p class="note"> 
    Pour en savoir plus sur l'exportation de vos données, consultez <a href="export_download.html">Exportation et téléchargement de vos données</a>.
</p>

## Liaison des données de groupes répétés
Dans les fichiers XLS exportés, les données de groupes répétés sont stockées **dans une feuille distincte**. La première feuille du fichier XLS contient les données de réponse principales, et les données de chaque groupe répété sont stockées dans leur propre feuille. Les groupes répétés imbriqués sont également stockés dans des feuilles distinctes.

Les données des groupes répétés peuvent être liées aux données principales en utilisant la colonne **_index** de la feuille de données principales et la colonne **_parent_index** de la feuille de données du groupe répété.

Dans l'exemple ci-dessous, la première feuille comprend une colonne **_index**, en vert, qui identifie la première soumission. La deuxième feuille, illustrée dans la deuxième image, contient une colonne **_parent_index**, également surlignée en vert, qui renvoie à la première feuille. Dans cet exemple, les deux lignes des données répétées proviennent de la première soumission de données.

![image](/images/managing_repeat_groups/main_data.png)

![image](/images/managing_repeat_groups/repeat_group_data.png)

<p class="note">
  <b>Remarque</b> : La feuille de données du groupe répété comprend également une <b>colonne _index</b>. Cette colonne est utilisée pour créer un lien vers les <b>groupes répétés imbriqués</b>, suivant la même configuration que celle décrite ci-dessus, avec le groupe répété comme données principales et le groupe répété imbriqué comme données liées.
</p>

Les données de groupes répétés peuvent être fusionnées avec les données principales à l'aide de différents outils d'analyse de données. Par exemple, dans Excel et Power BI, vous pouvez utiliser [Power Query](https://learn.microsoft.com/fr-fr/power-query/power-query-what-is-power-query) ou [RECHERCHEV()](https://support.microsoft.com/fr-fr/office/fonction-recherchev-0bbc8083-26fe-4963-8ab8-93a18ad188a1) pour fusionner les données. Dans SQL, R, SAS et d'autres langages de gestion de bases de données, vous pouvez combiner les ensembles de données à l'aide d'une [jointure gauche](https://learn.microsoft.com/fr-fr/sql/relational-databases/performance/joins?view=sql-server-ver17).

<p class="note">
  Pour en savoir plus sur la fusion des données de groupes répétés à l'aide de Power Query, consultez <a href="https://support.kobotoolbox.org/fr/merging_dataset_excel_power_query.html?highlight=power+query">Fusion de données individuelles avec des données de liste via Power Query dans Excel</a>.<br><br>Pour en savoir plus sur la combinaison d'ensembles de données dans R, consultez <a href="https://dplyr.tidyverse.org/reference/mutate-joins.html">Jointures mutantes</a>.
</p>