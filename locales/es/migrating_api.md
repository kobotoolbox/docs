# Migración de la API v1 a v2
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7a618b1d0f3bc3dffa450c17d9e5063ca4c69770/source/migrating_api.md" class="reference">7 ago 2025</a>

Como parte de nuestros esfuerzos continuos para optimizar y modernizar la plataforma KoboToolbox, estamos eliminando gradualmente los endpoints `v1` de KPI y KoboCAT. Todos los endpoints `v1` de KPI y KoboCAT están ahora obsoletos y se eliminarán por completo en enero de 2026. Los endpoints `v1` están siendo reemplazados por la API KPI `v2`, que es más robusta y cuenta con soporte completo.

Este artículo explica cómo migrar tus integraciones de API desde la API `v1` (KoboCAT y KPI) a la API KPI `v2`. Cubre cada endpoint `v1` obsoleto y su equivalente en `v2` para ayudarte a realizar la transición de tus flujos de trabajo.


## Migración de KPI v1 a KPI v2
La migración de la API KPI antigua (`v1`) a la nueva versión (`v2`) es sencilla en la mayoría de los casos.

En general, solo necesitas actualizar la ruta base de `/endpoint/` a `/api/v2/endpoint/`.

### Excepción para el endpoint de exportaciones
La única excepción a la regla anterior es el endpoint `/exports/`. En `v1`, el endpoint `/exports/` devolvía **todas las exportaciones del/de la usuario/a autenticado/a** en todos los proyectos.

En `v2`, por razones de rendimiento, las exportaciones ahora están **limitadas por proyecto** y deben accederse a través de `/api/v2/assets/{asset_uid}/exports/`.



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


**Ejemplo de respuesta `v1`**

```json
{
  "id": 474,
  "id_string": "a4etXeWtqcoodSxLV8a6Uq",
  "title": "Pathways Initiative",
  "description": "Pathways Initiative",
  "url": "https://kc.kobotoolbox.org/api/v1/data/474.json"
}
```

**Respuesta equivalente `v2`**

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

### Endpoints de datos: Datos de envío
Estos endpoints recuperan todos los datos de envío de un proyecto específico o un único envío del proyecto. `{uid}` es el identificador único del proyecto y `{submission_id}` es el identificador único de un envío de formulario.

| Endpoint `v1`    | Equivalente `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

Basándote en la `url` que obtienes de la propiedad `data` en el endpoint del asset, puedes obtener los datos de envío en `v2`.

<p class="note">
  <b>Nota:</b> La estructura de respuesta es casi la misma, <strong>excepto que <code>v2</code> introduce paginación</strong>.
</p>


**Ejemplo de respuesta `v1`**

```json
[
  {
    "_id": 49542,
    ...
  }
]
```
**Respuesta equivalente `v2`**

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

**Permisos**

En `v2`, los campos `public`, `public_data` y `require_auth` ya no están expuestos como atributos booleanos. En su lugar, **el acceso anónimo se controla mediante asignaciones de permisos explícitas al `AnonymousUser`**.

Se aplican los siguientes mapeos:
- `public: true` → el `AnonymousUser` tiene el permiso `view_asset`  
- `public_data: true` → el `AnonymousUser` tiene el permiso `view_submissions`  
- `require_auth: false` → el `AnonymousUser` tiene el permiso `add_submissions`  


<details>
<summary><strong>Ejemplo: permisos de usuario/a anónimo/a en <code>v2</code></strong></summary>
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

Este endpoint no se ha portado a `v2`, pero aún es posible **etiquetar** un proyecto, como se describe [arriba](#tags).

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

**Ejemplo de respuesta `v1`**

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

**Respuesta equivalente `v2`**

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