# Exporter et télécharger des données vers un logiciel SIG
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/upload_to_gis.md" class="reference">15 fév. 2022</a>


**Procédure simple, étape par étape, pour exporter et importer vos données sous forme de shapefile dans un logiciel SIG, tel qu'ArcMap.**

Il existe plusieurs façons d'importer des données de localisation collectées via KoboToolbox dans un logiciel SIG. Cet article décrit une procédure recommandée pour télécharger vos données depuis KoboToolbox sous forme de fichier CSV et les importer dans ArcMap en tant que shapefile. Bien que cet exemple utilise ArcMap, la procédure est similaire dans d'autres logiciels géospatiaux, notamment QGIS (gratuit).

1. Dans l'onglet **Téléchargements** de la page de votre projet dans KoboToolbox, exportez et téléchargez vos données sous forme de fichier CSV.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    _Remarque : vous pouvez modifier le jeu de données une fois qu'il se trouve dans le logiciel SIG. Cependant, il peut être plus simple de l'éditer d'abord dans Excel ou un programme similaire. Dans Excel, utilisez la fonction [Convertir.](https://support.office.com/en-us/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23) pour répartir vos données CSV en cellules individuelles._

2. Ouvrez un projet nouveau ou existant dans ArcMap, accédez à **Add Data**, puis accédez au dossier où votre fichier CSV est enregistré sur votre ordinateur.

    ![image](/images/upload_to_gis/find_file.jpg)

3. Ouvrez la fenêtre **Catalog** et cliquez sur **Folder Connections**. Trouvez votre fichier CSV, faites un clic droit dessus, puis sélectionnez **Create Feature Class** > **From XY Table**.

4. Dans la boîte de dialogue, cliquez sur le menu déroulant **X Field** et choisissez l'option GPS question_Longitude. Veillez également à sélectionner votre **Coordinate System of Input Coordinates**... (WGS 1984 est un bon choix si vous n'en utilisez pas déjà un) et assurez-vous que votre **Output** est défini sur le dossier approprié, puis cliquez sur **OK**.

    ![image](/images/upload_to_gis/create_feature.jpg)

5. De retour dans la fenêtre **Catalog**, cliquez et faites glisser votre nouveau shapefile vers la fenêtre **Data View** ou vers la **Table of Contents**.

6. Vos points devraient maintenant apparaître à l'écran. Si vous ouvrez la **Table des attributs** (**Attributes Table**), vous verrez toutes les données associées à chaque point. À partir de là, vous pouvez visualiser vos données et effectuer diverses analyses spatiales.

    ![image](/images/upload_to_gis/dataview_table.jpg)