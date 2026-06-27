# Droits d'accès au niveau de l’utilisateur
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/managing_permissions.md" class="reference">23 avril 2026</a>

<iframe src="https://www.youtube.com/embed/WnCNuxgaMoQ?si=bktZdlug2uBKUyzq&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox vous permet de définir différents niveaux d'accès pour les utilisateurs sur chaque projet. Certains utilisateurs peuvent avoir besoin uniquement de soumettre ou de consulter des données, tandis que d'autres nécessitent un accès plus avancé, comme modifier des formulaires, valider des soumissions ou modifier des données.

Cet article explique comment accorder des autorisations à d'autres utilisateurs KoboToolbox pour collaborer sur vos projets. Il couvre les autorisations au niveau de l'utilisateur, les autorisations au niveau des lignes et la copie d'autorisations depuis un autre projet.

<p class="note">
Pour en savoir plus sur le partage de votre projet avec d'autres personnes pour la collecte de données, consultez <a href="../fr/data_through_webforms.html">Collecte de données via des formulaires web</a>. Pour en savoir plus sur les paramètres au niveau du projet pour le partage de vos projets, consultez <a href="../fr/project_sharing_settings.html">Partager des projets avec des paramètres au niveau du projet</a>.
</p>

## Définir des autorisations au niveau de l'utilisateur

Les autorisations au niveau de l'utilisateur vous permettent de partager les données du projet avec d'autres utilisateurs KoboToolbox et de contrôler leur accès à votre formulaire ou à vos soumissions.

Pour configurer des autorisations au niveau de l'utilisateur :
1. Accédez à la page **PARAMÈTRES** de votre projet de collecte de données, puis cliquez sur **Partage**.
2. Sous la liste des utilisateurs ayant actuellement accès, cliquez sur **Ajouter un utilisateur**.
3. Saisissez le nom d'utilisateur de l'utilisateur avec lequel vous souhaitez partager le formulaire.
4. Sélectionnez le niveau d'autorisation souhaité.
5. Cliquez sur **ACCORDER DES AUTORISATIONS**.

![Ajouter un utilisateur](images/managing_permissions/add_user.png)

Les autorisations suivantes sont disponibles :
| **Autorisation**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Afficher le formulaire               | L'utilisateur peut prévisualiser le formulaire.                                  |
| Modifier le formulaire      | L'utilisateur peut modifier le formulaire.                                  |
| Afficher les soumissions           | L'utilisateur peut consulter les données soumises.           |
| Ajouter des soumissions           | L'utilisateur peut soumettre des données à l'aide du formulaire.         |
| Modifier les soumissions         | L'utilisateur peut modifier les données soumises.           |
| Valider les soumissions | L'utilisateur peut [approuver ou rejeter](../fr/viewing_validating_data.html#valider-vos-donnees) les données soumises. |
| Supprimer les soumissions         | L'utilisateur peut supprimer les données soumises.        |
| Gérer le projet      | L'utilisateur peut effectuer toutes les actions ci-dessus et gérer les paramètres du projet.                  |

<p class="note">
<strong>Remarque</strong> : Lorsque certaines autorisations sont accordées, d'autres autorisations sont également accordées automatiquement. Par exemple, si un utilisateur se voit accorder l'autorisation <strong>Ajouter des soumissions</strong>, il se verra également accorder automatiquement l'autorisation <strong>Afficher le formulaire</strong>.
</p>

## Définir des autorisations au niveau des lignes

Les autorisations au niveau des lignes vous permettent de définir des autorisations de consultation, de modification, de validation et de suppression pour les soumissions en fonction de conditions prédéfinies. Ces autorisations peuvent être :

- **Uniquement d'utilisateurs spécifiques** : Les autorisations basées sur l'utilisateur vous permettent de partager les données du projet avec un autre utilisateur KoboToolbox uniquement lorsqu'elles sont soumises par des utilisateurs spécifiques. Cela peut être utile pour permettre aux collecteurs de données de consulter et de modifier leurs propres soumissions sans accéder aux données d'autres collecteurs.
- **En fonction d'une condition** : Les autorisations basées sur une condition accordent l'accès aux données du projet en fonction d'une réponse à une question de votre formulaire. Par exemple, cela peut être utilisé pour partager des données collectées avant une certaine date ou pour une région spécifique.

### Autorisations basées sur l'utilisateur

Pour ajouter des autorisations basées sur l'utilisateur :

1. Ouvrez votre projet et accédez à l'onglet **PARAMÈTRES**.
2. Accédez à la section **Partage**.
3. Cliquez sur **Ajouter un utilisateur** et saisissez le nom d'utilisateur de l'utilisateur avec lequel vous souhaitez partager le projet.
4. Sélectionnez les autorisations basées sur l'utilisateur que vous souhaitez autoriser (**Afficher**, **Modifier**, **Supprimer** et/ou **Valider**).
5. Sous chaque autorisation, saisissez le(s) nom(s) d'utilisateur des utilisateurs dont vous accordez l'accès aux soumissions. Les noms d'utilisateur doivent être séparés par des virgules.
6. Cliquez sur **Accorder des autorisations** pour enregistrer vos paramètres d'autorisations.

Une fois que vous avez enregistré vos autorisations, l'utilisateur avec lequel vous avez partagé le projet pourra consulter, modifier, valider ou supprimer les données du projet soumises par les noms d'utilisateur spécifiés, en fonction des autorisations sélectionnées.

### Autorisations basées sur une condition

Pour ajouter des autorisations basées sur une condition :

