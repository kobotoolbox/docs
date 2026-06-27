# Télécharger des photos et d'autres fichiers multimédias

Si votre formulaire [inclut](question_types.md) une question de type photo, vidéo ou enregistrement audio, ces fichiers seront importés sur le serveur avec vos autres données. Lors de l'export de votre base de données au format XLS ou CSV, ces fichiers incluront des références aux noms des fichiers multimédias joints, mais pas les fichiers eux-mêmes. Pour télécharger tous vos fichiers multimédias en une seule fois, choisissez l'option **Fichier média (ZIP)** sous **DONNÉES>Téléchargements>Sélectionner le type d'exportation**.

La section suivante présente d'autres options pour télécharger et accéder à vos fichiers multimédias collectés.

<p class='note'>L'export ZIP peut échouer pour les projets très volumineux en raison d'un délai d'expiration du serveur de 30 minutes. Si c'est le cas, veuillez suivre les méthodes ci-dessous pour extraire vos fichiers multimédias du serveur <strong>KoboToolbox</strong>.</p>

## Inclure des hyperliens directs vers les fichiers multimédias collectés dans l'export XLS

1. Accédez à **DONNÉES>Téléchargements** et développez la section **Options avancées**
2. Assurez-vous que l'option _Inclure les URL des médias_ est cochée (activée par défaut)

![Inclure les URL des médias](/images/photo_download/include_media_urls.png)

3. Cliquez sur **EXPORTER**

Si votre questionnaire contient la question suivante :

**onglet survey**

| type  | name    | label           |
| :---- | :------ | :-------------- |
| image | image_1 | Submit an image |
| survey |

Et qu'une soumission à cette question a pour nom de fichier « image.jpg », l'export aura le résultat suivant :

| image_1   | image_1_URL               |
| :-------- | :------------------------ |
| image.jpg | https://link/to/image.jpg |

## Pour les connexions lentes ou les projets très volumineux : utiliser DownThemAll

La méthode de téléchargement ZIP inclut toujours l'ensemble des fichiers multimédias de votre projet. Cela peut prendre beaucoup de temps en cas de grand nombre d'images ou de vidéos collectées, ou en cas de connexion lente. Voici une solution alternative pour télécharger tout ou une sélection de fichiers multimédias à l'aide du gestionnaire de téléchargement **DownThemAll** (uniquement compatible avec le navigateur Firefox) :

1. Enregistrez votre fichier Excel contenant les hyperliens ajoutés (voir les instructions ci-dessus) en tant que fichier HTML sur votre Bureau, via l'option Fichier > Enregistrer sous... (choisissez « Page web »)

2. Connectez-vous à votre compte KoboToolbox sur lequel vos photos sont hébergées, en utilisant le navigateur Firefox

3. Dans Firefox, installez l'[extension DownThemAll](https://addons.mozilla.org/en-CA/firefox/addon/downthemall)

4. Toujours dans Firefox, ouvrez la page web HTML enregistrée à l'**étape 1**

5. Faites un clic droit sur la page et choisissez _DownThemAll!_, ou cliquez sur le bouton de l'extension dans la barre d'outils Firefox

6. Dans la fenêtre de l'extension qui s'ouvre, cliquez sur **Download**. Par défaut, Firefox enregistre tous les fichiers dans le dossier Téléchargements de votre ordinateur (ce paramètre peut être modifié)

7. Facultatif : dans la fenêtre qui s'ouvre, définissez une limite de vitesse de téléchargement pour éviter d'utiliser toute la bande passante disponible. Les paramètres permettent également de définir le nombre de tentatives à effectuer pour chaque fichier en cas de problème de connexion.

Si vous avez un grand nombre de fichiers multimédias, le téléchargement prendra un certain temps. Cependant, le gestionnaire de téléchargement **DownThemAll** s'assurera que tous les fichiers ont bien été téléchargés et vous informera si certains ne l'ont pas été, afin que vous puissiez réessayer.

![Extension DownThemAll](/images/photo_download/downthemall_extension.jpg)

![Liens DownThemAll](/images/photo_download/downthemall_links.jpg)