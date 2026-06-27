# Liaison dynamique de projets avec XLSForm
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/8f9a856ca94d358f333f60f6e563a9ecbb879202/source/dynamic_data_attachment.md" class="reference">6 mai 2026</a>


La liaison dynamique vous permet d'utiliser les données d'un **projet principal** dans des **projets secondaires**, ce qui simplifie la gestion de la collecte de données longitudinales. Cet article explique comment lier dynamiquement des données entre des projets KoboToolbox.

<p class="note">
    <strong>Note :</strong> La liaison dynamique de projets fonctionne de manière similaire à la fonction <a href="https://support.kobotoolbox.org/fr/pull_data_kobotoolbox.html"><code>pulldata()</code></a>, mais elle élimine le besoin de fichiers CSV séparés, puisque les données du projet principal lié servent de source de données.
</p>

Vous pouvez récupérer diverses **réponses (hors fichiers média)** d'un projet principal et effectuer des calculs sur ces données liées dans un projet secondaire. Cela peut être utile pour récupérer des données de référence, des coordonnées ou des dossiers médicaux dans des études de cohorte, ou pour confirmer ou vérifier des données précédemment collectées.

Nous recommandons d'utiliser [XLSForm](https://support.kobotoolbox.org/fr/edit_forms_excel.html) pour configurer la liaison dynamique de projets. Pour des exemples de projets principaux et secondaires, téléchargez des fichiers types [ici](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) et [ici](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx). Pour apprendre à configurer la liaison dynamique de projets dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, consultez l'article <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment_formbuilder.html">Liaison dynamique de projets avec le Formbuilder</a>.

## Lier dynamiquement des projets dans XLSForm

La liaison dynamique de projets nécessite un **projet principal** et au moins un **projet secondaire**. Le **projet principal** ne nécessite aucune modification par rapport à un XLSForm normal. En revanche, la configuration du ou des **projets secondaires** implique les étapes suivantes :
1. Dans l'**onglet survey** de votre XLSForm, ajoutez une ligne et définissez le type de question comme `xml-external`.
2. Dans la colonne `name`, indiquez un nom court pour le formulaire principal. Ce nom peut être composé de caractères de l'alphabet latin, de tirets bas et de chiffres.

**onglet survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. Dans l'ensemble du formulaire, vous pouvez récupérer des valeurs du projet principal en créant une nouvelle question et en incluant l'expression appropriée dans la colonne `calculation` (voir le tableau [ci-dessous](https://support.kobotoolbox.org/fr/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). Vous pouvez utiliser les types de questions suivants pour récupérer des données :
    - Utilisez un type de question `calculate` pour récupérer et stocker des valeurs en vue d'une utilisation ultérieure dans le formulaire ou le jeu de données (par exemple, pour des calculs ou des libellés de questions dynamiques).
    - Utilisez les types de questions `text`, `integer`, `decimal`, `date`, `select_one` ou `select_multiple` pour inclure les valeurs récupérées comme réponses par défaut dans des champs modifiables. Les données modifiées dans le projet secondaire ne changeront pas les données d'origine dans le projet principal.

**onglet survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | What is the participant's ID? |  |
| integer | age | Confirm the participant's age | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Note :</strong> 
    Pour afficher des données liées sans permettre aux utilisateurs de modifier le champ, utilisez une question <code>calculate</code> suivie d'une question <code>note</code> qui affiche la valeur calculée. Vous pouvez également utiliser des questions <code>text</code>, <code>integer</code>, <code>decimal</code>, <code>select_one</code> ou <code>select_multiple</code> avec `dans la colonne <code>read_only</code> définie comme <code>TRUE</code>.
</p>

## Syntaxe de calcul pour la liaison dynamique de projets

Dans la colonne `calculation` de la ligne où les données liées seront récupérées, incluez l'une des expressions du tableau ci-dessous. Ces expressions sont appelées **XPaths**.

Pour chaque expression du tableau ci-dessous :

- `parent` est le nom unique attribué au **formulaire principal** (par exemple, dans la question `xml-external` du **formulaire secondaire**).
- `parent_question` désigne le `name` d'une question du **formulaire principal**.
- `child_question` désigne le `name` d'une question du **formulaire secondaire**.
- `parent_index_question` est la question d'identification du **formulaire principal** qui le relie au **formulaire secondaire** (par exemple, un identifiant unique, le nom d'une organisation).
- `child_index_question` est la question d'identification du **formulaire secondaire** qui le relie au **formulaire principal** (par exemple, un identifiant unique, le nom d'une organisation).
- `parent_group` désigne le `name` du groupe dans le **formulaire principal** dans lequel se trouve `parent_question`.
- `parent_index_group` désigne le `name` du groupe dans le **formulaire principal** dans lequel se trouve `parent_index_question`.

