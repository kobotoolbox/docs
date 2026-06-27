# Ajouter une logique de saut dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/e562a3b12a843642706dec4700529f57fee501f5/source/skip_logic.md" class="reference">5 juin 2026</a>


<iframe src="https://www.youtube.com/embed/uLSnoG0mqV4?si=63o4YeQUZWOsZmfF&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La logique de saut, également appelée branchement conditionnel ou conditions de pertinence, contrôle quelles questions sont affichées dans un formulaire. Par défaut, toutes les questions sont visibles. La logique de saut détermine sous quelle(s) condition(s) une question doit apparaître. Les conditions de logique de saut s'appliquent toujours à la question ou au groupe qui doit être affiché de manière conditionnelle.

<p class="note">
    <strong>Note :</strong> Vous pouvez appliquer une logique de saut à des <a href="group_repeat.html">groupes de questions</a> entiers ainsi qu'à des questions individuelles. Cela permet de simplifier la logique de formulaire et de faciliter la gestion de questionnaires complexes.
</p>

Il existe deux méthodes pour ajouter une logique de saut dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** : ajouter une condition via le **générateur de logique de saut**, ou saisir manuellement la logique de saut en **code XLSForm**.

## Ajouter une condition

Cette première méthode vous permet d'utiliser le générateur de logique de saut pour ajouter vos conditions. Elle est recommandée pour les débutants. Pour ajouter une condition de logique de saut, suivez les étapes ci-dessous :

1. Ouvrez les <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question ou du groupe à afficher de manière conditionnelle.
2. Sélectionnez **Branchement conditionnel**, puis cliquez sur **Ajouter une condition**.
3. Sélectionnez la question du formulaire qui déterminera si la question actuelle est affichée ou non.
4. Choisissez l'opérateur logique approprié pour votre condition (par exemple, >, =, !=).
5. Dans le champ **valeur de réponse**, sélectionnez ou saisissez la réponse requise pour que la condition soit remplie.

La question s'affichera uniquement lorsque la condition spécifiée est remplie.

Pour ajouter plusieurs conditions, ajoutez votre première condition, puis cliquez sur le bouton **Ajouter une autre condition**. Lorsque vous utilisez plusieurs conditions, précisez si au moins l'une de ces conditions doit être remplie ou si toutes doivent l'être.

<p class="note">
    <strong>Note :</strong> Vous pouvez supprimer des conditions de logique de saut en cliquant sur la corbeille <i class="k-icon-trash"></i>.
</p>

## Saisir manuellement la logique de saut en code XLSForm

Pour les utilisateurs avancés, la logique de saut peut être saisie directement en code XLSForm. La structure de base des conditions reste inchangée : vous devrez identifier la question de contrôle, choisir un opérateur logique et saisir la valeur de réponse requise.

Pour saisir manuellement la logique de saut en code XLSForm, suivez les étapes ci-dessous :

1. Ouvrez les <i class="k-icon-settings"></i> **Paramètres** dans le menu latéral droit de la question ou du groupe à afficher de manière conditionnelle.
2. Sélectionnez **Branchement conditionnel**, puis cliquez sur **Saisir manuellement votre branchement conditionnel dans le code XLSForm**.
3. Saisissez la condition en code XLSForm.

En code XLSForm, les questions sont référencées par leur **nom de question** (nom du champ) en utilisant le format `${question_name}`. Par exemple, si Q2 doit être posée uniquement si la réponse à Q1 est « Oui », la condition de logique de saut pour Q2 serait `${Q1} = 'yes'`.

<p class="note">
    Pour plus d'informations sur le code XLSForm et les opérateurs, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic.html">Introduction à la logique de formulaire dans le Formbuilder</a>.
</p>