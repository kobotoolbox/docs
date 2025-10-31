# الترحيل من واجهة برمجة التطبيقات v1 إلى v2
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/7a618b1d0f3bc3dffa450c17d9e5063ca4c69770/source/migrating_api.md" class="reference">7 أغسطس 2025</a>

كجزء من جهودنا المستمرة لتبسيط وتحديث منصة KoboToolbox، نقوم بإيقاف نقاط نهاية KPI وKoboCAT `v1` تدريجياً. جميع نقاط نهاية KPI وKoboCAT `v1` أصبحت الآن قديمة، وسيتم إزالتها بالكامل في يناير 2026. يتم إيقاف نقاط نهاية `v1` تدريجياً لصالح واجهة برمجة التطبيقات KPI `v2` الأكثر قوة والمدعومة بالكامل.

يشرح هذا المقال كيفية ترحيل تكاملات واجهة برمجة التطبيقات الخاصة بك من واجهة برمجة التطبيقات `v1` (KoboCAT وKPI) إلى واجهة برمجة التطبيقات KPI `v2`. ويغطي كل نقطة نهاية `v1` قديمة ومعادلها في `v2` لمساعدتك في نقل سير العمل الخاص بك.


## الترحيل من KPI v1 إلى KPI v2
الترحيل من واجهة برمجة التطبيقات KPI القديمة (`v1`) إلى الإصدار الجديد (`v2`) أمر مباشر في معظم الحالات.

بشكل عام، تحتاج فقط إلى تحديث المسار الأساسي من `/endpoint/` إلى `/api/v2/endpoint/`.

### استثناء لنقطة نهاية exports
الاستثناء الوحيد للقاعدة أعلاه هو نقطة نهاية `/exports/`. في `v1`، كانت نقطة نهاية `/exports/` تُرجع **جميع الصادرات للمستخدم المصادق عليه** عبر جميع المشاريع.

في `v2`، لأسباب تتعلق بالأداء، أصبحت الصادرات الآن **محددة النطاق لكل مشروع** ويجب الوصول إليها عبر `/api/v2/assets/{asset_uid}/exports/`.



## الترحيل من KoboCAT v1 إلى KPI v2
يسرد القسم التالي نقاط النهاية الرئيسية من واجهة برمجة التطبيقات KoboCAT `v1` ويوفر معادلاتها في `v2`.

### نقاط نهاية البيانات: قائمة المشاريع
تُرجع نقطة النهاية هذه قائمة بالنماذج التي يمكنك الوصول إليها، مع روابط لبيانات الإرسال الخاصة بها، وتعمل كنقطة دخول للوصول إلى الاستجابات أو تنزيلها.

**تعيين نقطة النهاية من `v1` إلى `v2`**

| نقطة نهاية `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data`          | `/api/v2/assets/?asset_type=survey`  |


**تعيين الحقول من `v1` إلى `v2`**

| حقل `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `id`          | `uid`<sup>1</sup>      |
| `id_string`   | `uid`                  |
| `title`       | `name`                 |
| `description` | `settings.description` |
| `url`         | `data`                 |

<sup>1</sup> _في نقطة نهاية `/api/v2/assets`، لم تعد المعرفات الصحيحة المتسلسلة مستخدمة. يتم تحديد كل إدخال بشكل فريد بواسطة `uid` أبجدي رقمي_


**مثال على استجابة `v1`**

```json
{
  "id": 474,
  "id_string": "a4etXeWtqcoodSxLV8a6Uq",
  "title": "Pathways Initiative",
  "description": "Pathways Initiative",
  "url": "https://kc.kobotoolbox.org/api/v1/data/474.json"
}
```

**استجابة `v2` المعادلة**

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

### نقاط نهاية البيانات: بيانات الإرسال
تسترجع نقاط النهاية هذه جميع بيانات الإرسال لمشروع معين أو إرسال واحد من المشروع. `{uid}` هو المعرف الفريد للمشروع و`{submission_id}` هو المعرف الفريد لإرسال النموذج.

| نقطة نهاية `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

بناءً على `url` الذي تحصل عليه من خاصية `data` في نقطة نهاية الأصل، يمكنك جلب بيانات الإرسال في `v2` باستخدام.

