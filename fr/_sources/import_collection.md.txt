# Importer une collection avec XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/import_collection.md" class="reference">20 Mar 2026</a>

Une **collection** est un groupe de questions, de blocs de questions et de modèles associés, organisés dans votre [bibliothèque de questions KoboToolbox](https://support.kobotoolbox.org/fr/question_library.html). Les collections vous permettent de gérer du contenu réutilisable par projet, thème, pays ou organisation.

Vous pouvez importer plusieurs questions ou blocs de questions à la fois sous forme de collection à l'aide d'un [XLSForm](https://support.kobotoolbox.org/fr/getting_started_xlsform.html). Cette approche est utile pour préparer des ensembles de questions standardisés en dehors de l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, ou pour migrer du contenu XLSForm existant dans votre bibliothèque.

Cet article explique comment structurer et importer un XLSForm afin qu'il soit intégré en tant que collection.

## Configurer votre XLSForm

Pour être importé correctement dans votre bibliothèque de questions KoboToolbox, votre XLSForm doit respecter une structure spécifique. Une fois que vous disposez d'un [XLSForm fonctionnel](https://support.kobotoolbox.org/fr/getting_started_xlsform.html), vous pouvez l'adapter pour qu'il fonctionne comme une collection en modifiant sa structure :

1. **Renommez l'onglet principal :** Remplacez l'**onglet survey** standard par un onglet nommé `library`.
    - Cet onglet doit contenir les mêmes colonnes que vous incluriez normalement dans un onglet survey, telles que `type`, `name`, `label`, les [colonnes de libellés traduits](https://support.kobotoolbox.org/fr/language_xls.html) et toutes les [options de questions](https://support.kobotoolbox.org/fr/question_options_xls.html) pertinentes.
2. **Incluez des questions individuelles ou des groupes de questions :** Vous pouvez inclure des questions indépendantes ou des groupes de questions complets dans l'**onglet** `library`.
3. **Définissez des blocs de questions à l'aide d'une colonne `block` :** Ajoutez une colonne nommée `block` pour regrouper des questions associées en un bloc de questions.
    - Saisissez le même titre de bloc dans chaque ligne appartenant à ce bloc.
    - Toute ligne sans valeur dans la colonne `block` sera importée en tant que question individuelle.
4. **Ajoutez des étiquettes (facultatif) :** Pour attribuer des étiquettes à une question ou à un bloc, ajoutez une colonne au format `tag:[nom de l'étiquette]` (par exemple, `tag:wash`).
    - Saisissez `1` dans chaque ligne devant recevoir l'étiquette.
    - Au sein des blocs, il suffit de marquer une seule ligne du bloc, bien que marquer plusieurs lignes ne pose pas de problème.

<p class="note">
  Pour un exemple de la structure requise, consultez cet <a href="https://support.kobotoolbox.org/_static/files/question_library/collection_import_sample.xlsx">XLSForm type</a>.
</p>

## Importer votre XLSForm

Une fois votre XLSForm correctement structuré en tant que collection, vous pouvez l'importer dans votre bibliothèque de questions KoboToolbox.

Pour importer votre XLSForm :

1. Connectez-vous à votre compte KoboToolbox.
2. Cliquez sur <i class="k-icon-library"></i> **Bibliothèque** dans le menu de gauche pour ouvrir la bibliothèque.
3. Cliquez sur **NOUVEAU** en haut à gauche.
4. Sélectionnez <i class="k-icon-upload"></i> **Importer** et importez votre XLSForm. Cliquez sur **Importer**.

Le fichier sera importé en tant que collection dans votre bibliothèque de questions.

<p class="note">
  Pour en savoir plus sur la bibliothèque de questions KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_library.html">Utiliser la bibliothèque de questions de KoboToolbox</a>.
</p>

## Considérations supplémentaires

### Groupes au sein des blocs

Vous pouvez inclure des lignes `begin_group` et `end_group` à l'intérieur d'un bloc. Assurez-vous que la ligne `begin_group` possède une valeur `name` unique, comme requis dans la structure XLSForm standard. Les lignes d'ouverture et de fermeture du groupe doivent toutes deux être incluses dans le même bloc.

Utiliser le nom du bloc comme libellé du groupe peut contribuer à maintenir la clarté après l'import.

<p class="note">
  Pour en savoir plus sur les groupes de questions dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/grouping_questions_xls.html">Groupes de questions dans XLSForm</a>.
</p>

### Logique de saut et règles de validation

Vous pouvez inclure une logique de pertinence, des contraintes et d'autres éléments de logique de formulaire dans votre XLSForm. Ces paramètres seront conservés lors de l'import, ce qui est utile pour réutiliser des blocs de questions complexes sans avoir à reconstruire une logique avancée.

<p class="note">
  Pour en savoir plus sur la logique de formulaire dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/form_logic_xls.html">Introduction à la logique de formulaire dans XLSForm</a>.
</p>

### Plusieurs langues

Vous pouvez inclure des traductions en utilisant la syntaxe XLSForm standard, telle que `label::English (en)` ou `label::Español (es)`. Les libellés traduits et les libellés de choix seront importés avec le bloc.

<p class="note">
  Pour en savoir plus sur l'ajout de traductions dans XLSForm, consultez l'article <a href="https://support.kobotoolbox.org/fr/language_xls.html#">Ajouter des traductions dans XLSForm</a>.
</p>