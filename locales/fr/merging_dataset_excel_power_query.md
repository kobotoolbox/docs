# Fusionner des données individuelles avec des données répétées via Power Query dans Excel
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/73dbdbb56448bbfbdb62af8017b71582965291d2/source/merging_dataset_excel_power_query.md" class="reference">6 Apr 2022</a>


Comme illustré dans l'article d'aide
[Groupes et groupes répétés dans le Formbuilder](group_repeat.md), vous pouvez utiliser
des groupes répétés pour répondre à certaines exigences d'enquête. Vous pourriez également avoir besoin
d'analyser les données issues des groupes répétés collectées. Lors du
[téléchargement des données depuis le serveur (au format XLS)](export_download.md), vous
devriez voir les données dans la structure suivante :

![Dataset Sheets](/images/merging_dataset_excel_power_query/dataset_sheets.png)

Le premier onglet portant le nom **Repeat Group (Merge)** visible dans l'image
ci-dessus contient les _données individuelles_ de l'enquête, tandis que le second onglet portant le nom **CR** contient les _données répétées_.

<p class="note">
  Pour les bases de données téléchargées, vous devriez avoir un onglet de plus que le nombre de
  <em>groupes répétés</em>. Par exemple, si votre formulaire d'enquête contient un
  <em>groupe répété</em>, vous devriez avoir deux onglets
  dans votre base de données.
</p>

Cet article d'aide illustrera également la différence entre les _données
individuelles_ et les _données répétées_. Il présentera ensuite les étapes permettant de les fusionner en
une seule base de données via **Power Query** dans **Excel**.

La fusion des _données individuelles_ et des _données répétées_ via le système n'est actuellement pas
disponible, mais elle est possible via **Power Query** dans **Excel**. Excel a
été choisi plutôt que d'autres logiciels car c'est un tableur largement utilisé et disponible
sur presque tous les PC. Il est également relativement facile à utiliser.

## Différences entre les données individuelles et les données répétées

Les _données individuelles_ sont des informations généralement collectées une seule fois au cours d'un
entretien. Les _données répétées_, en revanche, sont collectées plusieurs fois _(par exemple,
les détails de tous les membres d'une famille vivant au sein d'un même ménage)_ auprès du même
individu lors d'un entretien. Le nombre de cas dans les _données individuelles_ peut être égal
aux _données répétées_ mais ne peut jamais les dépasser, tandis que le nombre de cas dans les _données
répétées_ dépasse généralement les _données individuelles_, mais peut parfois être égal (sans jamais être inférieur).

Un formulaire d'enquête rempli, comme illustré ci-dessous, permet de visualiser les
différences entre les _données individuelles_ et les _données répétées_. _Veuillez noter que toutes les données
utilisées dans cet article d'aide sont hypothétiques_.

![Form](/images/merging_dataset_excel_power_query/form.png)

<p class="note">
  Toute donnée collectée en dehors du groupe répété constitue une
  <em>donnée individuelle</em>, et toute donnée collectée à l'intérieur d'un groupe répété
  constitue une <em>donnée répétée</em>.
</p>

Les données téléchargées au format XLS illustrent également la différence entre
les _données individuelles_ et les _données répétées_.

