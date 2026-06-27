# Personnaliser vos formulaires à l'aide de XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/8e8a733c7bdc3e6479696bfba96ce397c1425ab4/source/form_style_xls.md" class="reference">22 Jun 2026</a>

Avec KoboToolbox, vous pouvez personnaliser l'apparence de vos formulaires et de vos questions pour mettre en valeur les informations clés et adapter la mise en page à vos besoins de collecte de données. Cela inclut l'application de thèmes aux formulaires web, l'ajout d'en-têtes et de listes dans les questions de type note, ainsi que l'utilisation de couleurs ou de la mise en gras pour souligner certains éléments.

Cet article traite des thèmes pour les formulaires web ainsi que des options de mise en forme pour les notes et les questions au sein d'un formulaire.

<p class="note">
<strong>Note :</strong> Cet article porte sur la mise en forme des formulaires dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur la définition des thèmes de formulaires web dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/alternative_enketo.html">Styliser vos formulaires web dans le Formbuilder</a>.
</p>

## Thèmes pour les formulaires web

Les thèmes de formulaires web vous permettent de personnaliser l'apparence et la mise en page des [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html). Les thèmes s'appliquent uniquement aux formulaires web et ne sont pas visibles dans KoboCollect.

### Ajouter des thèmes dans un XLSForm

Pour ajouter un thème dans un XLSForm :
1. Ajoutez une colonne `style` dans votre **onglet settings**.
2. Indiquez le thème que vous souhaitez utiliser, en reprenant exactement le nom indiqué dans le tableau ci-dessous.

**onglet settings**

| style       |
|:------------|
| theme-grid  |
| settings |

<p class="note">
<strong>Note :</strong> Les thèmes peuvent être combinés en saisissant les deux noms de thèmes dans la même cellule de la colonne <code>style</code>, séparés par un espace (par exemple, <code>theme-grid pages</code>).
</p>

### Thèmes disponibles pour les formulaires web

Les thèmes suivants sont disponibles pour personnaliser vos formulaires :

| Thème XLSForm                | Description                                                                 | Aperçu |
|:-----------------------------|:----------------------------------------------------------------------------|:-------|
| Thème par défaut             | Affiche les questions les unes après les autres, sur une seule page.        | ![Style par défaut](images/form_style_xls/theme_default.png) |
| <code>pages</code>           | Affiche une question par écran ou un <a href="https://support.kobotoolbox.org/fr/grouping_questions_xls.html">groupe de questions</a> sur le même écran, de manière similaire à la mise en page de KoboCollect. | ![Style pages](images/form_style_xls/theme_pages.png) |
| <code>theme-grid</code>      | Un affichage alternatif plus compact, similaire aux formulaires papier, qui utilise efficacement l'espace en disposant plusieurs questions par ligne. Les questions sont mises en majuscules par défaut. Nécessite de <a href="https://support.kobotoolbox.org/fr/form_style_xls.html#setting-up-an-xlsform-for-theme-grid">configurer votre XLSForm</a>. | ![Theme-grid](images/form_style_xls/theme_grid.png) |
| <code>theme-grid no-text-transform</code> | Identique à theme-grid, mais sans mise en majuscules automatique des questions. | ![Theme-grid no-text-transform](images/form_style_xls/theme_grid_no_text_transform.png) |

### Configurer un XLSForm pour theme_grid

Dans les formulaires web, la mise en page `theme_grid` vous permet d'afficher les questions en plusieurs colonnes, rendant votre formulaire plus compact et visuellement organisé. La configuration de ces colonnes — notamment leur nombre et leur largeur — est contrôlée en attribuant des `w-values` à chaque question dans la colonne `appearance` de votre XLSForm.

<p class="note">
  Pour une présentation complète de l'utilisation de <code>theme_grid</code> dans XLSForm, consultez ce <a href="https://ee.kobotoolbox.org/n41GqUkf">tutoriel sur le thème grille</a> et cet <a href="https://docs.google.com/spreadsheets/d/1qKmxPTA4B0vihU6GsKgi1CJE2Db2FfE7KZpOig4nTEI/edit?gid=0#gid=0">XLSForm type</a>.
</p>

