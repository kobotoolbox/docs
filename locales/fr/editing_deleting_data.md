# Modifier et supprimer vos données
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/93bd2f1869f8d0d9b512b5ba42f05d5cf68ca56b/source/editing_deleting_data.md" class="reference">6 mai 2026</a>

Modifier et supprimer des données permet de **maintenir la qualité des données** après la collecte des soumissions. Vous pouvez avoir besoin de corriger des réponses individuelles, de mettre à jour plusieurs enregistrements à la fois, de dupliquer une soumission ou de supprimer des enregistrements qui ne sont plus nécessaires. KoboToolbox offre plusieurs façons de gérer ces tâches, notamment **la modification des soumissions via un formulaire web, la modification directe des données brutes et l'application de mises à jour en masse.** Cet article explique chaque méthode et quand l'utiliser.

<p class="note">
<strong>Note :</strong> Les soumissions collectées avec <a href="https://support.kobotoolbox.org/fr/data_collection_kobocollect.html">l'application KoboCollect</a> ne peuvent pas être modifiées ni supprimées <strong>dans KoboCollect</strong> après leur envoi. Toutes les modifications après soumission doivent être effectuées dans KoboToolbox.
</p>

Les propriétaires de projet peuvent contrôler l'accès aux données en attribuant des permissions distinctes pour afficher, modifier, valider et supprimer des soumissions. Par exemple, ils peuvent autoriser certains membres de l'équipe à modifier des données tout en restreignant les permissions de suppression.

<p class="note">
Pour en savoir plus sur les droits d'accès au niveau de l'utilisateur pour la modification et la suppression de données, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_permissions.html">Droits d'accès au niveau de l'utilisateur</a>.
</p>

## Modifier des soumissions individuelles

KoboToolbox propose deux approches de modification, chacune conçue pour des cas d'utilisation différents. Comprendre leurs différences vous aide à choisir la méthode la plus sûre et la plus appropriée pour mettre à jour vos données.

Les deux méthodes de modification des soumissions dans KoboToolbox sont :

