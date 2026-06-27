# Sécurité des données chez KoboToolbox
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/f7c0f5afa58cad4b40bd6075209daef21a83ee6b/source/is_my_data_safe.md" class="reference">9 oct. 2025</a>


Nous prenons la protection des données très au sérieux. La sécurité des données consiste à protéger les données de nos utilisateurs contre toute menace potentielle. Cet article résume certaines de nos mesures administratives, physiques, organisationnelles et techniques visant à garantir la sécurité des données sur les serveurs KoboToolbox gérés par Kobo, Inc., l'[organisation à but non lucratif à l'origine de KoboToolbox](https://www.kobotoolbox.org/about-us/).

Nous sommes pleinement conformes au Règlement général sur la protection des données (RGPD) de l'Union européenne. Si vous êtes situé dans l'Union européenne, [vous pouvez signer un accord de traitement des données (DPA) ici](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Confidentialité

**Contrôle de l'accès physique**

-   Des mesures de contrôle de l'accès physique, entre autres, sont mises en œuvre par Amazon Web Services (AWS), qui héberge nos serveurs KoboToolbox. Ces mesures comprennent, par exemple, la vidéosurveillance et la sécurité physique des installations de serveurs et de réseaux, le maintien d'un contrôle d'accès par badge, et la restriction de l'accès au seul personnel autorisé. Pour une liste complète des mesures techniques et organisationnelles d'AWS en matière de contrôle de l'accès physique, [consultez cet article](https://aws.amazon.com/compliance/data-center/controls/) sur les contrôles des centres de données fourni par AWS.

**Contrôle de l'accès électronique**

-   Tous les comptes KoboToolbox sont protégés par un mot de passe. Les utilisateurs reçoivent un retour visuel sur la complexité de leur mot de passe, ce qui les encourage à choisir un mot de passe plus robuste le cas échéant. Seuls des hachages de mots de passe chiffrés sont stockés sur le serveur KoboToolbox, en utilisant le framework open source par défaut fourni par Django, qui utilise l'algorithme [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) avec un hachage SHA256. Les mots de passe en texte clair ne sont jamais enregistrés sur le serveur.
-   Tout le contenu des bases de données est chiffré au repos (chiffrement au niveau du disque).
-   Les données envoyées au serveur sont chiffrées en transit à l'aide de SHA-256 avec chiffrement RSA.
-   Les utilisateurs peuvent [choisir d'activer également le chiffrement des données de leur projet (chiffrement au niveau des données)](encrypting_forms.md), ce qui les rend inaccessibles à toutes les étapes du traitement des données et nécessite une clé privée pour les déchiffrer localement.

**Contrôle de l'accès interne**

-   Seuls les administrateurs système autorisés peuvent accéder au serveur KoboToolbox. Ils ne peuvent le faire qu'à la seule fin de mettre à jour les logiciels installés ou de maintenir l'infrastructure du serveur.
-   Les administrateurs système doivent s'authentifier de manière supplémentaire, notamment par authentification par clé publique SSH, pour accéder au serveur KoboToolbox, et par authentification à deux facteurs pour accéder aux panneaux de contrôle fournis par AWS.
-   AWS fournit un journal des actions effectuées dans la console AWS. Pour les connexions SSH aux instances individuelles du serveur KoboToolbox, Kobo collecte des « événements d'accès système » par clé SSH, qui peuvent ensuite être associés aux utilisateurs autorisés.
-   SSH est en outre protégé contre les tentatives de force brute et les accès non autorisés en limitant les connexions au niveau du pare-feu à une courte liste d'adresses IP explicitement autorisées.

**Protection des données dès la conception et par défaut**

-   Seules des informations limitées sont requises pour créer un compte KoboToolbox.
-   Le personnel de Kobo est tenu de respecter les règles énoncées dans les politiques de confidentialité de Kobo.
-   Les données traitées pour le compte de l'utilisateur ne sont pas consultées par Kobo.
-   Les utilisateurs ont la possibilité d'appliquer un chiffrement avancé. Cela garantit que les données sont chiffrées à l'aide d'une clé publique avant d'être soumises à un serveur KoboToolbox, et qu'elles ne peuvent être déchiffrées qu'avec une clé privée sur un ordinateur local. KoboToolbox offre également la possibilité de supprimer des informations en masse une fois qu'elles ont été collectées, facilitant ainsi la pseudonymisation des données personnelles (par la suppression des identifiants).
-   Consultez la sous-section « Contrôle de l'accès électronique » ci-dessus pour plus de détails sur le retour visuel concernant la complexité des mots de passe.

## Intégrité

**Contrôle du transfert de données**

-   Toutes les données en transit sont protégées à l'aide de SHA-256 avec chiffrement RSA.

**Contrôle de la saisie des données**

-   Les utilisateurs contrôlent qui a la permission de saisir des données en fonction de leurs droits d'accès KoboToolbox. Les journaux d'accès HTTP stockés sur le serveur incluent l'utilisateur authentifié pour la plupart des requêtes.

## Disponibilité et résilience

-   Kobo effectue des sauvegardes quotidiennes de toutes les bases de données vers un emplacement distant distinct. En cas de panne critique, toutes les données des utilisateurs seront restaurées à partir de la sauvegarde la plus récente dans les meilleurs délais.
-   Les pare-feux bloquent toutes les requêtes externes, à l'exception des connexions SSH provenant d'une courte liste d'adresses IP explicitement autorisées. Le trafic HTTP et HTTPS public ne peut pas se connecter directement au serveur KoboToolbox ; il est acheminé par l'équilibreur de charge AWS, qui le transfère ensuite aux serveurs frontaux de Kobo.
-   Les serveurs KoboToolbox sont configurés pour utiliser plusieurs instances de serveur fonctionnant simultanément et sont paramétrés pour augmenter le nombre de ces instances afin d'éviter l'impact de toute défaillance localisée. En cas d'autres défaillances menaçant le fonctionnement continu des aspects critiques du logiciel KoboToolbox, les administrateurs système sont disponibles pour intervenir dans de brefs délais afin de rétablir le service.
-   Les procédures de reporting de Kobo comprennent des alertes automatisées, l'escalade des problèmes signalés par les utilisateurs et les problèmes constatés par le personnel.
-   Les plans de continuité prévoient la disponibilité de plusieurs personnes situées dans plusieurs zones géographiques, capables de répondre aux urgences et de rétablir le service.
-   Les serveurs KoboToolbox ont démontré leur capacité à continuer de fonctionner en mode dégradé, en recevant des soumissions tout en récupérant simultanément les projets et soumissions perdus grâce à la récupération à un instant précis (PITR).
-   Les utilisateurs dont il est établi qu'ils abusent de leur compte en surchargeant le serveur KoboToolbox peuvent être suspendus ou voir leur compte restreint.