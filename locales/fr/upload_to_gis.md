# Exporter et importer des données dans un logiciel SIG
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/upload_to_gis.md" class="reference">15 février 2022</a>

**Processus simple étape par étape pour exporter et importer vos données sous forme de fichier shapefile dans un logiciel SIG, tel qu'ArcMap.**

Il existe plusieurs façons d'importer dans un logiciel SIG des données géolocalisées collectées via KoboToolbox. Cet article décrit une procédure recommandée pour télécharger des données depuis KoboToolbox sous forme de fichier CSV et les importer dans ArcMap sous forme de fichier shapefile. Bien que cet exemple utilise ArcMap, le processus est similaire dans d'autres logiciels géospatiaux, notamment QGIS (gratuit).

1. Dans l'onglet **Téléchargements** de la page de votre projet dans KoboToolbox, exportez et téléchargez vos données sous forme de fichier CSV.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    _Remarque : Vous pouvez modifier l'ensemble de données une fois qu'il est dans le logiciel SIG, mais il peut être plus facile de le modifier d'abord dans Excel ou un programme similaire. Dans Excel, utilisez la fonction [Convertir](https://support.office.com/fr-fr/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23) pour diviser vos données CSV en cellules individuelles._

2. Ouvrez un nouveau projet ou un projet existant dans ArcMap, allez dans **Add Data**, puis liez le dossier où votre fichier CSV est enregistré sur votre ordinateur.

    ![image](/images/upload_to_gis/find_file.jpg)

3. Ouvrez la fenêtre **Catalog** et cliquez sur **Folder Connections**. Trouvez votre fichier CSV, faites un clic droit dessus, puis sélectionnez **Create Feature Class** > **From XY Table**.

4. Dans la fenêtre modale, cliquez sur le menu déroulant **X Field** et choisissez votre option question_Longitude GPS. Assurez-vous également de choisir votre **Coordinate System of Input Coordinates**... (WGS 1984 est un bon choix, si vous n'en utilisez pas déjà un) et vérifiez que votre **Output** est défini sur le dossier approprié, puis cliquez sur **OK**.

    ![image](/images/upload_to_gis/create_feature.jpg)

5. De retour dans la fenêtre **Catalog**, cliquez et faites glisser votre nouveau fichier shapefile dans la fenêtre **Data View** ou **Table of Contents**.

6. Vous devriez maintenant voir vos points à l'écran et si vous ouvrez la **Attributes Table**, vous verrez toutes les données associées à chaque point. À partir de là, vous pouvez maintenant visualiser et effectuer diverses analyses spatiales avec vos données.

    ![image](/images/upload_to_gis/dataview_table.jpg)