1. Ouvrez votre projet et accédez à l'onglet **PARAMÈTRES**.
2. Accédez à la section **Partage**.
3. Cliquez sur **Ajouter un utilisateur** et saisissez le nom d'utilisateur de l'utilisateur avec lequel vous souhaitez partager le projet.
4. Sélectionnez les autorisations basées sur une condition que vous souhaitez autoriser (**Afficher**, **Modifier**, **Supprimer** et/ou **Valider**).
5. Ouvrez le menu déroulant **Sélectionner…** pour afficher la liste complète des questions du formulaire et sélectionnez la question qui doit être utilisée pour filtrer les soumissions partagées avec l'utilisateur.
6. Sur le côté droit du signe égal (=), saisissez la valeur de réponse qui doit être respectée.
7. Cliquez sur **Accorder des autorisations** pour enregistrer vos paramètres d'autorisations.

Une fois que vous avez enregistré vos autorisations, l'utilisateur pourra consulter, modifier, valider ou supprimer les soumissions de données du projet qui répondent à la condition spécifiée, en fonction des autorisations sélectionnées.

Les valeurs de réponse doivent suivre un format spécifique pour que la condition fonctionne :

| **Type de question**    | **Format**                                |
| :----------------- | :--------------------------------------------- |
| Date               | <code>AAAA-MM-JJ</code> (par exemple, <code>1974-12-31</code>)                                  |
| Choix unique et Choix multiple      | Valeur XML/nom du choix (par exemple, <code>first_grade</code> plutôt que <code>First grade</code>)                                   |
| Chiffre et Décimale           | Un nombre entier ou décimal spécifique            |

## Copier des autorisations depuis un autre projet

Pour copier les autorisations d'équipe depuis un autre projet :

1. Ouvrez l'onglet **Partage** dans la page **PARAMÈTRES** de votre projet.
2. Cliquez sur « Copier une équipe à partir d'un autre projet ».
3. Sélectionnez le projet à partir duquel vous souhaitez copier les autorisations.

<p class="note">
<strong>Remarque</strong> : Cela remplacera tous les paramètres de partage existants sur le projet auquel vous ajoutez les autorisations.
</p>

## Résolution de problèmes

<details>
<summary><strong>Suivi des modifications apportées par d'autres utilisateurs</strong></summary>
KoboToolbox conserve des <a href="../fr/activity_logs.html">journaux d'activité</a> qui affichent une chronologie complète des actions du compte et du projet. Les <strong>journaux d'historique du projet</strong> enregistrent chaque modification à l'intérieur d'un projet — importations, modifications, suppressions et soumissions — afin que vous puissiez retracer les changements, attribuer la responsabilité et identifier le moment où les problèmes ont commencé.
</details>
<br>
<details>
<summary><strong>Demande de nom d'utilisateur et de mot de passe lors de l'envoi de données</strong></summary>
Si une fenêtre de connexion apparaît lorsque vous essayez de soumettre, le projet est configuré pour <a href="../fr/project_sharing_settings.html">exiger une authentification</a> pour la collecte de données. Dans ce cas, vous ne pouvez soumettre des données que si votre compte dispose de l'autorisation Ajouter des soumissions. Saisissez votre nom d'utilisateur et votre mot de passe KoboToolbox pour continuer.
</details>
<br>
<details>
<summary><strong>Les autorisations basées sur l'utilisateur ne semblent pas fonctionner</strong></summary>
Les autorisations basées sur l'utilisateur s'appliquent uniquement lorsque <a href="../fr/project_sharing_settings.html">l'authentification est requise</a> et que chaque soumission porte un nom d'utilisateur. Ouvrez l'onglet <strong>FORMULAIRE</strong> du projet et désactivez « Autoriser les soumissions à ce formulaire sans nom d'utilisateur ni mot de passe » sous <strong>Collecter des données</strong>.
</details>
<br>
<details>
<summary><strong>Les anciens enregistrements ignorent les règles au niveau des lignes</strong></summary>
Les soumissions effectuées avant que <a href="../fr/project_sharing_settings.html">l'authentification ne soit requise</a> peuvent ne pas avoir de nom d'utilisateur associé, de sorte que les règles basées sur l'utilisateur ne peuvent pas les filtrer.
</details>
<br>
<details>
<summary><strong>Les autorisations basées sur une condition ne correspondent pas au texte partiel</strong></summary>
Le filtre doit inclure la valeur de réponse exacte. Par exemple, filtrer sur <code>developer</code> ne correspondra pas à <code>software_developer</code>. Écrivez la valeur complète que vous attendez, ou ajustez votre formulaire afin que la valeur exacte soit capturée.
</details>
<br>
<details>
<summary><strong>Les autorisations basées sur une condition échouent sur les questions de groupe répété</strong></summary>
Les filtres ne peuvent pas regarder à l'intérieur d'un groupe répété car une soumission peut contenir plusieurs réponses différentes. Si vous en avez besoin, consultez le message du forum communautaire <a href="https://community.kobotoolbox.org/t/condition-based-permissions-from-a-repeat-group-value/59449">Autorisations basées sur une condition utilisant une valeur de groupe répété</a> pour une solution de contournement avec un tableur.
</details>
<br>
<details>
<summary><strong>Conditions multiples non prises en charge</strong></summary>
Les autorisations basées sur une condition n'acceptent qu'une seule condition. Si vous devez définir des autorisations en fonction de plusieurs conditions, envisagez de créer un calcul basé sur une condition dans votre formulaire qui génère une valeur unique pour le filtrage.
</details>