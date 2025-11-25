# تكامل KoboToolbox على monday.com
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/3d800e00d14000ecaa30ed97fcbf03a9feee65eb/source/kobotoolbox_monday_integration.md" class="reference">3 مايو 2024</a>

<p class="note">
تحدد هذه المقالة الإصدار المبكر من التكامل بين KoboToolbox
وMonday.com. كما هو الحال مع أي إصدار جديد، قد تكون هناك بعض الأخطاء غير المتوقعة. إذا
واجهتك مشكلات، يرجى <a
href="https://www.kobotoolbox.org/contact/?contact_reason=Monday.com%20integration"
class="reference">الاتصال بنا</a> فوراً حتى نتمكن من معالجتها.
</br>
⚠️ نوصي بإجراء اختبار دقيق قبل نشر هذا التكامل للمشاريع الحيوية. ⚠️
</p>


يتيح تكامل KoboToolbox للمستخدمين مزامنة بيانات مشاريعهم بسهولة من مشروع KoboToolbox إلى لوحة monday.com.

في بضع خطوات فقط يمكنك إعداد التكامل لنسخ عمليات إرسال البيانات المستلمة في KoboToolbox تلقائياً إلى أي من لوحات monday.com الخاصة بك. يقلل هذا التكامل بشكل كبير من العمل اليدوي المتضمن في نسخ ولصق بيانات المشروع من KoboToolbox إلى monday.com.

## الخصائص

- عملية مبسطة لربط مشاريع KoboToolbox بلوحات monday.com.
- سهولة ربط حقول monday.com بأسئلة KoboToolbox باستخدام أي لغة تسمية محددة في النموذج.
- مزامنة فورية لعمليات الإرسال المنشأة حديثاً لإنشاء عناصر جديدة.

## التثبيت والاستخدام لأول مرة

### قبل تثبيت التكامل

1. أنشئ حساباً على KoboToolbox إذا لم يكن لديك حساب بالفعل. تعرف على المزيد حول
    [إنشاء حساب](creating_account.md).
2. جهز لوحة monday.com تعكس بنية مشروع KoboToolbox الخاص بك بحيث يتم تمثيل جميع الحقول من مشروع KoboToolbox الخاص بك على
    لوحة monday.com.
3. أثناء إعداد التكامل، ستحتاج إلى
    مصادقة الوصول إلى حسابك من خلال توفير مفتاح API الخاص بـ KoboToolbox.
   تعرف على كيفية الحصول على [مفتاح API](api.md).

<p class="note">
  **ملاحظة:** مفتاح API هو معرف فريد يستخدم للمصادقة. في KoboToolbox، يشار إليه باسم **مفتاح API**. في monday.com، يشار إليه باسم **رمز API**.
</p>

### التثبيت

