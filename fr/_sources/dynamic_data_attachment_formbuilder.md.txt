# Liaison dynamique de projets avec le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/dynamic_data_attachment_formbuilder.md" class="reference">23 avr. 2026</a>

La liaison dynamique vous permet de récupérer des données d'un **projet principal** dans des **projets secondaires**, simplifiant ainsi la gestion de la collecte de données longitudinales.

Vous pouvez récupérer diverses **réponses (hors fichiers média)** d'un projet principal et effectuer des calculs sur ces données liées dans un projet secondaire. Cela peut être utile pour récupérer des données de référence, des informations de contact ou des dossiers de santé dans des études de cohorte, ou pour confirmer ou vérifier des données précédemment collectées.

Cet article explique comment lier dynamiquement des données entre des projets KoboToolbox au sein de l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**.

<p class="note">
<strong>Remarque :</strong> Il peut être plus facile d'utiliser XLSForm pour configurer des liaisons dynamiques de projets. Pour en savoir plus, consultez l'article <a href="../fr/dynamic_data_attachment.html">Liaison dynamique de projets avec XLSForm</a>.
</p>

## Lier dynamiquement des projets dans le Formbuilder

La liaison dynamique de projets nécessite un **projet principal** et au moins un **projet secondaire**. Le **projet principal** ne nécessite aucune modification par rapport à un formulaire KoboToolbox normal. Cependant, la configuration du ou des **projet(s) secondaire(s)** implique les étapes suivantes :

Tout d'abord, ajoutez une question **XML externe** à votre formulaire secondaire. Cela lie le formulaire principal au formulaire secondaire. Pour ce faire :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Cliquez sur **+ AJOUTER UNE QUESTION**.
3. Choisissez le type de question <i class="k-icon-qt-external-xml"></i> **XML externe**.
4. Au lieu du libellé de la question, fournissez un nom court pour le formulaire principal. Ce nom peut être composé de caractères de l'alphabet latin, de tirets bas et de chiffres.

![Sélectionner la question XML externe](images/dynamic_data_attachment_formbuilder/external_xml.png)

Ensuite, tout au long du formulaire, vous pouvez récupérer des valeurs du projet principal en utilisant des questions de type **Calcul** :

