# Fusionner des données individuelles avec des données de liste via Power Query dans Excel
<a href="../merging_dataset_excel_power_query.html">Read in English</a> | <a href="../es/merging_dataset_excel_power_query.html">Leer en español</a> | <a href="../ar/merging_dataset_excel_power_query.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/73dbdbb56448bbfbdb62af8017b71582965291d2/source/merging_dataset_excel_power_query.md" class="reference">6 avr. 2022</a>

Comme illustré dans l'article d'aide,
[Regrouper des questions et groupes répétés](group_repeat.md), vous pouvez utiliser
des groupes répétés pour répondre à certaines exigences d'enquête. Vous pourriez également avoir besoin
d'analyser les données des groupes répétés qui ont été collectées. Lorsque vous
[téléchargez les données depuis le serveur (au format XLS)](export_download.md), vous
devriez voir les données dans la structure suivante :

![Dataset Sheets](/images/merging_dataset_excel_power_query/dataset_sheets.png)

La première feuille avec le nom de feuille **Repeat Group (Merge)** visible dans l'image
ci-dessus contient les _données individuelles_ de l'enquête tandis que la deuxième feuille avec
le nom de feuille **CR** contient les _données de liste_.

<p class="note">
  Pour les jeux de données téléchargés, vous devriez avoir une feuille de plus que le nombre de
  <em>groupes répétés</em>. Par exemple, si vous aviez un
  <em>groupe répété</em> inclus dans le formulaire d'enquête, vous devriez avoir deux feuilles
  dans votre jeu de données.
</p>

Cet article d'aide illustrera également la différence entre les _données
individuelles_ et les _données de liste_. Il montrera ensuite les étapes pour les fusionner en
un seul jeu de données via **Power Query** dans **Excel**.

La fusion des _données individuelles_ et des _données de liste_ via le système n'est actuellement pas
disponible mais elle est possible via **Power Query** dans **Excel**. Excel a été
choisi plutôt que d'autres logiciels car c'est un tableur largement utilisé et disponible
sur presque tous les PC. Il est également relativement facile à utiliser.

## Différences entre données individuelles et données de liste :

Les _données individuelles_ sont des informations qui sont généralement capturées une seule fois dans un
entretien. Les _données de liste_, en revanche, sont capturées plus d'une fois _(par exemple,
les détails de tous les membres de la famille vivant dans un ménage)_ auprès du même
individu dans un entretien. Le nombre de cas dans les _données individuelles_ peut être égal
aux _données de liste_ mais ne peut jamais les dépasser, tandis que le nombre de cas dans les _données
de liste_ dépasse généralement les _données individuelles_ mais peut parfois être égal (mais
jamais inférieur).

Un formulaire d'enquête rempli, comme montré ci-dessous, devrait illustrer en image les
différences entre les _données individuelles_ et les _données de liste_. _Veuillez noter que toutes les données
utilisées dans cet article d'aide sont hypothétiques_.

![Form](/images/merging_dataset_excel_power_query/form.png)

<p class="note">
  Toute donnée collectée en dehors du groupe répété est une
  <em>donnée individuelle</em> et toute donnée collectée à l'intérieur d'un groupe répété
  est une <em>donnée de liste</em>.
</p>

Les données téléchargées au format XLS devraient également montrer la différence entre
les _données individuelles_ et les _données de liste_.

