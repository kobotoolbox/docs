# Migration de l'API v1 vers l'API v2
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/235a3cc8f0f84190b5e792cf191b424123e88f46/source/migrating_api.md" class="reference">22 Jun 2026</a>


Dans le cadre de nos efforts continus pour simplifier et moderniser la plateforme KoboToolbox, tous les endpoints KPI et KoboCAT `v1` ont été supprimés. Les endpoints `v1` ont été remplacés par l'API KPI `v2`, plus robuste et entièrement disponible.

Cet article explique comment migrer vos intégrations API de l'API `v1` (KoboCAT et KPI) vers l'API KPI `v2`. Il présente chaque endpoint `v1` déprécié et son équivalent `v2` pour vous aider à faire évoluer vos workflows.

<p class="note">
  <strong>Note :</strong> Cet article s'adresse aux <strong>utilisateurs avancés</strong> qui utilisent l'API KoboToolbox pour des <strong>workflows de gestion de projets</strong>. Tous les autres utilisateurs ne sont pas concernés par cette migration. Les intégrations qui utilisent les <a href="https://support.kobotoolbox.org/fr/synchronous_exports.html">exports synchronisés</a>, tels que les tableaux de bord et autres outils de reporting externes, ne nécessitent aucune modification et continueront de fonctionner normalement.
</p>


## Authentification

Toutes les requêtes API — v1 et v2 — nécessitent un token API. Incluez-le dans chaque requête via l'en-tête `Authorization` :

```
Authorization: Token xxxx
```

Remplacez `xxxx` par votre token réel. Vous pouvez trouver votre token à l'adresse `https://kf.kobotoolbox.org/token/` (ou l'équivalent pour votre serveur).

**curl**
```bash
curl -H "Authorization: Token xxxx" "https://kf.kobotoolbox.org/api/v2/assets/"
```

**Python** (`requests`)
```python
import requests

TOKEN = "xxxx"
BASE_URL = "https://kf.kobotoolbox.org"
headers = {"Authorization": f"Token {TOKEN}"}

response = requests.get(f"{BASE_URL}/api/v2/assets/", headers=headers)
response.raise_for_status()
data = response.json()
```

**R** (`httr`)
```r
library(httr)

TOKEN <- "xxxx"
BASE_URL <- "https://kf.kobotoolbox.org"

response <- GET(
  paste0(BASE_URL, "/api/v2/assets/"),
  add_headers(Authorization = paste("Token", TOKEN))
)
data <- content(response, as = "parsed")
```

<p class="note">
  <strong>Note :</strong> L'en-tête d'authentification est identique pour toutes les versions de l'API. Ce qui change dépend du chemin de migration emprunté : si vous migrez de <strong>KPI v1 vers KPI v2</strong>, vous devez uniquement mettre à jour le chemin de l'URL. Si vous migrez de <strong>KoboCAT v1 vers KPI v2</strong>, vous devrez également mettre à jour le domaine de base (<code>kc.kobotoolbox.org</code> → <code>kf.kobotoolbox.org</code>), les chemins des endpoints, et adapter votre code pour gérer la nouvelle structure de réponse et les nouveaux noms de champs — voir les sections ci-dessous.
</p>


## Migration de KPI v1 vers KPI v2
La migration de l'ancienne API KPI (`v1`) vers la nouvelle version (`v2`) est simple dans la plupart des cas.

En général, il vous suffit de mettre à jour le chemin de base de `/endpoint/` vers `/api/v2/endpoint/`.

### Exceptions
Il existe deux exceptions à la règle ci-dessus.

**Exception pour l'endpoint exports**

Dans `v1`, l'endpoint `/exports/` retournait **tous les exports de l'utilisateur authentifié** pour tous les projets.

Dans `v2`, pour des raisons de performance, les exports sont désormais **limités par projet** et doivent être accessibles via `/api/v2/assets/{asset_uid}/exports/`.

**Exception pour l'endpoint submissions**

L'endpoint `/assets/{asset_uid}/submissions/` a été **renommé** dans `v2`. En plus de mettre à jour le chemin de base, vous devez également changer le nom de l'endpoint de `submissions` en `data` :

