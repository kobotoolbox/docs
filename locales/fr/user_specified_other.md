# Réponses « Autre » spécifiées par l'utilisatrice ou l'utilisateur pour les questions à choix multiples
<a href="../user_specified_other.html">Read in English</a> | <a href="../es/user_specified_other.html">Leer en español</a> | <a href="../ar/user_specified_other.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/user_specified_other.md" class="reference">15 fév. 2022</a>

La création de réponses « Autre » spécifiées par l'utilisatrice ou l'utilisateur pour les questions à choix multiples en une seule étape est une fonctionnalité qui figure actuellement dans la feuille de route de développement de KoboToolbox. En attendant, voici comment les créer manuellement dans votre formulaire en utilisant la logique de saut.

1. Ajoutez la question souhaitée à votre formulaire en tant que question à choix multiples ordinaire. Il peut s'agir soit du type « sélection unique » (comme illustré ici), soit du type « sélection multiple ».

    ![image](/images/user_specified_other/type.png)

2. Ajoutez une question de suivi de type « Texte » dans laquelle la personne interrogée peut spécifier manuellement sa réponse si nécessaire.

    ![image](/images/user_specified_other/text.png)

    REMARQUE : Si vous utilisez l'application Android KoboCollect pour la collecte de données, il est important de ne pas afficher la deuxième question de texte dans un groupe sur le même écran, car elle ne serait pas visible autrement. En effet, KoboCollect n'affiche sur le même écran que les questions qui sont pertinentes au moment où l'écran est affiché pour la première fois. Assurez-vous simplement de la placer en dehors du groupe lorsque vous choisissez d'afficher plusieurs questions sur le même écran. (Lorsque vous utilisez Enketo Webforms, ce n'est pas un problème car il affiche dynamiquement les questions dès qu'elles deviennent pertinentes.)

3. Ajoutez une [logique de saut](skip_logic.md) à la question de suivi précédente afin qu'elle ne soit affichée que lorsque cela est nécessaire.

    ![image](/images/user_specified_other/skip_logic.png)

4. Enfin, prévisualisez votre formulaire pour vous assurer qu'il se comporte comme prévu.

    ![image](/images/user_specified_other/preview.png)