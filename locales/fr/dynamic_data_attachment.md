# Pièces jointes de données dynamiques
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/0c4cbe231491ab3ee9bd1e3a82967d30ac63e2c6/source/dynamic_data_attachment.md" class="reference">15 oct. 2025</a>

La liaison dynamique vous permet d'utiliser les données d'un **projet parent** dans des **projets enfants**, simplifiant ainsi la gestion de la collecte de données longitudinales. Cet article explique comment lier dynamiquement des données entre des projets KoboToolbox.

<p class="note">
    <strong>Remarque :</strong> Les pièces jointes de données dynamiques fonctionnent de manière similaire à la fonction <a href="https://support.kobotoolbox.org/fr/pull_data_kobotoolbox.html"><code>pulldata()</code></a>, mais éliminent le besoin de fichiers CSV séparés, puisque les données d'un projet parent lié servent de source de données.
</p>

Vous pouvez récupérer diverses **réponses non médiatiques** d'un projet parent et effectuer des calculs sur ces données liées dans un projet enfant. Cela peut être utile pour récupérer des données de référence, des informations de contact ou des dossiers médicaux dans des études de cohorte, ou pour confirmer ou vérifier des données précédemment collectées.

Nous recommandons d'utiliser [XLSForm](edit_forms_excel.md) pour configurer les pièces jointes de données dynamiques. Pour des exemples de projets parents et enfants, téléchargez des fichiers d'exemple [ici](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) et [ici](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx).

## Lier dynamiquement des projets dans XLSForm

La liaison dynamique de projets nécessite un **projet parent** et au moins un **projet enfant**. Le **projet parent** ne nécessite aucune modification par rapport à un XLSForm normal. Cependant, la configuration du ou des **projets enfants** implique les étapes suivantes :
1. Dans la feuille `survey` de votre XLSForm, ajoutez une ligne et définissez le type de question sur `xml-external`.
2. Dans la colonne `name`, fournissez un nom court pour le formulaire parent. Ce nom peut être composé de caractères de l'alphabet latin, de traits de soulignement et de chiffres.

**Feuille survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. Tout au long du formulaire, vous pouvez récupérer des valeurs du projet parent en créant une nouvelle question et en incluant l'expression appropriée dans la colonne `calculation` (voir le tableau [ci-dessous](https://support.kobotoolbox.org/fr/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). Vous pouvez utiliser les types de questions suivants pour récupérer des données :
    - Utilisez un type de question **calculate** pour récupérer et stocker des valeurs pour une utilisation future dans le formulaire ou l'ensemble de données (par exemple, pour des calculs ou des libellés de questions dynamiques).
    - Utilisez les types de questions **text**, **integer**, **decimal**, **select_one** ou **select_multiple** pour inclure les valeurs récupérées comme réponses par défaut dans des champs modifiables. Les données modifiées dans le projet enfant ne changeront pas les données d'origine dans le projet parent.
  
**Feuille survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | Quel est l'identifiant du participant ? |  |
| integer | age | Confirmez l'âge du participant | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Remarque :</strong> 
    Pour afficher des données liées sans permettre aux utilisatrices et utilisateurs de modifier le champ, utilisez une question <strong>calculate</strong> suivie d'une question <strong>note</strong> qui affiche la valeur calculée. Vous pouvez également utiliser des questions <strong>text</strong>, <strong>integer</strong>, <strong>decimal</strong>, <strong>select_one</strong> ou <strong>select_multiple</strong> avec la colonne <code>read_only</code> définie sur <code>TRUE</code>.
</p>

## Syntaxe de calcul pour les pièces jointes de données dynamiques

Dans la colonne `calculation` de la ligne où les données liées seront récupérées, incluez l'une des expressions du tableau ci-dessous. Ces expressions sont appelées **XPaths**.

Pour chaque expression du tableau ci-dessous :

- `parent` est le nom unique attribué au **formulaire parent** (par exemple, dans la question `xml-external` du **formulaire enfant**).
- `parent_question` fait référence au `name` d'une question du **formulaire parent**.
- `child_question` fait référence au `name` d'une question du **formulaire enfant**.
- `parent_index_question` est la question d'identification du **formulaire parent** qui le relie au **formulaire enfant** (par exemple, identifiant unique, nom de l'organisation).
- `child_index_question` est la question d'identification du **formulaire enfant** qui le relie au **formulaire parent** (par exemple, identifiant unique, nom de l'organisation).
- `parent_group` fait référence au `name` du groupe dans le **formulaire parent** dans lequel se trouve la `parent_question`.
- `parent_index_group` fait référence au `name` du groupe dans le **formulaire parent** dans lequel se trouve la `parent_index_question`.

