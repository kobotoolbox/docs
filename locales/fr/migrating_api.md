# Migration de l'API v1 vers v2
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/7a618b1d0f3bc3dffa450c17d9e5063ca4c69770/source/migrating_api.md" class="reference">7 août 2025</a>

Dans le cadre de nos efforts continus pour rationaliser et moderniser la plateforme KoboToolbox, nous supprimons progressivement les points de terminaison KPI et KoboCAT `v1`. Tous les points de terminaison KPI et KoboCAT `v1` sont désormais obsolètes et seront entièrement supprimés en janvier 2026. Les points de terminaison `v1` sont progressivement supprimés au profit de l'API KPI `v2`, plus robuste et entièrement prise en charge.

Cet article explique comment migrer vos intégrations API de l'API `v1` (KoboCAT et KPI) vers l'API KPI `v2`. Il couvre chaque point de terminaison `v1` obsolète et son équivalent `v2` pour vous aider à faire la transition de vos flux de travail.


## Migration de KPI v1 vers KPI v2
La migration de l'ancienne API KPI (`v1`) vers la nouvelle version (`v2`) est simple dans la plupart des cas.

En général, vous devez uniquement mettre à jour le chemin de base de `/endpoint/` vers `/api/v2/endpoint/`.

### Exception pour le point de terminaison exports
La seule exception à la règle ci-dessus concerne le point de terminaison `/exports/`. Dans `v1`, le point de terminaison `/exports/` renvoyait **tous les exports pour l'utilisatrice ou utilisateur authentifié** sur tous les projets.

Dans `v2`, pour des raisons de performance, les exports sont désormais **limités par projet** et doivent être accessibles via `/api/v2/assets/{asset_uid}/exports/`.



## Migration de KoboCAT v1 vers KPI v2
La section suivante répertorie les principaux points de terminaison de l'API KoboCAT `v1` et fournit leurs équivalents `v2`.

### Points de terminaison de données : Liste de projets
Ce point de terminaison renvoie une liste de formulaires auxquels vous avez accès, avec des liens vers leurs données de soumission, servant de point d'entrée pour accéder ou télécharger les réponses.

**Correspondance des points de terminaison de `v1` à `v2`**

| Point de terminaison `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data`          | `/api/v2/assets/?asset_type=survey`  |


**Correspondance des champs de `v1` à `v2`**

| Champ `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `id`          | `uid`<sup>1</sup>      |
| `id_string`   | `uid`                  |
| `title`       | `name`                 |
| `description` | `settings.description` |
| `url`         | `data`                 |

<sup>1</sup> _Dans le point de terminaison `/api/v2/assets`, les identifiants entiers séquentiels ne sont plus utilisés. Chaque entrée est identifiée de manière unique par un `uid` alphanumérique_


**Exemple de réponse `v1`**

```json
{
  "id": 474,
  "id_string": "a4etXeWtqcoodSxLV8a6Uq",
  "title": "Pathways Initiative",
  "description": "Pathways Initiative",
  "url": "https://kc.kobotoolbox.org/api/v1/data/474.json"
}
```

**Réponse équivalente `v2`**

```json
{
  "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/",
  "uid": "a4etXeWtqcoodSxLV8a6Uq",
  "name": "Pathways Initiative",
  "settings": {
    "description": "A humanitarian project supporting access"
  },
  "data": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/data/"
  ...
}

```

---

### Points de terminaison de données : Données de soumission
Ces points de terminaison récupèrent toutes les données de soumission pour un projet spécifique ou une seule soumission du projet. `{uid}` est l'identifiant unique du projet et `{submission_id}` est l'identifiant unique d'une soumission de formulaire.

| Point de terminaison `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

En vous basant sur l'`url` que vous obtenez de la propriété `data` dans le point de terminaison asset, vous pouvez récupérer les données de soumission dans `v2`.

<p class="note">
  <b>Remarque :</b> La structure de réponse est presque identique, <strong>sauf que <code>v2</code> introduit la pagination</strong>.
</p>


**Exemple de réponse `v1`**

```json
[
  {
    "_id": 49542,
    ...
  }
]
```
**Réponse équivalente `v2`**

