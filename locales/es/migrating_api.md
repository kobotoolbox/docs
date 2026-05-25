# Migración de la API v1 a v2
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/e9270720e3600bf065cd670e73664ec246c45976/source/migrating_api.md" class="reference">19 may 2026</a>

Como parte de nuestros esfuerzos continuos para optimizar y modernizar la plataforma KoboToolbox, estamos eliminando gradualmente los endpoints `v1` de KPI y KoboCAT. Todos los endpoints `v1` de KPI y KoboCAT están ahora obsoletos y se eliminarán por completo en junio de 2026. Los endpoints `v1` están siendo reemplazados por la API KPI `v2`, que es más robusta y cuenta con soporte completo.

Este artículo explica cómo migrar tus integraciones de API desde la API `v1` (KoboCAT y KPI) a la API KPI `v2`. Cubre cada endpoint `v1` obsoleto y su equivalente en `v2` para ayudarte a realizar la transición de tus flujos de trabajo.


## Autenticación

Todas las solicitudes a la API — v1 y v2 — requieren un token de API. Inclúyelo en cada solicitud mediante el encabezado `Authorization`:

```
Authorization: Token xxxx
```

Reemplaza `xxxx` con tu token real. Puedes encontrar tu token en `https://kf.kobotoolbox.org/token/` (o el equivalente de tu servidor).

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
  <b>Nota:</b> El encabezado de autenticación es el mismo en todas las versiones de la API. Lo que cambia depende de tu ruta de migración: si estás migrando de <strong>KPI v1 a KPI v2</strong>, solo necesitas actualizar la ruta URL. Si estás migrando de <strong>KoboCAT v1 a KPI v2</strong>, también deberás actualizar el dominio base (<code>kc.kobotoolbox.org</code> → <code>kf.kobotoolbox.org</code>), las rutas de los endpoints y adaptar tu código para manejar la nueva estructura de respuesta y los nuevos nombres de campos — consulta las secciones a continuación.
</p>


## Migración de KPI v1 a KPI v2
La migración de la API KPI antigua (`v1`) a la nueva versión (`v2`) es sencilla en la mayoría de los casos.

En general, solo necesitas actualizar la ruta base de `/endpoint/` a `/api/v2/endpoint/`.

### Excepciones
Hay dos excepciones a la regla anterior.

#### Excepción para el endpoint de exportaciones
En `v1`, el endpoint `/exports/` devolvía **todas las exportaciones del/de la usuario/a autenticado/a** en todos los proyectos.

En `v2`, por razones de rendimiento, las exportaciones ahora están **limitadas por proyecto** y deben accederse a través de `/api/v2/assets/{asset_uid}/exports/`.

#### Excepción para el endpoint de envíos (submissions)
El endpoint `/assets/{asset_uid}/submissions/` ha sido **renombrado** en `v2`. Además de actualizar la ruta base, también debes cambiar el nombre del endpoint de `submissions` a `data`:

| Endpoint `v1`                               | Equivalente `v2`                               |
|---------------------------------------------|------------------------------------------------|
| `/assets/{asset_uid}/submissions/`          | `/api/v2/assets/{asset_uid}/data/`             |
| `/assets/{asset_uid}/submissions/{id}/`     | `/api/v2/assets/{asset_uid}/data/{id}/`<sup>1</sup> |

<sup>1</sup> `{id}` puede ser el identificador entero del envío o su `root_uuid`.



## Migración de KoboCAT v1 a KPI v2
La siguiente sección enumera los principales endpoints de la API KoboCAT `v1` y proporciona sus equivalentes en `v2`.

### Endpoints de datos: Lista de proyectos
Este endpoint devuelve una lista de formularios a los que tienes acceso, con enlaces a sus datos de envío, sirviendo como punto de entrada para acceder o descargar respuestas.

**Mapeo de endpoints de `v1` a `v2`**

| Endpoint `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data`          | `/api/v2/assets/?asset_type=survey`  |


**Mapeo de campos de `v1` a `v2`**

| Campo `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `id`          | `uid`<sup>1</sup>      |
| `id_string`   | `uid`                  |
| `title`       | `name`                 |
| `description` | `settings.description` |
| `url`         | `data`                 |

<sup>1</sup> _En el endpoint `/api/v2/assets`, ya no se utilizan identificadores enteros secuenciales. Cada entrada se identifica de forma única mediante un `uid` alfanumérico_


#### Ejemplos de código

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (obsoleto)
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

# v1 (obsoleto)
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

# v1 (obsoleto)
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

#### Ejemplos de respuestas

<details>
<summary><strong>Respuesta v1</strong></summary>

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
<summary><strong>Equivalente v2</strong></summary>

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

### Endpoints de datos: Datos de envío
Estos endpoints recuperan todos los datos de envío de un proyecto específico o un único envío del proyecto. `{uid}` es el identificador único del proyecto y `{submission_id}` es el identificador único de un envío de formulario.

| Endpoint `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

