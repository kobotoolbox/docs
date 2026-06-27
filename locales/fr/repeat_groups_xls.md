# Groupes répétés dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/3256884be21cabd4238e7470299b347a34510d49/source/repeat_groups_xls.md" class="reference">23 Jun 2026</a>

Les groupes répétés dans XLSForm vous permettent de poser le même ensemble de questions plusieurs fois au sein d'un formulaire. Cette fonctionnalité est particulièrement utile pour collecter des informations similaires sur plusieurs personnes, éléments ou événements.

Par exemple, si vous recueillez des informations sur chaque membre d'un ménage, vous pouvez utiliser un groupe répété pour poser les mêmes questions démographiques pour chaque individu.

Cet article aborde les sujets suivants :
- Créer un groupe répété
- Définir un nombre de répétitions pour limiter le nombre de fois que le groupe est répété
- Compter le nombre de répétitions à l'intérieur d'un groupe répété
- Extraire des valeurs depuis des groupes répétés

<p class="note">
<strong>Note :</strong> Cet article porte sur les groupes répétés dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur les groupes répétés dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong> et pour voir des exemples de groupes répétés en action, consultez l'article <a href="https://support.kobotoolbox.org/fr/group_repeat.html">Groupes et groupes répétés dans le Formbuilder</a>.
</p>

## Créer un groupe répété

Pour créer un groupe répété dans XLSForm :

1. Dans la colonne `type` de l'onglet survey, saisissez `begin_repeat` pour indiquer le début du groupe répété.
2. Dans la colonne `name` de la ligne `begin_repeat`, saisissez l'identifiant unique du groupe.
3. Dans la colonne `label`, saisissez le titre du groupe tel que vous souhaitez qu'il apparaisse dans le formulaire. Le libellé est facultatif et peut être laissé vide.
4. Saisissez chaque question du groupe dans sa propre ligne, comme vous le feriez normalement.
5. Dans une nouvelle ligne après les questions répétées, saisissez `end_repeat` dans la colonne `type` pour indiquer la fin du groupe répété.
    - Dans la ligne `end_repeat`, laissez les colonnes `name` et `label` vides.

**onglet survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_repeat** | household_members | Household Members |
| text | name | What is the person's name? |
| integer | age | How old are they? |
| select_one yn | married | Are they married? |
| **end_repeat** | | |
| survey |

Les groupes répétés fonctionnent de manière similaire aux groupes de questions. Avec les groupes répétés, vous pouvez :

