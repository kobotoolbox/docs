# Collecte de données via les formulaires Web
<a href="../data_through_webforms.html">Read in English</a> | <a href="../es/data_through_webforms.html">Leer en español</a> | <a href="../ar/data_through_webforms.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/9153704b013430e55a763ac5c392dd30ae5d6bb9/source/data_through_webforms.md" class="reference">24 Sep 2025</a>

## Que sont les formulaires Web ?

Les [formulaires Web Enketo](enketo.md) sont utilisés par KoboToolbox pour prévisualiser vos formulaires et
pour saisir des données directement sur votre ordinateur. Vous pouvez également utiliser les formulaires Web pour
collecter des données sur vos appareils mobiles - même si vous êtes hors ligne au moment de
la collecte de données. Cela fonctionne sur pratiquement tous les appareils, y compris les iPhone, iPad, ou
tout autre smartphone, tablette ou ordinateur. Certaines fonctionnalités sont encore en cours de
développement actif pour Enketo, donc certaines questions spéciales peuvent ne pas être entièrement
prises en charge sur tous les appareils.

## Pourquoi ai-je besoin de formulaires Web au lieu de l'application Android KoboCollect ?

Vous utiliserez toujours les formulaires Web Enketo si vous n'utilisez pas [l'application KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) sur un
appareil Android pour la collecte de données. Cependant, il existe également certains paramètres d'apparence
comme likert pour le type de question à choix unique, multiline pour le type de question texte, etc. et des paramètres de style pour la Mise en page et les paramètres de KoboToolbox qui fonctionnent mieux sur les formulaires Web par rapport à l'application KoboCollect.

## Comment utiliser les formulaires Web pour la collecte de données ?

### Paramètres de collecte :

Pour commencer à collecter des données, vous devrez d'abord déployer votre projet. Une fois votre
projet déployé, vous verrez un écran comme celui illustré ci-dessous avec des options sur la façon de
**Collecter des données**.

![image](/images/data_through_webforms/collection_settings.png)

Dans le menu déroulant sous **Collecter des données**, vous avez plusieurs options disponibles
pour les formulaires Web :

**En ligne-Hors ligne (soumissions multiples) :** Cela permet les soumissions en ligne et hors ligne et est la meilleure option pour collecter des données sur le terrain.

**En ligne uniquement (soumissions multiples) :** C'est la meilleure option pour saisir
de nombreux enregistrements à la fois sur un ordinateur, par exemple pour transcrire des enregistrements papier.

**En ligne uniquement (soumission unique) :** Cela permet une seule soumission et peut être
associé au paramètre 'return_url' (expliqué ci-dessous) pour rediriger l'utilisatrice ou l'utilisateur vers
une URL de votre choix après que le formulaire a été soumis.

**En ligne uniquement (une fois par répondant) :** Cela permet à votre formulaire Web d'être
soumis une seule fois par utilisatrice ou utilisateur, en utilisant une protection de base pour empêcher la même utilisatrice ou le même utilisateur (sur le
même navigateur et appareil) de soumettre plus d'une fois.

**Code de formulaire Web intégrable :** Utilisez cet extrait de code html5 pour intégrer votre formulaire
sur votre propre site Web en utilisant des marges plus petites.

**Affichage uniquement :** Utilisez cette version pour tester, obtenir des commentaires. Ne permet pas de
soumettre des données.

**Application Android :** Utilisez cette option pour collecter des données sur le terrain avec votre
appareil Android.

### Démarrer la collecte de données :

Sélectionnez une option appropriée dans le menu déroulant **Collecter des données** puis appuyez sur COPIER
pour copier le lien de l'enquête à partager avec d'autres ou appuyez sur OUVRIR pour ouvrir le formulaire d'enquête dans un nouvel onglet de votre navigateur. Une fois le formulaire ouvert, vous devriez voir un
écran comme celui illustré dans l'image ci-dessous :

![image](/images/data_through_webforms/data_collection.jpg)

**1. Barres de signal :** Les barres de signal indiquent si le formulaire peut être lancé
hors ligne ou non. Les formulaires Web sont conçus pour pouvoir collecter des données pendant que vous êtes
hors ligne, cependant, il est essentiel de visiter l'URL du formulaire avec une connexion Internet
avant de passer hors ligne. Une fois que votre formulaire a été chargé et mis en cache,
vous verrez l'icône de disponibilité hors ligne (« barres de signal » vides et une coche)
dans le coin supérieur gauche indiquant que vous pouvez maintenant accéder au formulaire hors ligne.

