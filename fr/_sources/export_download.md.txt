# Exporter et télécharger vos données
<a href="../export_download.html">Read in English</a> | <a href="../es/export_download.html">Leer en español</a> | <a href="../ar/export_download.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/8a772b24abadb4e8d54f9716b798c5479432f0e6/source/export_download.md" class="reference">6 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/bXzwvvnhj7U" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Lorsque vous utilisez KoboToolbox, vous pouvez télécharger vos données collectées dans différents formats et personnaliser vos paramètres d'export. Cet article explique comment télécharger vos données collectées, y compris un aperçu des types d'export et des formats disponibles.

## Télécharger vos données

Pour télécharger vos données :

1. Ouvrez votre projet et accédez à **DONNÉES > Téléchargements**.
2. Choisissez vos paramètres d'export (détaillés ci-dessous).
3. Cliquez sur **EXPORTER**. Cela générera un export qui sera affiché dans un tableau sous les paramètres d'export.
4. Cliquez sur **TÉLÉCHARGER** pour télécharger le fichier exporté.

![Exporting data example](images/export_download/export.png)

<p class="note">
    <strong>Remarque :</strong> Un export peut prendre de quelques secondes à plusieurs minutes à générer, selon le nombre de soumissions, la taille du formulaire et la charge du serveur. Une fois créé, il apparaîtra dans la section <strong>Exports</strong> de la page.
</p>

## Types d'export

Vous pouvez choisir parmi les types d'export suivants :

| **Type d'export**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| XLS               | Fichier Microsoft Excel (format .xlsx). Ce type de fichier est recommandé lors de la collecte de données de groupes répétés.                                  |
| CSV      | Fichier de valeurs séparées par des virgules. Ce type de fichier est idéal pour importer dans la plupart des logiciels de gestion de données, y compris les bases de données.                                  |
| GeoJSON           | Il s'agit d'un format d'échange de données géospatiales ouvert standard, idéal pour l'intégration avec des logiciels SIG comme ArcGIS.            |
| SPSS Labels           | Génère un fichier de syntaxe SPSS qui applique des étiquettes de questions et des étiquettes de valeurs aux variables des données KoboToolbox importées dans SPSS. Pour plus d'informations, consultez <a href="converting_to_spss_and_stata.html">Convertir les données en SPSS et/ou Stata</a>.         |
| GPS Coordinates (KML)               | Génère un fichier KML pour travailler avec vos données dans un logiciel SIG, tel que Google Earth.                               |
| Media Attachments (ZIP)               |  Télécharge un fichier ZIP contenant tous les médias collectés via le formulaire.                               |
| XLS (legacy)              | Génère un fichier .xlsx (Microsoft Excel) en utilisant une ancienne interface KoboToolbox. N'utilisez cette option qu'en cas de problèmes occasionnels avec les exports XLS et CSV standard, car elle sera supprimée dans une future mise à jour.                                  |
| CSV (legacy)               | Génère un fichier CSV en utilisant une ancienne interface KoboToolbox. N'utilisez cette option qu'en cas de problèmes occasionnels avec les exports XLS et CSV standard, car elle sera supprimée dans une future mise à jour.                                  |

## Format des valeurs et des en-têtes

Lorsque vous utilisez les formats d'export standard (XLS, CSV, GeoJSON et SPSS Labels), vous pouvez sélectionner le format de vos valeurs de données et de vos en-têtes :

| **Format**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Labels (default)               | Le fichier exporté utilise les <strong>étiquettes de questions</strong> (texte de la question) comme en-têtes de colonnes et les <strong>étiquettes de choix</strong> pour les réponses aux questions Sélectionner un ou Sélectionner plusieurs.                                  |
| XML values and headers      | Le fichier exporté utilise les <strong>noms de questions</strong> (Noms de colonnes de données) comme en-têtes de colonnes et les <strong>noms de choix</strong> (valeurs XML) pour les réponses. Ce paramètre d'export est recommandé pour importer vos données dans un logiciel d'analyse de données.                                  |
| Labels in any of the defined languages           | Le fichier exporté utilise les <strong>étiquettes de questions et de choix</strong> dans l'une des langues définies dans le formulaire.            |

## Options avancées

En plus de personnaliser les formats de valeurs et d'en-têtes, les formats d'export non hérités offrent également d'autres options de personnalisation dans la section **Options avancées**. Pour plus d'informations sur les options avancées, consultez [Options avancées pour l'export de données](advanced_export.md).

## Dépannage

<details>
    <summary><strong>Exports bloqués en état d'attente ou échoués</strong></summary>
    
Le temps d'export dépend du nombre de soumissions, de la complexité du formulaire et de la charge actuelle du serveur. Si les exports restent en état d'attente pendant une période prolongée :
- Supprimez les exports bloqués en cliquant sur l'<i class="k-icon-trash"></i> <strong>icône de corbeille.</strong>
- Réessayez l'export en cliquant à nouveau sur le bouton <strong>EXPORTER</strong>.
- Évitez de créer plusieurs exports rapidement, car cela peut surcharger le serveur et réduire les performances pour toutes les utilisatrices et tous les utilisateurs.

<p class="note">
    <strong>Remarque :</strong> Les exports expireront et s'afficheront comme <strong>échoués</strong> après 30 minutes. Cette limite au niveau du serveur peut vous obliger à filtrer le nombre de soumissions incluses dans l'export pour terminer dans le délai imparti. Un exemple de la façon de procéder est discuté dans le <a href="https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4">Forum communautaire</a>.
</p>

Si vous continuez à rencontrer des problèmes lors de l'export de vos données, veuillez publier sur le <a href="https://community.kobotoolbox.org/">Forum communautaire</a>.
</details>

<br>

<details>
    <summary><strong>Données de groupe répété introuvables</strong></summary>
Seul le <b>format XLS</b> prend en charge les données de groupe répété. Chaque groupe répété sera exporté <strong>sous forme de feuille séparée</strong> dans le fichier exporté. Les téléchargements CSV ne fourniront que les données principales, sans les données de groupe répété. 
<br><br>
Pour plus d'informations sur l'export et l'utilisation des données de groupe répété, consultez <a href="managing_repeat_groups.html">Gérer les données de groupe répété</a>.    
</details>

<br>

<details>
    <summary><strong>Certaines données ne sont pas exportées</strong></summary>
    Si certaines de vos données ne sont pas exportées, vérifiez les <a href="advanced_export.html">options avancées</a>. Par exemple, assurez-vous que les données de toutes les versions de votre formulaire sont sélectionnées pour l'export.
</details>

<br>

<details>
    <summary><strong>Téléchargement de données de différentes versions</strong></summary>
    Lors du téléchargement de données incluant plusieurs versions de formulaire, vous pouvez rencontrer des changements dans le format de vos fichiers de données. 
</details>

<br>

<details>
    <summary><strong>Données de fuseau horaire perdues lors de l'export</strong></summary>
    Les formats horaires Excel ne prennent pas en charge les données de fuseau horaire. Par conséquent, toutes les données de fuseau horaire dans la valeur de réponse seront supprimées lors de l'export XLS. Pour conserver ces informations, cochez l'option d'export des dates sous forme de valeurs textuelles. 
<br><br>
Pour plus d'informations sur ce paramètre, consultez <a href="advanced_export.html">Options avancées pour l'export de données</a>.
</details>