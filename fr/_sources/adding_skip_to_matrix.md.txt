# Ajouter une logique de saut à une question matricielle
<a href="../adding_skip_to_matrix.html">Read in English</a> | <a href="../es/adding_skip_to_matrix.html">Leer en español</a> | <a href="../ar/adding_skip_to_matrix.html">اقرأ باللغة العربية</a>

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/83d9dadfcc132d75f99e2705f77c425c2fee6d70/source/adding_skip_to_matrix.md" class="reference">11
mars 2022</a>

Dans la plupart des situations, vous pouvez ajouter une logique de saut à n'importe quel type de question comme indiqué dans l'article d'aide **[Ajouter une logique de saut](skip_logic.md)**. Cependant, lorsque vous travaillez dans l'interface de création de formulaires, il n'est pas encore possible d'ajouter une logique de saut à une question de type `matrix`. À la place, un XLSForm peut être utilisé pour implémenter une logique de saut pour ce type de question. Cet article d'aide illustre comment vous pouvez ajouter une logique de saut à une question `matrix` en utilisant XLSForm.

Si vous avez consulté l'article d'aide **[Type de réponse matricielle](matrix_response.md)**, vous savez déjà qu'il existe 2 approches pour créer une question `matrix` dans KoboToolbox : l'_approche par l'interface de création de formulaires_ et l'_approche `kobo--matrix_list`_. Cet article d'aide fournit un aperçu des étapes nécessaires pour ajouter une logique de saut à une question `matrix` en utilisant l'une ou l'autre de ces approches.

## L'approche par l'interface de création de formulaires :

Cette approche fonctionne avec **Enketo**, également connu sous le nom de **formulaires web**, en utilisant la **mise en page Grid-theme**. Elle peut ne pas fonctionner comme prévu si vous ignorez les paramètres de **mise en page Grid-theme** comme indiqué dans l'article d'aide **[Utiliser des styles alternatifs de formulaires web Enketo](alternative_enketo.md)**.

Suivez les étapes décrites ci-dessous pour ajouter une logique de saut à une question `matrix` en utilisant l'approche par l'interface de création de formulaires.

**Étape 1 :** Créer une question `matrix` dans l'interface de création de formulaires :

La première étape consiste à créer une question `matrix` dans l'interface de création de formulaires comme indiqué dans l'article d'aide **[Type de réponse matricielle](matrix_response.md)**. Ajoutez simplement des lignes et des colonnes avec les variables pour lesquelles vous avez l'intention de collecter des données.

**Étape 2 :** Télécharger le formulaire en tant que XLSForm :

Une fois que la question `matrix` est prête, **ENREGISTREZ** le formulaire puis [téléchargez-le en tant que XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Étape 3 :** Ajouter l'en-tête de colonne relevant et la logique de saut à votre XLSForm :

Ouvrez maintenant le XLSForm et ajoutez l'en-tête de colonne `relevant` au XLSForm. Une fois que vous avez l'en-tête de colonne `relevant`, vous pourrez ajouter une logique de saut à toutes les questions selon vos besoins.

Pour améliorer la façon dont les questions `matrix` sont affichées lors de la réponse, il est conseillé d'ajouter un type de question `note` (surligné en jaune dans l'image ci-dessous) puis d'y inclure une logique de saut selon les besoins. Ceci est entièrement optionnel car cela affectera simplement la mise en forme de la question `matrix`. La différence entre _l'utilisation_ et _la non-utilisation_ du type de question `note` est illustrée ci-dessous dans **Étape 6 : Collecter des données**.

![XLSForm approche interface de création de formulaires](images/adding_skip_to_matrix/formbuilder_xlsform.png)

**Étape 4 :** Remplacer le XLSForm :

Importez et remplacez votre XLSForm dans le projet existant, ou créez un nouveau projet (si nécessaire).

**Étape 5 :** Déployer le formulaire :

