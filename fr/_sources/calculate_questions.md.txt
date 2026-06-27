# Ajouter des calculs avec le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/calculate_questions.md" class="reference">20 Mar 2026</a>

Les calculs permettent aux utilisateurs de dériver de nouvelles variables, de construire une logique de formulaire avancée et d'afficher des résultats aux répondants pendant la collecte de données. La question de type **Calcul** effectue des opérations mathématiques à partir des valeurs saisies dans les questions précédentes. Par défaut, le résultat est masqué, mais il peut être affiché dans le formulaire si nécessaire.

Les calculs sont traités au sein du formulaire, ce qui peut réduire la nécessité de manipuler les données après la collecte. Les résultats sont stockés en tant que nouvelles variables dans la base de données et peuvent être utilisés dans l'ensemble du formulaire pour appliquer une [logique de saut](https://support.kobotoolbox.org/fr/skip_logic.html), définir des [critères de validation](https://support.kobotoolbox.org/fr/validation_criteria.html) ou afficher du [contenu dynamique](https://support.kobotoolbox.org/fr/form_logic.html#question-referencing) dans les libellés de questions et les notes.

Cet article explique comment ajouter des calculs dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, en couvrant l'arithmétique de base et en présentant des expressions plus avancées.

## Ajouter des calculs avec le Formbuilder

Pour ajouter un calcul à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez l'expression de calcul à la place du libellé de la question.
3. Cliquez sur **+ ADD QUESTION**.
4. Choisissez le type de question <i class="k-icon-qt-calculate"></i> **Calcul**.

![Question de type Calcul](images/calculate_questions/calculate.png)

Les expressions de calcul sont construites à partir d'une combinaison de références à des questions, d'opérateurs mathématiques, de fonctions et de constantes. Par exemple :
* `${usd_cost} * 0.87` convertit la valeur saisie dans la question `usd_cost` dans une autre devise en utilisant un taux de change fixe.
* `${total_cost} div ${units_purchased}` divise le coût total par le nombre d'unités achetées pour calculer le coût unitaire.

<p class="note">
Pour en savoir plus sur chacun de ces composants, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic.html">Introduction à la logique de formulaire dans le Formbuilder</a>.
</p>

Pour afficher le résultat du calcul dans une note, utilisez le format de référencement de questions `${nom_champ}`, en remplaçant `nom_champ` par le [nom du champ](https://support.kobotoolbox.org/fr/question_options.html#data-column-name) de la question de type Calcul. Vous pouvez également utiliser ce format pour référencer le résultat du calcul dans le libellé d'une question ou dans la logique de votre formulaire.

![Référence à une question](images/calculate_questions/reference.png)

## Calculs arithmétiques

Les calculs peuvent aller de simples opérations arithmétiques à des dérivations de variables plus avancées.

Les calculs arithmétiques vous permettent d'effectuer des opérations de base à l'aide des **opérateurs** suivants :

| Opérateur | Description |
|:---------:|:------------|
| <strong>+</strong>        | addition |
| <strong>-</strong>        | soustraction |
| <strong>*</strong>        | multiplication |
| <strong>div</strong>      | division |
| <strong>mod</strong>      | modulo (calcule le reste d'une division) |

Les calculs dans XLSForm suivent la règle **BODMAS** pour l'ordre des opérations mathématiques : **P**arenthèses, **E**xposants, **D**ivision, **M**ultiplication, **A**ddition et **S**oustraction. Cela signifie que les calculs entre parenthèses sont effectués en premier, suivis des exposants, puis des divisions, des multiplications, et ainsi de suite. L'utilisation correcte des parenthèses garantit que vos calculs fonctionnent comme prévu.

## Calculs avancés

Les calculs avancés dans KoboToolbox reposent souvent sur des **fonctions** et des **expressions régulières** pour rendre les calculs plus efficaces.

- Les **fonctions** sont des [opérations prédéfinies](https://support.kobotoolbox.org/fr/functions_xls.html) utilisées pour effectuer automatiquement des tâches complexes telles qu'arrondir des valeurs, calculer des puissances ou extraire la date actuelle.
- Les **expressions régulières (regex)** sont des [modèles de recherche](https://support.kobotoolbox.org/fr/restrict_responses.html) utilisés pour identifier des caractères spécifiques dans une chaîne de texte.

<p class="note">
  Pour des exemples de calculs avancés utilisables dans vos formulaires et des suggestions de résolution de problèmes, consultez l'article <a href="https://support.kobotoolbox.org/fr/calculations_xls.html#advanced-calculations">Ajouter des calculs dans XLSForm</a>.
</p>