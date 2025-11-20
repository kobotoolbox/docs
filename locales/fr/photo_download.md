# Télécharger des photos et autres médias
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/photo_download.md" class="reference">29 Jul 2025</a>

Si votre formulaire [inclut](question_types.md) une question de type photo, vidéo ou enregistrement audio, ces fichiers seront importés sur le serveur avec vos autres données. Lors de l'export de votre ensemble de données vers XLS ou CSV, ces fichiers incluront des références aux noms de fichiers des pièces jointes multimédias, mais pas les fichiers eux-mêmes. Pour télécharger tous vos fichiers multimédias en masse, choisissez l'option **Pièces jointes multimédias (ZIP)** sous **DONNÉES>Téléchargements>Sélectionner le type d'export**.

Ce qui suit explique d'autres options pour télécharger et accéder à vos fichiers multimédias collectés.

<p class='note'>L'export ZIP peut échouer pour les très grands projets en raison d'une limite de délai d'attente du serveur de 30 minutes. Si c'est le cas, veuillez suivre les méthodes ci-dessous pour extraire vos fichiers multimédias du serveur <strong>KoboToolbox</strong>.</p>

## Inclure des hyperliens directs vers les médias collectés dans l'export XLS

1. Accédez à **DONNÉES>Téléchargements** et développez la section **Options avancées**
2. Assurez-vous que l'option _Inclure les URL des médias_ est cochée (activée par défaut)

![Inclure les URL des médias](/images/photo_download/include_media_urls.png)

3. Cliquez sur **EXPORTER**

Si votre enquête comportait la question suivante :

**feuille survey**

| type  | name    | label              |
| :---- | :------ | :----------------- |
| image | image_1 | Soumettre une image |
| survey |

Et une soumission à cette question avec le nom de fichier « image.jpg », l'export aura le résultat suivant :

| image_1   | image_1_URL               |
| :-------- | :------------------------ |
| image.jpg | https://link/to/image.jpg |

## Pour les connexions lentes ou les très grands projets : Utiliser DownThemAll

La méthode de téléchargement ZIP inclura toujours tous les fichiers multimédias de votre projet. Cela peut prendre beaucoup de temps à télécharger en cas d'un grand nombre d'images ou de vidéos collectées ou en cas de connexion lente. Voici une solution de contournement pour télécharger tous (ou une sélection de) médias en utilisant le gestionnaire de téléchargement populaire **DownThemAll** (uniquement pris en charge par le navigateur Firefox) :

1. Enregistrez votre fichier Excel avec les hyperliens ajoutés (voir les instructions ci-dessus) en tant que fichier HTML sur votre Bureau, en utilisant l'option Fichier > Enregistrer sous... (choisissez « Page Web »)

2. Connectez-vous à votre compte KoboToolbox où vos photos sont hébergées en utilisant le navigateur Firefox

3. Dans Firefox, installez l'[extension DownThemAll](https://addons.mozilla.org/en-CA/firefox/addon/downthemall)

4. Toujours dans Firefox, ouvrez la page Web HTML enregistrée à l'**Étape 1**

5. Faites un clic droit quelque part sur cette page et choisissez _DownThemAll!_, ou cliquez sur le bouton de l'extension dans la barre d'outils de Firefox

6. Dans la fenêtre d'extension qui s'ouvre, cliquez sur **Télécharger**. Par défaut, Firefox enregistrera tous les fichiers dans le dossier Téléchargements de votre ordinateur (qui peut être modifié)

7. Optionnel : Dans la fenêtre qui s'ouvre, définissez une limite de vitesse de téléchargement pour éviter d'utiliser toute la bande passante disponible. Les paramètres vous permettent également de définir le nombre de tentatives qui doivent être effectuées pour chaque fichier en cas de problèmes de connexion.

Si vous avez beaucoup de fichiers multimédias, cela prendra un certain temps à télécharger. Mais le gestionnaire de téléchargement **DownThemAll** s'assurera que vous avez téléchargé toutes les images et vous informera au cas où certaines d'entre elles n'auraient pas été téléchargées afin que vous puissiez réessayer.

![Extension DownThemAll](/images/photo_download/downthemall_extension.jpg)

![Liens DownThemAll](/images/photo_download/downthemall_links.jpg)