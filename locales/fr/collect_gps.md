# Collecte de localisations GPS
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/collect_gps.md" class="reference">29 juil. 2025</a>

Les coordonnées de localisation peuvent être collectées facilement dans tous les formulaires avec les types de réponse « GPS ».

## Créer les différents types de questions GPS

Pour collecter des coordonnées GPS pendant le processus de collecte de données, il suffit d'ajouter une question GPS à votre formulaire. Il existe trois types de questions GPS : **Point**, **Ligne** et **Zone**

-   Lorsque vous utilisez l'**interface de création de formulaires**, ces types de questions se trouvent lorsque l'on clique sur le bouton d'ajout de question comme illustré ci-dessous.

![image](/images/collect_gps/formbuilder.jpg)

-   Lorsque vous utilisez la conception **XLSForm**, vous devez définir les types de questions comme ci-dessous pour obtenir la question souhaitée.

**Feuille survey**

| type     | name  | label                                 | hint                                                                                                       |
| :------- | :---- | :------------------------------------ | :--------------------------------------------------------------------------------------------------------- |
| geopoint | point | Enregistrez votre localisation actuelle | Cette question collecte une seule coordonnée GPS qui désigne un point unique                               |
| geotrace | line  | Enregistrez une ligne                 | Cette question collecte deux coordonnées pour former une ligne                                             |
| geoshape | area  | Enregistrez une zone                  | Cette question collecte des coordonnées GPS qui délimitent une boucle/zone fermée de n'importe quelle forme |
| survey |

## Collecter des données en utilisant les questions GPS

Pendant la saisie des données, l'enquêtrice ou l'enquêteur verra différentes options pour collecter les coordonnées, qui dépendent du type d'appareil de collecte de données et de l'approche.

## Collecter des données en utilisant les formulaires web Enketo

Le formulaire aura diverses options de collecte, notamment

**1. Collecte manuelle :** Appuyez simplement sur n'importe quel(s) point(s) sur la carte pour collecter les coordonnées de localisation ou vous pouvez saisir les coordonnées de latitude et de longitude si elles sont connues.

![image](/images/collect_gps/point_manual.png)

**2. Coller des points KML :** Collez les coordonnées KML dans la zone de texte qui apparaît.

![image](/images/collect_gps/kml.png)

**3. Détecter la localisation actuelle :** Cliquez simplement sur le bouton illustré ci-dessous pour collecter les coordonnées GPS actuelles de la localisation de l'appareil.

![image](/images/collect_gps/current_location.jpg)

## Collecter des données en utilisant KoboCollect

L'enquêtrice ou l'enquêteur verra diverses options selon le type de question GPS

**1. Coordonnée de point GPS unique**

-   L'enquêtrice ou l'enquêteur verra cet écran sur lequel elle ou il peut appuyer sur Démarrer le point.

![image](/images/collect_gps/geopoint.jpg)

-   Si l'enquêtrice ou l'enquêteur appuie sur Démarrer le point, elle ou il verra la localisation se charger et la précision atteinte. Si la question n'avait pas été configurée pour sélectionner un niveau de précision spécifique, elle attendra que l'enquêtrice ou l'enquêteur enregistre le point comme illustré ci-dessous.

![image](/images/collect_gps/autopoint.jpg)

**2. Ligne GPS**

-   Les enquêtrices et enquêteurs verront l'option suivante pour la question de ligne.

![image](/images/collect_gps/line.jpg)

-   S'ils appuient sur le bouton Démarrer la ligne, ils verront une option pour collecter la trace manuellement ou automatiquement comme indiqué ci-dessous.

![image](/images/collect_gps/trace_mode.jpg)

-   Si les enquêtrices et enquêteurs sélectionnent le mode manuel pour collecter les données, ils pourront sélectionner les points manuellement en appuyant sur les points de la carte. L'enquêtrice ou l'enquêteur devra sélectionner au moins deux coordonnées pour créer une trace de ligne.

-   Si les enquêtrices et enquêteurs sélectionnent le mode automatique, ils verront une option indiquant combien de temps le système doit attendre avant de collecter différents points, comme illustré dans la figure ci-dessous.

![image](/images/collect_gps/automodes.jpg)

**3. Zone GPS**

La zone GPS vous permet de collecter manuellement une zone GPS en mode manuel en appuyant sur la carte pour sélectionner les points qui créent le polygone ; les enquêtrices et enquêteurs devraient collecter au moins trois points pour créer un polygone.

## Précision des coordonnées GPS collectées

La précision du GPS collecté dépend de divers facteurs.

**Absence de capteur GPS ou GPS désactivé**

Lors de la collecte de coordonnées GPS, si l'appareil n'a pas de capteur GPS ou si le GPS est désactivé, une localisation peut être déterminée par d'autres moyens, qui peuvent ne pas être aussi précis. Les services de localisation sont contrôlés par l'appareil, et tous les appareils ne sont pas équipés d'un capteur GPS. Le GPS peut également être désactivé, ou l'appareil peut être configuré pour utiliser le WiFi et les réseaux cellulaires pour établir une localisation plutôt que d'utiliser des systèmes de navigation par satellite.

**Le temps nécessaire à un appareil pour déterminer ses coordonnées GPS varie fortement et peut dépendre de :**

-   La qualité du capteur GPS
-   Le temps écoulé depuis la dernière fois que l'appareil a déterminé sa localisation GPS
-   La couverture nuageuse
-   Les bâtiments ou autres structures obstruant la vue du ciel

**Pour obtenir un signal GPS, vous devez être à l'extérieur avec une bonne visibilité du ciel. Pour obtenir un signal GPS fort :**

-   Tenez-vous aussi loin que possible des bâtiments, des arbres ou d'autres structures
-   Assurez-vous que votre corps n'obstrue pas la vue du ciel
-   Obtenez une localisation GPS initiale au début de la journée avant de commencer à collecter des points sur le terrain
-   Activez l'A-GPS (assisté par réseau de données) sur votre appareil

<p class="note">GPS dans ce contexte ne fait pas exclusivement référence au <a class="reference" href="https://en.wikipedia.org/wiki/Global_Positioning_System">Global Positioning System</a> mais également à d'autres systèmes de navigation par satellite utilisés par les appareils mobiles, tels que <a class="reference" href="https://en.wikipedia.org/wiki/GLONASS">GLONASS</a>.</p>

## Dépannage

Si vous ne parvenez pas à obtenir une localisation GPS avec le type de réponse GPS, veuillez vérifier ces options :

-   Les paramètres de localisation sur votre appareil pour vous assurer que le GPS est activé
-   Installez une application gratuite qui utilise le GPS pour voir si vous pouvez obtenir une localisation GPS de cette façon (par exemple
    [GPS Status pour Android](https://play.google.com/store/apps/details?id=com.eclipsim.gpsstatus2)
    ou
    [GPS Status pour iPhone](https://apps.apple.com/ca/app/gps-status/id378085995)
-   Vérifiez les paramètres de votre téléphone/manuel du fabricant pour voir si l'appareil dispose du GPS
-   Si vos points GPS collectés pointent vers le mauvais emplacement, il est possible que votre appareil soit configuré pour collecter sa localisation à partir d'une tour de réseau qui a été achetée d'occasion et n'a pas été correctement réinitialisée avec la nouvelle localisation codée en dur. Vous pouvez éviter ce problème en désactivant la localisation réseau comme option dans les paramètres du système Android, forçant Collect à attendre la localisation GPS réelle.