| **XPath**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Renvoie le nombre total de lignes dans le projet parent. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Renvoie le nombre total de lignes dans le projet parent où `parent_question` (dans `parent_group`) n'est pas vide. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question]` | Renvoie le nombre total d'instances où la valeur de `parent_question` (dans `parent_group`) dans le projet parent est égale à la valeur de `child_question` dans le projet enfant. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Renvoie la valeur de `parent_question` (dans `parent_group`) du projet parent où `child_index_question` dans le projet enfant est égale à `parent_index_question` dans le projet parent. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Identique à ce qui précède, mais spécifie que seules les données de la première instance de `parent_index_question` doivent être renvoyées, en utilisant l'argument `[position() = 1]`. Utilisé en cas de doublons possibles dans le formulaire parent. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Renvoie la somme des valeurs de `parent_question` (dans `parent_group`) du projet parent. Notez que `parent_question` doit être numérique. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Renvoie la valeur maximale saisie dans `parent_question` (dans `parent_group`) du projet parent. Notez que `parent_question` doit être numérique.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Renvoie la valeur minimale saisie dans `parent_question` (dans `parent_group`) du projet parent. Notez que `parent_question` doit être numérique.     |   


<p class="note">
    <strong>Remarque :</strong> Si la question parent n'est incluse dans aucun groupe, omettez <code>parent_group</code> de l'expression.
</p>

## Configuration des projets pour la liaison dynamique

Une fois vos XLSForms configurés, connectez-vous à votre compte KoboToolbox et suivez ces étapes :

1. Importez et déployez le **projet parent**, s'il n'est pas déjà déployé. Assurez-vous que le projet parent contient au moins une soumission.
2. Activez le partage de données pour le projet parent : 
    - Dans l'onglet **PARAMÈTRES > Connecter des projets** du projet parent, activez le bouton **Partage de données** (désactivé par défaut) et cliquez sur **RECONNAÎTRE ET CONTINUER** dans la fenêtre de confirmation.
    - Toutes les données sont partagées par défaut, mais vous pouvez restreindre des variables spécifiques à partager avec les projets enfants en cliquant sur « Sélectionner des questions spécifiques à partager ».

<p class="note">
    <strong>Remarque :</strong> Si les projets ont des propriétaires différents, le propriétaire du projet parent doit <a href="managing_permissions.html">partager le projet</a> avec le propriétaire du projet enfant. Les autorisations minimales requises pour que les pièces jointes de données dynamiques fonctionnent sont <strong>Voir le formulaire</strong> et <strong>Voir les soumissions</strong>. Notez que cela permet aux administratrices et administrateurs du projet enfant de voir toutes les données du projet parent.
</p>

3. Importez et déployez le **projet enfant**.
4. Connectez le projet enfant au projet parent : 
    - Dans l'onglet **PARAMÈTRES > Connecter des projets** du projet enfant, cliquez sur « Sélectionner un projet différent pour importer des données ». Un menu déroulant vous permettra de sélectionner un projet parent à lier.
    - Renommez le projet parent lié avec le nom de question `xml-external` défini dans le XLSForm et cliquez sur **IMPORTER**.
    - Vous pouvez ensuite sélectionner des questions spécifiques du projet parent à partager avec le projet enfant, ou sélectionner toutes les questions.
5. Si vous ajoutez de nouveaux champs au formulaire parent et souhaitez les utiliser dans le projet enfant, réimportez le projet parent dans les paramètres du projet enfant.

<p class="note">
    <strong>Remarque :</strong> Les formulaires ne peuvent être liés ensemble que s'ils se trouvent sur le même serveur KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzU4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lier dynamiquement un formulaire à lui-même

Il est possible qu'un projet parent et un projet enfant soient le même projet. Les étapes sont les mêmes que celles décrites ci-dessus. Voici des exemples de cas d'utilisation :

- **Suivi quotidien** : Si un formulaire est utilisé pour interroger la même personne au fil du temps, vous pouvez le lier à lui-même pour compter les soumissions précédentes. Cela peut vous permettre d'afficher un message (par exemple, « le suivi est terminé ») après un certain nombre d'entrées ou d'informer l'enquêtrice ou l'enquêteur du nombre de formulaires soumis, comme illustré dans l'exemple ci-dessous.

**Feuille survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | Quel est l'identifiant du participant ? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | Ce participant a été interrogé ${count} fois. | |
| survey | 

- **Formulaire d'inscription** : En liant un formulaire d'inscription à lui-même, vous pouvez vérifier si une utilisatrice ou un utilisateur a déjà été inscrit. Cela peut vous permettre de générer un message d'erreur ou d'ajouter une contrainte s'ils sont déjà inscrits, empêchant ainsi les inscriptions en double, comme illustré dans l'exemple ci-dessous.