| Endpoint `v1`                               | Équivalent `v2`                                     |
|---------------------------------------------|-----------------------------------------------------|
| `/assets/{asset_uid}/submissions/`          | `/api/v2/assets/{asset_uid}/data/`                  |
| `/assets/{asset_uid}/submissions/{id}/`     | `/api/v2/assets/{asset_uid}/data/{id}/`<sup>1</sup> |

<sup>1</sup> `{id}` peut être soit l'identifiant entier de la soumission, soit son `root_uuid`.



## Migration de KoboCAT v1 vers KPI v2
La section suivante liste les principaux endpoints de l'API KoboCAT `v1` et fournit leurs équivalents `v2`.

### Endpoints de données : liste des projets
Cet endpoint retourne la liste des formulaires auxquels vous avez accès, avec des liens vers leurs données de soumission, servant de point d'entrée pour accéder aux réponses ou les télécharger.

**Correspondance des endpoints de `v1` à `v2`**

| Endpoint `v1`    | Équivalent `v2`        |
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

<sup>1</sup> _Dans l'endpoint `/api/v2/assets`, les identifiants entiers séquentiels ne sont plus utilisés. Chaque entrée est identifiée de manière unique par un `uid` alphanumérique._


**Exemples de code**

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (déprécié)
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/data"

# v2
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/?asset_type=survey"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
headers = {"Authorization": f"Token {TOKEN}"}

# v1 (déprécié)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/data", headers=headers)

# v2
response = requests.get(
    "https://kf.kobotoolbox.org/api/v2/assets/",
    params={"asset_type": "survey"},
    headers=headers
)
response.raise_for_status()
projects = response.json()["results"]

