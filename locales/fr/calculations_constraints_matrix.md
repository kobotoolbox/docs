# Ajouter des calculs et des contraintes dans une question matricielle
<a href="../calculations_constraints_matrix.html">Read in English</a> | <a href="../es/calculations_constraints_matrix.html">Leer en español</a> | <a href="../ar/calculations_constraints_matrix.html">اقرأ باللغة العربية</a>

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/aaabdac8ec257d3157ec2ab2ceae65130e8c12d4/source/calculations_constraints_matrix.md" class="reference">14
avr. 2022</a>

Lorsque vous travaillez dans l'interface de création de formulaires, il est simple d'
[ajouter des calculs](calculate_questions.md) ou des
[contraintes](validation_criteria.md) à presque tous les types de questions. Bien que l'
interface de création de formulaires ne prenne actuellement pas en charge l'ajout de ces fonctionnalités à une question matricielle, vous pouvez utiliser XLSForm pour le faire. Les étapes énumérées ci-dessous dans cet article d'aide illustreront comment vous pouvez ajouter des calculs et des contraintes à une question matricielle en utilisant XLSForm.

## Configuration de la question et des champs

**Étape 1 : Créer une question matricielle dans l'interface de création de formulaires**

La première étape consiste à créer une question matricielle dans l'interface de création de formulaires (comme indiqué dans l'article d'aide [Type de réponse matricielle](matrix_response.md)). Ajoutez simplement des lignes et des colonnes avec les variables nécessaires pour la collecte de données.

**Étape 2 : Télécharger le formulaire en tant que XLSForm**

Une fois la question matricielle créée, **ENREGISTREZ** le formulaire et
[téléchargez-le en tant que XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Étape 3 : Ajouter de la logique à la question matricielle**

Ouvrez le XLSForm et ajoutez les en-têtes de colonnes `calculation`, `constraint` et `constraint_message`. Avec ces en-têtes de colonnes, vous pourrez ajouter les expressions de _total de colonne_ et _total de ligne_ sous l'en-tête de colonne `calculation`. Vous pouvez également ajouter des _contraintes_ appropriées sous l'en-tête de colonne `constraint` et un _message de contrainte_ sous l'en-tête `constraint_message` selon les besoins.

De plus, vous pouvez également choisir d'ajouter un en-tête de colonne `read_only` pour empêcher les enquêtrices et enquêteurs de modifier les réponses lors de la collecte de données pour certaines questions (par exemple, le _total de ligne_ et le _total de colonne_ qui sont calculés).

![Onglet Survey](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  Dans l'image ci-dessus, vous remarquerez peut-être que les entrées <code>name</code> sont plus courtes. Dans cet exemple, elles ont été renommées à partir de celles générées automatiquement dans l'interface de création de formulaires pour capturer la capture d'écran complète de l'onglet survey. Si vous choisissez de renommer les vôtres, assurez-vous d'utiliser vos nouveaux noms de variables dans les en-têtes de colonnes <code>calculation</code> et <code>constraint</code>. Si le formulaire a déjà été déployé et que des données ont été collectées, il est recommandé de <em>ne pas</em> renommer les variables existantes.
</p>

**Étape 4 : Remplacer le formulaire**

Importez et remplacez votre XLSForm dans le projet existant, ou créez un nouveau projet (si nécessaire).

**Étape 5 : Déployer le formulaire**

**Étape 6 : Collecter des données**

Après avoir déployé le formulaire, vous pouvez aller dans **FORMULAIRE>Collecte de données>OUVRIR** pour commencer à collecter des données avec le formulaire web.

## Visualisation du résultat

Les images suivantes illustrent comment le formulaire apparaîtra et fonctionnera dans le formulaire web Enketo après avoir suivi les étapes ci-dessus :

**Aucune donnée n'est saisie :**

![Enketo rien de saisi](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Une erreur de saisie est commise :**

![Enketo mauvaises entrées saisies](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Ici, vous verrez qu'il y a seulement cinq membres du ménage au total. Si une enquêtrice ou un enquêteur saisit 6 pour le nombre d'hommes (0-14 ans), la contrainte affichera un message d'erreur.

**Aucune erreur de saisie :**

![Enketo entrées correctes saisies](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Ici, lorsque vous saisissez des valeurs dans un tableau matriciel, les lignes et les colonnes sont automatiquement calculées.

<p class="note">
  Vous pouvez télécharger le XLSForm qui a été utilisé pour cet article
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >ici</a
  >.
</p>

## Dépannage

-   La question matricielle ne fonctionne qu'avec les **formulaires web Enketo**. Elle n'est pas prise en charge avec l'**application Android KoboCollect**.

-   Le tableau matriciel apparaîtra déformé si vous ne définissez pas la mise en page sur **Grid-theme**. Pour plus de détails sur l'apparence des formulaires web, vous pouvez consulter [Utilisation de styles alternatifs pour les formulaires web Enketo](alternative_enketo.md).