# Voir et valider vos données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/54acbc6a5e616ccc3a13d7a6fcb1c3f2f29d9243/source/viewing_validating_data.md" class="reference">5 juin 2026</a>

<iframe src="https://www.youtube.com/embed/X5W6nv9gYUo?si=n3eniC0Uq_PzFsbT&cc_lang_pref=fr&hl=fr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Le mode **Tableau** dans la section **DONNÉES** de votre projet KoboToolbox offre une vue d'ensemble complète et personnalisable de toutes les soumissions du projet. Par défaut, toutes les soumissions sont affichées, les plus récentes en premier. Ce mode est l'espace de travail principal pour explorer les données, surveiller leur qualité, valider les soumissions et effectuer des modifications.

Cet article explique comment :

- Configurer le tableau de données en mode **Tableau**
- Filtrer et trier vos données
- Voir et valider les soumissions

<p class="note">
Pour en savoir plus sur la modification de vos données, consultez l'article <a href="https://support.kobotoolbox.org/fr/editing_deleting_data.html">Modifier et supprimer vos données</a>.
</p>

Les propriétaires de projet peuvent contrôler l'accès aux données en attribuant des permissions distinctes pour voir, modifier, valider et supprimer les soumissions. Par exemple, ils peuvent autoriser certains membres de l'équipe à voir et valider les données tout en restreignant les permissions de modification et de suppression.

<p class="note">
Pour en savoir plus sur les droits d'accès au niveau de l'utilisateur pour voir, valider et modifier les données, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_permissions.html">Droits d'accès au niveau de l'utilisateur</a>.
</p>

## Configurer le tableau de données

Le tableau de données en mode **Tableau** affiche par défaut toutes les soumissions et tous les champs. Dans de nombreux projets, une vue plus ciblée est nécessaire. Ajuster ce qui apparaît dans le tableau vous permet de travailler plus efficacement, en particulier pour les formulaires comportant de nombreuses questions ou des sous-groupes. Vous pouvez choisir les champs à afficher et la façon dont les données sont présentées pour mieux correspondre à votre flux de travail.

![Choisir les champs à afficher dans le tableau de données](images/viewing_validating_data/table_view.png)

### Personnaliser le tableau de données

Au-dessus du tableau de données, vous pouvez configurer les paramètres suivants :

- **Masquer les champs :** Cliquez sur <i class="k-icon-qt-hidden"></i> **masquer les champs** pour afficher la liste de toutes les questions et de tous les champs de votre formulaire. Tous les champs sont sélectionnés par défaut. Décochez la case d'un champ pour le masquer, puis cliquez sur **Appliquer** pour enregistrer vos modifications.
- **Basculer en plein écran :** Cliquez sur <i class="k-icon-expand"></i> **Basculer en plein écran** pour agrandir le tableau de données afin qu'il occupe toute la fenêtre du navigateur.
- **Options d'affichage :** Cliquez sur <i class="k-icon-settings"></i> **Options d'affichage** pour contrôler la façon dont les libellés, les groupes et les balises HXL sont affichés dans le tableau. Les options d'affichage suivantes peuvent être configurées :

| Option d'affichage | Description |
|:---|:---|
| Afficher les libellés ou des valeurs XML ? | Choisissez d'afficher les <a href="https://support.kobotoolbox.org/fr/glossary.html#xml-value">valeurs XML</a> ou les libellés complets des questions et des choix dans <a href="https://support.kobotoolbox.org/fr/collecting_data_multiple_languages.html">n'importe quelle langue du formulaire</a> dans votre tableau. |
| Afficher le nom des groupes dans l'en-tête du tableau | Choisissez si les en-têtes de colonnes du tableau incluent le nom du groupe de questions (par ex., `demographics / age`). |
| Afficher les tags HXL | Affiche les balises du <a href="https://support.kobotoolbox.org/fr/question_options.html#hxl">langage d'échange humanitaire</a> (HXL) si elles ont été ajoutées à votre formulaire. |

Dans le tableau de données, vous pouvez cliquer sur un en-tête de colonne et sélectionner <i class="k-icon-qt-hidden"></i> **Masquer le champ** pour supprimer les champs dont vous n'avez pas besoin, ou <i class="k-icon-freeze"></i> **Figer le champ** pour garder un champ fréquemment utilisé visible pendant le défilement.

<p class="note">
<strong>Remarque :</strong> Ces paramètres affectent le mode <strong>Tableau</strong> pour tous les utilisateurs du projet.
</p>

### Naviguer dans le tableau de données

Vous pouvez modifier le nombre de lignes affichées par page à l'aide du menu déroulant situé en bas du tableau. Par défaut, le tableau affiche 30 lignes.

<p class="note">
<strong>Remarque :</strong> Afficher un grand nombre de lignes à la fois peut ralentir votre navigateur.
</p>

