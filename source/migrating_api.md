# Migrating from v1 to v2 API
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/7a618b1d0f3bc3dffa450c17d9e5063ca4c69770/source/migrating_api.md" class="reference">7 Aug 2025</a>


As part of our ongoing efforts to streamline and modernize the KoboToolbox platform, we are phasing out KPI and KoboCAT `v1` endpoints. All KPI and KoboCAT `v1` endpoints are now deprecated, and will be removed entirely in June 2026. `v1` endpoints are being phased out in favor of the more robust and fully supported KPI `v2` API. 

This article explains how to migrate your API integrations from the `v1` API (KoboCAT and KPI) to the KPI `v2` API. It covers each deprecated `v1` endpoint and its `v2` equivalent to help you transition your workflows.


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


**Example `v1` response**

```json
{
  "id": 474,
  "id_string": "a4etXeWtqcoodSxLV8a6Uq",
  "title": "Pathways Initiative",
  "description": "Pathways Initiative",
  "url": "https://kc.kobotoolbox.org/api/v1/data/474.json"
}
```

**Equivalent `v2` response**

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

### Data endpoints: Submission data
These endpoints retrieve all submission data for a specific project or a single submission from the project. `{uid}` is the unique identifier of the project and `{submission_id}` is the unique identifier of a form submission.

| `v1` Endpoint    | `v2` Equivalent        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

Based on the `url` you get from the `data` property in the asset endpoint, you can fetch the submission data in `v2` using. 

<p class="note">
  <b>Note:</b> The response structure is nearly the same, <strong>except that <code>v2</code> introduces pagination</strong>.
</p>


**Example `v1` response**

```json
[
  {
    "_id": 49542,
    ...
  }
]
```
**Equivalent `v2` response**

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

**Permissions**

In `v2`, the fields `public`, `public_data`, and `require_auth` are no longer exposed as boolean attributes. Instead, **anonymous access is controlled via explicit permission assignments to the `AnonymousUser`**.

The following mappings apply:
- `public: true` → the `AnonymousUser` has the `view_asset` permission  
- `public_data: true` → the `AnonymousUser` has the `view_submissions` permission  
- `require_auth: false` → the `AnonymousUser` has the `add_submissions` permission  


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

**Example `v1` response**

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

**Equivalent `v2` response**

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





