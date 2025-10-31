# Dépannage des formulaires web Enketo
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/troubleshooting_webforms.md" class="reference">15 février 2022</a>

[Les formulaires web Enketo](enketo.md) fonctionnent sur tous les appareils car ils s'ouvrent dans des navigateurs web classiques et permettent la collecte de données en ligne ou hors ligne. En général, nous recommandons vivement la dernière version de tous les
[navigateurs modernes](https://enke.to/modern-browsers). Vous pouvez également consulter
[la Foire aux questions d'Enketo](https://enketo.org/faq/#browsers) pour en savoir
plus sur _quels navigateurs sont pris en charge et recommandés_ par Enketo.

## Problèmes connus avec les formulaires hors ligne sur iOS

Les appareils iOS (fonctionnant sur iPhone et iPad) présentent plusieurs limitations connues lors de
l'utilisation de formulaires hors ligne en raison de la plateforme du système d'exploitation Apple. Nous
nous efforçons de prendre en charge entièrement la dernière version d'iOS.

-   La collecte de données hors ligne fonctionne dans tout navigateur moderne. Sur iOS, nous
    recommandons uniquement Chrome ou Safari.
-   La version 9.x affiche « NotFoundError: DOM IDBDatabase Exception 8 ». Solution :
    Fermez tous les onglets Enketo dans votre navigateur, puis rouvrez le formulaire. L'erreur
    devrait maintenant avoir disparu définitivement.
-   La version 9.3.1 affiche « Attempted to assign to readonly property » lors du chargement
    du formulaire hors ligne
-   La version 8.x affiche « undefined is not an object (evaluating 'c.resources') ».
    Solution : Mettez à jour vers la dernière version d'iOS

Si la collecte de données hors ligne n'est pas requise et que vous rencontrez une erreur sur iOS,
envisagez d'utiliser la _version en ligne uniquement_ au lieu de l'URL hors ligne.

## Perte de données

Lors de la collecte de données via Enketo, les utilisatrices et utilisateurs ne doivent jamais vider le cache du navigateur
(que ce soit manuellement ou en utilisant une application). Vider le cache de votre navigateur (pendant
la collecte de données) supprimera toutes les informations stockées dans le navigateur et donc
vos informations n'atteindront pas votre serveur KoboToolbox. Cette perte de données est
irréversible. Par conséquent, nous conseillons vivement aux utilisatrices et utilisateurs de vider le cache du navigateur si et
seulement si vous avez soumis avec succès toutes vos données à votre serveur KoboToolbox.