Utilisez les flèches <i class="k-icon-caret-left"></i> **PREV** et **NEXT** <i class="k-icon-caret-right"></i>, ou saisissez un numéro de page, pour naviguer dans le tableau de données.

### Champs de soumission générés par le système

Chaque soumission dans le tableau de données inclut des champs générés par le système qui permettent d'identifier les soumissions et de suivre leurs détails. Ces champs apparaissent sous forme de colonnes distinctes à la fin du tableau et ne peuvent pas être modifiés.

| Champ | Description |
|:---|:---|
| `__version__` | Un identifiant unique pour la version du formulaire utilisée pour la soumission. Ce champ est utile si votre formulaire a évolué au fil du temps et que vous devez savoir quelle version a collecté les données. |
| <code>_id</code> | Un numéro d'identifiant généré par le serveur pour la soumission. Il est attribué une fois que la soumission parvient à KoboToolbox et est unique sur ce serveur KoboToolbox. |
| <code>_uuid</code> | Un identifiant généré automatiquement pour la soumission. Il peut aider à identifier une soumission, mais il peut changer si la soumission est modifiée ; il n'est donc pas le champ le plus fiable pour un suivi à long terme. |
| <code>_submission_time</code> | La date et l'heure auxquelles la soumission a été reçue par le serveur KoboToolbox. Dans les exports, cette valeur est stockée en UTC. Dans le tableau de données, elle est affichée dans le fuseau horaire de l'utilisateur. |
| <code>_submitted_by</code> | Le nom d'utilisateur de la personne qui a soumis les données. Ce champ est toujours enregistré pour les soumissions KoboCollect, et est enregistré pour les soumissions via formulaire web uniquement lorsque <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">l'authentification est requise</a>. |
| <code>rootUuid</code> | Un identifiant stable pour la soumission au sein du projet. Il est tiré du <code>_uuid</code> original de la soumission lors du premier envoi, et ne change pas lorsque la soumission est modifiée ; c'est donc le champ le plus fiable pour suivre une soumission spécifique dans le temps. |

<p class="note">
<strong>Remarque :</strong> Ces champs diffèrent des <a href="https://support.kobotoolbox.org/fr/form_meta.html">métadonnées de formulaire</a> activées par l'utilisateur, car ils sont générés automatiquement pour chaque soumission. Vous n'avez pas besoin de les ajouter lors de la création du formulaire.
</p>

## Filtrer et trier vos données

Par défaut, les soumissions dans KoboToolbox apparaissent dans le tableau de données dans l'ordre de soumission, les entrées les plus récentes en haut. Dans les grands projets, le filtrage et le tri sont essentiels pour explorer, examiner et nettoyer les données. Ils vous permettent de trouver rapidement des répondants spécifiques, d'examiner des tendances et d'identifier les soumissions qui nécessitent une attention particulière.

<p class="note">
<strong>Remarque :</strong> Le mode <strong>Tableau</strong> dans KoboToolbox offre des fonctions de filtrage et de tri de base pour la surveillance et la modification des données. Pour une analyse de données plus avancée, notamment le filtrage avec plusieurs conditions, nous recommandons d'<a href="https://support.kobotoolbox.org/fr/export_download.html">exporter votre base de données</a> et d'utiliser un logiciel de tableur ou d'analyse.
</p>

Pour chaque colonne du tableau de données, vous pouvez utiliser les fonctionnalités suivantes :

- **Recherche :** Utilisez la barre de recherche au-dessus des champs de type texte, chiffre et date pour filtrer les résultats. Par exemple, vous pouvez rechercher un identifiant unique ou filtrer par un âge spécifique.
- **Filtre :** Pour les champs basés sur des questions à choix multiple, cliquez sur **Afficher tout** dans l'en-tête de colonne pour ouvrir une liste d'options de réponse. Sélectionnez une option pour filtrer les réponses.
- **Tri :** Cliquez sur un en-tête de colonne et choisissez **Trier A → Z** ou **Trier Z → A** pour modifier l'ordre des soumissions.

<p class="note">
<strong>Remarque :</strong> Le tri du tableau s'applique à tous les utilisateurs et persiste après que vous avez quitté le mode <strong>Tableau</strong>. La recherche et le filtrage ne s'appliquent qu'à vous pendant que vous êtes en mode <strong>Tableau</strong> et se réinitialisent automatiquement lorsque vous le quittez.
</p>

## Voir les soumissions individuelles

Ouvrir une soumission individuelle vous permet d'examiner toutes les données d'un seul répondant. La vue de soumission individuelle inclut des outils pour examiner et gérer une soumission.

Pour ouvrir une soumission, cliquez sur <i class="k-icon-view"></i> **Afficher** dans la ligne correspondante.