```json
{
  "count": 1200,
  "next": null,
  "previous": null,
  "results": [
    {
      "_id": 49542,
      ...
    }
  ]
}
```
</details>

---


### Points de terminaison de formulaire
Ces points de terminaison renvoient les attributs détaillés de tous les formulaires partagés avec vous ou d'un formulaire spécifique, où `{uid}` est l'identifiant unique du projet.

**Correspondance des points de terminaison**

| Point de terminaison `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/forms`   | `/api/v2/assets/?asset_type=survey` |
| `/api/v1/forms/<pk>`       | `/api/v2/assets/{asset_uid}/`                 |


<p class="note">
  <b>Remarque :</b> Le point de terminaison <code>v2</code> suit la même structure pour chaque élément que celle listée ci-dessous, mais introduit la pagination. Certaines propriétés du point de terminaison <code>v1</code> ne sont pas directement disponibles sur le point de terminaison asset <code>v2</code>, mais elles peuvent toujours être accessibles différemment (voir la légende sous le tableau pour plus de détails).
</p>


**Correspondance des champs**
| Champ `v1`                 | Équivalent `v2`                          |
|----------------------------|------------------------------------------|
| `formid`                   | `uid`<sup>1</sup>                        |
| `owner`                    | `owner__username`                        |
| `metadata`                 | `files`                                  |
| `tags`                     | `tag_string`<sup>2</sup>                 |
| `title`                    | `name`                                   |
| `public`                   | _N/A_<sup>3</sup>                        |
| `public_data`              | _N/A_<sup>3</sup>                        |
| `require_auth`             | _N/A_<sup>3</sup>                        |
| `users`                    | `permissions`                            |
| `hash`                     | `version__content_hash`                  |
| `downloadable`             | `deployment__active`                     |
| `encrypted`                | `deployment__encrypted`                  |
| `last_submission_time`     | `deployment__last_submission_time`       |
| `uuid`                     | `deployment__uuid`                       |
| `instances_with_geopoints` | `summary.geo`                            |
| `num_of_submissions`       | `deployment__submission_count`           |
| `attachment_storage_bytes` | _N/A_<sup>4</sup>                        |

<sup>1</sup> _Dans le point de terminaison `/api/v2/assets`, les identifiants entiers séquentiels ne sont plus utilisés. Chaque entrée est identifiée de manière unique par un `uid` alphanumérique_.  
<sup>2</sup> _Dans `v1`, les balises étaient renvoyées sous forme de tableau ; dans `v2`, elles sont renvoyées sous forme de chaîne séparée par des virgules._  
<sup>3</sup> _Ces champs ne sont plus exposés. Voir la section **Permissions** ci-dessous pour plus de détails._  
<sup>4</sup> _Non directement accessible via le point de terminaison asset. Utilisez le point de terminaison `/api/v2/asset_usage/` et récupérez le champ `storage_bytes` du projet correspondant._

<details>
<summary><strong>Exemple de réponse <code>v1</code></strong></summary>
<br>
  
```json
{
  "url": "https://kf.kobotoolbox.org/api/v1/forms/474",
  "formid": 474,
  "metadata": [],
  "owner": "project_owner",
  "public": false,
  "public_data": false,
  "require_auth": true,
  "tags": ["my_tag", "my_other_tag"],
  "title": "Pathways Initiative",
  "users": [
    {
      "user": "project_owner",
      "permissions": [
        "add_xform",
        "change_xform",
        "delete_data_xform",
        "delete_xform",
        "move_xform",
        "report_xform",
        "transfer_xform",
        "validate_xform",
        "view_xform"
      ]
    }
  ],
  "hash": "md5:65ee54b6412379b0e35b27a97d606c29",
  "downloadable": true,
  "encrypted": false,
  "id_string": "a4etXeWtqcoodSxLV8a6Uq",
  "last_submission_time": "2025-06-03T15:16:20.838131Z",
  "uuid": "f739945244514a6bb304dc35d6049880",
  "instances_with_geopoints": false,
  "num_of_submissions": 1200,
  "attachment_storage_bytes": 27240767883
}
```

</details>


<details>
<summary><strong>Réponse équivalente <code>v2</code></strong></summary>
<br>

