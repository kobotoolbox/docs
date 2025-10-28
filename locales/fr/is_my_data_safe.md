# Mesures de sécurité des données KoboToolbox : Protéger vos données
<a href="../is_my_data_safe.html">Read in English</a> | <a href="../es/is_my_data_safe.html">Leer en español</a> | <a href="../ar/is_my_data_safe.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/f7c0f5afa58cad4b40bd6075209daef21a83ee6b/source/is_my_data_safe.md" class="reference">9 oct. 2025</a>

Nous prenons la protection des données très au sérieux. La sécurité des données signifie protéger les données de nos utilisatrices et utilisateurs contre toute menace potentielle. Cet article résume certaines de nos mesures administratives, physiques, organisationnelles et techniques pour garantir la sécurité des données sur les serveurs KoboToolbox maintenus par Kobo, Inc., l'[organisation à but non lucratif derrière KoboToolbox](https://www.kobotoolbox.org/about-us/).

Nous sommes entièrement conformes au Règlement général sur la protection des données (RGPD) de l'Union européenne. Si vous êtes situé dans l'Union européenne, [vous pouvez signer un accord de traitement des données (DPA) ici](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Confidentialité

**Contrôle d'accès physique**

-   Des mesures de contrôle d'accès physique sont notamment mises en œuvre par Amazon Web Services (AWS), qui est utilisé pour héberger nos serveurs KoboToolbox. Ces mesures comprennent, par exemple, la vidéosurveillance et la sécurité physique des installations de serveurs et de réseaux, le maintien d'un contrôle d'accès par carte à puce, la limitation de l'accès au seul personnel autorisé. Pour une liste complète des détails sur les mesures techniques et organisationnelles d'AWS pour le contrôle d'accès physique, [consultez cet article](https://aws.amazon.com/compliance/data-center/controls/) sur les contrôles des centres de données fournis par AWS.

**Contrôle d'accès électronique**

-   Tous les comptes KoboToolbox sont protégés par mot de passe. Les utilisatrices et utilisateurs reçoivent un retour visuel sur la complexité de leur mot de passe, ce qui les encourage à sélectionner un mot de passe plus fort le cas échéant. Seuls les hachages de mots de passe chiffrés sont stockés sur le serveur KoboToolbox, en utilisant le framework open-source par défaut fourni par Django, qui utilise l'algorithme [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) avec un hachage SHA256. Les mots de passe en texte clair ne sont jamais enregistrés sur le serveur.
-   Tout le contenu de la base de données est chiffré au repos (chiffrement au niveau du disque).
-   Les données envoyées au serveur sont chiffrées en transit en utilisant SHA-256 avec chiffrement RSA.
-   Les utilisatrices et utilisateurs peuvent [choisir d'activer également le chiffrement de leurs données de projet (chiffrement au niveau des données)](encrypting_forms.md), ce qui les rend inaccessibles à toutes les étapes du traitement des données et nécessite une clé privée pour les déchiffrer localement.

**Contrôle d'accès interne**

-   Seuls les administrateurs système autorisés peuvent accéder au serveur KoboToolbox. Ils ne peuvent le faire que dans le but exprès de mettre à jour les logiciels installés ou de maintenir l'infrastructure du serveur.
-   Les administrateurs système nécessitent une authentification supplémentaire, y compris l'authentification par clé publique SSH, pour accéder au serveur KoboToolbox et une authentification à deux facteurs pour accéder aux panneaux de contrôle fournis par AWS.
-   AWS fournit un journal des actions effectuées dans la console AWS. Pour les connexions SSH aux instances individuelles du serveur KoboToolbox, Kobo collecte les « événements d'accès système » par clé SSH, qui peuvent ensuite être associés aux utilisatrices et utilisateurs autorisés.
-   SSH est davantage protégé contre les tentatives de force brute et les accès non autorisés en limitant les connexions au niveau du pare-feu à une petite liste d'adresses IP explicitement autorisées.

**Protection des données dès la conception et par défaut**

-   Seules des informations limitées sont requises pour créer un compte utilisateur KoboToolbox.
-   Le personnel de Kobo est tenu de respecter les règles énoncées dans les politiques de confidentialité de Kobo.
-   Les données traitées au nom de l'utilisatrice ou de l'utilisateur ne sont pas consultées par Kobo.
-   Les utilisatrices et utilisateurs ont la possibilité d'appliquer un chiffrement avancé. Cela garantit que les données sont chiffrées à l'aide d'une clé publique avant d'être soumises à un serveur KoboToolbox, et qu'elles ne peuvent être déchiffrées qu'avec une clé privée sur un ordinateur local. KoboToolbox offre également la possibilité de supprimer des informations en masse une fois qu'elles ont été collectées, facilitant ainsi la pseudonymisation des données personnelles (par la suppression des identifiants).
-   Voir la sous-section ci-dessus « Contrôle d'accès électronique » pour plus de détails sur le retour visuel concernant la complexité du mot de passe.

## Intégrité

**Contrôle du transfert de données**

-   Toutes les données en transit sont protégées en utilisant SHA-256 avec chiffrement RSA.

**Contrôle de la saisie de données**

-   Les utilisatrices et utilisateurs contrôlent qui a la permission de saisir des données en fonction de leurs autorisations KoboToolbox. Les journaux d'accès HTTP stockés sur le serveur incluent l'utilisatrice ou l'utilisateur authentifié pour la plupart des requêtes.

## Disponibilité et résilience

-   Kobo effectue des sauvegardes quotidiennes de toutes les bases de données vers un emplacement distant distinct. En cas de panne critique, toutes les données des utilisatrices et utilisateurs seront restaurées à partir de la sauvegarde la plus récente aussi rapidement que possible.
-   Les pare-feu bloquent toutes les requêtes externes à l'exception des connexions SSH provenant d'une petite liste d'adresses IP explicitement autorisées. Le trafic HTTP et HTTPS public ne peut pas se connecter directement au serveur KoboToolbox, il est plutôt desservi par l'équilibreur de charge AWS, qui le transmet ensuite aux serveurs frontaux de Kobo.
-   Les serveurs KoboToolbox sont configurés pour utiliser plusieurs instances de serveur fonctionnant simultanément et sont paramétrés pour augmenter le nombre de ces instances afin d'éviter l'impact de toute défaillance localisée. En cas d'autres défaillances menaçant le fonctionnement continu des aspects critiques du logiciel KoboToolbox, les administrateurs système sont prêts à intervenir dans un court délai pour rétablir le service.
-   Les procédures de signalement de Kobo incluent des alertes automatisées, l'escalade des problèmes signalés par les utilisatrices et utilisateurs, et les problèmes auto-détectés par le personnel.
-   Les plans d'urgence incluent la disponibilité de plusieurs personnes dans plusieurs emplacements géographiques qui peuvent répondre aux urgences et rétablir le service.
-   Les serveurs KoboToolbox ont la capacité démontrée de continuer à fonctionner dans un état dégradé, en recevant des soumissions tout en récupérant simultanément les projets/soumissions perdus via une récupération ponctuelle à la minute près (PITR).
-   Les utilisatrices et utilisateurs qui abusent de l'utilisation de leurs comptes en surchargeant le serveur KoboToolbox peuvent être suspendus ou leur compte peut être restreint.