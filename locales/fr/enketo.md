# Que sont les formulaires Web Enketo ?
<a href="../enketo.html">Read in English</a> | <a href="../es/enketo.html">Leer en español</a> | <a href="../ar/enketo.html">اقرأ باللغة العربية</a>

**Dernière mise à jour :**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/enketo.md" class="reference">15
fév. 2022</a>

Selon [Enketo.org](https://enketo.org), **Enketo** est le nom d'un
projet open-source ainsi que le nom d'une application Web open-source qui
utilise un format de formulaire open-source populaire.

Enketo a été développé à la suite d'une thèse de Master de 2009 à
l'Université de Liverpool sur « l'applicabilité des
[technologies Web compatibles hors ligne](https://blog.enketo.org/offline-capable-web-applications/)
pour la gestion de l'information dans l'aide humanitaire ».

Après un an de développement initial, il a été adopté par
[un laboratoire de l'Université Columbia](https://qsel.columbia.edu/products-tools/) et
[lancé pour la première fois](https://blog.enketo.org/enketo-is-now-open-source-and-will-be-used-in-formhub/)
en 2012. Ce fut le début d'une cascade
[d'adoption](https://enketo.org/about/adoption/) par des entreprises et des organisations
à travers le monde.

## Quel écosystème Enketo utilise-t-il ?

Enketo fait partie de l'écosystème OpenRosa/ODK, ce qui signifie :

1. Enketo peut être combiné avec d'autres outils pour créer de manière flexible un système
   de gestion de l'information complet. Cela a conduit à l'adoption d'Enketo
   dans KoboToolbox. Cela signifie également que le projet Enketo peut se concentrer uniquement
   sur la collecte de données et le faire de la meilleure façon possible.
2. Enketo ne nécessite pas d'engagement à long terme de la part de l'utilisatrice ou l'utilisateur.

## Quelles sont les fonctionnalités générales ?

Les enquêtes déployées avec Enketo :

-   fonctionnent hors ligne
-   ont de beaux thèmes et widgets
-   sont adaptées à l'impression
-   peuvent utiliser une logique de saut et de validation très puissante
-   fonctionnent sur n'importe quel appareil, mobile ou ordinateur, tant qu'il dispose d'un
    [navigateur moderne](https://enke.to/modern-browsers)

## Comment puis-je accéder à Enketo dans KoboToolbox ?

Chaque fois que vous ouvrez un formulaire sur la version webform dans KoboToolbox, vous
utilisez en fait Enketo. Pour plus de détails, veuillez consulter notre article d'assistance
[Collecter des données via des formulaires Web](data_through_webforms.md).

## Comment résoudre les problèmes avec Enketo ?

Les formulaires Web Enketo fonctionnent sur tous les appareils car ils s'ouvrent dans des navigateurs Web ordinaires et
permettent la collecte de données en ligne ou hors ligne. En général, nous recommandons fortement la
dernière version de tous les navigateurs modernes ;
[voir ici pour plus de détails sur les navigateurs fonctionnant avec Enketo](https://enketo.org/faq/#browsers).

**Problèmes connus avec les formulaires hors ligne sur iOS**

Les appareils iOS (fonctionnant sur iPhone et iPad) présentent plusieurs limitations connues avec
l'utilisation de formulaires hors ligne en raison de la plateforme du système d'exploitation Apple. Nous
nous efforçons de prendre en charge entièrement la dernière version d'iOS.

-   La collecte de données hors ligne fonctionne dans n'importe quel navigateur moderne. Sur iOS, nous
    recommandons uniquement Chrome ou Safari.
-   La version 9.x affiche « NotFoundError: DOM IDBDatabase Exception 8 ». Solution :
    Fermez tous les onglets Enketo dans votre navigateur, puis rouvrez le formulaire. L'erreur
    devrait maintenant avoir disparu définitivement.
-   La version 9.3.1 affiche « Attempted to assign to readonly property » lors du chargement
    du formulaire hors ligne
-   La version 8.x affiche « undefined is not an object (evaluating 'c.resources') ».
    Solution : Mettez à jour vers la dernière version d'iOS

Si la collecte de données hors ligne n'est pas requise et que vous voyez une erreur sur iOS,
envisagez d'utiliser la version _en ligne uniquement_ au lieu de l'URL hors ligne.

Pour plus de détails sur le dépannage, veuillez consulter notre article d'assistance
[Résolution des problèmes avec les formulaires Web Enketo](troubleshooting_webforms.md).