# Ajouter des questions de sélection en cascade dans l'interface de création de formulaires
<a href="../cascading_select.html">Read in English</a> | <a href="../es/cascading_select.html">Leer en español</a> | <a href="../ar/cascading_select.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/d3acfe1ff9024088d8786974939afa969289bf79/source/cascading_select.md" class="reference">5 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/JDDNmErhV7o?si=S2k3G0sadiFJursu" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Les questions de sélection en cascade vous permettent de créer des formulaires dynamiques où les options d'une question dépendent de la réponse à une question précédente. Cette fonctionnalité aide à rationaliser la collecte de données en ne présentant que les choix pertinents, améliorant ainsi l'efficacité et la précision de vos enquêtes.

<p class="note">
  <strong>Remarque :</strong> Cet article se concentre sur les questions de sélection en cascade de base utilisant l'interface de création de formulaires. Pour en savoir plus sur l'utilisation de XLSForm pour créer des questions de sélection en cascade avancées et ajouter des filtres de choix, consultez la <a href="https://xlsform.org/en/#cascading-selects">documentation XLSForm</a>.
</p>

## Préparer un tableau de choix en cascade

Pour importer des questions de sélection en cascade dans l'interface de création de formulaires, vous devez d'abord préparer votre liste de choix dans Excel ou un autre tableur. Vous pouvez utiliser ce <a href="https://docs.google.com/spreadsheets/d/1C_uDOkjjbv5Kx3lyOY7ORwM-muW6BKVzdaPMB1X8-2A/edit?gid=0#gid=0">modèle d'importation en cascade</a> pour commencer.

Le tableau de choix doit inclure les colonnes suivantes :
- **list_name :** Identifiant unique pour la liste de choix d'une question. Ce sera également le nom de colonne de données pour la question créée.
- **name :** Identifiant unique pour chaque choix au sein d'une liste.
- **label :** Texte qui apparaît sur le formulaire pour chaque choix.

<p class="note">
  <strong>Remarque :</strong> Lors de la définition d'un <strong>list_name</strong> ou d'un <strong>name</strong>, n'utilisez pas de symboles tels que le tiret cadratin ou le point d'interrogation. Seules les lettres de l'alphabet, les traits de soulignement et les chiffres peuvent être utilisés.
</p>

Ensuite, vous devez ajouter une colonne pour chaque **liste parent**, qui est une liste incluant une sous-liste. Par exemple, une **liste parent** de continents pourrait inclure une **liste enfant** de pays.

Pour chaque élément de la **liste enfant**, indiquez dans la colonne **liste parent** à quel élément parent l'élément enfant appartient. Par exemple, si le pays dans la liste enfant est le Malawi, alors dans la colonne continent, indiquez Afrique. Pour faire référence à un élément de la liste parent, utilisez le **nom du choix**, et non le libellé du choix.

![Exemple de sélection en cascade](images/cascading_select/sample.png)

## Importer le tableau dans l'interface de création de formulaires

Une fois votre liste de choix prête, vous pouvez l'importer dans l'interface de création de formulaires en suivant ces étapes :
1. Copiez l'intégralité du tableau de choix depuis votre tableur.
2. Dans l'interface de création de formulaires, cliquez sur <i class="k-icon-cascading"></i> **Insérer une sélection en cascade**.
3. Collez le tableau copié dans la zone de texte et cliquez sur **Terminé** pour importer. Ce processus créera automatiquement de nouvelles questions dans votre formulaire.
    - S'il y a des erreurs de formatage, l'importation échouera. Corrigez toute erreur et assurez-vous d'avoir suivi les instructions du modèle.
4. Une fois importées, vous pouvez déplacer les questions dans votre formulaire, modifier les libellés des questions et des choix, et même supprimer des options de choix.
5. Pour ajouter d'autres choix à la liste en cascade, supprimez les questions importées existantes et importez une nouvelle liste depuis votre tableur mis à jour, en suivant le même processus que ci-dessus.

