# Migrating from v1 to v2 API
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/62f9bf5497b6f6a7e0d1ff3f2e5d1da7bad99168/source/migrating_api.md" class="reference">19 May 2026</a>


As part of our ongoing efforts to streamline and modernize the KoboToolbox platform, we are phasing out KPI and KoboCAT `v1` endpoints. All KPI and KoboCAT `v1` endpoints are now deprecated, and will be removed entirely in June 2026. `v1` endpoints are being phased out in favor of the more robust and fully supported KPI `v2` API. 

This article explains how to migrate your API integrations from the `v1` API (KoboCAT and KPI) to the KPI `v2` API. It covers each deprecated `v1` endpoint and its `v2` equivalent to help you transition your workflows.


## Authentication

All API requests — v1 and v2 — require an API token. Include it in every request using the `Authorization` header:

```
Authorization: Token xxxx
```

Replace `xxxx` with your actual token. You can find your token at `https://kf.kobotoolbox.org/token/` (or your server's equivalent).

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
  <b>Note:</b> The authentication header is the same across all API versions. What changes depends on which migration path you are on: if you are migrating from <strong>KPI v1 to KPI v2</strong>, you only need to update the URL path. If you are migrating from <strong>KoboCAT v1 to KPI v2</strong>, you will also need to update the base domain (<code>kc.kobotoolbox.org</code> → <code>kf.kobotoolbox.org</code>), the endpoint paths, and adapt your code to handle the new response structure and field names — see the sections below.
</p>


## Migrating from KPI v1 to KPI v2
Migrating from the old KPI API (`v1`) to the new version (`v2`) is straightforward in most cases.  

In general, you only need to update the base path from `/endpoint/` to `/api/v2/endpoint/`.

### Exception for exports endpoint
The only exception to the rule above is for the `/exports/` endpoint. In `v1`, the `/exports/` endpoint returned **all exports for the authenticated user** across all projects.

In `v2`, for performance reasons, exports are now **scoped per project** and must be accessed via `/api/v2/assets/{asset_uid}/exports/`. 



## Migrating from KoboCAT v1 to KPI v2 
The following section lists the main endpoints from the KoboCAT `v1` API and provides their `v2` equivalents.

### Data endpoints: Project list
This endpoint returns a list of forms you have access to, with links to their submission data, serving as an entry point for accessing or downloading responses.

**Endpoint mapping from `v1` to `v2`**

| `v1` Endpoint    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `/api/v1/data`          | `/api/v2/assets/?asset_type=survey`  |


**Field mapping from `v1` to `v2`**

| `v1` Field    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `id`          | `uid`<sup>1</sup>      |
| `id_string`   | `uid`                  |
| `title`       | `name`                 |
| `description` | `settings.description` |
| `url`         | `data`                 |

<sup>1</sup> _In the `/api/v2/assets` endpoint, sequential integer identifiers are no longer used. Each entry is uniquely identified by an alphanumeric `uid`_


#### Code examples

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (deprecated)
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

# v1 (deprecated)
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

# v1 (deprecated)
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

#### Response examples

<details>
<summary><strong>v1 response</strong></summary>

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
<summary><strong>v2 equivalent</strong></summary>

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

### Data endpoints: Submission data
These endpoints retrieve all submission data for a specific project or a single submission from the project. `{uid}` is the unique identifier of the project and `{submission_id}` is the unique identifier of a form submission.

| `v1` Endpoint    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

Based on the `url` you get from the `data` property in the asset endpoint, you can fetch the submission data in `v2` using. 

<p class="note">
  <b>Note:</b> The response structure is nearly the same, <strong>except that <code>v2</code> introduces pagination</strong>. If you have more than 30,000 submissions, you will need to follow the <code>next</code> URL to retrieve subsequent pages.
</p>

#### Code examples

Replace `a4etXeWtqcoodSxLV8a6Uq` with your project's `uid` (see [project list endpoint](#data-endpoints-project-list) above).

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (deprecated) — used the integer form ID
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/data/474"

# v2 — use the alphanumeric uid
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

# v1 (deprecated)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/data/474", headers=headers)
# submissions = response.json()  # returned a flat list

# v2 — results are paginated
url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data/"
all_submissions = []

while url:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    page = response.json()
    all_submissions.extend(page["results"])
    url = page["next"]  # None when there are no more pages

print(f"Total submissions: {len(all_submissions)}")
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

# v1 (deprecated)
# response <- GET(paste0("https://kc.kobotoolbox.org/api/v1/data/474"), headers)
# submissions <- content(response, as = "parsed")  # flat list

# v2 — handle pagination
url <- paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/data/")
all_submissions <- list()

repeat {
  response <- GET(url, headers)
  page <- content(response, as = "parsed")
  all_submissions <- c(all_submissions, page$results)
  if (is.null(page$`next`)) break
  url <- page$`next`
}

cat("Total submissions:", length(all_submissions), "\n")
```
</details>

#### Response examples

<details>
<summary><strong>v1 response</strong></summary>

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
<summary><strong>v2 equivalent</strong></summary>

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


### Form endpoints
These endpoints return detailed attributes of all forms shared with you or about a specific form, where `{uid}` is the unique identifier of the project. 

**Endpoint mapping**

| `v1` Endpoint    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `/api/v1/forms`   | `/api/v2/assets/?asset_type=survey` |
| `/api/v1/forms/<pk>`       | `/api/v2/assets/{asset_uid}/`                 |


<p class="note">
  <b>Note:</b> The <code>v2</code> endpoint follows the same structure for each item as listed below, but introduces pagination. Some properties from the <code>v1</code> endpoint are not directly available on the <code>v2</code> asset endpoint, but they can still be accessed differently (see the legend below the table for more details).
</p>


**Field mapping**

| `v1` Field                 | `v2` Equivalent                          |
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

<sup>1</sup> _In the `/api/v2/assets` endpoint, sequential integer identifiers are no longer used. Each entry is uniquely identified by an alphanumeric `uid`_.  
<sup>2</sup> _In `v1`, tags were returned as an array; in `v2`, they are returned as a comma-separated string._  
<sup>3</sup> _These fields are no longer exposed. See the **Permissions** section below for more details._  
<sup>4</sup> _Not directly accessible via the asset endpoint. Use the `/api/v2/asset_usage/` endpoint and retrieve the `storage_bytes` field of the corresponding project._

#### Code examples

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (deprecated) — list all forms
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms"

# v1 (deprecated) — single form by integer ID
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms/474"

# v2 — list all forms (paginated)
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/?asset_type=survey"

# v2 — single form by uid
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

# v1 (deprecated)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/forms/474", headers=headers)
# form = response.json()

# v2 — single form
response = requests.get(
    f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/",
    headers=headers
)
response.raise_for_status()
form = response.json()

print(form["name"])                          # was: form["title"]
print(form["deployment__submission_count"])  # was: form["num_of_submissions"]
print(form["tag_string"])                    # was: ", ".join(form["tags"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (deprecated)
# response <- GET("https://kc.kobotoolbox.org/api/v1/forms/474", headers)
# form <- content(response, as = "parsed")

# v2 — single form
response <- GET(
  paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/"),
  headers
)
form <- content(response, as = "parsed")

cat(form$name)                           # was: form$title
cat(form$deployment__submission_count)   # was: form$num_of_submissions
cat(form$tag_string)                     # was: paste(form$tags, collapse = ", ")
```
</details>

#### Response examples

<details>
<summary><strong>Example <code>v1</code> response</strong></summary>
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
<summary><strong>Equivalent <code>v2</code> response</strong></summary>
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

Tags in `v1` and `v2` do not share the same underlying database. As a result, tags from `v1` **will not be automatically migrated** to `v2`. If you need to preserve them, you must reapply the tags manually using a `PATCH` request to `/api/v2/assets/{uid}/`.

Example payload:
```json
{ "tag_string": "tag1,tag2,tag3" }
```

#### Code examples

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
print("Tags updated:", response.json()["tag_string"])
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
cat("Tags updated:", result$tag_string, "\n")
```
</details>

**Permissions**

In `v2`, the fields `public`, `public_data`, and `require_auth` are no longer exposed as boolean attributes. Instead, **anonymous access is controlled via explicit permission assignments to the `AnonymousUser`**.

The following mappings apply:
- `public: true` → the `AnonymousUser` has the `view_asset` permission  
- `public_data: true` → the `AnonymousUser` has the `view_submissions` permission  
- `require_auth: false` → the `AnonymousUser` has the `add_submissions` permission  

Permissions are available on the asset detail endpoint (`/api/v2/assets/{uid}/`) under the `permissions` property.

#### Code examples

**Reading permissions**

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

# Check which permissions are assigned to AnonymousUser
# (equivalent of v1 public/public_data/require_auth fields)
anon_permissions = [
    p["permission"].split("/")[-2]  # extract permission codename from URL
    for p in permissions
    if p["user"].endswith("/AnonymousUser/")
]
print("Anonymous user permissions:", anon_permissions)
# e.g. ['view_asset', 'view_submissions']
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

# Check which permissions are assigned to AnonymousUser
anon_permissions <- Filter(
  function(p) grepl("AnonymousUser", p$user),
  permissions
)
for (p in anon_permissions) cat(p$label, "\n")
```
</details>

**Assigning permissions to AnonymousUser**

To replicate a v1 `public: true` setting, POST a new permission assignment to the `permission-assignments` endpoint.

<details>
<summary><strong>curl</strong></summary>

```bash
# Grant AnonymousUser view_asset (equivalent of v1 public: true)
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

# Grant AnonymousUser view_asset (equivalent of v1 public: true)
response = requests.post(
    f"{BASE_URL}/api/v2/assets/{ASSET_UID}/permission-assignments/",
    headers=headers,
    json={
        "user": f"{BASE_URL}/api/v2/users/AnonymousUser/",
        "permission": f"{BASE_URL}/api/v2/permissions/view_asset/",
    }
)
response.raise_for_status()
print("Permission assigned:", response.json()["label"])
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

# Grant AnonymousUser view_asset (equivalent of v1 public: true)
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
cat("Permission assigned:", result$label, "\n")
```
</details>

#### Response examples

<details>
<summary><strong>Example: <code>v2</code> anonymous user permissions</strong></summary>
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

### Label endpoint
The `/api/v1/forms/<pk>/labels` endpoint from `v1` returns a dictionary mapping each field name in the form to its corresponding label, enabling more user-friendly display of form data.

This endpoint has not been ported to `v2`, but it is still possible to **label** or **tag** a project, as described [above](#tags).

---

### Metadata endpoints
These endpoints return a flat list of all media files associated with the current user, across all deployed projects or a specific project. In `v2`, media files are now scoped per project. As with other endpoints, `v2` introduces pagination, whereas `v1` returns all results in a single response.

**Endpoint mapping**

| `v1` Endpoint    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `/api/v1/metadata`   | `/api/v2/assets/{asset_uid}/files/` |
| `/api/v1/metadata/<pk>`       | `/api/v2/assets/{asset_uid}/files/{file_uid}/`                 |


<p class="note">
  <b>Note:</b> <code>v2</code> only supports media files: <code>media</code> from <code>v1</code> is mapped to <code>form_media</code> in <code>v2</code>. <strong>Other metadata types</strong> from <code>v1</code> (e.g., <code>doc</code>, <code>mapbox_layer</code>, <code>source</code> etc.) have not been ported to <code>v2</code>.
</p>


**Field mapping**

| `v1` Field        | `v2` Equivalent                        |
|-------------------|----------------------------------------|
| `id`              | `uid`                                  |
| `data_type`       | `file_type`                            |
| `xform`           | _N/A_<sup>1</sup>                      |
| `data_value`      | `metadata.filename` or `metadata.redirect_url` |
| `data_filename`   | `metadata.filename`                    |
| `data_file`       | `content`                              |
| `data_file_type`  | `metadata.mimetype`                    |
| `file_hash`       | `metadata.hash`                        |
| `from_kpi`        | _N/A_                                  |

<sup>1</sup> _In `v2`, the related project is accessible via the `asset` field, which contains a full URL instead of an integer ID._

#### Code examples

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (deprecated) — list all media files across all projects
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata"

# v1 (deprecated) — single file by integer ID
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata/271"

# v2 — list media files for a specific project
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/"

# v2 — single file by uid
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/afoeCcF3AcGNpWUoM6bvKj9/"

# v2 — upload a new media file
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

# v1 (deprecated)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/metadata", headers=headers)
# files = response.json()  # flat list across all projects

# v2 — list media files for a specific project (paginated)
response = requests.get(
    f"{BASE_URL}/api/v2/assets/{ASSET_UID}/files/",
    headers=headers
)
response.raise_for_status()
files = response.json()["results"]

for f in files:
    print(f["uid"], f["metadata"]["filename"])  # was: f["id"], f["data_filename"]

# v2 — upload a new media file
with open("/path/to/goose.jpg", "rb") as fh:
    upload = requests.post(
        f"{BASE_URL}/api/v2/assets/{ASSET_UID}/files/",
        headers=headers,
        data={"file_type": "form_media"},
        files={"content": fh}
    )
upload.raise_for_status()
print("Uploaded:", upload.json()["metadata"]["filename"])
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

# v1 (deprecated)
# response <- GET("https://kc.kobotoolbox.org/api/v1/metadata", headers)
# files <- content(response, as = "parsed")  # flat list across all projects

# v2 — list media files for a specific project
response <- GET(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/files/"),
  headers
)
files <- content(response, as = "parsed")$results

for (f in files) {
  cat(f$uid, f$metadata$filename, "\n")  # was: f$id, f$data_filename
}

# v2 — upload a new media file
upload <- POST(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/files/"),
  headers,
  body = list(
    file_type = "form_media",
    content   = upload_file("/path/to/goose.jpg")
  )
)
cat("Uploaded:", content(upload, as = "parsed")$metadata$filename, "\n")
```
</details>

#### Response examples

<details>
<summary><strong>v1 response</strong></summary>

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
<summary><strong>v2 equivalent</strong></summary>

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

### User endpoints
This endpoint returns profile information about the authenticated user, including account identity and associated details.

**Endpoint mapping**

| `v1` Endpoint    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `/api/v1/user`   | `/me/` |


**Field mapping**

| `v1` Field        | `v2` Equivalent                        |
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


<sup>1</sup> _Not ported to `v2`_

<sup>2</sup> _Use https://kf.domain.tld/token instead_

#### Code examples

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (deprecated)
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

# v1 (deprecated)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/user", headers=headers)
# user = response.json()
# print(user["username"], user["email"])

# v2
response = requests.get(f"{BASE_URL}/me/", headers=headers)
response.raise_for_status()
user = response.json()

print(user["username"])                        # same as v1
print(user["email"])                           # same as v1
print(user["extra_details"]["organization"])   # was: user["organization"]
print(user["extra_details"]["country"])        # was: user["country"]
print(user["extra_details__uid"])              # was: user["id"]
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
BASE_URL <- "https://kf.kobotoolbox.org"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (deprecated)
# response <- GET("https://kc.kobotoolbox.org/api/v1/user", headers)
# user <- content(response, as = "parsed")

# v2
response <- GET(paste0(BASE_URL, "/me/"), headers)
user <- content(response, as = "parsed")

cat(user$username, "\n")                         # same as v1
cat(user$email, "\n")                            # same as v1
cat(user$extra_details$organization, "\n")       # was: user$organization
cat(user$extra_details$country, "\n")            # was: user$country
cat(user$extra_details__uid, "\n")               # was: user$id
```
</details>

#### Response examples

<details>
<summary><strong>v1 response</strong></summary>

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
<summary><strong>v2 equivalent</strong></summary>

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