**2. Icône d'imprimante :** L'icône d'imprimante vous donne accès pour imprimer votre formulaire ou
l'enregistrer en version PDF. Pour cela, appuyez sur l'icône d'imprimante puis sélectionnez
Destination (une imprimante appropriée connectée à votre appareil pour imprimer votre
formulaire d'enquête ou Enregistrer au format PDF pour enregistrer votre formulaire d'enquête au format PDF).

**3. Choisir la langue :** Cette fonctionnalité dans le formulaire Web est activée si vous avez
plusieurs langues pour votre projet d'enquête. Vous pouvez basculer entre la
langue par défaut et les autres langues présentes dans votre formulaire d'enquête.

**4. Sauvegarder le brouillon :** Utilisez cette fonctionnalité pour modifier ou mettre à jour vos enregistrements avant
de les soumettre au serveur KoboToolbox. Une fois que vous avez coché Sauvegarder le brouillon, vous
aurez une option pour Sauvegarder le brouillon. L'enregistrement brouillon est mis en file d'attente mais ne se
synchronise pas avec le serveur KoboToolbox. Pour le synchroniser avec le serveur, vous devrez ouvrir
l'enregistrement depuis la liste en file d'attente et décocher Sauvegarder le brouillon et appuyer sur Soumettre.

**5. Soumettre :** Appuyez sur le bouton Soumettre si vous avez terminé de collecter
des informations et souhaitez envoyer le formulaire rempli au serveur KoboToolbox. Après
avoir appuyé sur le bouton Soumettre, vous n'aurez pas la possibilité de modifier les enregistrements sur
votre appareil.

**6. Compteur d'enregistrements en file d'attente :** Le compteur d'enregistrements en file d'attente vous montre le nombre total
d'enregistrements soumis et en attente d'être importés sur un serveur. Les enregistrements en file d'attente
sont importés automatiquement en arrière-plan toutes les 5 minutes lorsque la
page Web est ouverte et qu'une connexion Internet est disponible.

**7. Volet des enregistrements en file d'attente :** Cliquer sur le bouton latéral vous montre les enregistrements qui
sont disponibles en tant que brouillons (qui peuvent encore être modifiés) et les enregistrements soumis finalisés en file d'attente pour être soit importés sur votre serveur avec une connexion Internet,
soit exportés sous forme de fichier zip comme indiqué dans
[l'article d'assistance ici](manual_upload.md).

## Comment enregistrer un formulaire Web hors ligne sur un appareil mobile ?

Suivez les étapes décrites ci-dessous pour enregistrer un formulaire et collecter des données dans un formulaire Web
en utilisant un appareil mobile :

1. Connectez votre appareil à Internet.

2. Ouvrez un navigateur Web disponible (Chrome préféré) sur votre appareil mobile.

3. Tapez ou collez l'URL de votre formulaire Web pour ouvrir une page de formulaire qui ressemble à
   celle illustrée ci-dessous :

    ![image](/images/data_through_webforms/offline_webform.jpg)

4. Cliquez sur l'icône des 3 POINTS en haut à droite (encerclée dans l'image ci-dessus) et
   sélectionnez AJOUTER À L'ÉCRAN D'ACCUEIL pour créer un raccourci vers votre appareil.

5. Une fenêtre apparaîtra pour saisir un nom pour le raccourci de votre projet. Nommez le
   raccourci puis appuyez sur AJOUTER.

6. Vous verrez maintenant une icône de raccourci de formulaire Web KoboToolbox sur votre appareil, similaire
   à ce qui est illustré ci-dessous :

    ![image](/images/data_through_webforms/kobo_icon.png)

7. Sélectionnez l'icône de raccourci pour commencer à collecter des données pour votre projet d'enquête.

## Redirection après soumission

Par défaut, le formulaire se rafraîchit pour la prochaine saisie une fois que les données ont été
soumises. Si les utilisatrices et utilisateurs ne sont censés saisir qu'une seule entrée (par exemple dans une enquête en ligne),
vous pouvez les envoyer vers un autre site Web après la soumission. Pour utiliser cette
fonctionnalité, vous devez 1) utiliser le formulaire En ligne uniquement du formulaire, et 2) ajouter
`?return_url=https://www.somewebsite.com` à votre URL.

![image](/images/data_through_webforms/url-single.png)

## Dépannage des formulaires Web

Utilisez toujours la dernière version du navigateur. Nous recommandons aux utilisatrices et utilisateurs d'utiliser Chrome
comme navigateur lorsqu'ils travaillent avec des formulaires Web. Pour d'autres détails sur
le dépannage des formulaires Web, veuillez consulter notre
[article d'assistance (Dépannage des formulaires Web Enketo) ici](troubleshooting_webforms.md).