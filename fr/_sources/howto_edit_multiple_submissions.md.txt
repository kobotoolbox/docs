# Modifier les réponses dans plusieurs soumissions

Les utilisateurs peuvent toujours modifier des soumissions individuelles comme indiqué dans notre article d'aide [Modifier et supprimer vos données](howto_edit_single_submissions.md). Que faire si un utilisateur doit corriger des erreurs de frappe répétées ou mettre à jour des réponses manquantes pour tout ou partie des soumissions d'un projet ? Suivre la méthode décrite précédemment prendrait beaucoup de temps. C'est pourquoi KoboToolbox a développé une fonctionnalité qui simplifie la modification en masse, permettant ainsi de gagner du temps.

## Limitations lors de la modification de réponses dans plusieurs soumissions

Il existe plusieurs limitations lors de l'exécution des actions de modification en masse décrites dans cet article. Ce n'est pas le cas lors de la modification de [soumissions individuelles](howto_edit_single_submissions.md). Lors de l'utilisation de cette méthode :

- La logique de validation et les calculs de votre formulaire ne sont pas réévalués.
- La modification de questions au sein de groupes répétés n'est pas disponible actuellement.
- Les coordonnées géographiques doivent suivre le format : `latitude longitude altitude accuracy`. Le non-respect de ce format ne génère pas d'erreur, mais peut fausser l'analyse de vos données.
- Les réponses à choix multiple doivent être composées des **noms de choix** corrects, séparés par un espace. Le non-respect de cette règle ne génère pas d'erreur, mais les libellés ne seront pas correctement appliqués lors de l'export.

## Modifier les réponses dans plusieurs soumissions

L'image suivante présente l'affichage habituel de la page **DONNÉES>Tableau**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_1.png)

L'image ci-dessus montre une variation dans la saisie des données pour la question **Country** (Pays), avec des valeurs allant de _America_, _U.S.A_, _US_, _United States of America_, _United States_, _usa_ à _USA_. Cette section de l'article d'aide explique _comment remplacer toutes ces variantes du nom **Country** par **USA**_.

**Étape 1 :**

Pour commencer à modifier les réponses de plusieurs soumissions, les utilisateurs doivent sélectionner un seul enregistrement (repère **1**) ou plusieurs enregistrements (repère **2**). La sélection telle qu'illustrée dans l'image ci-dessous active les fonctionnalités de modification ainsi que d'autres fonctionnalités.

![image](/images/howto_edit_multiple_submissions/edit_multiple_2.png)

- **1.** Les utilisateurs peuvent sélectionner plusieurs enregistrements nécessitant une modification en masse.
- **2.** En alternative à l'approche décrite ci-dessus (en **1**), les utilisateurs peuvent sélectionner _tous les enregistrements_ ou _tous les enregistrements visibles_ sous **DONNÉES>Tableau**. _Tous les enregistrements_ désigne l'ensemble des enregistrements présents dans le projet, tandis que _tous les enregistrements visibles_ désigne les 30 enregistrements affichés par défaut sous **DONNÉES>Tableau**. Les utilisateurs doivent bien distinguer ces deux options lorsque le projet contient plus de 30 enregistrements (soumissions).
- **3.** Indique le nombre total d'enregistrements sélectionnés pour _modifier/mettre à jour le statut de validation_, _la modification en masse_ ou _la suppression en masse_.
- **4.** Les utilisateurs peuvent modifier en masse le statut de validation comme indiqué dans notre article d'aide [Voir et valider vos données](record_validation.md).
- **5.** Les utilisateurs peuvent modifier en masse les réponses de plusieurs soumissions.
- **6.** Les utilisateurs peuvent supprimer en masse les enregistrements.

**Étape 2 :**

