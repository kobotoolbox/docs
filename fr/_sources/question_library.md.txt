# Utiliser la bibliothèque de questions de KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/26da17c7c8203fb51267183a3c44789ce7576a47/source/question_library.md" class="reference">25 Mar 2026</a>

La **bibliothèque de questions** de KoboToolbox vous permet de sauvegarder, de réutiliser et de partager des questions dans plusieurs formulaires. Plutôt que de recréer des questions et des choix de réponse fréquemment utilisés, vous pouvez les stocker dans la bibliothèque et les insérer rapidement dans de nouveaux formulaires.

La bibliothèque de questions peut contenir des **questions individuelles, des blocs de questions** et des **modèles de formulaires complets.** Vous pouvez également organiser votre contenu à l'aide de **collections** pour regrouper des éléments connexes par projet, thème, pays ou organisation.

L'utilisation de la bibliothèque de questions contribue à maintenir la cohérence entre les projets, simplifie le processus de création de formulaires et facilite le partage de contenu standardisé avec les autres membres de votre équipe. Vous pouvez accéder à la bibliothèque de questions depuis le menu de gauche du site KoboToolbox.

![Accéder à la bibliothèque de questions](images/question_library/access.png)

<p class="note">
<strong>Note :</strong> La bibliothèque de questions de KoboToolbox peut contenir du contenu public et privé. Cet article porte sur <strong>Ma bibliothèque</strong>, où vous pouvez sauvegarder, organiser, réutiliser et partager vos propres questions, blocs de questions et modèles de formulaires. Pour en savoir plus sur la mise à disposition publique du contenu de la bibliothèque, consultez l'article <a href="https://support.kobotoolbox.org/fr/using_public_collections.html#">Collections publiques dans la bibliothèque KoboToolbox</a>.
</p>

Cet article couvre les sujets suivants :
- Ajouter des questions à la bibliothèque de questions et les utiliser dans vos formulaires
- Ajouter des modèles à votre bibliothèque de questions et créer des formulaires à partir de modèles
- Utiliser des collections pour organiser votre contenu

## Ajouter des questions à la bibliothèque de questions

### Ajouter des questions depuis le Formbuilder

Lorsque vous créez un formulaire dans l'[interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**](https://support.kobotoolbox.org/fr/formbuilder.html), vous pouvez sauvegarder n'importe quelle question dans votre bibliothèque de questions en cliquant sur <i class="k-icon-folder-plus"></i> **Ajouter une question à la bibliothèque** dans le menu latéral droit de la question.

![Ajouter une question à la bibliothèque](images/question_library/add_to_library.png)

