# Aperçu des outils de collecte de données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/53c2e7dae53b8450c51194fb49c7d915fe735012/source/data-collection-tools.md" class="reference">11 Sep 2025</a>

KoboToolbox permet la collecte de données de plusieurs façons. Parce que KoboToolbox est
construit sur les [standards Xform/ODK](https://xlsform.org), nos formulaires sont
compatibles avec
[un certain nombre d'outils différents](https://xlsform.org/en/#tools-that-support-xlsforms)
qui peuvent être utilisés pour la collecte de données.

Pour les appareils Android, nous recommandons d'utiliser
l'application [Collect Android](https://play.google.com/store/apps/details?id=org.koboc.collect.android&hl=en_US),
qui peut être téléchargée depuis le Google Play Store et installée sur n'importe quel
téléphone ou tablette Android standard.

Pour tous les autres appareils (y compris iPhone, iPad, ou tout ordinateur portable ou ordinateur), nous
recommandons d'utiliser le formulaire web [pour collecter des données](data_through_webforms.md).

## Un aperçu rapide des différences entre les deux options

| &nbsp;                                                                         | Formulaires web                                    | KoboCollect                                            |
| :----------------------------------------------------------------------------- | :------------------------------------------------- | :----------------------------------------------------- |
| Appareils                                                                      | Tout appareil mobile ou ordinateur                 | Android uniquement                                     |
| Fonctionne dans...                                                             | Navigateur                                         | Application Android native                             |
| Configurable                                                                   | À l'échelle du serveur                             | Sur chaque appareil                                    |
| Affichage par défaut du formulaire                                             | Toutes les questions sur le même écran             | Une question par écran                                 |
| Téléversement des données                                                      | Automatiquement lorsque la connexion est disponible| Sur demande de l'utilisatrice ou utilisateur ou immédiatement si connexion disponible |
| Méta-questions spécifiques au téléphone (`subscriberid`, `simserial`, `phonenumber`) | Non                                          | Oui                                                    |
| Type de question `barcode`                                                     | Non (sauf saisie manuelle)                         | Oui                                                    |
| Différents styles de formulaire                                                | Oui                                                | Non                                                    |
| Chiffrement                                                                    | Pas pour le stockage, mais toujours pendant le transfert | Peut être activé sur l'appareil, toujours pendant le transfert |
| Apparence `hide-input` pour les cartes afin de masquer les entrées GPS manuelles | Oui                                             | Non                                                    |
| Options d'apparence de carte avancées (`streets`, `terrain`, `satellite`, `[other]`) | Oui                                         | Non                                                    |
| Formatage du texte dans les notes et étiquettes (gras, italique, liens)       | Oui                                                | Non                                                    |
| Combiner les notes consécutives en une seule note à l'écran                    | Oui                                                | Non                                                    |
| Apparence `multiline` pour les questions `text`                                | Oui                                                | Oui                                                    |
| Apparence `horizontal-compact` pour les questions de type sélection            | Oui                                                | Non                                                    |
| Apparence d'échelle `likert` pour les questions de type sélection              | Oui                                                | Oui                                                    |
| Apparence `compact-2` pour les questions de type sélection                     | Non                                                | Oui                                                    |
| Apparence `no-calendar`                                                        | Non                                                | Oui                                                    |
| Apparences d'image avancées (`annotate`, `draw`, `signature`)                  | Oui                                                | Oui                                                    |
| Commande de calcul `repeat_count()`                                            | Définir un nombre minimum de groupes répétés       | Définir un nombre exact de groupes répétés             |

### Collecter des données en utilisant KoboCollect

Après avoir déployé un projet, vous pouvez aller dans **Formulaire - Collecter des données**, puis
sélectionner l'application Android.

![image](/images/data_collection_tool/KoboCollect.gif)

Pour plus de détails sur la configuration de KoboCollect sur n'importe quel appareil Android,
[lisez cet article](kobocollect_on_android_latest.md).

### Collecter des données en utilisant le formulaire web Enketo

Pour [utiliser le formulaire web](data_through_webforms.md), après avoir déployé un projet, vous
pouvez aller dans **Formulaire - Collecter des données**, plusieurs options (en ligne ou hors ligne, soumission
unique ou multiple) sont disponibles. L'option par défaut est **En ligne-Hors ligne
(soumissions multiples)**.

![image](/images/data_collection_tool/Webform.gif)