```json
{
  "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/",
  "owner__username": "project_owner",
  "files": [],
  "summary": {
    "geo": false
  },
  "version__content_hash": "05be1113c6ae66665059fea5943ce90a97d966db",
  "deployment__active": true,
  "deployment__submission_count": 1200,
  "deployment__last_submission_time": "2025-06-03T15:16:20.838131Z",
  "deployment__encrypted": false,
  "deployment__uuid": "f739945244514a6bb304dc35d6049880",
  "tag_string": "my_tag,my_other_tag",
  "uid": "a4etXeWtqcoodSxLV8a6Uq",
  "name": "Pathways Initiative",
  "permissions": [
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pQnggGHaPGGmJtPCbCCVpU/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/add_submissions/",
      "label": "Add submissions"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pcn2g8ezroevNsP7CuCkrf/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/change_asset/",
      "label": "Edit form"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pVMKQ4bDSn5SCAgefzMRLX/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/change_submissions/",
      "label": "Edit submissions"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pwoCoBBLmyWsdF2dXPBaHt/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/delete_submissions/",
      "label": "Delete submissions"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pqDGr7M7au4NsFiuKkEeTr/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/manage_asset/",
      "label": "Manage project"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/p3dFAXPvHX3ib93twD7rPG/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/validate_submissions/",
      "label": "Validate submissions"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pE38Wi89CavBvNHGqQ2WZj/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/view_asset/",
      "label": "View form"
    },
    {
      "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pWeJkdjjFk9cQVFvLnr6cS/",
      "user": "https://kf.kobotoolbox.org/api/v2/users/project_owner/",
      "permission": "https://kf.kobotoolbox.org/api/v2/permissions/view_submissions/",
      "label": "View submissions"
    }
  ]
}
```
</details>

<br>

<a id="tags"></a>
**Balises**

Les balises dans `v1` et `v2` ne partagent pas la même base de données sous-jacente. Par conséquent, les balises de `v1` **ne seront pas automatiquement migrées** vers `v2`. Si vous devez les conserver, vous devez réappliquer les balises manuellement en utilisant une requête `PATCH` vers `/api/v2/assets/{uid}/`.

Exemple de charge utile :
```json
{ "tag_string": "tag1,tag2,tag3" }
```

**Permissions**

Dans `v2`, les champs `public`, `public_data` et `require_auth` ne sont plus exposés en tant qu'attributs booléens. Au lieu de cela, **l'accès anonyme est contrôlé via des attributions de permissions explicites à l'`AnonymousUser`**.

Les correspondances suivantes s'appliquent :
- `public: true` → l'`AnonymousUser` a la permission `view_asset`  
- `public_data: true` → l'`AnonymousUser` a la permission `view_submissions`  
- `require_auth: false` → l'`AnonymousUser` a la permission `add_submissions`  


<details>
<summary><strong>Exemple : permissions d'utilisatrice ou utilisateur anonyme <code>v2</code></strong></summary>
<br>
  
```json
[
  {
    "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pqEVtLkmHerjBYcEWBcZPG/",
    "user": "https://kf.kobotoolbox.org/api/v2/users/AnonymousUser/",
    "permission": "https://kf.kobotoolbox.org/api/v2/permissions/add_submissions/",
    "label": "Add submissions"
  },
  {
    "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/phjb8xYQ9CjcLuXfnpZCHu/",
    "user": "https://kf.kobotoolbox.org/api/v2/users/AnonymousUser/",
    "permission": "https://kf.kobotoolbox.org/api/v2/permissions/view_asset/",
    "label": "View form"
  },
  {
    "url": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/pQpqWikpQbjzeVCJgHoubH/",
    "user": "https://kf.kobotoolbox.org/api/v2/users/AnonymousUser/",
    "permission": "https://kf.kobotoolbox.org/api/v2/permissions/view_submissions/",
    "label": "View submissions"
  }
]
```
</details>

<br>

---

### Point de terminaison Label
Le point de terminaison `/api/v1/forms/<pk>/labels` de `v1` renvoie un dictionnaire mappant chaque nom de champ du formulaire à son étiquette correspondante, permettant un affichage plus convivial des données du formulaire.

