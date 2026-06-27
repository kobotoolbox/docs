# Ajouter des calculs et des contraintes dans un tableau de questions

Lorsque vous travaillez dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, il est simple d'[ajouter des calculs](calculate_questions.md) ou des [contraintes](validation_criteria.md) à presque tous les types de questions. Bien que le Formbuilder ne permette pas actuellement d'ajouter ces fonctionnalités à un tableau de questions, vous pouvez utiliser XLSForm pour ce faire. Les étapes décrites ci-dessous dans cet article d'aide illustrent comment ajouter des calculs et des contraintes à un tableau de questions à l'aide de XLSForm.

## Configurer la question et les champs

**Étape 1 : Créer un tableau de questions dans le Formbuilder**

La première étape consiste à créer un tableau de questions dans le Formbuilder (comme indiqué dans l'article d'aide [Ajouter une matrice de questions avec le Formbuilder](matrix_response.md)). Ajoutez simplement des lignes et des colonnes avec les variables nécessaires à la collecte de données.

**Étape 2 : Télécharger le formulaire en tant que XLSForm**

Une fois le tableau de questions créé, **ENREGISTREZ** le formulaire et [téléchargez-le en tant que XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Étape 3 : Ajouter une logique au tableau de questions**

Ouvrez le XLSForm et ajoutez les en-têtes de colonnes `calculation`, `constraint` et `constraint_message`. Grâce à ces en-têtes de colonnes, vous pourrez ajouter les expressions de _total par ligne_ et de _total par colonne_ sous l'en-tête de colonne `calculation`. Vous pouvez également ajouter les _contraintes_ appropriées sous l'en-tête de colonne `constraint` et le _message de contrainte_ sous l'en-tête `constraint_message` selon vos besoins.

De plus, vous pouvez choisir d'ajouter un en-tête de colonne `read_only` pour empêcher les enquêteurs de modifier les réponses lors de la collecte de données pour certaines questions (par exemple, le _total par ligne_ et le _total par colonne_ calculés automatiquement).

![Onglet survey](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  Dans l'image ci-dessus, vous remarquerez peut-être que les valeurs du champ <code>name</code> sont plus courtes. Dans cet exemple, elles ont été renommées par rapport à celles générées automatiquement dans le Formbuilder afin de capturer l'intégralité de la capture d'écran de l'onglet survey. Si vous choisissez de renommer les vôtres, veillez à utiliser vos nouveaux noms de variables dans les en-têtes de colonnes <code>calculation</code> et <code>constraint</code>. Si le formulaire a déjà été déployé et que des données ont été collectées, il est recommandé de <em>ne pas</em> renommer les variables existantes.
</p>

**Étape 4 : Remplacer le formulaire**

Importez et remplacez votre XLSForm dans le projet existant, ou créez un nouveau projet (si nécessaire).

**Étape 5 : Déployer le formulaire**

**Étape 6 : Collecter des données**

Après avoir déployé le formulaire, vous pouvez accéder à **FORMULAIRE > Collecter des données > OUVRIR** pour commencer à collecter des données avec le formulaire web.

## Visualiser le résultat

Les images suivantes illustrent l'apparence et le fonctionnement du formulaire dans le formulaire web Enketo après avoir suivi les étapes ci-dessus :

**Aucune donnée saisie :**

![Enketo sans saisie](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Une erreur de saisie est commise :**

![Enketo avec saisies incorrectes](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Ici, vous verrez qu'il y a au total cinq membres dans le ménage. Si un enquêteur saisit 6 pour le nombre de personnes de sexe masculin (0-14 ans), la contrainte affichera un message d'erreur.

**Aucune erreur de saisie :**

![Enketo avec saisies correctes](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Ici, lorsque vous saisissez des valeurs dans un tableau de questions, les totaux des lignes et des colonnes sont calculés automatiquement.

<p class="note">
  Vous pouvez télécharger le XLSForm utilisé pour cet article
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >ici</a
  >.
</p>

## Résolution de problèmes

-   Le tableau de questions fonctionne uniquement avec les **formulaires web Enketo**. Il n'est pas disponible avec l'**application Android KoboCollect**.

-   Le tableau de questions apparaîtra déformé si vous ne définissez pas la mise en page sur le thème **Grille**. Pour plus d'informations sur les apparences des formulaires web, consultez l'article [Styliser vos formulaires web dans le Formbuilder](alternative_enketo.md).