Basándote en la `url` que obtienes de la propiedad `data` en el endpoint del asset, puedes obtener los datos de envío en `v2`.

<p class="note">
  <b>Nota:</b> La estructura de respuesta es casi la misma, <strong>excepto que <code>v2</code> introduce paginación</strong>. Si tienes más de 1.000 envíos, deberás seguir la URL <code>next</code> para recuperar las páginas siguientes.
</p>

#### Ejemplos de código

Reemplaza `a4etXeWtqcoodSxLV8a6Uq` con el `uid` de tu proyecto (consulta el [endpoint de lista de proyectos](#endpoints-de-datos-lista-de-proyectos) arriba).

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (obsoleto) — usaba el ID entero del formulario
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/data/474"

# v2 — usa el uid alfanumérico
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

# v1 (obsoleto)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/data/474", headers=headers)
# submissions = response.json()  # devolvía una lista plana

# v2 — resultados paginados
url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data/"
all_submissions = []

while url:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    page = response.json()
    all_submissions.extend(page["results"])
    url = page["next"]  # None cuando no hay más páginas

print(f"Total de envíos: {len(all_submissions)}")
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

# v1 (obsoleto)
# response <- GET(paste0("https://kc.kobotoolbox.org/api/v1/data/474"), headers)
# submissions <- content(response, as = "parsed")  # lista plana

# v2 — manejar paginación
url <- paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/data/")
all_submissions <- list()

repeat {
  response <- GET(url, headers)
  page <- content(response, as = "parsed")
  all_submissions <- c(all_submissions, page$results)
  if (is.null(page$`next`)) break
  url <- page$`next`
}

cat("Total de envíos:", length(all_submissions), "\n")
```
</details>

#### Ejemplos de respuestas

<details>
<summary><strong>Respuesta v1</strong></summary>

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
<summary><strong>Equivalente v2</strong></summary>

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


### Endpoints de formularios
Estos endpoints devuelven atributos detallados de todos los formularios compartidos contigo o sobre un formulario específico, donde `{uid}` es el identificador único del proyecto.

**Mapeo de endpoints**

| Endpoint `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `/api/v1/forms`   | `/api/v2/assets/?asset_type=survey` |
| `/api/v1/forms/<pk>`       | `/api/v2/assets/{asset_uid}/`                 |


<p class="note">
  <b>Nota:</b> El endpoint <code>v2</code> sigue la misma estructura para cada elemento como se enumera a continuación, pero introduce paginación. Algunas propiedades del endpoint <code>v1</code> no están disponibles directamente en el endpoint <code>v2</code> del asset, pero aún se pueden acceder de manera diferente (consulta la leyenda debajo de la tabla para más detalles).
</p>


**Mapeo de campos**

| Campo `v1`                 | Equivalente `v2`                          |
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

<sup>1</sup> _En el endpoint `/api/v2/assets`, ya no se utilizan identificadores enteros secuenciales. Cada entrada se identifica de forma única mediante un `uid` alfanumérico_.
<sup>2</sup> _En `v1`, las etiquetas se devolvían como un array; en `v2`, se devuelven como una cadena separada por comas._
<sup>3</sup> _Estos campos ya no están expuestos. Consulta la sección **Permisos** a continuación para más detalles._
<sup>4</sup> _No es directamente accesible a través del endpoint del asset. Usa el endpoint `/api/v2/asset_usage/` y recupera el campo `storage_bytes` del proyecto correspondiente._

#### Ejemplos de código

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (obsoleto) — listar todos los formularios
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms"

# v1 (obsoleto) — formulario individual por ID entero
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms/474"

# v2 — listar todos los formularios (paginado)
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/?asset_type=survey"

# v2 — formulario individual por uid
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

# v1 (obsoleto)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/forms/474", headers=headers)
# form = response.json()

# v2 — formulario individual
response = requests.get(
    f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/",
    headers=headers
)
response.raise_for_status()
form = response.json()

print(form["name"])                          # era: form["title"]
print(form["deployment__submission_count"])  # era: form["num_of_submissions"]
print(form["tag_string"])                    # era: ", ".join(form["tags"])
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
ASSET_UID <- "a4etXeWtqcoodSxLV8a6Uq"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (obsoleto)
# response <- GET("https://kc.kobotoolbox.org/api/v1/forms/474", headers)
# form <- content(response, as = "parsed")

# v2 — formulario individual
response <- GET(
  paste0("https://kf.kobotoolbox.org/api/v2/assets/", ASSET_UID, "/"),
  headers
)
form <- content(response, as = "parsed")

cat(form$name)                           # era: form$title
cat(form$deployment__submission_count)   # era: form$num_of_submissions
cat(form$tag_string)                     # era: paste(form$tags, collapse = ", ")
```
</details>

#### Ejemplos de respuestas

<details>
<summary><strong>Ejemplo de respuesta <code>v1</code></strong></summary>
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
<summary><strong>Respuesta equivalente <code>v2</code></strong></summary>
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
**Etiquetas**

Las etiquetas en `v1` y `v2` no comparten la misma base de datos subyacente. Como resultado, las etiquetas de `v1` **no se migrarán automáticamente** a `v2`. Si necesitas conservarlas, debes volver a aplicar las etiquetas manualmente usando una solicitud `PATCH` a `/api/v2/assets/{uid}/`.

Ejemplo de payload:
```json
{ "tag_string": "tag1,tag2,tag3" }
```

#### Ejemplos de código

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

**Permisos**

En `v2`, los campos `public`, `public_data` y `require_auth` ya no están expuestos como atributos booleanos. En su lugar, **el acceso anónimo se controla mediante asignaciones de permisos explícitas al `AnonymousUser`**.

Se aplican los siguientes mapeos:
- `public: true` → el `AnonymousUser` tiene el permiso `view_asset`
- `public_data: true` → el `AnonymousUser` tiene el permiso `view_submissions`
- `require_auth: false` → el `AnonymousUser` tiene el permiso `add_submissions`

Los permisos están disponibles en el endpoint de detalle del asset (`/api/v2/assets/{uid}/`) bajo la propiedad `permissions`.

#### Ejemplos de código

**Lectura de permisos**

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

# Verificar qué permisos están asignados al AnonymousUser
# (equivalente de los campos v1 public/public_data/require_auth)
anon_permissions = [
    p["permission"].split("/")[-2]  # extraer el codename del permiso desde la URL
    for p in permissions
    if p["user"].endswith("/AnonymousUser/")
]
print("Anonymous user permissions:", anon_permissions)
# ej. ['view_asset', 'view_submissions']
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

# Verificar qué permisos están asignados al AnonymousUser
anon_permissions <- Filter(
  function(p) grepl("AnonymousUser", p$user),
  permissions
)
for (p in anon_permissions) cat(p$label, "\n")
```
</details>

**Asignación de permisos al AnonymousUser**

Para replicar la configuración `public: true` de v1, envía un POST con una nueva asignación de permisos al endpoint `permission-assignments`.

<details>
<summary><strong>curl</strong></summary>

```bash
# Otorgar a AnonymousUser view_asset (equivalente de v1 public: true)
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

# Otorgar a AnonymousUser view_asset (equivalente de v1 public: true)
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

# Otorgar a AnonymousUser view_asset (equivalente de v1 public: true)
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

#### Ejemplos de respuestas

<details>
<summary><strong>Ejemplo: permisos de <code>v2</code> para el usuario anónimo</strong></summary>
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

### Endpoint de etiquetas
El endpoint `/api/v1/forms/<pk>/labels` de `v1` devuelve un diccionario que mapea cada nombre de campo en el formulario a su etiqueta correspondiente, permitiendo una visualización más amigable de los datos del formulario.

Este endpoint no se ha portado a `v2`, pero aún es posible **etiquetar** o **marcar** un proyecto, como se describe [arriba](#tags).

---

### Endpoints de metadatos
Estos endpoints devuelven una lista plana de todos los archivos multimedia asociados con el/la usuario/a actual, en todos los proyectos desplegados o en un proyecto específico. En `v2`, los archivos multimedia ahora están limitados por proyecto. Al igual que con otros endpoints, `v2` introduce paginación, mientras que `v1` devuelve todos los resultados en una sola respuesta.

**Mapeo de endpoints**

| Endpoint `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `/api/v1/metadata`   | `/api/v2/assets/{asset_uid}/files/` |
| `/api/v1/metadata/<pk>`       | `/api/v2/assets/{asset_uid}/files/{file_uid}/`                 |


<p class="note">
  <b>Nota:</b> <code>v2</code> solo admite archivos multimedia: <code>media</code> de <code>v1</code> se mapea a <code>form_media</code> en <code>v2</code>. <strong>Otros tipos de metadatos</strong> de <code>v1</code> (por ejemplo, <code>doc</code>, <code>mapbox_layer</code>, <code>source</code>, etc.) no se han portado a <code>v2</code>.
</p>


**Mapeo de campos**

| Campo `v1`        | Equivalente `v2`                        |
|-------------------|----------------------------------------|
| `id`              | `uid`                                  |
| `data_type`       | `file_type`                            |
| `xform`           | _N/A_<sup>1</sup>                      |
| `data_value`      | `metadata.filename` o `metadata.redirect_url` |
| `data_filename`   | `metadata.filename`                    |
| `data_file`       | `content`                              |
| `data_file_type`  | `metadata.mimetype`                    |
| `file_hash`       | `metadata.hash`                        |
| `from_kpi`        | _N/A_                                  |

<sup>1</sup> _En `v2`, el proyecto relacionado es accesible a través del campo `asset`, que contiene una URL completa en lugar de un ID entero._

#### Ejemplos de código

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (obsoleto) — listar todos los archivos multimedia de todos los proyectos
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata"

# v1 (obsoleto) — archivo individual por ID entero
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata/271"

# v2 — listar archivos multimedia de un proyecto específico
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/"

# v2 — archivo individual por uid
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/afoeCcF3AcGNpWUoM6bvKj9/"

# v2 — subir un nuevo archivo multimedia
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

# v1 (obsoleto)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/metadata", headers=headers)
# files = response.json()  # lista plana de todos los proyectos

# v2 — listar archivos multimedia de un proyecto específico (paginado)
response = requests.get(
    f"{BASE_URL}/api/v2/assets/{ASSET_UID}/files/",
    headers=headers
)
response.raise_for_status()
files = response.json()["results"]

for f in files:
    print(f["uid"], f["metadata"]["filename"])  # era: f["id"], f["data_filename"]

# v2 — subir un nuevo archivo multimedia
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

# v1 (obsoleto)
# response <- GET("https://kc.kobotoolbox.org/api/v1/metadata", headers)
# files <- content(response, as = "parsed")  # lista plana de todos los proyectos

# v2 — listar archivos multimedia de un proyecto específico
response <- GET(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/files/"),
  headers
)
files <- content(response, as = "parsed")$results

for (f in files) {
  cat(f$uid, f$metadata$filename, "\n")  # era: f$id, f$data_filename
}

# v2 — subir un nuevo archivo multimedia
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

#### Ejemplos de respuestas

<details>
<summary><strong>Respuesta v1</strong></summary>

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
<summary><strong>Equivalente v2</strong></summary>

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

### Endpoints de usuario/a
Este endpoint devuelve información de perfil sobre el/la usuario/a autenticado/a, incluyendo la identidad de la cuenta y detalles asociados.

**Mapeo de endpoints**

| Endpoint `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `/api/v1/user`   | `/me/` |


**Mapeo de campos**

| Campo `v1`        | Equivalente `v2`                        |
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


<sup>1</sup> _No portado a `v2`_

<sup>2</sup> _Usa https://kf.domain.tld/token en su lugar_

#### Ejemplos de código

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (obsoleto)
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

# v1 (obsoleto)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/user", headers=headers)
# user = response.json()
# print(user["username"], user["email"])

# v2
response = requests.get(f"{BASE_URL}/me/", headers=headers)
response.raise_for_status()
user = response.json()

print(user["username"])                        # igual que v1
print(user["email"])                           # igual que v1
print(user["extra_details"]["organization"])   # era: user["organization"]
print(user["extra_details"]["country"])        # era: user["country"]
print(user["extra_details__uid"])              # era: user["id"]
```
</details>

<details>
<summary><strong>R</strong></summary>

```r
library(httr)

TOKEN <- "xxxx"
BASE_URL <- "https://kf.kobotoolbox.org"
headers <- add_headers(Authorization = paste("Token", TOKEN))

# v1 (obsoleto)
# response <- GET("https://kc.kobotoolbox.org/api/v1/user", headers)
# user <- content(response, as = "parsed")

# v2
response <- GET(paste0(BASE_URL, "/me/"), headers)
user <- content(response, as = "parsed")

cat(user$username, "\n")                         # igual que v1
cat(user$email, "\n")                            # igual que v1
cat(user$extra_details$organization, "\n")       # era: user$organization
cat(user$extra_details$country, "\n")            # era: user$country
cat(user$extra_details__uid, "\n")               # era: user$id
```
</details>

#### Ejemplos de respuestas

<details>
<summary><strong>Respuesta v1</strong></summary>

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
<summary><strong>Equivalente v2</strong></summary>

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
