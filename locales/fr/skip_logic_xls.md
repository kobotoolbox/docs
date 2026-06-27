# Ajouter une logique de saut dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/0586118b5f55f20287bc6db496832b14bbfc6239/source/skip_logic_xls.md" class="reference">5 Jun 2026</a>

La logique de saut, également appelée logique de pertinence, vous permet de **déterminer quand une question ou un groupe de questions sera affiché** dans le formulaire en fonction d'une réponse précédente ou du résultat d'un calcul. Par exemple, vous pouvez l'utiliser pour poser des questions de suivi uniquement à un sous-ensemble de répondants, ou pour masquer des sections entières d'un formulaire si elles ne sont pas pertinentes.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

Cet article couvre les sujets suivants :
- Ajouter une logique de saut à des questions individuelles
- Combiner plusieurs conditions de logique de saut
- Ajouter une logique de saut selon qu'une question a reçu une réponse ou non
- Ajouter une logique de saut à des groupes de questions

<p class="note">
  <strong>Note :</strong> Cet article porte sur l'ajout d'une logique de saut dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout d'une logique de saut dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/skip_logic.html">Ajouter une logique de saut dans le Formbuilder</a>.
    <br><br>
Pour une pratique concrète de la logique de saut dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des conditions de logique de saut à des questions individuelles

La logique de saut utilise le [référencement de questions](https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing) pour n'afficher que les questions pertinentes pour le répondant en fonction des réponses précédentes. La question utilisée pour définir la logique de pertinence est appelée la **question de référence**.

Pour ajouter une logique de saut dans XLSForm :
1. Ajoutez une colonne `relevant` à l'onglet survey.
2. Dans la ligne de la question que vous souhaitez afficher ou masquer, saisissez la condition qui doit être remplie **pour que la question soit affichée.**

**onglet survey**

| type         | name     | label             | relevant     |
|:--------------|:----------|:------------------|:--------------|
| integer       | age       | How old are you?  |               |
| select_one yn | married   | Are you married?  | ${age} > 18   |
| survey |

Dans l'exemple ci-dessus, `${age}` est la question de référence, et la réponse à `${age}` doit être supérieure à 18 pour que la question « Are you married? » soit affichée.

### Mise en forme des conditions de logique de saut

Le format de la condition de logique de saut varie selon le **type de la question de référence**, comme indiqué dans le tableau ci-dessous.

| Type de question de référence | Condition de logique de saut | Exemple |
|:-------------------------|:--------------------|:---------|
| select_one | `${reference_question} = 'choice_name'` | `${consent} = 'yes'` |
| select_multiple | `selected(${reference_question}, 'choice_name')` | `selected(${reasons}, 'other')` |
| integer | `${reference_question}` suivi d'un opérateur logique (>, <, =) et d'un nombre (ou d'une référence à une autre question) | `${age} >= 18` |
| date | `${reference_question}` suivi d'un opérateur logique (>, <, =) et de `date('YYYY-MM-DD')` | `${dob} >= date('1975-01-01')` |

<p class="note">
  Pour en savoir plus sur la construction d'expressions de logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

## Combiner plusieurs conditions de logique de saut

Plusieurs conditions de pertinence peuvent être combinées en une seule expression pour déterminer quand une question est affichée en fonction d'une réponse précédente. Les conditions peuvent être combinées à l'aide des opérateurs logiques `and`, `or` et `not` :

- Utilisez `and` lorsque toutes les conditions doivent être remplies pour qu'une question soit affichée.
    - Par exemple : <code>${age} > 18 <strong>and</strong> ${student} = 'no'</code>
- Utilisez `or` lorsqu'au moins une condition doit être remplie pour qu'une question soit affichée.
    - Par exemple : <code>${age} < 18 <strong>or</strong> ${student} = 'yes'</code>
- Utilisez `not` pour indiquer qu'une condition ou un ensemble de conditions ne doit pas être rempli (par exemple, lorsque deux conditions ne peuvent pas être vraies simultanément pour qu'une question soit affichée).
    - Par exemple : <code><strong>not</strong>(${age} > 18 <strong>and</strong> ${student} = 'yes')</code>

**onglet survey**

| type         | name     | label              | relevant                          |
|:--------------|:----------|:-------------------|:----------------------------------|
| integer       | age       | What is your age?  |                                   |
| select_one yn | employed  | Are you employed?  | ${age} >= 16 <strong>and</strong> ${age} <= 75     |
| survey |

## Ajouter une logique de saut selon qu'une question a reçu une réponse ou non

En plus d'ajouter une logique de saut basée sur une réponse spécifique, vous pouvez ajouter une logique de saut selon qu'une question a reçu une réponse ou a été laissée vide. Cela peut être utile pour ajouter des questions de suivi, ou lors de l'utilisation de [questions de type consentement](https://support.kobotoolbox.org/fr/select_one_and_select_many.html) dans votre formulaire.

Les questions sans réponse sont traitées comme des chaînes vides, notées par deux apostrophes simples `''`. Les conditions de logique de saut suivantes peuvent être utilisées :

| Condition de logique de saut | Description |
|:---------------------|:-------------|
| `${reference_question} != ''` | Afficher uniquement si `reference_question` a reçu une réponse (non vide). |
| `${reference_question} = ''` | Afficher uniquement si `reference_question` n'a pas reçu de réponse (vide). |

**onglet survey**

| type         | name      | label                | relevant             |
|:--------------|:-----------|:---------------------|:---------------------|
| text          | why_joined | Why did you join?    |                      |
| select_one yn | benefits   | Are you seeing benefits? | ${why_joined} != '' |
| survey |

## Ajouter des conditions de logique de saut à des groupes de questions

La logique de saut peut être appliquée aux groupes de questions ainsi qu'aux questions individuelles. Appliquer une logique de saut à un groupe affichera ou masquera toutes les questions de ce groupe en fonction des réponses précédentes.

Pour ajouter une logique de saut à des groupes de questions :
1. Ajoutez une colonne `relevant` à l'onglet survey.
2. Dans la ligne `begin_group` du groupe de questions que vous souhaitez afficher ou masquer, saisissez la condition qui doit être remplie **pour que le groupe soit affiché.**

**onglet survey**

| type         | name        | label                                         | relevant            |
|:-------------|:------------|:---------------------------------------------|:-------------------|
| select_one yn | joined     | Did you join the association?                |                     |
| begin_group  | association | Association participation                    | ${joined} = 'yes'  |
| date         | date_joined | When did you join the association?           |                     |
| select_one yn | voted      | Have you ever voted in any election for the association? |                     |
| end_group    |             |                                              |                     |
| survey |

## Résolution de problèmes
<details>
<summary><strong>La logique de saut ne fonctionne pas comme prévu avec les questions à choix multiple</strong></summary>
Lorsque vous ajoutez une logique de saut basée sur une question à choix multiple, l'utilisation de <code>${question} = 'option1'</code> ne fonctionnera que si l'option 1 est <strong>la seule réponse sélectionnée</strong>. Pour appliquer une logique de saut lorsque l'option 1 est sélectionnée, qu'il y ait ou non d'autres options également sélectionnées, utilisez la fonction <code>selected()</code> : <code>selected(${question}, 'option1')</code> <br><br>
Ce cas se présente fréquemment lors de l'ajout d'une question de texte libre « Précisez autre » après une question à choix multiple. Par exemple, si vous souhaitez que la question « Précisez autre » apparaisse chaque fois que « Autre » est sélectionné, utilisez : <code>selected(${question}, 'other')</code>

</details>