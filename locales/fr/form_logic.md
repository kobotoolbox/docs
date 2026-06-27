# Introduction à la logique de formulaire dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/bc542b99d4fdd71ca6523665d625cdef49989ec5/source/form_logic.md" class="reference">21 Mar 2026</a>

La logique de formulaire contrôle le flux et le comportement de votre formulaire en fonction des réponses aux questions précédentes. Elle vous permet de créer des formulaires dynamiques qui s'adaptent aux saisies des utilisateurs. Par exemple, vous pouvez utiliser la logique de formulaire pour afficher certaines questions uniquement lorsqu'elles sont pertinentes, valider des réponses ou effectuer des calculs automatiquement.

Les principaux types de logique de formulaire sont les suivants :

- **Logique de saut :** Contrôle l'affichage ou le masquage des questions en fonction des réponses précédentes.
- **Critères de validation :** Valident les réponses pour s'assurer qu'elles respectent des règles ou des critères définis.
- **Sélections en cascade :** Affichent uniquement les options de réponse pertinentes en fonction des réponses précédentes.
- **Calculs :** Génèrent automatiquement des valeurs à l'aide d'expressions mathématiques ou logiques.
- **Logique de réponse obligatoire :** Définit quand une question doit obligatoirement recevoir une réponse.

<p class="note">
  Pour en savoir plus sur chaque type de logique de formulaire, consultez les articles d'aide sur la <a href="https://support.kobotoolbox.org/fr/skip_logic.html">logique de saut</a>, les <a href="https://support.kobotoolbox.org/fr/validation_criteria.html">critères de validation</a>, les <a href="https://support.kobotoolbox.org/fr/cascading_select.html">sélections en cascade</a>, la <a href="https://support.kobotoolbox.org/fr/question_options.html#setting-custom-logic-for-mandatory-responses">logique de réponse obligatoire</a> et les <a href="https://support.kobotoolbox.org/fr/calculate_questions.html">calculs</a> dans KoboToolbox.
</p>

Cet article présente les concepts clés de la logique de formulaire dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, notamment le référencement de questions, les constantes, les opérateurs, les fonctions et les expressions régulières, et explique comment les utiliser pour créer des formulaires dynamiques et réactifs.

## La logique de formulaire dans le Formbuilder KoboToolbox

Le Formbuilder KoboToolbox intègre des outils permettant d'ajouter de la logique de formulaire, tels que la [logique de saut](https://support.kobotoolbox.org/fr/skip_logic.html) et les [critères de validation](https://support.kobotoolbox.org/fr/validation_criteria.html). Ces outils conviennent à la plupart des cas d'utilisation standard, mais peuvent s'avérer limités pour des conditions plus complexes.

Pour la logique de saut et la validation, vous pouvez utiliser les **outils visuels du Formbuilder** ou **saisir manuellement des expressions XLSForm**. Pour cette deuxième option, il est utile de comprendre les bases de la syntaxe XLSForm, notamment le référencement de questions, les constantes, les opérateurs mathématiques et de comparaison, les opérateurs logiques pour combiner des conditions, les fonctions et les expressions régulières.

<p class="note">
Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html#">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

Si votre formulaire nécessite une logique complexe ou très personnalisée, il est recommandé de [télécharger votre formulaire en tant que XLSForm](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) et d'effectuer les modifications nécessaires directement dans le fichier Excel.

## Référencement de questions

Le référencement de questions vous permet d'intégrer la réponse à une question précédente dans le libellé ou la logique d'une question ultérieure. Le référencement de questions est fréquemment utilisé dans les formulaires avancés :

- **Dans les libellés ou les indices de questions :** Par exemple, vous pouvez inclure le prénom de l'enfant d'un répondant dans les questions ultérieures portant sur cet enfant.
- **Dans la logique de formulaire :** Par exemple, vous pouvez afficher ou masquer une question en fonction d'une réponse précédente, ou valider une réponse en la comparant à une réponse antérieure.

