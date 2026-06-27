# Ajouter des questions à sélection en cascade dans le Formbuilder
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/81d7045e8e9d21afcd7d94ef5c3c0fc97ce36be2/source/cascading_select.md" class="reference">25 nov. 2025</a>

<iframe src="https://www.youtube.com/embed/JDDNmErhV7o?si=S2k3G0sadiFJursu&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Les questions à sélection en cascade vous permettent de créer des formulaires dynamiques où les options d'une question dépendent de la réponse à une question précédente. Cette fonctionnalité permet de simplifier la collecte de données en ne présentant que les choix pertinents, améliorant ainsi l'efficacité et la précision de vos enquêtes.

<p class="note">
  <strong>Note :</strong> Cet article se concentre sur les questions à sélection en cascade de base utilisant le Formbuilder. Pour en savoir plus sur l'utilisation de XLSForm pour créer des questions à sélection en cascade avancées et ajouter des filtres de choix, consultez l'article <a href="../fr/choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a>.
</p>

## Préparer un tableau de choix en cascade

Pour importer des questions à sélection en cascade dans le Formbuilder, vous devez d'abord préparer votre liste de choix dans Excel ou un autre tableur. Vous pouvez utiliser ce <a href="https://docs.google.com/spreadsheets/d/1C_uDOkjjbv5Kx3lyOY7ORwM-muW6BKVzdaPMB1X8-2A/edit?gid=0#gid=0">modèle d'importation en cascade</a> pour commencer.

Le tableau de choix doit inclure les colonnes suivantes :
- **list_name :** Identifiant unique pour la liste de choix d'une question. Ce sera également le nom du champ pour la question créée.
- **name :** Identifiant unique pour chaque choix dans une liste.
- **label :** Texte qui apparaît sur le formulaire pour chaque choix.

<p class="note">
  <strong>Note :</strong> Lors de la définition d'un <strong>list_name</strong> ou d'un <strong>name</strong>, n'utilisez pas de symboles tels que le tiret cadratin ou le point d'interrogation. Seules les lettres de l'alphabet, les tirets bas et les chiffres peuvent être utilisés.
</p>

Ensuite, vous devez ajouter une colonne pour chaque **liste principale**, qui est une liste contenant une sous-liste. Par exemple, une **liste principale** de continents pourrait inclure une **liste secondaire** de pays.

Pour chaque élément de la **liste secondaire**, indiquez dans la colonne de la **liste principale** à quel élément parent l'élément enfant appartient. Par exemple, si le pays dans la liste secondaire est le Malawi, alors dans la colonne continent, indiquez Afrique. Pour faire référence à un élément de la liste principale, utilisez le **nom du choix**, et non le libellé du choix.

![Exemple de sélection en cascade](images/cascading_select/sample.png)

## Importer le tableau dans le Formbuilder

Une fois votre liste de choix prête, vous pouvez l'importer dans le Formbuilder en suivant ces étapes :
1. Copiez l'intégralité du tableau de choix depuis votre tableur.
2. Dans le Formbuilder, cliquez sur <i class="k-icon-cascading"></i> **Insérer sélection en cascade**.
3. Collez le tableau copié dans la zone de texte et cliquez sur **Terminé** pour importer. Ce processus créera automatiquement de nouvelles questions dans votre formulaire.
    - S'il y a des erreurs de formatage, l'importation échouera. Corrigez les erreurs et assurez-vous d'avoir suivi les instructions du modèle.
4. Une fois importées, vous pouvez déplacer les questions dans votre formulaire, modifier les libellés des questions et des choix, et même supprimer des options de choix.
5. Pour ajouter d'autres choix à la liste en cascade, supprimez les questions importées existantes et importez une nouvelle liste depuis votre tableur mis à jour, en suivant le même processus que ci-dessus.

