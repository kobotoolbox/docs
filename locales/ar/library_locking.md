# قفل المكتبة
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/de5e7dcfcec534ba447ee21ff65cf9fff07723f2/source/library_locking.md" class="reference">30 سبتمبر 2025</a>

يشير "قفل المكتبة" إلى الميزة التي تمكّن من "[قفل](#locked)" جوانب مختلفة من الاستبيان عند إنشائه من قالب يحتوي على [سمات القفل](#restrictions). جميع جوانب تحرير النموذج متاحة للقفل من خلال تعيين "[ملفات تعريف القفل](#profile)" على مستوى النموذج أو السؤال أو المجموعة. يمكن تعيين "[قيود](#restriction)" دقيقة لملفات تعريف القفل هذه والتي تجمع وظائف القفل معًا. بدلاً من ذلك، يمكن قفل النموذج بالكامل، مما يمنع جميع جوانب التحرير.

<p class="note">
  حاليًا، يتم دعم القفل المحدد ضمن XLSForm نفسه فقط، ولكن سيتم دمجه في أداة إنشاء النماذج في وقت ما في المستقبل.
</p>

قد تكون هذه الميزة مفيدة في بيئة فريق كبير وموزع حيث يتم استخدام قالب قياسي، مع بعض الميزات المقفلة، ويمكن لكل فريق إجراء التعديلات المحلية اللازمة لاحتياجاته. يمكن لمنشئ القالب الاستمرار في إجراء التحديثات، لكن الأقفال ستقيد التغييرات على جوانب محددة من النموذج لأولئك الذين [ينشئون مشروعًا بناءً على القالب](quick_start.md).

<p class="note">
  قفل جوانب النموذج منفصل عن
  <a class="reference" href="https://support.kobotoolbox.org/ar/managing_permissions.html">إدارة أذونات المشروع</a>.
</p>

## القيود

هناك ثلاثة مستويات من القيود التي يمكن تعيينها:

1. [السؤال](#question-level-restrictions)،
2. [المجموعة](#group-level-restrictions)، و
3. [النموذج](#form-level-restrictions)

بالإضافة إلى ذلك، هناك قيمة منطقية `kobo--lock_all` يمكن تعيينها في ورقة `settings` والتي ستجعل الاستبيان مقفلًا بالكامل.

### القيمة المنطقية `kobo--lock_all`

إذا تم تعيين `kobo--lock_all` على `True`، فإن جميع القيود الدقيقة الإضافية تكون زائدة عن الحاجة حيث يكون النموذج مقفلًا _بالكامل_. إذا تم تعيينها على `False` _أو_ تم حذفها من ورقة `settings`، فيمكن استخدام ملفات تعريف القفل المحددة للتحكم في سلوك القفل:

**ورقة settings**

| kobo--lock_all |
| :------------- |
| true           |
| settings |

القيم المقبولة لـ `kobo--lock_all` هي نفسها الموجودة في ورقة `survey` التي
[يدعمها pyxform](https://github.com/XLSForm/pyxform/blob/43ea039250f44cff23b3ad10740fca54dfa12383/pyxform/aliases.py#L127-L142).
لن يتم طرح خطأ إذا تم استخدام قيمة غير صالحة، فقط لن يعمل النموذج كما هو مقصود من وجهة نظر المستخدم.

<p class="note">
  لاحظ أن اسم القيد، مثل <code>choice_add</code> أدناه، هو
  <strong>محدد مسبقًا</strong> والقيود المدرجة أدناه فقط هي خيارات صالحة.
</p>

### قيود مستوى السؤال

| الاسم                      | الوصف                                                              |
| :------------------------- | :----------------------------------------------------------------- |
| `choice_add`               | إضافة خيارات جديدة إلى سؤال `select_*`                            |
| `choice_delete`            | إزالة خيار موجود من سؤال `select_*`                               |
| `choice_value_edit`        | تحرير `name` الخيار                                                |
| `choice_label_edit`        | تحرير `label` الخيار                                               |
| `choice_order_edit`        | إعادة ترتيب خيارات سؤال `select_*`                                |
| `question_delete`          | حذف سؤال معين                                                      |
| `question_label_edit`      | تحرير `label` أو `hint` موجود                                      |
| `question_settings_edit`   | تحرير إعدادات السؤال (بخلاف `constraint` أو `relevant`)            |
| `question_skip_logic_edit` | تحرير إعدادات منطق التخطي للسؤال (`relevant`)                      |
| `question_validation_edit` | تحرير إعدادات معايير التحقق من صحة السؤال (`constraint`)           |

### قيود مستوى المجموعة

| الاسم                       | الوصف                                                                                                      |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------- |
| `group_delete`              | زر **حذف كل شيء** في نافذة حذف المجموعة (أو زر حذف المجموعة إذا تم إقرانه مع `group_split`)              |
| `group_split`               | زر **إلغاء تجميع الأسئلة** في نافذة حذف المجموعة (أو زر حذف المجموعة إذا تم إقرانه مع `group_delete`)     |
| `group_label_edit`          | تحرير `label` المجموعة                                                                                    |
| `group_question_add`        | إضافة أو استنساخ الأسئلة داخل المجموعة المحددة (بما في ذلك المجموعات الفرعية)                            |
| `group_question_delete`     | حذف أي سؤال من المجموعة المحددة (بما في ذلك أسئلة المجموعات الفرعية)                                     |
| `group_question_order_edit` | تغيير ترتيب الأسئلة داخل المجموعة المحددة (بما في ذلك المجموعات الفرعية)                                |
| `group_settings_edit`       | تغيير **جميع إعدادات المجموعة** من **الإعدادات** للمجموعة المحددة                                        |
| `group_skip_logic_edit`     | تغيير **منطق التخطي** من **الإعدادات** للمجموعة المحددة                                                  |

### قيود مستوى النموذج

| الاسم                 | الوصف                                                                                        |
| :-------------------- | :------------------------------------------------------------------------------------------- |
| `form_appearance`     | تغيير مظهر النموذج من **التخطيط والإعدادات**                                                |
| `form_replace`        | استبدال النموذج باستخدام نافذة **استبدال النموذج**                                           |
| `group_add`           | زر تجميع الأسئلة                                                                             |
| `question_add`        | استخدام خيار **إدراج تحديد متتالي** وكل زر **إضافة سؤال** و **استنساخ سؤال**                |
| `question_order_edit` | تغيير ترتيب أي أسئلة                                                                         |
| `language_edit`       | تحرير اللغات في **نافذة الترجمات**                                                           |
| `form_meta_edit`      | تحرير الأسئلة الوصفية من **التخطيط والإعدادات**                                              |

## تكوين XLSForm

هناك ثلاث أوراق حيث يتم تعريف وتعيين ملفات تعريف القفل: `survey` و `settings` و `kobo--locking-profiles`. ورقة `kobo--locking-profiles` غير مدعومة رسميًا بواسطة [pyxform](https://github.com/XLSForm/pyxform) وهي خاصة بـ KoboToolbox.

يتم تعريف قيود مستوى النموذج في ورقة `settings` ويتم تعريف قيود مستوى السؤال والمجموعة في ورقة `survey`.

من داخل ورقة `kobo--locking-profiles`، يتم تعريف جميع ملفات تعريف القفل في بنية مصفوفة، باستخدام الكلمة الأساسية "[locked](#locked)" لتعيين "[قيد](#restriction)" إلى "[ملف تعريف](#profile)" محدد. على سبيل المثال:

**kobo--locking-profiles**

حدد ملفات التعريف وعيّن لها القيود. لا يوجد حد لعدد ملفات التعريف التي يمكن تعريفها (`profile_1`، ...، `profile_n`) ولكن هناك **ثلاثة ألوان فقط** تميز مظهر القفل الخاص بها في أداة إنشاء النماذج.

| restriction       | profile_1 | profile_2 | profile_3 |
| :---------------- | :-------- | :-------- | :-------- |
| choice_add        | locked    |           |           |
| choice_delete     |           | locked    |           |
| choice_label_edit | locked    |           |           |
| choice_order_edit | locked    | locked    |           |
| form_appearance   |           |           | locked    |
| kobo--locking-profiles |

<p class="note">
  لاحظ أنه ليس من الضروري تضمين جميع القيود الصالحة في عمود
  <code>restriction</code>، ولكن سيتم طرح خطأ إذا تم تضمين قيد غير صالح.
</p>

**ورقة settings**

عيّن قيود مستوى النموذج والقيمة المنطقية `kobo--lock_all`.

| kobo--locking-profile | kobo--lock_all |
| :-------------------- | :------------- |
| profile_3             | false          |
| settings |

<p class="note">
  لاحظ أن حذف <code>kobo--lock_all</code> من ورقة
  <code>settings</code> يعادل تعيينها على <code>False</code>.
</p>

**ورقة survey**

عيّن قيود مستوى السؤال والمجموعة.

| type                 | name    | label               | kobo--locking-profile |
| :------------------- | :------ | :------------------ | :-------------------- |
| select_one countries | country | Select your country | profile_1             |
| select_one cities    | city    | Select your city    | profile_2             |
| survey |

**ورقة choices**

لا يمكن تعيين قيود في ورقة `choices`.

| list_name | name      | label                    |
| :-------- | :-------- | :----------------------- |
| countries | canada    | Canada                   |
| countries | usa       | United States of America |
| cities    | vancouver | Vancouver                |
| cities    | toronto   | Toronto                  |
| cities    | baltimore | Baltimore                |
| cities    | boston    | Boston                   |
| choices |

<i>يمكن تنزيل مثال XLSForm هذا
<a download class="reference" href="/_static/files/library_locking/library-locking-example.xlsx">من هنا</a>.</i>

### استيراد XLSForms مقفلة

استورد XLSForm الخاص بك كـ `template` من خلال واجهة مستخدم KoboToolbox بالانتقال إلى **المكتبة** الخاصة بك والنقر على **جديد** ثم **رفع**. تأكد من تحديد `template` من القائمة المنسدلة **اختر النوع المطلوب** ثم استورد XLSForm الخاص بك.

![اختر نوع القالب](/images/library_locking/import-template.png)

سيظهر القالب المقفل الآن في عرض قائمة المكتبة الخاصة بك مع رمز قفل.

![قائمة المكتبة](/images/library_locking/library-list-view.png)

### إنشاء مشروع من قالب مقفل

بمجرد إضافة قالب مقفل إلى مكتبتك -- إما مباشرة من خلال استيراد XLSForm كقالب، أو إنشاء قالب بناءً على استبيان مقفل أو إضافة قالب مقفل من المجموعات العامة -- يمكنك إنشاء مشروع جديد. في قسم **المشاريع** من واجهة المستخدم، انقر على **جديد** ثم **استخدام قالب**.

![إنشاء مشروع من قالب](/images/library_locking/create-project-from-template.png)

-   اختر القالب المقفل الذي تريد استخدامه لإنشاء المشروع الجديد.

![تحديد القالب](/images/library_locking/select-template-for-new-project.png)

-   من هناك، تابع إنشاء المشروع.

![إنشاء المشروع](/images/library_locking/create-project.png)

عند استخدام هذا القالب المقفل كمثال لإنشاء مشروع جديد، ستبدو أداة إنشاء النماذج كما يلي:

-   المناطق الرمادية هي تلك التي تم تعطيلها من خلال القيود.

![نظرة عامة](/images/library_locking/formbuilder.png)

-   سيعرض مربع حوار فوق السؤال الأول نظرة عامة على بعض قيود النموذج.

![مربع الحوار](/images/library_locking/formbuilder-dialogue-box.png)

-   سيعرض كل سؤال يحتوي على ملفات تعريف قفل، في إعداداته، القيود التي تم تعيينها.

![قيود السؤال](/images/library_locking/formbuilder-question-settings.png)

-   ستكون بعض إعدادات مستوى النموذج رمادية أيضًا.

![قيود مستوى النموذج](/images/library_locking/form-style.png)

### التحقق من صحة النموذج

الحالات التالية ستطرح حاليًا `FormPackLibraryLockingError`:

-   إذا كان اسم ملف تعريف القفل (رأس العمود في ورقة `kobo--locking-profiles`) هو "locked" (نفس الكلمة الأساسية للقفل)
-   إذا كان القيد المدرج في `kobo--locking-profiles` غير صالح (ليس في قائمة [القيود المحددة مسبقًا](#restrictions))
-   إذا كانت هناك ورقة تسمى `kobo--locking-profiles` ولكن لا يوجد عمود `restriction`
-   إذا لم يتم تعريف ملفات تعريف القفل (رؤوس الأعمدة في ورقة `kobo--locking-profiles`)

<p class="note">
  سيتم توسيع التحقق من صحة ميزات قفل مكتبة XLSForm في المستقبل.
</p>

### تحذيرات

في بعض محررات جداول البيانات، يتم تحويل شرطتين مفردتين (`--`) تلقائيًا إلى شرطة m (—)، مما يجعل من الصعب كتابة `kobo--` في خلية. لذلك نقوم بتحويل جميع حالات شرطات n و m إلى شرطتين مفردتين (عندما تكون مسبوقة بـ `kobo`). سيتم تحويل XLSForm باسم ورقة "kobo—locking-profiles" إلى `kobo--locking-profiles` وبالمثل لرؤوس الأعمدة.

## تمثيل JSON

هناك سمتان للأصل حيث يمكن الوصول إلى معلومات القفل وتعديلها: `asset.summary` و `asset.content`.

إذا كان `kobo--locking-profile` اسم عمود في ورقة `survey`، فسيتم إدراجه أيضًا في مصفوفة `asset.summary.columns`.

في `asset.summary`، تصف السمتان المنطقيتان التاليتان نظرة عامة على بنية قفل النموذج:

-   `lock_all`، و
-   `lock_any`

المنطق الذي يتم من خلاله تعيين كل من هذه القيم المنطقية هو كما يلي:

-   `lock_all` هي `True` _فقط_ إذا تم تعيين `kobo--lock_all` على `True` في ورقة `settings`، وإلا فهي `False`
-   يتم تعيين `lock_any` على `True` إذا كانت _أي_ من الحالات التالية `True`:
    -   `lock_all` هي `True`،
    -   تم تعيين `kobo--locking-profile` في ورقة `settings`، أو
    -   تم تعيين `kobo--locking-profile` _واحد على الأقل_ في ورقة `survey`

في المثال أعلاه، سيكون التالي موجودًا في `asset.summary`:

```
{
  ...,
  "columns": [
    ...,
    "kobo--locking-profile"
  ],
  "lock_all": false,
  "lock_any": true,
  ...
}
```

في `asset.content`، توجد سمة `content.kobo--locking-profiles` كمصفوفة من كائنات JSON بالبنية التالية:

```
[
  {
    "name": "profile_1",
    "restrictions": [
      "choice_add",
      "choice_label_edit",
      "choice_order_edit"
    ]
  },
  ...
]
```

في `content.settings`، سيكون التالي موجودًا في كائن JSON:

```
{
  "kobo--locking-profile": "profile_3",
  "kobo--lock_all": false
}
```

وأخيرًا في `content.survey`، سيكون لكل سؤال تم تعيين ملف تعريف قفل له سمة `kobo--locking-profile` كما يلي:

```
[
  {
    "name": "country",
    "type": "select_one",
    ...
    "kobo--locking-profile": "profile_1"
  },
  {
    "name": "city",
    "type": "select_one",
    ...
    "kobo--locking-profile": "profile_2"
  },
  ...
]
```

## ملفات تعريف القفل وأنواع الأصول

من بين أنواع الأصول الأربعة (`survey` و `template` و `question` و `block`)، فقط `template` و `survey` تتعامل مع ميزات قفل المكتبة ويتم فرض الأقفال _فقط_ على الاستبيانات. عمليًا، هذا يعني ما يلي:

افترض أنه تم استيراد XLSForm يحتوي على ميزات قفل صالحة:

-   إذا تم استيراده كـ `block`، فسيتم استبعاد و/أو إزالة جميع آثار القفل من الأصل. ينتج عن هذا أصل `block` سيكون مكافئًا لنفس النموذج الذي تم رفعه بدون أي ميزات قفل؛
-   إذا تم استيراده كـ `survey` (تم استيراده من خلال قسم **المشاريع**) أو `template` فستكون جميع الأقفال سليمة:
    -   إذا، من داخل أداة إنشاء النماذج:
        -   تمت إضافة سؤال إلى المكتبة، فسيتم إزالة جميع الأقفال من أصل `question` الجديد
        -   تمت إضافة مجموعة من الأسئلة إلى المكتبة كـ `block`، فسيتم إزالة جميع الأقفال
    -   إذا تم إنشاء `template` _من_ أصل `survey` المقفل، فسيرث `template` جميع الأقفال التي كان لدى `survey` (ولكن نظرًا لأنه قالب، يمكنك تحرير المحتويات في أداة إنشاء النماذج)،
    -   إذا تم إنشاء `survey` _من_ `template` مقفل، فسيرث الاستبيان جميع الأقفال التي كان لدى `template`

| نوع الأصل الأصلي | العملية/الإجراء                                      | حالة `asset` الناتج |
| :--------------- | :---------------------------------------------------- | :------------------ |
| `survey`         | استيراد ملف XLSForm لـ `survey` مقفل                 | مقفل                |
| `survey`         | إنشاء `template` من `survey` مقفل                    | مقفل                |
| `survey`         | إنشاء `question` من `survey` مقفل※                  | غير مقفل            |
| `survey`         | إنشاء `block` من `survey` مقفل※                     | غير مقفل            |
| `template`       | استيراد ملف XLSForm لـ `template` مقفل               | مقفل                |
| `template`       | إنشاء `survey` من `template` مقفل                    | مقفل                |
| `template`       | إنشاء `question` من `template` مقفل※                | غير مقفل            |
| `template`       | إنشاء `block` من `template` مقفل※                   | غير مقفل            |
| `block`          | استيراد ملف XLSForm لـ `block` مقفل※                 | غير مقفل            |
| `block`          | إضافة `block` مقفل من المكتبة إلى `survey`           | غير مقفل            |
| `block`          | إضافة `block` مقفل من المكتبة إلى `template`         | غير مقفل            |
| `block`          | إنشاء `question` من `block` مقفل※                   | غير مقفل            |
| `question`       | استيراد ملف XLSForm لـ `block` مقفل※                 | غير مقفل            |
| `question`       | إضافة `question` مقفل من المكتبة إلى `survey`        | غير مقفل            |
| `question`       | إضافة `question` مقفل من المكتبة إلى `template`      | غير مقفل            |
| `question`       | إنشاء `block` من `question` مقفل※                   | غير مقفل            |

※ هذه الإجراءات غير ممكنة في واجهة المستخدم.

## المصطلحات

### `kobo--lock_all`

سمة تحتوي على قيمة منطقية، يتم تعيينها في ورقة `settings` وتطبق جميع قيود القفل على النموذج وجميع الأسئلة والمجموعات (مما يجعل ملفات تعريف القفل الدقيقة زائدة عن الحاجة).

### `kobo--locking-profile`

اسم العمود في أوراق `survey` و `settings` حيث يتم تعيين ملف تعريف القفل لسؤال أو مجموعة (في `survey`) أو للنموذج (في `settings`).

### `kobo--locking-profiles`

اسم الورقة حيث يتم تعيين القيود لملفات التعريف.

### `locked`

الكلمة الأساسية المستخدمة لتعيين قيد لملف تعريف في ورقة `kobo--locking-profiles`.

### ملف التعريف

الاسم المعين لمجموعة من القيود، المحددة في ورقة `kobo--locking-profiles`. يتم تعيينه للأسئلة والمجموعات في ورقة `survey` وللنموذج في ورقة `settings`.

### القيد

سمة قفل دقيقة يمكن تعيينها لملف تعريف والتحكم في سلوك القفل على مستوى السؤال أو المجموعة أو النموذج.

### غير مقفل

نموذج لا يحتوي على سمات قفل.