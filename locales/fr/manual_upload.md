# Téléverser manuellement des soumissions
<a href="../manual_upload.html">Read in English</a> | <a href="../es/manual_upload.html">Leer en español</a> | <a href="../ar/manual_upload.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/20273bf768ef8d800b55bacef5af057845b1559d/source/manual_upload.md" class="reference">6 Sep 2023</a>

<p class="note">Veuillez noter qu'il s'agit encore d'une fonctionnalité expérimentale et qu'elle ne vous empêche pas de créer des soumissions en double.</p>

Dans certaines situations, vous pourriez ne pas être en mesure d'utiliser l'option de téléversement standard après avoir collecté des données avec **KoboCollect** ou les **formulaires Web Enketo**. Cela peut être dû à des problèmes avec votre appareil mobile partiellement endommagé (par exemple, l'écran est brisé), ou au fait de vous trouver dans un endroit éloigné sans accès à Internet. Vous pouvez télécharger vos soumissions depuis l'appareil de collecte de données vers votre ordinateur local, puis les téléverser sur le serveur lorsque vous aurez retrouvé une connexion Internet.

## Exporter des données depuis les formulaires Web

1. Dans votre **formulaire Web** activé hors ligne, ouvrez le « Panneau latéral » en cliquant sur le crochet à gauche.

![Side Panel](/images/manual_upload/Side_Panel.png)

2. Cliquez sur le bouton **Export** et un fichier ZIP sera enregistré sur votre ordinateur. Si ce n'est pas le cas, cliquez à nouveau sur le bouton **Export**. Pour certains navigateurs, cela peut ne pas fonctionner et vous devrez cliquer sur le lien « alternative download - online », ce qui nécessitera une connexion Internet.

![Export](/images/manual_upload/Export.png)

3. Suivez maintenant les [instructions décrites ci-dessous](#importer-un-fichier-zip-de-données) pour importer vos soumissions.

## Exporter des données depuis KoboCollect

1. Connectez l'appareil à votre ordinateur via un câble USB.

2. Ouvrez le stockage interne de l'appareil sur votre ordinateur. (Pour **Windows**, les pilotes s'installeront automatiquement et l'appareil peut être ouvert dans **Poste de travail**. Sur **MacOS**, vous aurez besoin d'[Android File Transfer](https://www.android.com/intl/en_us/filetransfer/) de Google pour accéder aux fichiers de l'appareil.)

3. Sur votre appareil, naviguez vers le dossier **KoboCollect** (celui-ci se trouve dans le chemin ci-dessous) :

    `Phone\Android\data\org.koboc.collect.android\files\projects`

    Vous pouvez en savoir plus sur le chemin de stockage de l'appareil [ici](transferring_forms.md).

4. Copiez le dossier « instances » et collez-le quelque part sur votre ordinateur.

5. Si vous avez plus d'un appareil, répétez les étapes ci-dessus et renommez chacun des dossiers « instances » avec un nom ou un numéro unique.

6. Créez un fichier ZIP du dossier.

7. Suivez maintenant les [instructions décrites ci-dessous](#importer-un-fichier-zip-de-données) pour importer vos soumissions.

## Importer un fichier ZIP de données

1. Connectez-vous à votre compte KoboToolbox, puis visitez :
   `https://kc-eu.kobotoolbox.org/votre_nom_utilisateur/bulk-submission-form` OU
   `https://kc.kobotoolbox.org/votre_nom_utilisateur/bulk-submission-form` (selon l'endroit où vous vous êtes inscrit), et remplacez `votre_nom_utilisateur` par **votre propre nom d'utilisateur**.

2. Sélectionnez et téléversez le fichier ZIP. Tous les enregistrements seront téléversés sur le serveur, à condition qu'ils correspondent à un formulaire existant.

Une fois que toutes les instances ont été téléversées, vous verrez un message de confirmation pour chaque enregistrement. Si vous voyez un message d'expiration de délai, vous pouvez essayer de téléverser plusieurs fichiers ZIP plus petits avec moins d'enregistrements. Téléverser les mêmes enregistrements deux fois n'est pas un problème, car les enregistrements en double seront rejetés.