Cette approche préserve tous les composants de votre question, notamment les choix de réponse, les [traductions](https://support.kobotoolbox.org/fr/language_dashboard.html), les [options de questions](https://support.kobotoolbox.org/fr/question_options.html), la [logique de saut](https://support.kobotoolbox.org/fr/skip_logic.html) et les [critères de validation](https://support.kobotoolbox.org/fr/validation_criteria.html).

<p class="note">
<strong>Note :</strong> Lorsque vous ajoutez une question à votre bibliothèque, une copie de la question est sauvegardée. Les modifications apportées à la question d'origine n'affectent pas la version sauvegardée.
</p>

Vous pouvez également ajouter un [groupe de plusieurs questions](https://support.kobotoolbox.org/fr/group_repeat.html) à la bibliothèque de questions en cliquant sur <i class="k-icon-folder-plus"></i> **Ajouter une question à la bibliothèque** au niveau du groupe. Le groupe est sauvegardé en tant que **bloc de questions.**

![Ajouter plusieurs questions à la bibliothèque](images/question_library/add_group.png)

### Ajouter des questions depuis la bibliothèque

Vous pouvez également créer des questions directement depuis la bibliothèque de questions :

1. Cliquez sur <i class="k-icon-library"></i> **Bibliothèque** dans le menu de gauche pour ouvrir la bibliothèque.
2. Cliquez sur **NOUVEAU** en haut à gauche.
3. Sélectionnez <i class="k-icon-block"></i> **Bloc de questions**. Le Formbuilder s'ouvre, vous permettant d'ajouter la question ou le groupe de questions que vous souhaitez sauvegarder.
4. Cliquez sur **Créer** en haut à droite pour sauvegarder le bloc de questions dans votre bibliothèque.

![Créer un élément de bibliothèque](images/question_library/new.png)

Vous pouvez importer des questions ou des blocs de questions depuis un [XLSForm](https://support.kobotoolbox.org/fr/edit_forms_excel.html) en cliquant sur <i class="k-icon-upload"></i> **Importer** sous **Créer un élément de Bibliothèque** et en important un XLSForm.

### Gérer les questions dans la bibliothèque de questions

Dans la vue **Ma bibliothèque**, vous pouvez voir toutes les questions et tous les blocs de questions sauvegardés. Pour chaque élément, vous pouvez consulter des informations telles que le nombre de questions incluses, le propriétaire, les langues disponibles et la date de dernière modification.

Pour chaque élément sauvegardé, vous pouvez le survoler pour :

- <i class="k-icon-edit"></i> **Modifier** la ou les questions dans le Formbuilder
- <i class="k-icon-tag"></i> **Ajouter des tags** pour faciliter l'organisation et la catégorisation des éléments afin de simplifier la recherche
- <i class="k-icon-user-share"></i> **Partager** l'élément avec d'autres utilisateurs en leur attribuant des autorisations de consultation, de modification ou de gestion
- <i class="k-icon-duplicate"></i> **Cloner** l'élément pour créer un doublon que vous pouvez modifier indépendamment
- <i class="k-icon-more"></i> Cliquer sur **Plus d'actions** pour gérer les [traductions](https://support.kobotoolbox.org/fr/language_dashboard.html), télécharger l'élément au format XLS ou XML, ou le supprimer

![Gérer la bibliothèque de questions](images/question_library/manage_library.png)

Vous pouvez également cliquer sur n'importe quel élément sauvegardé pour afficher ses détails complets, notamment toutes les questions contenues dans un bloc de questions.

## Ajouter des questions à un formulaire depuis la bibliothèque de questions

Une fois que vous avez ajouté des questions à votre bibliothèque, vous pouvez les utiliser dans de futurs formulaires. Pour utiliser des questions de la bibliothèque dans votre formulaire :

1. Ouvrez votre formulaire dans le [Formbuilder](https://support.kobotoolbox.org/fr/formbuilder.html).
2. Cliquez sur <i class="k-icon-library"></i> **Ajouter à partir de la bibliothèque** dans le coin supérieur droit.
3. Sélectionnez la question ou le bloc de questions que vous souhaitez ajouter, puis faites-le glisser et déposez-le à l'emplacement souhaité dans votre formulaire.
4. Si votre bibliothèque de questions contient de nombreux éléments, vous pouvez utiliser la fonction **Recherche** pour localiser rapidement la question ou le bloc dont vous avez besoin.

![Ajouter une question à un formulaire depuis la bibliothèque](images/question_library/add_from_library.png)

<p class="note">
<strong>Note :</strong> Lorsque vous ajoutez une question de votre bibliothèque à un formulaire, les modifications que vous apportez dans le formulaire n'affectent pas la version d'origine sauvegardée dans la bibliothèque.
</p>

## Ajouter des modèles à votre bibliothèque de questions

<iframe src="https://www.youtube.com/embed/k-2jnfd3DrE?si=wR1zkjMjgM2Dq9mT&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En plus de sauvegarder des questions individuelles ou des blocs de questions, vous pouvez créer des modèles de formulaires complets pouvant être convertis en projets KoboToolbox. Les modèles sont utiles pour standardiser des formulaires complets qui peuvent être réutilisés par différentes équipes, dans différents projets ou pays.

<p class="note">
<strong>Note :</strong> Un <strong>bloc de questions</strong> est un groupe de questions pouvant être inséré n'importe où dans un formulaire, tandis qu'un <strong>modèle</strong> contient un formulaire complet pouvant devenir un projet.
</p>

### Créer un modèle

Vous pouvez créer un modèle depuis votre bibliothèque de questions ou à partir d'un formulaire KoboToolbox existant.

Depuis votre **bibliothèque de questions**, vous pouvez :

- Cliquer sur **NOUVEAU > <i class="k-icon-template"></i> Modèle.** Vous serez redirigé vers le Formbuilder pour concevoir le formulaire après avoir saisi les détails du modèle.
- Cliquer sur **NOUVEAU > <i class="k-icon-upload"></i> Importer**, importer un XLSForm et sélectionner **Importer comme modèle.**

![Importer un modèle dans la bibliothèque](images/question_library/upload_as_template.png)

<p class="note">
<strong>Note :</strong> Si vous utilisez XLSForm, vous pouvez créer des modèles verrouillés qui empêchent d'autres utilisateurs de modifier certaines parties du formulaire. Pour en savoir plus, consultez l'article <a href="https://support.kobotoolbox.org/fr/library_locking.html">Verrouillage de questionnaire avec XLSForm</a>.
</p>

Pour créer un modèle à partir d'un **formulaire KoboToolbox existant :**

1. Ouvrez la page **FORMULAIRE** du projet.
2. Cliquez sur <i class="k-icon-more"></i> **Plus d'actions** dans le coin supérieur droit.
3. Sélectionnez <i class="k-icon-template"></i> **Créer un modèle.**

![Créer un modèle](images/question_library/create_template.png)

Depuis la page **Ma bibliothèque**, vous pouvez gérer les modèles de la même manière que les questions ou les blocs de questions. Vous pouvez les partager avec d'autres utilisateurs, ajouter des tags, modifier les détails ou les supprimer.

### Créer un projet à partir d'un modèle

Vous pouvez utiliser un modèle pour créer un nouveau projet de formulaire depuis votre bibliothèque de questions ou depuis votre **page d'accueil Projets.**

Depuis la **bibliothèque de questions :**

1. Survolez le modèle et cliquez sur <i class="k-icon-projects"></i> **Créer le projet** à droite.
2. Saisissez un nom pour le nouveau projet.

![Créer un projet](images/question_library/create_project.png)

Depuis la **page d'accueil Projets :**

1. Cliquez sur **NOUVEAU** et sélectionnez <i class="k-icon-template"></i> **Utiliser un modèle.**
2. Choisissez un modèle sauvegardé et cliquez sur **Suivant.**
3. Saisissez les détails du projet et cliquez sur **Créer le projet.**

Dans les deux cas, un nouveau projet KoboToolbox sera créé, que vous pourrez modifier et déployer.

![Utiliser un modèle](images/question_library/use_template.png)

<p class="note">
<strong>Note :</strong> La modification d'un projet créé à partir d'un modèle ne modifie pas le modèle d'origine.
</p>

## Utiliser des collections dans la bibliothèque de questions

<iframe src="https://www.youtube.com/embed/EfnyQh-awqk?si=7Hhb499SgsEL9pg4&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Une **collection** est un groupe de questions, de blocs de questions et/ou de modèles organisés ensemble parce qu'ils sont liés au même projet, thème, pays ou autre contexte commun. Les collections vous aident à structurer et à gérer le contenu réutilisable dans votre bibliothèque de questions.

### Créer une collection

Pour créer une collection :

1. Depuis votre bibliothèque de questions, cliquez sur **NOUVEAU** et sélectionnez <i class="k-icon-folder"></i> **Collection.**
2. Saisissez un nom et, si vous le souhaitez, ajoutez une courte description, une organisation, un secteur primaire et un pays. Ces champs sont facultatifs.
3. Ajoutez des tags pour faciliter la catégorisation et l'organisation de votre collection.
4. Cliquez sur **Créer.**

![Créer une collection](images/question_library/create_collection.png)

<p class="note">
<strong>Note :</strong> Si vous souhaitez importer un grand nombre de questions ou de blocs de questions dans votre bibliothèque sous forme d'une seule collection, vous pouvez le faire à l'aide d'un <a href="https://support.kobotoolbox.org/fr/edit_forms_excel.html">XLSForm</a>. Pour en savoir plus, consultez l'article <a href="https://support.kobotoolbox.org/fr/import_collection.html">Importer une collection avec XLSForm</a>.
</p>

Après avoir créé la collection, vous serez redirigé vers la page principale de la collection, qui affichera le message : « Il n'y a pas d'actifs à afficher. »

### Ajouter des éléments à une collection

Vous pouvez ajouter des questions, des blocs de questions ou des modèles à une collection de plusieurs façons :

- Depuis la **page de la collection :**
    - Cliquez sur **NOUVEAU > <i class="k-icon-block"></i> Bloc de questions** pour créer une nouvelle question ou un nouveau bloc dans le Formbuilder et le sauvegarder dans la collection.
    - Cliquez sur **NOUVEAU > <i class="k-icon-template"></i> Modèle** pour créer un modèle et le sauvegarder dans la collection.
- Depuis **Ma bibliothèque**, survolez un élément existant, cliquez sur <i class="k-icon-more"></i> **Plus d'actions** et choisissez le nom de votre collection sous <i class="k-icon-folder-in"></i> **Déplacer sous.**

![Ajouter à une collection](images/question_library/add_to_collection.png)

<p class="note">
<strong>Note :</strong> Vous ne pouvez pas créer de collections imbriquées. Si vous créez une collection à l'intérieur d'une autre collection, elle sera sauvegardée en tant que collection distincte.
</p>

Pour retirer un élément d'une collection, cliquez sur <i class="k-icon-more"></i> **Plus d'actions** dans la ligne de l'élément et sélectionnez <i class="k-icon-folder-out"></i> **Retirer de la collection.**

### Gérer les collections

Vous pouvez gérer votre collection depuis la page **Ma bibliothèque** en la survolant et en sélectionnant les options disponibles pour <i class="k-icon-edit"></i> modifier ses détails, <i class="k-icon-tag"></i> ajouter des tags, <i class="k-icon-user-share"></i> la partager avec d'autres utilisateurs, ou <i class="k-icon-trash"></i> la supprimer. Vous pouvez également effectuer ces actions directement depuis la page de la collection.

<p class="note">
<strong>Note :</strong> La suppression d'une collection supprime définitivement tous les éléments qu'elle contient.
</p>

Pour **rendre une collection publique**, ouvrez la collection et cliquez sur le bouton <i class="k-icon-globe-alt"></i> **Rendre public** dans le coin supérieur droit. Notez que les champs **nom, organisation** et **secteur** doivent être renseignés avant qu'une collection puisse être rendue publique.

<p class="note"> Pour en savoir plus sur les collections publiques, consultez l'article <a href="https://support.kobotoolbox.org/fr/using_public_collections.html">Collections publiques dans la bibliothèque KoboToolbox</a>.
</p>