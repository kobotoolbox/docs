# Options avancées pour l'export des données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/b0d195136b7fb3fe51b687cc03a5e8dcde946309/source/advanced_export.md" class="reference">22 Jun 2026</a>


Les options avancées offrent un contrôle et une flexibilité accrus lors du téléchargement et de l'export de vos données. Cet article vous guidera dans la personnalisation de vos exports de données, depuis la sélection des champs jusqu'à la gestion des différents types de questions, en passant par la définition de paramètres adaptés à vos besoins analytiques.

<p class="note">
    Pour en savoir plus sur le téléchargement de données, notamment un aperçu des types d'exports et des formats disponibles, consultez l'article <a href="https://support.kobotoolbox.org/fr/export_download.html?highlight=export">Exporter et télécharger vos données.</a>
</p>

## Options d'export pour les questions à choix multiple

L'option **Exporter les questions à choix multiple (Select Many) comme…** vous permet de choisir comment exporter les données des questions **Choix multiple** (également appelées `select_multiple`). Vous pouvez choisir de les exporter sous les formes suivantes :

| **Option d'export**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Colonnes uniques et distinctes &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Ce paramètre par défaut exporte une colonne contenant toutes les options sélectionnées pour les questions **Choix multiple**, ainsi que des colonnes individuelles pour chaque réponse, comme illustré ci-dessous.<br> ![How to select many columns](images/advanced_export/select_many_columns.png) |
| Colonnes distinctes  | Chaque réponse aux questions **Choix multiple** sera exportée dans des colonnes séparées.|
| Colonne unique   | Les réponses aux questions **Choix multiple** seront exportées dans une seule colonne.            |


<p class="note">
  <strong>Note :</strong> Dans les colonnes séparées, une valeur « 1 » indique que l'option a été sélectionnée, tandis que « 0 » signifie que le répondant n'a pas choisi cette option.
</p>

## Sélectionner les champs à exporter

Les options d'export avancées vous permettent d'affiner votre téléchargement de données en incluant les données de toutes les versions du formulaire ou en sélectionnant des questions spécifiques à exporter.

| **Paramètre d'export**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Inclure les champs des […] versions &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Par défaut, cette option est cochée. Elle vous permet de télécharger les données de toutes les versions du formulaire, y compris les questions ou choix supprimés. Si elle est décochée, seules les données de la dernière version déployée du formulaire seront téléchargées. |
| Sélectionner les questions à exporter | Pour exporter les données de questions spécifiques, activez cette option et sélectionnez les questions à inclure. |
| Plage de dates | Pour exporter les données soumises dans une plage de dates spécifique, activez cette option et sélectionnez les dates de **début** et/ou de **fin**. Les filtres de dates sont basés sur l'heure de soumission et utilisent le fuseau horaire UTC. Les soumissions effectuées aux dates de début et de fin sont incluses dans les exports. |

![How to select data fields](images/advanced_export/select_data_fields.png)

## Options de format de données supplémentaires

KoboToolbox propose des options de format de données supplémentaires pour personnaliser davantage vos exports, comme l'inclusion des noms de groupes dans les en-têtes, l'enregistrement des réponses de type date et nombre sous forme de texte, ou l'inclusion des URL des médias.

| **Paramètre d'export**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Inclure les groupes dans les en-têtes | Choisissez cette option pour ajouter les noms de groupes à chaque en-tête de question, comme illustré dans l'exemple ci-dessous. ![Include groups in headers](images/advanced_export/group_headers2.png) | 
| Enregistrer les réponses date et nombre sous forme de texte &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Par défaut, les questions **Date, Date et heure, Chiffre** et **Décimale** sont enregistrées avec leurs types de données correspondants lors de l'export au format XLS. Cochez cette option si vous préférez les exporter sous forme de texte.<br><br><strong>Note :</strong> Les formats d'heure d'Excel ne sont pas compatibles avec les données de fuseau horaire ; par conséquent, toute donnée de fuseau horaire présente dans la valeur de réponse sera supprimée lors de l'export. Pour conserver ces informations, cochez l'option permettant d'exporter les dates sous forme de valeurs texte. |
| Inclure les URL des médias | Si votre formulaire a collecté des médias (photos, audio, vidéos ou fichiers), cochez cette option pour vous assurer que votre fichier exporté inclut des liens vers ces fichiers médias. |

## Enregistrer les paramètres d'export

Vous pouvez enregistrer vos paramètres d'export définis pour une utilisation ultérieure ou pour générer un lien d'[export synchronisé](https://support.kobotoolbox.org/fr/synchronous_exports.html) pour des logiciels tels que Power BI ou Excel.

| **Paramètre d'export** | **Description**                                |
| :-------------------- | :------------------------------------ |
| Enregistrer la sélection sous… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Cochez cette option et saisissez un nom pour vos paramètres d'export. Lorsque vous cliquez sur **EXPORT**, ces paramètres seront enregistrés et le nom apparaîtra dans la zone **Appliquer les paramètres d'exportation enregistrés**. | 

Pour utiliser des paramètres d'export enregistrés, cliquez sur le menu déroulant sous **Appliquer les paramètres d'exportation enregistrés** et sélectionnez les paramètres d'export de votre choix.

## Résolution de problèmes

<details>
  <summary><strong>Des champs provenant de versions antérieures du formulaire sont absents de l'export</strong></summary>
  Si les données de questions renommées ou supprimées sont absentes des exports après la modification et le redéploiement d'un formulaire, assurez-vous que l'option <strong>Inclure les champs des versions déployées</strong> est sélectionnée lors du téléchargement des données. Si cette option n'est pas sélectionnée, seuls les champs de la version la plus récente du formulaire sont inclus. Toutes les soumissions sont toujours incluses dans le téléchargement — cette option affecte uniquement les champs inclus.
</details>

<br>

<details>
  <summary><strong>Les URL des médias provenant d'anciens exports ne fonctionnent plus</strong></summary>
Les utilisateurs qui s'appuient sur les URL des médias provenant d'anciens exports Excel ou CSV peuvent constater que ces liens ne fonctionnent plus depuis la <a href="https://support.kobotoolbox.org/fr/migrating_api.html">dépréciation de l'API v1</a>.
<br><br> 
Les URL concernées utilisent l'ancien format : 
<code>https://kc.kobotoolbox.org/media/original?media_file=...</code>
<br><br>
Pour résoudre ce problème, réexportez vos données en sélectionnant l'option <strong>Inclure les URL des médias</strong>. Le nouvel export inclura des URL de médias mises à jour.
</details>