# Modifier les réponses dans plusieurs soumissions
<a href="../howto_edit_multiple_submissions.html">Read in English</a> | <a href="../es/howto_edit_multiple_submissions.html">Leer en español</a> | <a href="../ar/howto_edit_multiple_submissions.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/509a98dad39e2899a5eff7e870481cf99749f321/source/howto_edit_multiple_submissions.md" class="reference">22 Sep 2022</a>

Les utilisatrices et utilisateurs ont toujours pu modifier les soumissions comme indiqué dans notre article d'assistance
[Modifier ou supprimer une soumission unique](howto_edit_single_submissions.md).
Mais que faire si une utilisatrice ou un utilisateur doit corriger des erreurs de frappe répétées ou mettre à jour des réponses manquantes pour
toutes ou la plupart des soumissions d'un projet d'enquête particulier ? Suivre la
méthode décrite précédemment prendrait beaucoup de temps. C'est pourquoi KoboToolbox a
développé une fonctionnalité qui devrait simplifier la modification et faire gagner du temps.

## Limitations lors de la modification de réponses pour plusieurs soumissions

Il existe plusieurs limitations lors de l'exécution des actions de modification en masse décrites dans
cet article. Ce n'est pas le cas lors de la modification de
[soumissions individuelles](howto_edit_single_submissions.md). Lors de l'utilisation de cette
méthode :

- La logique de validation et les calculs dans votre formulaire ne sont pas réévalués.
- La modification de questions dans des groupes répétés n'est actuellement pas prise en charge.
- Les points de coordonnées doivent suivre le modèle : `latitude longitude altitude précision`.
  Ne pas le faire ne causera pas d'erreur, mais peut compliquer l'analyse de vos données.
- Les réponses à choix multiples doivent être composées des **noms de choix** corrects,
  séparés par un espace. Ne pas le faire ne causera pas d'erreur, mais
  entraînera l'application incorrecte des étiquettes lors de l'exportation.

## Modifier les réponses pour plusieurs soumissions

Voici un écran généralement visible pour **DONNÉES>Tableau**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_1.png)

L'image partagée ci-dessus montre une variance de saisie de données avec la question **Country**
allant de _America_, _U.S.A_, _US_, _United States of America_, _United
States_, _usa_ à _USA_. Cette section de l'article d'assistance expliquera _comment
changer tous ces noms de **Country** variables en **USA**_.

**Étape 1 :**

Pour commencer à modifier les réponses pour plusieurs soumissions, les utilisatrices et utilisateurs doivent soit sélectionner
un seul enregistrement (marqué **1**) soit sélectionner plusieurs enregistrements (marqué **2**).
Sélectionner comme indiqué dans l'image ci-dessous devrait activer les fonctionnalités de modification ainsi
que d'autres fonctionnalités.

![image](/images/howto_edit_multiple_submissions/edit_multiple_2.png)

- **1.** Les utilisatrices et utilisateurs peuvent sélectionner plusieurs enregistrements nécessitant une modification en masse.
- **2.** Alternative à l'approche décrite ci-dessus (en **1**), les utilisatrices et utilisateurs peuvent sélectionner
  _tous les enregistrements_ ou _tous les enregistrements visibles_ sous **DONNÉES>Tableau**. _Tous les enregistrements_
  font référence à l'ensemble des enregistrements présents dans le projet d'enquête tandis que
  _tous les enregistrements visibles_ font référence aux 30 enregistrements visibles par défaut sous
  **DONNÉES>Tableau**. Les utilisatrices et utilisateurs doivent clairement distinguer les deux lorsqu'il y a
  plus de 30 enregistrements (soumissions) dans le projet d'enquête.
- **3.** Affiche le nombre total d'enregistrements sélectionnés pour _modifier/mettre à jour le
  statut de validation_, _modifier en masse_ ou _supprimer en masse_.
- **4.** Les utilisatrices et utilisateurs peuvent modifier en masse le statut de validation comme indiqué dans notre
  article d'assistance [Validation des enregistrements](record_validation.md).
- **5.** Les utilisatrices et utilisateurs peuvent modifier en masse les réponses pour plusieurs soumissions.
- **6.** Les utilisatrices et utilisateurs peuvent supprimer en masse les enregistrements.

**Étape 2 :**

