# Ajouter des contraintes dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/c6f58131d275f1d56d26e1aaa599c31a3f1b53d5/source/constraints_xls.md" class="reference">24 Jun 2026</a>

Les contraintes, également appelées critères de validation, sont un type de logique de formulaire permettant de **restreindre les réponses acceptables à une question en fonction d'une condition prédéfinie**. Si la condition de contrainte n'est pas remplie, un message d'erreur personnalisable s'affiche, invitant l'utilisateur du formulaire à saisir une réponse valide.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

Cet article couvre les sujets suivants :
- Ajouter des contraintes aux questions dans XLSForm
- Combiner plusieurs conditions de contrainte
- Personnaliser les messages d'erreur de contrainte
- Contraintes avancées dans XLSForm

<p class="note">
  <strong>Note :</strong> Cet article porte sur l'ajout de contraintes dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de contraintes dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/validation_criteria.html?highlight=limiting">Ajouter des critères de validation dans le Formbuilder</a>.
<br><br>
Pour vous exercer à l'ajout de contraintes dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter une contrainte

Les contraintes sont construites à l'aide de [références de questions](https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing), d'[opérateurs de comparaison](https://support.kobotoolbox.org/fr/form_logic_xls.html#mathematical-and-comparison-operators) et de constantes. Les conditions de contrainte doivent être remplies pour valider ou envoyer un formulaire. Dans le cas contraire, un **message d'erreur** s'affiche et les utilisateurs ne peuvent pas passer à la page suivante ni envoyer le formulaire.

Pour ajouter des contraintes dans XLSForm :
1. Ajoutez une colonne `constraint` à l'**onglet survey**.
2. Dans la colonne `constraint`, définissez la condition qui doit être remplie **pour que la réponse soit valide.**
    - Utilisez un point `.` pour référencer la question de la ligne où vous ajoutez une contrainte.
    - Utilisez un [opérateur de comparaison](https://support.kobotoolbox.org/fr/form_logic_xls.html#mathematical-and-comparison-operators), suivi d'une valeur de référence, pour construire une contrainte simple.
    - Par exemple, `. > 18` restreint une question de type `integer` pour n'accepter que les valeurs supérieures à 18.

**onglet survey**

| type     | name       | label                                | constraint       |
|:---------|:-----------|:-------------------------------------|:----------------|
| integer  | age        | What is your age?                    | . >= 18         |
| integer  | household  | How many people live in your household? | . <= 30         |
| integer  | income     | Out of those, how many earn income?  | . <= ${household} |
| survey | 

### Formater les valeurs de référence
La valeur de référence dans une condition de contrainte doit correspondre au `type` de la question pour laquelle vous ajoutez une contrainte. Les formats de valeurs de référence pour les principaux types de questions sont listés ci-dessous :

| Type de question | Format de la valeur de référence                                      | Exemple                      |
|:----------------|:----------------------------------------------------------------------|:------------------------------|
| integer         | Nombre                                                                 | `. > 35`                     |
| select_one      | Nom du choix (tel que défini dans l'onglet choices) entre guillemets  | `. = 'yes'`                  |
| select_multiple | Nom du choix combiné avec la <a href="https://support.kobotoolbox.org/fr/functions_xls.html">fonction</a> `selected()` | `selected(., 'chair')`       |
| date            | Date au format `date('YYYY-MM-DD')`                                   | `. > date('2021-01-01')`    |
| text            | Texte entre guillemets (rarement utilisé pour les contraintes)        | `. != 'Not applicable'`      |

<p class="note">
  Pour en savoir plus sur la construction d'expressions de logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Combiner plusieurs conditions de contrainte
Plusieurs conditions de contrainte peuvent être combinées en une seule expression pour déterminer si une réponse est valide. Les conditions peuvent être combinées à l'aide des opérateurs logiques `and`, `or` et `not` :

- Utilisez `and` lorsque toutes les conditions doivent être remplies pour qu'une réponse soit valide.
    - Par exemple : <code>. > 18 <strong>and</strong> . < 65</code>
- Utilisez `or` lorsqu'au moins une condition doit être remplie pour qu'une réponse soit valide.
    - Par exemple : <code>. < 18 <strong>or</strong> ${student} = 'yes'</code>
- Utilisez `not` pour indiquer qu'une condition ou un ensemble de conditions ne doit pas être rempli (par exemple, lorsque deux conditions ne peuvent pas être vraies simultanément pour qu'une réponse soit valide).
    - Par exemple : <code><strong>not</strong>(. < 18 <strong>and</strong> ${household_head} = 'yes')</code>

**onglet survey**

| type     | name   | label              | hint                                        | constraint                                               |
|:---------|:-------|:------------------|:--------------------------------------------|:---------------------------------------------------------|
| integer  | age    | What is your age? | Must be less than 18 or above 65 to participate | <code>. < 18 <strong>or</strong> . > 65</code>         |
| integer  | weight | How much do you weigh? | Must be between 30 and 200 kg               | <code>. >= 30 <strong>and</strong> . <= 200</code>     |
| survey |


## Personnaliser les messages d'erreur de contrainte

Par défaut, lorsqu'une valeur de réponse dans le formulaire ne remplit pas la condition de contrainte, un message d'erreur « Value not allowed » s'affiche. Il est recommandé de personnaliser ce message pour informer les utilisateurs de la raison pour laquelle la valeur est invalide, leur permettant ainsi de corriger leur saisie.

Pour personnaliser le message d'erreur de contrainte :
1. Ajoutez une colonne `constraint_message` à l'**onglet survey**.
2. Dans la colonne `constraint_message`, saisissez le texte que vous souhaitez afficher comme message d'erreur lorsque les conditions de contrainte ne sont pas remplies.

**onglet survey**

| type    | name | label           | constraint | constraint_message     |
|:--------|:-----|:----------------|:-----------|:----------------------|
| integer | age  | What is your age? | . >= 18   | Must be older than 18. |

## Contraintes avancées dans XLSForm

Au-delà des contraintes de base, vous pouvez personnaliser les conditions pour garantir la qualité des données et vous adapter à de nombreux scénarios de collecte de données. Pour construire des conditions de contrainte plus avancées dans XLSForm :

- Utilisez des parenthèses pour combiner plus de deux conditions
- Utilisez des [fonctions](https://support.kobotoolbox.org/fr/functions_xls.html) pour plus de flexibilité
- Utilisez des [expressions régulières](https://support.kobotoolbox.org/fr/restrict_responses.html) pour restreindre les réponses de type texte

Voici des exemples de critères de validation plus avancés :

| Critère | Description |
|:---------|:------------|
| <code>(. >= 18 and . < 130) or (. = 999)</code> | La réponse doit être comprise entre 17 et 130 ou être égale à 999 (souvent utilisé pour les non-réponses). |
| <code>count-selected(.)<=3</code> | Limite la sélection multiple à trois options au maximum. |
| <code>not(${in_university} = 'yes' and . < 16)</code> | Si la réponse à `in_university` est 'yes', la réponse actuelle doit être supérieure à 16. |
| <code>not(selected(., 'none') and count-selected(.)>1)</code> | L'option 'none' ne peut pas être sélectionnée si une autre réponse dans une question `select_multiple` est déjà sélectionnée. |
| <code>. < today()</code> | La date saisie doit être antérieure à la date du jour. |
| <code>regex(., '^\d{2}$')</code> | La saisie est limitée à deux chiffres (à l'aide d'[expressions régulières](https://support.kobotoolbox.org/fr/restrict_responses.html)). |
| <code>decimal-time(.)>=0.5</code> | L'heure saisie doit être égale ou postérieure à 12h00. |