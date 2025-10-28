# Utilisation de l'API pour les exports synchrones
<a href="../synchronous_exports.html">Read in English</a> | <a href="../es/synchronous_exports.html">Leer en español</a> | <a href="../ar/synchronous_exports.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/a4e0388d846fe94926c32f6dacb82b6e34c7f102/source/synchronous_exports.md" class="reference">13 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/qrkLi3VixVs?si=UXE40HQX2jEQrjBs" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox propose deux méthodes principales pour accéder à vos données : les exports asynchrones et synchrones. La méthode asynchrone standard consiste à [télécharger manuellement des fichiers de données](export_download.md) contenant toutes les soumissions jusqu'au moment du téléchargement. En revanche, les exports synchrones permettent l'intégration automatique de vos données KoboToolbox avec des applications externes telles que Microsoft Power BI, Excel ou Google Sheets.

Avec les exports synchrones, vos données se mettent à jour automatiquement à mesure que de nouvelles soumissions sont reçues, éliminant ainsi le besoin d'actualisation manuelle. Cette méthode fournit un fichier CSV ou XLSX, configuré avec vos paramètres d'export prédéfinis, qui peuvent inclure les libellés de questions, les langues, les filtres et les données de groupes répétés.

<p class="note">
    <strong>Remarque :</strong> Cet article se concentre sur les exports synchrones, qui constituent l'une des deux principales façons d'utiliser l'API KoboToolbox. L'autre est l'API JSON, conçue pour les scripts personnalisés et les automatisations en temps réel, fournissant des données JSON brutes, enregistrement par enregistrement. Contrairement aux exports synchrones, l'API JSON n'inclut pas de fonctionnalités d'export avancées telles que les libellés de questions ou la prise en charge de plusieurs langues.
</p>

Cet article couvre les étapes suivantes :

- Générer un export nommé
- Récupérer le lien d'export synchrone
- Connecter vos données à une application externe et authentification
  
## Générer un export nommé

Pour générer des exports synchrones, vous devez d'abord créer un export nommé pour votre projet en suivant ces étapes :

1. Dans votre projet KoboToolbox, accédez à l'onglet **DONNÉES > Téléchargements**.
2. Ajustez les [paramètres d'export](export_download.md) selon vos besoins.
3. Cliquez sur **Options avancées** pour [personnaliser les données](advanced_export.md) à exporter.
4. Choisissez **Enregistrer la sélection sous…** et fournissez un nom pour votre export.
5. Cliquez sur **Exporter** pour enregistrer ces paramètres.

## Récupérer le lien d'export synchrone

Pour récupérer le lien d'export synchrone, vous aurez besoin des éléments suivants :

- **UID de l'actif du projet :** Un identifiant unique pour chaque projet KoboToolbox, trouvé dans l'URL du projet.
- **URL du serveur :** L'URL du serveur que vous utilisez (`kf.kobotoolbox.org` pour Le serveur KoboToolbox mondial, `eu.kobotoolbox.org` pour Le serveur KoboToolbox Union européenne, ou `[votre organisation].kobotoolbox.org` pour les serveurs privés).

<p class="note">
    Pour plus d'informations sur la récupération de l'URL du serveur et de l'UID de l'actif du projet, consultez <a href="api.html">Premiers pas avec l'API</a>.
</p>

Pour récupérer le lien d'export, suivez ces étapes :

1. Ouvrez un nouvel onglet de navigateur.
2. Remplacez votre **URL du serveur** et votre **UID de l'actif du projet** dans l'URL suivante : `https://[server_url]/api/v2/assets/[project_asset_uid]/export-settings/`.
3. Ouvrez la page web correspondant à l'URL modifiée.
4. Faites défiler jusqu'à la section **CURRENT ENDPOINT**.
5. Trouvez le paramètre d'export qui correspond à l'export nommé que vous avez créé lors de la première étape.
6. Localisez les liens `data_url_csv` et `data_url_xlsx`, qui sont les liens d'export synchrone de votre projet.
7. Copiez le lien qui correspond le mieux à vos besoins (fichier CSV ou XLSX).

![Récupération du lien d'export synchrone](images/synchronous_exports/export_link.png)

<p class="note">
    <strong>Remarque :</strong> Les groupes répétés sont exportés sous forme de feuilles séparées dans les fichiers Excel et ne sont pas inclus dans les exports CSV. Si votre projet contient des groupes répétés, utilisez le lien <code>data_url_xlsx</code>.
</p>

## Connecter vos données à une application externe

Après avoir récupéré le lien d'export synchrone, vous pouvez connecter vos données à votre application externe préférée. La méthode d'intégration du lien d'export synchrone variera selon l'application.

<p class="note">
    Pour apprendre à connecter vos données à Power BI afin de créer des tableaux de bord personnalisés, consultez <a href="pulling_data_into_powerbi.html">Connexion de KoboToolbox à Power BI</a>. 
    <br><br>
    Pour apprendre à connecter vos données à Microsoft Excel, consultez <a href="pulling_data_into_excelquery.html">Connexion de KoboToolbox à Microsoft Excel</a>.
</p>

### Authentification

De nombreuses applications externes peuvent se connecter à vos données KoboToolbox. Cependant, toutes ne prennent pas en charge les **requêtes authentifiées**, qui sont des requêtes contenant des identifiants (par exemple, la clé API ou le nom d'utilisateur et le mot de passe) afin que le serveur puisse vérifier l'identité de l'appelant. Si l'application externe ne prend pas en charge les requêtes authentifiées, elle ne pourra accéder qu'aux ressources qui ont été rendues **accessibles publiquement** via un lien d'export anonyme.

Pour connecter votre projet sans authentification (par exemple, à Google Sheets), vous devrez vous assurer que le paramètre « Tout le monde peut voir les soumissions faites à ce formulaire » est coché dans **PARAMÈTRES > Partage**.

<p class="note">
    Pour plus d'informations sur le partage de projets, consultez <a href="project_sharing_settings.html">Partage de projets avec les paramètres au niveau du projet</a>.
</p>

Pour les projets contenant des données sensibles ou privées, l'option « Tout le monde peut voir les soumissions faites à ce formulaire » doit rester décochée. Dans ces cas, envisagez d'utiliser uniquement des applications prenant en charge les requêtes authentifiées.

Lors de l'utilisation d'applications prenant en charge les requêtes authentifiées, telles que Power BI, il vous sera demandé une authentification de base avec votre nom d'utilisateur et votre mot de passe ou un jeton (également appelé clé API) pour accéder aux données. Votre clé API se trouve dans vos **PARAMÈTRES DU COMPTE** sous l'onglet **Sécurité**.

<p class="note">
    Pour plus d'informations sur la clé API, consultez <a href="api.html">Premiers pas avec l'API</a>.
</p>

## Limitations

Pour maintenir la fiabilité du serveur, les exports synchrones présentent les limitations suivantes :

- **Intervalle d'actualisation des données :** Les données dans les exports synchrones se mettent à jour toutes les 5 minutes. Les demandes d'export effectuées dans cette fenêtre de 5 minutes n'incluront pas les nouvelles données de soumission reçues pendant cet intervalle de 5 minutes.
- **Temps de finalisation de l'export :** Les exports doivent se terminer dans les 120 secondes. Les projets comportant un grand nombre de soumissions ou de questions peuvent échouer. Pour éviter cela, ajoutez une contrainte de requête dans les paramètres d'export pour limiter les soumissions ou filtrer les questions inutiles. Consultez ce [post du Forum communautaire](https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4) pour obtenir des conseils.