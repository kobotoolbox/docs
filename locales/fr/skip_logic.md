# Ajouter une logique de saut dans l'interface de création de formulaires
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/0d832566f7fb9d5e452c73468e52ec242eac992f/source/skip_logic.md" class="reference">30 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/uLSnoG0mqV4?si=63o4YeQUZWOsZmfF" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La logique de saut, également appelée branchement ou conditions de pertinence, contrôle quelles questions sont affichées dans un formulaire. Par défaut, toutes les questions sont visibles. La logique de saut détermine sous quelle(s) condition(s) une question doit apparaître. Les conditions de logique de saut sont toujours appliquées à la question ou au groupe qui doit être visible de manière conditionnelle.

<p class="note">
    <strong>Remarque :</strong> Vous pouvez appliquer une logique de saut à des <a href="group_repeat.html">groupes de questions</a> entiers ainsi qu'à des questions individuelles. Cela peut simplifier la logique du formulaire et faciliter la gestion de questionnaires complexes.
</p>

Il existe deux méthodes pour ajouter une logique de saut dans l'interface de création de formulaires : ajouter une condition via le **générateur de logique de saut**, ou saisir manuellement la logique de saut en **code XLSForm**.

## Ajouter une condition

Cette première méthode vous permet d'utiliser le générateur de logique de saut pour ajouter vos conditions. Elle est recommandée pour les débutantes et débutants. Pour ajouter une condition de logique de saut, suivez ces étapes :

1. Ouvrez les <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question ou du groupe à afficher de manière conditionnelle.
2. Sélectionnez **Logique de saut**, et cliquez sur **Ajouter une condition**.
3. Sélectionnez la question dans le formulaire qui déterminera si la question actuelle est affichée ou non.
4. Choisissez l'opérateur logique approprié pour votre condition (par exemple, >, =, !=).
5. Dans le champ **valeur de réponse**, sélectionnez ou saisissez la réponse requise pour que la condition soit remplie.

La question sera affichée uniquement lorsque la condition spécifiée est remplie.

Pour ajouter plusieurs conditions, ajoutez votre première condition, puis cliquez sur le bouton **Ajouter une autre condition**. Lorsque vous utilisez plusieurs conditions, spécifiez si au moins une de ces conditions doit être remplie ou si toutes doivent l'être.

<p class="note">
    <strong>Remarque :</strong> Vous pouvez supprimer les conditions de logique de saut en cliquant sur la <i class="k-icon-trash"></i> corbeille.
</p>

## Saisir manuellement la logique de saut en code XLSForm
Pour les utilisatrices et utilisateurs avancés, la logique de saut peut être saisie directement en code XLSForm. La structure de base des conditions reste inchangée : vous devrez identifier la question de contrôle, choisir un opérateur logique et saisir la valeur de réponse requise.

Pour saisir manuellement la logique de saut en code XLSForm, suivez ces étapes :
1. Ouvrez les <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question ou du groupe à afficher de manière conditionnelle.
2. Sélectionnez **Logique de saut**, et cliquez sur **Saisir manuellement votre logique de saut en code XLSForm**.
3. Saisissez la condition en code XLSForm.

En code XLSForm, les questions sont désignées par leur **nom de question** (Nom de colonne de données) en utilisant le format `${nom_question}`. Par exemple, si Q2 doit être posée uniquement si la réponse à Q1 est « Oui », la condition de logique de saut pour Q2 serait `${Q1} = 'yes'`.

<p class="note">
    Pour plus d'informations sur le code XLSForm et les opérateurs, consultez la <a href="https://xlsform.org/en/#relevant">documentation XLSForm</a>.
</p>