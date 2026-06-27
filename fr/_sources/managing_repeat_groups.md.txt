# Gestion des données de groupes répétés
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/c6ce761972d44dffc7387a7fbc1dbeb413e56933/source/managing_repeat_groups.md" class="reference">5 juin 2026</a>


KoboToolbox vous permet de collecter des données répétées dans un formulaire, par exemple lors d'une enquête ménage où tous les membres répondent aux mêmes questions. Cet article explique comment visualiser, modifier et exporter des données de groupes répétés, et comment les relier aux données principales.

<p class="note">
  Pour en savoir plus sur la configuration des groupes répétés dans vos formulaires, consultez les articles <a href="https://support.kobotoolbox.org/fr/group_repeat.html">Groupes et groupes répétés dans l'interface de création de formulaires KoboToolbox (KoboToolbox Formbuilder)</a> et <a href="https://support.kobotoolbox.org/fr/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>

## Visualiser et modifier les données de groupes répétés
Vous pouvez visualiser les données répétées dans le tableau de données, accessible depuis le mode **Tableau** de l'onglet **DONNÉES** dans l'interface du projet KoboToolbox. Les réponses aux questions répétées apparaissent dans une seule colonne par question, les réponses étant séparées par une virgule, comme illustré ci-dessous.

 ![image](/images/managing_repeat_groups/data_table.png) 

Vous pouvez également visualiser l'ensemble des données d'une soumission donnée, y compris chaque répétition des groupes répétés, en cliquant sur le bouton <i class="k-icon-view"></i>**Afficher** à gauche de chaque soumission.

Pour modifier les données d'un groupe répété, cliquez sur le bouton <i class="k-icon-edit"></i>**Modifier**. Le formulaire s'ouvre et vous permet de [modifier les données du formulaire](https://support.kobotoolbox.org/fr/editing_deleting_data.html#editing-submissions-via-web-form) avant de le soumettre à nouveau. La [modification en masse](https://support.kobotoolbox.org/fr/editing_deleting_data.html#editing-multiple-submissions-in-bulk) des données de groupes répétés n'est pas disponible actuellement.

<p class="note">
  <b>Note</b> : Les données de groupes répétés ne peuvent pas être affichées dans les modes <b>Rapports</b> ou <b>Carte</b> en raison de la structure des données des groupes répétés.
</p>

## Exporter les données de groupes répétés
Pour exporter les données d'un formulaire contenant des groupes répétés, vous devez télécharger vos données au **format XLS**. Chaque groupe répété sera exporté **dans un onglet distinct** du fichier exporté. Le téléchargement au format CSV ne fournit que les données du questionnaire principal.

![image](/images/managing_repeat_groups/download.png)

<p class="note">
  Pour en savoir plus sur l'export de vos données, consultez l'article <a href="https://support.kobotoolbox.org/fr/export_download.html">Exporter et télécharger vos données</a>.
</p>

## Relier les données de groupes répétés
Dans les fichiers XLS exportés, les données de groupes répétés sont stockées **dans un onglet distinct**. Le premier onglet du fichier XLS contient les données de réponses principales, et les données de chaque groupe répété sont stockées dans leur propre onglet. Les groupes répétés imbriqués sont également stockés dans des onglets distincts.

Les données des groupes répétés peuvent être reliées aux données principales à l'aide de la colonne `_index` de l'onglet de données principales et de la colonne `_parent_index` de l'onglet de données du groupe répété.

Dans l'exemple ci-dessous, le premier onglet comprend une colonne `_index`, en vert, qui identifie la première soumission. Le deuxième onglet, illustré dans la deuxième image, contient une colonne `_parent_index`, également surlignée en vert, qui renvoie au premier onglet. Dans cet exemple, les deux lignes des données répétées proviennent de la première soumission de données.

![image](/images/managing_repeat_groups/main_data.png)

![image](/images/managing_repeat_groups/repeat_group_data.png)

<p class="note">
  <b>Note</b> : L'onglet de données du groupe répété comprend également une <b>colonne _index</b>. Cette colonne est utilisée pour établir un lien avec les <b>groupes répétés imbriqués</b>, selon le même principe que celui décrit ci-dessus, avec le groupe répété comme données principales et le groupe répété imbriqué comme données liées.
</p>

Les données de groupes répétés peuvent être fusionnées avec les données principales à l'aide de différents outils d'analyse de données. Par exemple, dans Excel et Power BI, vous pouvez utiliser [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) ou [VLOOKUP()](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1) pour fusionner les données. Dans SQL, R, SAS et d'autres langages de gestion de bases de données, vous pouvez combiner les jeux de données à l'aide d'une [jointure gauche](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17) (left join).

<p class="note">
  Pour en savoir plus sur la fusion des données de groupes répétés à l'aide de Power Query, consultez l'article <a href="https://support.kobotoolbox.org/fr/merging_dataset_excel_power_query.html?highlight=power+query">Fusionner des données individuelles avec des données répétées via Power Query dans Excel</a>.<br><br>Pour en savoir plus sur la combinaison de jeux de données dans R, consultez <a href="https://dplyr.tidyverse.org/reference/mutate-joins.html">Mutating joins</a>.
</p>