- Utiliser l'apparence `field-list` pour [afficher toutes les questions](https://support.kobotoolbox.org/fr/grouping_questions_xls.html#appearance-settings-for-question-groups) sur la même page.
- Ajouter une [logique de saut](https://support.kobotoolbox.org/fr/grouping_questions_xls.html#applying-skip-logic-to-question-groups) aux groupes répétés dans la colonne `relevant`.
- Créer des **sous-groupes répétés**, où un groupe répété est ajouté [à l'intérieur d'un autre](https://support.kobotoolbox.org/fr/grouping_questions_xls.html#nested-groups).

<p class="note">
  <strong>Note :</strong> L'ajout de groupes répétés à votre formulaire crée une structure de données différente de celle des variables ou groupes standard. Lorsque vous téléchargez vos données au format <code>.xlsx</code>, vous trouverez un onglet distinct pour chaque groupe répété. Pour plus d'informations sur l'export et l'utilisation des données de groupes répétés, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_repeat_groups.html">Gestion des données de groupes répétés</a>.
</p>

## Définir un nombre de répétitions

Par défaut, les groupes répétés peuvent être répétés autant de fois que nécessaire. Pour limiter le nombre de fois qu'un groupe répété est répété dans le formulaire, vous pouvez définir un nombre de répétitions. Le **nombre de répétitions** peut être soit un nombre fixe, soit déterminé dynamiquement en fonction d'une réponse précédente.

Pour définir un nombre fixe de répétitions :

1. Ajoutez une colonne `repeat_count` dans l'onglet survey.
2. Saisissez un nombre dans la colonne `repeat_count`.

**onglet survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| begin_repeat | participant_profile | Participant profile | 3 |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| survey |

Pour déterminer dynamiquement le nombre de répétitions en fonction d'une réponse précédente :

1. Ajoutez une colonne `repeat_count` dans l'onglet survey.
2. Saisissez la référence de la question dans la colonne `repeat_count`.
    - La question référencée doit être de type `integer`.

**onglet survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| integer | participants | Total number of training participants | |
| begin_repeat | participant_profile | Participant profile | ${participants} |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| survey |

<p class="note">
  <strong>Note :</strong> Dans la colonne <code>repeat_count</code>, vous pouvez également inclure des instructions conditionnelles avancées pour déterminer si les répétitions doivent se poursuivre. Pour plus d'informations, consultez la <a href="https://docs.getodk.org/form-logic/#repeating-as-long-as-a-condition-is-met">documentation ODK</a>.
</p>

## Compter le nombre de répétitions à l'intérieur d'un groupe répété

Lorsque vous utilisez des groupes répétés, vous pouvez avoir besoin d'un champ qui compte le nombre de fois que le groupe a été répété. Cela peut être utile pour des calculs ou la logique de formulaire. Par exemple, vous pouvez appliquer une logique de saut après une répétition spécifique ou inclure dynamiquement le numéro de répétition dans le libellé d'une question (ex. : Enfant 1, Enfant 2).

Pour compter le nombre de fois qu'un groupe répété a été répété :
1. Ajoutez une question de type `calculate` à l'intérieur du groupe répété.
2. Saisissez `position(..)` dans la colonne `calculation`.

Cette variable stocke l'index de répétition actuel. Vous pouvez l'utiliser dans la logique de formulaire ou pour créer des libellés de questions dynamiques.

**onglet survey**

| type | name | label | calculation | relevant |
| :--- | :--- | :--- | :--- | :--- |
| begin_repeat | profile | Participant profile | | |
| calculate | number | | **position(..)** | |
| note | instructions | Answer the questions below for each participant. | | **${number} = 1** |
| text | name | Name of participant **${number}** | | |
| select_one gender | gender | Gender of participant **${number}** | | |
| integer | age | Age of participant **${number}** | | |
| end_repeat | | | | |
| survey |

## Compter le nombre total de répétitions d'un groupe répété

Vous pouvez également ajouter une question distincte en dehors du groupe répété pour compter le nombre total de répétitions. Cela est utile, par exemple, pour confirmer le nombre de participants ou d'enfants répertoriés dans le groupe répété.

Pour compter le nombre de fois qu'un groupe répété a été rempli :
1. Ajoutez une question de type `calculate` après le groupe répété.
2. Dans la colonne `calculation`, saisissez `count(${repeat_group_name})`, où `repeat_group_name` est le nom du groupe répété.

Cette variable stocke le nombre total de répétitions du groupe. Vous pouvez l'utiliser dans des calculs ou pour créer des libellés de questions dynamiques dans votre formulaire.

**onglet survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Children roster | |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| calculate | count_children | | **count(${children})** |
| acknowledge | confirm_children | Confirm that there are **${count_children}** children in the household. | |
| survey |

## Extraire des valeurs depuis des groupes répétés

Les formulaires avancés utilisent souvent le [référencement de questions](https://support.kobotoolbox.org/fr/form_logic_xls.html#question-referencing) pour inclure des réponses à des questions précédentes dans des libellés de questions, des calculs ou une logique de saut. Vous pouvez également utiliser le référencement de questions **à l'intérieur des groupes répétés** ou pour faire référence à des données répétées ailleurs dans votre formulaire.

À l'intérieur d'un groupe répété, vous pouvez référencer la réponse d'une autre question de la même répétition à l'aide du référencement de questions, comme illustré ci-dessous.

**onglet survey**

| type | name | label |
| :--- | :--- | :--- |
| begin_repeat | children | Children roster |
| text | name | What is the child's name? |
| integer | age | How old is ${name}? |
| select_one gender | married | What is ${name}'s gender? |
| end_repeat | | |
| survey |

En dehors d'un groupe répété, vous pouvez extraire des données du groupe répété pour les utiliser dans la logique de formulaire ou les libellés de questions :

1. Ajoutez une question de type `calculate` après votre groupe répété.
2. Incluez l'une des formules listées ci-dessous dans la colonne `calculation`.
3. La question `calculate` stocke la valeur extraite, que vous pouvez ensuite utiliser dans la logique de formulaire ou les libellés de questions.

**Formules pour extraire des données depuis des groupes répétés**

| Formule | Description |
| :--- | :--- |
| `max(${question-name})` | Extrait la valeur maximale saisie pour une question dans le groupe répété. |
| `min(${question-name})` | Extrait la valeur minimale saisie pour une question dans le groupe répété. |
| `sum(${question-name})` | Calcule la somme des valeurs numériques saisies pour une question dans le groupe répété. |
| `join('; ', ${question-name})` | Liste toutes les réponses à une question donnée dans un groupe répété, séparées par un point-virgule. |
| `indexed-repeat(${question-name}, ${repeat-name}, n)` | Extrait la valeur de `${question-name}`, dans le groupe répété appelé `${repeat-name}`, à la n<sup>ième</sup> répétition. |

**onglet survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Children roster | |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| calculate | max_age | | **max(${age})** |
| acknowledge | confirm_age | Confirm that the oldest child in the household is **${max_age}** years old. | |
| survey |

## Résolution de problèmes

<details>
<summary><strong>Erreur KoboCollect : "Repeats in 'field-list' groups are not supported"</strong></summary>
Cette erreur se produit dans KoboCollect lorsqu'un groupe répété est imbriqué dans un groupe plus large qui utilise l'apparence <code>field-list</code>. KoboCollect ne permet pas d'utiliser les groupes répétés à l'intérieur de groupes <code>field-list</code>. Les groupes répétés doivent apparaître sur leur propre page.
<br><br>
Pour résoudre ce problème, déplacez le groupe répété en dehors du groupe principal, ou supprimez l'apparence <code>field-list</code> du groupe principal.
<br><br>
Ce problème ne concerne que KoboCollect et n'affecte pas les formulaires web.
</details>