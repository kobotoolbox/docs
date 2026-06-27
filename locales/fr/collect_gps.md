# Collecter des données GPS avec KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/75a01d18e539cff0694a03ac2ffe032abb6a14d5/source/collect_gps.md" class="reference">23 Apr 2026</a>

KoboToolbox vous permet de collecter des données GPS dans vos formulaires, y compris en mode hors ligne. Les questions GPS peuvent capturer **un emplacement unique, un itinéraire ou une zone** lors de la collecte de données. Cela est utile pour des tâches telles que la cartographie d'infrastructures, le suivi de visites terrain, la surveillance de sites environnementaux ou l'enregistrement de lieux de service. Les données GPS peuvent être collectées à la fois avec des [formulaires web](../fr/data_through_webforms.html) et avec [KoboCollect](../fr/data_collection_kobocollect.html).

Cet article explique comment collecter des données GPS dans KoboToolbox, notamment les types de questions GPS disponibles, la façon dont les données GPS sont collectées dans les formulaires web et dans KoboCollect, comment utiliser les données GPS dans une logique de formulaire avancée, comment gérer les données GPS dans KoboToolbox, et comment résoudre les problèmes GPS courants.

## Configurer votre formulaire pour collecter des données GPS

KoboToolbox propose trois types de questions GPS pour collecter des données géographiques directement dans un formulaire, plusieurs options de métadonnées qui collectent automatiquement des informations de localisation en arrière-plan, ainsi que des questions à choix multiple basées sur une carte dans XLSForm.

### Types de questions GPS

Les questions GPS sont visibles par les répondants. Elles leur permettent de collecter des coordonnées GPS en sélectionnant manuellement ou en enregistrant automatiquement un point unique, une ligne ou une zone. Les types de questions GPS suivants sont disponibles dans KoboToolbox :

| Formbuilder | XLSForm | Description |
| :--- | :--- | :--- |
| Position | `geopoint` | Collecte un emplacement géographique unique, tel que les coordonnées d'une école, d'une clinique ou d'un ménage. |
| Ligne | `geotrace` | Collecte plusieurs points GPS formant une ligne, comme un chemin, une route ou un itinéraire. |
| Zone | `geoshape` | Collecte plusieurs points GPS formant une zone délimitée, comme une parcelle de terrain ou un champ. |

<p class="note">
Pour en savoir plus sur l'ajout de questions GPS à vos formulaires, consultez l'article <a href="../fr/gps_questions.html">Questions GPS dans KoboToolbox</a> et <a href="../fr/question_types_xls.html#gps-question-types">Types de questions dans XLSForm</a>.
</p>

### Questions de métadonnées GPS

Les questions de métadonnées GPS ne sont pas visibles par les répondants. Lorsqu'elles sont activées, elles collectent automatiquement des données GPS en arrière-plan pendant la complétion du formulaire. Les types de questions de métadonnées suivants sont disponibles dans KoboToolbox :

| Formbuilder | XLSForm | Description |
| :--- | :--- | :--- |
| audit | `audit` | Enregistre des informations détaillées sur la localisation GPS et d'autres informations d'audit pendant la complétion du formulaire, y compris les informations de localisation pour chaque question au fur et à mesure que le formulaire est rempli. |
| start geopoint early | `start-geopoint` | Capture automatiquement un emplacement unique en arrière-plan à l'ouverture du formulaire. |
| *Non disponible* | `background-geopoint` | Capture automatiquement un emplacement unique en arrière-plan après que les répondants ont répondu à une question spécifique. |

<p class="note">
Pour en savoir plus sur l'ajout de métadonnées GPS à vos formulaires, consultez l'article <a href="../fr/form_meta.html#">Ajouter des métadonnées dans le Formbuilder</a> et <a href="../fr/metadata_xls.html#">Métadonnées de formulaires dans XLSForm</a>.
</p>

### Sélectionner des options à partir d'une carte

En plus de collecter des coordonnées GPS, vous pouvez également permettre aux répondants de sélectionner des emplacements prédéfinis sur une carte dans XLSForm. Cette fonctionnalité est configurée à l'aide d'une **question à choix multiple** avec l'apparence `map` ou `quick map`, ainsi qu'une colonne `geometry` dans l'onglet choices qui stocke les coordonnées de chaque choix.

