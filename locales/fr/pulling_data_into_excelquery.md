# Connexion de KoboToolbox à Microsoft Excel
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/df082614a0ae0bce8543b0c1474a9567fea7293e/source/pulling_data_into_excelquery.md" class="reference">23 août 2022</a>

KoboToolbox vous permet de connecter votre projet de collecte de données à des programmes externes tels que Microsoft Excel, Power BI ou Google Sheets, ce qui est rendu possible grâce à l'interface de programmation d'application (API).

Cet article vous guide à travers le processus de connexion de votre projet à Excel. Si vous souhaitez vous connecter à Power BI, consultez l'article [ici](pulling_data_into_powerbi.md).

## Étape 1 : Obtenir l'URL des exportations synchrones

Pour importer des données dans Excel, vous devez d'abord obtenir l'URL des exportations synchrones via l'API KoboToolbox. Le processus étape par étape pour ce faire est décrit dans l'article [ici](synchronous_exports.md).

## Étape 2 : Ajouter la source de données

<p class="note">Ces étapes ne fonctionnent que dans Excel 2016 et versions ultérieures.</p>

- Ouvrez Excel et créez un classeur vierge. Vous pouvez également travailler dans un classeur existant, même s'il contient déjà des données.
- Cliquez sur l'onglet **Données**, choisissez **Obtenir des données -> À partir d'autres sources -> À partir du web**.
- Collez l'URL des exportations synchrones que vous avez copiée et cliquez sur **OK**.

![Get data](images/pulling_data_excelquery/get_data.gif)

- Dans la boîte de dialogue « Accéder au contenu web », cliquez sur **De base** pour ajouter vos informations d'authentification.
- Entrez votre nom d'utilisateur et mot de passe KoboToolbox et cliquez sur **CONNEXION**.

![Authentication](images/pulling_data_excelquery/authentication.gif)

<p class="note">
  Si vous avez rendu les données de votre projet publiques, vous pouvez vous connecter sans authentification en choisissant « Anonyme » dans la boîte de dialogue « Accéder au contenu web ». Pour en savoir plus sur les autorisations de projet, consultez
  <a href="managing_permissions.html" class="reference">ici</a>.
</p>

Une liste des données contenues dans votre projet s'affichera dans le Navigateur.

<p class="note">
  Si votre formulaire contient des groupes répétés, chaque groupe apparaîtra comme une feuille de calcul distincte dans le Navigateur. Assurez-vous d'utiliser le lien « data_url_xlsx » car l'exportation CSV <em>n'inclut pas</em> les groupes répétés.
</p>

- Choisissez les données que vous souhaitez importer. Pour importer plusieurs tableaux à la fois, cliquez sur « Sélectionner plusieurs éléments », puis choisissez les éléments dans la liste.
- Cliquez sur **Charger** pour importer les données ou cliquez sur **Transformer les données** pour ouvrir l'Éditeur Power Query que vous pouvez utiliser pour nettoyer et transformer les données avant de les charger.

![Choosing tables](images/pulling_data_excelquery/navigator.gif)

<p class="note">
  Vous pouvez connecter plusieurs projets dans un seul classeur Excel. Répétez le processus ci-dessus pour chaque projet, en utilisant leur URL d'exportation synchrone. Dans la plupart des cas où vous avez plusieurs tableaux, il peut être nécessaire de configurer des relations entre les tableaux avant de pouvoir utiliser les champs pour créer des rapports et des tableaux de bord. Configurez les relations en allant dans
  <strong>Données -> Outils de données -> Relations</strong>. Pour en savoir plus sur la création de relations entre tableaux, consultez
  <a
    href="https://support.microsoft.com/en-us/office/create-a-relationship-between-tables-in-excel-fe1b6be7-1d85-4add-a629-8a3848820be3"
    class="reference"
    >ici</a
  >.
</p>

### Utilisation des données importées

Excel vous offre plusieurs façons de travailler avec les données que vous venez d'importer.

#### 1. Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques à partir du modèle de données

Un tableau croisé dynamique est un outil puissant utilisé pour calculer, résumer et analyser des données - vous permettant de voir des comparaisons, des modèles et des tendances dans les données. Les données résumées dans les tableaux croisés dynamiques peuvent être visualisées de manière simple à l'aide de graphiques croisés dynamiques.

- Cliquez sur l'onglet **Insertion**, puis cliquez sur la flèche déroulante sur Tableau croisé dynamique
- Choisissez **À partir du modèle de données**
- Choisissez **Nouvelle feuille de calcul**
- Cliquez sur **OK**

![Creating a pivot table](images/pulling_data_excelquery/pivot.gif)

Les tableaux importés seront affichés dans le volet latéral **Champs de tableau croisé dynamique** où vous pouvez choisir les champs nécessaires.

#### 2. Charger les données dans la feuille de calcul

Lorsque vous importez un seul tableau, par exemple lorsque votre projet ne comportait aucun groupe répété, les données sont automatiquement chargées sous forme de tableau dans la feuille de calcul. Cependant, lorsque vos données se présentent sous forme de plusieurs tableaux, les tableaux sont répertoriés dans le panneau **Requêtes et connexions**.

Pour charger ces données dans votre feuille de calcul :

- Faites un clic droit sur un tableau du volet **Requêtes et connexions** et choisissez **Charger vers**. (si vous ne voyez pas le volet, allez dans **Données -> Requêtes et connexions**.
- Dans la boîte de dialogue suivante, choisissez **Tableau** et cliquez sur **OK**. Vous pouvez également choisir les autres options disponibles selon vos besoins.

![Loading a table in Excel](images/pulling_data_excelquery/load_table.gif)

Vous pouvez faire cela pour tous les tableaux répertoriés dans le volet **Requêtes et connexions**.

## Mise à jour des données dans vos rapports

Lorsque les données de votre projet sont mises à jour sur le serveur KoboToolbox, par exemple lorsque vous avez de nouvelles soumissions, des statuts de validation modifiés, des modifications ou des suppressions, vous devrez les synchroniser avec vos rapports. Dans Excel :

- Accédez à l'onglet **Données**
- Sous « Requêtes et connexions », cliquez sur **Actualiser**

## Dépannage

### Échec de connexion à KoboToolbox

Parfois, même après avoir saisi les informations d'identification correctes pour vous connecter à votre projet, vous pouvez obtenir une erreur. Cela peut se produire si Excel a été configuré pour se connecter à un compte auparavant, et que vous essayez maintenant de vous connecter en utilisant un compte différent du même serveur KoboToolbox, c'est-à-dire tous deux du serveur humanitaire.

Pour réinitialiser les paramètres d'authentification :

- Allez dans **Onglet Données -> Obtenir des données -> Paramètres de la source de données**. Sélectionnez les autorisations existantes dans la boîte de dialogue et cliquez sur **Effacer les autorisations**. Fermez et essayez d'ajouter à nouveau la nouvelle connexion.

![Clearing data source settings](images/pulling_data_excelquery/data_source_settings.gif)

### Échec de l'actualisation des données

Si vous obtenez une erreur lors de l'actualisation des données, il peut y avoir plusieurs raisons :

- Vos informations d'authentification ont peut-être changé. Vous devrez suivre les instructions ci-dessus pour modifier vos **Paramètres de la source de données**.
- Un ou plusieurs champs de votre formulaire ont peut-être été supprimés ou renommés. [Vous devrez modifier la requête dans Power Query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Il peut y avoir une incompatibilité de type de données, surtout si vous avez modifié le type de données d'un ou plusieurs champs dans Excel. Vous pouvez essayer de réinitialiser le type de données avant d'actualiser la connexion.