# Cartographie, partage et exportation de données GPS
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/export_gps.md" class="reference">15 fév. 2022</a>

Votre projet peut inclure une ou plusieurs questions GPS dans son formulaire. KoboToolbox
inclura les données GPS (latitude, longitude, altitude, précision) dans l'ensemble de données
qui peut être téléchargé au format XLS ou CSV. Il est également possible de visualiser les
coordonnées GPS sur une carte en ligne et de télécharger les points sous forme de fichier KML pour
les utiliser dans d'autres applications.

## Visualiser vos points GPS

![image](/images/export_gps/view_gps.jpg)

Les deux options suivantes n'apparaissent que si votre formulaire contient des questions GPS et
possède des soumissions avec des coordonnées GPS.

**Option 1 - Visualiser les points GPS en ligne.**

Cliquez sur le bouton **View on Map**, qui mène à la vue cartographique en ligne. Cette
visualisation permet également de voir les soumissions en fonction de certaines réponses aux questions.
Lorsque vous visualisez vos données sur une carte, vous pouvez également désagréger par
réponses aux questions, comme afficher les répondants masculins et féminins, ou d'autres
types de réponses où une simple distribution géographique pourrait être intéressante.
Une liste complète des fonctionnalités cartographiques actuelles est présentée ci-dessous :

1. Settings : Importez des superpositions de données et choisissez des schémas de couleurs pour les marqueurs.
2. Toggle layers : Basculez entre plusieurs options d'arrière-plan de carte.
3. Toggle fullscreen
4. Show data as points (par défaut)
5. Show data as heat map

**Option 2 - Télécharger les points GPS au format KML.**

Cliquez sur le bouton **Download GPS Points**. Cela lancera un nouveau processus d'exportation
avec les dernières données. Les exportations précédentes seront listées par leur date de création,
vous permettant de voir des instantanés de coordonnées GPS à différents moments dans le
temps. Les fichiers KML peuvent être importés dans une variété de logiciels, notamment Google
Earth, Google Maps ou des logiciels SIG professionnels, tels qu'ArcMap.

![image](/images/export_gps/kml_exports.jpg)

Remarque : Si votre formulaire utilise plus d'une question GPS, seule la première sera
utilisée sur la carte.

**Option 3 - Exporter les données au format CSV et les importer dans un logiciel SIG.**

Comme alternative à l'exportation de vos données GPS sous forme de fichier KML, il est possible et
facile d'exporter et d'importer vos données sous forme de fichier CSV (qui inclura tous les
attributs) directement dans un logiciel SIG sous forme de shapefile. Pour un guide étape par étape,
consultez cet [article d'aide](upload_to_gis.md).

## Comment partager des données cartographiques

Vous pouvez partager une carte avec d'autres personnes en accédant aux paramètres de votre projet et en activant
Share Data. Cela signifie que n'importe qui peut visualiser vos données - c'est-à-dire sous forme de carte, de tableau ou
de téléchargement de fichier. Les utilisatrices et utilisateurs ne pourront rien modifier, ce qui nécessiterait
d'accorder des autorisations Can Edit à une utilisatrice ou un utilisateur en particulier. Après cela, vous pouvez envoyer l'URL de la carte (voir ci-dessus).