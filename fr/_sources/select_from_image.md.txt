# Sélectionner des options à partir d'une image
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_from_image.md" class="reference">23 avr. 2026</a>

La sélection d'options à partir d'une image permet aux répondants d'appuyer ou de cliquer directement sur **des zones spécifiques d'un fichier SVG** plutôt que de choisir dans une liste de texte. Cette fonctionnalité est disponible avec les formulaires web et l'application Android KoboCollect.

Vous pouvez utiliser cette fonctionnalité pour :

- Sélectionner un emplacement à partir de l'image d'une pièce ou d'un bâtiment
- Sélectionner une partie du corps à partir d'un schéma du corps humain
- Sélectionner des zones endommagées à partir d'une photo d'un bâtiment après une catastrophe

Cet article explique comment créer une image SVG avec des zones sélectionnables et configurer votre XLSForm afin que les répondants puissent choisir des options directement à partir de l'image.

![](images/select_from_image/select_image.png)


## Créer votre image sélectionnable

Pour créer une image avec des zones sélectionnables, vous devez utiliser un fichier **SVG (Scalable Vector Graphics)**.

<p class="note">
 Pour en savoir plus sur les fichiers SVG, consultez la <a href="https://developer.mozilla.org/en-US/docs/Web/SVG">documentation SVG</a>. Nous recommandons d'utiliser <a href="https://inkscape.org/">Inkscape</a>, un éditeur de graphiques vectoriels gratuit et open source, pour créer et modifier des fichiers SVG.
</p>

Chaque zone sélectionnable de l'image doit inclure un attribut `id`. Ces valeurs `id` doivent correspondre exactement aux valeurs `name` dans l'onglet `choices` de votre XLSForm ; elles doivent donc respecter les mêmes [conventions de nommage](https://support.kobotoolbox.org/fr/option_choices_xls.html#best-practices-for-defining-choice-names).

Pour créer votre fichier image sélectionnable :

1. Créez ou modifiez un fichier `.svg`.
2. Ajoutez des attributs `id` à chaque élément que vous souhaitez rendre sélectionnable.
3. Enregistrez le fichier.

<p class="note">
<strong>Remarque :</strong> Dans les formulaires web, seuls les éléments SVG <code>&lt;path&gt;</code> sont disponibles comme zones sélectionnables. D'autres formes SVG, telles que les rectangles ou les cercles, peuvent ne pas fonctionner comme prévu. KoboCollect fonctionne avec des primitives SVG supplémentaires.
</p>

## Configurer votre XLSForm

Pour permettre aux répondants de sélectionner des options à partir de votre image dans XLSForm :

1. Dans l'**onglet survey**, ajoutez une question `select_one` ou `select_multiple`.
2. Ajoutez une colonne `appearance` et saisissez `image-map`.
3. Ajoutez une colonne `image` et saisissez le nom exact du fichier SVG.
4. Dans l'**onglet choices**, ajoutez la liste des choix.
    - La colonne `name` doit correspondre exactement aux valeurs `id` de votre fichier SVG.

**onglet survey**

| type | name | label | appearance | image |
|:---|:---|:---|:---|:---|
| select_one body | body_part | Which body part hurts the most? | image-map | body.svg |
| survey |

**onglet choices**

| list_name | name | label |
|:---|:---|:---|
| body | leg | Leg |
| body | arm | Arm |
| body | head | Head |
| choices |

## Importer le fichier SVG dans KoboToolbox

Après avoir créé votre fichier SVG et l'avoir référencé dans votre XLSForm, vous devez l'importer dans votre projet.

Pour importer des fichiers multimédias :

1. Connectez-vous à votre compte KoboToolbox.
2. Ouvrez votre projet.
3. Accédez à **PARAMÈTRES > Média**.
4. Importez le fichier SVG. Assurez-vous que le nom du fichier correspond exactement à ce qui est indiqué dans la colonne `image` de votre XLSForm.
5. Déployez ou redéployez votre formulaire pour appliquer les modifications.

<p class="note">
Pour en savoir plus sur l'importation de fichiers multimédias, consultez l'article <a href="https://support.kobotoolbox.org/fr/upload_media.html">Importer des fichiers multimédias dans un projet</a>.
</p>