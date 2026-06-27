# Exporter et télécharger vos données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/43efdbb222e3213fa548509bb34819c5238f7e83/source/export_download.md" class="reference">6 mai 2026</a>


<iframe src="https://www.youtube.com/embed/bXzwvvnhj7U?cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Avec KoboToolbox, vous pouvez télécharger vos données collectées dans différents formats et personnaliser vos paramètres d'exportation. Cet article explique comment télécharger vos données collectées, avec une présentation des types d'export et des formats disponibles.

## Télécharger vos données

Pour télécharger vos données :

1. Ouvrez votre projet et accédez à **DONNÉES > Téléchargements**.
2. Choisissez vos paramètres d'exportation (décrits ci-dessous).
3. Cliquez sur **EXPORTER**. Un export sera généré et affiché dans un tableau sous les paramètres d'exportation.
4. Cliquez sur **TÉLÉCHARGER** pour télécharger le fichier exporté.

![Exemple d'exportation de données](images/export_download/export.png)

<p class="note">
    <strong>Note :</strong> La génération d'un export peut prendre de quelques secondes à plusieurs minutes, selon le nombre de soumissions, la taille du formulaire et la charge du serveur. Une fois créé, il apparaîtra dans la section <strong>Exports</strong> de la page.
</p>

## Types d'export

Vous pouvez choisir parmi les types d'export suivants :

| **Type d'export**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| XLS               | Fichier Microsoft Excel (format .xlsx). Ce format est recommandé pour l'exportation de données de groupes répétés.                                  |
| CSV      | Fichier de valeurs séparées par des virgules. Ce format est idéal pour l'importation dans la plupart des logiciels de gestion de données, y compris les bases de données.                                  |
| GeoJSON           | Format ouvert standard d'échange de données géospatiales, particulièrement adapté à l'intégration avec des logiciels SIG tels qu'ArcGIS. Ce format est recommandé pour <a href="https://support.kobotoolbox.org/fr/mapping_gps.html#exporting-as-geojson">l'analyse de données GPS</a>.            |
| SPSS Labels           | Génère un <a href="https://support.kobotoolbox.org/fr/converting_to_spss_and_stata.html">fichier de syntaxe SPSS</a> qui applique les libellés de questions et les libellés de valeurs aux variables des données KoboToolbox importées dans SPSS.         |
| GPS Coordinates (KML)               | Génère un <a href="https://support.kobotoolbox.org/fr/mapping_gps.html#exporting-as-kml">fichier KML</a> pour utiliser vos données dans des logiciels SIG tels que Google Earth. Ce format d'export ne sera plus disponible à l'avenir. Nous recommandons d'utiliser l'un des autres types d'export disponibles. |
| Media Attachments (ZIP)               | Télécharge un fichier ZIP contenant tous les <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#downloading-media-files">fichiers média</a> collectés via le formulaire.                               |
| XLS (legacy)              | Génère un fichier .xlsx (Microsoft Excel) via une interface KoboToolbox ancienne version. N'utilisez cette option qu'en cas de problèmes occasionnels avec les exports XLS et CSV standard, car elle sera supprimée dans une prochaine mise à jour.                                  |
| CSV (legacy)               | Génère un fichier CSV via une interface KoboToolbox ancienne version. N'utilisez cette option qu'en cas de problèmes occasionnels avec les exports XLS et CSV standard, car elle sera supprimée dans une prochaine mise à jour.                                  |

<p class="note">
    Pour en savoir plus sur les types d'export, consultez les articles <a href="https://support.kobotoolbox.org/fr/mapping_gps.html#exporting-gps-data">Cartographier vos données GPS</a> et <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#downloading-media-files">Gérer les réponses média soumises par les répondants</a>.
</p>

## Format pour les valeurs et l'en-tête

Lorsque vous utilisez les formats d'export standard (XLS, CSV, GeoJSON et SPSS Labels), vous pouvez sélectionner le format des valeurs et des en-têtes de vos données :

| **Format**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Labels (default)               | Le fichier exporté utilise les <strong>libellés de questions</strong> (texte de la question) comme en-têtes de colonnes et les <strong>libellés de choix</strong> pour les réponses aux questions de type Choix unique et Choix multiple.                                  |
| XML values and headers      | Le fichier exporté utilise les <strong>noms des questions</strong> (noms des champs) comme en-têtes de colonnes et les <strong>noms des choix</strong> (valeurs XML) pour les réponses. Ce paramètre d'exportation est recommandé pour l'importation de vos données dans des logiciels d'analyse de données.                                  |
| Labels in any of the defined languages           | Le fichier exporté utilise les <strong>libellés de questions et de choix</strong> dans l'une des langues définies dans le formulaire.            |

## Options avancées

En plus de la personnalisation des formats de valeurs et d'en-têtes, les formats d'export non-legacy proposent également d'autres options de personnalisation dans la section **Options avancées**. Pour plus d'informations sur les options avancées, consultez l'article [Options avancées pour l'export des données](https://support.kobotoolbox.org/fr/advanced_export.html).

## Résolution de problèmes

<details>
    <summary><strong>Exporter des données GPS</strong></summary>
Plusieurs options sont disponibles pour <a href="https://support.kobotoolbox.org/fr/mapping_gps.html#exporting-gps-data">télécharger des données GPS</a>. Lorsque vous exportez vos données au format CSV ou XLS, les coordonnées apparaissent dans plusieurs colonnes : une colonne avec l'ensemble complet des coordonnées, et des colonnes supplémentaires pour la latitude, la longitude, l'altitude et la précision. Pour préparer vos données en vue d'une utilisation dans un logiciel SIG tel qu'ArcGIS, utilisez l'option d'export GeoJSON. Le format d'export KML est limité et ne sera plus disponible à l'avenir.
</details>

<br>

<details>
    <summary><strong>Exports bloqués en attente ou en échec</strong></summary>
    
La durée d'un export dépend du nombre de soumissions, de la complexité du formulaire et de la charge actuelle du serveur. Si des exports restent en attente pendant une période prolongée :
- Supprimez les exports bloqués en cliquant sur l'icône <i class="k-icon-trash"></i> <strong>corbeille.</strong>
- Relancez l'export en cliquant à nouveau sur le bouton **EXPORTER**.
- Évitez de créer plusieurs exports rapidement, car cela peut surcharger le serveur et réduire les performances pour tous les utilisateurs.

<p class="note">
    <strong>Note :</strong> Les exports expirent et s'affichent comme <strong>en échec</strong> après 30 minutes. Cette limite au niveau du serveur peut nécessiter de filtrer le nombre de soumissions incluses dans l'export afin de terminer dans le délai imparti. Un exemple de procédure est présenté dans le <a href="https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4">Forum communautaire</a>.
</p>

Si vous continuez à rencontrer des problèmes lors de l'exportation de vos données, publiez un message dans le <a href="https://community.kobotoolbox.org/">Forum communautaire</a>.
</details>

<br>

<details>
    <summary><strong>Données de groupes répétés introuvables</strong></summary>
Seul le <b>format XLS</b> permet d'exporter les données de groupes répétés. Chaque groupe répété sera exporté <strong>dans un onglet distinct</strong> du fichier exporté. Les téléchargements CSV ne fournissent que les données principales, sans les données de groupes répétés.
<br><br>
Pour plus d'informations sur l'exportation et l'utilisation des données de groupes répétés, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_repeat_groups.html">Gestion des données de groupes répétés</a>.
</details>

<br>

<details>
    <summary><strong>Certaines données ne sont pas exportées</strong></summary>
    Si certaines de vos données ne sont pas exportées, vérifiez les <a href="https://support.kobotoolbox.org/fr/advanced_export.html">options avancées</a>. Par exemple, assurez-vous que toutes les versions du formulaire sont sélectionnées pour l'export et que toutes les questions que vous souhaitez inclure ont bien été sélectionnées.
</details>

<br>

<details>
<summary><strong>Télécharger des données provenant de différentes versions</strong></summary>
    Lorsque vous téléchargez des données incluant plusieurs versions d'un formulaire, vous pouvez constater des modifications dans le format de vos fichiers de données.
    <br><br>
Pour plus d'informations sur les modifications attendues de la structure des données lors de l'utilisation de différentes versions d'un formulaire, consultez l'article <a href="https://support.kobotoolbox.org/fr/deploy_form_new_project.html#important-considerations-when-redeploying-a-form">Déployer vos formulaires pour la collecte de données</a>.
</details>

<br>

<details>
    <summary><strong>Perte des données de fuseau horaire lors de l'export</strong></summary>
    Les formats de date d'Excel ne prennent pas en charge les données de fuseau horaire. Par conséquent, toute information de fuseau horaire contenue dans la valeur de réponse sera supprimée lors de l'export XLS. Pour conserver ces informations, cochez l'option permettant d'exporter les dates sous forme de valeurs texte.
<br><br>
Pour plus d'informations sur ce paramètre, consultez l'article <a href="https://support.kobotoolbox.org/fr/advanced_export.html">Options avancées pour l'export des données</a>.
</details>

<br>

<details>
    <summary><strong>Colonnes supplémentaires ajoutées à l'export de données</strong></summary>
     Votre export de données peut inclure des colonnes supplémentaires qui n'ont pas été ajoutées en tant que questions dans votre formulaire. KoboToolbox inclut des <a href="https://support.kobotoolbox.org/fr/viewing_validating_data.html#system-generated-submission-fields">champs générés automatiquement</a> pour chaque soumission, tels que <code>_id</code>, <code>_uuid</code>, <code>_submission_time</code>, <code>_submitted_by</code> et <code>rootUuid</code>.
<br><br>
En plus des champs générés automatiquement affichés dans le tableau de données, certains champs supplémentaires peuvent être ajoutés lors de l'export de vos données.
<br><br>

<ul>
    <li><code>_validation_status</code> : indique le <a href="https://support.kobotoolbox.org/fr/viewing_validating_data.html#validating-your-data">statut de validation</a> de la soumission. Ce champ permet de suivre si une soumission a été examinée et si elle est prête à être utilisée. Les valeurs possibles sont <strong>Approuvé</strong>, <strong>Non approuvé</strong> et <strong>En attente</strong>.</li>
    <li><code>_index</code> : numéro de ligne séquentiel généré au moment de l'export. Il est principalement utilisé pour relier les lignes entre l'onglet principal et les onglets de groupes répétés dans les exports multi-onglets. Étant donné qu'il est créé lors de l'export, il ne doit pas être utilisé comme identifiant stable d'une soumission.
</li>
    <li><code>_status</code> : indique comment la soumission a été envoyée. Dans de nombreux exports, ce champ n'est pas très utile car il peut contenir la même valeur pour tous les enregistrements.
    </li>
    <li>Vous pouvez également voir <code>_notes</code> et <code>_tags</code> dans certains exports. Ces champs sont obsolètes mais peuvent encore apparaître dans des workflows d'export anciens ou existants.
    </li>
</ul>

Si vous n'avez pas besoin de ces colonnes pour votre analyse, vous pouvez les supprimer du fichier exporté après le téléchargement ou lors de la configuration des <a href="https://support.kobotoolbox.org/fr/advanced_export.html#selecting-data-fields-for-export">paramètres d'exportation</a>.
</details>