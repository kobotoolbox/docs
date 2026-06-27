# Ajouter une logique de saut à un tableau de questions

Dans la plupart des cas, vous pouvez ajouter une logique de saut à n'importe quel type de question, comme décrit dans l'article d'aide **[Ajouter une logique de saut dans le Formbuilder](skip_logic.md)**. Cependant, lorsque vous travaillez dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, il n'est pas encore possible d'ajouter une logique de saut à une question de type `matrix`. Il est toutefois possible d'utiliser un XLSForm pour implémenter une logique de saut pour ce type de question. Cet article d'aide illustre comment ajouter une logique de saut à une question `matrix` à l'aide d'un XLSForm.

Si vous avez consulté l'article d'aide **[Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)**, vous savez déjà qu'il existe 2 approches pour créer une question `matrix` dans KoboToolbox : l'_approche via le Formbuilder_ et l'_approche `kobo--matrix_list`_. Cet article d'aide présente les étapes nécessaires pour ajouter une logique de saut à une question `matrix` avec l'une ou l'autre de ces approches.

## Approche via le Formbuilder

Cette approche fonctionne avec **Enketo**, également connu sous le nom de **formulaires web**, en utilisant la **mise en page Thème grille**. Elle peut ne pas fonctionner comme prévu si vous ignorez les paramètres de **mise en page Thème grille** décrits dans l'article d'aide **[Styliser vos formulaires web dans le Formbuilder](alternative_enketo.md)**.

Suivez les étapes ci-dessous pour ajouter une logique de saut à une question `matrix` en utilisant l'approche via le Formbuilder.

**Étape 1 :** Créez une question `matrix` dans le Formbuilder :

La première étape consiste à créer une question `matrix` dans le Formbuilder, comme décrit dans l'article d'aide **[Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)**. Ajoutez simplement des lignes et des colonnes avec les variables pour lesquelles vous souhaitez collecter des données.

**Étape 2 :** Téléchargez le formulaire en tant que XLSForm :

Une fois la question `matrix` prête, **ENREGISTREZ** le formulaire, puis [téléchargez-le en tant que XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Étape 3 :** Ajoutez l'en-tête de colonne `relevant` et la logique de saut à votre XLSForm :

Ouvrez maintenant le XLSForm et ajoutez l'en-tête de colonne `relevant`. Une fois cet en-tête de colonne `relevant` ajouté, vous pourrez ajouter une logique de saut à toutes les questions selon vos besoins.

Pour améliorer l'affichage des questions `matrix` lors de la saisie des réponses, il est conseillé d'ajouter une question de type `note` (mise en évidence en jaune dans l'image ci-dessous) et d'y inclure une logique de saut appropriée. Cette étape est entièrement facultative, car elle n'affecte que la mise en forme de la question `matrix`. La différence entre l'_utilisation_ et la _non-utilisation_ du type de question `note` est illustrée ci-dessous à l'**Étape 6 : Collecter des données**.

![XLSForm approche Formbuilder](images/adding_skip_to_matrix/formbuilder_xlsform.png)

**Étape 4 :** Remplacez le XLSForm :

Importez et remplacez votre XLSForm dans le projet existant, ou créez un nouveau projet (si nécessaire).

**Étape 5 :** Déployez le formulaire :

Une fois le XLSForm remplacé (ou importé en tant que nouveau projet), vous devez déployer votre formulaire.

**Étape 6 :** Collectez des données :

Après avoir déployé le formulaire, vous pouvez accéder à **FORMULAIRE > Collecter des données > OUVRIR** pour commencer à collecter des données avec le formulaire web.

**Écran de saisie des données dans Enketo (formulaire web) : _lorsqu'aucune donnée n'est saisie_.**

![Formulaire Enketo vide — approche Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_empty.png)

**Écran de saisie des données dans Enketo (formulaire web) avec le type de question `note` ajouté : _lorsque la question `matrix` est remplie_.**

![Formulaire Enketo rempli — approche Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_no_issue.png)

Comme vous pouvez le voir dans l'image ci-dessus, la mise en forme de la question `matrix` n'a pas été altérée. C'est ainsi que le tableau `matrix` s'affichera lorsque vous utilisez le type de question `note` mis en évidence dans l'image partagée précédemment.

**Écran de saisie des données dans Enketo (formulaire web) sans le type de question `note` : _lorsque la question `matrix` est remplie_.**

![Formulaire Enketo rempli — approche Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_with_issue.png)

Dans ce cas, la mise en forme de la question `matrix` a été altérée. C'est ainsi que le tableau `matrix` s'affichera lorsque le type de question `note` n'est pas utilisé.

<p class="note">
  Vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls"
    >ici</a
  >
  utilisé pour cette approche
  <em
    >(ajout d'une logique de saut à une question <code>matrix</code> en utilisant
    l'approche via le Formbuilder)</em
  >.
</p>

## Approche `kobo--matrix_list`

Tout comme l'approche via le Formbuilder, cette méthode d'ajout de logique de saut avec un XLSForm fonctionne avec **Enketo** en utilisant la **mise en page Thème grille**.

Suivez les étapes ci-dessous pour ajouter une logique de saut à une question `matrix` avec un XLSForm en utilisant l'approche `kobo--matrix_list`.

**Étape 1 :** Créez une question `matrix` dans le XLSForm :

Créez une question `matrix` dans le XLSForm, comme décrit dans l'article d'aide **[Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)**.

**Étape 2 :** Ajoutez l'en-tête de colonne `relevant` et la logique de saut à votre XLSForm :

Une fois la question `matrix` prête, vous devez ajouter l'en-tête de colonne `relevant`. Vous pouvez maintenant ajouter une logique de saut à toutes les questions sous l'en-tête de colonne `relevant`.

![XLSForm approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_xlsform.png)

**Étape 3 :** Importez le XLSForm :

Si votre XLSForm est prêt, importez-le en tant que nouveau projet.

**Étape 4 :** Déployez le formulaire :

Une fois le XLSForm importé, vous devez déployer votre formulaire.

**Étape 5 :** Collectez des données :

Vous pouvez maintenant accéder à **FORMULAIRE > Collecter des données > OUVRIR** pour commencer à collecter des données.

**Écran de saisie des données dans Enketo (formulaire web) : _lorsqu'aucune donnée n'est saisie_.**

![Formulaire Enketo vide — approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_empty.png)

**Écran de saisie des données dans Enketo (formulaire web) : _lorsque la question `matrix` est remplie_.**

![Formulaire Enketo rempli — approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_filled.png)

Comme vous pouvez le voir dans la deuxième image, la mise en forme de la question `matrix` a été altérée. Avec l'approche `kobo--matrix_list`, vous ne disposez pas de l'espace nécessaire pour corriger le tableau `matrix` comme c'était possible avec l'approche via le Formbuilder.

<p class="note">
  Vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question_kobo_matrix.xls"
    >ici</a
  >
  utilisé pour cette approche
  <em
    >(ajout d'une logique de saut à une question <code>matrix</code> en utilisant
    l'approche <code>kobo--matrix_list</code>)</em
  >.
</p>