# Réduire la taille de fichiers multimédias
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/lower_file_size.md" class="reference">15 Feb 2022</a>


Lorsque votre formulaire collecte plusieurs images ou que vous collectez des dizaines de milliers de soumissions, vous pourriez rencontrer des difficultés lors de la génération du fichier ZIP des pièces jointes multimédias si vous n'ajustez pas les paramètres de qualité d'image avant de commencer la collecte de données.

Open Camera est une application tierce open source qui peut vous aider à effectuer ce réglage.

## Instructions

[Installez Open Camera](https://play.google.com/store/apps/details?id=net.sourceforge.opencamera&hl=en_US)
depuis le Play Store Android.

![image](/images/lower_file_size/open_cam.png)

## KoboCollect

Dans KoboCollect, lorsque vous prenez une photo, il vous sera demandé quelle application utiliser par défaut : choisissez Open Camera et sélectionnez « Toujours » afin de ne plus être invité à faire ce choix.

## Open Camera

Dans les paramètres d'Open Camera, accédez aux paramètres photo, puis :

1. Ouvrez la résolution de l'appareil photo et choisissez la résolution acceptable la plus basse.
2. Ouvrez la qualité d'image et choisissez un pourcentage : 90 % donnera un résultat presque parfait, en dessous de 50 % l'image deviendra difficile à reconnaître. Commencez à 70 % et testez quelques images à différents niveaux de qualité pour trouver la taille acceptable la plus basse.

Ce site web fournit un aperçu de la façon d'[estimer](http://fotoforensics.com/tutorial-estq.php) le niveau de qualité JPEG optimal.