<p class="note">
Pour en savoir plus sur la configuration de questions de sélection à partir d'une carte, consultez l'article <a href="../fr/select_from_map_xls.html">Sélectionner des options à partir d'une carte</a>.
</p>

## Collecter des données GPS

Les données GPS peuvent être collectées à la fois dans des [formulaires web](../fr/data_through_webforms.html) et dans l'application [KoboCollect](../fr/data_collection_kobocollect.html), mais le processus de collecte diffère entre les deux.

### Formulaires web

Lorsque vous utilisez des formulaires web, les répondants peuvent saisir des données GPS de plusieurs façons :

- Détecter la position actuelle de l'appareil
- Sélectionner un emplacement directement sur la carte
- Rechercher une adresse
- Saisir manuellement des coordonnées GPS

Pour les questions de type Ligne et Zone, les répondants peuvent ajouter plusieurs points sur la carte pour créer un itinéraire ou un polygone.

![Localisation GPS](images/collect_gps/webform.png)

<p class="note">
<strong>Note :</strong>
Vous pouvez détecter la position actuelle de l'appareil en cliquant sur le <strong>bouton de ciblage de localisation</strong> en haut à droite, à côté de la barre de recherche.
</p>

Vous pouvez utiliser des [apparences](../fr/gps_questions.html#advanced-appearances) pour modifier l'affichage de la question GPS dans les formulaires web, notamment pour masquer les champs de saisie des coordonnées GPS. Cependant, les formulaires web ne permettent pas d'empêcher entièrement la sélection manuelle d'un emplacement. Si vous souhaitez capturer automatiquement un emplacement sans autoriser la sélection manuelle, utilisez plutôt **background-geopoint**.

### KoboCollect

<iframe src="https://www.youtube.com/embed/akG0_cESv6U?si=vB9ByYkcP74Neu8x&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Dans KoboCollect, les données GPS sont capturées automatiquement à partir de la position actuelle de l'appareil lorsque l'utilisateur appuie sur un bouton. La sélection manuelle d'un emplacement n'est pas activée par défaut pour les questions de type Point, bien que des [apparences](../fr/gps_questions.html#advanced-appearances) supplémentaires puissent modifier le comportement des questions GPS.

La méthode de capture dans KoboCollect varie selon le type de question :

| Type de question | Capture des données GPS |
| :--- | :--- |
| Position / `geopoint` | Appuyez sur **Get point** pour commencer à capturer la position de l'appareil. <br><ul><li>Une fois que l'appareil atteint la précision cible par défaut de **5 mètres ou mieux**, le point est enregistré automatiquement.</li><li>L'enquêteur peut également appuyer sur **Save** pour enregistrer la position actuelle manuellement avant d'atteindre cette précision.</li></ul> |
| Ligne / `geotrace` | Appuyez sur **Get line** et cliquez sur <i class="k-icon-qt-point"></i> pour choisir une méthode de saisie. Les méthodes disponibles sont : <br><ul><li><strong>Placement en tapotant :</strong> L'enquêteur appuie manuellement sur des points de la carte pour tracer la ligne.</li><li><strong>Enregistrement manuel de la localisation :</strong> L'enquêteur se déplace vers chaque emplacement et appuie sur Record a Point pour capturer chaque point à partir de la position actuelle de l'appareil.</li><li><strong>Enregistrement automatique de la localisation :</strong> L'application enregistre automatiquement les points pendant que l'enquêteur se déplace, selon un intervalle de temps sélectionné et une précision requise.</li></ul>Une ligne nécessite au moins deux points. Après avoir enregistré vos points, cliquez sur le bouton **Save** en bas à gauche. |
| Zone / `geoshape` | Appuyez sur **Get polygon** et cliquez sur <i class="k-icon-qt-point"></i> pour choisir une méthode de saisie. Les mêmes méthodes de saisie que ci-dessus sont disponibles, mais pour créer une zone délimitée plutôt qu'une ligne. Une zone nécessite au moins trois points. |

Au-delà du comportement par défaut, vous pouvez utiliser des [apparences](../fr/gps_questions.html#advanced-appearances) pour modifier le fonctionnement des questions GPS dans KoboCollect. Par exemple, vous pouvez utiliser des apparences pour :

- Afficher une carte de l'emplacement sélectionné automatiquement
- Activer la sélection manuelle d'un emplacement

<p class="note">
Pour en savoir plus sur les apparences des questions GPS, consultez l'article <a href="../fr/gps_questions.html#advanced-appearances">Questions GPS dans KoboToolbox</a>.
</p>

Vous pouvez également configurer les paramètres de carte de KoboCollect pour contrôler l'affichage des cartes pour les questions basées sur le GPS, notamment en définissant la source de la carte, en sélectionnant un style de carte et en ajoutant des [couches de carte hors ligne](https://docs.getodk.org/collect-offline-maps/).

<p class="note">
Pour en savoir plus sur les paramètres de carte de KoboCollect, consultez l'article <a href="../fr/kobocollect_settings.html#maps-settings">Personnaliser les paramètres KoboCollect</a>.
</p>

## Améliorer la précision GPS

La précision GPS dépend à la fois de l'appareil et de l'environnement. Elle peut être affectée par des facteurs tels que l'activation du GPS sur l'appareil et la présence d'un capteur GPS intégré, la date à laquelle l'appareil a déterminé sa position pour la dernière fois, l'utilisation de services de localisation par satellite ou par réseau, et les conditions environnementales telles que la couverture nuageuse ou la proximité de bâtiments et d'arbres.

### Paramètres GPS

Lors de la création de formulaires dans XLSForm, vous pouvez utiliser des [paramètres](../fr/question_options_xls.html#question-parameters) pour contrôler la précision GPS de manière plus précise.

Les paramètres courants sont les suivants :

| Paramètre | Exemple | Description |
| :--- | :--- | :--- |
| `capture-accuracy` | `capture-accuracy=15` | Capture automatiquement le point une fois que l'appareil atteint la précision cible. Si défini comme 0, l'enquêteur doit explicitement accepter le point. La valeur par défaut est de 5 mètres. |
| `warning-accuracy` | `warning-accuracy=30` | Déclenche un message d'avertissement si la précision GPS n'est pas dans le seuil de précision spécifié. Cela n'empêche pas l'enregistrement du point. La valeur par défaut est de 100 mètres. |

<p class="note">
<strong>Note :</strong>
Pour la plupart des flux de travail, une valeur de <strong>capture-accuracy</strong> d'environ <strong>5 mètres</strong> est un objectif pratique. En général, il n'est pas recommandé de définir la cible en dessous de <strong>3 mètres</strong> à moins d'utiliser un appareil GPS externe, car le GPS intégré des appareils n'est souvent pas suffisamment précis pour atteindre ce niveau de manière fiable.
</p>

### Recommandations pour améliorer la précision GPS

Pour améliorer la précision GPS :

- Collectez des données en extérieur dans un espace dégagé avec une vue dégagée du ciel
- Éloignez-vous des bâtiments, des arbres et autres obstacles
- Assurez-vous que votre corps ne bloque pas la vue du ciel pour l'appareil
- Préchauffez le GPS de votre appareil en incluant `start-geopoint` au début de votre formulaire
- Activez le GPS assisté sur l'appareil si disponible

## Logique de formulaire avancée avec les données GPS

KoboToolbox prend en charge une logique de formulaire avancée avec les données GPS dans XLSForm. Par exemple, vous pouvez utiliser des fonctions GPS dans des calculs, des contraintes et une logique de saut pour mesurer une distance, un périmètre ou une superficie, ou pour vérifier si un emplacement se trouve dans une zone délimitée.

![Calculer la distance d'un itinéraire](images/collect_gps/calculate.png)

Les fonctions GPS courantes sont les suivantes :

| Fonction | Description |
| :--- | :--- |
| `area(${geoshape})` | Retourne la superficie, en mètres carrés, d'une valeur `geoshape`. |
| `distance(geo)` | Retourne la distance, en mètres, de : <ul><li>le périmètre d'une valeur `geoshape`</li><li>la longueur d'une valeur `geotrace`</li><li>une liste de geopoints spécifiés sous forme de chaînes de caractères ou de références à d'autres champs (y compris depuis des groupes répétés), séparés par des virgules</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Retourne `TRUE` si le `${geopoint}` spécifié se trouve à l'intérieur du `${geoshape}` spécifié, `FALSE` dans le cas contraire. Disponible uniquement dans KoboCollect. |

<p class="note">
Pour en savoir plus sur les fonctions permettant de manipuler des données GPS dans XLSForm, consultez l'article <a href="../fr/functions_xls.html#functions-to-manipulate-gps-data">Utiliser des fonctions avec XLSForm</a>.
</p>

## Gérer les données GPS

Après la collecte, les données GPS peuvent être consultées, cartographiées et exportées dans KoboToolbox.

### Afficher les données GPS dans le tableau de données

Les réponses GPS apparaissent dans le tableau de données comme les autres réponses du formulaire. Un point GPS unique est stocké sous la forme de quatre valeurs séparées par des espaces dans ce format : `latitude longitude altitude accuracy`.

Pour les questions de type Ligne et Zone, plusieurs points GPS sont stockés dans le même format et séparés par des points-virgules.

<p class="note">
Pour en savoir plus sur la consultation de vos données dans le tableau de données, consultez l'article <a href="../fr/viewing_validating_data.html">Voir et valider vos données</a>.
</p>

### Cartographier les données GPS dans KoboToolbox

KoboToolbox propose un mode **Carte** intégré pour visualiser les points GPS uniques. Cela facilite la consultation des emplacements où les soumissions ont été collectées, l'exploration des tendances spatiales et une meilleure compréhension de la distribution géographique de vos données.

<p class="note">
Pour en savoir plus sur le mode <strong>Carte</strong> dans KoboToolbox, consultez l'article <a href="../fr/mapping_gps.html">Cartographier vos données GPS</a>.
</p>

### Exporter les données GPS

Vous pouvez également exporter des données GPS depuis KoboToolbox pour les utiliser dans des logiciels externes. Les formats d'export disponibles couvrent différents flux de travail, de la révision et du nettoyage des données à la cartographie et à l'analyse géospatiale :

- **Les exports CSV et XLS** sont utiles pour travailler avec des données GPS dans un logiciel de tableur et peuvent également être importés dans de nombreux outils SIG, bien qu'ils nécessitent souvent une configuration supplémentaire, comme la définition des champs de coordonnées ou d'un système de référence de coordonnées.
- Pour les flux de travail SIG, le format **GeoJSON** est généralement recommandé car il fonctionne avec de nombreux outils tels qu'ArcGIS et QGIS.
- Le format **KML** est principalement destiné à la visualisation dans des applications telles que Google Earth et propose un style de carte de base, mais il est plus limité et ne doit être utilisé que lorsqu'il est requis pour un flux de travail spécifique.

<p class="note">
Pour en savoir plus sur l'export de vos données GPS pour une analyse externe, consultez l'article <a href="../fr/mapping_gps.html#exporting-gps-data">Exporter vos données GPS</a>.
</p>

## Résolution de problèmes

<details>
<summary><strong>La localisation GPS n'est pas capturée</strong></summary>
Vérifiez que les services de localisation et le GPS sont activés sur l'appareil et que l'appareil dispose d'un capteur GPS. Vous pouvez également tester le GPS avec une autre application pour confirmer que l'appareil peut déterminer une position. Pour de meilleurs résultats, déplacez-vous en extérieur, attendez un signal plus fort, éloignez-vous des bâtiments, des arbres et autres obstacles, et laissez à l'appareil le temps nécessaire pour obtenir sa première position GPS.
</details>

<br>

<details>
<summary><strong>La localisation GPS est incorrecte</strong></summary>
Si la position enregistrée semble incorrecte, l'appareil utilise peut-être la localisation par réseau plutôt que le GPS par satellite. Dans certains cas, désactiver la localisation par réseau dans les paramètres de l'appareil peut forcer KoboCollect à attendre la position GPS réelle.
</details>

<br>

<details>
<summary><strong>La précision GPS n'atteint pas le seuil cible</strong></summary>
Si un point n'atteint jamais la précision souhaitée, le seuil de <code>capture-accuracy</code> est peut-être trop strict pour l'appareil ou les conditions terrain.
</details>

<br>