1. ثبت تكامل KoboToolbox من
    [سوق تطبيقات monday.com](https://monday.com/marketplace).
2. بمجرد التثبيت، انتقل إلى لوحتك المعدة مسبقاً لإعداد
    التكامل.

<p class="note">
    **ملاحظة 1:** يمكن إنشاء وصفة تكامل KoboToolbox واحدة فقط لكل لوحة monday.
    **ملاحظة 2:** الشخص الذي قام بتثبيت الوصفة فقط يمكنه تعديلها، جميع أعضاء اللوحة الآخرين يمكنهم فتحها في وضع القراءة فقط.
</p>

### الاستخدام لأول مرة

1. انتقل إلى قائمة **Integration** في الأعلى على اليمين.
    ![monday-board-integrate](/images/kobotoolbox_monday_integration/monday-board-integrate.png)
2. ابحث عن **KoboToolbox** في مركز التكاملات.
    ![app-marketplace](/images/kobotoolbox_monday_integration/find-integration.png)
3. انقر على تكامل KoboToolbox واختر الوصفة المضمنة.
    ![kobo-integration](/images/kobotoolbox_monday_integration/choose-recipe.png)
4. صرح بتطبيق KoboToolbox:
    - أدخل عنوان URL لخادم KoboToolbox حيث أنشأت حسابك. بالنسبة لخادم KoboToolbox العالمي، استخدم عنوان URL للخادم [https://kf.kobotoolbox.org](https://kf.kobotoolbox.org). بالنسبة لخادم KoboToolbox في الاتحاد الأوروبي، استخدم عنوان URL للخادم [https://eu.kobotoolbox.org](https://eu.kobotoolbox.org).
    - أدخل مفتاح API الخاص بـ KoboToolbox في حقل "Kobo API token"
    ![provide-api-key](/images/kobotoolbox_monday_integration/provide-api-key.png)

<p class="note">
    **ملاحظة:** لتغيير مفتاح API بعد إعداد وصفة التكامل، يجب إعادة تثبيت تطبيق تكامل KoboToolbox بالكامل.
    </p>

5. لتكوين الوصفة، قم بإعداد المعاملات التالية:
    - اختر مشروع KoboToolbox المناسب الذي تريد ربطه بلوحة monday.com الخاصة بك من القائمة المنسدلة. المشاريع المنشورة فقط متاحة للاختيار.
    - اختر لغة التسمية من القائمة المنسدلة. إذا كان نموذجك يحتوي على أكثر
        من لغة واحدة، حدد اللغة التي يجب استخدامها لربط الأسئلة
        بالأعمدة. سيتم عرض اللغة المحددة فقط لربط
        أسئلة KoboToolbox بأعمدة monday.com. ستستخدم البيانات المعروضة في
        لوحة monday.com دائماً بنية بيانات XML الأساسية
        بدلاً من تسميات الاختيار الواحد أو الاختيار المتعدد المترجمة.
    - انقر على **Item** لإعداد ربط الأسئلة بالأعمدة.
        ![dynamic-linking](/images/kobotoolbox_monday_integration/item-mapping.png)
6. عند إكمال تكوين الوصفة، انقر على زر **Add to Board**.
    ![recipe](/images/kobotoolbox_monday_integration/recipe-config.png)
7. بعد إكمال إعداد التكامل، يجب عليك تكوين خدمات REST على KoboToolbox لمزامنة بيانات مشروعك تلقائياً مع لوحة monday.com. لتكوين خدمات REST على KoboToolbox:
    - انسخ رابط التكامل من إشعار إعداد التكامل أو من
        الوصف على لوحة monday.com الخاصة بك.\
        ![webhook-url](/images/kobotoolbox_monday_integration/description-link.png)
    - سجل الدخول إلى حساب KoboToolbox الخاص بك.
    - انتقل إلى المشروع الذي ترغب في ربطه. افتح علامة التبويب **SETTINGS**، ثم اختر REST
        Services، وانقر على زر **REGISTER A NEW SERVICE**.\
        ![create-rest-service](/images/kobotoolbox_monday_integration/create-rest-service.png)
    - أدخل "monday.com integration" كاسم الخدمة وأدخل رابط التكامل في حقل "Endpoint URL".
    - في قسم "Custom HTTP Headers"، أدخل القيمة "webhook-auth" في
        حقل "Name" وأدخل مفتاح API الخاص بـ KoboToolbox في حقل "Value".\
        ![rest-service-modal](/images/kobotoolbox_monday_integration/rest-service-modal.png)
    - انقر على زر **SAVE**.
8. انتهى الأمر! سيتم إضافة كل عملية إرسال جديدة إلى مشروع KoboToolbox الخاص بك
    تلقائياً إلى لوحة monday.com الخاصة بك وفقاً لتكوين الوصفة الخاص بك.\

    ![kobo-monday-data](/images/kobotoolbox_monday_integration/kobo-monday-data.png)

    ### ملاحظات مهمة
    1. أي تحديثات يتم إجراؤها على نموذج أو عملية إرسال فردية في مشروع KoboToolbox
    الذي تمت إضافته بالفعل إلى لوحة monday.com الخاصة بك لن يتم تحديثها تلقائياً
    على لوحة monday.com الخاصة بك. التغييرات مثل إزالة أو إعادة تسمية سؤال،
    تغيير تسلسل هرمي للمجموعة، تغيير مجموعة إلى مجموعة متكررة، أو تعديل
    التسميات في نموذج KoboToolbox لن تؤثر على العناصر الموجودة على لوحة monday.com
    الخاصة بك.
    2. الموقع غير مدعوم تلقائياً في ربط الحقول الديناميكية. لنقل موقع أو إحداثيات من KoboToolbox إلى عمود monday.com:
      - أنشئ عمودين على لوحة monday.com الخاصة بك لملء بيانات الموقع: عمود واحد من نوع Text وعمود ثانٍ من نوع Location. من المهم تسميتهما بشكل متطابق.
      - في ربط الحقول الديناميكية، اربط موقع KoboToolbox بعمود monday.com من نوع Text. - لن يظهر عمود نوع Location في الربط الديناميكي.
      - سيتم ملء عملية إرسال موقع KoboToolbox تلقائياً في عمود monday.com من نوع Location.
    3. عمود الملف غير مدعوم تلقائياً في ربط الحقول الديناميكية. لنقل الملفات من KoboToolbox إلى monday.com:
      - أضف عمود ملف إلى لوحة monday.com وأعطه نفس الاسم المستخدم لحقل الملف في مشروع KoboToolbox الخاص بك. يجب استخدام نفس اسم عمود الملف في كل من monday.com وKoboToolbox.
      - إذا لم تكن قد ثبت وصفة التكامل، أكمل عملية التثبيت. بمجرد إكمال التثبيت، انتقل إلى مركز التكاملات، وافتح الوصفة الموجودة، وانقر على زر **Update automation** لتطبيق أحدث التغييرات الوظيفية.
      - لا حاجة لتغييرات تكوين أخرى. سيتم الآن نقل الملفات تلقائياً من مشروع KoboToolbox إلى العمود المناسب على لوحة monday.com الخاصة بك بناءً على اسم العمود.
    4. لضمان الأداء العالي في لوحات monday.com، تحدد monday.com عدد الأعمدة لكل لوحة: 200 عمود للحسابات غير المؤسسية و300 عمود للحسابات المؤسسية.



## الأسئلة الشائعة

**ما هي خدمات REST؟**

مزيد من المعلومات حول خدمات REST متاحة في
[مقالة الدعم هذه](rest_services.md).

**ما هو ربط الحقول الديناميكية؟**

ربط الحقول الديناميكية هو إقران الحقول الممثلة على لوحة monday.com
مع الأسئلة المناسبة من مشروع KoboToolbox.

**ماذا يحدث إذا قمت بتغيير بياناتي على حساب Kobo؟**

أي تحديثات يتم إجراؤها على نموذج أو عملية إرسال فردية في مشروع KoboToolbox الخاص بك والتي
تم إرسالها بالفعل إلى لوحة monday.com لن تتم مزامنتها تلقائياً.

**ماذا يحدث إذا قمت بتغيير بياناتي على لوحة monday.com؟**

التغييرات التي يتم إجراؤها على البيانات الممثلة على لوحة monday.com لن تنعكس
في مشروع KoboToolbox.

**ماذا يحدث إذا احتجت لاحقاً إلى تغيير اللغة؟**

يؤثر اختيار اللغة فقط على عرض ربط الحقول الديناميكية لتكوين وصفة التكامل. لن تتم ترجمة بيانات اللوحة.

**ماذا يحدث إذا قمت بحذف المشروع على KoboToolbox؟**

إذا تم حذف مشروع في KoboToolbox، فلن يعمل التكامل بعد الآن حتى يتم تحديث
وصفة التكامل بمشروع جديد.

**ما هي "أنواع الأعمدة"؟**

"نوع العمود" في monday.com هو نوع السؤال في KoboToolbox.

**ما أنواع الأسئلة من KoboToolbox التي يمكن نقلها إلى monday.com؟**

جميع [أنواع الأسئلة](question_types.md) باستثناء External XML مدعومة من قبل monday.com. إذا
لم تتمكن من العثور على نوع العمود المناسب على لوحة monday.com، استخدم عمود من نوع Text.

لنقل أنواع الأسئلة [Point](gps_questions.md) و[Area](gps_questions.md) في KoboToolbox إلى نوع عمود Location على لوحة monday.com، استخدم النهج الموضح في [الملاحظة المهمة رقم 2](#ملاحظات-مهمة). إذا لم يكن من الضروري نقل البيانات إلى عمود Location، فيمكن استخدام عمود واحد من نوع Text بدون إضافات.

**كيف يتم نقل أسئلة الاختيار المتعدد في KoboToolbox إلى monday.com؟**

بالنسبة لأسئلة [الاختيار المتعدد](select_one_and_select_many.md)، يجب استخدام عمود من نوع Drop-down على
لوحة monday.com لنقل جميع الخيارات المحددة بشكل صحيح إلى
اللوحة.

**كيف يتم نقل أسئلة الاختيار الواحد في KoboToolbox إلى monday.com؟**

بالنسبة لأسئلة [الاختيار الواحد](select_one_and_select_many.md)، استخدم عمود من نوع Status (محدود بـ 40 خيار تسمية)، أو Drop-down، أو Text لنقل الخيار المحدد بشكل صحيح إلى اللوحة.

**هل يمكنني مزامنة أكثر من مشروع KoboToolbox واحد مع لوحة monday الخاصة بي؟**

لا. يمكن إنشاء وصفة تكامل KoboToolbox واحدة فقط لكل لوحة.
وجود أكثر من وصفة واحدة سيؤدي إلى خطأ في الخادم.

**لماذا لا يمكنني تغيير وصفة أنشأها عضو آخر في لوحة monday.com؟**

عضو اللوحة الذي أنشأ الوصفة فقط يمكنه تعديلها. جميع أعضاء اللوحة الآخرين يمكنهم فتحها في وضع القراءة فقط.