![Exemple d'insertion de sélection en cascade](images/cascading_select/insert_cascading_select.png)

<p class="note">
  <strong>Note :</strong> Si vous modifiez le libellé de la question dans le Formbuilder, assurez-vous que le nom du champ dans ses paramètres correspond toujours au <strong>list_name</strong> de votre tableau de liste de choix.
</p>

## Gestion avancée de la sélection en cascade avec XLSForm

Pour plus de flexibilité dans la gestion et la mise à jour de vos questions à sélection en cascade, en particulier si vous prévoyez des modifications fréquentes de vos listes de choix, l'utilisation de XLSForm est recommandée. Cette méthode vous permet de modifier directement vos listes de choix, sans perdre les modifications apportées aux libellés et aux paramètres des questions.

Pour mettre à jour vos questions à sélection en cascade en utilisant XLSForm :
1. Téléchargez votre XLSForm en quittant le Formbuilder, en cliquant sur <i class="k-icon-more"></i><strong>Plus d'actions</strong> dans l'onglet <strong>FORMULAIRE</strong>, et en sélectionnant <strong>Télécharger XLS</strong>.
2. Accédez à **l'onglet choices** dans le fichier téléchargé et modifiez votre liste de choix. Maintenez la même approche et le même format que ceux décrits ci-dessus pour préparer un tableau de choix en cascade.
3. Téléchargez à nouveau le XLSForm mis à jour vers KoboToolbox en cliquant sur **Remplacer le formulaire** et en téléchargeant votre fichier modifié.

<p class="note">
    Pour en savoir plus sur l'ajout de questions à sélection en cascade et l'utilisation de filtres de choix dans XLSForm, consultez l'article <a href="../fr/choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a>. Pour plus d'informations sur l'utilisation de XLSForm avec KoboToolbox, consultez l'article <a href="../fr/xlsform_with_kobotoolbox.html">Utiliser XLSForm avec KoboToolbox</a>. 
</p>

## Résolution de problèmes
<details>
<summary><strong>La liste de choix en cascade est vide</strong></summary>
Si la liste de choix pour la question secondaire est vide, la liste secondaire ne trouve pas de correspondance dans la liste principale. Vérifiez que les noms de choix ne contiennent aucun symbole (lettres, chiffres ou tirets bas uniquement) et que chaque option parent a au moins un enfant lié.
</details>
<br>
<details>
<summary><strong>Les cascades ne fonctionnent plus après avoir modifié le formulaire</strong></summary>
Renommer une question ou modifier des listes de choix peut changer le code backend sur lequel la cascade repose. Lors du renommage d'une question, assurez-vous que le <strong>nom du champ</strong> reste le même que le <strong>list_name</strong> correspondant. Pour des modifications importantes de listes de choix, reconstruisez la cascade à partir de zéro ou téléchargez le XLSForm, effectuez vos modifications là-bas, puis téléchargez-le à nouveau.
</details>
<br>
<details>
<summary><strong>Sélection en cascade à partir d'une question Choix multiple</strong></summary>
La fonctionnalité de sélection en cascade dans le Formbuilder est conçue uniquement pour les questions <strong>Choix unique</strong>. Créer une cascade qui commence à partir d'une question <strong>Choix multiple</strong> nécessite l'utilisation de XLSForm. 
Pour en savoir plus sur la sélection en cascade avancée avec XLSForm, consultez l'article <a href="../fr/choice_filters_xls.html">Ajouter des filtres de choix dans XLSForm</a>.
</details>
<br>
<details>
<summary><strong>L'élément de l'enquête est introuvable</strong></summary>
Une erreur indiquant qu'un élément de l'enquête est introuvable signifie généralement que le code interne ne correspond pas aux attentes de la cascade. Pour corriger cela, ouvrez les paramètres de la question, localisez le <strong>nom du champ</strong>, et rétablissez-le à sa valeur d'origine (qui devrait correspondre au <strong>list_name</strong> correspondant) avant de redéployer votre formulaire.
</details>