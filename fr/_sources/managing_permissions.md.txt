# Partager des projets avec des permissions au niveau utilisateur
<a href="../managing_permissions.html">Read in English</a> | <a href="../es/managing_permissions.html">Leer en español</a> | <a href="../ar/managing_permissions.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/2d936225c821d33163324c6fe6093fa30da3c5fa/source/managing_permissions.md" class="reference">29 août 2025</a>

<iframe src="https://www.youtube.com/embed/WnCNuxgaMoQ?si=bktZdlug2uBKUyzq" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox vous permet de définir différents niveaux d'accès pour les utilisatrices et utilisateurs sur chaque projet. Certaines utilisatrices et certains utilisateurs peuvent avoir besoin uniquement de soumettre ou de consulter des données, tandis que d'autres nécessitent un accès plus avancé, comme la modification de formulaires, la validation de soumissions ou la modification de données.

Cet article explique comment accorder des permissions à d'autres utilisatrices et utilisateurs de KoboToolbox pour collaborer sur vos projets. Il couvre les permissions au niveau utilisateur, les permissions au niveau des lignes et la copie de permissions depuis un autre projet.

<p class="note">
Pour en savoir plus sur le partage de votre projet avec d'autres personnes pour la collecte de données, consultez <a href="data_through_webforms.html">Collecter des données via des formulaires Web</a>. Pour en savoir plus sur les paramètres au niveau du projet pour partager vos projets, consultez <a href="project_sharing_settings.html">Partager des projets avec des paramètres au niveau du projet</a>.
</p>

## Définir des permissions au niveau utilisateur

Les permissions au niveau utilisateur vous permettent de partager les données d'un projet avec d'autres utilisatrices et utilisateurs de KoboToolbox et de contrôler leur accès à votre formulaire ou à vos soumissions.

Pour configurer des permissions au niveau utilisateur :
1. Accédez à la page **PARAMÈTRES** de votre projet de collecte de données et cliquez sur **Partage**.
2. Sous la liste des utilisatrices et utilisateurs ayant un accès actuel, cliquez sur **Ajouter un utilisateur**.
3. Saisissez le nom d'utilisateur de la personne avec laquelle vous souhaitez partager le formulaire.
4. Sélectionnez le niveau de permission souhaité.
5. Cliquez sur **ACCORDER DES PERMISSIONS**.

![Ajouter un utilisateur](images/managing_permissions/add_user.png)

Les permissions suivantes sont disponibles :
| **Permission**    | **Description**                                |
| :----------------- | :--------------------------------------------- |
| Voir le formulaire               | L'utilisatrice ou l'utilisateur peut prévisualiser le formulaire.                                  |
| Modifier le formulaire      | L'utilisatrice ou l'utilisateur peut modifier le formulaire.                                  |
| Voir les soumissions           | L'utilisatrice ou l'utilisateur peut consulter les données soumises.           |
| Ajouter des soumissions           | L'utilisatrice ou l'utilisateur peut soumettre des données en utilisant le formulaire.         |
| Modifier les soumissions         | L'utilisatrice ou l'utilisateur peut modifier les données soumises.           |
| Valider les soumissions | L'utilisatrice ou l'utilisateur peut [approuver ou rejeter](record_validation.md) les données soumises. |
| Supprimer les soumissions         | L'utilisatrice ou l'utilisateur peut supprimer les données soumises.        |
| Gérer le projet      | L'utilisatrice ou l'utilisateur peut effectuer toutes les actions ci-dessus et gérer les paramètres du projet.                  |

<p class="note">
<strong>Remarque</strong> : Lorsque certaines permissions sont accordées, d'autres permissions sont également accordées automatiquement. Par exemple, si une utilisatrice ou un utilisateur se voit accorder la permission <strong>Ajouter des soumissions</strong>, la permission <strong>Voir le formulaire</strong> lui sera également accordée automatiquement.
</p>