Les utilisateurs doivent appuyer sur **Modifier** (**5** dans l'image ci-dessus) pour effectuer une modification en masse après avoir sélectionné tous les enregistrements à modifier. La boîte de dialogue suivante apparaît alors.

![image](/images/howto_edit_multiple_submissions/edit_multiple_3.png)

Les utilisateurs peuvent filtrer la question souhaitée en la saisissant dans le filtre de recherche situé juste en dessous de l'en-tête **Question**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_4.png)

Les utilisateurs verront _Réponses multiples_ sous l'en-tête **Réponse** (comme indiqué dans l'image ci-dessus) si différentes valeurs ont été saisies. Dans notre exemple, les saisies vont de _America_, _U.S.A_, _US_, _United States of America_, _United States_, _usa_ à _USA_. En revanche, si les utilisateurs sélectionnent un seul enregistrement et appuient sur **Modifier**, la boîte de dialogue suivante s'affiche.

![image](/images/howto_edit_multiple_submissions/edit_multiple_5.png)

Les utilisateurs peuvent filtrer la réponse souhaitée en la saisissant dans le filtre de recherche situé juste en dessous de l'en-tête **Réponse**. Cette approche est utile lorsqu'un utilisateur souhaite modifier un seul enregistrement.

![image](/images/howto_edit_multiple_submissions/edit_multiple_6.png)

**Étape 3 :**

Les utilisateurs peuvent appuyer sur le bouton **MODIFIER** une fois qu'ils savent _quoi modifier et où le modifier_.

![image](/images/howto_edit_multiple_submissions/edit_multiple_7.png)

**Étape 4 :**

Il existe deux approches pour effectuer des modifications en masse. L'_approche 1_ consiste à saisir le texte souhaité (**USA** dans notre exemple) dans le champ vide (repère **1.1**), puis à appuyer sur **SAUVEGARDER** (repère **2**). L'_approche 2_ consiste à appuyer sur **SÉLECTIONNER** (repère **1.2**) pour choisir le texte approprié, puis à appuyer sur **SAUVEGARDER** (repère **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_8.png)

**Étape 5 :**

Une boîte de dialogue apparaît. Les utilisateurs doivent appuyer sur **CONFIRMER ET FERMER** pour enregistrer les modifications effectuées.

![image](/images/howto_edit_multiple_submissions/edit_multiple_9.png)

Les utilisateurs peuvent retourner à **DONNÉES>Tableau** pour vérifier si les modifications en masse ont bien été appliquées.

![image](/images/howto_edit_multiple_submissions/edit_multiple_10.png)

## Modifier les réponses vides dans plusieurs soumissions

Il peut arriver que les utilisateurs doivent ajouter une question au milieu ou à la fin d'une enquête. Dans ce cas, les données du projet sous **DONNÉES>Tableau** se présentent comme dans l'image ci-dessous.

![image](/images/howto_edit_multiple_submissions/edit_multiple_11.png)

Cette section de l'article d'aide explique _comment remplacer tous ces champs vides par **Alabama**_.

**Étape 1 :**

Pour commencer à modifier les réponses vides dans plusieurs soumissions, les utilisateurs doivent sélectionner plusieurs enregistrements (repère **1**), puis appuyer sur **Modifier** (repère **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_12.png)

**Étape 2 :**

Les utilisateurs doivent appuyer sur **Modifier** (comme indiqué dans l'image ci-dessous), sur la ligne correspondant à _State_ (État), car nous mettons à jour les champs vides pour tous les enregistrements.

![image](/images/howto_edit_multiple_submissions/edit_multiple_13.png)

**Étape 3 :**

Dans ce cas, les utilisateurs doivent saisir le texte souhaité (**Alabama** dans notre exemple) dans le champ vide (repère **1**), puis appuyer sur **SAUVEGARDER** (repère **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_14.png)

**Étape 4 :**

Une boîte de dialogue apparaît. Les utilisateurs doivent appuyer sur **CONFIRMER ET FERMER** pour enregistrer les modifications effectuées.

![image](/images/howto_edit_multiple_submissions/edit_multiple_15.png)

Les utilisateurs peuvent retourner à **DONNÉES>Tableau** pour vérifier si les modifications en masse ont bien été appliquées.

![image](/images/howto_edit_multiple_submissions/edit_multiple_16.png)