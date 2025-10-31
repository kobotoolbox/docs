# Récupération des données des versions précédentes du formulaire
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6c4fc8e55497e4a00b39095f090a6f43eb01c37b/source/recovering_previous_formdata.md" class="reference">26 juil. 2020</a>

**Cet article présente les étapes pour récupérer les données des versions précédentes du formulaire en cas de suppression de questions**

Normalement, lorsque vous modifiez un formulaire, les données seront téléchargées en fonction de la définition de ce nouveau formulaire. Ainsi, si vous avez changé le nom d'une question ou supprimé une question, toutes les données précédemment collectées pour cette question ne seront pas visibles sous la nouvelle question, sauf si vous choisissez d'inclure les données collectées à partir des versions précédentes comme expliqué ci-dessous.

En général, lorsque vous modifiez vos formulaires d'enquête et que vous les redéployez, vous devriez pouvoir télécharger les données qui ont été soumises au serveur de deux manières différentes. Pour cela, veuillez d'abord consulter les images ci-dessous pour une meilleure compréhension :

**Image 1 :**

![image](/images/recovering_previous_formdata/no_redeployment.jpg)

**L'image 1** représente un scénario où il n'y a pas de redéploiement dans le projet d'enquête tandis que

**Image 2 :**

![image](/images/recovering_previous_formdata/redeployment.jpg)

**L'image 2** représente un scénario où il y a un redéploiement dans le projet d'enquête (*comme indiqué par le marquage rouge*).

Par conséquent, la différence entre le projet qui n'a pas de redéploiement et celui qui a un redéploiement est visible comme le montre **l'image 2** qui comporte une case à cocher avec un message **Include fields from all 3 deployed versions**. Le **3** indiqué dans le message correspond à ce qui suit : le premier comme déployé, le deuxième et le troisième comme versions redéployées.

Ce que vous devez garder à l'esprit ici, c'est que si vous sélectionnez la case à cocher (*qui est cochée par défaut lorsqu'un projet a été redéployé*) marquée **Include fields from all 3 deployed versions**, vous devriez pouvoir télécharger tous les cas avec toutes les variables (*y compris les variables qui ont été supprimées lors du déploiement récent*). De même, si vous ne sélectionnez pas la case à cocher, vous êtes autorisé à télécharger tous les cas **mais** uniquement avec les variables disponibles dans le dernier déploiement.