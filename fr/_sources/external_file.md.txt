# Sélectionner des options à partir de fichiers externes dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/a476e76f62e857ee7dd45ee394421eb4bf7dd22a/source/external_file.md" class="reference">21 Mar 2026</a>

Les questions **Choix unique à partir d'un fichier** et **Choix multiple à partir d'un fichier** vous permettent d'utiliser une liste de choix de réponse stockée dans un fichier externe plutôt que de la définir directement dans votre formulaire. Il en existe deux types :
* **Choix unique à partir d'un fichier** pour sélectionner un seul choix
* **Choix multiple à partir d'un fichier** pour sélectionner plusieurs choix

L'utilisation d'un fichier externe pour votre liste de choix facilite la gestion de longues listes dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**. Les formats de fichiers disponibles sont CSV, XML et GeoJSON.

Cet article explique comment formater votre fichier externe, l'importer dans KoboToolbox et configurer des questions **Choix à partir d'un fichier** dans le Formbuilder.

## Formater les listes de choix externes

Pour commencer, créez votre liste de choix dans un fichier externe séparé. La structure requise de ce fichier dépend du format choisi (CSV, XML ou GeoJSON). Utilisez un fichier distinct pour chaque liste de choix.

<p class="note">
Pour en savoir plus sur le formatage des fichiers XML ou GeoJSON, consultez la documentation <a href="https://xlsform.org/en/#multiple-choice-from-file">XLSForm</a> et <a href="https://docs.getodk.org/form-datasets/#building-selects-from-geojson-files">ODK</a>. Les fichiers GeoJSON sont principalement utilisés pour <a href="https://support.kobotoolbox.org/fr/select_from_map_xls.html">sélectionner des options à partir d'une carte</a>.
</p>

Si vous utilisez un fichier CSV pour vos choix de réponse, il doit contenir au minimum deux colonnes : `name` et `label`.
* La colonne `name` représente la [valeur XML](https://support.kobotoolbox.org/fr/question_types.html#setting-xml-values-for-option-choices) de votre choix de réponse.
* La colonne `label` représente le libellé du choix tel qu'il s'affiche dans votre formulaire.

**Fichier CSV externe**

| name    | label    |
|:--------|:---------|
| option1 | Option 1 |
| option2 | Option 2 |
| option3 | Option 3 |

Si votre fichier utilise des noms différents pour le nom et le libellé du choix, vous pouvez [le préciser](https://support.kobotoolbox.org/fr/select_from_file_xls.html#configuring-choice-name-and-label-columns) en [téléchargeant votre formulaire en tant que XLSForm](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) et en ajoutant une colonne `parameters`.

<p class="note">
<strong>Note :</strong> Utilisez des noms de fichiers courts et simples pour vos fichiers externes, en évitant les espaces et les caractères spéciaux. Le nom du fichier sera utilisé pour associer les questions à leurs listes de choix. Si vous utilisez plusieurs fichiers externes, assurez-vous que chacun porte un nom unique, même s'ils utilisent des types de fichiers différents.
</p>

## Importer le fichier externe dans KoboToolbox

Avant de créer une question **Choix à partir d'un fichier** dans le Formbuilder, vous devez importer le fichier externe contenant votre liste de choix :

1. Dans KoboToolbox, accédez à la page **PARAMÈTRES** du projet.
2. Dans l'onglet **Média**, importez le fichier externe. Vérifiez que le nom du fichier correspond exactement au nom de fichier indiqué dans le XLSForm.

Pour mettre à jour votre liste de choix, modifiez le fichier externe selon vos besoins, importez-le à nouveau dans KoboToolbox, puis redéployez votre formulaire.

![Importer un média](images/external_file/upload_media.png)

<p class="note">
  Pour en savoir plus sur l'importation de fichiers multimédias, consultez l'article <a href="https://support.kobotoolbox.org/fr/upload_media.html">Importer des fichiers multimédias dans un projet</a>.
</p>

## Configurer la question dans le Formbuilder

Après avoir importé votre fichier CSV externe dans KoboToolbox, vous pouvez ajouter une question **Choix unique à partir d'un fichier** ou **Choix multiple à partir d'un fichier** dans le Formbuilder.

Pour ajouter une question de type choix à partir d'un fichier :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ AJOUTER UNE QUESTION**.
4. Choisissez <i class="k-icon-qt-select-one-from-file"></i> **Choix unique à partir d'un fichier** ou <i class="k-icon-qt-select-many-from-file"></i> **Choix multiple à partir d'un fichier** comme type de question.

![Questions à choix multiple](images/external_file/select.png)

<p class="note">
<strong>Note :</strong> Les types de questions <strong>Choix unique à partir d'un fichier</strong> et <strong>Choix multiple à partir d'un fichier</strong> n'apparaissent comme options dans le Formbuilder que si un fichier de choix externe a été importé dans KoboToolbox.
</p>

Si un seul fichier externe a été importé dans votre projet, il sera automatiquement associé à la question. Si plusieurs fichiers ont été importés, ouvrez les <i class="k-icon-settings"></i> **Paramètres** de la question et sélectionnez le fichier approprié dans le menu déroulant <i class=""></i> **Fichier des choix**.

![Fichier des choix](images/external_file/choices_file.png)

<p class="note">
Pour apprendre à configurer des questions de type choix à partir d'un fichier dans XLSForm et pour obtenir une aide supplémentaire à la résolution de problèmes, consultez l'article <a href="https://support.kobotoolbox.org/fr/select_from_file_xls.html#">Sélectionner des options à partir d'un fichier externe avec XLSForm</a>.
</p>