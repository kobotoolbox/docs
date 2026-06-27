# Récupérer des données issues de versions précédentes d'un formulaire

**Cet article décrit les étapes à suivre pour récupérer des données issues de versions précédentes d'un formulaire en cas de suppression de questions.**

En règle générale, lorsque vous modifiez un formulaire, les données sont téléchargées selon la définition du nouveau formulaire. Ainsi, si vous avez modifié le nom d'une question ou supprimé une question, toutes les données précédemment collectées pour cette question ne seront pas visibles dans la nouvelle version du formulaire, sauf si vous choisissez d'inclure les données collectées dans les versions précédentes, comme expliqué ci-dessous.

En général, lorsque vous modifiez vos formulaires et les redéployez, vous pouvez télécharger les données soumises au serveur de deux manières différentes. Pour mieux comprendre, veuillez d'abord consulter les images ci-dessous :

**Image 1 :**

![image](/images/recovering_previous_formdata/no_redeployment.jpg)

L'**image 1** illustre un scénario sans redéploiement dans le projet, tandis que

**Image 2 :**

![image](/images/recovering_previous_formdata/redeployment.jpg)

l'**image 2** illustre un scénario avec redéploiement dans le projet (*indiqué par le marquage en rouge*).

La différence entre un projet sans redéploiement et un projet avec redéploiement est visible dans l'**image 2**, qui affiche une case à cocher accompagnée du message **Include fields from all 3 deployed versions**. Le chiffre **3** mentionné dans ce message correspond à : la première version déployée, la deuxième et la troisième versions redéployées.

Il est important de noter que si vous cochez la case (*cochée par défaut lorsqu'un projet a été redéployé*) **Include fields from all 3 deployed versions**, vous pourrez télécharger toutes les soumissions avec l'ensemble des variables (*y compris les variables supprimées lors du déploiement le plus récent*). À l'inverse, si vous ne cochez pas cette case, vous pourrez télécharger toutes les soumissions **mais** uniquement avec les variables disponibles dans la dernière version déployée.