Avant d'attribuer des `w-values` à chaque question, commencez par regrouper toutes les questions dans des [groupes de questions](https://support.kobotoolbox.org/fr/grouping_questions_xls.html). La largeur par défaut d'un groupe ou d'un groupe répété est de quatre colonnes (`w4`), ce qui signifie qu'un groupe avec `w4` peut contenir au maximum quatre questions `w1` sur une même ligne. La `w-value` d'une question est relative à la `w-value` de son groupe.

Pour définir la largeur relative de chaque question au sein d'une ligne :
1. Ajoutez une colonne `appearance` dans votre **onglet survey**.
2. Pour chaque question, attribuez des valeurs d'apparence (par exemple, `w1`, `w2`, `w3`) pour définir sa largeur relative au sein d'une ligne.
3. Modifiez la largeur du groupe si nécessaire en utilisant la même approche.

Les lignes s'étendent toujours automatiquement sur toute la largeur de la page. Par exemple, une ligne contenant une question avec une valeur d'apparence `w2` et une autre avec `w1` divisera la ligne en deux tiers et un tiers, respectivement.

<p class="note">
<strong>Note :</strong> Appliquez les <code>w-values</code> uniquement aux groupes ou groupes répétés de premier niveau. Bien que leur application à des sous-groupes ou groupes répétés imbriqués soit disponible, l'affichage peut ne pas être optimal.
</p>

## Mise en forme du texte

Vous pouvez utiliser Markdown et HTML dans XLSForm pour **mettre en forme le texte**, **ajouter de l'emphase** avec du gras ou de l'italique, **créer des en-têtes** de différentes tailles, **modifier les polices et les couleurs**, et **ajouter des liens web cliquables**. La mise en forme du texte peut être appliquée aux questions, aux indices de question et aux notes.

<p class="note">
<strong>Note :</strong> Certaines fonctionnalités de mise en forme peuvent ne pas être prises en charge dans KoboCollect ou dans les formulaires web. Il est recommandé de prévisualiser vos formulaires dans la méthode de collecte de données choisie pour vérifier que toutes les fonctionnalités de mise en forme sont bien disponibles.
</p>

Les fonctionnalités de mise en forme du texte dans XLSForm incluent :

| Fonctionnalité  | Mise en forme |
|:----------------|:--------------|
| Italique        | `*italics*` ou `_italics_` |
| Gras            | `**bold**` ou `__bold__` |
| Lien hypertexte | `[nom du lien](url)` |
| E-mail          | `[email@domain.org](mailto:email@domain.org)` |
| En-têtes        | `# Header 1` (le plus grand) à `###### Header 6` (le plus petit) |
| Listes à puces  | - Ceci est une liste non ordonnée<br>- en markdown |
| Listes numérotées | 1. Ceci est une liste numérotée<br>2. en markdown |
| Emojis          | Par exemple, 🙂 😐 🙁 😦 😧 😩 😱 |
| Exposant        | `100 m<sup>2</sup>` devient 100 m² |
| Indice          | `H<sub>2</sub>O` devient H₂O |
| Texte coloré    | `<span style="color:#f58a1f">orange</span>` devient <span style="color:#f58a1f">orange</span> <br>`<span style="color:red">red</span>` devient <span style="color:red">red</span> |
| Police          | `<span style="font-family:cursive">cursive</span>` devient <span style="font-family:cursive">cursive</span> <br>`<span style="color:red; font-family:cursive">red and cursive</span>` devient <span style="color:red; font-family:cursive">red and cursive</span> |
| Centrer le texte | `<p style="text-align:center">Centered label</p>` centre le texte à l'écran (KoboCollect uniquement) |
| Masquer le libellé | `<span style="display:none">Hidden label</span>` masque le libellé de la question (formulaires web uniquement) |
| Supprimer le gras | `<span style="font-weight: normal;">What is your age?</span>` supprime la mise en gras du libellé de la question (formulaires web uniquement) |
| Soulignement    | `<span style="text-decoration: underline;">This text is underlined</span>` souligne le texte (formulaires web uniquement) |

<p class="note">
<strong>Note :</strong> Utilisez le caractère <code>\</code> avant <code>#</code>, <code>*</code>, <code>_</code> et <code>\</code> pour empêcher ces caractères de déclencher des effets de mise en forme spéciaux.
</p>