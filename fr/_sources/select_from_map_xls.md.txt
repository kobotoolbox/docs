# Sélectionner des options à partir d'une carte
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_from_map_xls.md" class="reference">23 avr. 2026</a>

Avec les types de questions `select_one` et `select_one_from_file`, vous pouvez configurer votre XLSForm pour permettre aux utilisateurs de sélectionner un choix directement sur une carte plutôt que dans une liste. Lorsque la carte s'ouvre, elle affiche tous les points, lignes ou polygones disponibles en fonction des choix fournis. Les utilisateurs peuvent alors appuyer sur un élément de la carte pour enregistrer leur sélection. Cette fonctionnalité est disponible **uniquement dans KoboCollect.**

Cet article explique comment configurer votre XLSForm pour permettre la sélection d'options à partir d'une carte, comment personnaliser les options de style telles que les couleurs, les symboles et les largeurs de ligne, et comment les choix sont affichés et sélectionnés sur la carte.

<p class="note">
<strong>Note :</strong> L'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong> ne permet pas la sélection sur carte pour le type de question <code>select_one</code>. Pour utiliser cette fonctionnalité, configurez-la dans un XLSForm et importez le formulaire dans KoboToolbox.
  <br><br>
  Pour en savoir plus sur le téléchargement et la modification de votre formulaire en tant que XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>.
</p>

## Configurer votre XLSForm

Pour configurer une question **sélection à partir d'une carte** dans XLSForm :

1. Dans l'**onglet survey**, ajoutez une question de type `select_one` ou `select_one_from_file`.
2. Ajoutez une colonne `appearance`.
3. Dans la colonne `appearance` de la question à choix multiple, saisissez `map` ou `quick map`.
    - L'**apparence map** permet aux répondants de cliquer sur différents emplacements et de consulter des informations sur chacun d'eux avant de confirmer leur sélection.
    - L'**apparence quick map** enregistre automatiquement le premier emplacement sélectionné sans afficher d'informations supplémentaires.

**onglet survey**

| type        | name     | label                       | appearance |
|:------------|:---------|:----------------------------|:-----------|
| select_one  | location | Où êtes-vous actuellement basé ? | map       |
| survey |

4. Dans l'**onglet choices** ou dans votre [liste de choix externe](https://support.kobotoolbox.org/fr/select_from_file_xls.html), saisissez les choix comme vous le feriez normalement.
5. À côté de votre liste de choix, ajoutez une colonne `geometry`.
6. Pour chaque choix, saisissez les coordonnées GPS correspondantes dans la colonne `geometry`.
    - Ce champ peut inclure des coordonnées GPS uniques ou multiples, pour définir un point, une ligne ou un polygone.

**onglet choices**

| list_name | name | label  | geometry           |
|:----------|:-----|:-------|:------------------|
| cities    | 1    | Warsaw | 52.2297 21.0122 0 0 |
| cities    | 2    | Berlin | 52.5200 13.4050 0 0 |
| cities    | 3    | Paris  | 48.8566 2.3522 0 0  |
| cities    | 4    | Kyiv   | 50.4501 30.5234 0 0 |
| cities    | 5    | Prague | 50.0755 14.4378 0 0 |
| choices |

### Format des coordonnées GPS

Lors de la saisie des coordonnées GPS dans l'**onglet choices** ou dans un fichier CSV ou XML externe, le format suivant doit être utilisé : `longitude latitude altitude précision`.

- Par exemple, les coordonnées GPS de Paris seraient `48.8566 2.3522 0 0`.

Lorsque vous fournissez plusieurs coordonnées GPS (par exemple, pour une ligne ou un polygone), les coordonnées sont séparées par un point-virgule.
- Par exemple, les coordonnées GPS d'une ligne allant de Paris à Madrid seraient `48.8566 2.3522 0 0;40.4637 -3.6556 0 0`.
- Pour un polygone, les coordonnées GPS doivent commencer et se terminer par les mêmes coordonnées.

<p class="note">
<strong>Note :</strong> Pour obtenir vos coordonnées GPS dans le format correct, vous pouvez utiliser ce <a href="https://ee.kobotoolbox.org/preview/7OmWg7pD">formulaire KoboToolbox</a>. Il vous permet de sélectionner des points sur une carte et génère automatiquement les coordonnées GPS correspondantes au format ODK.
</p>

