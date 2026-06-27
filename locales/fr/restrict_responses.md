# Utiliser des expressions régulières avec XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/d7c5254864f652f34ecb1d4bfe52ef2ddb1247e1/source/restrict_responses.md" class="reference">6 mai 2026</a>

Une **expression régulière**, ou regex, est un modèle de recherche utilisé pour identifier des caractères ou des plages de caractères spécifiques dans un texte. Les expressions régulières sont couramment utilisées pour valider, rechercher, extraire ou restreindre la saisie de texte.

Dans KoboToolbox, les expressions régulières sont généralement utilisées pour contrôler la façon dont les utilisateurs saisissent des données. Par exemple, vous pouvez limiter un numéro de téléphone à exactement 10 chiffres, imposer un format d'identifiant spécifique, ou restreindre la saisie aux lettres majuscules uniquement.

Cet article présente les composants courants des expressions régulières ainsi que des exemples pratiques que vous pouvez utiliser pour valider et restreindre la saisie de texte dans vos formulaires.

<p class="note">
   Pour en savoir plus sur l'utilisation des expressions régulières dans vos formulaires, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a> et l'article <a href="https://support.kobotoolbox.org/fr/form_logic.html">Introduction à la logique de formulaire dans le Formbuilder</a>.
</p>

## Composants courants des expressions régulières

Les expressions régulières dans KoboToolbox sont écrites à l'intérieur de la fonction `regex()`. Par exemple, `regex(., '^[0-9]{10}$')` limite la saisie à exactement 10 chiffres.

Les tableaux suivants décrivent les éléments regex les plus couramment utilisés.

### Ancres et regroupements

| Regex | Description |
|:---|:---|
| <code>^</code> | Correspond au début d'une chaîne de caractères |
| <code>$</code> | Correspond à la fin d'une chaîne de caractères |
| <code>( )</code> | Regroupe des caractères ensemble |
| <code>\|</code> | Correspond à un modèle ou à un autre (OU logique) |

### Classes de caractères

| Regex | Description |
|:---|:---|
| <code>[abc]</code> | Correspond à a, b ou c |
| <code>[a-z]</code> | Correspond à n'importe quelle lettre minuscule |
| <code>[A-Z]</code> | Correspond à n'importe quelle lettre majuscule |
| <code>[0-9]</code> | Correspond à n'importe quel chiffre de 0 à 9 |
| <code>[a-zA-Z0-9]</code> | Correspond à des lettres ou des chiffres |
| <code>\[^abc]</code> | Correspond à n'importe quel caractère sauf a, b ou c |
| <code>\[^A-Z]</code> | Correspond à n'importe quel caractère sauf les lettres majuscules |

### Raccourcis pour les caractères spéciaux

| Regex | Description |
|:---|:---|
| <code>\d</code> | Correspond à n'importe quel chiffre (équivalent à [0-9]) |
| <code>\D</code> | Correspond à n'importe quel caractère non numérique |
| <code>\w</code> | Correspond à n'importe quelle lettre, chiffre ou tiret bas (`_`) |
| <code>\W</code> | Correspond à tout sauf les lettres, les chiffres et les tirets bas (`_`) |
| <code>\s</code> | Correspond à un espace ou une tabulation |
| <code>\b</code> | Correspond à une limite de mot |
| `\.` | Correspond à un point littéral (<code>.</code>) |
| <code>\\@</code> | Correspond à un <code>@</code> littéral |
| <code>\\$</code> | Correspond à un <code>$</code> littéral |
| `\\` | Correspond à une barre oblique inverse littérale (<code>\\</code>) |
| <code>\number</code> | Fait référence à un groupe précédemment mis en correspondance |

### Quantificateurs

| Regex | Description |
|:---|:---|
| <code>?</code> | Correspond à zéro ou une occurrence |
| <code>*</code> | Correspond à zéro ou plusieurs occurrences |
| <code>+</code> | Correspond à une ou plusieurs occurrences |
| <code>{x}</code> | Correspond exactement à x occurrences |
| <code>{x,}</code> | Correspond à au moins x occurrences |
| <code>{x,y}</code> | Correspond à entre x et y occurrences |

