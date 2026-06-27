# Questions GPS dans KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/gps_questions.md" class="reference">23 Apr 2026</a>

Les questions GPS permettent de **collecter des coordonnées géographiques et des données spatiales** lors de la collecte de données. Elles vous permettent de capturer des localisations précises, de cartographier des itinéraires ou de délimiter des zones directement dans votre formulaire. Ces types de questions sont utiles pour des activités telles que la cartographie d'infrastructures, le suivi de visites terrain, la surveillance de sites environnementaux ou l'enregistrement de lieux de prestation de services.

Cet article présente les types de questions GPS disponibles dans l'interface de création de formulaires KoboToolbox **(KoboToolbox Formbuilder)**, la manière de les ajouter et de les configurer, les différences de comportement entre les formulaires web et KoboCollect, ainsi que les options d'apparence avancées disponibles pour la collecte de données de localisation.

<p class="note">
<strong>Note :</strong> L'enregistrement de coordonnées GPS ne nécessite pas de connexion internet et est compatible avec la collecte de données hors ligne.
</p>

## Types de questions GPS

Les types de questions suivants sont disponibles dans le Formbuilder pour permettre aux répondants d'enregistrer des données GPS :

| Type de question | Description |
|:---|:---|
| <i class="k-icon-qt-point"></i> Position | Collecte une localisation géographique unique, par exemple les coordonnées d'une école, d'une clinique ou d'un logement. |
| <i class="k-icon-qt-line"></i> Ligne | Enregistre plusieurs points GPS formant une ligne, par exemple pour suivre un chemin, tracer un itinéraire ou cartographier un drain. |
| <i class="k-icon-qt-area"></i> Zone | Collecte des points formant une zone délimitée, par exemple une parcelle de terrain ou un champ. |

<p class="note">
<strong>Note :</strong> Vous pouvez également collecter automatiquement des données de localisation à l'aide de <a href="https://support.kobotoolbox.org/fr/form_meta.html">questions de métadonnées</a>. Les options <strong>start geopoint early</strong> et <strong>audit</strong> sont disponibles dans le Formbuilder, tandis que <code>background-geopoint</code> n'est disponible que lors de la création de votre formulaire <a href="https://support.kobotoolbox.org/fr/metadata_xls.html">dans XLSForm</a>.
</p>

## Ajouter une question GPS dans le Formbuilder

Pour ajouter une question GPS à votre formulaire :
1. Cliquez sur le bouton <i class="k-icon-plus"></i>.
2. Saisissez le libellé de votre question.
3. Cliquez sur **+ AJOUTER UNE QUESTION.**
4. Choisissez le type de question approprié.

![Question GPS](images/gps_questions/gps.png)

## Apparences des questions GPS

Le tableau ci-dessous présente les apparences par défaut des questions GPS :

![Apparences par défaut des questions GPS](images/gps_questions/table.png)

Dans les **formulaires web**, les répondants peuvent sélectionner une localisation directement sur la carte, rechercher une adresse ou saisir manuellement des coordonnées GPS.

Dans **KoboCollect**, la localisation actuelle de l'appareil est enregistrée automatiquement ; la sélection manuelle ou la saisie de coordonnées n'est pas disponible par défaut.

<p class="note">
<strong>Note :</strong> Pour en savoir plus sur les comportements de collecte de données GPS dans les formulaires web et KoboCollect, consultez l'article <a href="https://support.kobotoolbox.org/fr/collect_gps.html">Collecter des données GPS avec KoboToolbox</a>.
</p>

### Apparences avancées

Vous pouvez appliquer des apparences avancées aux questions GPS pour modifier leur affichage et leur comportement dans votre formulaire.

Pour ajouter une apparence avancée :
1. Ouvrez les paramètres de la question en cliquant sur <i class="k-icon-settings"></i> **Paramètres** à droite de la question. Vous accéderez alors à l'onglet **Options des questions**.
2. Dans **Apparence (avancée)**, saisissez le nom de l'apparence dans le champ de texte, exactement tel qu'il est indiqué ci-dessous.

![Apparence avancée de question GPS](images/gps_questions/appearance.png)

Les apparences avancées suivantes sont disponibles pour les questions GPS :

| Apparence | Description | Compatibilité |
|:---|:---|:---|
| <code>maps</code> | Affiche une carte permettant aux utilisateurs de visualiser la localisation en cours d'enregistrement automatique (type **Position** uniquement). | KoboCollect uniquement (inclus dans l'apparence par défaut des formulaires web) |
| <code>placement-map</code> | Permet la sélection manuelle d'une localisation sur une carte (type **Position** uniquement). | KoboCollect uniquement (inclus dans l'apparence par défaut des formulaires web) |
| <code>hide-input</code> | Affiche une carte plus grande et masque les autres champs de saisie (latitude, longitude, altitude, précision).<br>![Apparence avancée hide-input](images/gps_questions/hide-input.png) | Formulaires web uniquement |

<p class="note">
<strong>Note :</strong> Si vous utilisez des formulaires web et souhaitez enregistrer automatiquement la localisation GPS sans permettre aux répondants de sélectionner ou de saisir manuellement des coordonnées, envisagez d'utiliser la <a href="https://support.kobotoolbox.org/fr/metadata_xls.html">question de métadonnées</a> <code>background-geopoint</code>.
</p>