# Ajouter des critères de validation dans le Formbuilder
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/validation_criteria.md" class="reference">20 Mar 2026</a>


<iframe src="https://www.youtube.com/embed/ya9usVpEo9Q?si=-rDzXcCRazcY0Bws&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La logique de validation, également appelée critères de validation ou contraintes, définit les conditions qu'une réponse doit remplir pour être acceptée. Cette fonctionnalité contribue à garantir la qualité des données en empêchant les réponses accidentelles ou invalides.

Les critères de validation peuvent être appliqués à n'importe quel type de question. Vous pouvez par exemple les utiliser pour vérifier qu'un participant est au-dessus d'un certain âge, qu'une date se situe dans une plage spécifique, ou qu'une saisie de texte correspond à un certain format.

Il existe deux méthodes pour ajouter des critères de validation dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** : ajouter une condition via le **générateur de critères de validation**, ou saisir manuellement la logique de validation en **code XLSForm**.


## Ajouter une condition

Le générateur de critères de validation vous permet d'ajouter des conditions pour les questions de type **Texte**, **Chiffre**, **Décimale** et **Date**. Il n'est pas compatible avec les questions de type **Choix unique** ou **Choix multiple**. Pour utiliser le générateur :

1. Ouvrez <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question.
2. Sélectionnez **Validation**, puis cliquez sur **Ajouter une condition**.
3. Choisissez l'opérateur logique approprié pour votre condition (par exemple >, =, !=).
4. Dans le champ **valeur de réponse**, sélectionnez ou saisissez la valeur que la réponse doit avoir pour être considérée comme valide.

<p class="note">
    <strong>Note :</strong> Pour ajouter des critères de validation à des questions de type <strong>Date</strong>, la valeur de réponse doit être au format <code>YYYY-MM-DD</code>. Par exemple, pour définir un critère de validation exigeant qu'une date soit antérieure au 1er janvier 2021, utilisez <code>< 2021-01-01</code>.
</p>

Pour ajouter plusieurs conditions (par exemple une valeur minimale et une valeur maximale), ajoutez votre première condition, puis cliquez sur **Ajouter une autre condition**. Lorsque vous utilisez plusieurs conditions, précisez si au moins l'une d'entre elles doit être remplie ou si toutes doivent l'être. Vous pouvez supprimer des conditions en cliquant sur la corbeille <i class="k-icon-trash"></i>.

Si les conditions de validation ne sont pas remplies, la saisie ne sera pas acceptée lors de la collecte de données. Un [message d'erreur](#message-derreur) s'affichera.


## Saisir manuellement la logique de validation en code XLSForm

Pour les utilisateurs avancés et pour les questions de type **Choix unique** ou **Choix multiple**, les critères de validation peuvent être saisis directement en code XLSForm.

Pour saisir manuellement la logique de validation en code XLSForm, suivez ces étapes :

1. Ouvrez <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question.
2. Sélectionnez **Validation**, puis cliquez sur **Entrez manuellement votre logique de validation dans le code XLSForm**.
3. Saisissez les critères en code XLSForm.

Dans la syntaxe XLSForm, un point `.` est utilisé pour faire référence à la question en cours, et `${question_name}` (${nom_question}) est utilisé pour faire référence à d'autres questions. Vous devrez également inclure l'opérateur logique et la valeur de réponse appropriés.

### Exemples de critères de validation

| Critère | Description |
| :------------------- | :------------------------------------------- |
| `. > 17` | La réponse doit être supérieure à 17 |
| `. >= 17 and . <= 130` | La réponse doit être égale ou comprise entre 17 et 130 |
| `not(${in_university} = 'yes' and . < 16)` | Impossible de fournir une réponse inférieure à 16 si la réponse à `in_university` est « Yes » |
| `not(selected(., 'none') and count-selected(.)>1)` | Impossible de sélectionner « None » et d'autres options dans une question de type Choix multiple |


<p class="note">
    Pour plus d'informations sur le code XLSForm et les opérateurs, consultez l'article <a href="../fr/form_logic.html">Introduction à la logique de formulaire dans le Formbuilder</a>.
</p>

## Message d'erreur

Le **message d'erreur** est un message facultatif que l'enquêteur ou le répondant verra lorsqu'une réponse invalide est saisie. Il peut être défini aussi bien avec l'approche du **générateur de critères de validation** qu'avec l'approche du **code XLSForm**, en bas de la zone de saisie.

Si aucun message d'erreur n'est spécifié, le message par défaut est "Value not allowed". Les messages d'erreur personnalisés précisent généralement les critères de validation pour aider le répondant à corriger sa réponse (par exemple, « L'âge doit être supérieur à 18 »).