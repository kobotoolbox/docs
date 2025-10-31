# مرفقات البيانات الديناميكية
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/0c4cbe231491ab3ee9bd1e3a82967d30ac63e2c6/source/dynamic_data_attachment.md" class="reference">15 أكتوبر 2025</a>

يتيح لك الربط الديناميكي استخدام البيانات من **مشروع أساسي** داخل **مشاريع فرعية**، مما يبسط إدارة جمع البيانات الطولية. يشرح هذا المقال كيفية ربط البيانات ديناميكيًا بين مشاريع KoboToolbox.

<p class="note">
    <strong>ملاحظة:</strong> تعمل مرفقات البيانات الديناميكية بشكل مشابه لوظيفة <a href="https://support.kobotoolbox.org/ar/pull_data_kobotoolbox.html"><code>pulldata()</code></a> ولكنها تلغي الحاجة إلى ملفات CSV منفصلة، حيث تعمل البيانات من المشروع الأساسي المرتبط كمصدر للبيانات.
</p>

يمكنك استرداد مختلف **الإجابات غير الإعلامية** من مشروع أساسي وإجراء عمليات حسابية على هذه البيانات المرتبطة في مشروع فرعي. يمكن أن يكون هذا مفيدًا لاسترداد البيانات الأساسية أو معلومات الاتصال أو السجلات الصحية في الدراسات الجماعية، أو لتأكيد أو التحقق من البيانات التي تم جمعها مسبقًا.

نوصي باستخدام [XLSForm](edit_forms_excel.md) لإعداد مرفقات البيانات الديناميكية. للحصول على أمثلة للمشاريع الأساسية والفرعية، قم بتنزيل الملفات النموذجية [هنا](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) و[هنا](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx).

## الربط الديناميكي للمشاريع في XLSForm

يتطلب الربط الديناميكي للمشاريع **مشروعًا أساسيًا** ومشروعًا **فرعيًا** واحدًا على الأقل. لا يتطلب **المشروع الأساسي** أي تعديل عن XLSForm العادي. ومع ذلك، فإن إعداد **المشروع (المشاريع) الفرعية** يتضمن الخطوات التالية:
1. في ورقة عمل `survey` الخاصة بـ XLSForm، أضف صفًا وحدد نوع السؤال على أنه `xml-external`.
2. في عمود `name`، قدم اسمًا قصيرًا للنموذج الأساسي. يمكن أن يتكون هذا الاسم من أحرف الأبجدية اللاتينية والشرطات السفلية والأرقام.

