# Sélectionner des options à partir d'un fichier externe avec XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_from_file_xls.md" class="reference">23 avr. 2026</a>

Les questions **Sélectionner à partir d'un fichier** vous permettent d'utiliser une liste de choix stockée dans un fichier externe plutôt que de la définir directement dans votre formulaire. Il en existe deux types : `select_one_from_file` pour sélectionner un **choix unique**, et `select_multiple_from_file` pour sélectionner **plusieurs choix**.

Utiliser un fichier séparé pour votre liste de choix facilite la gestion de longues listes, leur réutilisation dans plusieurs formulaires, et la mise à jour des options en cas de besoin. Les formats de fichiers disponibles sont CSV, XML et GeoJSON.

Cet article explique comment mettre en forme votre fichier externe, configurer votre XLSForm pour utiliser des questions **Sélectionner à partir d'un fichier**, et importer votre fichier externe dans KoboToolbox.

<p class="note">
<strong>Note :</strong> Cet article porte sur l'ajout de questions Sélectionner à partir d'un fichier dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de ce type de questions dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/external_file.html">Sélectionner des options à partir de fichiers externes dans le Formbuilder</a>.
<br><br>
Pour vous exercer avec les questions Sélectionner à partir d'un fichier dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Mettre en forme les listes de choix externes

Pour commencer, créez votre liste de choix dans un fichier externe séparé. La structure requise dépend du format choisi (CSV, XML ou GeoJSON). Utilisez un fichier distinct pour chaque liste de choix.

<p class="note">
Pour en savoir plus sur la mise en forme des fichiers XML ou GeoJSON, consultez la documentation <a href="https://xlsform.org/en/#multiple-choice-from-file">XLSForm</a> et <a href="https://docs.getodk.org/form-datasets/#building-selects-from-geojson-files">ODK</a>. Les fichiers GeoJSON sont principalement utilisés pour <a href="https://support.kobotoolbox.org/fr/select_from_map_xls.html">sélectionner des options à partir d'une carte</a>.
</p>

Pour les fichiers CSV, la structure est similaire à celle de l'onglet choices dans un XLSForm. Elle doit inclure les colonnes `name` et `label`, mais la colonne `list_name` n'est pas nécessaire.

**Fichier CSV externe**

| name    | label     |
|:--------|:----------|
| option1 | Option 1  |
| option2 | Option 2  |
| option3 | Option 3  |

Si votre fichier utilise des noms différents pour le nom et le libellé du choix, vous pouvez le préciser dans votre XLSForm (voir les instructions [ci-dessous](https://support.kobotoolbox.org/fr/select_from_file_xls.html#configuring-choice-name-and-label-columns)).

<p class="note">
<strong>Note :</strong> Utilisez des noms de fichiers courts et simples pour vos fichiers externes, sans espaces ni caractères spéciaux. Le nom du fichier sera utilisé dans votre XLSForm pour associer les questions à leurs listes de choix. Si vous utilisez plusieurs fichiers externes, assurez-vous que chacun porte un nom unique, même s'ils utilisent des types de fichiers différents.
</p>

## Configurer votre XLSForm

Pour ajouter une question Sélectionner à partir d'un fichier à votre XLSForm :
1. Dans la colonne `type` de l'onglet survey, saisissez le type de question Sélectionner à partir d'un fichier (`select_one_from_file` ou `select_multiple_from_file`).
2. Dans la même cellule, au lieu du `list_name` des choix, ajoutez un espace suivi du nom du fichier externe, extension comprise.
    - Par exemple : `select_one_from_file households.csv`

**onglet survey**

| type                     | name | label           |
|:-------------------------|:-----|:----------------|
| select_one_from_file households.csv | hh   | Select household |
| survey |

### Configurer les colonnes de nom et de libellé des choix

Si votre fichier externe utilise des noms de colonnes différents de `name` et `label` :
1. Ajoutez une colonne `parameters` à l'onglet survey.
2. Dans la ligne de la question Sélectionner à partir d'un fichier, spécifiez les noms personnalisés à l'aide des paramètres `value` et `label`.
    - `value` correspond au `name` du choix.
    - `label` correspond au `label` du choix.

**onglet survey**

| type                     | name | label            | parameters                   |
|:-------------------------|:-----|:-----------------|:-----------------------------|
| select_one_from_file households.csv | hh   | Select household | value=housenum label=housename |
| survey |

## Importer le fichier externe dans KoboToolbox

Lorsque vous importez votre XLSForm dans KoboToolbox, vous devez également importer le fichier externe contenant votre liste de choix :
1. Dans KoboToolbox, accédez à la page **PARAMÈTRES** du projet.
2. Dans l'onglet **Média**, importez le fichier externe. Vérifiez que le nom du fichier correspond exactement au nom indiqué dans le XLSForm.

Pour mettre à jour votre liste de choix, modifiez le fichier externe selon vos besoins, importez-le à nouveau dans KoboToolbox, puis redéployez votre formulaire.

![Importer un média](images/select_from_file_xls/upload_media.png)

<p class="note">
Pour en savoir plus sur l'importation de fichiers multimédias, consultez l'article <a href="https://support.kobotoolbox.org/fr/upload_media.html">Importer des fichiers multimédias dans un projet</a>.
</p>

## Résolution de problèmes

<details>
  <summary><strong>Listes de choix traduites</strong></summary>
  Les questions Sélectionner à partir d'un fichier ne permettent pas encore d'utiliser les <a href="https://support.kobotoolbox.org/fr/language_xls.html">listes de choix traduites</a>. Votre fichier de choix externe ne peut contenir qu'une seule colonne <code>label</code>. Toute colonne <code>label</code> traduite supplémentaire sera ignorée dans les formulaires web ou provoquera une erreur dans KoboCollect. Pour les formulaires incluant des traductions, utilisez des listes de choix internes, ou configurez plusieurs questions <strong>Sélectionner à partir d'un fichier</strong> avec une logique de saut afin d'utiliser différents fichiers selon la langue du formulaire.
</details>

<br>

<details>
  <summary><strong>Fichier CSV introuvable</strong></summary>
  Si un message d'erreur indique que le fichier CSV est introuvable lors de l'ouverture de votre formulaire, vérifiez que le fichier commence bien par les colonnes <code>name</code> et <code>label</code>. Si les colonnes portent des noms différents, assurez-vous que la colonne <code>parameters</code> contient bien les paramètres <code>value</code> et <code>label</code>.
</details>