# Ajouter des critères de validation dans l'interface de création de formulaires
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/9c216c0650cac549ce4c2836cb5b8a588a47357a/source/validation_criteria.md" class="reference">2 oct. 2025</a>

<iframe src="https://www.youtube.com/embed/ya9usVpEo9Q?si=-rDzXcCRazcY0Bws" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La logique de validation, également appelée critères de validation ou contraintes, définit les conditions d'une réponse acceptable à une question. Cette fonctionnalité permet de garantir des données de haute qualité en empêchant les réponses accidentelles ou non valides.

Les critères de validation peuvent être appliqués à tout type de question. Par exemple, vous pouvez les utiliser pour vous assurer qu'un participant a plus d'un certain âge, qu'une date se situe dans une plage spécifique ou qu'une entrée de texte correspond à un certain modèle.

Il existe deux méthodes pour ajouter des critères de validation dans l'interface de création de formulaires : ajouter une condition via le **générateur de critères de validation**, ou saisir manuellement la logique de validation en **code XLSForm.**


## Ajouter une condition

Le générateur de critères de validation vous permet d'ajouter des conditions pour les questions de type **Texte**, **Nombre**, **Décimal** et **Date**. Il n'est pas compatible avec les questions **Sélectionner un** ou **Sélectionner plusieurs**. Pour utiliser le générateur :
1. Ouvrez les <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question.
2. Sélectionnez **Critères de validation**, et cliquez sur **Ajouter une condition.**
3. Choisissez l'opérateur logique approprié pour votre condition (par exemple, >, =, !=).
4. Dans le champ **valeur de réponse**, sélectionnez ou saisissez la valeur requise pour que la réponse soit valide.

<p class="note">
    <strong>Remarque :</strong> Pour ajouter des critères de validation aux questions de type <strong>Date</strong>, la valeur de réponse doit être au format <code>AAAA-MM-JJ</code>. Par exemple, pour définir un critère de validation pour une date antérieure au 1er janvier 2021, utilisez <code>< 2021-01-01</code>.
</p>

Pour ajouter plusieurs conditions (par exemple, une valeur minimale et une valeur maximale), ajoutez votre première condition, puis cliquez sur **Ajouter une autre condition.** Lorsque vous utilisez plusieurs conditions, spécifiez si au moins l'une de ces conditions doit être remplie ou si toutes doivent l'être. Vous pouvez supprimer des conditions en cliquant sur la <i class="k-icon-trash"></i> corbeille.

Si les conditions de validation ne sont pas remplies, la saisie ne sera pas acceptée lors de la collecte de données. Un [message d'erreur](#message-derreur) sera affiché.


## Saisir manuellement la logique de validation en code XLSForm
Pour les utilisatrices et utilisateurs avancés et pour les questions **Sélectionner un** ou **Sélectionner plusieurs**, les critères de validation peuvent être saisis directement en code XLSForm.

Pour saisir manuellement la logique de validation en code XLSForm, suivez ces étapes :
1. Ouvrez les <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question.
2. Sélectionnez **Critères de validation**, et cliquez sur **Saisir manuellement votre logique de validation en code XLSForm.**
3. Saisissez les critères en code XLSForm.

Dans la syntaxe XLSForm, un point `.` est utilisé pour faire référence à la question actuelle, et `${nom_question}` est utilisé pour faire référence à d'autres questions. Vous devrez également inclure l'opérateur logique pertinent et la valeur de réponse.

### Exemples de critères de validation

| Critères             | Description                                  |
| :------------------- | :------------------------------------------- |
| `. > 17`             | La réponse doit être supérieure à 17             |
| `. >= 17 and . <= 130` | La réponse doit être égale ou comprise entre 17 et 130          |
| `not(${in_university} = 'yes' and . < 16)` | Impossible de fournir une réponse inférieure à 16 si la réponse à `in_university` est « Oui »|
| `not(selected(., 'none') and count-selected(.)>1)`| Impossible de sélectionner « Aucun » et d'autres options dans une question Sélectionner plusieurs |


<p class="note">
    Pour plus d'informations sur le code XLSForm et les opérateurs, consultez la <a href="https://xlsform.org/en/#constraints">documentation XLSForm</a>.
</p>

## Message d'erreur
Le **message d'erreur** est un message facultatif que l'enquêtrice ou l'enquêteur ou la personne interrogée verra lorsqu'une réponse non valide est saisie. Il peut être défini en utilisant à la fois l'approche du **générateur de critères de validation** et l'approche du **code XLSForm**, en bas de la zone.

Si aucun message d'erreur n'est spécifié, le message par défaut est « Valeur non autorisée ». Les messages d'erreur personnalisés spécifient généralement les critères de validation pour aider la personne interrogée à corriger sa réponse (par exemple, « L'âge doit être supérieur à 18 ans »).