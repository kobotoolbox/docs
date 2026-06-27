# Résolution de problèmes liés aux formulaires web Enketo

Les [formulaires web Enketo](enketo.md) fonctionnent sur tous les appareils, car ils s'ouvrent dans des navigateurs web classiques et permettent la collecte de données en ligne ou hors ligne. Nous recommandons vivement d'utiliser la dernière version de tous les [navigateurs modernes](https://enke.to/modern-browsers). Vous pouvez également consulter la [Foire aux questions d'Enketo](https://enketo.org/faq/#browsers) pour en savoir plus sur _les navigateurs disponibles et recommandés_ par Enketo.

## Problèmes connus avec les formulaires hors ligne sur iOS

Les appareils iOS (iPhone et iPad) présentent plusieurs limitations connues lors de l'utilisation de formulaires avec mode hors ligne activé, en raison de la plateforme du système d'exploitation Apple. Nous nous efforçons de garantir la compatibilité avec la dernière version d'iOS.

-   La collecte de données hors ligne fonctionne dans n'importe quel navigateur moderne. Sur iOS, nous recommandons uniquement Chrome ou Safari.
-   La version 9.x affiche le message "NotFoundError: DOM IDBDatabase Exception 8". Solution : fermez tous les onglets Enketo dans votre navigateur, puis rouvrez le formulaire. L'erreur devrait disparaître définitivement.
-   La version 9.3.1 affiche le message "Attempted to assign to readonly property" lors du chargement du formulaire hors ligne.
-   La version 8.x affiche le message "undefined is not an object (evaluating 'c.resources')". Solution : mettez à jour iOS vers la dernière version disponible.

Si la collecte de données hors ligne n'est pas nécessaire et que vous rencontrez une erreur sur iOS, envisagez d'utiliser la _version en ligne uniquement_ plutôt que l'URL hors ligne.

## Perte de données

Lors de la collecte de données via Enketo, les utilisateurs ne doivent jamais vider le cache du navigateur (manuellement ou à l'aide d'une application). Vider le cache de votre navigateur pendant la collecte de données supprimera toutes les informations stockées dans le navigateur, et vos données n'atteindront pas votre serveur KoboToolbox. Cette perte de données est irréversible. Nous déconseillons donc fortement aux utilisateurs de vider le cache du navigateur, sauf si vous avez soumis avec succès toutes vos données à votre serveur KoboToolbox.