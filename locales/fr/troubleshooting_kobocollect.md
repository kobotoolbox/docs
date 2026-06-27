# Résolution de problèmes liés à l'application Android KoboCollect

**-- Veuillez signaler tout problème non répertorié sur notre
[Forum communautaire](https://community.kobotoolbox.org/) --**

<p class="note">
    Pour en savoir plus sur la connexion de KoboCollect à votre compte KoboToolbox, la personnalisation des paramètres KoboCollect et la collecte de données avec l'application, consultez <a href="https://support.kobotoolbox.org/fr/kobocollect_on_android_latest.html">Configurer l'application KoboCollect</a>, <a href="https://support.kobotoolbox.org/fr/kobocollect_settings.html">Personnaliser les paramètres KoboCollect</a> et <a href="https://support.kobotoolbox.org/fr/data_collection_kobocollect.html">Collecte de données avec KoboCollect</a>.
</p>

_Messages d'erreur courants avec guides de résolution de problèmes :_

**Erreur : Message 'Error getting form list' après avoir sélectionné 'Download form'**

**Résolution :** Les solutions les plus probables à ce problème sont les suivantes :

1. Vérifiez votre URL. Il y a probablement une faute de frappe dans l'URL que vous avez saisie dans les paramètres. Consultez [cet article](kobocollect_on_android_latest.md) sur la configuration de votre téléphone ou tablette Android pour la collecte de données.

2. Une autre explication possible est que votre téléphone n'était pas connecté à Internet lorsque vous avez sélectionné **Download form**, par exemple si vous êtes connecté à un réseau WiFi public qui vous demande de vous identifier via votre navigateur. [Cet article](kobocollect_on_android_latest.md) explique plus en détail comment connecter votre appareil à votre compte.

**Erreur : Generic Exception: No peer certificate ou Form listing failed. Error: javx.net.ssl.SSLPeerUnverifiedException...**

Cette erreur apparaît lorsque KoboCollect tente de communiquer avec le serveur mais ne parvient pas à établir une connexion sécurisée (SSL/HTTPS).

**Résolution :**

1. Il est très probable que la date de votre appareil soit incorrecte. Vérifiez que la date est correcte, puis réessayez. _Veuillez consulter le manuel de votre téléphone ou tablette pour savoir comment régler la date._ Les appareils Android réinitialisent leur date à l'année 2000 ou à une autre année si la batterie atteint 0 %, ce qui explique pourquoi cette erreur peut apparaître fréquemment si votre équipe a tendance à décharger complètement la batterie.

2. Vous pouvez également voir ce message d'erreur si vous utilisez un point d'accès WiFi qui vous demande de vous identifier après la connexion.

**Erreur : KoboCollect a planté**

**Résolution :**

1. Si cela **se produit** lorsque vous tentez d'**envoyer des soumissions ou de télécharger un nouveau formulaire**, votre appareil subit une interruption importante de sa connexion Internet. Bien que cela puisse sembler alarmant, il n'y a aucun risque : répétez simplement le processus d'envoi ou de téléchargement.

2. Si cela **se produit** lorsque vous tentez d'**ouvrir un nouveau formulaire** sur votre téléphone, les raisons possibles suivantes peuvent vous aider à résoudre le problème :

    - Le formulaire que vous essayez d'ouvrir contient des erreurs dans les calculs, les contraintes ou les logiques de saut. Cela est rare, car le système aurait normalement déjà détecté ces erreurs.
    - Le formulaire que vous essayez d'ouvrir est soit trop volumineux, soit contient de nombreuses actions (calculs, longues listes de réponses ou autres procédures complexes) que la mémoire de votre appareil ne peut pas gérer. Veuillez consulter [cet article](devices_for_data_collection.md) sur les appareils recommandés.

**Erreur : Unable to edit this blank form because the corresponding blank form is not present or was deleted**

**Résolution :**

Ce type de message d'erreur apparaît lorsque vous essayez de modifier un formulaire enregistré alors que le formulaire vierge correspondant est absent ou a été supprimé.

Si cela se produit, récupérez le formulaire vierge correspondant depuis votre compte KoboToolbox en cliquant sur **Download form** sur l'écran d'accueil, puis sélectionnez le formulaire concerné qui nécessite des modifications.

**Erreur : Unable to install KoboCollect android app in a device. Shows the following error message (can't create directory/storage/sdcard0/odk)**

**Résolution :**

Ce message d'erreur s'affiche lorsque l'espace de stockage de votre appareil est insuffisant. Pour résoudre ce problème, libérez de l'espace sur votre appareil en désinstallant certaines applications inutiles, puis essayez à nouveau d'installer KoboCollect.