- **Modifier les soumissions via un formulaire web :** Ouvre la soumission sous forme de [formulaire web](https://support.kobotoolbox.org/fr/glossary.html#enketo-web-forms) afin que vous puissiez corriger les réponses et renvoyer le formulaire. Cette méthode est recommandée lorsque la logique de formulaire doit être appliquée.
- **Modifier les données brutes directement dans KoboToolbox :** Ouvre un éditeur de données qui vous permet de modifier des réponses spécifiques directement. Cette méthode est recommandée lorsque vous avez besoin d'un contrôle précis sur les modifications et que vous n'avez pas besoin d'appliquer la logique de formulaire.

Chaque méthode présente ses avantages et ses limites :

![Editing data](images/editing_deleting_data/table.png)

<p class="note">
<strong>Note :</strong> Lors de la modification de données avec l'une ou l'autre méthode, le champ de métadonnées <code>_uuid</code> est mis à jour à chaque fois qu'une modification est enregistrée. Lors de la modification via un formulaire web, le champ <code>end</code> est également mis à jour. Tous les autres champs de métadonnées restent inchangés, notamment <code>_id</code>, <code>rootUuid</code>, <code>start</code>, <code>today</code>, <code>_submission_time</code> et <code>_submitted_by</code>.
</p>

### Modifier des soumissions via un formulaire web

Cette méthode ouvre une soumission sous forme de formulaire web afin que vous puissiez corriger les réponses.

Pour modifier une soumission via un formulaire web :

1. Dans la ligne de soumission, à côté de la case à cocher, cliquez sur <i class="k-icon-edit"></i> **Modifier.** La soumission s'ouvre sous forme de [formulaire web](https://support.kobotoolbox.org/fr/glossary.html#enketo-web-forms).
2. Apportez les modifications nécessaires.
3. Cliquez sur **Envoyer.**

Toutes les mises à jour, y compris les champs recalculés et les métadonnées mises à jour, apparaissent dans le tableau de données.

![Resubmit data](images/editing_deleting_data/resubmit.png)

<p class="note">
<strong>Note :</strong> Étant donné que cette méthode rouvre et renvoie le formulaire, elle peut <strong>modifier involontairement d'autres champs</strong>, notamment ceux affectés par la logique de saut ou les calculs. Elle utilise également la version la plus récente du formulaire. Par conséquent, vous devrez peut-être <strong>fournir des réponses aux questions nouvellement ajoutées</strong>, et les réponses aux questions qui ont été supprimées du formulaire <strong>seront effacées.</strong>
</p>

### Modifier les données brutes dans KoboToolbox

Cette méthode vous permet de contourner la logique de formulaire et de modifier directement les réponses stockées sans rouvrir le formulaire. Elle est utile lorsque des modifications ne peuvent pas être effectuées via un formulaire web, par exemple si la logique de formulaire empêche le renvoi ou si des questions nouvellement obligatoires nécessitent des réponses.

Pour modifier les données brutes dans KoboToolbox :

1. Sélectionnez la soumission à l'aide de la case à cocher.
2. Cliquez sur <i class="k-icon-edit"></i> **Modifier** au-dessus du tableau de données.
3. Dans la fenêtre de modification, cliquez sur **Modifier** à côté du champ que vous souhaitez changer et saisissez la nouvelle valeur.
    - Pour les questions à choix multiple, saisissez une ou plusieurs [valeurs XML](https://support.kobotoolbox.org/fr/glossary.html#xml-value) valides, séparées par des espaces.
4. Cliquez sur **Sauvegarder**, puis sur **Confirmer et fermer.**

![Edit your data](images/editing_deleting_data/edit.png)

<p class="note">
<strong>Note :</strong> Il est recommandé de suivre les modifications de données dans un journal externe ou dans un champ de commentaires dédié. Les modifications ne peuvent pas être annulées, mais elles peuvent être modifiées à nouveau ultérieurement.
</p>

## Modifier plusieurs soumissions en masse

Lorsque vous travaillez avec de grands ensembles de données, vous pouvez avoir besoin de mettre à jour plusieurs enregistrements en même temps. La modification en masse permet de corriger des erreurs systématiques, de compléter des informations manquantes et de standardiser les réponses dans de nombreuses soumissions. Cette approche réduit les tâches répétitives et accélère le processus de nettoyage des données.

Vous pouvez modifier plusieurs soumissions en masse en utilisant la méthode de modification des données brutes dans KoboToolbox :

1. Sélectionnez les soumissions que vous souhaitez modifier à l'aide des cases à cocher.
2. Cliquez sur <i class="k-icon-edit"></i> **Modifier** au-dessus du tableau. Une fenêtre s'ouvre affichant les réponses pour toutes les soumissions sélectionnées.
3. Cliquez sur **Modifier** à côté du champ que vous souhaitez mettre à jour.
4. Saisissez une nouvelle valeur, ou cliquez sur **Sélectionner** pour appliquer une valeur existante à toutes les soumissions sélectionnées.
5. Cliquez sur **Sauvegarder**, puis sur **Confirmer et fermer.**

![Bulk edit data](images/editing_deleting_data/bulk_edit.png)

<p class="note">
<strong>Note :</strong> Vous pouvez sélectionner toutes les soumissions de la page en cours en cliquant sur la case à cocher dans l'en-tête du tableau. Pour sélectionner toutes les soumissions du projet sur toutes les pages, cliquez sur la flèche à côté de la case à cocher et choisissez <strong>Sélectionner tous les résultats.</strong>
</p>

## Dupliquer des soumissions

Vous pouvez dupliquer une soumission en suivant les étapes ci-dessous :

1. Dans la ligne de soumission, à côté de la case à cocher, cliquez sur <i class="k-icon-view"></i> **Afficher.**
2. En haut à droite de la fenêtre de soumission, cliquez sur **Dupliquer.**
3. La soumission dupliquée s'ouvre dans une nouvelle fenêtre, où vous pouvez la **Modifier** ou l'**Éliminer** selon vos besoins.

![Duplicate submissions](images/editing_deleting_data/duplicate.png)

<p class="note">
<strong>Note :</strong> Lors de la duplication d'une soumission, les données de réponse sont copiées, mais le statut de validation est réinitialisé. Les champs de métadonnées sont mis à jour pour refléter la nouvelle soumission, notamment <code>start</code>, <code>end</code>, <code>today</code>, <code>_id</code>, <code>_uuid</code>, <code>_submission_time</code> et <code>_submitted_by</code>.
</p>

## Supprimer vos données

La suppression de données retire définitivement des enregistrements de votre projet et doit être effectuée avec précaution. Vous pouvez avoir besoin de supprimer des soumissions pour éliminer des doublons, nettoyer des données de test ou résoudre des problèmes de qualité des données. KoboToolbox vous permet de supprimer des soumissions individuelles ou plusieurs soumissions à la fois.

### Supprimer des soumissions

1. Sélectionnez la ou les soumissions que vous souhaitez supprimer.
2. Cliquez sur <i class="k-icon-trash"></i> **Supprimer** au-dessus du tableau de données.
3. Confirmez la suppression.

Les soumissions supprimées sont définitivement retirées et ne peuvent pas être récupérées.

![Delete submissions](images/editing_deleting_data/delete.png)

<p class="note">
<strong>Note :</strong> Vous pouvez utiliser les <strong>journaux d'historique du projet</strong> pour <a href="https://support.kobotoolbox.org/fr/activity_logs.html">suivre les modifications et les suppressions</a> effectuées par les utilisateurs du projet.
</p>

### Supprimer la réponse d'un champ spécifique

Dans certains cas, vous pouvez souhaiter supprimer les réponses d'un seul champ sans supprimer l'intégralité de la soumission. Cela peut être utile pour l'anonymisation des données, par exemple lors de la suppression d'informations personnellement identifiables après qu'elles ont été stockées en toute sécurité.

Il n'existe pas d'option dédiée à la suppression d'une valeur de champ unique. Vous pouvez toutefois effacer ou remplacer la valeur en suivant l'approche ci-dessous :

1. Sélectionnez la ou les soumissions que vous souhaitez mettre à jour.
2. Cliquez sur <i class="k-icon-edit"></i> **Modifier** au-dessus du tableau de données.
3. Cliquez sur **Modifier** à côté du champ que vous souhaitez effacer, puis saisissez un espace ou une valeur de remplacement telle que « deleted » ou « N/A ».
4. Cliquez sur **Sauvegarder**, puis sur **Confirmer et fermer.**

<p class="note">
<strong>Note :</strong> Vous pouvez supprimer des <strong>pièces jointes multimédias</strong> de vos données, individuellement ou en masse. Pour plus d'informations, consultez l'article <a href="https://support.kobotoolbox.org/fr/managing_media_responses.html#deleting-media-files">Gérer les réponses média soumises par les répondants</a>.
</p>

## Résolution de problèmes

<details>
  <summary><strong>La modification via un formulaire web modifie ou supprime des données</strong></summary>
  Lorsque vous rouvrez des formulaires complexes sous forme de formulaire web, les champs affectés par la logique de saut, les calculs ou les liaisons dynamiques de projets peuvent changer. Ces comportements peuvent empêcher le renvoi du formulaire ou supprimer des données qui ne satisfont plus les conditions logiques. Si vous ne pouvez pas renvoyer le formulaire, vous pouvez quitter le formulaire web et aucune modification ne sera enregistrée. Pour éviter ces effets, modifiez plutôt les données brutes directement.
</details>

<br>

<details>
  <summary><strong>Modification via un formulaire web après l'ajout de nouvelles questions</strong></summary>
  Si vous modifiez une soumission plus ancienne via un formulaire web après avoir mis à jour et redéployé le formulaire, la soumission s'ouvre dans la dernière version du formulaire. Cela peut poser des problèmes lorsque de nouvelles questions obligatoires ont été ajoutées, car vous devez fournir des réponses valides à ces questions pour pouvoir enregistrer vos modifications dans la soumission d'origine.
</details>

<br>

<details>
  <summary><strong>Les données modifiées n'apparaissent pas dans les exports</strong></summary>
  Si vous modifiez une soumission et ajoutez des données à une question qui n'existe que dans une version plus récente du formulaire, ces données peuvent ne pas apparaître dans les exports lorsque l'option <strong>Inclure les champs de toutes les versions</strong> est sélectionnée dans les <a href="https://support.kobotoolbox.org/fr/advanced_export.html#selecting-data-fields-for-export">paramètres d'exportation</a>.
<br><br>
Pour résoudre ce problème, décochez <strong>Inclure les champs de toutes les versions</strong> dans les paramètres d'exportation. Les données ajoutées aux questions des versions plus récentes du formulaire seront alors incluses dans l'export.
</details>

<br>

<details>
  <summary><strong>Les géoformes auto-intersectantes bloquent les modifications dans les formulaires web</strong></summary>
  KoboCollect peut enregistrer des géoformes auto-intersectantes lorsque les coordonnées GPS fluctuent pendant qu'un collecteur de données est immobile. Ces polygones peuvent être envoyés avec succès depuis KoboCollect, mais la réouverture de la même soumission via un formulaire web peut déclencher une erreur de géométrie. Les formulaires web ne permettent pas d'enregistrer le formulaire tant que le polygone n'est pas corrigé, ce qui peut être difficile à corriger manuellement.
    <br><br>
Dans cette situation, utilisez la modification des données brutes dans KoboToolbox pour mettre à jour les champs requis sans rouvrir la soumission via un formulaire web. Cela permet d'éviter l'erreur de validation de géométrie.
</details>

<br>

<details>
  <summary><strong>Les modifications de coordonnées échouent si le format requis n'est pas utilisé</strong></summary>
  Lors de la modification de coordonnées à l'aide de la méthode de modification des données brutes, les valeurs doivent suivre le format exact de KoboToolbox : <code>latitude longitude altitude précision</code>. Par exemple, les coordonnées de Paris seraient <code>48.8566 2.3522 0 0</code>. <br><br>
Si une partie est manquante ou mal formatée, la modification peut ne pas être enregistrée ou peut causer des problèmes lors de l'export. Assurez-vous que les quatre valeurs sont incluses et séparées par des espaces avant d'enregistrer.
</details>

<br>

<details>
  <summary><strong>Un formulaire utilisant des liaisons dynamiques de projets pour empêcher les soumissions en double ne peut pas être modifié via un formulaire web</strong></summary>
  Si votre formulaire utilise des liaisons dynamiques de projets pour <a href="https://support.kobotoolbox.org/fr/dynamic_data_attachment.html#dynamically-linking-a-form-to-itself">empêcher les soumissions en double</a>, la réouverture d'une soumission via un formulaire web bloquera le renvoi car elle est détectée comme un doublon. Dans ce cas, utilisez la modification des données brutes dans KoboToolbox plutôt que la modification via un formulaire web.
</details>

<br>

<details>
  <summary><strong>Vérifier si une soumission a été modifiée</strong></summary>
  Pour vérifier si une soumission a été modifiée, vous pouvez généralement comparer le champ <code>_uuid</code> avec le champ <code>rootUuid</code> dans le tableau de données ou dans les données exportées. La valeur <code>rootUuid</code> reste la même pour la soumission d'origine, tandis que la valeur <code>_uuid</code> change à chaque fois que la soumission est modifiée. Si les valeurs sont différentes, la soumission a probablement été modifiée.
</details>

<br>