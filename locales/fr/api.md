# Premiers pas avec l'API
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/24c740499cf305ed0e9bece1dde237b9b23a05c0/source/api.md" class="reference">15 Sep 2025</a>

Une **interface de programmation d'application (API)** permet à deux composants logiciels de communiquer en utilisant un ensemble de définitions et de protocoles. Avec une API, un script ou une application peut fonctionner avec KoboToolbox sans utiliser l'interface web. Par exemple, vous pouvez générer automatiquement des exports de données qui se connectent à des sources externes comme des tableaux de bord ou des dossiers de sauvegarde.

Avec l'**API** KoboToolbox, vous pouvez :

- **Télécharger des données** automatiquement en JSON, CSV ou XLSX.
- **Générer des exports à la demande** pour des tableaux de bord, des sauvegardes ou des analyses.
- **Soumettre ou modifier des enregistrements** à partir d'autres outils de collecte de données.
- **Créer ou déployer des projets** et cloner des projets existants via du code.
- **Gérer les utilisatrices et utilisateurs**, les permissions et l'activité des projets à grande échelle.

L'utilisation de l'API KoboToolbox vous permet d'automatiser les tâches routinières, de maintenir les tableaux de bord à jour et d'intégrer KoboToolbox avec d'autres systèmes, tout en réduisant les étapes manuelles et les erreurs. Cet article fournit une introduction à l'API KoboToolbox et couvre les étapes suivantes :

- Récupérer votre **URL de serveur**
- Récupérer votre **clé API**
- Récupérer l'UID de l'actif du projet
- Exporter vos données en utilisant l'API

<p class="note">
    <strong>Note :</strong> Les points de terminaison V1 sont désormais obsolètes et leur déclassement est prévu pour janvier 2026, au profit de l'API KPI v2 plus robuste et entièrement prise en charge. Pour plus d'informations sur la migration vers KPI v2, consultez <a href="migrating_api.html">Migrer de l'API v1 vers v2</a>.
</p>

## Récupérer votre URL de serveur
L'**URL de serveur** est l'adresse web de base de votre serveur KoboToolbox. Elle est placée au début de chaque requête API.

Pour la plupart des utilisatrices et utilisateurs, l'URL de serveur est [kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (si vous utilisez Le serveur KoboToolbox mondial) ou [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (si vous utilisez Le serveur KoboToolbox Union européenne).

![Récupérer l'URL de serveur](images/api/server_URL.png)

## Récupérer votre clé API
Votre **clé API** est un jeton personnel qui agit comme un mot de passe, permettant à un logiciel d'accéder à votre compte via l'API. Elle peut être requise lorsqu'un script, un tableau de bord ou une application externe nécessite une authentification pour récupérer ou envoyer des données de projet via l'API.

Il existe différentes façons d'obtenir votre **clé API**.

**Méthode 1 :**

1. Cliquez sur l'icône de votre profil dans le coin supérieur droit.
2. Sélectionnez **PARAMÈTRES DU COMPTE**.
3. Allez dans l'onglet **Sécurité**.
4. Votre clé API est masquée par défaut. Cliquez sur **Afficher** pour la visualiser.

**Méthode 2 :**

Dans votre navigateur web, accédez à `https://[url-serveur]/token/?format=json`. Assurez-vous de remplacer `[url-serveur]` par votre URL de serveur.

**Méthode 3 :**

Dans le terminal, utilisez la commande curl suivante :

`curl -u nom_utilisateur:mot_de_passe "https://[url-serveur]/token/?format=json"`

Assurez-vous de remplacer `[url-serveur]` par votre URL de serveur.

## Récupérer l'UID de l'actif de votre projet

L'**UID de l'actif du projet** est un code unique qui identifie un projet KoboToolbox spécifique et doit être inclus dans les appels API pour cibler ce projet.

Vous pouvez trouver l'**UID de l'actif du projet** dans l'URL de la page de résumé de votre projet. Il s'agit de la chaîne de lettres et de chiffres qui apparaît après "forms/" dans l'URL, comme suit : `https://[url-serveur]/#/forms/[UID de l'actif du projet]/summary`.

![Récupérer l'UID de l'actif du projet](images/api/project_UID.png)

## Exporter vos données en utilisant l'API

Il existe deux approches principales pour connecter vos données en utilisant l'API avec KoboToolbox :

- **Exports synchrones :** Renvoie un fichier CSV ou XLSX prêt à l'emploi, basé sur des paramètres d'export prédéfinis, que les applications externes (par exemple, Power BI ou Excel) peuvent charger directement.
- **Point de terminaison JSON :** Envoie chaque enregistrement sous forme de fichier JSON brut. C'est la meilleure option pour les pipelines basés sur du code, pas pour une utilisation directe dans des outils de tableur ou de tableau de bord.

Chaque approche nécessite de connaître l'URL du serveur et l'UID de l'actif du projet pour construire une URL d'export personnalisée. Selon l'application, votre clé API peut être nécessaire pour l'authentification.

<p class="note">
    Pour plus d'informations sur les exports synchrones, consultez <a href="synchronous_exports.html">Utiliser l'API pour les exports synchrones</a>.
<br><br>
Pour en savoir plus sur la connexion de vos données à Power BI pour créer des tableaux de bord personnalisés, consultez <a href="pulling_data_into_powerbi.html">Connecter KoboToolbox à Power BI</a>.
<br><br>
Pour en savoir plus sur la connexion de vos données à Microsoft Excel, consultez <a href="pulling_data_into_excelquery.html">Connecter KoboToolbox à Microsoft Excel</a>.
</p>