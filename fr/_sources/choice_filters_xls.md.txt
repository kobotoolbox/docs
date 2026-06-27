# Ajouter des filtres de choix dans XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/1b55b2580defd73765e9c2ad608141a3428ee504/source/choice_filters_xls.md" class="reference">4 jan. 2026</a>

Les filtres de choix permettent de créer des formulaires dynamiques dans lesquels les options d'une question dépendent de la réponse à une question précédente. Cela simplifie la collecte de données en ne présentant que les choix pertinents, ce qui améliore l'efficacité et la précision de l'enquête.

Les filtres de choix peuvent être utilisés dans différents contextes, notamment :
- **Les listes hiérarchiques**, comme les continents et les pays, où la liste des pays dépend du continent sélectionné (également appelées **sélections en cascade**).
- **La suppression d'une ou plusieurs options d'une liste** si elles ne sont pas pertinentes pour un répondant en fonction de ses réponses précédentes.
- **La réutilisation d'une liste d'options** dans un XLSForm pour plusieurs questions, lorsque la liste varie légèrement d'une question à l'autre.
- La réutilisation d'une liste d'options d'une question précédente, en n'incluant **que les options sélectionnées par le répondant.**

Cet article explique comment ajouter des filtres de choix dans un XLSForm et présente des exemples pour différents cas d'utilisation. Les filtres de choix sont définis dans la colonne `choice_filter` de l'**onglet survey**, et mis en œuvre dans l'**onglet choices**.

<p class="note">
<strong>Note :</strong> Cet article porte sur l'ajout de filtres de choix dans <a href="https://support.kobotoolbox.org/fr/getting_started_xlsform.html">XLSForm</a>. Pour en savoir plus sur l'ajout de questions à sélection en cascade dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>, consultez l'article <a href="https://support.kobotoolbox.org/fr/cascading_select.html">Ajouter des questions à sélection en cascade dans le Formbuilder</a>.
<br><br>
Pour vous exercer à utiliser les filtres de choix dans XLSForm, consultez le <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">cours XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Ajouter des filtres de choix statiques

Les **filtres de choix statiques** appliquent les mêmes conditions de filtrage pour tous les répondants. Lorsque vous utilisez des filtres de choix statiques, une liste d'options est filtrée, mais elle ne varie pas en fonction des réponses précédentes. Cela peut être utile lorsque vous souhaitez réutiliser une liste d'options dans plusieurs questions de votre formulaire avec de légères variations, sans dupliquer la liste de choix plusieurs fois dans votre **onglet choices**.

