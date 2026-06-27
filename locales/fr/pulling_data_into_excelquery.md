# Connexion de KoboToolbox à Microsoft Excel
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/df082614a0ae0bce8543b0c1474a9567fea7293e/source/pulling_data_into_excelquery.md" class="reference">23 août 2022</a>


KoboToolbox vous permet de connecter votre projet de collecte de données à des programmes externes tels que Microsoft Excel, Power BI ou Google Sheets, grâce à l'interface de programmation d'application (API).

Cet article vous guide tout au long du processus de connexion de votre projet à Excel. Si vous souhaitez vous connecter à Power BI, consultez l'article [Connexion de KoboToolbox à Power BI](pulling_data_into_powerbi.md).

## Étape 1 : Obtenir l'URL des exports synchronisés

Pour importer des données dans Excel, vous devez d'abord obtenir l'URL des exports synchronisés via l'API KoboToolbox. La procédure détaillée est décrite dans l'article [Utiliser l'API pour les exports synchronisées](synchronous_exports.md).

## Étape 2 : Ajouter la source de données

<p class="note">Ces étapes ne fonctionnent que dans Excel 2016 et versions ultérieures.</p>

- Ouvrez Excel et créez un classeur vide. Vous pouvez également travailler dans un classeur existant, même s'il contient déjà des données.
- Cliquez sur l'onglet **Données**, puis choisissez **Obtenir des données -> À partir d'autres sources -> À partir du web**.
- Collez l'URL des exports synchronisés que vous avez copiée et cliquez sur **OK**.

![Obtenir des données](images/pulling_data_excelquery/get_data.gif)

- Dans la boîte de dialogue « Accéder au contenu web », cliquez sur **De base** pour saisir vos informations d'authentification.
- Entrez votre nom d'utilisateur et votre mot de passe KoboToolbox, puis cliquez sur **CONNECTER**.

![Authentification](images/pulling_data_excelquery/authentication.gif)

<p class="note">
  Si vous avez rendu les données de votre projet publiques, vous pouvez vous connecter sans authentification en choisissant « Anonyme » dans la boîte de dialogue « Accéder au contenu web ». Pour en savoir plus sur les droits d'accès au niveau du projet, consultez l'article
  <a href="managing_permissions.html" class="reference">Droits d'accès au niveau de l'utilisateur</a>.
</p>

La liste des données contenues dans votre projet s'affiche dans le Navigateur.

<p class="note">
  Si votre formulaire contient des groupes répétés, chaque groupe apparaîtra sous la forme d'un onglet distinct dans le Navigateur. Veillez à utiliser le lien « data_url_xlsx », car l'export CSV <em>n'inclut pas</em> les groupes répétés.
</p>

- Choisissez les données que vous souhaitez importer. Pour importer plusieurs tables à la fois, cliquez sur « Sélectionner plusieurs éléments », puis choisissez les éléments dans la liste.
- Cliquez sur **Charger** pour importer les données, ou sur **Transformer les données** pour ouvrir l'éditeur Power Query, qui vous permet de nettoyer et de transformer les données avant de les charger.

![Sélection des tables](images/pulling_data_excelquery/navigator.gif)

<p class="note">
  Vous pouvez connecter plusieurs projets dans un même classeur Excel. Répétez la procédure ci-dessus pour chaque projet en utilisant son URL d'export synchronisé. Dans la plupart des cas où vous disposez de plusieurs tables, il peut être nécessaire de définir des relations entre les tables avant de pouvoir utiliser les champs pour créer des rapports et des tableaux de bord. Pour définir des relations, accédez à
  <strong>Données -> Outils de données -> Relations</strong>. Pour en savoir plus sur la création de relations entre tables, consultez la documentation
  <a
    href="https://support.microsoft.com/en-us/office/create-a-relationship-between-tables-in-excel-fe1b6be7-1d85-4add-a629-8a3848820be3"
    class="reference"
    >Microsoft</a
  >.
</p>

### Utiliser les données importées

Excel vous offre plusieurs façons de travailler avec les données que vous venez d'importer.

#### 1. Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques à partir du modèle de données

Un tableau croisé dynamique est un outil puissant permettant de calculer, de synthétiser et d'analyser des données, afin de visualiser des comparaisons, des tendances et des modèles. Les données synthétisées dans les tableaux croisés dynamiques peuvent être visualisées de manière simple à l'aide de graphiques croisés dynamiques.

- Cliquez sur l'**onglet Insertion**, puis sur la flèche déroulante du tableau croisé dynamique.
- Choisissez **À partir du modèle de données**.
- Choisissez **Nouvelle feuille de calcul**.
- Cliquez sur **OK**.

![Création d'un tableau croisé dynamique](images/pulling_data_excelquery/pivot.gif)

Les tables importées s'affichent dans le volet **Champs de tableau croisé dynamique**, où vous pouvez sélectionner les champs souhaités.

#### 2. Charger les données dans la feuille de calcul

Lorsque vous importez une seule table, par exemple si votre projet ne contient pas de groupes répétés, les données sont automatiquement chargées sous forme de tableau dans la feuille de calcul. En revanche, lorsque vos données se présentent sous la forme de plusieurs tables, celles-ci sont répertoriées dans le volet **Requêtes et connexions**.

Pour charger ces données dans votre feuille de calcul :

- Faites un clic droit sur une table dans le volet **Requêtes et connexions** et choisissez **Charger dans**. (Si le volet n'est pas visible, accédez à **Données -> Requêtes et connexions**.)
- Dans la boîte de dialogue suivante, choisissez **Tableau** et cliquez sur **OK**. Vous pouvez également choisir d'autres options disponibles selon vos besoins.

![Chargement d'une table dans Excel](images/pulling_data_excelquery/load_table.gif)

Vous pouvez effectuer cette opération pour toutes les tables répertoriées dans le volet **Requêtes et connexions**.

## Mettre à jour les données dans vos rapports

Lorsque les données de votre projet sont mises à jour sur le serveur KoboToolbox — par exemple lors de nouvelles soumissions, de modifications du statut de validation, de modifications ou de suppressions — vous devez les synchroniser avec vos rapports. Dans Excel :

- Accédez à l'onglet **Données**.
- Sous « Requêtes et connexions », cliquez sur **Actualiser**.

## Résolution de problèmes

### Échec de la connexion à KoboToolbox

Il peut arriver que, même après avoir saisi les identifiants corrects pour vous connecter à votre projet, vous obteniez une erreur. Cela peut se produire si Excel a été configuré pour se connecter à un compte précédent et que vous tentez maintenant de vous connecter avec un compte différent sur le même serveur KoboToolbox, par exemple deux comptes sur le serveur humanitaire.

Pour réinitialiser les paramètres d'authentification :

- Accédez à **Onglet Données -> Obtenir des données -> Paramètres de la source de données**. Sélectionnez les autorisations existantes dans la boîte de dialogue et cliquez sur **Effacer les autorisations**. Fermez la boîte de dialogue et essayez d'ajouter à nouveau la connexion.

![Effacer les paramètres de la source de données](images/pulling_data_excelquery/data_source_settings.gif)

### Échec de l'actualisation des données

Si vous obtenez une erreur lors de l'actualisation des données, plusieurs raisons sont possibles :

- Vos informations d'authentification ont peut-être changé. Vous devrez suivre les instructions ci-dessus pour modifier vos **Paramètres de la source de données**.
- Un ou plusieurs champs de votre formulaire ont peut-être été supprimés ou renommés. [Vous devrez modifier la requête dans Power Query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Il peut y avoir une incompatibilité de type de données, notamment si vous avez modifié le type de données d'un ou plusieurs champs dans Excel. Vous pouvez essayer de réinitialiser le type de données avant d'actualiser la connexion.