# الترحيل من واجهة برمجة التطبيقات v1 إلى v2
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/62f9bf5497b6f6a7e0d1ff3f2e5d1da7bad99168/source/migrating_api.md" class="reference">19 مايو 2026</a>

كجزء من جهودنا المستمرة لتبسيط وتحديث منصة KoboToolbox، نقوم بإيقاف نقاط نهاية KPI وKoboCAT `v1` تدريجياً. جميع نقاط نهاية KPI وKoboCAT `v1` أصبحت الآن قديمة، وسيتم إزالتها بالكامل في يونيو 2026. يتم إيقاف نقاط نهاية `v1` تدريجياً لصالح واجهة برمجة التطبيقات KPI `v2` الأكثر قوة والمدعومة بالكامل.

يشرح هذا المقال كيفية ترحيل تكاملات واجهة برمجة التطبيقات الخاصة بك من واجهة برمجة التطبيقات `v1` (KoboCAT وKPI) إلى واجهة برمجة التطبيقات KPI `v2`. ويغطي كل نقطة نهاية `v1` قديمة ومعادلها في `v2` لمساعدتك في نقل سير العمل الخاص بك.


## المصادقة

تتطلب جميع طلبات واجهة برمجة التطبيقات — v1 وv2 — رمز API. أدرجه في كل طلب باستخدام رأس `Authorization`:

```
Authorization: Token xxxx
```

استبدل `xxxx` برمزك الفعلي. يمكنك العثور على رمزك في `https://kf.kobotoolbox.org/token/` (أو ما يعادله على خادمك).

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
  <b>ملاحظة:</b> رأس المصادقة هو نفسه عبر جميع إصدارات واجهة برمجة التطبيقات. ما يتغير يعتمد على مسار الترحيل الذي تسلكه: إذا كنت تنتقل من <strong>KPI v1 إلى KPI v2</strong>، فأنت تحتاج فقط إلى تحديث مسار URL. أما إذا كنت تنتقل من <strong>KoboCAT v1 إلى KPI v2</strong>، فستحتاج أيضاً إلى تحديث النطاق الأساسي (<code>kc.kobotoolbox.org</code> → <code>kf.kobotoolbox.org</code>)، ومسارات نقاط النهاية، وتكييف الكود للتعامل مع بنية الاستجابة الجديدة وأسماء الحقول — راجع الأقسام أدناه.
</p>


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


#### أمثلة على الكود

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (قديم)
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

# v1 (قديم)
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

# v1 (قديم)
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

#### أمثلة على الاستجابات

<details>
<summary><strong>استجابة v1</strong></summary>

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
<summary><strong>المعادل في v2</strong></summary>

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

### نقاط نهاية البيانات: بيانات الإرسال
تسترجع نقاط النهاية هذه جميع بيانات الإرسال لمشروع معين أو إرسال واحد من المشروع. `{uid}` هو المعرف الفريد للمشروع و`{submission_id}` هو المعرف الفريد لإرسال النموذج.

| نقطة نهاية `v1`    | معادل `v2`        |
| ------------- | ---------------------- |
| `/api/v1/data/<pk>`   | `/api/v2/assets/{uid}/data/` |
| `/api/v1/data/<pk>/<dataid>`       | `/api/v2/assets/{uid}/data/{submission_id}/`                 |

بناءً على `url` الذي تحصل عليه من خاصية `data` في نقطة نهاية الأصل، يمكنك جلب بيانات الإرسال في `v2` باستخدام. 

<p class="note">
  <b>ملاحظة:</b> بنية الاستجابة متشابهة تقريباً، <strong>باستثناء أن <code>v2</code> يقدم ترقيم الصفحات</strong>. إذا كان لديك أكثر من 30,000 إرسال، ستحتاج إلى متابعة عنوان URL في `next` لاسترجاع الصفحات التالية.
</p>

#### أمثلة على الكود