Le référencement de questions utilise le format `${data_column_name}`. Le [nom du champ](https://support.kobotoolbox.org/fr/question_options.html#data-column-name) d'une question peut être consulté et modifié dans les paramètres de la question.

Pour **afficher une réponse précédente dans le libellé d'une autre question**, insérez `${data_column_name}` directement dans le libellé de la question à l'endroit où vous souhaitez faire apparaître la valeur.

![Référencement de questions](images/form_logic/question_referencing.png)

Si une référence de question contient une erreur d'orthographe ou est incorrecte, un message d'erreur s'affichera lors de la prévisualisation ou de l'envoi du formulaire.

<p class="note">
<strong>Note :</strong> Lorsque vous référencez une question dans sa propre logique (par exemple, pour des critères de validation), un point <code>.</code> peut être utilisé comme raccourci.
</p>

## Stocker des constantes dans votre formulaire

Une **constante** est une valeur fixe qui ne change pas pendant la collecte de données. Les constantes sont utiles lorsque vous devez utiliser la même valeur plusieurs fois dans des calculs, comme un taux de conversion fixe, un seuil ou un multiplicateur.

Dans le Formbuilder, vous pouvez stocker une constante à l'aide du type de question Caché. Une question **Caché** n'apparaît pas dans le formulaire et ne possède pas d'élément d'interface utilisateur. Elle stocke en arrière-plan une valeur qui peut être référencée dans des questions de type **Calcul** plus loin dans le formulaire.

Pour stocker une constante dans votre formulaire :

1. Ajoutez une nouvelle question à votre formulaire.
2. Sélectionnez le type de question <i class="k-icon-qt-hidden"></i> **Caché**.
3. Ouvrez les <i class="k-icon-settings"></i>**Paramètres** de la question.
4. Dans le champ **Réponse par défaut**, saisissez la valeur de la constante.

![Option de question Caché](images/form_logic/hidden.png)

La valeur saisie dans le champ **Réponse par défaut** sera stockée en tant que constante. Vous pouvez ensuite référencer cette valeur en utilisant le [nom du champ](https://support.kobotoolbox.org/fr/question_options.html#data-column-name) de la question Caché dans les calculs et la logique de votre formulaire.

## Opérateurs mathématiques et de comparaison

Les **opérateurs mathématiques** sont utilisés pour effectuer des calculs arithmétiques à partir de valeurs numériques dans le formulaire. Les opérateurs mathématiques utilisés dans la logique de formulaire sont les suivants :

| Opérateur | Description |
|:---|:---|
| <code>+</code> | Addition |
| <code>-</code> | Soustraction |
| <code>*</code> | Multiplication |
| <code>div</code> | Division |
| <code>mod</code> | Modulo (reste d'une division) |

Les **opérateurs de comparaison** sont utilisés pour comparer des valeurs. Les opérateurs de comparaison utilisés dans la logique de formulaire sont les suivants :

| Opérateur | Description |
|:---------|:------------|
| <code>=</code>  | Égal à |
| <code>></code>  | Supérieur à |
| <code><</code>  | Inférieur à |
| <code>>=</code> | Supérieur ou égal à |
| <code><=</code> | Inférieur ou égal à |
| <code>!=</code> | Différent de |

## Combiner des conditions à l'aide d'opérateurs logiques

Les **opérateurs logiques** peuvent être utilisés dans la logique de formulaire pour combiner plusieurs conditions. Les opérateurs logiques sont les suivants :

- **and** (toutes les conditions doivent être remplies)
- **or** (au moins une des conditions doit être remplie)
- **not** (la ou les conditions ne doivent pas être remplies)

![Combiner des conditions avec des opérateurs logiques](images/form_logic/combine.png)

## Fonctions

Les fonctions sont des opérations prédéfinies utilisées pour effectuer des calculs ou manipuler des données dans la logique de formulaire. Elles rendent les calculs et la logique de formulaire plus efficaces en exécutant automatiquement des tâches complexes, comme arrondir des valeurs, calculer des puissances ou extraire la date actuelle.

<p class="note">
  Pour une liste complète des fonctions utilisables dans la logique de formulaire, consultez l'article <a href="https://support.kobotoolbox.org/fr/functions_xls.html">Utiliser des fonctions avec XLSForm</a>.
</p>

## Regex

Une expression régulière (regex) est un modèle de recherche utilisé pour identifier des caractères spécifiques dans une chaîne de texte. Elle est largement utilisée pour valider, rechercher, extraire et restreindre du texte dans la plupart des langages de programmation, y compris dans KoboToolbox.

La regex peut être utilisée dans les **critères de validation** pour contrôler la longueur et les caractères saisis dans une question (par exemple, limiter la saisie d'un numéro de téléphone à exactement 10 chiffres, contrôler le format des numéros d'identification ou vérifier la validité d'une adresse e-mail). Elle peut également être utilisée dans les **calculs** et d'autres éléments de logique de formulaire.

Dans KoboToolbox, les expressions régulières sont évaluées à l'aide de la fonction `regex(., ' ')`, où la regex est saisie entre apostrophes et le point `.` représente la question en cours. `regex(., ' ')` renvoie TRUE si l'expression régulière est satisfaite, et FALSE dans le cas contraire.

<p class="note">
  Pour en savoir plus sur l'utilisation de la regex dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/restrict_responses.html">Utiliser des expressions régulières avec XLSForm</a>.
</p>