<p class="note">
  <b>ملاحظة:</b> بنية الاستجابة متشابهة تقريباً، <strong>باستثناء أن <code>v2</code> يقدم ترقيم الصفحات</strong>.
</p>


**مثال على استجابة `v1`**

```json
[
  {
    "_id": 49542,
    ...
  }
]
```
**استجابة `v2` المعادلة**

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


### نقاط نهاية النموذج
تُرجع نقاط النهاية هذه سمات تفصيلية لجميع النماذج المشتركة معك أو حول نموذج معين، حيث `{uid}` هو المعرف الفريد للمشروع.

**تعيين نقطة النهاية**

| نقطة نهاية `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `/api/v1/forms`   | `/api/v2/assets/?asset_type=survey` |
| `/api/v1/forms/<pk>`       | `/api/v2/assets/{asset_uid}/`                 |


<p class="note">
  <b>ملاحظة:</b> تتبع نقطة نهاية <code>v2</code> نفس البنية لكل عنصر كما هو مدرج أدناه، لكنها تقدم ترقيم الصفحات. بعض الخصائص من نقطة نهاية <code>v1</code> غير متاحة مباشرة في نقطة نهاية الأصل <code>v2</code>، لكن لا يزال من الممكن الوصول إليها بشكل مختلف (انظر الشرح أسفل الجدول لمزيد من التفاصيل).
</p>


**تعيين الحقول**
| حقل `v1`                 | معادل `v2`                          |
|----------------------------|------------------------------------------|
| `formid`                   | `uid`<sup>1</sup>                        |
| `owner`                    | `owner__username`                        |
| `metadata`                 | `files`                                  |
| `tags`                     | `tag_string`<sup>2</sup>                 |
| `title`                    | `name`                                   |
| `public`                   | _غير متاح_<sup>3</sup>                        |
| `public_data`              | _غير متاح_<sup>3</sup>                        |
| `require_auth`             | _غير متاح_<sup>3</sup>                        |
| `users`                    | `permissions`                            |
| `hash`                     | `version__content_hash`                  |
| `downloadable`             | `deployment__active`                     |
| `encrypted`                | `deployment__encrypted`                  |
| `last_submission_time`     | `deployment__last_submission_time`       |
| `uuid`                     | `deployment__uuid`                       |
| `instances_with_geopoints` | `summary.geo`                            |
| `num_of_submissions`       | `deployment__submission_count`           |
| `attachment_storage_bytes` | _غير متاح_<sup>4</sup>                        |

<sup>1</sup> _في نقطة نهاية `/api/v2/assets`، لم تعد المعرفات الصحيحة المتسلسلة مستخدمة. يتم تحديد كل إدخال بشكل فريد بواسطة `uid` أبجدي رقمي_.  
<sup>2</sup> _في `v1`، تم إرجاع العلامات كمصفوفة؛ في `v2`، يتم إرجاعها كسلسلة مفصولة بفواصل._  
<sup>3</sup> _لم تعد هذه الحقول معروضة. راجع قسم **الأذونات** أدناه لمزيد من التفاصيل._  
<sup>4</sup> _غير قابل للوصول مباشرة عبر نقطة نهاية الأصل. استخدم نقطة نهاية `/api/v2/asset_usage/` واسترجع حقل `storage_bytes` للمشروع المقابل._

<details>
<summary><strong>مثال على استجابة <code>v1</code></strong></summary>
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
<summary><strong>استجابة <code>v2</code> المعادلة</strong></summary>
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
**العلامات**

العلامات في `v1` و`v2` لا تشترك في نفس قاعدة البيانات الأساسية. ونتيجة لذلك، **لن يتم ترحيل** العلامات من `v1` تلقائياً إلى `v2`. إذا كنت بحاجة إلى الاحتفاظ بها، يجب عليك إعادة تطبيق العلامات يدوياً باستخدام طلب `PATCH` إلى `/api/v2/assets/{uid}/`.

مثال على البيانات:
```json
{ "tag_string": "tag1,tag2,tag3" }
```

**الأذونات**

في `v2`، لم تعد الحقول `public` و`public_data` و`require_auth` معروضة كسمات منطقية. بدلاً من ذلك، **يتم التحكم في الوصول المجهول عبر تعيينات أذونات صريحة لـ `AnonymousUser`**.

تنطبق التعيينات التالية:
- `public: true` ← لدى `AnonymousUser` إذن `view_asset`  
- `public_data: true` ← لدى `AnonymousUser` إذن `view_submissions`  
- `require_auth: false` ← لدى `AnonymousUser` إذن `add_submissions`  


<details>
<summary><strong>مثال: أذونات المستخدم المجهول في <code>v2</code></strong></summary>
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

### نقطة نهاية التسمية
تُرجع نقطة نهاية `/api/v1/forms/<pk>/labels` من `v1` قاموساً يربط كل اسم حقل في النموذج بتسميته المقابلة، مما يتيح عرضاً أكثر سهولة لبيانات النموذج.

لم يتم نقل نقطة النهاية هذه إلى `v2`، لكن لا يزال من الممكن **تسمية** أو **وضع علامة** على مشروع، كما هو موضح [أعلاه](#tags).

---

### نقاط نهاية البيانات الوصفية
تُرجع نقاط النهاية هذه قائمة مسطحة بجميع ملفات الوسائط المرتبطة بالمستخدم الحالي، عبر جميع المشاريع المنشورة أو مشروع معين. في `v2`، أصبحت ملفات الوسائط الآن محددة النطاق لكل مشروع. كما هو الحال مع نقاط النهاية الأخرى، يقدم `v2` ترقيم الصفحات، بينما يُرجع `v1` جميع النتائج في استجابة واحدة.

**تعيين نقطة النهاية**

| نقطة نهاية `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `/api/v1/metadata`   | `/api/v2/assets/{asset_uid}/files/` |
| `/api/v1/metadata/<pk>`       | `/api/v2/assets/{asset_uid}/files/{file_uid}/`                 |


