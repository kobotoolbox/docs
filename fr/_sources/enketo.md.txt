# Qu'est-ce que les formulaires web Enketo ?

Selon [Enketo.org](https://enketo.org), **Enketo** est le nom d'un projet open-source ainsi que le nom d'une application web open-source qui utilise un format de formulaire open-source répandu.

Enketo a été développé dans le prolongement d'un mémoire de master soutenu en 2009 à l'Université de Liverpool sur « l'applicabilité des [technologies web utilisables hors ligne](https://blog.enketo.org/offline-capable-web-applications/) pour la gestion de l'information dans l'aide humanitaire ».

Après une première année de développement, le projet a été adopté par [un laboratoire de l'Université Columbia](https://qsel.columbia.edu/products-tools/) et [lancé pour la première fois](https://blog.enketo.org/enketo-is-now-open-source-and-will-be-used-in-formhub/) en 2012. C'est ainsi qu'a débuté une vague d'[adoption](https://enketo.org/about/adoption/) par des entreprises et des organisations à travers le monde.

## Dans quel écosystème s'inscrit Enketo ?

Enketo fait partie de l'écosystème OpenRosa/ODK, ce qui signifie que :

1. Enketo peut être combiné avec d'autres outils pour créer de manière flexible un système de gestion de l'information complet. C'est ce qui a conduit à l'intégration d'Enketo dans KoboToolbox. Cela signifie également que le projet Enketo peut se concentrer uniquement sur la collecte de données et l'optimiser au maximum.
2. Enketo n'exige pas d'engagement à long terme de la part de l'utilisateur.

## Quelles sont les fonctionnalités générales ?

Les formulaires déployés avec Enketo :

-   fonctionnent hors ligne
-   disposent de thèmes et de widgets soignés
-   sont adaptés à l'impression
-   peuvent utiliser des logiques de saut et de validation très puissantes
-   fonctionnent sur tout appareil, mobile ou ordinateur de bureau, à condition de disposer d'un [navigateur suffisamment récent](https://enke.to/modern-browsers)

## Comment accéder à Enketo dans KoboToolbox ?

Chaque fois que vous ouvrez un formulaire en version web dans KoboToolbox, vous utilisez en réalité Enketo. Pour plus de détails, consultez notre article d'aide [Collecte de données via des formulaires web](../fr/data_through_webforms.md).

## Comment résoudre les problèmes liés à Enketo ?

Les formulaires web Enketo fonctionnent sur tous les appareils, car ils s'ouvrent dans des navigateurs web classiques et permettent la collecte de données en ligne ou hors ligne. En général, nous recommandons vivement d'utiliser la dernière version de tous les navigateurs modernes ; [consultez cette page pour plus de détails sur les navigateurs compatibles avec Enketo](https://enketo.org/faq/#browsers).

**Problèmes connus avec les formulaires hors ligne sur iOS**

Les appareils iOS (iPhone et iPad) présentent plusieurs limitations connues lors de l'utilisation de formulaires activés pour une utilisation hors ligne, en raison de la plateforme du système d'exploitation Apple. Nous nous efforçons de garantir une compatibilité complète avec la dernière version d'iOS.

-   La collecte de données hors ligne fonctionne dans tout navigateur moderne. Sur iOS, nous recommandons uniquement Chrome ou Safari.
-   La version 9.x affiche le message « NotFoundError: DOM IDBDatabase Exception 8 ». Solution : fermez tous les onglets Enketo dans votre navigateur, puis rouvrez le formulaire. L'erreur devrait disparaître définitivement.
-   La version 9.3.1 affiche « Attempted to assign to readonly property » lors du chargement d'un formulaire hors ligne.
-   La version 8.x affiche « undefined is not an object (evaluating 'c.resources') ». Solution : mettez à jour iOS vers la dernière version disponible.

Si la collecte de données hors ligne n'est pas nécessaire et que vous rencontrez une erreur sur iOS, envisagez d'utiliser la version _en ligne uniquement_ plutôt que l'URL hors ligne.

Pour plus de détails sur la résolution de problèmes, consultez notre article d'aide [Résolution des problèmes liés aux formulaires web Enketo](../fr/troubleshooting_webforms.md).