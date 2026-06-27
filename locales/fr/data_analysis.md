# Analyse de données avec KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/977b859244796b0c30002db811ee84f02bf98dee/source/data_analysis.md" class="reference">15 Jun 2026</a>

KoboToolbox propose des **outils intégrés** pour vous aider à consulter, visualiser et analyser vos données collectées. Ces outils peuvent être utilisés pour des statistiques descriptives, la cartographie et l'analyse qualitative.

Au-delà des outils intégrés, vous pouvez également **exporter vos données** ou **les connecter à des plateformes externes** pour un nettoyage, un traitement, une analyse et une visualisation plus avancés.

Cet article présente les options d'analyse de données de KoboToolbox, des rapports intégrés, des cartes et des outils d'analyse qualitative aux exports de données, aux exports synchronisés et aux pratiques de conception de formulaires qui facilitent une analyse plus propre.

## Analyser et visualiser des données dans KoboToolbox

KoboToolbox comprend plusieurs outils qui vous permettent de comprendre vos données directement dans la plateforme.

### Rapports de données

KoboToolbox inclut un outil de rapport et de visualisation que vous pouvez utiliser pour **surveiller les données entrantes** et consulter des **statistiques descriptives simples.**

Vous pouvez utiliser les rapports pour afficher des graphiques, consulter le nombre de réponses, comparer les réponses par sous-groupe, et partager ou imprimer un résumé des questions sélectionnées dans votre formulaire.

![Rapport de données](images/data_analysis/report.png)

Les rapports sont utiles pour consulter rapidement vos données, mais ils ne remplacent pas un nettoyage, un traitement, une analyse ou une visualisation approfondis dans des outils externes.

<p class="note">
  Pour en savoir plus sur les rapports de données, consultez l'article <a href="https://support.kobotoolbox.org/fr/creating_custom_reports.html">Visualiser vos données à l'aide de rapports personnalisés</a>.
</p>

### Mode Carte

KoboToolbox propose également un **mode Carte** intégré pour les soumissions qui incluent des données GPS. Le mode Carte vous permet de visualiser des points GPS individuels, d'explorer des tendances géographiques et de mieux comprendre où les soumissions ont été collectées.

![Cartographie des données GPS](images/data_analysis/map.png)

<p class="note">
  Pour en savoir plus sur la cartographie des données GPS avec KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/mapping_gps.html#">Cartographier vos données GPS</a>.
</p>

### Transcription audio, traduction et analyse qualitative

Les outils de traitement du langage naturel de KoboToolbox vous permettent de **transcrire, traduire et analyser des données qualitatives.** Cela peut vous aider à transformer des réponses audio ouvertes en résultats plus clairs et exploitables.

Vous pouvez traiter et analyser les réponses audio directement dans l'interface utilisateur, puis enregistrer les transcriptions, traductions, résumés, catégories et autres résultats d'analyse sous forme de nouvelles colonnes dans votre base de données.

![Analyse de données qualitatives](images/data_analysis/qual.png)

<p class="note">
  Pour en savoir plus sur l'analyse des données qualitatives dans KoboToolbox, consultez les articles <a href="https://support.kobotoolbox.org/fr/transcription-translation.html">Transcription et traduction de réponses audio</a> et <a href="https://support.kobotoolbox.org/fr/qualitative_analysis.html">Analyse qualitative des réponses audio</a>.
</p>

## Exporter et connecter des données pour une analyse externe

Les outils intégrés de KoboToolbox peuvent assurer une analyse descriptive simple, la cartographie et l'analyse qualitative. Cependant, de nombreux projets nécessitent des outils externes pour un nettoyage, un traitement, une analyse et une visualisation des données plus avancés. Pour ce faire, vous pouvez utiliser des **exports de données classiques** ou des **exports synchronisés** pour travailler avec vos données KoboToolbox en dehors de la plateforme.

### Exports de données

Vous pouvez exporter vos données depuis KoboToolbox dans plusieurs formats, selon la façon dont vous prévoyez de les utiliser.

- Pour une analyse générale, vous pouvez **exporter vos données au format Excel ou CSV.** Ces formats peuvent être utilisés pour nettoyer et traiter des données, ou pour importer des données dans des logiciels d'analyse tels que R, Stata, SPSS ou Python.
- Pour la cartographie et l'analyse géospatiale, vous pouvez **exporter des données GPS dans des formats tels que CSV, XLS, GeoJSON ou KML.** Ces formats peuvent être utilisés dans des outils de cartographie et des logiciels SIG.

<p class="note">
  Pour en savoir plus sur l'export des données KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/export_download.html">Exporter et télécharger vos données.</a>
</p>

Lors de l'export de données pour une analyse dans des logiciels externes, il est recommandé d'exporter vos données en **valeurs XML et en-tête XML**, et de **séparer les réponses à choix multiple** en colonnes distinctes. Ces paramètres facilitent le traitement et l'analyse des données exportées.

Si vous partagez des données brutes avec des publics non techniques, **exporter les libellés** plutôt que les **valeurs XML et en-tête XML** peut être plus accessible. Les libellés peuvent également être exportés dans plusieurs langues.

D'autres paramètres d'export, tels que l'enregistrement des réponses de type date et nombre sous forme de texte ou l'inclusion des données de toutes les versions du formulaire, dépendent de vos besoins et préférences en matière d'analyse.

<p class="note">
  Pour en savoir plus sur les paramètres avancés d'export des données, consultez l'article <a href="https://support.kobotoolbox.org/fr/advanced_export.html#">Options avancées pour l'export des données</a>.
</p>

### Exports synchronisés

Pour les projets en cours, vous souhaiterez peut-être **connecter vos données KoboToolbox à des outils externes** plutôt que de télécharger un nouvel export à chaque modification de vos données.

Les **exports synchronisés** vous permettent de connecter automatiquement les données KoboToolbox à des applications externes telles que Microsoft Power BI, Excel ou Google Sheets. Cela peut être utile pour les tableaux de bord, le suivi de projet, le traitement avancé ou les flux de travail de reporting partagés.

Avec les exports synchronisés, vos données connectées se mettent à jour à mesure que de nouvelles soumissions sont reçues, ce qui réduit le besoin de téléchargements et d'actualisations manuels.

<p class="note">
  Pour en savoir plus sur la connexion de vos données à des outils externes, consultez l'article <a href="https://support.kobotoolbox.org/fr/synchronous_exports.html">Utiliser l'API pour les exports synchronisées</a>.
</p>

## Préparer l'analyse de données avec KoboToolbox

De nombreux problèmes de qualité des données ne commencent pas lors de l'analyse, mais lors de la collecte de données. Les décisions prises lors de la création d'un formulaire — comme la façon dont les questions sont structurées, la façon dont les choix de réponse sont nommés et la façon dont les données manquantes sont gérées — peuvent influer sur la quantité de nettoyage et de préparation requise par la suite.

KoboToolbox inclut plusieurs outils qui **favorisent une collecte de données de haute qualité** et contribuent à préparer vos données pour l'analyse à long terme.

<p class="note">
  Pour en savoir plus sur les bonnes pratiques de conception de formulaires, consultez l'article <a href="https://support.kobotoolbox.org/fr/preparing_for_analysis.html">Préparer votre formulaire pour l'analyse de données</a>.
</p>