![Ouvrir les détails d'une soumission](images/viewing_validating_data/open_submission.png)

La fenêtre de soumission affiche toutes les réponses et inclut les options suivantes :

- Voir les données dans [n'importe quelle langue du formulaire](https://support.kobotoolbox.org/fr/collecting_data_multiple_languages.html).
- Afficher les [valeurs XML](https://support.kobotoolbox.org/fr/glossary.html#xml-value) à côté de chaque question.
- **Afficher** et **Modifier** la soumission sous forme de [formulaire web](https://support.kobotoolbox.org/fr/editing_deleting_data.html).
- **Dupliquer** la soumission.
- <i class="k-icon-print"></i> **Imprimer** la soumission.
- <i class="k-icon-trash"></i> **Supprimer** la soumission.
- Attribuer un **statut de validation**.

![Fenêtre de visualisation d'une soumission](images/viewing_validating_data/view_submission.png)

Dans la vue de soumission individuelle, naviguez entre les soumissions à l'aide de **< Précédent** et **Suivant >**.

## Valider vos données

La validation des soumissions aide les équipes de projet à maintenir la qualité des données, à suivre l'état de la révision et à signaler les problèmes nécessitant un suivi. Le statut de validation apparaît sous forme de colonne dédiée dans le mode **Tableau**, et les utilisateurs disposant des permissions appropriées peuvent le mettre à jour pour des soumissions individuelles ou multiples.

Les statuts disponibles sont :

- **Approuvé :** La soumission a été examinée et confirmée comme complète, exacte et utilisable pour l'analyse.
- **Non approuvé :** La soumission ne répond pas aux exigences de qualité des données et doit être exclue de l'analyse ou supprimée de la base de données.
- **En attente :** La soumission nécessite un examen. Une vérification ou un suivi supplémentaire est nécessaire avant que les données puissent être acceptées ou rejetées.

La validation permet un examen structuré des données au sein d'équipes collaboratives. Par exemple, les réviseurs peuvent filtrer le tableau pour n'afficher que les soumissions nécessitant un examen.

<p class="note">
<strong>Remarque :</strong> Un propriétaire de projet peut accorder la permission <strong>Valider les soumissions</strong> à d'autres utilisateurs <a href="https://support.kobotoolbox.org/fr/managing_permissions.html">séparément</a> de la permission <strong>Modifier les soumissions</strong>.
</p>

### Mettre à jour le statut de validation en masse

Le statut de validation peut être appliqué à plusieurs soumissions à la fois, ce qui est utile pour les révisions à grande échelle ou les contrôles qualité.

Pour valider des soumissions en masse :

1. Sélectionnez les soumissions à l'aide des cases à cocher.
2. Cliquez sur **Changer le statut**.
3. Choisissez un statut de validation.

<p class="note">
<strong>Remarque :</strong> Vous pouvez sélectionner toutes les soumissions de la page actuelle en cochant la case dans l'en-tête du tableau. Pour sélectionner toutes les soumissions du projet sur toutes les pages, cliquez sur la flèche à côté de la case à cocher et choisissez <strong>Sélectionner tous les résultats.</strong>
</p>

![Sélectionner des soumissions](images/viewing_validating_data/select.png)

## Résolution de problèmes

<details>
  <summary><strong>Champs ou questions n'apparaissant pas dans le tableau de données</strong></summary>
Si vous avez ajouté de nouvelles questions après le début de la collecte de données, les champs peuvent rester masqués si la visibilité du tableau avait été configurée précédemment. Cliquez sur <i class="k-icon-qt-hidden"></i> <strong>masquer les champs</strong>, localisez et sélectionnez la nouvelle question, puis cliquez sur <strong>Appliquer.</strong>
</details>

<br>

<details>
  <summary><strong>Fonctionnalité de recherche pour les questions de type Caché</strong></summary>
  La fonctionnalité <strong>Recherche</strong> n'est pas disponible actuellement pour les questions de type <strong>Caché</strong>. Pour localiser une valeur spécifique dans un champ <strong>Caché</strong>, triez le tableau par ce champ et faites défiler jusqu'à la valeur dans l'ordre alphabétique ou numérique.
</details>

<br>

<details>
  <summary><strong>Le champ _submitted_by est vide</strong></summary>
  Le champ <code>_submitted_by</code> est renseigné uniquement lorsqu'une soumission est associée à un nom d'utilisateur KoboToolbox. Dans KoboCollect, ce champ est toujours enregistré. Dans les formulaires web, il est enregistré uniquement lorsque le projet <a href="https://support.kobotoolbox.org/fr/project_sharing_settings.html#allowing-submissions-without-authentication">requiert une authentification</a>. Si le formulaire autorise les soumissions sans nom d'utilisateur ni mot de passe, ce champ sera vide.<br><br>
Pour enregistrer <code>_submitted_by</code> pour les soumissions via formulaire web, accédez à <strong>FORMULAIRE > Collecter des données</strong> et désactivez l'option « Autoriser les soumissions sans nom d'utilisateur ni mot de passe pour ce formulaire ».
</details>

<br>