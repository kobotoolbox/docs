# Questions à choix multiple dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_one_and_select_many.md" class="reference">23 Apr 2026</a>

Les questions à choix multiple permettent aux répondants de **choisir parmi des options de réponse prédéfinies.** Elles sont utiles pour standardiser les réponses, améliorer la qualité des données et faciliter leur nettoyage, leur analyse et leur comparaison.

Selon vos besoins, les questions à choix multiple peuvent être utilisées pour sélectionner une ou plusieurs options, confirmer un consentement, classer des éléments par ordre, évaluer des éléments selon une échelle commune, ou sélectionner des options à partir d'un fichier externe.

Cet article présente les différentes questions à choix multiple disponibles dans KoboToolbox, explique comment les ajouter dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, décrit les options d'apparence disponibles et expose les points importants à prendre en compte lors de l'utilisation de ces types de questions.

## Types de questions à choix multiple

Les types de questions suivants sont disponibles dans le Formbuilder pour permettre aux répondants de sélectionner des options :

| Type de question | Description |
|:---|:---|
| <i class="k-icon-qt-select-one"></i> Choix unique | Permet aux répondants de sélectionner une option dans une liste prédéfinie. |
| <i class="k-icon-qt-select-many"></i> Choix multiple | Permet aux répondants de sélectionner plusieurs options dans une liste prédéfinie. |
| <i class="k-icon-qt-ranking"></i> Classement | Permet aux répondants de classer des éléments ou des options d'une liste de choix. |
| <i class="k-icon-qt-rating"></i> Notation | Permet aux répondants d'évaluer plusieurs éléments selon la même échelle de réponse. |
| <i class="k-icon-qt-acknowledge"></i> Consentement | Permet aux répondants de confirmer leur accord avec une déclaration. |
| <i class="k-icon-qt-select-one-from-file"></i> Choix unique à partir d'un fichier | Permet aux répondants de sélectionner une option dans une liste prédéfinie stockée dans un fichier CSV externe. |
| <i class="k-icon-qt-select-many-from-file"></i> Sélectionner plusieurs dans le fichier | Permet aux répondants de sélectionner plusieurs options dans une liste prédéfinie stockée dans un fichier CSV externe. |

<p class="note"> Pour en savoir plus sur les types de questions Choix unique à partir d'un fichier et Sélectionner plusieurs dans le fichier, consultez l'article <a href="https://support.kobotoolbox.org/fr/external_file.html">Sélectionner des options à partir de fichiers externes dans le Formbuilder</a>.
</p>

## Ajouter une question à choix multiple dans le Formbuilder

Pour ajouter une question à choix multiple à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ AJOUTER UNE QUESTION.**
4. Choisissez le type de question approprié.
6. Saisissez les choix de réponse pour la question à choix multiple.

![Types de questions dans le Formbuilder](images/select_one_and_select_many/select.png)

<p class="note">
    Pour en savoir plus sur la gestion des choix de réponse pour les questions à choix multiple dans le Formbuilder, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_types.html#adding-option-choices">Ajouter des questions avec le Formbuilder</a>.
</p>

### Configurer les questions de type Classement

Les questions de type **Classement** permettent de demander aux répondants de placer des éléments dans un ordre de préférence, d'importance ou de séquence.

Après avoir ajouté une question de type **Classement** dans le Formbuilder, configurez les composants suivants :

1. **Libellé de la question** : L'instruction générale pour la tâche de classement, par exemple « Sélectionnez votre premier et deuxième choix par ordre de préférence. »
2. **Nombre de rangs** : Par défaut, la question inclut uniquement un 1er choix. Cliquez sur le signe <i class="k-icon-plus"></i> sous le premier rang pour ajouter des rangs supplémentaires. Vous pouvez également modifier le libellé de chaque rang.
3. **Éléments à classer** : La liste des éléments que les répondants devront classer. Cliquez sur le signe <i class="k-icon-plus"></i> sous le dernier élément pour ajouter d'autres options.
4. **Message de contrainte** : Chaque élément ne peut être sélectionné qu'une seule fois. Si un répondant sélectionne le même élément plusieurs fois, un message d'erreur s'affiche indiquant « Items cannot be selected more than once. » Vous pouvez modifier ce message d'erreur par défaut sous la liste des éléments.

![Type de question Classement](images/select_one_and_select_many/ranking.png)

<p class="note">
<strong>Note :</strong> Vous pouvez inclure plus d'éléments que de rangs, mais le nombre de rangs ne peut pas dépasser le nombre d'éléments.
</p>