استبدل `a4etXeWtqcoodSxLV8a6Uq` بـ `uid` مشروعك (راجع [نقطة نهاية قائمة المشاريع](#data-endpoints-project-list) أعلاه).

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (قديم) — كان يستخدم معرف النموذج الصحيح
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/data/474"

# v2 — استخدم uid الأبجدي الرقمي
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

# v1 (قديم)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/data/474", headers=headers)
# submissions = response.json()  # أرجع قائمة مسطحة

# v2 — النتائج مقسمة إلى صفحات
url = f"https://kf.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data/"
all_submissions = []

while url:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    page = response.json()
    all_submissions.extend(page["results"])
    url = page["next"]  # None عندما لا توجد صفحات أخرى

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

# v1 (قديم)
# response <- GET(paste0("https://kc.kobotoolbox.org/api/v1/data/474"), headers)
# submissions <- content(response, as = "parsed")  # قائمة مسطحة

# v2 — التعامل مع ترقيم الصفحات
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

#### أمثلة على الاستجابات

<details>
<summary><strong>استجابة v1</strong></summary>

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
<summary><strong>المعادل في v2</strong></summary>

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

#### أمثلة على الكود

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (قديم) — قائمة بجميع النماذج
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms"

# v1 (قديم) — نموذج واحد بالمعرف الصحيح
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/forms/474"

# v2 — قائمة بجميع النماذج (مع ترقيم الصفحات)
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/?asset_type=survey"

# v2 — نموذج واحد بالـ uid
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

# v1 (قديم)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/forms/474", headers=headers)
# form = response.json()

# v2 — نموذج واحد
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

# v1 (قديم)
# response <- GET("https://kc.kobotoolbox.org/api/v1/forms/474", headers)
# form <- content(response, as = "parsed")

# v2 — نموذج واحد
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

#### أمثلة على الاستجابات

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

#### أمثلة على الكود

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

**الأذونات**

في `v2`، لم تعد الحقول `public` و`public_data` و`require_auth` معروضة كسمات منطقية. بدلاً من ذلك، **يتم التحكم في الوصول المجهول عبر تعيينات أذونات صريحة لـ `AnonymousUser`**.

تنطبق التعيينات التالية:
- `public: true` → لدى `AnonymousUser` إذن `view_asset`  
- `public_data: true` → لدى `AnonymousUser` إذن `view_submissions`  
- `require_auth: false` → لدى `AnonymousUser` إذن `add_submissions`  

الأذونات متاحة في نقطة نهاية تفاصيل الأصل (`/api/v2/assets/{uid}/`) تحت خاصية `permissions`.

#### أمثلة على الكود

**قراءة الأذونات**

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

**تعيين الأذونات لـ AnonymousUser**

لتكرار إعداد `public: true` في v1، أرسل طلب POST لتعيين إذن جديد إلى نقطة نهاية `permission-assignments`.

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

#### أمثلة على الاستجابات

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

#### أمثلة على الكود

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (قديم) — قائمة بجميع ملفات الوسائط عبر جميع المشاريع
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata"

# v1 (قديم) — ملف واحد بالمعرف الصحيح
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kc.kobotoolbox.org/api/v1/metadata/271"

# v2 — قائمة ملفات الوسائط لمشروع معين
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/"

# v2 — ملف واحد بالـ uid
curl -H "Authorization: Token xxxx" \
     -H "Content-Type: application/json" \
  "https://kf.kobotoolbox.org/api/v2/assets/a4etXeWtqcoodSxLV8a6Uq/files/afoeCcF3AcGNpWUoM6bvKj9/"

# v2 — رفع ملف وسائط جديد
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

# v1 (قديم)
# response = requests.get("https://kc.kobotoolbox.org/api/v1/metadata", headers=headers)
# files = response.json()  # قائمة مسطحة عبر جميع المشاريع

# v2 — قائمة ملفات الوسائط لمشروع معين (مع ترقيم الصفحات)
response = requests.get(
    f"{BASE_URL}/api/v2/assets/{ASSET_UID}/files/",
    headers=headers
)
response.raise_for_status()
files = response.json()["results"]

for f in files:
    print(f["uid"], f["metadata"]["filename"])  # was: f["id"], f["data_filename"]

# v2 — رفع ملف وسائط جديد
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

# v1 (قديم)
# response <- GET("https://kc.kobotoolbox.org/api/v1/metadata", headers)
# files <- content(response, as = "parsed")  # قائمة مسطحة عبر جميع المشاريع

# v2 — قائمة ملفات الوسائط لمشروع معين
response <- GET(
  paste0(BASE_URL, "/api/v2/assets/", ASSET_UID, "/files/"),
  headers
)
files <- content(response, as = "parsed")$results

for (f in files) {
  cat(f$uid, f$metadata$filename, "\n")  # was: f$id, f$data_filename
}

# v2 — رفع ملف وسائط جديد
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

#### أمثلة على الاستجابات

<details>
<summary><strong>استجابة v1</strong></summary>

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
<summary><strong>المعادل في v2</strong></summary>

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

#### أمثلة على الكود

<details>
<summary><strong>curl</strong></summary>

```bash
# v1 (قديم)
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

# v1 (قديم)
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

# v1 (قديم)
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

#### أمثلة على الاستجابات

<details>
<summary><strong>استجابة v1</strong></summary>

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
<summary><strong>المعادل في v2</strong></summary>

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
