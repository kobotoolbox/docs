# Groupes de questions dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/grouping_questions_xls.md" class="reference">23 avr. 2026</a>

Regrouper des questions dans XLSForm permet d'organiser le contenu connexe en sections claires et structurées, améliorant ainsi la mise en page et la navigation dans le formulaire. Par exemple, vous pouvez regrouper toutes les questions démographiques dans une même section.

XLSForm facilite la création de groupes et de [sous-groupes](https://support.kobotoolbox.org/fr/grouping_questions_xls.html#nested-groups), ainsi que l'application d'une [logique de saut](https://support.kobotoolbox.org/fr/grouping_questions_xls.html#applying-skip-logic-to-question-groups) à des groupes de questions entiers. La logique de saut au niveau du groupe simplifie l'expérience du répondant en n'affichant que les sections pertinentes en fonction des réponses précédentes.

Cet article couvre les sujets suivants :

- Créer des groupes de questions et des sous-groupes dans XLSForm
- Afficher toutes les questions d'un groupe sur une seule page
- Ajouter une logique de saut à des groupes de questions

<p class="note">
<strong>Note :</strong> Cet article porte sur le regroupement de questions dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur le regroupement de questions dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/group_repeat.html">Groupes et groupes répétés dans le Formbuilder</a>.
</p>

## Créer un groupe de questions

Pour créer un groupe de questions dans XLSForm :

1.  Dans la colonne `type` de l'onglet survey, saisissez `begin_group` pour indiquer le début du groupe.
2.  Dans la colonne `name` de la ligne `begin_group`, saisissez l'identifiant unique du groupe.
3.  Dans la colonne `label`, saisissez le titre du groupe tel qu'il doit apparaître dans le formulaire. Le libellé est facultatif et peut être laissé vide.
4.  Saisissez chaque question du groupe dans sa propre ligne, comme vous le feriez normalement.
5.  Dans une nouvelle ligne après les questions du groupe, saisissez `end_group` dans la colonne `type` pour indiquer la fin du groupe.
    - Dans la ligne `end_group`, laissez les colonnes `name` et `label` vides.

<p class="note">
<strong>Note :</strong> Les noms de groupes dans la colonne <code>name</code> doivent être uniques et ne doivent pas reproduire le nom d'une question existante.
</p>

**onglet survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Section A : Informations personnelles |
| text | name | Quel est votre nom ? |
| integer | age | Quel est votre âge ? |
| select_one yn | married | Êtes-vous marié(e) ? |
| **end_group** | | |
| survey |

### Sous-groupes

Les sous-groupes sont des groupes de questions imbriqués à l'intérieur d'un autre groupe de questions. Ils permettent de créer une structure hiérarchique dans votre XLSForm. Par exemple, vous pouvez inclure un groupe de questions sur un enfant à l'intérieur d'un groupe plus large portant sur le ménage.

Lorsque vous créez plusieurs groupes, assurez-vous que chaque ligne `begin_group` possède une ligne `end_group` correspondante. Si le nombre de lignes `begin_group` ne correspond pas au nombre de lignes `end_group`, le formulaire génèrera une erreur qui l'empêchera de fonctionner correctement lors de la prévisualisation ou du déploiement.

**onglet survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Section A : Informations personnelles |
| text | name | Quel est votre nom ? |
| integer | age | Quel est votre âge ? |
| select_one yn | married | Êtes-vous marié(e) ? |
| **begin_group** | education | Éducation |
| select_one yn | student | Êtes-vous actuellement étudiant(e) ? |
| select_one edu | education_level | Quel est le niveau d'études le plus élevé que vous avez atteint ? |
| **end_group** | | |
| **end_group** | | |
| survey |

### Groupes répétés

Dans XLSForm, les groupes de questions peuvent être répétés afin de collecter le même ensemble de réponses plusieurs fois au sein d'un formulaire. Cela est utile lorsque vous recueillez des informations similaires sur plusieurs personnes, éléments ou événements. Les groupes répétés sont appelés **groupes répétés**.

<p class="note">
  Pour en savoir plus sur la configuration de groupes répétés dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/repeat_groups_xls.html">Groupes répétés dans XLSForm</a>.
</p>

## Paramètres d'apparence pour les groupes de questions

L'une des raisons courantes de regrouper des questions est de les afficher ensemble sur une seule page. Vous pouvez ajuster les paramètres d'apparence du groupe pour contrôler la façon dont les questions groupées sont affichées lors de la collecte de données. Les étapes varient selon que vous utilisez [KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html) ou des [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html).

<p class="note">
<strong>Note :</strong> Les paramètres d'apparence permettant d'afficher des groupes sur une seule page fonctionnent aussi bien pour les groupes de questions que pour les <a href="https://support.kobotoolbox.org/fr/repeat_groups_xls.html">groupes répétés</a>.
</p>

### Utiliser KoboCollect pour la collecte de données

Par défaut, KoboCollect affiche chaque question sur un écran distinct. Les utilisateurs doivent naviguer manuellement d'une question à la suivante.

Pour **afficher toutes les questions d'un groupe sur le même écran** dans KoboCollect :
1.  Dans l'onglet `survey`, ajoutez une colonne `appearance`.
2.  Dans la colonne `appearance`, saisissez `field-list` dans la ligne `begin_group`.
    * Chaque groupe de questions apparaîtra désormais sur sa propre page.

**onglet survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Section A : Informations personnelles | **field-list** |
| text | name | Quel est votre nom ? | |
| integer | age | Quel est votre âge ? | |
| select_one yn | married | Êtes-vous marié(e) ? | |
| end_group | | | |
| survey |

### Utiliser les formulaires web pour la collecte de données

Par défaut, les formulaires web affichent toutes les questions sur une seule page.

Pour afficher chaque groupe de questions sur sa propre page dans les formulaires web :
1.  Dans l'onglet `settings`, ajoutez une colonne `style`.
2.  Dans la deuxième cellule de la colonne `style`, saisissez `pages`.
    * Cela applique le [thème pages](https://support.kobotoolbox.org/fr/form_style_xls.html) à votre formulaire web, le divisant en pages distinctes, de façon similaire à KoboCollect.

**onglet settings**

| style |
| :--- |
| pages |
| settings |

3.  Dans l'onglet `survey`, ajoutez une colonne `appearance`.
4.  Dans la colonne `appearance`, saisissez `field-list` dans la ligne `begin_group`.
    * Chaque groupe de questions apparaîtra désormais sur sa propre page.

**onglet survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Section A : Informations personnelles | **field-list** |
| text | name | Quel est votre nom ? | |
| integer | age | Quel est votre âge ? | |
| select_one yn | married | Êtes-vous marié(e) ? | |
| end_group | | | |
| survey |

## Appliquer une logique de saut aux groupes de questions

Appliquer une logique de saut aux groupes de questions permet de n'afficher que les sections pertinentes en fonction des réponses précédentes. Par exemple, dans une enquête ménage, vous pouvez utiliser la logique de saut pour afficher un groupe de questions destiné au chef de ménage uniquement lorsqu'une question précédente identifie le répondant comme tel. Cela facilite la navigation dans le formulaire et le rend plus adaptatif aux saisies des utilisateurs.

Pour [appliquer une logique de saut](https://support.kobotoolbox.org/fr/skip_logic_xls.html) à des groupes de questions dans XLSForm, utilisez la même approche que pour les questions individuelles :
1.  Ajoutez une colonne `relevant` à votre onglet `survey`.
2.  Dans la colonne `relevant` de la ligne `begin_group`, saisissez la condition qui détermine quand le groupe doit être affiché.
3.  Si la condition est remplie, l'ensemble du groupe sera affiché. Dans le cas contraire, le groupe sera masqué.

Cela permet de contrôler le déroulement de votre formulaire afin que seules les sections pertinentes apparaissent en fonction des réponses précédentes, rendant le formulaire plus simple et plus adaptatif aux saisies des utilisateurs.

<p class="note">
<strong>Note :</strong> La logique de saut peut être appliquée aussi bien aux groupes de questions qu'aux <a href="https://support.kobotoolbox.org/fr/repeat_groups_xls.html">groupes répétés</a>. Pour en savoir plus sur la logique de saut dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/skip_logic_xls.html">Ajouter une logique de saut dans XLSForm</a>.
</p>