Ce point de terminaison n'a pas été porté vers `v2`, mais il est toujours possible d'**étiqueter** ou de **baliser** un projet, comme décrit [ci-dessus](#tags).

---

### Points de terminaison de métadonnées
Ces points de terminaison renvoient une liste plate de tous les fichiers médias associés à l'utilisatrice ou utilisateur actuel, sur tous les projets déployés ou un projet spécifique. Dans `v2`, les fichiers médias sont désormais limités par projet. Comme pour les autres points de terminaison, `v2` introduit la pagination, alors que `v1` renvoie tous les résultats en une seule réponse.

**Correspondance des points de terminaison**

| Point de terminaison `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/metadata`   | `/api/v2/assets/{asset_uid}/files/` |
| `/api/v1/metadata/<pk>`       | `/api/v2/assets/{asset_uid}/files/{file_uid}/`                 |


<p class="note">
  <b>Remarque :</b> <code>v2</code> ne prend en charge que les fichiers médias : <code>media</code> de <code>v1</code> est mappé à <code>form_media</code> dans <code>v2</code>. <strong>Les autres types de métadonnées</strong> de <code>v1</code> (par exemple, <code>doc</code>, <code>mapbox_layer</code>, <code>source</code> etc.) n'ont pas été portés vers <code>v2</code>.
</p>


**Correspondance des champs**

| Champ `v1`        | Équivalent `v2`                        |
|-------------------|----------------------------------------|
| `id`              | `uid`                                  |
| `data_type`       | `file_type`                            |
| `xform`           | _N/A_<sup>1</sup>                      |
| `data_value`      | `metadata.filename` ou `metadata.redirect_url` |
| `data_filename`   | `metadata.filename`                    |
| `data_file`       | `content`                              |
| `data_file_type`  | `metadata.mimetype`                    |
| `file_hash`       | `metadata.hash`                        |
| `from_kpi`        | _N/A_                                  |

<sup>1</sup> _Dans `v2`, le projet associé est accessible via le champ `asset`, qui contient une URL complète au lieu d'un ID entier._

**Exemple de réponse `v1`**

```
{
  "id": 271,
  "xform": 374,
  "data_value": "goose.jpg",
  "data_type": "media",
  "data_file": "/project_owner/form-media/b44a7c2cd0f244e6b405821582364657/goose.jpg",
  "data_file_type": "image/jpeg",
  "file_hash": "md5:93fb96bced1e3b392abfc22934afe51a",
  "url": "https://kc.kobotoolbox.org/api/v1/metadata/271?format=json",
  "from_kpi": true,
  "data_filename": "goose.jpg"
}
```

**Réponse équivalente `v2`**

```
{
  "uid": "afoeCcF3AcGNpWUoM6bvKj9",
  "asset": "http://kf.kobo.localhost/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/",
  "file_type": "form_media",
  "content": "http://kf.kobo.localhost/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/afoeCcF3AcGNpWUoM6bvKj9/content/",
  "metadata": {
    "hash": "md5:93fb96bced1e3b392abfc22934afe51a",
    "filename": "goose.jpg",
    "mimetype": "image/jpeg"
  },
  ...  
}
```

---

### Points de terminaison utilisateur
Ce point de terminaison renvoie les informations de profil sur l'utilisatrice ou utilisateur authentifié, y compris l'identité du compte et les détails associés.

**Correspondance des points de terminaison**

| Point de terminaison `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/user`   | `/me/` |


**Correspondance des champs**

| Champ `v1`        | Équivalent `v2`                        |
|-------------------|----------------------------------------|
| `id`              | `extra_details__uid`                                  |
| `username`       | `username`                            |
| `email`           |  `email`               |
| `city`           |  `extra_details.city`  |
| `country`           |  `extra_details.country`  |
| `organization`           |  `extra_details.organization`  |
| `website`           |  `extra_details.website`  |
| `twitter`           |  `extra_details.twitter`  |
| `url`           |  N/A<sup>1</sup>  |
| `user`           |  N/A<sup>1</sup>  |
| `gravatar`           |  `gravatar`  |
| `require_auth`           |  `require_auth`  |
| `api_token`           |  N/A<sup>2</sup>  |
| `temp_token`           |  N/A<sup>1</sup>  |


<sup>1</sup> _Non porté vers `v2`_

<sup>2</sup> _Utilisez https://kf.domain.tld/token à la place_