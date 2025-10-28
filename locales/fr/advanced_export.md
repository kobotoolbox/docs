# Options avancées pour l'exportation des données
<a href="../advanced_export.html">Read in English</a> | <a href="../es/advanced_export.html">Leer en español</a> | <a href="../ar/advanced_export.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/9bc8dc162b89d329fd6161bbe168dd554df770a9/source/advanced_export.md" class="reference">6 Sep 2025</a>

Les options avancées offrent un meilleur contrôle et une plus grande flexibilité lors du téléchargement et de l'exportation de vos données. Cet article vous guidera dans la personnalisation de vos exportations de données, de la sélection des champs de données et de la gestion de divers types de questions à la définition de paramètres pour différents besoins analytiques.

<p class="note">
    Pour en savoir plus sur le téléchargement de données, y compris un aperçu des types d'exportation et des formats disponibles, consultez <a href="https://support.kobotoolbox.org/export_download.html?highlight=export">Exporter et télécharger vos données.</a>
</p>

## Options d'exportation pour les questions à choix multiples

L'option **Exporter les questions à choix multiples sous forme de…** vous permet de choisir comment exporter les données des questions **Choix multiples** (également appelées `select_multiple`). Vous pouvez choisir de les exporter sous forme de :

| **Option d'exportation**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Colonnes uniques et séparées &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Ce paramètre par défaut exporte une colonne avec toutes les options sélectionnées des questions <strong>Choix multiples</strong>, plus des colonnes individuelles pour chaque réponse, comme indiqué ci-dessous.<br> ![How to select many columns](images/advanced_export/select_many_columns.png) |
| Colonnes séparées  | Chaque réponse aux questions <strong>Choix multiples</strong> sera exportée dans des colonnes séparées.|
| Colonne unique   | Les réponses aux questions <strong>Choix multiples</strong> seront exportées dans une seule colonne.            |


<p class="note">
  <strong>Remarque :</strong> Dans les colonnes séparées, une valeur de « 1 » indique que l'option a été sélectionnée, tandis que « 0 » signifie que la personne interrogée n'a pas choisi cette option.
</p>

## Sélection des champs de données pour l'exportation

Les options d'exportation avancées vous permettent d'affiner votre téléchargement de données en incluant les données de toutes les versions du formulaire ou en sélectionnant des questions spécifiques à exporter.

| **Paramètre d'exportation**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Inclure les données de toutes les […] versions &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Par défaut, cette option est cochée. Cela vous permet de télécharger les données de toutes les versions du formulaire, y compris les questions ou choix supprimés. Si elle n'est pas cochée, seules les données de la dernière version du formulaire déployée seront téléchargées. |
| Sélectionner les questions à exporter | Pour exporter les données de questions spécifiques, activez cette option et sélectionnez les questions à inclure. |
| Plage de données | Pour exporter les données soumises dans une plage de dates spécifique, activez cette option et sélectionnez les dates de début et/ou de fin. Les filtres de date sont basés sur l'heure de soumission et utilisent le fuseau horaire UTC. Les données soumises aux dates de <strong>début</strong> et de <strong>fin</strong> sont incluses dans les exportations. |

![How to select data fields](images/advanced_export/select_data_fields.png)

## Options supplémentaires de format de données

KoboToolbox offre des options supplémentaires de format de données pour personnaliser davantage vos exportations, telles que l'inclusion des noms de groupes dans les en-têtes, le stockage des réponses de date et de nombre sous forme de texte, ou l'inclusion des URL de médias.

| **Paramètre d'exportation**    | **Description**                                |
| :----------------- | :------------------------------------ |
| Inclure les groupes dans les en-têtes | Choisissez cette option pour ajouter les noms de groupes à chaque en-tête de question, comme indiqué dans l'exemple ci-dessous. ![Include groups in headers](images/advanced_export/group_headers2.png) | 
| Stocker les réponses de date et de nombre sous forme de texte &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Par défaut, les questions <strong>Date, Date et heure, Nombre,</strong> et <strong>Décimal</strong> sont enregistrées avec leurs types de données correspondants lors de l'exportation vers XLS. Cochez cette option si vous préférez les exporter sous forme de texte.<br><br><strong>Remarque :</strong> Les formats d'heure Excel ne prennent pas en charge les données de fuseau horaire ; par conséquent, toutes les données de fuseau horaire dans la valeur de réponse seront supprimées lors de l'exportation. Pour conserver ces informations, cochez l'option pour exporter les dates sous forme de valeurs textuelles. |
| Inclure les URL de médias | Si votre formulaire a collecté des médias (photos, audio, vidéos ou fichiers), cochez cette option pour vous assurer que votre fichier exporté inclut des liens vers ces fichiers multimédias. |

## Enregistrement des paramètres d'exportation

Vous pouvez enregistrer vos paramètres d'exportation définis pour une utilisation future ou pour générer un lien d'[exportation synchrone](https://support.kobotoolbox.org/synchronous_exports.html) pour des logiciels comme PowerBI ou Excel.

| **Paramètre d'exportation** | **Description**                                |
| :-------------------- | :------------------------------------ |
| Enregistrer la sélection sous… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Cochez cette option et saisissez un nom pour vos paramètres d'exportation. Lorsque vous cliquez sur <strong>EXPORTER</strong>, ces paramètres seront enregistrés et le nom apparaîtra dans la zone <strong>Appliquer les paramètres d'exportation enregistrés</strong>. | 

Pour utiliser les paramètres d'exportation enregistrés, cliquez sur le menu déroulant sous **Appliquer les paramètres d'exportation enregistrés** et sélectionnez les paramètres d'exportation nommés de votre choix.