### Configurer les questions de type Notation

Les questions de type **Notation** sont utilisées lorsque vous avez plusieurs questions de type **Choix unique** qui partagent le même ensemble d'options de réponse, par exemple une échelle allant de « Pas du tout d'accord » à « Tout à fait d'accord ».

Après avoir ajouté une question de type **Notation** dans le Formbuilder, configurez les composants suivants :

- **Libellé de la question** : L'instruction générale pour l'ensemble de questions, par exemple « Évaluez les éléments suivants sur une échelle de 1 à 5. »
- **Lignes** : Les éléments, affirmations ou questions individuels que les répondants devront évaluer. Cliquez sur le signe <i class="k-icon-plus"></i> en bas du tableau pour ajouter des lignes.
- **Colonnes** : Les options de réponse qui composent l'échelle de notation, par exemple de « Pas du tout d'accord » à « Tout à fait d'accord ». Cliquez sur le signe <i class="k-icon-plus"></i> à droite du tableau pour ajouter des colonnes.

![Type de question Notation](images/select_one_and_select_many/rating.png)

## Apparences des questions à choix multiple

Le tableau ci-dessous présente les apparences par défaut pour les questions à choix multiple :

![Apparences de questions dans le Formbuilder](images/select_one_and_select_many/table.png)

<p class="note">
<strong>Note :</strong> Les types de questions <strong>Classement</strong> et <strong>Notation</strong> sont disponibles uniquement dans le Formbuilder de KoboToolbox. Si vous créez des formulaires avec XLSForm, l'apparence et le comportement du type de question <code>rank</code> différeront de la version du Formbuilder. Pour créer une question de type <strong>Notation</strong> dans XLSForm, ajoutez des questions à choix multiple avec les <a href="https://support.kobotoolbox.org/fr/appearances_xls.html#select-question-types">apparences</a> <code>label</code> et <code>list-nolabel</code>.
</p>

### Apparences avancées

Vous pouvez appliquer des apparences avancées aux questions de type **Choix unique, Choix multiple, Choix unique à partir d'un fichier** et **Sélectionner plusieurs dans le fichier** pour modifier leur affichage et leur comportement dans votre formulaire.

Pour ajouter une apparence avancée :

1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accéderez alors à l'onglet **Options des questions**.
2. Dans **Apparence (avancée)**, choisissez l'apparence souhaitée.
    - Si l'apparence n'est pas répertoriée, sélectionnez **other** et saisissez le nom de l'apparence dans la zone de texte, exactement tel qu'il est indiqué ci-dessous.

![Apparence avancée](images/select_one_and_select_many/appearance.png)

Les apparences avancées suivantes sont disponibles pour les questions de type **Choix unique, Choix multiple, Choix unique à partir d'un fichier** et **Sélectionner plusieurs dans le fichier** :

| Apparence | Description | Compatibilité |
|:---|:---|:---|
| `minimal` | Affiche les choix dans un menu déroulant.<br>![Apparence minimal](images/select_one_and_select_many/minimal.png) | Formulaires web et KoboCollect |
| `autocomplete` | Ajoute une barre de recherche en haut de la liste d'options.<br> ![Apparence autocomplete](images/select_one_and_select_many/autocomplete.png) | Formulaires web et KoboCollect (à combiner avec l'apparence `minimal`) |
| `likert` | Affiche les choix de réponse sous forme d'échelle de Likert (type **Choix unique** uniquement).<br>![Échelle de Likert](images/select_one_and_select_many/likert.png) | Formulaires web et KoboCollect |
| `compact` | Affiche les choix côte à côte avec un espacement minimal et sans cases de sélection visibles. Le nombre de choix par ligne peut varier selon la longueur du libellé de chaque option.<br>![Apparence compact](images/select_one_and_select_many/compact.png) | Formulaires web et KoboCollect |
| `quick` | Fait avancer automatiquement le formulaire à la question suivante après la sélection d'une réponse (type **Choix unique** uniquement). | KoboCollect uniquement |
| `quickcompact` | Affiche les choix côte à côte avec un espacement minimal et sans cases de sélection, et fait avancer automatiquement le formulaire à la question suivante après la sélection d'une réponse (type **Choix unique** uniquement). <br>![Apparence quick compact](images/select_one_and_select_many/compact.png) | KoboCollect uniquement |
| `horizontal` | Affiche les choix dans des colonnes de taille égale, avec le même nombre de choix par ligne. <br>![Apparence horizontal](images/select_one_and_select_many/horizontal_columns.png) | Formulaires web uniquement. Utilisez `columns` pour la compatibilité avec KoboCollect. |
| `columns` (other) | Affiche les choix dans des colonnes de taille égale, avec le même nombre de choix par ligne.<br>![Apparence columns other](images/select_one_and_select_many/horizontal_columns.png) | Formulaires web et KoboCollect. |
| `horizontal-compact` | Affiche les choix dans des colonnes avec des cases de sélection visibles. Le nombre de colonnes peut varier par ligne selon la longueur du libellé de chaque option.<br>![Apparence horizontal compact](images/select_one_and_select_many/horizontal-compact_columns-pack.png) | Formulaires web uniquement. Utilisez `columns-pack` pour la compatibilité avec KoboCollect. |
| `columns-pack` (other) | Affiche les choix dans des colonnes avec des cases de sélection visibles. Le nombre de colonnes peut varier par ligne selon la longueur du libellé de chaque option.<br>![Apparence columns pack](images/select_one_and_select_many/horizontal-compact_columns-pack.png) | Formulaires web et KoboCollect |
| `columns-n` (other) | Affiche les choix disponibles dans le nombre (n) de colonnes spécifié.<br>![Apparence columns-n](images/select_one_and_select_many/columns_n.png) | Formulaires web et KoboCollect |
| `label` | Affiche les libellés des choix sans les cases de sélection. | Formulaires web et KoboCollect |
| `list-nolabel` | Affiche les cases de sélection des choix sans les libellés. | Formulaires web et KoboCollect |