Si vous utilisez un fichier GeoJSON pour fournir des coordonnées GPS, suivez le [format GeoJSON](https://docs.getodk.org/form-datasets/#selects-from-geojson) pour spécifier la `geometry` de l'élément.

<p class="note">
  Pour un exemple de questions à sélection sur carte, consultez cet <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/SelectFromMap.xlsx">XLSForm type</a>. Les fichiers de choix externes à importer dans KoboToolbox sont disponibles <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities1.csv">ici</a> (CSV), <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities2.geojson">ici</a> (GeoJSON) et <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities3.xml">ici</a> (XML). Pour en savoir plus sur l'utilisation de fichiers de choix externes, consultez l'article <a href="https://support.kobotoolbox.org/fr/select_from_file_xls.html">Sélectionner des options à partir d'un fichier externe avec XLSForm</a>.
</p>

## Ajouter des propriétés de choix

Vous pouvez personnaliser davantage votre carte en ajoutant des propriétés de choix dans l'**onglet choices** ou dans un fichier de choix externe.

Les propriétés de choix disponibles sont les suivantes :

| Propriété de choix | Description |
|:----------------|:------------|
| `info`            | Description textuelle du choix. |
| `marker-color`    | Couleur HEX du marqueur de géopoint. |
| `marker-symbol`   | Caractère unique, symbole ou emoji affiché sur le marqueur de géopoint. |
| `stroke`          | Couleur HEX de la ligne de géotrace ou du contour du polygone de géoforme. |
| `stroke-width`    | Largeur de la ligne de géotrace ou du contour du polygone de géoforme (par exemple, 5 ou 6,5). |
| `fill`            | Couleur HEX de l'intérieur du polygone. La couleur de remplissage est affichée avec une transparence fixe. |

Pour ajouter des propriétés dans l'**onglet choices** de votre XLSForm :

1. Ajoutez une colonne avec le nom de propriété approprié (par exemple, `info`, `stroke` ou `fill`).
2. Pour chaque choix, saisissez la valeur correspondante (par exemple, une description textuelle ou un code HEX).

**onglet choices**

| list_name | name | label  | geometry           | info                       |
|:----------|:-----|:-------|:------------------|:---------------------------|
| cities    | 1    | Warsaw | 52.2297 21.0122 0 0 | Capitale de la Pologne          |
| cities    | 2    | Berlin | 52.5200 13.4050 0 0 | Capitale de l'Allemagne         |
| cities    | 3    | Paris  | 48.8566 2.3522 0 0  | Capitale de la France          |
| cities    | 4    | Kyiv   | 50.4501 30.5234 0 0 | Capitale de l'Ukraine         |
| cities    | 5    | Prague | 50.0755 14.4378 0 0 | Capitale de la République tchèque  |
| choices |

Si vous utilisez un fichier GeoJSON pour fournir des coordonnées GPS, suivez le [format GeoJSON](https://docs.getodk.org/form-datasets/#selects-from-geojson) pour spécifier les `properties` de l'élément.

## Sélection sur carte dans KoboCollect

<iframe src="https://www.youtube.com/embed/C7o9rCKmCeo?si=h9y-meFvNwury_mI&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<p class="note">
<strong>Note :</strong> La sélection d'options à partir d'une carte est <strong>uniquement disponible dans KoboCollect.</strong> Dans les formulaires web, les choix de réponse s'affichent sous forme de liste normale d'options.
</p>

Dans KoboCollect, l'ajout d'une **question à choix multiple** avec une apparence `map` ou `quick map` permet aux utilisateurs de choisir une option directement sur une carte plutôt que dans une liste. Lorsque la carte s'ouvre, elle est centrée sur la position actuelle de l'appareil. Des boutons sur la droite permettent aux utilisateurs de recentrer la vue sur leur position ou d'afficher tous les points disponibles sur la carte.

Les choix de type point sont affichés sous forme de marqueurs sur la carte. Appuyer sur un marqueur augmente sa taille.
Les choix de type ligne et polygone sont affichés sous forme de contours rouges, les polygones étant ombrés en rouge. Les utilisateurs peuvent appuyer sur une ligne ou un polygone pour le sélectionner. Lorsqu'un emplacement est sélectionné, ses [propriétés](https://support.kobotoolbox.org/fr/select_from_map_xls.html#adding-choice-properties) apparaissent en bas de l'écran, sauf si l'apparence `quick map` est utilisée.

Sous le libellé du choix, un bouton **Select** apparaît pour confirmer et enregistrer l'emplacement sélectionné dans le formulaire, sauf si l'apparence `quick map` est utilisée.

<p class="note">
<strong>Note :</strong> Les apparences <code>map</code> et <code>quick map</code> peuvent être combinées avec des <a href="https://support.kobotoolbox.org/fr/choice_filters_xls.html">filtres de choix</a> pour afficher des options sur la carte en fonction d'une sélection précédente.
</p>