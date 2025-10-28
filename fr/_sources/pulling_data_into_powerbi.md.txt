# Connecter KoboToolbox à Power BI
<a href="../pulling_data_into_powerbi.html">Read in English</a> | <a href="../es/pulling_data_into_powerbi.html">Leer en español</a> | <a href="../ar/pulling_data_into_powerbi.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/ae9e699afd6c0ed484945430ba6722b974b99b49/source/pulling_data_into_powerbi.md" class="reference">22 août 2022</a>

L'API KoboToolbox vous permet de connecter votre projet à d'autres outils d'analyse de données tels que Power BI, Excel et Google Sheets. Les données que vous collectez sont partagées avec l'application externe qui peut ensuite être utilisée pour l'analyse, les visualisations et les tableaux de bord.

L'un des programmes d'analyse et de visualisation de données les plus populaires auquel vous pouvez vous connecter est [Microsoft Power BI](https://powerbi.microsoft.com).

Cet article vous guide à travers les étapes de connexion de votre projet avec Power BI. Si vous souhaitez vous connecter à Excel, consultez l'article [ici](pulling_data_into_excelquery.md).

## Étape 1 : Obtenir l'URL des exports synchrones

La première étape pour importer des données dans Power BI consiste à obtenir l'URL des exports synchrones via l'API KoboToolbox. Un processus détaillé pour ce faire est décrit dans l'article [ici](synchronous_exports.md).

## Étape 2 : Ajouter la source de données

Une fois que vous avez votre URL, vous pouvez procéder aux étapes ci-dessous dans Power BI :

- Cliquez sur la flèche déroulante du bouton « Obtenir des données »
- Choisissez « Web »
- Collez l'URL d'export synchrone que vous avez copiée et cliquez sur **OK**
- Cliquez sur **De base** pour ajouter vos informations d'authentification
- Saisissez votre nom d'utilisateur et mot de passe KoboToolbox et cliquez sur **CONNEXION**

<p class="note">
  Si vous avez rendu les données de votre projet publiques, vous pouvez vous connecter sans avoir besoin d'authentification en choisissant « Anonyme » dans la boîte de dialogue « Accéder au contenu Web ». Pour en savoir plus sur les autorisations de projet, consultez
  <a href="managing_permissions.html" class="reference">ici</a>.
</p>

Une liste des données contenues dans votre projet s'affichera dans le Navigateur.

- Choisissez les données que vous souhaitez importer.
- Cliquez sur **Charger** pour importer les données ou cliquez sur **Transformer les données** pour ouvrir l'Éditeur Power Query, que vous pouvez utiliser pour nettoyer et transformer les données avant de les charger.

![Obtenir des données et Authentification](images/pulling_data_into_powerbi/get_data_auth.gif)

Les tableaux seront affichés dans le panneau **Champs** où vous pouvez développer vos tableaux de bord et rapports.

<p class="note">
  Dans Power BI, vous pouvez connecter plusieurs projets. Répétez le processus ci-dessus pour chaque projet, en utilisant leur URL d'export synchrone. Dans le cas où vous avez plusieurs tableaux (par exemple si vous aviez des groupes répétés), vous devrez peut-être également configurer des relations entre les tableaux. Cela se fait dans la <strong>Vue Modèle</strong>. Pour en savoir plus sur la création de relations entre tableaux, consultez
  <a
    href="https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships"
    class="reference"
    >ici</a
  >.
</p>

## Mettre à jour les données dans vos rapports

Lorsque les données de votre projet sont mises à jour sur le serveur KoboToolbox, par exemple lorsque vous avez de nouvelles soumissions, des statuts de validation modifiés, des modifications ou des suppressions, vous devrez les synchroniser avec vos rapports.

Pour ce faire, cliquez sur **Actualiser** dans l'onglet « Accueil ».

## Dépannage

### Échec de connexion à KoboToolbox

Parfois, même après avoir saisi les informations d'identification correctes pour vous connecter à votre projet, vous pourriez voir une erreur. Cela peut se produire si Power BI a été configuré pour se connecter à un compte auparavant, et que vous essayez maintenant de vous connecter en utilisant un compte différent du même serveur KoboToolbox.

Pour réinitialiser les paramètres d'authentification :

- Allez dans **Fichier -> Options et paramètres -> Paramètres de source de données**. Sélectionnez les autorisations existantes dans la boîte de dialogue et cliquez sur **Effacer les autorisations**. Fermez et essayez d'ajouter à nouveau la nouvelle connexion.

![Effacer les autorisations](images/pulling_data_into_powerbi/data_source_settings.gif)

### Échec de l'actualisation des données

Si vous obtenez une erreur lors de l'actualisation des données, il peut y avoir plusieurs raisons :

- Vos informations d'authentification ont peut-être changé. Vous devrez suivre les instructions ci-dessus pour modifier vos **Paramètres de source de données**.
- Un ou plusieurs champs de votre formulaire ont peut-être été supprimés ou renommés. Vous devrez [modifier la requête](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Il peut y avoir une incompatibilité de type de données, surtout si vous avez modifié le type de données d'un ou plusieurs champs dans Power BI. Vous pouvez essayer de réinitialiser le type de données avant d'actualiser la connexion.