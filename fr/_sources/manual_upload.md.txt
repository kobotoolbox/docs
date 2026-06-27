# Télécharger manuellement des soumissions
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/manual_upload.md" class="reference">23 Apr 2026</a>


<p class="note">Veuillez noter qu'il s'agit encore d'une fonctionnalité expérimentale qui ne vous empêche pas de créer des soumissions en double.</p>

Dans certaines situations, il se peut que vous ne puissiez pas utiliser l'option d'importation standard après avoir collecté des données avec **KoboCollect** ou des **formulaires web**. Cela peut être dû à des problèmes liés à votre appareil mobile partiellement endommagé (par exemple, un écran brisé), ou au fait de vous trouver dans un endroit isolé sans accès à Internet. Vous pouvez télécharger vos soumissions depuis l'appareil de collecte de données vers votre ordinateur, puis les importer sur le serveur une fois que vous avez retrouvé une connexion Internet.

## Exporter des données depuis des formulaires web

1. Dans votre **formulaire web** disponible hors ligne, ouvrez le « Panneau latéral » en cliquant sur le crochet situé à gauche.

![Side Panel](/images/manual_upload/Side_Panel.png)

2. Cliquez sur le bouton **Export** et un fichier ZIP sera enregistré sur votre ordinateur. Si ce n'est pas le cas, cliquez à nouveau sur le bouton **Export**. Pour certains navigateurs, cela peut ne pas fonctionner et vous devrez cliquer sur le lien « alternative download - online », ce qui nécessitera une connexion Internet.

![Export](/images/manual_upload/Export.png)

3. Suivez maintenant les [instructions ci-dessous](#importing-a-data-zip-file) pour importer vos soumissions.

## Exporter des données depuis KoboCollect

1. Connectez l'appareil à votre ordinateur via un câble USB.

2. Ouvrez le stockage interne de l'appareil sur votre ordinateur. (Sous **Windows**, les pilotes s'installent automatiquement et l'appareil est accessible depuis **Poste de travail**. Sous **MacOS**, vous aurez besoin de [Android File Transfer](https://www.android.com/intl/en_us/filetransfer/) de Google pour accéder aux fichiers de l'appareil.)

3. Sur votre appareil, accédez au dossier **KoboCollect** (accessible via le chemin suivant) :

    `Phone\Android\data\org.koboc.collect.android\files\projects`

    Vous pouvez en savoir plus sur le chemin de stockage de l'appareil [ici](transferring_forms.md).

4. Copiez le dossier « instances » et collez-le à un emplacement de votre choix sur votre ordinateur.

5. Si vous disposez de plusieurs appareils, répétez les étapes ci-dessus et renommez chaque dossier « instances » avec un nom ou un numéro unique.

6. Créez un fichier ZIP du dossier.

7. Suivez maintenant les [instructions ci-dessous](#importing-a-data-zip-file) pour importer vos soumissions.

## Importer un fichier ZIP de données

1. Connectez-vous à votre compte KoboToolbox, puis accédez à :
   `https://kc-eu.kobotoolbox.org/your_username/bulk-submission-form` OU
   `https://kc.kobotoolbox.org/your_username/bulk-submission-form` (selon le serveur sur lequel vous vous êtes inscrit), et remplacez `your_username` par **votre propre nom d'utilisateur**.

2. Sélectionnez et importez le fichier ZIP. Tous les enregistrements seront importés sur le serveur, à condition qu'ils correspondent à un formulaire existant.

Une fois toutes les instances importées, un message de confirmation s'affichera pour chaque enregistrement. Si un message d'expiration apparaît, vous pouvez essayer d'importer plusieurs fichiers ZIP plus petits contenant moins d'enregistrements. Importer les mêmes enregistrements deux fois ne pose pas de problème, car les enregistrements en double seront rejetés.