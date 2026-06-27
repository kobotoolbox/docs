# Spécifier une réponse autre pour les questions à choix multiples
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/user_specified_other.md" class="reference">23 Apr 2026</a>


La création de réponses « Autre » spécifiées par l'utilisateur pour les questions à choix multiples en une seule étape est une fonctionnalité qui figure actuellement sur la feuille de route de développement de KoboToolbox. En attendant, voici comment les créer manuellement dans votre formulaire à l'aide d'une logique de saut.

1. Ajoutez la question souhaitée à votre formulaire en tant que question à choix multiples ordinaire. Il peut s'agir d'une question de type « Choix unique » (comme illustré ici) ou « Choix multiple ».

    ![image](/images/user_specified_other/type.png)

2. Ajoutez une question de suivi de type « Texte » dans laquelle le répondant peut saisir manuellement sa réponse si nécessaire.

    ![image](/images/user_specified_other/text.png)

    NOTE : Si vous utilisez l'application Android KoboCollect pour la collecte de données, il est important de ne pas afficher la deuxième question de type texte dans un groupe sur le même écran, car elle ne serait pas visible autrement. En effet, KoboCollect n'affiche sur le même écran que les questions qui sont pertinentes au moment où l'écran est affiché pour la première fois. Veillez donc à la placer en dehors du groupe lorsque vous choisissez d'afficher plusieurs questions sur le même écran. (Avec les formulaires web, ce n'est pas un problème, car les questions s'affichent dynamiquement dès qu'elles deviennent pertinentes.)

3. Ajoutez une [logique de saut](skip_logic.md) à la question de suivi précédente afin qu'elle ne s'affiche que lorsque cela est nécessaire.

    ![image](/images/user_specified_other/skip_logic.png)

4. Enfin, prévisualisez votre formulaire pour vous assurer qu'il se comporte comme prévu.

    ![image](/images/user_specified_other/preview.png)