Chaque enregistrement _(comme montré dans l'image ci-dessous)_, sous `Name of the household head`,
`Sex of the household head`, `Total family members in the household`, et
`Total school going children (aged 6-16 years) in the household` de la première
feuille **Repeat Group (Merge)** est une _donnée individuelle_.

![Individual Data](/images/merging_dataset_excel_power_query/individual_data.png)

Cet exemple de jeu de données a un total de 7 entretiens comme _données individuelles_.

De même, chaque enregistrement _(comme montré dans l'image ci-dessous)_, sous `Name of child`,
`Age of child`, et `Sex of child` de la deuxième feuille, **CR**, est une _donnée
de liste_.

![Roster Data](/images/merging_dataset_excel_power_query/roster_data.png)

Donc, cet exemple de jeu de données a un total de 12 enregistrements comme _données de liste_.

<p class="note">
  <strong>Remarque :</strong> Lors du téléchargement d'un jeu de données depuis le serveur, vous devriez
  également pouvoir voir d'autres variables (variables de métadonnées) si elles n'ont pas été
  filtrées. Elles ont été supprimées de cet exemple de jeu de données pour plus de simplicité.
</p>

## Fusionner les données individuelles avec les données de liste :

Si vous regardez attentivement les images partagées ci-dessus, vous pouvez voir la colonne `_index` avec
la valeur "1" dans la première feuille **Repeat Group (Merge)**. De même, il y a aussi
une colonne `_parent_index` avec la valeur "1" dans la deuxième feuille **CR**. `_index` et
`_parent_index` sont des variables supplémentaires créées par le système pour gérer les groupes répétés. Ce sont les variables de correspondance nécessaires pour fusionner les _données individuelles_ et
les _données de liste_ ensemble en un seul jeu.

Voici deux approches pour fusionner les _données individuelles_ et les _données de liste_ en un
seul jeu de données via **Power Query** dans **Excel**. Vous pouvez utiliser l'une des
approches suivantes :

### Première approche : Fusionner les données individuelles avec les données de liste (lorsque le jeu de données est déjà ouvert)

Pour la première approche, vous devez avoir ouvert votre jeu de données XLS. Pour plus de détails,
veuillez consulter la vidéo ci-dessous :

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/xls_dataset_open.mp4"
    type="video/mp4"
  />
</video>

-   Ouvrez le jeu de données qui contient à la fois les _données individuelles_ et les _données de liste_.

-   Sélectionnez toutes les données de la première feuille _(données individuelles)_.

-   Sous l'onglet **Données**, sélectionnez **À partir d'un tableau/d'une plage**.

-   Une boîte de dialogue **(Créer un tableau)** apparaîtra. Sélectionnez **OK**.

-   Sélectionnez l'icône **Fermer et charger** qui se trouve dans le coin supérieur gauche de
    l'écran. Vous devriez maintenant voir deux options déroulantes : **Fermer et charger** et
    **Fermer et charger vers…**.

-   Sélectionnez **Fermer et charger vers…**.

-   Une boîte de dialogue **(Importer des données)** apparaîtra. Sélectionnez **Créer uniquement une
    connexion** puis appuyez sur **OK**.

-   Vous avez maintenant créé une table de requête pour les _(données individuelles)_.

-   Vous pouvez maintenant aller à la deuxième feuille, _(données de liste)_, et suivre exactement les
    mêmes étapes que vous avez effectuées ci-dessus.

-   Avec cela, vous avez créé une table de requête pour les _(données de liste)_.

-   Sous l'onglet **Données**, sélectionnez **Obtenir des données**. De là, sélectionnez **Combiner
    des requêtes** puis **Fusionner**.

-   Une boîte de dialogue **Fusionner** apparaît.

-   Chargez les deux tables de requête. Une fois les deux tables chargées, sélectionnez la
    variable de correspondance `_index` de la première table. De même, sélectionnez la
    variable de correspondance `_parent_index` de la deuxième table. Dès que vous
    sélectionnez les deux variables de correspondance, vous devriez pouvoir voir **La sélection
    correspond à … des … lignes de la première table**. La table de requête devrait maintenant être
    fusionnée.

-   Pour développer la table fusionnée, cochez toutes les variables que vous souhaitez avoir dans
    le jeu de données fusionné. Vous pouvez également décocher **Utiliser le nom de colonne d'origine comme
    préfixe** pour avoir le nom de variable d'origine dans le jeu de données fusionné. Lorsque
    tout est terminé, sélectionnez **OK**.

-   Vous devriez maintenant avoir le jeu de données fusionné final.

-   Une fois de plus, sélectionnez l'icône **Fermer et charger** qui se trouve dans le coin supérieur gauche
    de l'écran. Vous devriez voir deux options déroulantes : **Fermer et charger** et
    **Fermer et charger vers…**.

-   Sélectionnez **Fermer et charger**. Avec ce dernier clic, vous avez fusionné vos
    _données individuelles_ et vos _données de liste_ en un seul jeu de données.

### Deuxième approche : Fusionner les données individuelles avec les données de liste (lorsque le jeu de données n'est pas encore ouvert)

Utilisez la deuxième approche lorsque vous n'avez pas encore ouvert votre jeu de données XLS et que vous avez
seulement ouvert un nouveau classeur Excel. Pour plus de détails, veuillez consulter la vidéo ci-dessous :

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/new_excel_workbook.mp4"
    type="video/mp4"
  />
</video>

-   Ouvrez un nouveau classeur Excel.

-   Sous l'onglet **Données**, sélectionnez **Obtenir des données**. De là, sélectionnez **À partir d'un fichier**
    puis **À partir d'un classeur**.

-   Recherchez le fichier sur votre PC. Une fois que vous le voyez, sélectionnez le fichier puis
    appuyez sur **Importer**.

-   Une boîte de dialogue **Navigateur** apparaît. Ici, cochez **Sélectionner plusieurs éléments**
    et les noms de feuilles **CR** et **Repeat Group (Merge)** qui sont visibles.
    Une fois qu'ils sont cochés, le bouton **Charger** en bas de la boîte de dialogue
    s'active.

-   Sélectionnez le bouton **Charger**. Vous devriez voir deux options déroulantes : **Charger**
    et **Charger vers…**. Sélectionnez **Charger**.

-   Avec cela, vous avez créé des tables de requête pour les _(données individuelles)_ et les
    _(données de liste)_.

-   Sous l'onglet **Données**, sélectionnez **Obtenir des données**. De là, sélectionnez **Combiner
    des requêtes** puis sélectionnez **Fusionner**.

-   Une boîte de dialogue **Fusionner** apparaît.

-   Chargez les deux tables de requête. Une fois les deux tables chargées, sélectionnez la
    variable de correspondance `_index` de la première table. De même, sélectionnez la
    variable de correspondance `_parent_index` de la deuxième table. Dès que vous
    sélectionnez les deux variables de correspondance, vous devriez pouvoir voir **La sélection
    correspond à … des … lignes de la première table**. La table de requête devrait maintenant être
    fusionnée.

-   Pour développer la table fusionnée, cochez toutes les variables que vous souhaitez avoir dans
    le jeu de données fusionné. Vous pouvez également décocher **Utiliser le nom de colonne d'origine comme
    préfixe** pour avoir le nom de variable d'origine dans le jeu de données fusionné. Lorsque
    tout est terminé, sélectionnez **OK**.

-   Vous devriez maintenant avoir le jeu de données fusionné final.

-   Une fois de plus, sélectionnez l'icône **Fermer et charger** qui se trouve dans le coin supérieur gauche
    de l'écran. Vous devriez voir deux options déroulantes : **Fermer et charger** et
    **Fermer et charger vers…**.

-   Sélectionnez **Fermer et charger**. Avec ce dernier clic, vous avez fusionné vos
    _données individuelles_ et vos _données de liste_ en un seul jeu de données.

<p class="note">
  Les différences entre les deux approches concernent le chargement de la table de requête. Une fois
  que les tables de requête sont chargées, vous devrez suivre les mêmes étapes pour fusionner
  les <em>données individuelles</em> et les <em>données de liste</em>.
</p>

## Dépannage :

-   L'exportation de _groupes répétés_ n'est pas prise en charge au format CSV. Vous devrez
    télécharger les données au format XLS.

-   Microsoft Power Query pour Excel est un complément Excel. Vous pouvez le télécharger
    via ce
    [site de téléchargement Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=39379).
    Il devrait fonctionner au mieux sur _Excel pour Microsoft 365_ ou _Excel 2021_, _Excel
    2019_, _Excel 2016_, _Excel 2013_, et _Excel 2010_. Pour plus de détails,
    veuillez consulter le
    [site d'assistance Microsoft](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a).

<p class="note">
  Pour vous exercer, vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge).xlsx"
    >ici</a
  >
  et à l'exemple de jeu de données
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge)_dataset.xlsx"
    >ici</a
  >
  qui ont été utilisés dans cet article.
</p>