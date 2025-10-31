# Restreindre les réponses textuelles avec des expressions régulières
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/restrict_responses.md" class="reference">29 juil. 2025</a>

Une expression régulière, ou regex, est un modèle de recherche utilisé pour faire correspondre des caractères spécifiques et des plages de caractères dans une chaîne. Elle est largement utilisée pour valider, rechercher, extraire et restreindre du texte dans la plupart des langages de programmation. KoboToolbox prend en charge les regex pour contrôler la longueur et les caractères lors de la saisie de données pour une question particulière _(par exemple, contrôler la saisie d'un numéro de téléphone portable à exactement 10 chiffres, contrôler la saisie d'une adresse e-mail valide, etc.)_.

## Pour utiliser une regex dans KoboToolbox, suivez ces étapes

1. Préparez une question de type _Texte_.

2. Accédez aux _Paramètres_ de la question.

3. Accédez à _Critères de validation_ et choisissez l'option _Saisir manuellement votre logique de validation en code XLSForm_.

4. Dans la zone _Code de validation_, saisissez votre formule regex entre les guillemets `(' ')` du format `regex(., ' ')`. Pour référence, le point (`.`) fait référence à _'cette question'_, tandis que l'expression régulière à l'intérieur des guillemets (`' '`) doit être conforme aux règles regex établies.

5. (Facultatif) Ajoutez un _Message d'erreur_ personnalisé que la personne saisissant les données verra lorsqu'elle ne respecte pas les critères regex.

![image](/images/restrict_responses/regrex.jpg)

Les regex peuvent également être codées dans XLSForm, sous la colonne _constraint_ :

**feuille survey**

| type | name | label                       | appearance | constraint              | constraint_message                          |
| :--- | :--- | :-------------------------- | :--------- | :---------------------- | :------------------------------------------ |
| text | q1   | Numéro de téléphone portable du répondant | numbers    | regex(., '^[0-9]{10}$') | Cette valeur doit contenir uniquement 10 chiffres |
| survey |

Alternativement, vous pouvez créer une question de type `calculate` puis définir le code regex sous la colonne _calculation_. Vous pourriez ensuite utiliser cette variable autant de fois que nécessaire dans l'enquête :

**feuille survey**

| type      | name | label                  | calculation                              | constraint      | constraint_message                  |
| :-------- | :--- | :--------------------- | :--------------------------------------- | :-------------- | :---------------------------------- |
| calculate | q0   |                        | '^[A-Z]{1}[a-z]{1,}\s[A-Z]{1}[a-z]{1,}$' |                 |                                     |
| text      | q1   | Nom de l'enquêteur |                                          | regex(., ${q0}) | Veuillez utiliser ce format : Kobe Bryant |
| text      | q2   | Nom du répondant |                                          | regex(., ${q0}) | Veuillez utiliser ce format : Kobe Bryant |
| integer   | q3   | Âge du répondant  |                                          |                 |                                     |
| survey |

## Comment construire la regex dont j'ai besoin ?

