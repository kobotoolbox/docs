# Connexion de KoboToolbox à Power BI
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/ae9e699afd6c0ed484945430ba6722b974b99b49/source/pulling_data_into_powerbi.md" class="reference">22 août 2022</a>


L'API KoboToolbox vous permet de connecter votre projet à d'autres outils d'analyse de données tels que Power BI, Excel et Google Sheets. Les données que vous collectez sont partagées avec l'application externe, qui peut ensuite les utiliser pour des analyses, des visualisations et des tableaux de bord.

L'un des programmes d'analyse et de visualisation de données les plus populaires auxquels vous pouvez vous connecter est [Microsoft Power BI](https://powerbi.microsoft.com).

Cet article vous guide à travers les étapes de connexion de votre projet à Power BI. Si vous souhaitez vous connecter à Excel, consultez l'article [Connexion de KoboToolbox à Microsoft Excel](pulling_data_into_excelquery.md).

## Étape 1 : Obtenir l'URL des exports synchronisés

La première étape pour importer des données dans Power BI consiste à obtenir l'URL des exports synchronisés via l'API KoboToolbox. La procédure détaillée est décrite dans l'article [Utiliser l'API pour les exports synchronisées](synchronous_exports.md).

## Étape 2 : Ajouter la source de données

Une fois que vous disposez de votre URL, vous pouvez suivre les étapes ci-dessous dans Power BI :

- Cliquez sur la flèche du menu déroulant du bouton « Get Data »
- Choisissez « Web »
- Collez l'URL d'export synchronisé que vous avez copiée et cliquez sur **OK**
- Cliquez sur **Basic** pour renseigner vos informations d'authentification
- Saisissez votre nom d'utilisateur et votre mot de passe KoboToolbox, puis cliquez sur **CONNECT**

<p class="note">
  Si vous avez rendu les données de votre projet publiques, vous pouvez vous connecter sans authentification en choisissant « Anonymous » dans la boîte de dialogue « Access Web content ». Pour en savoir plus sur les droits d'accès au niveau du projet, consultez l'article <a href="managing_permissions.html" class="reference">Droits d'accès au niveau de l'utilisateur</a>.
</p>

La liste des données contenues dans votre projet s'affiche dans le Navigateur.

- Choisissez les données que vous souhaitez importer.
- Cliquez sur **Load** pour importer les données, ou sur **Transform Data** pour ouvrir l'éditeur Power Query, qui vous permet de nettoyer et de transformer les données avant de les charger.

![Obtenir des données et authentification](images/pulling_data_into_powerbi/get_data_auth.gif)

Les tableaux s'affichent dans le panneau **Fields**, où vous pouvez développer vos tableaux de bord et vos rapports.

<p class="note">
  Dans Power BI, vous pouvez connecter plusieurs projets. Répétez la procédure ci-dessus pour chaque projet en utilisant son URL d'export synchronisé. Si vous disposez de plusieurs tableaux (par exemple en cas de groupes répétés), vous devrez peut-être également configurer des relations entre les tableaux. Cette opération s'effectue dans la <strong>Model View</strong>. Pour en savoir plus sur la création de relations entre tableaux, consultez la documentation <a href="https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships" class="reference">ici</a>.
</p>

## Mettre à jour les données dans vos rapports

Lorsque les données de votre projet sont mises à jour sur le serveur KoboToolbox — par exemple lors de nouvelles soumissions, de modifications des statuts de validation, de modifications ou de suppressions — vous devez les synchroniser avec vos rapports.

Pour ce faire, cliquez sur **Refresh** dans l'onglet « Home ».

## Résolution de problèmes

### Échec de la connexion à KoboToolbox

Il peut arriver que, même après avoir saisi les identifiants corrects pour vous connecter à votre projet, une erreur s'affiche. Cela peut se produire si Power BI a été configuré pour se connecter à un compte précédent et que vous tentez maintenant de vous connecter avec un compte différent sur le même serveur KoboToolbox.

Pour réinitialiser les paramètres d'authentification :

- Accédez à **File -> Options and Settings -> Data Source Settings**. Sélectionnez les autorisations existantes dans la boîte de dialogue et cliquez sur **Clear Permissions**. Fermez la fenêtre et essayez d'ajouter à nouveau la connexion.

![Effacer les autorisations](images/pulling_data_into_powerbi/data_source_settings.gif)

### Échec de l'actualisation des données

Si une erreur s'affiche lors de l'actualisation des données, plusieurs raisons sont possibles :

- Vos informations d'authentification ont peut-être changé. Vous devrez suivre les instructions ci-dessus pour modifier vos **Data Source Settings**.
- Un ou plusieurs champs de votre formulaire ont peut-être été supprimés ou renommés. Vous devrez [modifier la requête](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Il peut y avoir une incompatibilité de types de données, notamment si vous avez modifié le type de données d'un ou plusieurs champs dans Power BI. Vous pouvez essayer de réinitialiser le type de données avant d'actualiser la connexion.