## Définir des permissions au niveau des lignes

Les permissions au niveau des lignes vous permettent de définir des permissions de consultation, de modification, de validation et de suppression pour les soumissions en fonction de conditions prédéfinies. Ces permissions peuvent être :

- **Uniquement d'utilisatrices et utilisateurs spécifiques** : Les permissions basées sur l'utilisateur vous permettent de partager les données d'un projet avec une autre utilisatrice ou un autre utilisateur de KoboToolbox uniquement lorsqu'elles sont soumises par des utilisatrices et utilisateurs spécifiques. Cela peut être utile pour permettre aux collectrices et collecteurs de données de consulter et de modifier leurs propres soumissions sans accéder aux données d'autres collectrices et collecteurs.
- **Basées sur une condition** : Les permissions basées sur une condition accordent l'accès aux données du projet en fonction d'une réponse à une question de votre formulaire. Par exemple, cela peut être utilisé pour partager des données collectées avant une certaine date ou pour une région spécifique.

### Permissions basées sur l'utilisateur

Pour ajouter des permissions basées sur l'utilisateur :

1. Ouvrez votre projet et accédez à l'onglet **PARAMÈTRES**.
2. Accédez à la section **Partage**.
3. Cliquez sur **Ajouter un utilisateur** et saisissez le nom d'utilisateur de la personne avec laquelle vous souhaitez partager le projet.
4. Sélectionnez les permissions basées sur l'utilisateur que vous souhaitez autoriser (**Voir**, **Modifier**, **Supprimer** et/ou **Valider**).
5. Sous chaque permission, saisissez le ou les noms d'utilisateur des personnes dont vous accordez l'accès aux soumissions. Les noms d'utilisateur doivent être séparés par des virgules.
6. Cliquez sur **Accorder des permissions** pour enregistrer vos paramètres de permissions.

Une fois que vous avez enregistré vos permissions, l'utilisatrice ou l'utilisateur avec qui vous avez partagé le projet pourra consulter, modifier, valider ou supprimer les données du projet soumises par les noms d'utilisateur spécifiés, selon les permissions sélectionnées.

### Permissions basées sur une condition

Pour ajouter des permissions basées sur une condition :

1. Ouvrez votre projet et accédez à l'onglet **PARAMÈTRES**.
2. Accédez à la section **Partage**.
3. Cliquez sur **Ajouter un utilisateur** et saisissez le nom d'utilisateur de la personne avec laquelle vous souhaitez partager le projet.
4. Sélectionnez les permissions basées sur une condition que vous souhaitez autoriser (**Voir**, **Modifier**, **Supprimer** et/ou **Valider**).
5. Ouvrez le menu déroulant **Sélectionner…** pour afficher la liste complète des questions du formulaire et sélectionnez la question qui doit être utilisée pour filtrer les soumissions partagées avec l'utilisatrice ou l'utilisateur.
6. Sur le côté droit du signe égal (=), saisissez la valeur de réponse qui doit être satisfaite.
7. Cliquez sur **Accorder des permissions** pour enregistrer vos paramètres de permissions.
   
Une fois que vous avez enregistré vos permissions, l'utilisatrice ou l'utilisateur pourra consulter, modifier, valider ou supprimer les soumissions de données du projet qui répondent à la condition spécifiée, selon les permissions sélectionnées.

Les valeurs de réponse doivent suivre un format spécifique pour que la condition fonctionne :

| **Type de question**    | **Format**                                |
| :----------------- | :--------------------------------------------- |
| Date               | <code>AAAA-MM-JJ</code> (par ex., <code>1974-12-31</code>)                                  |
| Sélectionner un et Sélectionner plusieurs      | Valeur XML/nom du choix (par ex., <code>first_grade</code> plutôt que <code>First grade</code>)                                   |
| Nombre et Décimal           | Un nombre entier ou décimal spécifique            |

