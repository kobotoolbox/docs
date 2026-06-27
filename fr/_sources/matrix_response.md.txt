# Ajouter une matrice de questions avec le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/matrix_response.md" class="reference">23 avr. 2026</a>

Le type de question **Tableau de questions** vous permet de créer un tableau structuré de questions, dans lequel chaque colonne représente une question et chaque ligne représente un élément. Plutôt que de créer plusieurs questions séparées, vous pouvez les regrouper dans une seule matrice afin de rendre votre formulaire plus organisé et plus efficace pour la collecte de données.

Cet article explique comment ajouter et configurer un tableau de questions dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, comment il s'affiche lors de la collecte de données, et comment appliquer une logique avancée à l'aide de XLSForm si nécessaire.

<p class="note">
<strong>Note :</strong> Les tableaux de questions sont disponibles uniquement dans les <a href="https://support.kobotoolbox.org/fr/data_through_webforms.html">formulaires web</a> avec le <a href="https://support.kobotoolbox.org/fr/alternative_enketo.html">thème Grille</a> activé. Ils ne sont pas disponibles dans KoboCollect.
</p>

## Ajouter un tableau de questions dans le Formbuilder

Pour ajouter un tableau de questions à votre formulaire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez une instruction générale comme libellé de la question.
3. Cliquez sur **+ AJOUTER UNE QUESTION.**
4. Choisissez le type de question <i class="k-icon-qt-question-matrix"></i> **Tableau de questions**.

![Tableau de questions](images/matrix_response/matrix.png)

### Configurer le tableau de questions

Dans votre tableau de questions :

- Chaque **colonne** représente une question distincte qui sera répétée pour chaque élément listé dans les lignes.
- Chaque **ligne** représente un élément sur lequel les questions des colonnes seront posées.

![Exemple de tableau de questions](images/matrix_response/example.png)

Pour configurer votre tableau de questions, pour chaque colonne :

1. Cliquez sur l'icône <i class="k-icon-settings"></i> **Paramètres**.
2. Sélectionnez le **Type de réponse**.
    - Les types disponibles sont **Choix unique**, **Choix multiple**, **Texte** et **Chiffre**.
    - Vous pouvez utiliser différents types de questions au sein d'une même matrice.
3. Saisissez un **Libellé de la question**.
4. Saisissez un **Suffixe du champ**. Ce suffixe sera ajouté aux noms de variables de chaque élément dans les lignes et doit respecter les [règles standard pour les noms de champs](https://support.kobotoolbox.org/fr/question_options.html#important-considerations-for-data-column-names).
5. Si vous utilisez **Choix unique** ou **Choix multiple**, ajoutez les choix de réponse et leurs [valeurs XML](https://support.kobotoolbox.org/fr/question_types.html#setting-xml-values-for-option-choices).
6. Définissez la question comme [obligatoire](https://support.kobotoolbox.org/fr/question_options.html#mandatory-response), si nécessaire.
7. Pour ajouter une autre colonne, cliquez sur l'icône <i class="k-icon-plus"></i> à droite de la dernière colonne.

<p class="note">
<strong>Note :</strong> Vous pouvez ajouter jusqu'à 12 colonnes à un tableau de questions. Cependant, chaque colonne supplémentaire réduit la largeur disponible pour les autres, ce qui peut affecter la lisibilité sur les écrans de petite taille.
</p>

Pour configurer chaque ligne :

1. Cliquez sur l'icône <i class="k-icon-settings"></i> **Paramètres**.
2. Saisissez un **Libellé** pour l'élément.
3. Saisissez un **Préfixe du champ**. Ce préfixe sera ajouté aux noms de variables de toutes les questions des colonnes associées à cet élément et doit respecter les [règles standard pour les noms de champs](https://support.kobotoolbox.org/fr/question_options.html#important-considerations-for-data-column-names).
4. Pour ajouter une autre ligne, cliquez sur l'icône <i class="k-icon-plus"></i> sous la dernière ligne.

## Collecter des données à partir d'un tableau de questions

Les tableaux de questions sont disponibles uniquement dans les formulaires web et nécessitent l'activation du [thème Grille](https://support.kobotoolbox.org/fr/alternative_enketo.html). Ils ne sont pas pris en charge dans KoboCollect.

Le tableau de questions s'affiche sous forme de tableau, chaque colonne représentant une question et chaque ligne représentant un élément.

![Tableau de questions](images/matrix_response/enketo.png)

<p class="note">
<strong>Note :</strong> Lors de l'export des données ou de la consultation des soumissions dans le tableau de données, les variables du tableau de questions sont converties en structure XLSForm standard. Chaque cellule de la matrice devient une variable individuelle, et les noms de variables finaux sont créés en combinant le <strong>préfixe du champ</strong> de la ligne et le <strong>suffixe du champ</strong> de la colonne. Par conséquent, les noms de variables exportés peuvent légèrement différer de la façon dont la matrice apparaît dans le Formbuilder.
</p>

## Tableaux de questions avancés

Il n'est pas possible d'ajouter des critères de validation, des calculs ou certaines options de questions avancées, comme la répétition d'un tableau de questions ou la définition d'un message de contrainte personnalisé, directement dans un tableau de questions **via le Formbuilder.**

Pour appliquer ces paramètres, [téléchargez votre formulaire](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) au format XLSForm et ajoutez des [contraintes](https://support.kobotoolbox.org/fr/constraints_xls.html), des [calculs](https://support.kobotoolbox.org/fr/calculations_xls.html) et d'autres [options de questions](https://support.kobotoolbox.org/fr/question_options_xls.html) directement dans le XLSForm.

<p class="note">
Pour un exemple d'ajout de contraintes et de calculs dans un tableau de questions, consultez cet <a href="https://support.kobotoolbox.org/_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx">XLSForm type</a>. Pour un exemple de répétition d'un tableau de questions sous forme de groupe répété, consultez cet <a href="https://support.kobotoolbox.org/_static/files/calculations_constraints_matrix/repeating_matrix_question.xlsx">XLSForm type</a>.
</p>

### Ajouter une logique de saut à un tableau de questions

De même, il n'est pas possible d'ajouter une logique de saut directement à un tableau de questions dans le Formbuilder. Vous pouvez toutefois [télécharger votre formulaire](https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) au format XLSForm et ajouter la logique de saut directement dans le XLSForm.

Lors de l'export vers XLSForm, un tableau de questions est structuré comme un groupe de questions utilisant les [valeurs w](https://support.kobotoolbox.org/fr/form_style_xls.html#setting-up-an-xlsform-for-theme-grid) du thème Grille. Vous pouvez [appliquer une logique de saut](https://support.kobotoolbox.org/fr/skip_logic_xls.html) à l'ensemble de la matrice en l'ajoutant au groupe entier, ou l'appliquer à des lignes individuelles au sein de la matrice.

Notez que l'ajout d'une logique de saut à des cellules individuelles peut affecter la mise en page visuelle de la matrice, car les questions masquées peuvent perturber la structure du tableau. Pour préserver la mise en forme, envisagez d'ajouter des questions de type **Note** avec une logique de saut qui affiche un message à la place de la question masquée, comme dans cet [XLSForm type](https://support.kobotoolbox.org/_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls). Cette approche maintient la mise en page de la matrice tout en empêchant la saisie dans des cellules spécifiques.

![Logique de saut dans un tableau de questions](images/matrix_response/skip_matrix.png)