![Exemple d'insertion de sélection en cascade](images/cascading_select/insert_cascading_select.png)

<p class="note">
  <strong>Remarque :</strong> Si vous modifiez le libellé de la question dans l'interface de création de formulaires, assurez-vous que le nom de colonne de données dans ses paramètres correspond toujours au <strong>list_name</strong> de votre tableau de liste de choix.
</p>

## Gestion avancée de la sélection en cascade à l'aide de XLSForm

Pour plus de flexibilité dans la gestion et la mise à jour de vos questions de sélection en cascade, en particulier si vous prévoyez des modifications fréquentes de vos listes de choix, l'utilisation de XLSForm est recommandée. Cette méthode vous permet de modifier directement vos listes de choix, sans perdre les modifications apportées aux libellés et paramètres des questions.

Pour mettre à jour vos questions de sélection en cascade à l'aide de XLSForm :
1. Téléchargez votre XLSForm en quittant l'interface de création de formulaires, en cliquant sur <i class="k-icon-more"></i><strong>Plus d'actions</strong> dans l'onglet <strong>FORMULAIRE</strong>, et en sélectionnant <strong>Télécharger XLS</strong>.
2. Accédez à la feuille de calcul `choices` dans le fichier téléchargé et modifiez votre liste de choix. Maintenez la même approche et le même format que ceux décrits ci-dessus pour la préparation d'un tableau de choix en cascade.
3. Importez à nouveau le XLSForm mis à jour dans KoboToolbox en cliquant sur <strong>Remplacer le formulaire</strong> et en important votre fichier modifié.

<p class="note">
    Pour en savoir plus sur l'ajout de questions de sélection en cascade et l'utilisation de filtres de choix dans XLSForm, consultez la <a href="https://xlsform.org/en/#cascading-selects">documentation XLSForm</a>. Pour plus d'informations sur l'utilisation de XLSForm avec KoboToolbox, consultez <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">Premiers pas avec XLSForm</a>. 
</p>

## Dépannage
<details>
<summary><strong>La liste de choix en cascade est vide</strong></summary>
Si la liste de choix pour la question enfant est vide, la liste enfant ne trouve pas de correspondance dans la liste parent. Vérifiez que les noms de choix ne contiennent aucun symbole (lettres, chiffres ou traits de soulignement uniquement) et que chaque option parent a au moins un enfant lié.
</details>
<br>
<details>
<summary><strong>Les cascades se cassent après modification du formulaire</strong></summary>
Renommer une question ou modifier des listes de choix peut changer le code backend sur lequel la cascade repose. Lors du renommage d'une question, assurez-vous que le <strong>nom de colonne de données</strong> reste identique au <strong>list_name</strong> correspondant. Pour des modifications importantes de listes de choix, reconstruisez la cascade à partir de zéro ou téléchargez le XLSForm, effectuez vos modifications là-bas, puis importez-le à nouveau.
</details>
<br>
<details>
<summary><strong>Sélection en cascade à partir d'une question à choix multiples</strong></summary>
La fonctionnalité de sélection en cascade dans l'interface de création de formulaires est conçue uniquement pour les questions <strong>Sélection unique</strong>. Construire une cascade qui commence à partir d'une question <strong>Sélection multiple</strong> nécessite l'utilisation de XLSForm. 
Pour en savoir plus sur la sélection en cascade avancée à l'aide de XLSForm, consultez la <a href="https://xlsform.org/en/#cascading-selects">documentation XLSForm</a>.
</details>
<br>
<details>
<summary><strong>L'élément d'enquête est introuvable</strong></summary>
Une erreur indiquant qu'un élément d'enquête est introuvable signifie généralement que le code interne ne correspond pas aux attentes de la cascade. Pour corriger cela, ouvrez les paramètres de la question, localisez le <strong>nom de colonne de données</strong> et rétablissez-le à sa valeur d'origine (qui devrait correspondre au <strong>list_name</strong> correspondant) avant de redéployer votre formulaire.
</details>