1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Cliquez sur **+ AJOUTER UNE QUESTION**.
3. Choisissez le type de question <i class="k-icon-qt-calculate"></i> **Calcul**.
4. Au lieu du libellé de la question, incluez une expression de calcul pour récupérer les données du projet principal (voir le tableau [ci-dessous](#syntaxe-de-calcul-pour-les-liaisons-dynamiques-de-projets)).

Après avoir récupéré les données du projet principal dans une question de type **Calcul**, vous pouvez les référencer ailleurs dans votre formulaire, y compris dans les libellés de questions, les notes ou la logique de formulaire, en utilisant le [format de référencement de questions](../fr/form_logic.html#référencement-de-questions) standard.

![Récupérer des données à partir d'une question de calcul](images/dynamic_data_attachment_formbuilder/example.png)

<p class="note">
Pour en savoir plus sur les calculs dans le Formbuilder, consultez l'article <a href="../fr/calculate_questions.html">Ajouter des calculs avec le Formbuilder</a>.
</p>

## Syntaxe de calcul pour les liaisons dynamiques de projets

Dans le champ **libellé de la question** de la question de type Calcul où les données liées seront récupérées, incluez l'une des expressions du tableau ci-dessous. Ces expressions sont appelées **XPaths**.

Pour chaque expression du tableau ci-dessous :

- `parent` est le nom unique attribué au **formulaire principal** (dans la question XML externe du **formulaire secondaire**).
- `parent_question` fait référence au nom du champ d'une question du **formulaire principal**.
- `child_question` fait référence au nom du champ d'une question du **formulaire secondaire**.
- `parent_index_question` est la question d'identification du **formulaire principal** qui le relie au **formulaire secondaire** (par exemple, identifiant unique, nom de l'organisation).
- `child_index_question` est la question d'identification du **formulaire secondaire** qui le relie au **formulaire principal** (par exemple, identifiant unique, nom de l'organisation).
- `parent_group` fait référence au nom du champ du groupe dans le **formulaire principal** dans lequel se trouve `parent_question`.
- `parent_index_group` fait référence au nom du champ du groupe dans le **formulaire principal** dans lequel se trouve `parent_index_question`.

| **XPath**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Renvoie le nombre total de lignes dans le projet principal. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Renvoie le nombre total de lignes dans le projet principal où `parent_question` (dans `parent_group`) n'est pas vide. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question])` | Renvoie le nombre total d'instances où la valeur de `parent_question` (dans `parent_group`) dans le projet principal est égale à la valeur de `child_question` dans le projet secondaire. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Renvoie la valeur de `parent_question` (dans `parent_group`) du projet principal où `child_index_question` dans le projet secondaire est égal à `parent_index_question` dans le projet principal. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Identique à ce qui précède, mais spécifie que seules les données de la première instance de `parent_index_question` doivent être renvoyées, en utilisant l'argument `[position() = 1]`. Utilisé en cas de doublons possibles dans le formulaire principal. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Renvoie la somme des valeurs de `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Renvoie la valeur maximale saisie dans `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Renvoie la valeur minimale saisie dans `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique.     |   

<p class="note">
<strong>Remarque :</strong> Si la question du projet principal n'est incluse dans aucun groupe, omettez <code>parent_group/</code> de l'expression.
</p>

## Configurer des projets pour la liaison dynamique

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Une fois vos projets principal et secondaire configurés et déployés dans KoboToolbox, suivez ces étapes :

1. Activez le partage de données pour le projet principal :
    - Dans l'onglet **PARAMÈTRES > Connecter des Projets** du projet principal, activez le bouton **Partage de données** (désactivé par défaut) et cliquez sur **CONSENTIR ET POURSUIVRE** dans la fenêtre de confirmation.
    - Toutes les données sont partagées par défaut, mais vous pouvez restreindre des variables spécifiques à partager avec les projets secondaires en cliquant sur « Sélectionner des questions précises à partager ».

<p class="note">
    <strong>Remarque :</strong> Si les projets ont des propriétaires différents, le propriétaire du projet principal doit <a href="../fr/managing_permissions.html">partager le projet</a> avec le propriétaire du projet secondaire. Les autorisations minimales requises pour que les liaisons dynamiques de projets fonctionnent sont <strong>Afficher le formulaire</strong> et <strong>Afficher les soumissions</strong>. Notez que cela permet aux administrateur(rice)s du projet secondaire de voir toutes les données du projet principal.
</p>

2. Connectez le projet secondaire au projet principal :
    - Dans l'onglet **PARAMÈTRES > Connecter des Projets** du projet secondaire, cliquez sur « Sélectionner un autre projet pour importer des données ». Un menu déroulant vous permettra de sélectionner un projet principal à lier.
    - Renommez le projet principal lié avec le libellé de la question XML externe défini dans le Formbuilder et cliquez sur **IMPORTER**.
    - Vous pouvez ensuite sélectionner des questions spécifiques du projet principal à partager avec le projet secondaire (recommandé), ou sélectionner toutes les questions.
3. Si vous ajoutez de nouveaux champs au formulaire principal et souhaitez les utiliser dans le projet secondaire, réimportez le projet principal dans les paramètres du projet secondaire.

<p class="note">
<strong>Remarque :</strong> Les formulaires ne peuvent être liés ensemble que s'ils se trouvent sur le même serveur KoboToolbox.
</p>

## Lier dynamiquement un formulaire à lui-même

Il est possible qu'un projet principal et un projet secondaire soient le même projet. Les étapes sont les mêmes que celles décrites ci-dessus. Voici des exemples de cas d'utilisation :

- **Suivi quotidien :** Si un formulaire est utilisé pour enquêter sur la même personne au fil du temps, vous pouvez le lier à lui-même pour compter les soumissions précédentes. Cela peut permettre d'afficher un message (par exemple, « le suivi est terminé ») après un certain nombre d'entrées ou d'informer l'enquêteur(rice) du nombre de formulaires soumis, comme illustré dans l'exemple ci-dessous.

![Suivi quotidien d'une enquête](images/dynamic_data_attachment_formbuilder/monitoring.png)

- **Formulaire d'inscription :** En liant un formulaire d'inscription à lui-même, vous pouvez vérifier si un(e) utilisateur(rice) a déjà été inscrit(e). Cela peut permettre de générer un message d'erreur ou d'ajouter des [critères de validation](../fr/validation_criteria.html) s'il(elle) est déjà inscrit(e), empêchant ainsi les inscriptions en double.

## Collecter et gérer des données avec la liaison dynamique

Les données des projets liés dynamiquement peuvent être collectées à l'aide de [l'application Android KoboCollect](../fr/data_collection_kobocollect.html) ou des [formulaires web](../fr/data_through_webforms.html).

Lors de la collecte de données, notez ce qui suit :

- Le projet principal doit avoir au moins une soumission pour que le projet secondaire fonctionne correctement.
- Lors de la collecte de données en ligne, il y a un délai de cinq minutes pour synchroniser les nouvelles données du projet principal avec le projet secondaire.
- En mode hors ligne, téléchargez fréquemment le projet secondaire pour assurer la synchronisation des données avec le projet principal.

Vous pouvez [configurer l'application Android KoboCollect](../fr/kobocollect_settings.html#paramètres-de-gestion-des-formulaires) pour mettre à jour automatiquement les données du projet principal lorsqu'une connexion Internet est disponible :

1. Allez dans **Paramètres > Gestion des formulaires > Mode de mise à jour des formulaires vierges**
2. Sélectionnez soit **Formulaires précédemment téléchargés uniquement** soit **Correspondance exacte avec le serveur**.
3. Définissez la fréquence de téléchargement automatique pour qu'elle se produise toutes les 15 minutes, toutes les heures, toutes les six heures ou toutes les 24 heures. Notez que l'activation de ce paramètre peut augmenter la consommation de la batterie.

<p class="note">
<strong>Remarque :</strong> Pour apprendre à configurer des liaisons dynamiques de projets dans XLSForm et pour obtenir une assistance supplémentaire en matière de dépannage, consultez l'article <a href="../fr/dynamic_data_attachment.html">Liaison dynamique de projets avec XLSForm</a>.
</p>