Une fois que vous avez remplacé le XLSForm (ou importé le XLSForm en tant que nouveau projet), vous devrez déployer votre formulaire.

**Étape 6 :** Collecter des données :

Après avoir déployé le formulaire, vous pouvez aller dans **FORMULAIRE>Collecter des données>OUVRIR** pour commencer à collecter des données avec le formulaire web.

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) : _lorsque rien n'est saisi_.**

![Formulaire Enketo vide approche interface de création de formulaires](images/adding_skip_to_matrix/formbuilder_enketo_form_empty.png)

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) avec le type de question `note` ajouté : _lorsque la question `matrix` est remplie_.**

![Formulaire Enketo rempli approche interface de création de formulaires](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_no_issue.png)

Comme vous pouvez le voir dans l'image ci-dessus, le format de la question `matrix` n'a pas été déformé. C'est ainsi que le tableau `matrix` sera affiché lorsque vous utilisez le type de question `note` qui a été surligné dans l'image partagée précédemment.

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) avec le type de question `note` non ajouté : _lorsque la question `matrix` est remplie_.**

![Formulaire Enketo rempli approche interface de création de formulaires](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_with_issue.png)

Dans ce cas, le format de la question `matrix` a été déformé. C'est le tableau `matrix` qui sera affiché lorsque le type de question `note` n'est pas utilisé.

<p class="note">
  Vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls"
    >ici</a
  >
  qui a été utilisé pour cette approche
  <em
    >(ajouter une logique de saut à une question <code>matrix</code> en utilisant l'approche par l'interface de création de formulaires)</em
  >.
</p>

## Approche `kobo--matrix_list` :

Tout comme avec l'approche par l'interface de création de formulaires, cette méthode d'ajout de logique de saut avec un XLSForm fonctionne avec **Enketo** en utilisant la **mise en page Grid-theme**.

Suivez les étapes ci-dessous pour ajouter une logique de saut à une question `matrix` avec un XLSForm en utilisant l'approche `kobo--matrix_list`.

**Étape 1 :** Créer une question `matrix` dans le XLSForm :

Créez une question `matrix` dans le XLSForm, comme indiqué dans l'article d'aide **[Type de réponse matricielle](matrix_response.md)**.

**Étape 2 :** Ajouter l'en-tête de colonne `relevant` et la logique de saut à votre XLSForm :

Une fois que la question `matrix` est prête, vous devez ajouter l'en-tête de colonne `relevant`. Vous pouvez maintenant ajouter une logique de saut à toutes les questions sous l'en-tête de colonne `relevant`.

![XLSForm approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_xlsform.png)

**Étape 3 :** Importer le XLSForm :

Si votre XLSForm est prêt, importez-le en tant que nouveau projet.

**Étape 4 :** Déployer le formulaire :

Une fois que vous avez importé le XLSForm, vous devrez déployer votre formulaire.

**Étape 5 :** Collecter des données :

Vous pouvez maintenant aller dans **FORMULAIRE>Collecter des données>OUVRIR** pour commencer à collecter des données.

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) : _lorsque rien n'est saisi_.**

![Formulaire Enketo vide approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_empty.png)

**Écran de saisie de données tel qu'il apparaît dans Enketo (formulaire web) : _lorsque la question `matrix` est remplie_.**

![Formulaire Enketo rempli approche kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_filled.png)

Comme vous pouvez le voir dans la deuxième image, le format de la question `matrix` a été déformé. Dans l'approche `kobo--matrix_list`, vous n'avez pas l'espace pour corriger le tableau `matrix` comme vous l'aviez avec l'approche par l'interface de création de formulaires.

<p class="note">
  Vous pouvez accéder au XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question_kobo_matrix.xls"
    >ici</a
  >
  qui a été utilisé pour cette approche
  <em
    >(ajouter une logique de saut à une question <code>matrix</code> en utilisant l'approche
    <code>kobo--matrix_list</code>)</em
  >.
</p>