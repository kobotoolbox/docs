# Questions de type note dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/1833c42c415ddc826146609c1915525d77cf94c8/source/note_questions.md" class="reference">22 Jun 2026</a>

Les questions de type note permettent d'afficher des informations dans votre formulaire sans collecter de réponse. Bien qu'elles soient répertoriées comme un type de question, les questions de type note ne stockent aucune donnée. Elles servent plutôt à **fournir des instructions, du contexte ou des informations complémentaires** qui aident les répondants ou les enquêteurs à comprendre et à remplir correctement le formulaire.

Vous pouvez utiliser les questions de type note pour introduire une nouvelle section, expliquer pourquoi certaines questions sont posées, fournir des indications sur la façon de répondre, [afficher des médias](https://support.kobotoolbox.org/fr/media.html), ou afficher les résultats de [calculs cachés](https://support.kobotoolbox.org/fr/calculate_questions.html) ou de [réponses précédentes](https://support.kobotoolbox.org/fr/form_logic.html#question-referencing).

Cet article explique comment ajouter une question de type **Note** dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** et comment appliquer une mise en forme au texte de votre note.

## Ajouter une question de type note dans le Formbuilder

Pour ajouter une question de type note à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ AJOUTER UNE QUESTION.**
4. Choisissez le type de question <i class="k-icon-qt-note"></i> **Note**.

![Choisir le type de question note](images/note_questions/note.png)

## Apparences des questions de type note

Par défaut, les questions de type note apparaissent sous forme de texte simple dans votre formulaire.

| Formulaires web | KoboCollect |
|:----------------|:------------|
| ![Question de type note dans les formulaires web](images/note_questions/enketo_note.png) | ![Question de type note dans KoboCollect](images/note_questions/kobocollect_note.png) |

### Apparences avancées

Lors de l'ajout de notes à votre formulaire, vous pouvez utiliser Markdown et HTML pour **mettre en forme le texte, ajouter de l'emphase** en gras ou en italique, **créer des titres** de différentes tailles, **modifier les polices et les couleurs**, et **ajouter des liens web cliquables.**

<p class="note">
<strong>Note :</strong> La mise en forme du texte peut également être appliquée aux libellés et aux indices de questions.
</p>

Les fonctionnalités de mise en forme du texte dans le Formbuilder comprennent :

| Fonctionnalité | Mise en forme |
|:---------------|:-------------|
| Italique       | `*italics*` ou `_italics_` |
| Gras           | `**bold**` ou `__bold__` |
| Lien hypertexte | `[nom du lien](url)` |
| Email          | `[email@domain.org](mailto:email@domain.org)` |
| Titres         | `# Header 1` (le plus grand) à `###### Header 6` (le plus petit) |
| Emojis         | Par exemple, 🙂 😐 🙁 😦 😧 😩 😱 |
| Exposant       | `100 m<sup>2</sup>` devient 100 m² |
| Indice         | `H<sub>2</sub>O` devient H₂O |
| Texte coloré   | `<span style="color:#f58a1f">orange</span>` devient <span style="color:#f58a1f">orange</span> <br>`<span style="color:red">red</span>` devient <span style="color:red">rouge</span> |
| Police         | `<span style="font-family:cursive">cursive</span>` devient <span style="font-family:cursive">cursive</span> <br>`<span style="color:red; font-family:cursive">red and cursive</span>` devient <span style="color:red; font-family:cursive">rouge et cursive</span>|
| Centrer        | `<p style="text-align:center">Centered label</p>` centre le texte à l'écran (KoboCollect uniquement) |
| Souligner      | `<span style="text-decoration: underline;">This text is underlined</span>` souligne le texte (formulaires web uniquement) |


<p class="note">
<strong>Note :</strong> Des fonctionnalités de mise en forme supplémentaires, telles que les sauts de ligne, les listes à puces et les listes numérotées, sont disponibles uniquement lors de la <a href="https://support.kobotoolbox.org/fr/form_style_xls.html#styling-text">création de votre formulaire dans XLSForm</a>.
</p>