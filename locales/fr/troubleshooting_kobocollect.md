# Dépannage de l'application Android KoboCollect
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/f6c6ac34b1fe55e7aab87f7b61c26e1607b4306b/source/troubleshooting_kobocollect.md" class="reference">24 Sep 2025</a>

**-- Veuillez signaler tout problème non couvert sur notre
[Forum communautaire](https://community.kobotoolbox.org/)--**

<p class="note">
    Pour en savoir plus sur la connexion de KoboCollect à votre compte KoboToolbox, la configuration des paramètres de KoboCollect et la collecte de données avec l'application, consultez <a href="kobocollect_on_android_latest.html">Premiers pas avec KoboCollect</a>, <a href="kobocollect_settings.html">Personnalisation des paramètres de KoboCollect</a> et <a href="data_collection_kobocollect.html">Collecte de données avec KoboCollect</a>.
</p>


_Messages d'erreur courants avec guides de dépannage :_

**Erreur : Message « Erreur lors de l'obtention de la liste des formulaires » après avoir sélectionné « Télécharger formulaire »**

**Dépannage :** Les solutions les plus probables à ce problème sont les suivantes

1. Vérifiez votre URL, vous avez très probablement une petite faute de frappe dans l'URL que vous avez saisie dans
   les paramètres. Consultez [cet article](kobocollect_on_android_latest.md) sur la configuration de
   votre téléphone/tablette Android pour la collecte de données.

2. Une autre explication possible est que votre téléphone n'était pas connecté à
   Internet lorsque vous avez sélectionné **Télécharger formulaire**, par exemple lorsque vous êtes
   connecté à un réseau WiFi dans un lieu public qui vous oblige à vous connecter
   via votre navigateur. [Cet article](kobocollect_on_android_latest.md) explique plus
   en détail comment connecter votre appareil à votre compte.

**Erreur : Exception générique : Aucun certificat homologue ou Échec de la liste des formulaires. Erreur :
javx.net.ssl.SSLPeerUnverifiedException...**

Cette erreur apparaît lorsque KoboCollect tente de communiquer avec le serveur mais
ne peut pas établir une connexion sécurisée (SSL/HTTPS).

**Dépannage :**

1. Il est très probable que votre appareil utilise la mauvaise date. Vérifiez que la date est
   correcte, puis réessayez. _Veuillez consulter le manuel de votre téléphone/tablette pour savoir comment
   régler la date._ Les appareils Android réinitialisent leurs dates à 2000 ou une autre année si
   jamais la batterie tombe à 0 %, c'est pourquoi cette erreur peut apparaître fréquemment si
   votre équipe a tendance à vider complètement la batterie.

2. Vous pouvez également voir ce message d'erreur si vous utilisez un point d'accès WiFi qui
   vous oblige à vous connecter après la connexion.

**Erreur : KoboCollect s'est arrêté**

**Dépannage :**

1. Si cela **se produit** pendant que vous essayez de **téléverser des soumissions ou de télécharger un
   nouveau formulaire**, alors votre appareil subit une interruption importante de sa connexion
   Internet. Bien que cela semble alarmant, c'est inoffensif : Répétez simplement le
   processus de téléversement ou de téléchargement.

2. Si cela **se produit** pendant que vous essayez d'**ouvrir un nouveau formulaire** sur votre téléphone,
   alors les raisons possibles suivantes pourraient vous aider à résoudre le problème :

    - Le formulaire que vous essayez d'ouvrir contient des erreurs soit dans les calculs,
      les contraintes ou les routines de saut. Ceci est rare car le système aurait déjà
      vérifié les erreurs.
    - Le formulaire que vous essayez d'ouvrir est soit trop volumineux, soit comporte de nombreuses
      actions (calculs, grande liste de réponses ou autres procédures
      complexes) qui ne peuvent pas être gérées par la capacité mémoire de votre appareil.
      Veuillez consulter [cet article](devices_for_data_collection.md) sur
      les appareils recommandés.

**Erreur : Impossible de modifier ce formulaire vierge car le formulaire vierge correspondant n'est
pas présent ou a été supprimé**

**Dépannage :**

Ce type de message d'erreur se produit lorsque vous essayez de modifier votre formulaire enregistré alors que le
formulaire vierge correspondant n'est pas présent ou a été supprimé.

Si cela se produit, récupérez le formulaire vierge correspondant depuis votre compte
KoboToolbox en cliquant sur **Télécharger formulaire** sur l'écran d'accueil, puis sélectionnez le
formulaire particulier qui nécessite des modifications.

**Erreur : Impossible d'installer l'application Android KoboCollect sur un appareil. Affiche le
message d'erreur suivant (impossible de créer le répertoire/storage/sdcard0/odk)**

**Dépannage :**

Vous voyez ce message d'erreur lorsque votre appareil manque d'espace de stockage. Pour résoudre
ce problème, libérez de l'espace sur votre appareil en désinstallant certaines applications inutiles, puis essayez
d'installer KoboCollect.