Les utilisatrices et utilisateurs devront maintenant appuyer sur **Modifier** (**5** comme indiqué dans l'image ci-dessus) pour
la modification en masse après avoir sélectionné tous les enregistrements nécessitant des modifications. La
boîte de dialogue suivante devrait alors apparaître.

![image](/images/howto_edit_multiple_submissions/edit_multiple_3.png)

Les utilisatrices et utilisateurs peuvent filtrer la question requise en la tapant dans le filtre de recherche
situé juste en dessous de l'en-tête **Question**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_4.png)

Les utilisatrices et utilisateurs devraient voir _Réponses multiples_ sous l'en-tête **Réponse** (montré dans
l'image ci-dessus) si différentes valeurs ont été saisies. Ici, nous avons une gamme de saisies
allant de _America_, _U.S.A_, _US_, _United States of America_, _United States_,
_usa_ à _USA_. Cependant, si les utilisatrices et utilisateurs sélectionnent un seul enregistrement et appuient sur **Modifier**,
ils verront la boîte de dialogue suivante.

![image](/images/howto_edit_multiple_submissions/edit_multiple_5.png)

Les utilisatrices et utilisateurs peuvent maintenant filtrer la réponse requise en la tapant dans le filtre de recherche
situé juste en dessous de l'en-tête **Réponse**. Cette approche est utile lorsqu'une utilisatrice ou un utilisateur
souhaite modifier un seul enregistrement.

![image](/images/howto_edit_multiple_submissions/edit_multiple_6.png)

**Étape 3 :**

Les utilisatrices et utilisateurs peuvent appuyer sur le bouton **MODIFIER** une fois qu'il est connu _quoi modifier et où
modifier_.

![image](/images/howto_edit_multiple_submissions/edit_multiple_7.png)

**Étape 4 :**

Maintenant, il existe deux approches pour effectuer des modifications en masse. _L'approche 1_ consiste à ce que les utilisatrices et utilisateurs
saisissent le texte requis (**USA** dans notre cas) dans la case vide (marquée
**1.1**) puis appuient sur **ENREGISTRER** (marqué **2**). _L'approche 2_ consiste à ce que les utilisatrices et utilisateurs
appuient sur **SÉLECTIONNER** (marqué **1.2**) pour un texte approprié puis appuient sur
**ENREGISTRER** (marqué **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_8.png)

**Étape 5 :**

Une boîte de dialogue apparaît maintenant. Les utilisatrices et utilisateurs devront maintenant appuyer sur **CONFIRMER & FERMER** pour
enregistrer les modifications effectuées.

![image](/images/howto_edit_multiple_submissions/edit_multiple_9.png)

Les utilisatrices et utilisateurs peuvent toujours retourner à **DONNÉES>Tableau** et vérifier si les modifications en masse ont été
réussies.

![image](/images/howto_edit_multiple_submissions/edit_multiple_10.png)

## Modifier les réponses vides pour plusieurs soumissions

Parfois, il peut y avoir un scénario où les utilisatrices et utilisateurs doivent ajouter une question au
milieu ou à la fin de l'enquête. Dans ce cas, les données d'enquête du
**DONNÉES>Tableau** devraient apparaître comme indiqué dans l'image ci-dessous.

![image](/images/howto_edit_multiple_submissions/edit_multiple_11.png)

Cette section de l'article d'assistance expliquera _comment changer tous ces
états vides en **Alabama**_.

**Étape 1 :**

Pour commencer à modifier les réponses vides pour plusieurs soumissions, les utilisatrices et utilisateurs doivent sélectionner
plusieurs enregistrements (marqué **1**) puis appuyer sur **Modifier** (marqué **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_12.png)

**Étape 2 :**

Les utilisatrices et utilisateurs devront maintenant appuyer sur **Modifier** (comme indiqué dans l'image ci-dessous), qui se trouve dans
une ligne parallèle directement à _State_ car nous mettons à jour les états vides pour tous
les enregistrements.

![image](/images/howto_edit_multiple_submissions/edit_multiple_13.png)

**Étape 3 :**

Dans ce cas, les utilisatrices et utilisateurs doivent saisir le texte requis (**Alabama** dans notre cas)
dans la case vide (marquée **1**) puis appuyer sur **ENREGISTRER** (marqué **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_14.png)

**Étape 4 :**

Une boîte de dialogue apparaît. Les utilisatrices et utilisateurs devront maintenant appuyer sur **CONFIRMER & FERMER** pour enregistrer
les modifications effectuées.

![image](/images/howto_edit_multiple_submissions/edit_multiple_15.png)

Les utilisatrices et utilisateurs peuvent toujours retourner à **DONNÉES>Tableau** et vérifier si les modifications en masse ont été
réussies.

![image](/images/howto_edit_multiple_submissions/edit_multiple_16.png)