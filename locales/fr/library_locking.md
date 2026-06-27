# Verrouillage de questionnaire avec XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/149e56f3d80934c2c952fd2ca7d057cc6cdbafff/source/library_locking.md" class="reference">21 Mar 2026</a>

La [bibliothèque de questions de KoboToolbox](https://support.kobotoolbox.org/fr/question_library.html) vous permet de stocker et de gérer des modèles, des questions et des blocs réutilisables dans plusieurs projets. **Les modèles de formulaires dans la bibliothèque** peuvent être partagés avec les membres d'une équipe afin de garantir une conception cohérente des formulaires et de réduire les doublons.

**Le verrouillage de questionnaire** va plus loin en vous permettant de contrôler la façon dont les modèles peuvent être modifiés une fois qu'ils sont utilisés pour créer de nouveaux projets. Grâce au verrouillage, vous pouvez spécifier quelles questions, quels groupes ou quels paramètres au niveau du formulaire peuvent être modifiés. Cette fonctionnalité est particulièrement utile pour les grandes équipes qui travaillent à partir d'un modèle partagé, lorsque certains éléments doivent rester fixes tandis que d'autres peuvent être adaptés aux besoins locaux.

Cet article explique le fonctionnement du verrouillage de questionnaire, les types de restrictions que vous pouvez appliquer, la façon de les configurer dans un XLSForm, et comment importer des XLSForms verrouillés dans KoboToolbox.

<p class="note">
<strong>Note :</strong> Le verrouillage de questionnaire n'est pas disponible dans l'interface de création de formulaires KoboToolbox <strong>(KoboToolbox Formbuilder)</strong>. Pour utiliser cette fonctionnalité, vous devez la mettre en œuvre via XLSForm, puis <a href="https://support.kobotoolbox.org/fr/xlsform_with_kobotoolbox.html">importer votre XLSForm</a> dans KoboToolbox.
<br><br>
Pour en savoir plus sur l'importation et l'utilisation de modèles dans KoboToolbox, consultez l'article <a href="https://support.kobotoolbox.org/fr/question_library.html#">Utiliser la bibliothèque de questions de KoboToolbox</a>.
</p>

## Introduction au verrouillage de questionnaire

Le verrouillage de questionnaire contrôle dans quelle mesure un formulaire **peut être modifié** lorsqu'un projet est créé à partir d'un modèle de bibliothèque. Les restrictions sont définies dans votre XLSForm avant d'importer le formulaire.

Lorsque vous créez un modèle verrouillé et le partagez via votre bibliothèque :
- Les utilisateurs peuvent effectuer des ajustements locaux là où les restrictions le permettent.
- Les éléments verrouillés apparaissent **grisés** dans le Formbuilder.
- Un message au-dessus du formulaire indique quelles restrictions sont actives.

Le verrouillage de questionnaire est distinct des [droits d'accès au niveau du projet](https://support.kobotoolbox.org/fr/managing_permissions.html), qui contrôlent ce que les différents utilisateurs peuvent faire dans un projet déployé.

<p class="note">
<strong>Note :</strong> Les restrictions de verrouillage de questionnaire s'appliquent uniquement dans le <strong>Formbuilder</strong> lorsqu'un projet est créé à partir d'un modèle verrouillé. Si le XLSForm est téléchargé et modifié dans un tableur, les restrictions n'empêcheront pas les modifications. Cependant, des configurations de verrouillage incorrectes ou invalides peuvent provoquer des erreurs lors de la réimportation du formulaire.
</p>

Le verrouillage de questionnaire est configuré dans trois onglets XLSForm :
- **onglet survey :** Pour appliquer des restrictions à des questions et des groupes spécifiques.
- **onglet settings :** Pour appliquer des restrictions au niveau du formulaire et définir l'option `kobo--lock_all`.
- **onglet kobo--locking-profiles :** Pour définir des profils qui regroupent des restrictions associées.

Ensemble, ces onglets vous permettent de définir quelles parties d'un formulaire restent fixes et lesquelles peuvent être modifiées lorsque le modèle est utilisé pour créer de nouveaux projets.

## Types de restrictions

Le verrouillage de questionnaire prend en charge des restrictions à trois niveaux : **question**, **groupe** et **formulaire**. Les restrictions définissent ce qui peut et ce qui ne peut pas être modifié lorsqu'un projet est créé à partir d'un modèle verrouillé.

En outre, un paramètre global (`kobo--lock_all`) peut être utilisé pour verrouiller l'intégralité du formulaire.

### Restrictions au niveau des questions

Les restrictions au niveau des questions s'appliquent à des questions individuelles. Vous pouvez appliquer les restrictions suivantes aux questions de votre XLSForm :

| Restriction | Description |
|:------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <code>choice_add</code> | Empêche l'ajout de nouveaux choix à une question de type **sélection**. |
| <code>choice_delete</code> | Empêche la suppression de choix existants dans une question de type **sélection**. |
| <code>choice_value_edit</code> | Empêche la modification du nom d'un choix (ou de la valeur XML). |
| <code>choice_label_edit</code> | Empêche la modification du libellé d'un choix. |
| <code>choice_order_edit</code> | Empêche la réorganisation des choix dans une question de type **sélection**. |
| <code>question_delete</code> | Empêche la suppression d'une question. |
| <code>question_label_edit</code> | Empêche la modification du libellé ou de l'indice d'une question. |
| <code>question_settings_edit</code> | Empêche la modification des paramètres d'une question, y compris son nom. Cela n'inclut pas la logique de saut ni les critères de validation. |
| <code>question_skip_logic_edit</code> | Empêche la modification des conditions de logique de saut. |
| <code>question_validation_edit</code> | Empêche la modification des critères de validation. |

### Restrictions au niveau des groupes

Les restrictions au niveau des groupes s'appliquent aux [groupes de questions](https://support.kobotoolbox.org/fr/grouping_questions_xls.html). Vous pouvez appliquer les restrictions suivantes aux groupes de votre XLSForm :

| Nom | Description |
|:------|:-------------|
| <code>group_delete</code> | Empêche la suppression d'un groupe. |
| <code>group_split</code> | Empêche la dégroupement des questions. |
| <code>group_label_edit</code> | Empêche la modification du libellé du groupe. |
| <code>group_question_add</code> | Empêche l'ajout ou la duplication de questions dans un groupe. |
| <code>group_question_delete</code> | Empêche la suppression de questions au sein d'un groupe. |
| <code>group_question_order_edit</code> | Empêche la réorganisation des questions dans un groupe. |
| <code>group_settings_edit</code> | Empêche la modification des paramètres du groupe, y compris son nom. Cela n'inclut pas la logique de saut. |
| <code>group_skip_logic_edit</code> | Empêche la modification de la logique de saut pour un groupe. |

### Restrictions au niveau du formulaire

Les restrictions au niveau du formulaire s'appliquent à l'ensemble du formulaire. Vous pouvez appliquer les restrictions suivantes à votre XLSForm :

| Nom | Description |
|:------|:-------------|
| <code>form_appearance</code> | Empêche les modifications du [thème](https://support.kobotoolbox.org/fr/form_style_xls.html) du formulaire. |
| <code>form_replace</code> | Empêche le remplacement du formulaire dans KoboToolbox via l'option <i class="k-icon k-icon-replace"></i> **Remplacer le formulaire**. |
| <code>group_add</code> | Empêche la création de nouveaux groupes. |
| <code>question_add</code> | Empêche l'ajout ou la duplication de questions dans un groupe. |
| <code>question_order_edit</code> | Empêche la réorganisation des questions. |
| <code>language_edit</code> | Empêche la modification des traductions. |
| <code>form_meta_edit</code> | Empêche la modification des questions de [métadonnées](https://support.kobotoolbox.org/fr/metadata_xls.html). |

### Verrouiller l'intégralité d'un formulaire

Le paramètre `kobo--lock_all` peut être ajouté à l'**onglet settings** de votre XLSForm.
- Si défini comme `TRUE`, l'intégralité du formulaire est verrouillée et toutes les restrictions granulaires deviennent redondantes.
- Si défini comme `FALSE` (ou omis), seules les restrictions définies dans vos profils de verrouillage sont appliquées.

**onglet settings**

| kobo--lock_all |
|:----------------- |
| TRUE |
| settings |

## Configurer le verrouillage de questionnaire dans XLSForm

### Définir des profils de verrouillage

Les profils de verrouillage sont des **ensembles de restrictions** qui peuvent être appliqués à des questions, des groupes ou à l'ensemble du formulaire. Ils sont définis dans l'onglet `kobo--locking-profiles` du XLSForm, puis appliqués dans les onglets `survey` et `settings`. Vous pouvez créer autant de profils que nécessaire.

Pour définir des profils de verrouillage dans votre XLSForm :
1. Créez un nouvel onglet nommé `kobo--locking-profiles`.
2. Ajoutez une colonne `restriction`, qui peut inclure n'importe quelle restriction des tableaux ci-dessus.
3. Créez une colonne par **profil** (par exemple, `profile_1`, `profile_2`).
4. Dans la cellule correspondant à une **restriction** et à un **profil**, incluez le mot-clé `locked` pour associer une restriction à un profil.

**onglet kobo--locking-profiles**

| restriction | profile_1 | profile_2 | profile_3 |
|:-------------------|:----------|:----------|:----------|
| choice_add | locked | locked | |
| choice_delete | | locked | |
| choice_value_edit | locked | locked | |
| choice_label_edit | | locked | |
| choice_order_edit | | locked | |
| question_delete | locked | locked | |
| form_appearance | | | locked |

### Appliquer des profils dans l'onglet survey

Une fois que vous avez défini des profils de verrouillage dans l'onglet `kobo--locking-profiles`, vous pouvez les appliquer à des questions et des groupes spécifiques. Pour appliquer des profils dans l'**onglet survey** :

1. Créez une colonne nommée `kobo--locking-profile` dans l'onglet `survey`.
2. Pour chaque question ou groupe que vous souhaitez restreindre, définissez le profil de verrouillage dans la colonne `kobo--locking-profile`.

**onglet survey**

| type | name | label | kobo--locking-profile |
|:-------------------------|:--------|:------------------|:--------------------|
| select_one country | country | Select your country | profile_1 |
| select_one city | city | Select your city | profile_2 |
| survey |

### Appliquer des profils dans l'onglet settings

En plus d'appliquer des profils aux questions et aux groupes dans l'onglet `survey`, vous pouvez également appliquer un profil avec des restrictions au niveau du formulaire dans l'onglet `settings`.

Pour appliquer un profil à l'**onglet settings** :
1. Créez une colonne `kobo--locking-profile` dans l'onglet `settings`.
2. Spécifiez le profil que vous souhaitez appliquer.

**onglet settings**

| kobo--locking-profile |
|:---------------------|
| profile_3 |
| settings |

<p class="note">
<strong>Note :</strong> Les restrictions ne peuvent pas être appliquées dans l'onglet <code>choices</code>. Toutes les restrictions liées aux choix sont définies au niveau de la question ou du groupe dans l'onglet <code>survey</code>.
</p>

## Utiliser des modèles verrouillés dans KoboToolbox

Une fois que vous avez créé et importé un XLSForm verrouillé en tant que modèle, vous pouvez l'utiliser pour créer de nouveaux projets dans KoboToolbox.

### Importer un XLSForm verrouillé dans votre bibliothèque

Pour importer un XLSForm verrouillé dans votre bibliothèque :
1. Accédez à la <i class="k-icon k-icon-library"></i> **Bibliothèque** depuis la barre de menu de gauche dans KoboToolbox.
2. Cliquez sur **NOUVEAU**, puis sélectionnez **Importer**.
3. Importez votre fichier XLSForm et sélectionnez **Importer comme modèle**.

![Upload template](images/library_locking/upload_template.png)

Le modèle apparaîtra dans votre bibliothèque avec un <i class="k-icon k-icon-template-locked"></i> **symbole de verrouillage**, indiquant qu'il contient des restrictions.

### Créer un projet à partir d'un modèle verrouillé

1. Accédez à la page d'accueil **Projets**.
2. Cliquez sur **NOUVEAU**, puis sélectionnez **Utiliser un modèle**.
3. Choisissez le modèle verrouillé que vous souhaitez utiliser.
4. Continuez à créer votre projet normalement.

![Use template](images/library_locking/use_template.png)

Lorsque vous ouvrez le projet dans le Formbuilder :
- Un message apparaît au-dessus de la première question pour résumer les restrictions.
- Les questions, groupes ou paramètres au niveau du formulaire verrouillés apparaissent **grisés**.
- Chaque question verrouillée indique quel profil lui a été appliqué dans ses **Paramètres > Fonctions verrouillées**.

![Locked library](images/library_locking/locked.png)

## Résolution de problèmes

<details>
  <summary><strong>Recommandations pour la résolution de problèmes</strong></summary>
  Si le verrouillage de questionnaire ne fonctionne pas comme prévu, essayez les actions suivantes :
```
    <ul>
  <li>Vérifiez que le formulaire a bien été importé en tant que <strong>Modèle</strong> dans la bibliothèque.</li>
  <li>Vérifiez l'onglet <code>settings</code> de votre XLSForm. Si <code>kobo--lock_all</code> est défini comme <code>TRUE</code>, l'intégralité du formulaire sera verrouillée.</li>
  <li>Vérifiez que tous les noms de restrictions dans l'onglet <code>kobo--locking-profiles</code> sont valides. Seuls les noms de restrictions prédéfinis sont acceptés.</li>
  <li>Assurez-vous que la colonne <code>kobo--locking-profile</code> existe dans l'onglet <code>survey</code> ou <code>settings</code> et que les noms de profils correspondent à ceux définis dans l'onglet <code>kobo--locking-profiles</code>.</li>
</ul>
</details>
```

<br>

<details>
  <summary><strong>Mises en garde et limitations</strong></summary>
<ul>
  <li>Les restrictions sont appliquées uniquement dans le <strong>Formbuilder.</strong> Si le XLSForm est téléchargé et modifié directement dans un tableur, les restrictions n'empêchent pas les modifications.</li>
  <li>Les restrictions s'appliquent uniquement aux projets créés à partir de modèles verrouillés. Les modèles et les questionnaires dans la bibliothèque restent modifiables.</li>
  <li>Le verrouillage est disponible uniquement pour les questionnaires et les modèles. Si vous importez un XLSForm verrouillé en tant que question ou bloc, le verrouillage est ignoré.</li>
  <li>Certains tableurs convertissent automatiquement deux tirets simples <code>--</code> en tiret long (—). Utilisez toujours deux tirets simples dans les noms tels que <code>kobo--locking-profiles</code>.</li>
</ul>

</details>