## Bonnes pratiques pour l'utilisation des questions à choix multiple

Les recommandations suivantes mettent en évidence les points importants à prendre en compte lors de l'utilisation des questions à choix multiple dans votre formulaire.

### Questions de type Consentement

Le type de question **Consentement** permet aux répondants d'indiquer leur accord avec une déclaration à l'aide d'une seule case à cocher. Cependant, ce type de question ne permet pas de distinguer les répondants qui sont activement en désaccord de ceux qui ignorent la question, ce qui peut affecter la qualité des données. De plus, le libellé par défaut du choix Consentement ne peut pas être modifié.

Si vous avez besoin de plus de flexibilité dans la formulation des options de réponse, ou si vous souhaitez inclure une option « Non » explicite, utilisez plutôt une question de type **Choix unique**.

### Définir les valeurs XML pour les choix

Il est fortement recommandé de définir les valeurs XML pour tous les choix des questions à choix multiple avant de déployer votre formulaire. Les valeurs XML garantissent la cohérence de votre base de données et évitent les problèmes lors de l'export et de l'analyse.

<p class="note"> Pour en savoir plus sur la définition des valeurs XML, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_types.html#setting-xml-values-for-option-choices">Ajouter des questions avec le Formbuilder</a>.
</p>

### Ajouter une option « Autre, précisez »

Si les choix prédéfinis ne couvrent pas toutes les réponses possibles, vous pouvez ajouter une option « Autre » suivie d'une [question de type Texte](https://support.kobotoolbox.org/fr/text_questions.html) permettant aux répondants de préciser leur réponse. Utilisez la logique de saut pour afficher la question de type Texte uniquement lorsque l'option « Autre » est sélectionnée.

<p class="note">
    Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/skip_logic.html#">Ajouter une logique de saut dans le Formbuilder</a>.
</p>

### Randomiser les choix de réponse

Pour les questions de type **Choix unique** et **Choix multiple**, vous pouvez randomiser l'ordre des choix de réponse en accédant aux **Paramètres > Options des questions > Paramètres** de la question et en sélectionnant **randomize.**

Vous pouvez également définir une **graine** (seed), qui garantit que la randomisation suit un schéma cohérent. L'utilisation d'une graine permet de reproduire le même ordre randomisé lorsque cela est nécessaire, par exemple lors de la consultation des soumissions ou du test du formulaire, tout en réduisant les biais liés à l'ordre lors de la collecte de données.

<p class="note">
    Pour en savoir plus sur les options de questions, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_options.html">Options de questions dans le Formbuilder</a>.
</p>

### Options d'export pour les questions de type Choix multiple

Lors de l'export des données pour les questions de type **Choix multiple**, vous pouvez choisir la structure des réponses dans votre base de données. Vous pouvez choisir de :

- Exporter toutes les options sélectionnées dans une seule colonne
- Exporter chaque option dans une colonne distincte
- Exporter les deux formats

<p class="note">
    Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/advanced_export.html#export-options-for-multiple-select-questions">Options avancées pour l'export des données</a>.
</p>