## Exemples courants

Les exemples suivants peuvent être utilisés comme [contraintes](https://support.kobotoolbox.org/fr/constraints_xls.html) ou [critères de validation](https://support.kobotoolbox.org/fr/validation_criteria.html) dans vos formulaires.

### Expressions régulières courantes avec des chiffres

| Regex | Description |
|:---|:---|
| <code>regex(., '^\d+$')</code> | Limiter la saisie aux chiffres |
| <code>regex(., '^\d{2}$')</code> | Limiter la saisie à 2 chiffres |
| <code>regex(., '^\d{2,4}$')</code> | Limiter la saisie à 2-4 chiffres |
| <code>regex(., '^\d{10}$')</code> | Limiter la saisie à 10 chiffres |
| <code>regex(., '^[1-9][0-9]?$&#124;^100$')</code> | Limiter la saisie à un nombre compris entre 1 et 100 (par exemple, pour un pourcentage) |
| <code>regex(., '^[1-9][0-9]{8}$')</code> | Limiter la saisie à 9 chiffres, le premier chiffre ne peut pas être 0 |
| <code>regex(., '^\d{2}\\.\d{3}$')</code> | Limiter la saisie à un nombre au format 12.345 |
| <code>regex(., '^(\d{10}&#124;\d{13}&#124;\d{17})$')</code> | Limiter la saisie à 10, 13 ou 17 chiffres |
| <code>regex(., '^(12&#124;345)$')</code> | La saisie doit être 12 ou 345 |
| `regex(., '^[0-9+]{7,15}$')` | Limiter la saisie à un numéro de téléphone (avec le signe `+` facultatif) |

### Expressions régulières courantes avec des lettres

| Regex | Description |
|:---|:---|
| <code>regex(., '^\D*$')</code> | Limiter la saisie aux lettres, espaces et symboles (sans chiffres) |
| <code>regex(., '^[A-Za-z]+$')</code> | Limiter la saisie aux lettres |
| <code>regex(., '^[A-Za-z\s]+$')</code> | Limiter la saisie aux lettres et aux espaces |
| <code>regex(., '^[a-z]{1,6}$')</code> | Limiter la saisie à 1–6 lettres minuscules |
| <code>regex(., '^[A-Z]{1,10}$')</code> | Limiter la saisie à 1–10 lettres majuscules |
| <code>regex(., '^(Apple&#124;Orange&#124;Banana)$')</code> | La saisie doit correspondre à un mot de la liste |
| <code>regex(., '^colou?r$')</code> | Accepte color ou colour |
| <code>regex(., '^[A-Z\s]+$')</code> | Limiter la saisie aux lettres majuscules et aux espaces uniquement |
| <code>regex(., '^[a-z_]+$')</code> | Limiter la saisie aux lettres minuscules et aux tirets bas (<code>_</code>) |

### Expressions régulières courantes avec des lettres et des chiffres

| Regex | Description |
|:---|:---|
| <code>regex(., '^\w{3}$')</code> | Limiter la saisie à exactement 3 lettres, chiffres ou tirets bas (<code>_</code>) |
| <code>regex(., '^[A-Z]{1}[0-9]{8}$')</code> | Limiter la saisie à une lettre et huit chiffres |
| <code>regex(., '^CAR-PRC-2020-\d{4}$')</code> | Limiter la saisie à un format d'identifiant spécifique |
| <code>regex(., '^\W*(\w+\b\W*){3}$')</code> | Limiter la saisie à exactement 3 mots |
| <code>regex(., '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)&#42;(\\&#92;.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)&#42;)&#42;\\&#92;.[a-zA-Z]{2,}$')</code> | Limiter la saisie au format e-mail courant |

<p class="note">
  Pour obtenir de l'aide supplémentaire pour créer et tester des modèles, visitez : <a href="http://www.regexr.com/">http://www.regexr.com/</a>
</p>