## Copier des permissions depuis un autre projet

Pour copier les permissions d'équipe depuis un autre projet :

1. Ouvrez l'onglet **Partage** dans la page **PARAMÈTRES** de votre projet.
2. Cliquez sur « Copier l'équipe depuis un autre projet ».
3. Sélectionnez le projet depuis lequel vous souhaitez copier les permissions.

<p class="note">
<strong>Remarque</strong> : Cela écrasera tous les paramètres de partage existants sur le projet auquel vous ajoutez les permissions.
</p>

## Dépannage

<details>
<summary><strong>Suivi des modifications effectuées par d'autres utilisatrices et utilisateurs</strong></summary>
KoboToolbox conserve des <a href="activity_logs.html">Journaux d'activité</a> qui affichent une chronologie complète des actions du compte et du projet. Les <strong>Journaux d'historique du projet</strong> enregistrent chaque modification à l'intérieur d'un projet—importations, modifications, suppressions et soumissions—afin que vous puissiez retracer les changements, attribuer la responsabilité et identifier le moment où les problèmes ont commencé.
</details>
<br>
<details>
<summary><strong>Demande de nom d'utilisateur et de mot de passe lors de l'envoi de données</strong></summary>
Si une fenêtre de connexion apparaît lorsque vous essayez de soumettre, le projet est configuré pour <a href="project_sharing_settings.html">exiger une authentification</a> pour la collecte de données. Dans ce cas, vous ne pouvez soumettre des données que si votre compte dispose de la permission Ajouter des soumissions. Saisissez votre nom d'utilisateur et votre mot de passe KoboToolbox pour continuer.
</details>
<br>
<details>
<summary><strong>Les permissions basées sur l'utilisateur ne semblent pas fonctionner</strong></summary>
Les permissions basées sur l'utilisateur s'appliquent uniquement lorsque <a href="project_sharing_settings.html">l'authentification est requise</a> et que chaque soumission porte un nom d'utilisateur. Ouvrez l'onglet <strong>FORMULAIRE</strong> du projet et désactivez « Autoriser les soumissions à ce formulaire sans nom d'utilisateur et mot de passe » sous <strong>Collecter des données</strong>.
</details>
<br>
<details>
<summary><strong>Les anciens enregistrements ignorent les règles au niveau des lignes</strong></summary>
Les soumissions effectuées avant que <a href="project_sharing_settings.html">l'authentification ne soit requise</a> peuvent ne pas avoir de nom d'utilisateur associé, de sorte que les règles basées sur l'utilisateur ne peuvent pas les filtrer.
</details>
<br>
<details>
<summary><strong>Les permissions basées sur une condition ne correspondent pas au texte partiel</strong></summary>
Le filtre doit inclure la valeur de réponse exacte. Par exemple, filtrer sur <code>developer</code> ne correspondra pas à <code>software_developer</code>. Écrivez la valeur complète que vous attendez, ou ajustez votre formulaire pour que la valeur exacte soit capturée.
</details>
<br>
<details>
<summary><strong>Les permissions basées sur une condition échouent sur les questions de groupe répété</strong></summary>
Les filtres ne peuvent pas regarder à l'intérieur d'un groupe répété car une soumission peut contenir plusieurs réponses différentes. Si vous avez besoin de cela, consultez le message du Forum communautaire <a href="https://community.kobotoolbox.org/t/condition-based-permissions-from-a-repeat-group-value/59449">Permissions basées sur une condition utilisant une valeur de groupe répété</a> pour une solution de contournement avec une feuille de calcul.
</details>
<br>
<details>
<summary><strong>Conditions multiples non prises en charge</strong></summary>
Les permissions basées sur une condition n'acceptent qu'une seule condition. Si vous devez définir des permissions basées sur plusieurs conditions, envisagez de créer un calcul basé sur une condition dans votre formulaire qui génère une seule valeur pour le filtrage.
</details>