Chaque enregistrement _(comme illustré dans l'image ci-dessous)_, sous `Name of the household head`,
`Sex of the household head`, `Total family members in the household` et
`Total school going children (aged 6-16 years) in the household` du premier
onglet **Repeat Group (Merge)** constitue une _donnée individuelle_.

![Individual Data](/images/merging_dataset_excel_power_query/individual_data.png)

Cet exemple de base de données contient un total de 7 entretiens en tant que _données individuelles_.

De même, chaque enregistrement _(comme illustré dans l'image ci-dessous)_, sous `Name of child`,
`Age of child` et `Sex of child` du second onglet, **CR**, constitue une _donnée
répétée_.

![Roster Data](/images/merging_dataset_excel_power_query/roster_data.png)

Ainsi, cet exemple de base de données contient un total de 12 enregistrements en tant que _données répétées_.

<p class="note">
  <strong>Note :</strong> Lors du téléchargement d'une base de données depuis le serveur, vous devriez
  également pouvoir voir d'autres variables (variables de métadonnées) si elles n'ont pas été
  filtrées. Elles ont été supprimées de cet exemple de base de données par souci de simplicité.
</p>

## Fusionner les données individuelles avec les données répétées

Si vous examinez attentivement les images partagées ci-dessus, vous pouvez voir la colonne `_index` avec
la valeur « 1 » dans le premier onglet **Repeat Group (Merge)**. De même, il existe également
une colonne `_parent_index` avec la valeur « 1 » dans le second onglet **CR**. `_index` et
`_parent_index` sont des variables supplémentaires créées par le système pour gérer les groupes
répétés. Ce sont les variables de correspondance nécessaires pour fusionner les _données individuelles_ et les
_données répétées_ en une seule base de données.

Vous trouverez ci-dessous deux approches pour fusionner les _données individuelles_ et les _données répétées_ en une
seule base de données via **Power Query** dans **Excel**. Vous pouvez utiliser l'une ou l'autre des
approches suivantes :

### Première approche : fusionner les données individuelles avec les données répétées (lorsque la base de données est déjà ouverte)

Pour la première approche, vous devez avoir ouvert votre base de données XLS. Pour plus de détails,
veuillez regarder la vidéo ci-dessous :

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/xls_dataset_open.mp4"
    type="video/mp4"
  />
</video>

-   Ouvrez la base de données contenant à la fois les _données individuelles_ et les _données répétées_.

-   Sélectionnez toutes les données du premier onglet _(données individuelles)_.

-   Sous l'onglet **Données**, sélectionnez **À partir du tableau/de la plage**.

-   Une boîte de dialogue **(Créer un tableau)** s'affiche. Sélectionnez **OK**.

-   Sélectionnez l'icône **Fermer et charger** située en haut à gauche de l'écran. Vous devriez voir deux options dans le menu déroulant : **Fermer et charger** et
    **Fermer et charger dans…**.

-   Sélectionnez **Fermer et charger dans…**.

-   Une boîte de dialogue **(Importer des données)** s'affiche. Sélectionnez **Créer uniquement la connexion**, puis appuyez sur **OK**.

-   Vous avez maintenant créé une table de requête pour les _(données individuelles)_.

-   Vous pouvez maintenant accéder au second onglet, _(données répétées)_, et suivre exactement
    les mêmes étapes que celles effectuées ci-dessus.

-   Vous avez ainsi créé une table de requête pour les _(données répétées)_.

-   Sous l'onglet **Données**, sélectionnez **Obtenir des données**. Ensuite, sélectionnez **Combiner
    des requêtes**, puis **Fusionner**.

-   Une boîte de dialogue **Fusionner** s'affiche.

-   Chargez les deux tables de requête. Une fois les deux tables chargées, sélectionnez la
    variable de correspondance `_index` dans la première table. De même, sélectionnez la
    variable de correspondance `_parent_index` dans la seconde table. Dès que vous
    sélectionnez les deux variables de correspondance, vous devriez voir **La sélection
    correspond à … lignes sur … de la première table**. La table de requête devrait maintenant être
    fusionnée.

-   Pour développer la table fusionnée, cochez toutes les variables que vous souhaitez inclure dans
    la base de données fusionnée. Vous pouvez également décocher **Utiliser le nom de colonne d'origine comme
    préfixe** pour conserver le nom de variable d'origine dans la base de données fusionnée. Une fois
    tout terminé, sélectionnez **OK**.

-   Vous devriez maintenant avoir la base de données fusionnée finale.

-   Sélectionnez à nouveau l'icône **Fermer et charger** située en haut à gauche de l'écran. Vous devriez voir deux options dans le menu déroulant : **Fermer et charger**
    et **Fermer et charger dans…**.

-   Sélectionnez **Fermer et charger**. Ce dernier clic vous permet de fusionner vos
    _données individuelles_ et vos _données répétées_ en une seule base de données.

### Seconde approche : fusionner les données individuelles avec les données répétées (lorsque la base de données n'est pas encore ouverte)

Utilisez la seconde approche lorsque vous n'avez pas encore ouvert votre base de données XLS et que vous avez
uniquement ouvert un nouveau classeur Excel. Pour plus de détails, veuillez regarder la vidéo ci-dessous :

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/new_excel_workbook.mp4"
    type="video/mp4"
  />
</video>

-   Ouvrez un nouveau classeur Excel.

-   Sous l'onglet **Données**, sélectionnez **Obtenir des données**. Ensuite, sélectionnez **À partir d'un fichier**,
    puis **À partir d'un classeur**.

-   Recherchez le fichier sur votre PC. Une fois que vous le voyez, sélectionnez le fichier, puis
    appuyez sur **Importer**.

-   Une boîte de dialogue **Navigateur** s'affiche. Ici, cochez **Sélectionner plusieurs éléments**
    ainsi que les noms d'onglets **CR** et **Repeat Group (Merge)** qui sont visibles.
    Une fois cochés, le bouton **Charger** en bas de la boîte de dialogue
    devient actif.

-   Sélectionnez le bouton **Charger**. Vous devriez voir deux options dans le menu déroulant : **Charger**
    et **Charger dans…**. Sélectionnez **Charger**.

-   Vous avez ainsi créé des tables de requête pour les _(données individuelles)_ et les
    _(données répétées)_.

-   Sous l'onglet **Données**, sélectionnez **Obtenir des données**. Ensuite, sélectionnez **Combiner
    des requêtes**, puis **Fusionner**.

-   Une boîte de dialogue **Fusionner** s'affiche.

-   Chargez les deux tables de requête. Une fois les deux tables chargées, sélectionnez la
    variable de correspondance `_index` dans la première table. De même, sélectionnez la
    variable de correspondance `_parent_index` dans la seconde table. Dès que vous
    sélectionnez les deux variables de correspondance, vous devriez voir **La sélection
    correspond à … lignes sur … de la première table**. La table de requête devrait maintenant être
    fusionnée.

-   Pour développer la table fusionnée, cochez toutes les variables que vous souhaitez inclure dans
    la base de données fusionnée. Vous pouvez également décocher **Utiliser le nom de colonne d'origine comme
    préfixe** pour conserver le nom de variable d'origine dans la base de données fusionnée. Une fois
    tout terminé, sélectionnez **OK**.

-   Vous devriez maintenant avoir la base de données fusionnée finale.

-   Sélectionnez à nouveau l'icône **Fermer et charger** située dans le coin supérieur gauche
    de l'écran. Vous devriez voir deux options dans le menu déroulant : **Fermer et charger**
    et **Fermer et charger dans…**.

-   Sélectionnez **Fermer et charger**. Ce dernier clic vous permet de fusionner vos
    _données individuelles_ et vos _données répétées_ en une seule base de données.

<p class="note">
  Les différences entre les deux approches concernent le chargement de la table de requête. Une fois
  les tables de requête chargées, vous devrez suivre les mêmes étapes pour fusionner les
  <em>données individuelles</em> et les <em>données répétées</em>.
</p>

## Résolution de problèmes

-   L'export des _groupes répétés_ n'est pas disponible au format CSV. Vous devrez
    télécharger les données au format XLS.

-   Microsoft Power Query pour Excel est un complément Excel. Vous pouvez le télécharger via ce
    [site de téléchargement Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=39379).
    Il fonctionne de manière optimale avec _Excel pour Microsoft 365_ ou _Excel 2021_, _Excel
    2019_, _Excel 2016_, _Excel 2013_ et _Excel 2010_. Pour plus de détails,
    veuillez consulter le
    [site d'assistance Microsoft](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a).

<p class="note">
  Pour vous entraîner, vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge).xlsx"
    >ici</a
  >
  et à l'exemple de base de données
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge)_dataset.xlsx"
    >ici</a
  >
  utilisés dans cet article.
</p>