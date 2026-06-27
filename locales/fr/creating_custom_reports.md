# Visualiser vos données à l'aide de rapports personnalisés
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6e9f496956ced232adb4985272fbee0a6465318d/source/creating_custom_reports.md" class="reference">15 Jun 2026</a>

KoboToolbox inclut un outil de création de rapports que vous pouvez utiliser pour suivre les données entrantes et consulter des statistiques descriptives simples. Les rapports vous permettent d'afficher des graphiques, de consulter le nombre de réponses, de comparer les réponses par sous-groupe, et de partager ou d'imprimer un résumé des questions sélectionnées dans votre formulaire.

<p class="note">
<strong>Note :</strong>
    Les rapports vous permettent de consulter vos données en un coup d'œil, mais ils ne remplacent pas le nettoyage, le traitement, l'analyse ou la visualisation approfondie des données avec des outils externes. Pour une analyse plus approfondie, KoboToolbox vous permet facilement d'<a href="../fr/export_download.html">exporter vos données</a> ou de les connecter à des <a href="../fr/synchronous_exports.html">outils externes via l'API</a>.
</p>

Cet article explique comment accéder aux rapports dans KoboToolbox, personnaliser les styles de rapport, créer des rapports personnalisés et gérer les droits d'accès aux rapports.

## Accéder aux rapports

Pour accéder aux rapports de votre projet :

1. Ouvrez votre projet.
2. Accédez à **DONNÉES.**
3. Cliquez sur <i class="k-icon-reports"></i> **Rapports.**

Le rapport par défaut inclut toutes les questions de votre formulaire. Chaque question est affichée avec un graphique et un tableau de données par défaut. Le rapport indique également le **type de question** et le **nombre de soumissions** ayant une réponse à cette question.

![Rapports de données](images/creating_custom_reports/reports.png)

Vous pouvez imprimer le rapport ou l'enregistrer en PDF en cliquant sur le bouton <i class="k-icon-print"></i> **Imprimer** en haut à droite. Vous pouvez également <i class=" k-icon-expand"></i> **basculer en plein écran** pour afficher le rapport sur toute la largeur de l'écran.

## Personnaliser votre rapport

Vous pouvez personnaliser le style et la configuration de votre rapport en cliquant sur <i class="k-icon-settings"></i> **Configurer le style du rapport.** Les modifications apportées s'appliqueront à tous les graphiques et tableaux après avoir cliqué sur **Sauvegarder.**

![Configurer le style du rapport](images/creating_custom_reports/configure.png)

Les paramètres suivants sont disponibles :

| Paramètre | Description |
|:---|:---|
| Type du graphique | Le type de graphique par défaut est un graphique à barres verticales. Vous pouvez sélectionner un autre type de graphique à appliquer à tous les graphiques du rapport. |
| Couleurs | Vous pouvez choisir une palette de couleurs différente pour tous les graphiques du rapport. |
| Grouper par | Vous pouvez sélectionner une question de type **Choix unique** de votre formulaire pour regrouper les graphiques et les tableaux selon cette variable. Cela peut être utile pour des comparaisons simples entre sous-groupes. |
| Traduction | Si votre formulaire comporte plusieurs langues, vous pouvez choisir la langue à afficher dans le rapport. |


## Personnaliser des questions individuelles

Vous pouvez également personnaliser des graphiques individuels dans le rapport.

Pour personnaliser un graphique :

1. Trouvez le graphique que vous souhaitez modifier.
2. Cliquez sur <i class="k-icon-more"></i> **Remplacer le style de graphique** en haut à droite du graphique.
3. Sélectionnez un type de graphique ou une palette de couleurs.

![Remplacer le style de graphique pour personnaliser le graphique](images/creating_custom_reports/override.png)

Ces paramètres s'appliquent uniquement au graphique sélectionné.

## Créer un rapport personnalisé

En plus du rapport par défaut, vous pouvez créer des rapports personnalisés. Les rapports personnalisés vous permettent de choisir les questions à inclure et d'enregistrer des paramètres de rapport personnalisés.

Pour créer un rapport personnalisé :

1. Cliquez sur <i class="k-icon-plus"></i> **Créer un nouveau rapport** à côté de **Rapport par défaut.**
2. Saisissez un titre pour votre rapport personnalisé.
3. Sélectionnez les questions que vous souhaitez inclure et cliquez sur **Sauvegarder.**
4. Cliquez sur <i class="k-icon-settings"></i> **Configurer le style du rapport** pour définir le style et la configuration du rapport.

![Créer un rapport personnalisé](images/creating_custom_reports/new.png)

Pour modifier le titre ou les questions affichées dans un rapport personnalisé, cliquez sur <i class="k-icon-edit"></i> **Modification des questions du rapport.**

<p class="note">
<strong>Note :</strong> Les paramètres des rapports personnalisés sont enregistrés et resteront disponibles lorsque vous quitterez la page et y reviendrez.
</p>

## Droits d'accès et partage

Les utilisateurs disposant de la permission **Afficher les soumissions** peuvent consulter les rapports, y compris les rapports personnalisés créés par d'autres utilisateurs. Ils ne peuvent cependant pas configurer les styles de rapport ni créer de rapports personnalisés.

Les utilisateurs disposant de la permission **Gérer le projet** peuvent consulter les rapports, configurer les styles de rapport et créer des rapports personnalisés.

<p class="note">
  Pour en savoir plus sur les droits d'accès et le partage, consultez l'article <a class="reference external" href="../fr/managing_permissions.html">Droits d'accès au niveau de l'utilisateur</a>.
</p>