for project in projects:
    print(project["uid"], project["name"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)
library(jsonlite)

TOKEN <- "xxxx"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (déprécié)
# response <- GET("https://kc.kobotoolbox.org/api/v1/data", headers)

# v2
response <- GET(
  "https://kf.kobotoolbox.org/api/v2/assets/",
  query = list(asset_type = "survey"),
  headers
)
projects <- content(response, as = "parsed")$results

for (p in projects) {
  cat(p$uid, p$name, "\n")
}
```
</details>

**Exemples de réponses**

<details>
<summary><strong>Réponse v1</strong></summary>

```json
{
  "id": 474,
  "id_string": "a4etXeWtqcoodSxLV8a6Uq",
  "title": "Pathways Initiative",
  "description": "Pathways Initiative",
  "url": "https://kc.kobotoolbox.org/api/v1/data/474.json"
}
```
</details>

<details>
<summary><strong>Équivalent v2</strong></summary>

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
</details>

---

### Endpoints de données : données de soumission
Ces endpoints récupèrent toutes les données de soumission d'un projet spécifique ou une soumission unique du projet. `{uid}` est l'identifiant unique du projet et `{submission_id}` est l'identifiant unique d'une soumission de formulaire.

| Endpoint `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

En vous basant sur l'`url` obtenue depuis la propriété `data` de l'endpoint asset, vous pouvez récupérer les données de soumission dans `v2` de la manière suivante.

<p class="note">
  <strong>Note :</strong> La structure de la réponse est quasiment identique, <strong>sauf que <code>v2</code> introduit la pagination</strong>. Si vous avez plus de 1 000 soumissions, vous devrez suivre l'URL <code>next</code> pour récupérer les pages suivantes.
</p>

**Exemples de code**

Remplacez `a4etXeWtqcoodSxLV8a6Uq` par le `uid` de votre projet (voir l'[endpoint de liste des projets](#data-endpoints-project-list) ci-dessus).

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (déprécié) — utilisait l'identifiant entier du formulaire
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/data/474"

# v2 — utilise l'uid alphanumérique
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/data/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
ASSET_UID = "a4etXeWtqcoodSxLV8a6Uq"
headers = {"Authorization": f"Token {TOKEN}"}

# v1 (déprécié)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/data/474", headers=headers)
# submissions = response.json()  # retournait une liste plate

# v2 — les résultats sont paginés
url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data/"
all_submissions = []

while url:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    page = response.json()
    all_submissions.extend(page["results"])
    url = page["next"]  # None quand il n'y a plus de pages

print(f"Total soumissions : {len(all_submissions)}")
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)
library(jsonlite)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (déprécié)
# response <- GET(paste0("https://kc.kobotoolbox.org/api/v1/data/474"), headers)
# submissions <- content(response, as = "parsed")  # liste plate

# v2 — gestion de la pagination
url <- paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/data/")
all_submissions <- list()

repeat {
  response <- GET(url, headers)
  page <- content(response, as = "parsed")
  all_submissions <- c(all_submissions, page$results)
  if (is.null(page$`next`)) break
  url <- page$`next`
}

cat("Total soumissions :", length(all_submissions), "\n")
```
</details>

**Exemples de réponses**

<details>
<summary><strong>Réponse v1</strong></summary>

```json
[
  {
    "_id": 49542,
    ...
  }
]
```
</details>

<details>
<summary><strong>Équivalent v2</strong></summary>

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


### Endpoints de formulaires
Ces endpoints retournent les attributs détaillés de tous les formulaires partagés avec vous ou d'un formulaire spécifique, où `{uid}` est l'identifiant unique du projet.

**Correspondance des endpoints**

| Endpoint `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/forms`   | `/api/v2/assets/?asset_type=survey` |
| `/api/v1/forms/<pk>`       | `/api/v2/assets/{asset_uid}/`                 |


<p class="note">
  <strong>Note :</strong> L'endpoint <code>v2</code> suit la même structure pour chaque élément que celle décrite ci-dessous, mais introduit la pagination. Certaines propriétés de l'endpoint <code>v1</code> ne sont pas directement disponibles sur l'endpoint asset <code>v2</code>, mais elles restent accessibles d'une autre manière (voir la légende sous le tableau pour plus de détails).
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

<sup>1</sup> _Dans l'endpoint `/api/v2/assets`, les identifiants entiers séquentiels ne sont plus utilisés. Chaque entrée est identifiée de manière unique par un `uid` alphanumérique._
<sup>2</sup> _Dans `v1`, les tags étaient retournés sous forme de tableau ; dans `v2`, ils sont retournés sous forme de chaîne séparée par des virgules._
<sup>3</sup> _Ces champs ne sont plus exposés. Consultez la section **Permissions** ci-dessous pour plus de détails._
<sup>4</sup> _Non directement accessible via l'endpoint asset. Utilisez l'endpoint `/api/v2/asset_usage/` et récupérez le champ `storage_bytes` du projet correspondant._

**Exemples de code**

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (déprécié) — lister tous les formulaires
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms"

# v1 (déprécié) — formulaire unique par identifiant entier
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms/474"

# v2 — lister tous les formulaires (paginé)
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/?asset_type=survey"

# v2 — formulaire unique par uid
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
ASSET_UID = "a4etXeWtqcoodSxLV8a6Uq"
headers = {"Authorization": f"Token {TOKEN}"}

# v1 (déprécié)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/forms/474", headers=headers)
# form = response.json()

# v2 — formulaire unique
response = requests.get(
    f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/",
    headers=headers
)
response.raise_for_status()
form = response.json()

print(form["name"])                          # était : form["title"]
print(form["deployment__submission_count"])  # était : form["num_of_submissions"]
print(form["tag_string"])                    # était : ", ".join(form["tags"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (déprécié)
# response <- GET("https://kc.kobotoolbox.org/api/v1/forms/474", headers)
# form <- content(response, as = "parsed")

# v2 — formulaire unique
response <- GET(
  paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/"),
  headers
)
form <- content(response, as = "parsed")

cat(form$name)                           # était : form$title
cat(form$deployment__submission_count)   # était : form$num_of_submissions
cat(form$tag_string)                     # était : paste(form$tags, collapse = ", ")
```
</details>

**Exemples de réponses**

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
<summary><strong>Réponse <code>v2</code> équivalente</strong></summary>
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
**Tags**

Les tags dans `v1` et `v2` ne partagent pas la même base de données sous-jacente. Par conséquent, les tags de `v1` **ne seront pas automatiquement migrés** vers `v2`. Si vous souhaitez les conserver, vous devez les réappliquer manuellement via une requête `PATCH` vers `/api/v2/assets/{uid}/`.

Exemple de payload :
```json
{ "tag_string": "tag1,tag2,tag3" }
```

**Exemples de code**

<details>
<summary><strong>curl</strong></summary>

```bash
curl -X PATCH \
  -H "Authorization: Token xxxx" \
  -H "Content-Type: application/json" \
  -d '{"tag_string": "tag1,tag2,tag3"}' \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
ASSET_UID = "a4etXeWtqcoodSxLV8a6Uq"
headers = {"Authorization": f"Token {TOKEN}"}

tags = ["tag1", "tag2", "tag3"]

response = requests.patch(
    f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/",
    headers=headers,
    json={"tag_string": ",".join(tags)}
)
response.raise_for_status()
print("Tags mis à jour :", response.json()["tag_string"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)
library(jsonlite)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
headers <- add_headers(Authorization = paste("Token", TOKEN))

tags <- c("tag1", "tag2", "tag3")

response <- PATCH(
  paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/"),
  headers,
  body = toJSON(list(tag_string = paste(tags, collapse = ",")), auto_unbox = TRUE),
  content_type_json()
)
result <- content(response, as = "parsed")
cat("Tags mis à jour :", result$tag_string, "\n")
```
</details>

**Permissions**

Dans `v2`, les champs `public`, `public_data` et `require_auth` ne sont plus exposés en tant qu'attributs booléens. À la place, **l'accès anonyme est contrôlé via des attributions de permissions explicites à l'`AnonymousUser`**.

Les correspondances suivantes s'appliquent :
- `public: true` → l'`AnonymousUser` dispose de la permission `view_asset`
- `public_data: true` → l'`AnonymousUser` dispose de la permission `view_submissions`
- `require_auth: false` → l'`AnonymousUser` dispose de la permission `add_submissions`

Les permissions sont disponibles sur l'endpoint de détail de l'asset (`/api/v2/assets/{uid}/`) sous la propriété `permissions`.

**Exemples de code**

**Lecture des permissions**

<details>
<summary><strong>curl</strong></summary>

```bash
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
ASSET_UID = "a4etXeWtqcoodSxLV8a6Uq"
BASE_URL = "https://kf.kobotoolbox.org"
headers = {"Authorization": f"Token {TOKEN}"}

response = requests.get(f"{BASE_URL}/api/v2/assets/{ASSET_UID}/", headers=headers)
response.raise_for_status()
permissions = response.json()["permissions"]

# Vérifier quelles permissions sont attribuées à AnonymousUser
# (équivalent des champs v1 public/public_data/require_auth)
anon_permissions = [
    p["permission"].split("/")[-2]  # extraire le nom de la permission depuis l'URL
    for p in permissions
    if p["user"].endswith("/AnonymousUser/")
]
print("Permissions de l'utilisateur anonyme :", anon_permissions)
# ex. ['view_asset', 'view_submissions']
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
BASE_URL <- "https://kf.kobotoolbox.org"
headers <- add_headers(Authorization = paste("Token", TOKEN))

response <- GET(paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/"), headers)
permissions <- content(response, as = "parsed")$permissions

# Vérifier quelles permissions sont attribuées à AnonymousUser
anon_permissions <- Filter(
  function(p) grepl("AnonymousUser", p$user),
  permissions
)
for (p in anon_permissions) cat(p$label, "\n")
```
</details>

**Attribution de permissions à AnonymousUser**

Pour reproduire un paramètre `public: true` de v1, envoyez une requête POST d'attribution de permission vers l'endpoint `permission-assignments`.

<details>
<summary><strong>curl</strong></summary>

```bash
# Accorder à AnonymousUser view_asset (équivalent de v1 public: true)
curl -X POST \
  -H "Authorization: Token xxxx" \
  -H "Content-Type: application/json" \
  -d '{"user": "https://kf.kobotoolbox.org/api/v2/users/AnonymousUser/", "permission": "https://kf.kobotoolbox.org/api/v2/permissions/view_asset/"}' \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/permission-assignments/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
ASSET_UID = "a4etXeWtqcoodSxLV8a6Uq"
BASE_URL = "https://kf.kobotoolbox.org"
headers = {"Authorization": f"Token {TOKEN}"}

# Accorder à AnonymousUser view_asset (équivalent de v1 public: true)
response = requests.post(
    f"{BASE_URL}/api/v2/assets/{ASSET_UID}/permission-assignments/",
    headers=headers,
    json={
        "user": f"{BASE_URL}/api/v2/users/AnonymousUser/",
        "permission": f"{BASE_URL}/api/v2/permissions/view_asset/",
    }
)
response.raise_for_status()
print("Permission attribuée :", response.json()["label"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)
library(jsonlite)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
BASE_URL <- "https://kf.kobotoolbox.org"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# Accorder à AnonymousUser view_asset (équivalent de v1 public: true)
response <- POST(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/permission-assignments/"),
  headers,
  body = toJSON(list(
    user       = paste0(BASE_URL, "/api/v2/users/AnonymousUser/"),
    permission = paste0(BASE_URL, "/api/v2/permissions/view_asset/")
  ), auto_unbox = TRUE),
  content_type_json()
)
result <- content(response, as = "parsed")
cat("Permission attribuée :", result$label, "\n")
```
</details>

**Exemples de réponses**

<details>
<summary><strong>Exemple : permissions de l'utilisateur anonyme dans <code>v2</code></strong></summary>
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

### Endpoint label
L'endpoint `/api/v1/forms/<pk>/labels` de `v1` retourne un dictionnaire associant chaque nom de champ du formulaire à son libellé correspondant, permettant un affichage plus facile à utiliser des données du formulaire.

Cet endpoint n'a pas été porté vers `v2`, mais il est toujours possible d'**étiqueter** ou de **taguer** un projet, comme décrit [ci-dessus](#tags).

---

### Endpoints de métadonnées
Ces endpoints retournent une liste plate de tous les fichiers média associés à l'utilisateur actuel, pour tous les projets déployés ou un projet spécifique. Dans `v2`, les fichiers média sont désormais limités par projet. Comme pour les autres endpoints, `v2` introduit la pagination, tandis que `v1` retourne tous les résultats en une seule réponse.

**Correspondance des endpoints**

| Endpoint `v1`    | Équivalent `v2`        |
| ------------- | ---------------------- |
| `/api/v1/metadata`   | `/api/v2/assets/{asset_uid}/files/` |
| `/api/v1/metadata/<pk>`       | `/api/v2/assets/{asset_uid}/files/{file_uid}/`                 |


<p class="note">
  <strong>Note :</strong> <code>v2</code> ne gère que les fichiers média : <code>media</code> de <code>v1</code> correspond à <code>form_media</code> dans <code>v2</code>. <strong>Les autres types de métadonnées</strong> de <code>v1</code> (par exemple <code>doc</code>, <code>mapbox_layer</code>, <code>source</code>, etc.) n'ont pas été portés vers <code>v2</code>.
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

<sup>1</sup> _Dans `v2`, le projet associé est accessible via le champ `asset`, qui contient une URL complète plutôt qu'un identifiant entier._

**Exemples de code**

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (déprécié) — lister tous les fichiers média pour tous les projets
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata"

# v1 (déprécié) — fichier unique par identifiant entier
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata/271"

# v2 — lister les fichiers média d'un projet spécifique
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/"

# v2 — fichier unique par uid
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/afoeCcF3AcGNpWUoM6bvKj9/"

# v2 — importer un nouveau fichier média
curl -X POST \
  -H "Authorization: Token xxxx" \
  -F "file_type=form_media" \
  -F "content=@/path/to/goose.jpg" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
ASSET_UID = "a4etXeWtqcoodSxLV8a6Uq"
BASE_URL = "https://kf.kobotoolbox.org"
headers = {"Authorization": f"Token {TOKEN}"}

# v1 (déprécié)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/metadata", headers=headers)
# files = response.json()  # liste plate pour tous les projets

# v2 — lister les fichiers média d'un projet spécifique (paginé)
response = requests.get(
    f"{BASE_URL}/api/v2/assets/{ASSET_UID}/files/",
    headers=headers
)
response.raise_for_status()
files = response.json()["results"]

for f in files:
    print(f["uid"], f["metadata"]["filename"])  # était : f["id"], f["data_filename"]

# v2 — importer un nouveau fichier média
with open("/path/to/goose.jpg", "rb") as fh:
    upload = requests.post(
        f"{BASE_URL}/api/v2/assets/{ASSET_UID}/files/",
        headers=headers,
        data={"file_type": "form_media"},
        files={"content": fh}
    )
upload.raise_for_status()
print("Importé :", upload.json()["metadata"]["filename"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
BASE_URL <- "https://kf.kobotoolbox.org"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (déprécié)
# response <- GET("https://kc.kobotoolbox.org/api/v1/metadata", headers)
# files <- content(response, as = "parsed")  # liste plate pour tous les projets

# v2 — lister les fichiers média d'un projet spécifique
response <- GET(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/files/"),
  headers
)
files <- content(response, as = "parsed")$results

for (f in files) {
  cat(f$uid, f$metadata$filename, "\n")  # était : f$id, f$data_filename
}

# v2 — importer un nouveau fichier média
upload <- POST(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/files/"),
  headers,
  body = list(
    file_type = "form_media",
    content   = upload_file("/path/to/goose.jpg")
  )
)
cat("Importé :", content(upload, as = "parsed")$metadata$filename, "\n")
```
</details>

**Exemples de réponses**

<details>
<summary><strong>Réponse v1</strong></summary>

```json
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
</details>

<details>
<summary><strong>Équivalent v2</strong></summary>

```json
{
  "uid": "afoeCcF3AcGNpWUoM6bvKj9",
  "asset": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/",
  "file_type": "form_media",
  "content": "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/afoeCcF3AcGNpWUoM6bvKj9/content/",
  "metadata": {
    "hash": "md5:93fb96bced1e3b392abfc22934afe51a",
    "filename": "goose.jpg",
    "mimetype": "image/jpeg"
  }
}
```
</details>

---

### Endpoints utilisateur
Cet endpoint retourne les informations de profil de l'utilisateur authentifié, notamment l'identité du compte et les détails associés.

**Correspondance des endpoints**

| Endpoint `v1`    | Équivalent `v2`        |
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

**Exemples de code**

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (déprécié)
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/user"

# v2
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/me/"
```
</details>

<details>
<summary><strong>Python</strong></summary>

```python
import requests

TOKEN = "xxxx"
BASE_URL = "https://kf.kobotoolbox.org"
headers = {"Authorization": f"Token {TOKEN}"}

# v1 (déprécié)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/user", headers=headers)
# user = response.json()
# print(user["username"], user["email"])

# v2
response = requests.get(f"{BASE_URL}/me/", headers=headers)
response.raise_for_status()
user = response.json()

print(user["username"])                        # identique à v1
print(user["email"])                           # identique à v1
print(user["extra_details"]["organization"])   # était : user["organization"]
print(user["extra_details"]["country"])        # était : user["country"]
print(user["extra_details__uid"])              # était : user["id"]
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
BASE_URL <- "https://kf.kobotoolbox.org"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (déprécié)
# response <- GET("https://kc.kobotoolbox.org/api/v1/user", headers)
# user <- content(response, as = "parsed")

# v2
response <- GET(paste0(BASE_URL, "/me/"), headers)
user <- content(response, as = "parsed")

cat(user$username, "\n")                         # identique à v1
cat(user$email, "\n")                            # identique à v1
cat(user$extra_details$organization, "\n")       # était : user$organization
cat(user$extra_details$country, "\n")            # était : user$country
cat(user$extra_details__uid, "\n")               # était : user$id
```
</details>

**Exemples de réponses**

<details>
<summary><strong>Réponse v1</strong></summary>

```json
{
  "id": 42,
  "username": "project_owner",
  "email": "owner@example.org",
  "city": "Nairobi",
  "country": "KEN",
  "organization": "Humanitarian Org",
  "website": "https://example.org",
  "twitter": "project_owner",
  "gravatar": "https://www.gravatar.com/avatar/abc123?s=40",
  "require_auth": true,
  "api_token": "e291a91bf3dd94b45748f6865cd4710246219347"
}
```
</details>

<details>
<summary><strong>Équivalent v2</strong></summary>

```json
{
  "username": "project_owner",
  "email": "owner@example.org",
  "gravatar": "https://www.gravatar.com/avatar/abc123?s=40",
  "extra_details": {
    "city": "Nairobi",
    "country": "KEN",
    "organization": "Humanitarian Org",
    "website": "https://example.org",
    "twitter": "project_owner",
    "require_auth": true
  },
  "extra_details__uid": "u9rb4EUVEgC22wbHfVfr7S"
}
```
</details>