**ورقة عمل survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. في جميع أنحاء النموذج، يمكنك استرداد القيم من المشروع الأساسي عن طريق إنشاء سؤال جديد وتضمين التعبير المناسب في عمود `calculation` (انظر الجدول [أدناه](https://support.kobotoolbox.org/ar/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). يمكنك استخدام أنواع الأسئلة التالية لاسترداد البيانات:
    - استخدم نوع السؤال **calculate** لاسترداد وتخزين القيم للاستخدام المستقبلي داخل النموذج أو مجموعة البيانات (على سبيل المثال، للحسابات أو تسميات الأسئلة الديناميكية).
    - استخدم أنواع الأسئلة **text** أو **integer** أو **decimal** أو **select_one** أو **select_multiple** لتضمين القيم المستردة كإجابات افتراضية في الحقول القابلة للتحرير. لن تؤدي البيانات المحررة في المشروع الفرعي إلى تغيير البيانات الأصلية في المشروع الأساسي.
  
**ورقة عمل survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | ما هو معرف المشارك؟ |  |
| integer | age | تأكيد عمر المشارك | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>ملاحظة:</strong> 
    لعرض البيانات المرتبطة دون السماح للمستخدمين بتحرير الحقل، استخدم سؤال <strong>calculate</strong> متبوعًا بسؤال <strong>note</strong> يعرض القيمة المحسوبة. بدلاً من ذلك، استخدم أسئلة <strong>text</strong> أو <strong>integer</strong> أو <strong>decimal</strong> أو <strong>select_one</strong> أو <strong>select_multiple</strong> مع تعيين عمود <code>read_only</code> على <code>TRUE</code>.
</p>

## بناء جملة الحساب لمرفقات البيانات الديناميكية

في عمود `calculation` للصف الذي سيتم فيه استرداد البيانات المرتبطة، قم بتضمين أحد التعبيرات في الجدول أدناه. تسمى هذه التعبيرات **XPaths**.

لكل تعبير في الجدول أدناه:

- `parent` هو الاسم الفريد المعين لـ **النموذج الأساسي** (على سبيل المثال، في سؤال `xml-external` الخاص بـ **النموذج الفرعي**).
- `parent_question` يشير إلى `name` السؤال من **النموذج الأساسي**.
- `child_question` يشير إلى `name` السؤال من **النموذج الفرعي**.
- `parent_index_question` هو السؤال المعرّف من **النموذج الأساسي** الذي يربطه بـ **النموذج الفرعي** (على سبيل المثال، المعرف الفريد، اسم المنظمة).
- `child_index_question` هو السؤال المعرّف من **النموذج الفرعي** الذي يربطه بـ **النموذج الأساسي** (على سبيل المثال، المعرف الفريد، اسم المنظمة).
- `parent_group` يشير إلى `name` المجموعة في **النموذج الأساسي** التي يوجد فيها `parent_question`.
- `parent_index_group` يشير إلى `name` المجموعة في **النموذج الأساسي** التي يوجد فيها `parent_index_question`.

| **XPath**    | **الوصف**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | يعيد العدد الإجمالي للصفوف في المشروع الأساسي. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | يعيد العدد الإجمالي للصفوف في المشروع الأساسي حيث `parent_question` (في `parent_group`) ليس فارغًا. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question]` | يعيد العدد الإجمالي للحالات التي تكون فيها قيمة `parent_question` (في `parent_group`) في المشروع الأساسي مساوية لقيمة `child_question` في المشروع الفرعي. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | يعيد قيمة `parent_question` (في `parent_group`) من المشروع الأساسي حيث `child_index_question` في المشروع الفرعي يساوي `parent_index_question` في المشروع الأساسي. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | نفس ما سبق، ولكنه يحدد أنه يجب إرجاع البيانات فقط من الحالة الأولى لـ `parent_index_question`، باستخدام الوسيطة `[position() = 1]`. يُستخدم في حالة وجود تكرارات محتملة في النموذج الأساسي. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | يعيد مجموع القيم من `parent_question` (في `parent_group`) من المشروع الأساسي. لاحظ أن `parent_question` يجب أن يكون رقميًا |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | يعيد القيمة القصوى المدخلة في `parent_question` (في `parent_group`) من المشروع الأساسي. لاحظ أن `parent_question` يجب أن يكون رقميًا.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | يعيد القيمة الدنيا المدخلة في `parent_question` (في `parent_group`) من المشروع الأساسي. لاحظ أن `parent_question` يجب أن يكون رقميًا.     |   


<p class="note">
    <strong>ملاحظة:</strong> إذا لم يكن السؤال الأساسي مضمنًا في أي مجموعة، فاحذف <code>parent_group</code> من التعبير
</p>

## إعداد المشاريع للربط الديناميكي

بمجرد إعداد نماذج XLSForm الخاصة بك، قم بتسجيل الدخول إلى حساب KoboToolbox الخاص بك واتبع الخطوات التالية:

1. قم بتحميل ونشر **المشروع الأساسي**، إذا لم يكن منشورًا بالفعل. تأكد من أن المشروع الأساسي يحتوي على إرسال واحد على الأقل.
2. قم بتمكين مشاركة البيانات للمشروع الأساسي:
    - في علامة التبويب **SETTINGS > Connect Projects** للمشروع الأساسي، قم بتبديل مفتاح **Data sharing** (معطل افتراضيًا) وانقر على **ACKNOWLEDGE AND CONTINUE** في نافذة التأكيد.
    - يتم مشاركة جميع البيانات افتراضيًا، ولكن يمكنك تقييد متغيرات معينة لمشاركتها مع المشاريع الفرعية بالنقر على "Select specific questions to share".

<p class="note">
    <strong>ملاحظة:</strong> إذا كانت المشاريع لها مالكون مختلفون، فيجب على مالك المشروع الأساسي <a href="managing_permissions.html">مشاركة المشروع</a> مع مالك المشروع الفرعي. الحد الأدنى من الأذونات المطلوبة لعمل مرفقات البيانات الديناميكية هي <strong>View form</strong> و <strong>View submissions</strong>. لاحظ أن هذا يسمح لمسؤولي المشروع الفرعي بعرض جميع بيانات المشروع الأساسي.
</p>

3. قم بتحميل ونشر **المشروع الفرعي**.
4. قم بربط المشروع الفرعي بالمشروع الأساسي:
    - في علامة التبويب **SETTINGS > Connect Projects** للمشروع الفرعي، انقر على "Select a different project to import data from." ستسمح لك قائمة منسدلة باختيار مشروع أساسي للربط.
    - أعد تسمية المشروع الأساسي المرتبط إلى اسم سؤال `xml-external` المحدد في XLSForm وانقر على **IMPORT**.
    - يمكنك بعد ذلك تحديد أسئلة معينة من المشروع الأساسي لمشاركتها مع المشروع الفرعي، أو تحديد جميع الأسئلة.
5. إذا أضفت حقولًا جديدة إلى النموذج الأساسي وترغب في استخدامها في المشروع الفرعي، فأعد استيراد المشروع الأساسي في إعدادات المشروع الفرعي.

<p class="note">
    <strong>ملاحظة:</strong> يمكن ربط النماذج معًا فقط إذا كانت على نفس خادم KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzU4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## الربط الديناميكي لنموذج بنفسه

من الممكن أن يكون المشروع الأساسي والفرعي نفس المشروع. الخطوات هي نفسها الموضحة أعلاه. تتضمن أمثلة حالات الاستخدام ما يلي:

- **المراقبة اليومية**: إذا تم استخدام نموذج لمسح نفس الشخص بمرور الوقت، يمكنك ربطه بنفسه لحساب الإرسالات السابقة. يمكن أن يسمح لك هذا بعرض رسالة (على سبيل المثال، "اكتملت المراقبة") بعد عدد معين من الإدخالات أو لإبلاغ جامع البيانات بعدد النماذج المقدمة، كما هو موضح في المثال أدناه.

**ورقة عمل survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | ما هو معرف المشارك؟ |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | تم مسح هذا المشارك ${count} مرة. | |
| survey | 

- **نموذج التسجيل**: من خلال ربط نموذج التسجيل بنفسه، يمكنك التحقق مما إذا كان المستخدم قد تم تسجيله بالفعل. يمكن أن يسمح لك هذا بإنشاء رسالة خطأ أو إضافة قيد إذا كان مسجلاً بالفعل، مما يمنع التسجيلات المكررة، كما هو موضح في المثال أدناه.

**ورقة عمل survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | ما هو رقم معرف العميل؟ |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | هذا العميل مسجل بالفعل. يرجى إغلاق هذا النموذج. | | ${count} > 0 |
| survey | 

## جمع وإدارة البيانات مع الربط الديناميكي

يمكن جمع البيانات للمشاريع المرتبطة ديناميكيًا باستخدام [تطبيق Android KoboCollect](kobocollect_on_android_latest.md) أو [نماذج Enketo الإلكترونية](data_through_webforms.md).

عند جمع البيانات، لاحظ ما يلي:

- يجب أن يحتوي المشروع الأساسي على إرسال واحد على الأقل حتى يعمل المشروع الفرعي بشكل صحيح.
- عند جمع البيانات عبر الإنترنت، هناك تأخير لمدة خمس دقائق في مزامنة بيانات المشروع الأساسي الجديدة مع المشروع الفرعي.
- في وضع عدم الاتصال، قم بتنزيل المشروع الفرعي بشكل متكرر لضمان مزامنة البيانات مع المشروع الأساسي.

<p class="note">
    <strong>ملاحظة:</strong> يمكنك <a href="https://support.kobotoolbox.org/ar/kobocollect_settings.html#form-management-settings">تكوين تطبيق Android KoboCollect</a> لتحديث بيانات المشروع الأساسي تلقائيًا عند توفر اتصال بالإنترنت. انتقل إلى <strong>Settings > Form management > Blank form update mode</strong> وحدد إما <strong>Previously downloaded forms only</strong> أو <strong>Exactly match server</strong>. يمكنك ضبط تكرار التنزيل التلقائي ليحدث كل 15 دقيقة، أو كل ساعة، أو كل ست ساعات، أو كل 24 ساعة. لاحظ أن تمكين هذا الإعداد قد يزيد من استهلاك البطارية.
</p>

## استكشاف الأخطاء وإصلاحها

<details>
<summary><strong>خطأ أو تعطل عند ربط النماذج</strong></summary>
لا يمكن لمرفقات البيانات الديناميكية الاتصال بمشروع أساسي فارغ. أضف إرسالًا واحدًا على الأقل إلى المشروع الأساسي أولاً، ثم اربط النماذج مرة أخرى.
</details>

<br>

<details>
<summary><strong>لا تظهر البيانات الأساسية في النموذج الفرعي</strong></summary>
تحقق من أن بناء جملة الحساب في النموذج الفرعي صحيح وأن الأسئلة ذات الصلة مشتركة في كلا المشروعين. إذا كان سؤالك الأساسي في مجموعة أسئلة، فتأكد من تضمين اسم المجموعة في تعبير XPath. لاحظ أن بيانات المشروع الأساسي الجديدة تستغرق ما يصل إلى خمس دقائق للمزامنة عندما تكون متصلاً بالإنترنت. إذا أضفت حقولًا جديدة إلى النموذج الأساسي وتريد استخدامها في المشروع الفرعي، فافتح إعدادات المشروع الفرعي، وأعد استيراد المشروع الأساسي، وأعد النشر.
</details>

<br>

<details>
<summary><strong>يتم تحميل النموذج الفرعي ببطء</strong></summary>
يمكن أن تؤدي مرفقات البيانات الديناميكية الكبيرة إلى إبطاء تحميل النموذج. شارك فقط الأسئلة التي يحتاجها النموذج الفرعي بدلاً من القائمة الكاملة للأسئلة، ثم أعد النشر وحاول مرة أخرى.
</details>

<br>

<details>
<summary><strong>لا يتم تحديث البيانات الديناميكية في KoboCollect</strong></summary>
إذا كنت تستخدم KoboCollect وتجمع البيانات دون اتصال بالإنترنت، فيجب أولاً إرسال البيانات إلى المشروع الأساسي ثم تنزيلها إلى جهاز جمع البيانات الخاص بك حتى يعمل مرفق البيانات الديناميكي. تتطلب كلتا الخطوتين اتصالاً بالإنترنت. يشبه تنزيل البيانات الأساسية تنزيل إصدار جديد من النموذج، ويمكن تكوين تطبيق KoboCollect <a href="https://support.kobotoolbox.org/ar/kobocollect_settings.html#form-management-settings">لتنزيل البيانات الجديدة تلقائيًا</a> بتكرار محدد. لا يُنصح بالاعتماد على مرفقات البيانات الديناميكية للبيانات التي يتم جمعها دون اتصال بالإنترنت خلال فترة زمنية قصيرة.
</details>

<br>

<details>
<summary><strong>مرفق البيانات الديناميكي لا يعمل داخل مجموعات الأسئلة</strong></summary>
لسحب البيانات الديناميكية من نموذج أساسي إلى نموذج فرعي يحتوي على مجموعات أسئلة، تأكد من أن سؤال الفهرس (على سبيل المثال، رقم التعريف) في النموذج الفرعي موجود في نفس المجموعة مثل الحساب للبيانات الديناميكية. راجع الملفات النموذجية <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> و <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> للحصول على مثال لمرفقات البيانات الديناميكية داخل المجموعات.
</details>

<br>

<details>
<summary><strong>خطأ في تقييم الحقول في KoboCollect</strong></summary>
إذا كان النموذج الأساسي الخاص بك يحتوي على إرسالات مكررة، فقد تتلقى رسالة خطأ في KoboCollect تفيد بـ "Error evaluating field / XPath evaluation: type mismatch /This field is repeated." لحل هذه المشكلة وسحب البيانات فقط من الإرسال الأول الذي يحتوي على قيمة فهرس معينة، استخدم الوسيطة <code>[position()=1]</code>، كما يلي:
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>