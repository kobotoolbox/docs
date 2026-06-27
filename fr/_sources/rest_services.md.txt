# Utiliser les services REST
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/7ca46b8455887292b012aeb709e7e244245bf6b9/source/rest_services.md" class="reference">7 juil. 2023</a>


**Comment lier vos données à d'autres serveurs ou services à l'aide des services REST**

KoboToolbox propose un certain nombre de fonctionnalités avancées intégrées, basées sur nos bibliothèques open source, qui incluent des suppléments utiles pour les cas d'utilisation avancés.

Vous pouvez lier les données collectées avec KoboToolbox à d'autres serveurs ou services que vous possédez via les services REST. Les services REST sont compatibles avec les formats JSON et XML, ainsi que l'authentification de base. Il est également possible d'envoyer uniquement un sous-ensemble de champs.

En cas d'échec, la tâche en arrière-plan effectuera 3 nouvelles tentatives d'envoi des données (la première après 60 secondes, la deuxième après 600 secondes, et la troisième après 6 000 secondes). Des notifications par e-mail peuvent être activées pour recevoir un rapport d'échec.

Notez que vos données sont envoyées au serveur externe uniquement lors de leur création. Rien n'est envoyé lorsque les données sont modifiées.

Voici quelques tutoriels vidéo sur l'utilisation des services REST :

1. Création

    [![Création](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Création")

2. Sous-ensemble de champs (Les champs sont ajoutés en appuyant sur « Entrée » ou « Tab »)

    [![Sous-ensemble de champs](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Sous-ensemble de champs")

3. Échec/Nouvelle tentative

    [![Échec / Nouvelle tentative](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Échec / Nouvelle tentative")

4. Wrapper personnalisé (Disponible uniquement avec le format JSON)

    [![Wrapper personnalisé](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Wrapper personnalisé")