**Feuille survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | Quel est le numéro d'identification du client ? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | Ce client est déjà inscrit. Veuillez fermer ce formulaire. | | ${count} > 0 |
| survey | 

## Collecte et gestion des données avec liaison dynamique

Les données des projets liés dynamiquement peuvent être collectées à l'aide de [l'application Android KoboCollect](kobocollect_on_android_latest.md) ou des [formulaires web Enketo](data_through_webforms.md).

Lors de la collecte de données, notez ce qui suit :

- Le projet parent doit avoir au moins une soumission pour que le projet enfant fonctionne correctement.
- Lors de la collecte de données en ligne, il y a un délai de cinq minutes pour synchroniser les nouvelles données du projet parent avec le projet enfant.
- En mode hors ligne, téléchargez fréquemment le projet enfant pour assurer la synchronisation des données avec le projet parent.

<p class="note">
    <strong>Remarque :</strong> Vous pouvez <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">configurer l'application Android KoboCollect</a> pour mettre à jour automatiquement les données du projet parent lorsqu'une connexion Internet est disponible. Allez dans <strong>Paramètres > Gestion des formulaires > Mode de mise à jour des formulaires vierges</strong> et sélectionnez soit <strong>Formulaires précédemment téléchargés uniquement</strong>, soit <strong>Correspondance exacte avec le serveur</strong>. Vous pouvez définir la fréquence de téléchargement automatique toutes les 15 minutes, toutes les heures, toutes les six heures ou toutes les 24 heures. Notez que l'activation de ce paramètre peut augmenter la consommation de la batterie.
</p>

## Dépannage

<details>
<summary><strong>Erreur ou plantage lors de la liaison de formulaires</strong></summary>
Les pièces jointes de données dynamiques ne peuvent pas se connecter à un projet parent vide. Ajoutez d'abord au moins une soumission au projet parent, puis liez à nouveau les formulaires.
</details>

<br>

<details>
<summary><strong>Les données parent ne s'affichent pas dans le formulaire enfant</strong></summary>
Vérifiez que la syntaxe de calcul dans le formulaire enfant est correcte et que les questions pertinentes sont partagées dans les deux projets. Si votre question parent se trouve dans un groupe de questions, assurez-vous d'inclure le nom du groupe dans l'expression XPath. Notez que les nouvelles données du projet parent prennent jusqu'à cinq minutes pour se synchroniser lorsque vous êtes en ligne. Si vous ajoutez de nouveaux champs au formulaire parent et souhaitez les utiliser dans le projet enfant, ouvrez les paramètres du projet enfant, réimportez le projet parent et redéployez.
</details>

<br>

<details>
<summary><strong>Le formulaire enfant se charge lentement</strong></summary>
Les pièces jointes de données dynamiques volumineuses peuvent ralentir le chargement du formulaire. Partagez uniquement les questions dont le formulaire enfant a besoin au lieu de la liste complète des questions, puis redéployez et réessayez.
</details>

<br>

<details>
<summary><strong>Les données dynamiques ne se rafraîchissent pas dans KoboCollect</strong></summary>
Si vous utilisez KoboCollect et collectez des données hors ligne, les données doivent d'abord être soumises au projet parent, puis téléchargées sur votre appareil de collecte de données pour que la pièce jointe de données dynamiques fonctionne. Les deux étapes nécessitent une connexion Internet. Le téléchargement des données parent est similaire au téléchargement d'une nouvelle version d'un formulaire, et l'application KoboCollect peut être configurée pour <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">télécharger automatiquement de nouvelles données</a> à une fréquence définie. Il n'est pas recommandé de s'appuyer sur les pièces jointes de données dynamiques pour les données collectées hors ligne dans un court laps de temps.
</details>

<br>

<details>
<summary><strong>La pièce jointe de données dynamiques ne fonctionne pas dans les groupes de questions</strong></summary>
Pour extraire des données dynamiques d'un formulaire parent vers un formulaire enfant avec des groupes de questions, assurez-vous que la question d'index (par exemple, le numéro d'identification) dans le formulaire enfant se trouve dans le même groupe que le calcul pour les données dynamiques. Consultez les fichiers d'exemple <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> et <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> pour un exemple de pièces jointes de données dynamiques dans des groupes.
</details>

<br>

<details>
<summary><strong>Erreur d'évaluation des champs dans KoboCollect</strong></summary>
Si votre formulaire parent contient des soumissions en double, vous pouvez recevoir un message d'erreur dans KoboCollect indiquant « Erreur d'évaluation du champ / Évaluation XPath : incompatibilité de type / Ce champ est répété ». Pour résoudre ce problème et extraire des données uniquement de la première soumission contenant une valeur d'index spécifique, utilisez l'argument <code>[position()=1]</code>, comme ci-dessous :
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>