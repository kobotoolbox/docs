# Introduction à la logique de formulaire dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/form_logic_xls.md" class="reference">20 mars 2026</a>

La logique de formulaire contrôle le flux et le comportement de votre formulaire en fonction des réponses aux questions précédentes. Elle vous permet de créer des formulaires dynamiques qui s'adaptent aux saisies des utilisateurs. Par exemple, vous pouvez utiliser la logique de formulaire pour afficher certaines questions uniquement lorsqu'elles sont pertinentes, valider des réponses ou effectuer des calculs automatiquement.

Les principaux types de logique de formulaire sont :
- **Logique de saut :** Contrôle l'affichage ou le masquage des questions en fonction des réponses précédentes.
- **Contraintes :** Valident les réponses pour s'assurer qu'elles respectent des règles ou des critères définis.
- **Filtres de choix :** Affichent uniquement les options de réponse pertinentes en fonction des réponses précédentes.
- **Calculs :** Génèrent automatiquement des valeurs à l'aide d'expressions mathématiques ou logiques.
- **Logique d'obligation conditionnelle :** Définit quand une question doit obligatoirement recevoir une réponse.

La logique de formulaire repose sur des **expressions**, qui combinent des **références de questions**, des **opérateurs**, des **fonctions** et des **constantes**. L'expression est évaluée comme TRUE ou FALSE pour contrôler le comportement du formulaire.

<p class="note">
  Cet article présente les composants de base de la logique de formulaire dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>, notamment le référencement de questions, les opérateurs et les fonctions. Pour en savoir plus sur chaque type de logique de formulaire, consultez les articles d'aide sur la <a href="https://support.kobotoolbox.org/fr/skip_logic_xls.html">logique de saut</a>, la <a href="https://support.kobotoolbox.org/fr/required_logic_xls.html">logique d'obligation conditionnelle</a>, les <a href="https://support.kobotoolbox.org/fr/constraints_xls.html">contraintes</a>, les <a href="https://support.kobotoolbox.org/fr/choice_filters_xls.html">filtres de choix</a> et les <a href="https://support.kobotoolbox.org/fr/calculations_xls.html">calculs</a> dans XLSForm.
</p>

## Référencement de questions

Le référencement de questions vous permet d'intégrer la réponse à une question précédente dans le libellé ou la logique d'une question ultérieure. Le référencement de questions est fréquemment utilisé dans les formulaires avancés :

- **Dans les libellés ou les indices de questions :** Par exemple, vous pouvez inclure le prénom de l'enfant d'un répondant dans les questions ultérieures portant sur cet enfant.
- **Dans la logique de formulaire :** Par exemple, vous pouvez afficher ou masquer une question en fonction d'une réponse précédente, ou valider une réponse en la comparant à une réponse antérieure.

Le référencement de questions utilise le format **${question_name}**, où `question_name` est remplacé par le nom unique de la question référencée.

Si une référence de question contient une erreur orthographique ou est incorrecte, un message d'erreur s'affichera lors de la prévisualisation ou de l'envoi du formulaire.

<p class="note">
  <strong>Note :</strong> Lorsqu'une question est référencée dans sa propre logique (c'est-à-dire dans sa propre ligne), un point <code>.</code> peut être utilisé comme raccourci.
</p>

**onglet survey**

| type     | name            | label                                                                 | constraint              |
|:-----------|:-----------------|:------------------------------------------------------------------------|:--------------------------|
| integer   | household_size  | How many people live in your household?                                |                          |
| integer   | total_under18   | Out of the ${household_size} people, how many are under the age of 18? | . < ${household_size}    |
| survey |

## Opérateurs mathématiques et de comparaison

Les **opérateurs mathématiques** sont utilisés pour effectuer des calculs arithmétiques à partir de valeurs numériques dans le formulaire. Les opérateurs mathématiques dans XLSForm sont :

| Opérateur | Description                     |
|:-----------|:---------------------------------|
| `+`       | Addition                        |
| `-`       | Soustraction                    |
| `*`       | Multiplication                  |
| `div`     | Division                        |
| `mod`     | Modulo (reste d'une division)   |

Les **opérateurs de comparaison** sont utilisés pour comparer des valeurs. Les opérateurs de comparaison dans XLSForm sont :

| Opérateur | Description                  |
|:-----------|:------------------------------|
| `=`       | Égal à                       |
| `>`       | Supérieur à                  |
| `<`       | Inférieur à                  |
| `>=`      | Supérieur ou égal à          |
| `<=`      | Inférieur ou égal à          |
| `!=`      | Différent de                 |

## Combiner des conditions à l'aide d'opérateurs logiques

Les **opérateurs logiques** peuvent être utilisés dans XLSForm pour combiner plusieurs conditions. Les opérateurs logiques dans XLSForm sont :
- **and** (toutes les conditions doivent être remplies)
- **or** (au moins une des conditions doit être remplie)
- **not** (la ou les conditions ne doivent pas être remplies)

**onglet survey**

| type     | name           | label                                | constraint                         |
|:-----------|:----------------|:--------------------------------------|:------------------------------------|
| integer   | household_size | How many people live in your household? |                                    |
| integer   | total_under18  | How many are under the age of 18?    | . < ${household_size} <strong>and</strong> . >= 0   |
| survey |

## Fonctions

Les fonctions sont des opérations prédéfinies utilisées pour effectuer des calculs ou manipuler des données dans XLSForm. Elles rendent les calculs et la logique de formulaire plus efficaces en automatisant des tâches complexes telles que l'arrondi de valeurs, le calcul de puissances ou l'extraction de la date actuelle.

<p class="note">
Pour une liste complète des fonctions dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/functions_xls.html">Utiliser des fonctions avec XLSForm</a>.
</p>

## Regex

Une expression régulière (regex) est un modèle de recherche utilisé pour identifier des caractères spécifiques dans une chaîne de texte. Elle est largement utilisée pour valider, rechercher, extraire et restreindre du texte dans la plupart des langages de programmation, y compris dans KoboToolbox.

La regex peut être utilisée dans les **contraintes** pour contrôler la longueur et les caractères saisis dans une question (par exemple, limiter la saisie d'un numéro de téléphone à exactement 10 chiffres, contrôler le format des numéros d'identification ou vérifier la validité d'une adresse e-mail). Elle peut également être utilisée dans les **calculs** et d'autres éléments de logique de formulaire.

Dans KoboToolbox, les expressions régulières sont évaluées à l'aide de la fonction `regex(., ' ')`, où la regex est saisie entre apostrophes et le point `.` représente la question en cours. `regex(., ' ')` renvoie TRUE si l'expression régulière est satisfaite, et FALSE dans le cas contraire.

<p class="note">
  Pour en savoir plus sur l'utilisation de la regex dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/restrict_responses.html">Utiliser des expressions régulières avec XLSForm</a>.
</p>