# Partager des projets avec des paramètres au niveau du projet
<a href="../project_sharing_settings.html">Read in English</a> | <a href="../es/project_sharing_settings.html">Leer en español</a> | <a href="../ar/project_sharing_settings.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/03c0981e6da0be6aec3385dfe68b2ebb0f71b2f8/source/project_sharing_settings.md" class="reference">5 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/vRuAan0aSfY?si=FbKeyjF9XitYdUWC" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox vous permet de personnaliser les paramètres de partage en fonction des besoins du projet. Cet article explique les **contrôles de confidentialité et de partage au niveau du projet** de KoboToolbox, notamment la possibilité d'autoriser les soumissions sans authentification, de rendre un projet public, de transférer la propriété et de supprimer des projets partagés.

<p class="note">
  Pour en savoir plus sur la gestion de ce que des <strong>utilisatrices et utilisateurs spécifiques</strong> peuvent faire dans un projet, consultez <a href="managing_permissions.html">Partager votre projet avec des autorisations spécifiques aux utilisatrices et utilisateurs</a>.
</p>

## Autoriser les soumissions sans authentification

Par défaut, KoboToolbox nécessite un nom d'utilisateur et un mot de passe pour soumettre des données, gérer des projets et accéder aux soumissions. Lorsqu'un nouveau projet est déployé, l'authentification est requise pour accéder au formulaire et envoyer des soumissions. Seules les utilisatrices et utilisateurs avec qui vous avez [partagé le formulaire](managing_permissions.md) et auxquels vous avez accordé l'autorisation **Ajouter des soumissions** pourront accéder au formulaire et soumettre des données.

Dans certains cas, vous pouvez souhaiter activer la saisie de données pour toute personne disposant de l'URL. Cela permet aux personnes disposant de l'URL du formulaire d'envoyer des soumissions sans se connecter à un compte KoboToolbox.

Pour autoriser la saisie de données pour toute personne disposant de l'URL du formulaire :
1. Ouvrez le projet dans KoboToolbox et accédez à la section **FORMULAIRE**
2. Sous **Collecter des données**, activez « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe ».

![Exemple d'authentification requise](images/project_sharing_settings/require_authentication.png)

Vous pouvez également modifier ce paramètre en accédant à l'onglet **Partage** dans la page **PARAMÈTRES** de votre projet et en basculant le paramètre par défaut pour activer « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe ».

<p class="note">
  <strong>Remarque :</strong> La configuration des formulaires pour exiger une authentification est désormais disponible en tant que paramètre par projet. Cette fonctionnalité de confidentialité remplace le paramètre précédent au niveau du compte « Exiger une authentification pour voir les formulaires et soumettre des données ». Avec cette mise à jour, les nouveaux projets nécessitent une authentification par défaut. Les projets existants héritent de vos paramètres précédents au niveau du compte tels qu'ils étaient au moment de cette mise à jour.
</p>

## Rendre votre projet public

En plus de partager votre projet avec des utilisatrices et utilisateurs KoboToolbox spécifiques, vous pouvez également rendre votre formulaire et/ou les données de votre projet publics. Pour ce faire :

1. Accédez à la page **PARAMÈTRES** de votre projet de collecte de données
2. Ouvrez l'onglet **Partage**
3. Sélectionnez les options « Tout le monde peut voir ce formulaire » et/ou « Tout le monde peut voir les soumissions faites à ce formulaire »

<p class="note">
  <strong>Remarque :</strong> Lorsque vous sélectionnez « Tout le monde peut voir les soumissions faites à ce formulaire », l'option « Tout le monde peut voir ce formulaire » est également sélectionnée par défaut.
</p>

Une URL sera affichée que vous pouvez partager pour fournir un accès au formulaire et/ou aux données du projet sans nécessiter de connexion à un compte KoboToolbox. Les utilisatrices et utilisateurs disposant du lien pourront effectuer les actions suivantes :

| **Option**    | **Actions autorisées**                                |
| :----------------- | :--------------------------------------------- |
| Tout le monde peut voir ce formulaire              | <ul><li>Accéder à la page **FORMULAIRE**</li> <li>Prévisualiser le formulaire</li> <li>Télécharger le formulaire au format XLS ou XML</li></ul> |
| Tout le monde peut voir les soumissions faites à ce formulaire      | <ul><li>Accéder à la page **DONNÉES**</li><li>Voir les données dans le mode **Tableau**</li><li>Voir et imprimer les **Rapports**</li><li>Voir la **Galerie Photo**</li><li>**Télécharger** les données du projet</li><li>Voir les données dans le mode **Carte**</li></ul> |

## Transférer la propriété d'un projet

Vous pouvez transférer la propriété d'un projet de votre compte vers un autre compte utilisateur. Les deux comptes doivent être sur le même serveur KoboToolbox.

Pour transférer un projet :
1. Accédez à la page **PARAMÈTRES** de votre projet de collecte de données.
2. Ouvrez l'onglet **Partage**.
3. Dans la section **Transférer la propriété du projet**, cliquez sur **Transférer**.
4. Saisissez le nom d'utilisateur du compte vers lequel vous souhaitez transférer le projet.
5. Cliquez sur **Transférer le projet**.
   
Un e-mail sera envoyé à l'utilisatrice ou l'utilisateur recevant le projet. Pour accepter le transfert, le destinataire doit cliquer sur le lien dans l'e-mail tout en étant connecté à son compte KoboToolbox. Lorsqu'il clique sur le lien, une boîte de dialogue de confirmation s'affiche. Le destinataire doit cliquer sur **Accepter** pour que le transfert du projet soit terminé.

<p class="note">
  <strong>Remarque :</strong> Après avoir accepté le transfert, quelques minutes peuvent être nécessaires pour le terminer. Le nouveau propriétaire du projet peut voir le projet dans sa liste de projets immédiatement, mais la vue du tableau de données peut prendre plus de temps à se mettre à jour.
</p>

## Supprimer des projets partagés de votre compte

Pour supprimer un projet qu'une autre utilisatrice ou un autre utilisateur a partagé avec vous :

1. Ouvrez le projet et accédez à la page **FORMULAIRE**.
2. Cliquez sur <i class="k-icon-more"></i> **Plus d'actions** dans le coin supérieur droit.
3. Sélectionnez **Supprimer le projet partagé**.
4. Confirmez en cliquant sur **SUPPRIMER**.

<iframe src="https://www.youtube.com/embed/EZyj0tQXtzA?si=EmE0bahqxFAW2Fqm" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>