Pour ajouter des filtres de choix statiques dans un XLSForm :
1. Ajoutez une question `select_one` ou `select_multiple` à votre XLSForm et [définissez vos choix de réponse](https://support.kobotoolbox.org/fr/option_choices_xls.html) dans l'**onglet choices**.
2. Dans l'**onglet choices**, ajoutez une colonne de filtre.
    - Vous pouvez nommer cette colonne comme vous le souhaitez (par exemple, `q2`).
3. Dans la colonne de filtre, saisissez une valeur quelconque (par exemple, `yes`) en regard du ou des choix que vous souhaitez inclure dans la liste de choix de votre question.
    - Cette valeur servira de filtre. Il peut s'agir de n'importe quel mot ou chiffre.
4. Dans l'**onglet survey**, ajoutez une colonne `choice_filter`. Cette colonne contiendra l'**expression de filtre de choix** utilisée pour filtrer les choix de réponse.
    - Dans sa forme la plus simple, l'expression de filtre de choix prend le format suivant : `filter = 'value'`.
    - Par exemple, `q2 = 'yes'` conservera tous les choix ayant la valeur **yes** dans la colonne `q2`.

### Exemple

Dans l'exemple ci-dessous, la même liste de choix (`activities`) est utilisée pour deux questions différentes. Pour la deuxième question, la liste est filtrée afin de n'afficher que les activités de plein air.

**onglet survey**

| type             | name               | label                                                   | choice_filter   |
|:-----------------|:------------------|:--------------------------------------------------------|:----------------|
| select_one activities | activities        | What activities do you enjoy doing in your free time?  |                 |
| select_one activities | outdoors_activities | Which of these outdoor activities are available in your city? | <strong>filter = 'outdoors'</strong> |
| survey |

**onglet choices**

| list_name  | name       | label                 | filter   |
|:-----------|:-----------|:--------------------|:---------|
| activities | reading    | Reading              |          |
| activities | swimming   | Swimming             | outdoors |
| activities | running    | Running              | outdoors |
| activities | television | Watching television  |          |
| activities | hiking     | Hiking               | outdoors |
| choices |

## Ajouter des filtres de choix dynamiques

Les filtres de choix peuvent également être utilisés pour filtrer une liste de choix en fonction d'une réponse précédente. Dans ce cas, vous aurez une **question principale** avec une **liste principale** de choix correspondante, et une **question secondaire** avec une **liste secondaire** de choix correspondante. La liste de choix de la question secondaire est filtrée en fonction de la réponse à la question principale.

<p class="note">
Pour un exemple de XLSForm utilisant des filtres de choix dynamiques, consultez ce <a href="https://docs.google.com/spreadsheets/d/10gpBV6YaYGx1i367hyW-w1Ms9tkUQnCx0V8YsdwYxmk/edit?gid=0#gid=0">formulaire type</a>.
</p>

Pour ajouter des filtres de choix dynamiques dans un XLSForm :
1. Ajoutez la **question principale** et la **question secondaire** à votre XLSForm et [définissez leurs choix de réponse](https://support.kobotoolbox.org/fr/option_choices_xls.html) dans l'**onglet choices**.
    - Ces questions doivent être de type `select_one` ou `select_multiple`.
2. Dans l'**onglet choices**, ajoutez une colonne de filtre.
    - Il peut être utile de nommer cette colonne de la même façon que la **question principale**.
3. Dans la colonne de filtre, saisissez le `name` du choix de la liste principale auquel correspond chaque option de la liste secondaire.
4. Dans l'**onglet survey**, ajoutez une colonne `choice_filter`. Cette colonne contiendra l'**expression de filtre de choix** utilisée pour filtrer les choix de réponse.
    - Si la question principale est de type `select_one`, l'expression de filtre de choix sera `filter_column = ${question_name}`, où `question_name` désigne la question principale.
    - Si la question principale est de type `select_multiple`, l'expression de filtre de choix sera `selected(${question_name}, filter_column)`.

Lorsqu'un répondant sélectionne une option dans la question principale, la liste de choix de la question secondaire est filtrée pour n'inclure que les choix correspondants.

### Exemple

Dans l'exemple ci-dessous, `continent` est la **question principale** et `country` est la **question secondaire**. La liste de choix de la question `country` sera filtrée en fonction de la réponse à la question `continent`.

**onglet survey**

| type              | name      | label     | choice_filter        |
|:------------------|:---------|:----------|:--------------------|
| select_one continent | continent | Continent |                     |
| select_one country   | country   | Country   | **continent = ${continent}** |
| survey |

**onglet choices**

| list_name  | name     | label   | continent |
|:-----------|:---------|:--------|:----------|
| continent  | africa   | Africa  |           |
| continent  | asia     | Asia    |           |
| country    | malawi   | Malawi  | africa    |
| country    | zambia   | Zambia  | africa    |
| country    | india    | India   | asia      |
| country    | pakistan | Pakistan| asia      |
| choices |

## Filtres de choix avancés dans XLSForm

Vous pouvez créer des filtres de choix plus avancés en utilisant des opérateurs logiques, des opérateurs mathématiques, des fonctions et des expressions régulières (regex) dans vos expressions de filtre de choix. Cela permet un filtrage des options hautement personnalisé et précis, adapté aux exigences spécifiques de collecte de données et aux caractéristiques des répondants.

<p class="note">
<strong>Note :</strong> Dans les expressions de filtre de choix avancées, la colonne <code>name</code> de l'<strong>onglet choices</strong> peut être utilisée comme colonne de filtre.
</p>

Voici des exemples d'expressions de filtre de choix avancées dans XLSForm :

| Filtre de choix | Description |
|:---------------|:------------|
| `selected(${parent_question}, name)` | Affiche uniquement les réponses qui ont été sélectionnées dans une `parent_question` précédente. |
| `filter = 'outdoors' and include = 'yes'` | Combine des expressions de filtre de choix de sorte que les deux conditions doivent être remplies pour que le choix soit affiché. |
| `name != 'none'` | Exclut l'option <strong>Aucun</strong> d'une liste de choix. |
| `selected(${Q1}, name) or name='none'` | Inclut les choix sélectionnés dans une question précédente ainsi qu'une option <strong>Aucun</strong> (même si elle n'a pas été sélectionnée précédemment). |
| `filter=${Q1} or name='other'` | Inclut les choix basés sur une question précédente ainsi qu'une option <strong>Autre</strong>. |
| `filter=${Q1} or always_include='yes'` | Inclut les choix basés sur une question précédente ainsi qu'un ensemble d'options qui doivent toujours être incluses. |
| `filter <= ${product_count}` | Utilise des chiffres dans la colonne de filtre au lieu de texte, et filtre en fonction d'un chiffre issu d'une question ou d'un calcul précédent. |
| `if(${relationship_status} = 'married', filter = 'married', filter = 'unmarried')` | Utilise des instructions conditionnelles pour afficher des choix de manière conditionnelle en fonction du profil du répondant. |

<p class="note">
  Pour en savoir plus sur la création d'expressions de logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

### Exemple

Dans l'exemple ci-dessous, la liste de choix sous-jacente pour `Q1` et `Q2` est identique, mais seules les options sélectionnées dans `Q1` seront affichées aux répondants lorsqu'ils répondront à `Q2`.

**onglet survey**

| type               | name | label                                              | choice_filter            |
|:------------------|:-----|:--------------------------------------------------|:-------------------------|
| select_multiple item | Q1  | Which household items do you currently own?      |                          |
| select_multiple item | Q2  | Which of these items would you consider upgrading in the future? | selected(${Q1}, name) |
| survey |

**onglet choices**

| list_name | name      | label            |
|:----------|:----------|:----------------|
| item      | fridge    | Refrigerator    |
| item      | tv        | Television      |
| item      | fan       | Ceiling fan     |
| item      | microwave | Microwave oven  |
| item      | radio     | Radio           |
| item      | bike      | Bicycle         |
| item      | phone     | Mobile phone    |
| item      | laptop    | Laptop computer |
| choices |

Dans le formulaire obtenu, `Q2` n'affichera que les options choisies dans `Q1`, comme illustré ci-dessous.

![Filtres de choix](images/choice_filters_xls/choice_filters.png)

## Résolution de problèmes

<details>
  <summary><strong>Le formulaire ralentit ou plante avec de très longues listes</strong></summary>
  Les listes de choix volumineuses contenant des milliers de lignes peuvent fonctionner en aperçu mais échouer lors du déploiement. Cela se produit parce que l'aperçu dans le navigateur peut gérer de grandes listes, contrairement à l'application mobile ou au parseur XLS. Pour résoudre ce problème, déplacez les grandes listes vers un fichier CSV externe et utilisez des <a href="https://support.kobotoolbox.org/fr/select_from_file_xls.html">questions select_from_file</a> avec des filtres de choix. Cette approche est recommandée pour les listes de plus de 3 000 options.
</details>

<br>

<details>
  <summary><strong>Noms d'options en double dans une liste</strong></summary>
  Si votre liste de choix contient des noms d'options en double (par exemple, si le même nom de quartier apparaît dans différentes villes), <a href="https://support.kobotoolbox.org/fr/form_settings_xls.html">activez les doublons de choix</a> dans l'<strong>onglet settings</strong> en définissant <code>allow_choice_duplicates</code> sur <code>yes</code>.
</details>