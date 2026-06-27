# Ajouter des calculs dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/calculations_xls.md" class="reference">23 avr. 2026</a>

Les calculs peuvent être utilisés dans votre formulaire pour dériver de nouvelles variables, construire une logique de formulaire avancée et afficher des résultats aux répondants pendant la collecte de données.

Les calculs sont traités au sein du formulaire, ce qui permet de gagner du temps lors de l'analyse des données. Les résultats sont stockés sous forme de nouvelles colonnes dans la base de données finale et peuvent être utilisés dans l'ensemble du formulaire pour appliquer une [logique de saut](https://support.kobotoolbox.org/fr/skip_logic_xls.html), définir des [contraintes](https://support.kobotoolbox.org/fr/constraints_xls.html) ou afficher du [contenu dynamique](https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing) dans les libellés de questions et les notes.

Cet article explique comment ajouter des calculs dans un XLSForm, en couvrant aussi bien l'arithmétique de base que les expressions plus avancées.

<p class="note">
<strong>Note :</strong> Cet article porte sur l'ajout de calculs dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour apprendre à ajouter des calculs dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/calculate_questions.html">Ajouter des calculs avec le Formbuilder</a>.
<br><br>
Pour vous exercer à utiliser les calculs dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des calculs dans XLSForm

Les expressions de calcul sont construites à partir d'une combinaison de [références de questions](https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing), d'[opérateurs mathématiques](https://support.kobotoolbox.org/fr/form_logic_xls.html#mathematical-and-comparison-operators), de [fonctions](https://support.kobotoolbox.org/fr/functions_xls.html) et de constantes.

Pour ajouter un calcul dans votre XLSForm :
1. Dans la colonne `type` de l'onglet survey, saisissez `calculate` pour ajouter un type de question calcul.
2. Saisissez un `name` pour la question `calculate`.
    - Étant donné que le calcul n'est pas affiché dans le formulaire, la question `calculate` **ne nécessite pas de libellé**.
3. Ajoutez une colonne `calculation` dans l'onglet survey.
4. Dans la colonne `calculation`, saisissez l'**expression de calcul**.
    - Les calculs peuvent aller de [calculs arithmétiques de base](https://support.kobotoolbox.org/fr/calculations_xls.html#arithmetic-calculations) à des [calculs avancés](https://support.kobotoolbox.org/fr/calculations_xls.html#advanced-calculations) utilisant des fonctions et des expressions régulières.

Pour faire référence au résultat du calcul dans le reste de votre formulaire (par exemple, dans une question de type note, un libellé de question ou une logique de formulaire), utilisez le format de [référencement de questions](https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing) `${nom_question}`, où `nom_question` est le nom de la question `calculate`.

**onglet survey**

| type      | name          | label                          | calculation           |
|:----------|:--------------|:-------------------------------|:----------------------|
| integer   | bags          | Nombre total de sacs vendus     |                       |
| decimal   | price         | Prix par sac                    |                       |
| calculate | total_amount  |                                | ${bags} * ${price}    |
| note      | display_total | Le total est ${total_amount}    |                       |
| survey |

## Calculs arithmétiques

Les calculs dans XLSForm peuvent aller de simples calculs arithmétiques à la dérivation avancée de variables.

Les calculs arithmétiques vous permettent d'effectuer des calculs de base à l'aide des **opérateurs** suivants :

| Opérateur | Description |
|:----------|:-------------|
| <strong>+</strong>   | Addition |
| <strong>-</strong>   | Soustraction |
| <strong>*</strong>   | Multiplication |
| <strong>div</strong> | Division |
| <strong>mod</strong> | Modulo (calcule le reste d'une division) |

Les calculs dans XLSForm suivent la règle **BODMAS** pour l'ordre des opérations mathématiques : **P**arenthèses, **E**xposants, **D**ivision, **M**ultiplication, **A**ddition et **S**oustraction. Cela signifie que les calculs entre parenthèses sont effectués en premier, suivis des exposants, puis des divisions, des multiplications, et ainsi de suite. L'utilisation correcte des parenthèses garantit que vos calculs fonctionnent comme prévu.

## Calculs avancés

Les calculs avancés dans XLSForm reposent souvent sur des **fonctions** et des **expressions régulières** pour les rendre plus efficaces.
* Les **fonctions** sont des opérations prédéfinies utilisées pour effectuer automatiquement des tâches complexes, comme arrondir des valeurs, calculer des puissances ou extraire la date actuelle.
* Les **expressions régulières (regex)** sont des modèles de recherche utilisés pour identifier des caractères spécifiques dans une chaîne de texte.

<p class="note">
  Pour une liste complète des fonctions disponibles dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/functions_xls.html">Utiliser des fonctions avec XLSForm</a>. Pour en savoir plus sur les expressions régulières, consultez l'article <a href="https://support.kobotoolbox.org/fr/restrict_responses.html">Utiliser des expressions régulières avec XLSForm</a>.
</p>

Voici des exemples de calculs avancés :

| Calcul | Description |
|:-------------|:-------------|
| `int((today()-${DOB}) div 365.25)` | Calculer l'âge à partir de la date de naissance. |
| `int(today()-${date})` | Calculer le nombre de jours depuis une date. |
| `format-date(${date}, '%b')` | Extraire uniquement le mois d'une date. |
| `concat(${first}, " ", ${middle}, " ", ${last})` | Créer une chaîne unique avec le nom complet d'un répondant. |
| `jr:choice-name(${question1}, '${question1}')` | Retourner le libellé d'un choix, dans la langue actuelle, à partir de la liste de choix. |
| `translate(${full_name}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "abcdefghijklmnopqrstuvwxyz_")` | Convertir les lettres majuscules en minuscules et les espaces en tirets bas. |
| `substr(${question}, 1, 2)` | Conserver uniquement la 1re lettre ou le 1er chiffre d'une chaîne. |
| `int(random()*10)` | Générer un nombre aléatoire entre 0 et 10. |
| `selected-at(${gps}, 0)` | Isoler la latitude à partir de coordonnées GPS. |
| `selected-at(${gps}, 1)` | Isoler la longitude à partir de coordonnées GPS. |
| `if(regex(${id}, '^ML-'), 'yes', 'no')` | Créer une variable binaire qui prend la valeur `yes` si l'identifiant du répondant commence par « ML- ». |

### Définir des réponses par défaut dynamiques

Le champ `calculation` peut également être utilisé pour définir des **réponses par défaut dynamiques**. Les réponses par défaut dynamiques permettent d'afficher une réponse par défaut dans une question en fonction d'une réponse précédente.

Pour définir une réponse par défaut dynamique :
1. Dans la colonne `calculation`, saisissez la **référence à la question** qui alimentera dynamiquement la réponse par défaut.
2. Dans la colonne `trigger`, saisissez la question qui activera le calcul.
    - En général, il s'agit de la même question référencée dans la colonne `calculation`, de sorte que toute modification apportée à la question déclencheur mettra également à jour la réponse par défaut.

**onglet survey**

| type | name       | label                     | calculation | trigger     |
|:------|:-----------|:--------------------------|:-------------|:-------------|
| text  | hh_name    | Nom du chef de ménage     |             |              |
| text  | phone      | Numéro de téléphone du ménage |          |              |
| text  | phone_name | Nom du propriétaire du téléphone | ${hh_name} | ${hh_name} |
| survey |

<p class="note">
<strong>Note :</strong> Si vous souhaitez empêcher les utilisateurs de modifier le champ, définissez la colonne <code>read_only</code> comme <code>TRUE</code>.
</p>

## Résolution de problèmes

<details>
  <summary><strong>Recommandations pour la résolution de problèmes</strong></summary>
  Pour faciliter la résolution de problèmes, affichez les résultats des calculs dans une note pendant le développement de votre formulaire. Cela permet de vérifier si le calcul s'évalue correctement et facilite l'identification des problèmes. Vous pouvez également décomposer les expressions longues en expressions plus courtes et afficher le résultat de chacune pour localiser les erreurs.
</details>

<br>

<details>
  <summary><strong>Les calculs ne fonctionnent pas correctement</strong></summary>
  Si vos calculs ne fonctionnent pas, vérifiez les points suivants :
  <ul>
  <li><strong>Syntaxe :</strong> toutes les parenthèses ouvertes sont fermées, des guillemets droits <code>'</code> sont utilisés et des virgules sont incluses là où elles sont nécessaires.</li>
  <li><strong>Références :</strong> les références de questions correspondent exactement au nom de la question, sans espaces ni fautes de frappe, et sans références circulaires (c'est-à-dire que le calcul ne dépend pas de lui-même).</li>
  <li><strong>Types de données :</strong> les calculs numériques et les calculs sur des chaînes de texte ne sont pas combinés dans la même question, et les types de données sont utilisés correctement.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Gestion des champs vides</strong></summary>
  Les questions sans réponse sont traitées comme des chaînes vides et ne sont pas automatiquement converties en zéro. Lorsqu'une valeur vide est utilisée dans un calcul, le résultat est « Not a Number » (NaN). Pour convertir les valeurs vides en zéro dans les calculs, utilisez les <a href="https://support.kobotoolbox.org/fr/functions_xls.html">fonctions</a> <code>coalesce()</code> ou <code>if()</code>. Par exemple :
  <ul>
  <li><code>coalesce(${potentially_empty_value}, 0)</code></li>
  <li><code>if(${potentially_empty_value}="", 0, ${potentially_empty_value})</code></li>
</ul>
  Une autre option consiste à définir des valeurs par défaut égales à 0 pour chacune des variables numériques dans la colonne <code>default</code>.
</details>

<br>

<details>
  <summary><strong>Division par zéro</strong></summary>
  Si un calcul inclut une division et que le diviseur est égal à zéro, le résultat est géré différemment dans les formulaires web et dans KoboCollect. Dans les formulaires web, une division par zéro est ignorée. Dans KoboCollect, la valeur calculée sera <code>Infinity</code>, ce qui peut entraîner des problèmes dans les rapports de données et lors du traitement des données exportées. Pour éviter cela, ajoutez une logique de saut afin que le calcul ne s'exécute pas lorsque le diviseur est égal à zéro, ou appliquez une contrainte pour empêcher la variable diviseur d'être égale à zéro.
</details>

<br>

<details>
  <summary><strong>Les calculs changent continuellement dans le formulaire</strong></summary>
  Les expressions sont réévaluées au fur et à mesure qu'un enquêteur progresse dans un formulaire. Cela est particulièrement important pour les <a href="https://support.kobotoolbox.org/fr/functions_xls.html">fonctions</a> non liées à des champs du formulaire, telles que <code>random()</code> ou <code>now()</code>, dont les valeurs peuvent changer dans ces conditions.
<br><br>
Les expressions sont réévaluées dans les cas suivants :
  <ul>
  <li>Un formulaire est ouvert</li>
  <li>La valeur d'une question utilisée dans le calcul change</li>
  <li>Un groupe répété est ajouté ou supprimé</li>
  <li>Un formulaire est sauvegardé ou finalisé</li>
</ul>
  Pour contrôler le moment où une expression est évaluée, définissez un <a href="https://support.kobotoolbox.org/fr/question_options_xls.html#additional-question-options">trigger</a> afin qu'elle ne soit évaluée que lorsqu'une question donnée reçoit une réponse, ou utilisez la fonction <code>once()</code> pour vous assurer que l'expression n'est évaluée qu'une seule fois (par exemple, <code>once(random())</code> ou <code>once(today())</code>).
</details>