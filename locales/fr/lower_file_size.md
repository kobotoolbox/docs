# Réduire la taille des fichiers multimédias collectés
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/lower_file_size.md" class="reference">15 fév. 2022</a>

Lorsque votre formulaire collecte plus d'une image ou que vous collectez des dizaines de milliers d'enregistrements, vous pourriez rencontrer des difficultés pour générer le fichier ZIP des pièces jointes multimédias si vous n'ajustez pas les paramètres de qualité d'image avant de commencer la collecte de données.

Open Camera est une application tierce open source qui peut vous aider à le faire.

## Instructions

[Installez Open Camera](https://play.google.com/store/apps/details?id=net.sourceforge.opencamera&hl=en_US)
depuis le Google Play Store Android.

![image](/images/lower_file_size/open_cam.png)

## KoboCollect

Dans KoboCollect, lorsque vous prenez une photo, il vous sera désormais demandé quelle application doit être utilisée par défaut : choisissez Open Camera et sélectionnez « Toujours » pour ne plus être interrogé.

## Open Camera

Dans les paramètres d'Open Camera, allez dans Photo Settings, puis :

1. Ouvrez Camera Resolution et choisissez la résolution la plus petite acceptable.
2. Ouvrez image quality et choisissez un pourcentage : 90 % aura un rendu presque parfait, en dessous de 50 % l'image deviendra plus difficile à reconnaître. Commencez avec 70 % et testez quelques images à différents niveaux de qualité pour trouver la taille la plus petite acceptable.

Ce site web fournit un aperçu de
[comment estimer](http://fotoforensics.com/tutorial-estq.php) le niveau de qualité JPEG optimal.