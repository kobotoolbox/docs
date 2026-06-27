# Découvrir l'interface de création de formulaires
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/b4dddc39234bcb1960d654dc36c30ad9c31e1fb9/source/formbuilder.md" class="reference">6 May 2026</a>


<iframe src="https://www.youtube.com/embed/PFL1_rBB5Q8?si=RkwB2XGHppAK-RRF&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

L'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)** est un outil facile à utiliser pour concevoir et déployer des formulaires de collecte de données. Cet article présente une vue d'ensemble de ses fonctionnalités, de l'ajout et de la gestion des questions à l'organisation de votre formulaire.

<p class="note">
    Pour apprendre à créer un nouveau formulaire dans KoboToolbox, consultez le <a href="https://support.kobotoolbox.org/fr/quick_start.html">Guide de démarrage rapide</a> de KoboToolbox. Pour une introduction complète au développement de formulaires avec KoboToolbox, nous vous recommandons le cours en ligne en autonomie <a href="https://academy.kobotoolbox.org/courses/initiation">Cours d'initiation à KoboToolbox</a> de la KoboToolbox Academy.
</p>

## Ajouter une question

Pour ajouter une question à votre formulaire, cliquez sur le bouton <i class="k-icon k-icon-plus"></i> qui apparaît sous chaque question. Saisissez le libellé de votre question et cliquez sur **Ajouter une question**. Ensuite, [choisissez le type de question](question_types.md).

Pour les types de questions [Choix unique ou Choix multiple](https://support.kobotoolbox.org/fr/select_one_and_select_many.html), ajoutez les choix de réponse sous la question.

<p class="note">
<strong>Note</strong> : Une fois le type de question sélectionné, il ne peut pas être modifié dans le Formbuilder. Pour changer le type d'une question existante, supprimez la question et créez-en une nouvelle avec le même libellé.
</p>

## Ajouter un indice de question

Un indice de question fournit des instructions supplémentaires sous le texte de la question dans le formulaire. Pour ajouter un indice de question, cliquez sur **Indice de question** sous la question et saisissez votre indice.

## Dupliquer une question

Pour dupliquer une question, cliquez sur <i class="k-icon-duplicate"></i> **Dupliquer la question** dans le menu de la question à droite. Une copie exacte apparaîtra directement sous la question d'origine.

## Supprimer une question

Pour supprimer une question, cliquez sur <i class="k-icon-trash"></i> **Supprimer la question** dans le menu de la question à droite. Il vous sera demandé de confirmer avant que la question soit définitivement supprimée de votre formulaire.

<p class="note">
<strong>Note</strong> : Pour supprimer plusieurs questions à la fois dans le Formbuilder, regroupez les questions, puis supprimez le groupe.
</p>

## Modifier les paramètres d'une question

Pour accéder aux paramètres avancés d'une question, cliquez sur <i class="k-icon-settings"></i> **Paramètres** dans le menu de la question à droite. Vous pouvez y ajouter une logique de saut, des critères de validation, des instructions supplémentaires (guidance hint), et rendre une question obligatoire.

<p class="note">
Pour en savoir plus sur les paramètres de questions, consultez les articles <a href="https://support.kobotoolbox.org/fr/question_options.html">Options de questions dans le Formbuilder</a>, <a href="https://support.kobotoolbox.org/fr/skip_logic.html">Ajouter une logique de saut dans le Formbuilder</a> et <a href="https://support.kobotoolbox.org/fr/validation_criteria.html">Ajouter des critères de validation dans le Formbuilder</a>.
</p>

## Ajouter des questions à la bibliothèque

Pour enregistrer une question en vue de la réutiliser dans de futurs formulaires, cliquez sur <i class="k-icon-folder-plus"></i> **Ajouter une question à la bibliothèque**. Elle sera sauvegardée en tant que copie dans votre [bibliothèque de questions](https://support.kobotoolbox.org/fr/question_library.html). Vous pouvez modifier ou supprimer la question d'origine dans votre formulaire sans affecter la copie dans la bibliothèque.

## Regrouper vos questions

Les questions peuvent être [regroupées](https://support.kobotoolbox.org/fr/group_repeat.html) pour organiser votre formulaire. Sélectionnez les questions à l'aide de la touche **CTRL** (Windows) ou **Commande** (Mac), puis cliquez sur <i class="k-icon k-icon-group"></i> **Créer un groupe avec les questions sélectionnées** dans la barre de menu en haut à gauche.

## Modifier l'ordre de vos questions

Les questions et les groupes peuvent être déplacés à n'importe quelle position dans le formulaire. Faites glisser une question ou un groupe depuis sa position actuelle vers l'endroit souhaité.

<p class="note">
<strong>Note</strong> : Pour déplacer plusieurs questions à la fois dans le Formbuilder, regroupez les questions, puis déplacez le groupe. Vous pouvez ensuite <a href="https://support.kobotoolbox.org/fr/group_repeat.html#removing-a-question-group">dissocier</a> les questions.
</p>

## Prévisualiser votre formulaire

Après avoir ajouté toutes les questions à votre formulaire, cliquez sur <i class="k-icon k-icon-view"></i> **Aperçu du formulaire** pour voir comment il apparaîtra une fois déployé.

## Sauvegarder votre formulaire

Pendant que vous modifiez votre formulaire, cliquez régulièrement sur **SAVE** en haut à droite de votre écran pour vous assurer que votre travail est sauvegardé. Un astérisque (*) apparaîtra à côté du bouton **SAVE** lorsque vous avez des modifications non sauvegardées.