En plus des exemples et conseils fournis ci-dessous, veuillez consulter [ce site web](http://www.regexr.com) pour plus d'aide et d'exemples.

<p class="note">Les regex dans KoboToolbox doivent toujours être écrites entre les apostrophes <code>regex(., ' ')</code> comme indiqué dans les exemples.</p>

| Regex               | Description                                                                                                                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `^`                 | Le symbole caret correspond au début d'une chaîne sans consommer aucun caractère.                                                                                                             |
| `$`                 | Le symbole dollar correspond à la fin d'une chaîne sans consommer aucun caractère.                                                                                                              |
| `[abc]`             | Correspond soit à `a`, `b` ou `c` parmi les crochets `[ ]`.                                                                                                                       |
| `[a-z]`             | Correspond à n'importe quel caractère minuscule de `a` à `z`.                                                                                                                                            |
| `[A-Z]`             | Correspond à n'importe quel caractère majuscule de `A` à `Z`.                                                                                                                            |
| `[0-9]`             | Correspond à n'importe quel nombre entier de `0` à `9`.                                                                                                                                                  |
| `[a-zA-Z0-9]`       | Correspond à n'importe quel caractère de `a` à `z` ou `A` à `Z` ou `0` à `9`.                                                                                                                          |
| `[^abc]`            | Correspond à n'importe quel caractère _sauf_ `a`, `b` ou `c`.                                                                                                                                             |
| `[^A-Z]`            | Correspond à n'importe quel caractère _sauf_ ceux de la plage `A` à `Z`.                                                                                                                              |
| `(apple)`           | Le caractère de regroupement `( )` correspond à tout ce qui se trouve entre les parenthèses.                                                                                                               |
| <code>&#x7c;</code> | Une barre verticale correspond à n'importe quel élément séparé.                                                                                                                                               |
| `\`                 | Une barre oblique inverse est utilisée pour correspondre à la valeur littérale de tout métacaractère (par exemple, essayez d'utiliser `\.` ou `\@` ou `\$` lors de la construction de regex).                                                            |
| `\number`           | Correspond au même caractère que celui récemment mis en correspondance par le n<sup>ième</sup> (numéro utilisé) groupe de capture.                                                                                    |
| `\s`                | Correspond à n'importe quel _espace_ ou _tabulation_.                                                                                                                                                               |
| `\b`                | Correspond, sans consommer aucun caractère, immédiatement entre un caractère correspondant à `\w` et un caractère ne correspondant pas à `\w` (dans les deux sens). `\b` est également connu sous le nom de _limite de mot_. |
| `\d`                | Correspond à n'importe quel nombre équivalent `[0-9]`                                                                                                                                                      |
| `\D`                | Correspond à tout sauf les nombres `(0 à 9)`.                                                                                                                             |
| `\w`                | Correspond à n'importe quel caractère de mot (c'est-à-dire `a` à `z` ou `A` à `Z` ou `0` à `9` ou `_`).                                                                                            |
| `\W`                | Correspond à tout sauf ce à quoi `\w` correspond (c'est-à-dire qu'il correspond aux caractères génériques et aux espaces).                                                                                                      |
| `?`                 | Un point d'interrogation utilisé juste derrière un caractère correspond ou ignore (si non requis) une correspondance de caractère.                                                                                          |
| `*`                 | Un symbole astérisque utilisé juste derrière un caractère correspond à zéro ou plusieurs caractères consécutifs.                                                                                                 |
| `+`                 | Le symbole plus utilisé juste derrière un caractère correspond à un ou plusieurs caractères consécutifs.                                                                                                     |
| `{x}`               | Correspond exactement à `x` caractères consécutifs.                                                                                                                                                 |
| `{x,}`              | Correspond à au moins `x` caractères consécutifs (ou plus).                                                                                                                                      |
| `{x,y}`             | Correspond entre `x` et `y` caractères consécutifs.                                                                                                                                         |

## Caractères avec accents

| **Regex**           | **Description**                                                                                                |
| :------------------ | :------------------------------------------------------------------------------------------------------------- |
| `[A-zÀ-ú]`          | Accepte les caractères accentués minuscules et majuscules                                                             |
| `[A-zÀ-ÿ]`          | Accepte les caractères accentués minuscules et majuscules mais incluant les lettres avec un tréma (inclut [ ] ^ \ × ÷) |
| `[A-Za-zÀ-ÿ]`       | Accepte les caractères accentués minuscules et majuscules mais n'incluant pas [ ] ^ \                                   |
| `[A-Za-zÀ-ÖØ-öø-ÿ]` | Accepte les caractères accentués minuscules et majuscules mais n'incluant pas [ ] ^ \ × ÷                               |

## Exemples liés à l'utilisation de nombres

<p class="note">Pour toutes les questions de type <code>text</code> qui utilisent des nombres, n'oubliez pas de saisir <code>numbers</code> sous la colonne <code>appearance</code>.</p>

| **Regex**                                                                                                                                                                                | **Description**                                                                                                  |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| `regex(., '^[0-9]{10}$')` ou `regex(., '^\d{10}$')`                                                                                                                                      | Restreindre le numéro de téléphone portable à dix chiffres                                                                             |
| `regex(., '^[0-9]{4}.[0-9]{2}.[0-9]{2}$')` ou `regex(., '^\d{4}\.\d{2}\.\d{2}$')`                                                                                                        | Restreindre une saisie à `1234.56.78`                                                                                |
| `regex(., '^[01-99]{2}$') and (. >= 01)`                                                                                                                                                 | Restreindre une saisie entre `01` et `99` chiffres où le format de saisie d'un seul nombre (comme 1 ou 2) n'est pas autorisé |
| `regex(., '^(12\|345)$')`                                                                                                                                                                | Restreindre une saisie soit à `12` soit à `345`                                                                     |
| `regex(., '^[1-9][0-9]{8}$')` ou `regex(., '^[^0][0-9]{8}$')`                                                                                                                            | Restreindre une saisie de neuf chiffres où le premier nombre ne peut pas être `0`                                             |
| `regex(., '^\d$')`                                                                                                                                                                       | Restreindre une saisie à un chiffre entre `0` et `9`                                                             |
| `regex(., '^\d{5}$')`                                                                                                                                                                    | Restreindre une saisie à cinq chiffres entre `0` et `9`                                                           |
| `regex(., '^\d{2}\.\d{3}$')`                                                                                                                                                             | Restreindre une saisie à deux chiffres et trois décimales (par exemple `12.345`)                                               |
| `regex(., '^\d{2}(\.\d{3})?$')`                                                                                                                                                          | Restreindre une saisie à deux chiffres et trois décimales (tandis que les décimales sont facultatives) (par exemple `12` ou `12.345`)     |
| `regex(., '^[0-9]{10}$') or regex(., '^[0-9]{13}$')` ou `regex(., '^[0-9]{17}$')` ou `regex(., '^([0-9]{10}\|[0-9]{13}\|[0-9]{17})$')` ou `regex(., '^([\d]{10}\|[\d]{13}\|[\d]{17})$')` | Restreindre une saisie à des nombres de `10`, `13` ou `17` chiffres uniquement                                                       |

## Exemples liés à l'utilisation de lettres

| **Regex**                                                                                               | **Description**                                                                                                                                                                                                                                                                                                                            |
| :------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex(., '^[a-z]{1,6}$')`                                                                              | Restreindre une saisie à n'importe quelles lettres minuscules (_jusqu'à 6 caractères_)                                                                                                                                                                                                                                                     |
| `regex(., '^[A-Z]{1,10}$')`                                                                             | Restreindre une saisie à n'importe quelles lettres majuscules (_jusqu'à 10 caractères_)                                                                                                                                                                                                                                                    |
| `regex(., '^(Apple\|Orange\|Banana)$')`                                                                 | Restreindre une saisie uniquement soit à `Apple` soit à `Orange` soit à `Banana`                                                                                                                                                                                                                                                        |
| `regex(., '^p(ea\|ai)r$')`                                                                              | Restreindre une saisie uniquement à `pear` ou `pair`                                                                                                                                                                                                                                                                                                 |
| `regex(., '^[A-Z]{1}[a-z]{1,}[ ]{1}[A-Z]{1}[a-z]{1,}$')`                                                | Restreindre une saisie du nom des bénéficiaires où les _initiales du prénom et du nom de famille sont en majuscules_ par exemple `Kobe Bryant`                                                                                                                                                                                                          |
| `regex(., '^\w{1,}\s(\w{1,})?(\s)?\w{1,}$')`                                                            | Restreindre une saisie du nom des bénéficiaires avec _prénom, deuxième prénom (le cas échéant) et nom de famille_ par exemple `Kobe Bean Bryant`                                                                                                                                                                                                  |
| `regex(., '^([A-Z]{1}[a-z]{1,}\s)([A-Z]{1}[a-z]{1,}\s?)+$')` ou `regex(., '^([A-Z]{1}[a-z]{1,}\s?)+$')` | Restreindre une saisie du nom complet des bénéficiaires où les _initiales des noms sont en majuscules_ et le nom est assez long (souvent supérieur à 3 mots) par exemple `Samayamantri Venkata Rama Naga Butchi Anjaneya Satya Krishna Vijay` (ceci est un exemple de noms du sud de l'Inde)                                                         |
| `regex(., '^(\D+)\s(\D+)\s?\1$')`                                                                       | Restreindre une saisie du prénom des bénéficiaires (afin de pouvoir capturer l'orthographe exacte) où les _enquêteurs sont obligés de saisir le prénom des bénéficiaires deux fois_ par exemple `Kobe Bryant Kobe`. (Cela pourrait être utile lorsque vous essayez de documenter les détails des bénéficiaires où une erreur de frappe pourrait vous coûter cher)      |
| `regex(., '^(\D+)\s(\D+)\s?\2$')`                                                                       | Restreindre une saisie du nom de famille des bénéficiaires (afin de pouvoir capturer l'orthographe exacte) où les _enquêteurs sont obligés de saisir le nom de famille des bénéficiaires deux fois_ par exemple `Kobe Bryant Bryant`. _(Cela pourrait être utile lorsque vous essayez de documenter les détails des bénéficiaires où une erreur de frappe pourrait vous coûter cher)_ |
| `regex(., '^colou?r$')`                                                                                 | Restreindre un caractère dans un mot en utilisant le `?` (quantificateur) par exemple autoriser soit `color` soit `colour` comme saisie                                                                                                                                                                                                         |
| `regex(., '^ah*!$')`                                                                                    | Restreindre un caractère dans un mot en utilisant le `*` (quantificateur) par exemple autoriser soit `a!` soit `ah!` soit `ahh!` soit `ahhh!` et ainsi de suite comme saisie                                                                                                                                                                                |
| `regex(., '^ah+!$')`                                                                                    | Restreindre un caractère dans un mot en utilisant le `+` (quantificateur) par exemple autoriser soit `ah!` soit `ahh!` soit `ahhh!` et ainsi de suite comme saisie                                                                                                                                                                                        |
| `regex(., '^\D$')`                                                                                      | Restreindre une saisie à un _caractère non numérique_ (par exemple `a` ou `c` ou `!` ou `#` ou `%` etc.)                                                                                                                                                                                                                                   |
| `regex(., '^\D{5 }$')`                                                                                  | Restreindre une saisie à _cinq caractères non numériques_ (par exemple `aZcB!#%` etc.)                                                                                                                                                                                                                                                      |
| `regex(., '^[A-Z\s]+$')`                                                                                | Restreindre toute la saisie de texte en majuscules, excluant les caractères spéciaux (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                                             |
| `regex(., '^[A-Z\W]+$')`                                                                                | Restreindre toute la saisie de texte en majuscules, incluant les caractères spéciaux (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                                             |
| `regex(., '^[a-z\s]+$')`                                                                                | Restreindre toute la saisie de texte en minuscules, excluant les caractères spéciaux (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                                             |
| `regex(., '^[a-z\W]+$')`                                                                                | Restreindre toute la saisie de texte en minuscules, incluant les caractères spéciaux (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                                             |

## Exemples liés à l'utilisation d'une combinaison de lettres et de nombres

| Regex XLSForm                                             | Description                                                                                                                                                                                                     |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex(., '^\w$')`                                        | Restreindre un caractère qui correspond entre `a` et `z` ou `A` et `Z` ou `0` et `9` ou `_` (c'est-à-dire correspondre à un caractère de `[a-zA-Z0-9_]`)                                                       |
| `regex(., '^\w{3}$')`                                     | Restreindre trois caractères qui correspondent entre `a` et `z` ou `A` et `Z` ou `0` et `9` ou `_` (c'est-à-dire correspondre à un caractère de `[a-zA-Z0-9_]`)                                                     |
| `regex(., '^[A-Z]{3}[_][A-Z]{3}[_][0-9]{4}[_][0-9]{4}$')` | Restreindre votre ID de bénéficiaire à un format spécifique par exemple `CAR_PRC_2020_0048`                                                                                                                      |
| `regex(., '^CAR-PRC-2020-[0-9]{4}$')`                     | Restreindre votre ID de bénéficiaire à un format spécifique par exemple `CAR-PRC-2020-0048` (_où les enquêteurs doivent saisir une correspondance exacte de `CAR` à `-` c'est-à-dire `CAR-PRC-2020-` et peuvent saisir n'importe quel numéro de série à 4 chiffres_) |
| <code>regex(., '^[\$&#x7c;\£]\d{3}$')</code>              | Restreindre une saisie de devise de _trois chiffres_ avec un symbole de devise (soit `dollar` soit `livre`) devant (par exemple `$999` ou `£500`)                                                                                  |
| `regex(., '^\W*(\w+\b\W*){3}$')`                          | Restreindre une saisie exacte du nombre de mots (par exemple pour restreindre exactement 3 mots `I love you.`)                                                                                                                     |
| `regex(., '^\W*(\w+\b\W*){3,5}$')`                        | Restreindre une saisie du nombre de mots (par exemple pour restreindre une plage de mots disons `3` à `5`)                                                                                                                         |

## Exemples liés à la restriction de saisies d'e-mails valides

<p class="note">Ces exemples sont purement illustratifs et doivent être ajustés pour votre cas d'utilisation. L'utilisation de regex pour contraindre les adresses e-mail ne garantit pas qu'elles sont valides, seulement qu'elles suivent un modèle attendu.</p>

| **Regex**                                                                                                          | **Description**                                                          |
| :----------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| `regex(., '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*(\.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)*\.[a-zA-Z]{2,}$')` | Restreindre la saisie à une adresse e-mail valide (par exemple, `example.domain.com` ou `example.domain.com.np`). |

## Exemples liés à l'utilisation de saisies d'heure

| **Regex**                                                | **Description**                           |
| :------------------------------------------------------- | :---------------------------------------- |
| `regex(., '^([00-23]{0,2}:[00-59]{0,2}:[00-59]{0,2})$')` | Restreindre une saisie d'heure au format `24` heures |
| `regex(., '^([00-12]{0,2}:[00-59]{0,2}:[00-59]{0,2})$')` | Restreindre une saisie d'heure au format `12` heures |

## Considérations lors de l'utilisation de regex

- Si vous souhaitez utiliser une contrainte regex sur un nombre dans une question de type `text`, assurez-vous d'avoir _toujours_ la valeur `numbers` sous la colonne `appearance`. Cela restreint l'affichage des lettres, rendant uniquement les nombres visibles pour les saisies.

- L'application Android Collect et Enketo se comportent différemment dans leur gestion des expressions regex. Collect se comporte comme si vous aviez utilisé les ancres `^` et `$` autour de l'expression (même si vous ne les avez pas utilisées), tandis qu'Enketo exige les ancres comme obligatoires pour une correspondance exacte.