<p class="note">
  <b>ملاحظة:</b> يدعم <code>v2</code> فقط ملفات الوسائط: <code>media</code> من <code>v1</code> يتم تعيينه إلى <code>form_media</code> في <code>v2</code>. <strong>أنواع البيانات الوصفية الأخرى</strong> من <code>v1</code> (مثل <code>doc</code> و<code>mapbox_layer</code> و<code>source</code> إلخ.) لم يتم نقلها إلى <code>v2</code>.
</p>


**تعيين الحقول**

| حقل `v1`        | معادل `v2`                        |
|-------------------|----------------------------------------|
| `id`              | `uid`                                  |
| `data_type`       | `file_type`                            |
| `xform`           | _غير متاح_<sup>1</sup>                      |
| `data_value`      | `metadata.filename` أو `metadata.redirect_url` |
| `data_filename`   | `metadata.filename`                    |
| `data_file`       | `content`                              |
| `data_file_type`  | `metadata.mimetype`                    |
| `file_hash`       | `metadata.hash`                        |
| `from_kpi`        | _غير متاح_                                  |

<sup>1</sup> _في `v2`، يمكن الوصول إلى المشروع ذي الصلة عبر حقل `asset`، الذي يحتوي على عنوان URL كامل بدلاً من معرف صحيح._

**مثال على استجابة `v1`**

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

**استجابة `v2` المعادلة**

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

### نقاط نهاية المستخدم
تُرجع نقطة النهاية هذه معلومات الملف الشخصي حول المستخدم المصادق عليه، بما في ذلك هوية الحساب والتفاصيل المرتبطة.

**تعيين نقطة النهاية**

| نقطة نهاية `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `/api/v1/user`   | `/me/` |


**تعيين الحقول**

| حقل `v1`        | معادل `v2`                        |
|-------------------|----------------------------------------|
| `id`              | `extra_details__uid`                                  |
| `username`       | `username`                            |
| `email`           |  `email`               |
| `city`           |  `extra_details.city`  |
| `country`           |  `extra_details.country`  |
| `organization`           |  `extra_details.organization`  |
| `website`           |  `extra_details.website`  |
| `twitter`           |  `extra_details.twitter`  |
| `url`           |  غير متاح<sup>1</sup>  |
| `user`           |  غير متاح<sup>1</sup>  |
| `gravatar`           |  `gravatar`  |
| `require_auth`           |  `require_auth`  |
| `api_token`           |  غير متاح<sup>2</sup>  |
| `temp_token`           |  غير متاح<sup>1</sup>  |


<sup>1</sup> _لم يتم نقله إلى `v2`_

<sup>2</sup> _استخدم https://kf.domain.tld/token بدلاً من ذلك_