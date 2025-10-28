# Services REST
<a href="../rest_services.html">Read in English</a> | <a href="../es/rest_services.html">Leer en español</a> | <a href="../ar/rest_services.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/7ca46b8455887292b012aeb709e7e244245bf6b9/source/rest_services.md" class="reference">7 juil. 2023</a>

**Comment lier vos données à d'autres serveurs ou services à l'aide des Services REST**

KoboToolbox dispose d'un certain nombre de fonctionnalités avancées intégrées basées sur nos bibliothèques open source, qui incluent des modules complémentaires utiles pour des cas d'usage avancés.

Vous pouvez lier vos données collectées avec KoboToolbox à d'autres serveurs ou services que vous pourriez posséder via les Services REST. Les Services REST prennent en charge les formats JSON ou XML, ainsi que l'authentification de base. De plus, il est possible d'envoyer uniquement un sous-ensemble de champs.

En cas d'échec, la tâche en arrière-plan réessaiera 3 fois d'envoyer les données (première fois après 60 secondes, deuxième fois après 600 secondes, et troisième fois après 6 000 secondes). Les notifications par e-mail peuvent être activées pour recevoir un rapport d'échec.

Notez que vos données sont envoyées au serveur externe uniquement lors de la création. Rien n'est envoyé lorsque les données sont modifiées.

Voici quelques vidéos tutorielles pour utiliser les Services REST :

1. Création

    [![Création](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Création")

2. Sous-ensemble de champs (Les champs sont ajoutés en appuyant sur « Entrée » ou « Tab »)

    [![Sous-ensemble de champs](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Sous-ensemble de champs")

3. Échec/Nouvelle tentative

    [![Échec / Nouvelle tentative](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Échec / Nouvelle tentative")

4. Wrapper personnalisé (Disponible uniquement avec le format JSON)

    [![Wrapper personnalisé](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Wrapper personnalisé")