| **XPath**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Renvoie le nombre total de lignes dans le projet principal. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Renvoie le nombre total de lignes dans le projet principal où `parent_question` (dans `parent_group`) n'est pas vide. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question])` | Renvoie le nombre total d'instances où la valeur de `parent_question` (dans `parent_group`) dans le projet principal est égale à la valeur de `child_question` dans le projet secondaire. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Renvoie la valeur de `parent_question` (dans `parent_group`) du projet principal où `child_index_question` dans le projet secondaire est égal à `parent_index_question` dans le projet principal. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Identique à l'expression ci-dessus, mais précise que seules les données de la première instance de `parent_index_question` doivent être renvoyées, en utilisant l'argument `[position() = 1]`. Utilisé en cas de doublons possibles dans le formulaire principal. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Renvoie la somme des valeurs de `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question doit être numérique`. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Renvoie la valeur maximale saisie dans `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Renvoie la valeur minimale saisie dans `parent_question` (dans `parent_group`) du projet principal. Notez que `parent_question` doit être numérique.     |   


<p class="note">
    <strong>Note :</strong> Si la question du formulaire principal n'est incluse dans aucun groupe, omettez <code>parent_group</code> de l'expression.
</p>

## Configurer des projets pour la liaison dynamique

Une fois vos XLSForms configurés, connectez-vous à votre compte KoboToolbox et suivez les étapes ci-dessous :

1. Créez et déployez le **projet principal**, s'il n'est pas déjà déployé.
2. Activez le partage de données pour le projet principal :
    - Dans l'onglet **PARAMÈTRES > Connect Projects** du projet principal, activez le bouton **Data sharing** (désactivé par défaut) et cliquez sur **ACKNOWLEDGE AND CONTINUE** dans la fenêtre de confirmation.
    - Toutes les données sont partagées par défaut, mais vous pouvez restreindre les variables spécifiques à partager avec les projets secondaires en cliquant sur « Select specific questions to share ».

<p class="note">
    <strong>Note :</strong> Si les projets ont des propriétaires différents, le propriétaire du projet principal doit <a href="https://support.kobotoolbox.org/fr/managing_permissions.html">partager le projet</a> avec le propriétaire du projet secondaire. Les droits d'accès minimaux requis pour que la liaison dynamique de projets fonctionne sont <strong>View form</strong> et <strong>View submissions</strong>. Notez que cela permet aux administrateurs du projet secondaire de consulter toutes les données du projet principal.
</p>

3. Créez et déployez le **projet secondaire**.
4. Connectez le projet secondaire au projet principal :
    - Dans l'onglet **PARAMÈTRES > Connect Projects** du projet secondaire, cliquez sur « Select a different project to import data from. » Un menu déroulant vous permettra de sélectionner un projet principal à lier.
    - Renommez le projet principal lié avec le nom de la question `xml-external` défini dans le XLSForm et cliquez sur **IMPORT**.
    - Vous pouvez ensuite sélectionner des questions spécifiques du projet principal à partager avec le projet secondaire (recommandé), ou sélectionner toutes les questions.
5. Si vous ajoutez de nouveaux champs au formulaire principal et souhaitez les utiliser dans le projet secondaire, réimportez le projet principal dans les paramètres du projet secondaire.

<p class="note">
    <strong>Note :</strong> Les formulaires ne peuvent être liés entre eux que s'ils se trouvent sur le même serveur KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Lier dynamiquement un formulaire à lui-même

Il est possible qu'un projet principal et un projet secondaire soient le même projet. Les étapes sont identiques à celles décrites ci-dessus. Voici quelques exemples de cas d'utilisation :

- **Suivi quotidien** : Si un formulaire est utilisé pour enquêter sur la même personne au fil du temps, vous pouvez le lier à lui-même pour comptabiliser les soumissions précédentes. Cela peut permettre d'afficher un message (par exemple, « le suivi est terminé ») après un certain nombre de saisies, ou d'informer l'enquêteur du nombre de formulaires soumis, comme illustré dans l'exemple ci-dessous.

**onglet survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | What is the participant's ID? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | This participant has been surveyed ${count} times. | |
| survey | 

- **Formulaire d'inscription** : En liant un formulaire d'inscription à lui-même, vous pouvez vérifier si un utilisateur a déjà été enregistré. Cela peut permettre de générer un message d'erreur ou d'ajouter une contrainte si la personne est déjà enregistrée, évitant ainsi les inscriptions en double, comme illustré dans l'exemple ci-dessous.

**onglet survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | What is the customer's ID number? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | This customer is already registered. Please close this form. | | ${count} > 0 |
| survey | 

## Collecter et gérer des données avec la liaison dynamique

Les données des projets liés dynamiquement peuvent être collectées à l'aide de [l'application Android KoboCollect](https://support.kobotoolbox.org/fr/data_collection_kobocollect.html) ou des [formulaires web](https://support.kobotoolbox.org/fr/data_through_webforms.html).

Lors de la collecte de données, tenez compte des points suivants :

- Le projet principal doit avoir au moins une soumission pour que le projet secondaire fonctionne correctement.
- Lors de la collecte de données en ligne, il y a un délai de cinq minutes pour la synchronisation des nouvelles données du projet principal avec le projet secondaire.
- En mode hors ligne, téléchargez fréquemment le projet secondaire pour assurer la synchronisation des données avec le projet principal.

<p class="note">
    <strong>Note :</strong> Vous pouvez <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">configurer l'application Android KoboCollect</a> pour mettre à jour automatiquement les données du projet principal lorsqu'une connexion internet est disponible. Accédez à <strong>Paramètres > Gestion des formulaires > Mode de mise à jour des formulaires vierges</strong> et sélectionnez <strong>Formulaires antérieurement téléchargés uniquement</strong> ou <strong>Copie exacte du serveur</strong>. Vous pouvez définir la fréquence de téléchargement automatique à toutes les 15 minutes, toutes les heures, toutes les six heures ou toutes les 24 heures. Notez que l'activation de ce paramètre peut augmenter la consommation de la batterie.
</p>

## Résolution de problèmes

<details>
  <summary><strong>Erreur ou plantage lors de la liaison de formulaires</strong></summary>
Si l'interface utilisateur plante lorsque vous tentez de lier des formulaires, vérifiez les points suivants :
  <ul>
    <li>Votre XLSForm ne contient pas de noms de questions ou de groupes en double dans la colonne <code>name</code> de l'<code>onglet survey</code>.</li>
    <li>Votre projet principal comporte au moins une soumission.</li>
  </ul>
Si l'interface utilisateur plante toujours, sélectionnez uniquement les questions dont vous avez besoin pour connecter les formulaires, au lieu de cliquer sur <strong>Select all</strong>.
</details>

<br>

<details>
<summary><strong>Les données du formulaire principal n'apparaissent pas dans le formulaire secondaire</strong></summary>
Vérifiez que la syntaxe de calcul dans le formulaire secondaire est correcte et que les questions concernées sont partagées dans les deux projets. Si votre question du formulaire principal se trouve dans un groupe de questions, veillez à inclure le nom du groupe dans l'expression XPath. Notez que les nouvelles données du projet principal peuvent prendre jusqu'à cinq minutes à se synchroniser lorsque vous êtes en ligne. Si vous ajoutez de nouveaux champs au formulaire principal et souhaitez les utiliser dans le projet secondaire, ouvrez les paramètres du projet secondaire, réimportez le projet principal et redéployez.
</details>

<br>

<details>
<summary><strong>Le formulaire secondaire se charge lentement</strong></summary>
Les liaisons dynamiques de projets volumineuses peuvent ralentir les formulaires, notamment lors de l'ouverture d'un formulaire web pour une nouvelle soumission ou lors de la modification de soumissions existantes.<br><br>Si vous travaillez avec un jeu de données volumineux, partagez uniquement les questions dont le formulaire secondaire a besoin, plutôt que la liste complète des questions. Vous pouvez également envisager de diviser le formulaire principal en plusieurs formulaires, par exemple par district ou par région, ou d'adopter une approche différente si le jeu de données est trop volumineux pour la liaison dynamique de projets.
</details>

<br>

<details>
<summary><strong>Les données dynamiques ne se rafraîchissent pas dans KoboCollect</strong></summary>
Si vous utilisez KoboCollect et collectez des données hors ligne, les données doivent d'abord être soumises au projet principal, puis téléchargées sur votre appareil de collecte de données pour que la liaison dynamique fonctionne. Ces deux étapes nécessitent une connexion internet. Le téléchargement des données du projet principal est similaire au téléchargement d'une nouvelle version d'un formulaire, et l'application KoboCollect peut être configurée pour <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html#form-management-settings">télécharger automatiquement les nouvelles données</a> à une fréquence définie. Il n'est pas recommandé de s'appuyer sur la liaison dynamique de projets pour des données collectées hors ligne sur une courte période.
</details>

<br>

<details>
<summary><strong>La liaison dynamique de projets ne fonctionne pas à l'intérieur de groupes de questions</strong></summary>
Pour extraire des données dynamiques d'un formulaire principal vers un formulaire secondaire contenant des groupes de questions, assurez-vous que la question d'index (par exemple, le numéro d'identification) dans le formulaire secondaire se trouve dans le même groupe que le calcul pour les données dynamiques. Consultez les fichiers types <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> et <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> pour un exemple de liaison dynamique de projets à l'intérieur de groupes.
</details>

<br>

<details>
<summary><strong>La liaison dynamique de projets ne récupère pas les valeurs des groupes répétés</strong></summary>
La liaison dynamique de projets ne prend actuellement pas en charge la récupération directe de valeurs depuis des groupes répétés dans un formulaire principal. Si vous tentez de récupérer une valeur d'un groupe répété, le formulaire secondaire peut renvoyer des valeurs vides, ne récupérer que la dernière entrée du groupe répété, ou ne pas parvenir à récupérer les données attendues.<br><br>Pour contourner ce problème, vous pouvez ajouter une ou plusieurs questions `calculate` en dehors du groupe répété dans le formulaire principal et les utiliser pour <a href="https://support.kobotoolbox.org/fr/repeat_groups_xls.html#retrieving-values-from-repeat-groups">stocker les valeurs du groupe répété</a> nécessaires dans le formulaire secondaire. Extrayez ensuite ces valeurs calculées dans le formulaire secondaire plutôt que de les extraire directement du groupe répété.<br><br>Pour des flux de travail plus complexes, vous devrez peut-être restructurer le formulaire principal, diviser les entrées du groupe répété en soumissions séparées, ou traiter les données du formulaire principal en dehors de KoboToolbox et les joindre en tant que <a href="https://support.kobotoolbox.org/fr/pull_data_kobotoolbox.html">CSV externe</a>.
</details>

<br>

<details>
<summary><strong>La variable d'index du formulaire principal se trouve à l'intérieur d'un groupe répété</strong></summary>
La liaison dynamique de projets ne prend actuellement pas en charge la liaison de soumissions provenant de groupes répétés. Si la variable d'index dans le formulaire principal se trouve à l'intérieur d'un groupe répété, le formulaire secondaire ne pourra pas faire correspondre et récupérer les données attendues.<br><br>Pour éviter ce problème, placez la variable de liaison en dehors du groupe répété dans la mesure du possible. Si chaque élément répété doit être lié à un formulaire secondaire, envisagez de restructurer le flux de travail de sorte que chaque élément soit soumis comme sa propre soumission principale, plutôt que comme une entrée dans un groupe répété.<br><br>Par exemple, au lieu de collecter tous les membres d'un ménage dans un groupe répété au sein d'une soumission de ménage, vous pourriez créer un formulaire principal séparé dans lequel chaque membre du ménage est soumis comme une soumission individuelle avec un identifiant unique. Le formulaire secondaire peut alors utiliser cet identifiant pour récupérer la soumission correspondante.
</details>

<br>

<details>
<summary><strong>Erreur d'évaluation des champs dans KoboCollect</strong></summary>
Si votre formulaire principal contient des soumissions en double, vous pouvez recevoir un message d'erreur dans KoboCollect indiquant « Error evaluating field / XPath evaluation: type mismatch /This field is repeated. » Pour résoudre ce problème et n'extraire les données que de la première soumission contenant une valeur d'index spécifique, utilisez l'argument <code>[position()=1]</code>, comme ci-dessous :
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>

<br>

<details>
<summary><strong>Impossible de mettre à jour les valeurs récupérées via la liaison dynamique de projets</strong></summary>
Si vous extrayez des données dynamiques dans des questions de type integer, text ou select et souhaitez que ces champs restent modifiables, ajoutez une colonne `trigger` à votre XLSForm. Dans la ligne contenant l'expression de données dynamiques, saisissez le `name` de la question d'index du formulaire secondaire dans la colonne `trigger`.
<br><br>
Cela permet de modifier la valeur manuellement. La valeur ne sera mise à jour à partir des données du formulaire principal que lorsque la réponse à la question d'index change.

</details>

<br>

<details>
<summary><strong>Les noms des choix s'affichent à la place des libellés</strong></summary>
Lors de l'extraction de données d'une question <code>select_one</code> ou <code>select_multiple</code>, la liaison dynamique de projets utilise le nom du choix, et non son libellé.
Pour afficher le libellé du choix dans votre formulaire secondaire, utilisez l'une des approches suivantes :
      <ul>
<li>Extrayez les données dans une question de type select et incluez les libellés correspondants dans l'onglet <code>choices</code>.</li>
<li>Dans le formulaire principal, utilisez un <a href="https://support.kobotoolbox.org/fr/calculations_xls.html#advanced-calculations">calcul</a> <code>jr:choice-name()</code> pour récupérer le libellé du choix, puis extrayez cette valeur calculée dans le formulaire secondaire.</li>
  </ul>

</details>