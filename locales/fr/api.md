# Introduction à l'API
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/afd562326337a448c613f919951aaed8005b62ef/source/api.md" class="reference">22 Jun 2026</a>


Une **interface de programmation d'application (API)** permet à deux composants logiciels de communiquer à l'aide d'un ensemble de définitions et de protocoles. Grâce à une API, un script ou une application peut interagir avec KoboToolbox sans utiliser l'interface web. Par exemple, vous pouvez générer automatiquement des exports de données reliés à des sources externes telles que des tableaux de bord ou des dossiers de sauvegarde.

Avec l'**API** KoboToolbox, vous pouvez :

- **Télécharger des données** automatiquement en JSON, CSV ou XLSX.
- **Générer des exports à la demande** pour des tableaux de bord, des sauvegardes ou des analyses.
- **Soumettre ou modifier des soumissions** depuis d'autres outils de collecte de données.
- **Créer ou déployer des projets** et cloner des projets existants par programmation.
- **Gérer les utilisateurs**, les droits d'accès et l'activité des projets à grande échelle.

L'utilisation de l'API KoboToolbox vous permet d'automatiser les tâches répétitives, de maintenir vos tableaux de bord à jour et d'intégrer KoboToolbox à d'autres systèmes, tout en réduisant les étapes manuelles et les erreurs. Cet article présente une introduction à l'API KoboToolbox et couvre les étapes suivantes :

- Récupérer l'**URL du serveur**
- Récupérer votre **clé API**
- Récupérer l'UID du projet
- Exporter vos données via l'API
- Documentation avancée de l'API

## Récupérer l'URL du serveur
L'**URL du serveur** est l'adresse web de base de votre serveur KoboToolbox. Elle est placée au début de chaque requête API.

Pour la plupart des utilisateurs, l'URL du serveur est [kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (si vous utilisez le serveur KoboToolbox mondial) ou [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (si vous utilisez le serveur KoboToolbox Union européenne).

![Récupérer l'URL du serveur](images/api/server_URL.png)

## Récupérer votre clé API
Votre **clé API** est un jeton personnel qui fonctionne comme un mot de passe, permettant à un logiciel d'accéder à votre compte via l'API. Elle peut être requise lorsqu'un script, un tableau de bord ou une application externe a besoin d'une authentification pour récupérer ou envoyer des données de projet via l'API.

Il existe différentes façons d'obtenir votre **clé API**.

**Méthode 1 :**

1. Cliquez sur l'icône de votre profil en haut à droite.
2. Sélectionnez **Paramètres du compte**.
3. Accédez à l'onglet **Sécurité**.
4. Votre clé API est masquée par défaut. Cliquez sur **Afficher** pour la consulter.

![Afficher la clé API](images/api/key.png)

**Méthode 2 :**

Dans votre navigateur web, accédez à `https://[server-url]/token/?format=json`. Veillez à remplacer `[server-url]` par l'URL de votre serveur.

**Méthode 3 :**

Dans le terminal, utilisez la commande curl suivante :

`curl -u username:password "https:/[server-url]/token/?format=json"`

Veillez à remplacer `[server-url]` par l'URL de votre serveur.

<p class="note">
    <strong>Note :</strong> Si votre clé API est partagée, rendue publique ou compromise d'une quelconque façon, régénérez-la immédiatement. Votre clé API donne accès à toutes les données de votre compte. Pour la régénérer, accédez à <strong>Paramètres du compte > Sécurité</strong> et cliquez sur <strong>Regenerate key</strong>. Cette action révoquera tout accès via votre clé API existante et en générera une nouvelle aléatoire.
</p>

## Récupérer l'UID du projet

L'**UID du projet** est un code unique qui identifie un projet KoboToolbox spécifique et doit être inclus dans les appels API pour cibler ce projet.

Vous pouvez trouver l'**UID du projet** dans l'URL de la page de résumé de votre projet. Il s'agit de la chaîne de lettres et de chiffres qui apparaît après « forms/ » dans l'URL, comme suit : `https://[server-url]/#/forms/[project asset UID]/summary`.

![Récupérer l'UID du projet](images/api/project_UID.png)

## Exporter vos données via l'API

Il existe deux principales approches pour connecter vos données via l'API avec KoboToolbox :

- **Exports synchronisés :** Renvoie un fichier CSV ou XLSX prêt à l'emploi, basé sur des paramètres d'export prédéfinis, que des applications externes (par exemple, Power BI ou Excel) peuvent charger directement.
- **Endpoint JSON :** Envoie chaque soumission sous forme de fichier JSON brut. Cette approche est préférable pour les pipelines basés sur du code, et non pour une utilisation directe dans des tableurs ou des outils de tableau de bord.

Chaque approche nécessite de connaître l'URL du serveur et l'UID du projet pour construire une URL d'export personnalisée. Selon l'application, votre clé API peut être requise pour l'authentification.

<p class="note">
    Pour plus d'informations sur les exports synchronisés, consultez l'article <a href="https://support.kobotoolbox.org/fr/synchronous_exports.html">Utiliser l'API pour les exports synchronisées</a>.
<br><br>
Pour en savoir plus sur la connexion de vos données à Power BI afin de créer des tableaux de bord personnalisés, consultez l'article <a href="https://support.kobotoolbox.org/fr/pulling_data_into_powerbi.html">Connexion de KoboToolbox à Power BI</a>.
<br><br>
Pour en savoir plus sur la connexion de vos données à Microsoft Excel, consultez l'article <a href="https://support.kobotoolbox.org/fr/pulling_data_into_excelquery.html">Connexion de KoboToolbox à Microsoft Excel</a>.
</p>

## Documentation avancée

La documentation de l'API disponible à l'adresse `https://[server-url]/api/v2/docs/` propose une interface interactive pour les endpoints de l'API. Elle remplace les informations précédemment présentées dans chaque endpoint.

| **Serveur KoboToolbox**    | **Documentation de l'API**                     |
| :----------------- | :--------------------------------------------- |
| Le serveur KoboToolbox mondial               | [https://kf.kobotoolbox.org/api/v2/docs/](https://kf.kobotoolbox.org/api/v2/docs/)  |
| Le serveur KoboToolbox Union européenne       | [https://eu.kobotoolbox.org/api/v2/docs/](https://eu.kobotoolbox.org/api/v2/docs/)  |

Ces pages de documentation avancée répertorient tous les endpoints, indiquent les paramètres de requête autorisés, incluent une barre de recherche, affichent des exemples de réponses et d'erreurs, et permettent de tester directement les requêtes dans votre navigateur. Utilisez cette documentation pour vérifier l'authentification, découvrir les fonctionnalités disponibles et copier les URL exactes dans vos scripts personnalisés.

Vous pouvez également télécharger le schéma de la documentation de l'API au format YAML à l'adresse `https://[server-url]/api/v2/schema/` ou au format JSON à l'adresse `https://[server-url]/api/v2/schema/?format=json`.

<p class="note">
    <strong>Note :</strong> Les endpoints V1 sont désormais obsolètes, au profit de l'API KPI v2, plus robuste et entièrement disponible. Pour plus d'informations sur la migration vers KPI v2, consultez l'article <a href="https://support.kobotoolbox.org/fr/migrating_api.html">Migration de l'API v1 vers l'API v2</a>.
</p>

Pour plus d'exemples d'utilisation de l'API, consultez ce [post du Forum communautaire](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).