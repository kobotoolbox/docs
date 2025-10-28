# البدء مع KoboCollect
<a href="../kobocollect_on_android_latest.html">Read in English</a> | <a href="../fr/kobocollect_on_android_latest.html">Lire en français</a> | <a href="../es/kobocollect_on_android_latest.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/562abda7896f1c80c1863f158d61432fa915a52f/source/kobocollect_on_android_latest.md" class="reference">19 سبتمبر 2025</a>

<iframe src="https://www.youtube.com/embed/qC2Bz8jZkIM?si=xSyTOxOMR6nE8tum" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect هو تطبيق KoboToolbox مجاني ومفتوح المصدر مصمم لجمع البيانات على أجهزة Android المحمولة. تجعل إمكانياته للعمل دون اتصال بالإنترنت وتوافقه مع معظم أجهزة Android منه مثالياً للعمل الميداني.

قبل استخدام KoboCollect، يجب عليك [إنشاء حساب KoboToolbox](https://support.kobotoolbox.org/creating_account.html) على موقع KoboToolbox و[نشر نماذج جمع البيانات](https://support.kobotoolbox.org/quick_start.html).

<p class="note">
    يغطي هذا المقال كيفية الاتصال بـ KoboCollect لجمع البيانات. لمعرفة المزيد حول تكوين إعدادات KoboCollect وجمع البيانات باستخدام التطبيق، راجع <a href="https://support.kobotoolbox.org/kobocollect_settings.html">تخصيص إعدادات KoboCollect</a> و<a href="https://support.kobotoolbox.org/data_collection_kobocollect.html">جمع البيانات باستخدام KoboCollect</a>.
</p>

## تثبيت تطبيق KoboCollect

يمكن تنزيل تطبيق KoboCollect من [متجر Google Play](https://play.google.com/store/apps/details?id=org.koboc.collect.android) لأجهزة Android التي تعمل بالإصدار 5 أو أحدث.

<p class="note">
    <strong>ملاحظة:</strong> نوصي باستخدام أحدث إصدار من التطبيق (v2025.2)، حيث يتضمن ميزات وإصلاحات للأخطاء غير متوفرة في الإصدارات الأقدم.
</p>

## إعداد تطبيق KoboCollect

لجمع البيانات باستخدام KoboCollect، يجب عليك تكوين تطبيق KoboCollect على جهازك المحمول للاتصال بخادم KoboToolbox. يتيح لك ذلك تنزيل النماذج المنشورة من KoboToolbox وإرسال البيانات المجمعة مرة أخرى إلى الخادم.

للاتصال بـ KoboCollect بخادم KoboToolbox، ستحتاج إلى **رابط KoboCollect** و**اسم المستخدم** و**كلمة المرور**. بعد الإعداد اليدوي الأولي، يمكنك [إنشاء رمز QR](https://support.kobotoolbox.org/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) لتكوين الأجهزة الأخرى.

<p class="note">
    <strong>ملاحظة:</strong> في تطبيق KoboCollect، تُسمى حسابات المستخدمين <strong>المشاريع</strong>.
</p>

### إعداد KoboCollect يدوياً
لإعداد KoboCollect يدوياً، ستحتاج إلى تحديد **رابط KoboCollect** الخاص بك. هذا الرابط خاص بـ KoboCollect ويختلف عن الرابط المستخدم للوصول إلى حساب KoboToolbox الخاص بك.

يعتمد رابط KoboCollect الخاص بك على خادم حسابك:

| **خادم KoboToolbox**    | **رابط KoboCollect**                     |
| :----------------- | :--------------------------------------------- |
| الخادم العالمي لـ KoboToolbox               | https://kc.kobotoolbox.org/ |
| خادم الاتحاد الأوروبي لـ KoboToolbox      | https://kc-eu.kobotoolbox.org/ |
| الخادم الخاص           | فريد لكل منظمة            |

يمكنك أيضاً العثور على رابط KoboCollect على منصة KoboToolbox. انتقل إلى علامة تبويب **النموذج** في مشروعك واختر **تطبيق Android** من القائمة المنسدلة **جمع البيانات**. سيتم إدراج رابط KoboCollect في الخطوة 3.

![Select Android app in browser](images/kobocollect_on_android_latest/select_android_app_in_browser.png)

بمجرد تحديد رابط KoboCollect الخاص بك، اتبع هذه الخطوات لإعداد اتصال الخادم:

1. افتح تطبيق KoboCollect.
2. اختر **إدخال تفاصيل المشروع يدوياً**.
3. أدخل **رابط KoboCollect** و**اسم المستخدم** و**كلمة المرور**.
4. انقر على **إضافة**.
5. عند اكتمال التكوين، ستظهر القائمة الرئيسية.

### إعداد KoboCollect باستخدام رمز QR

يؤدي استخدام رمز QR إلى تكوين KoboCollect بكفاءة على أجهزة متعددة **بنفس إعدادات الخادم** (رابط KoboCollect واسم المستخدم وكلمة المرور و<a href="https://support.kobotoolbox.org/kobocollect_settings.html">إعدادات تكوين المشروع</a>). يمكن أن يكون هذا مفيداً لتجنب تكرار الخطوات اليدوية أو لتكوين أجهزة جامعي البيانات دون مشاركة كلمات مرور الحساب.

<p class="note">
    <strong>ملاحظة:</strong> لاستخدام طريقة رمز QR، يجب عليك أولاً تكوين جهاز واحد يدوياً ثم نسخ رمز QR المُنشأ إلى الأجهزة الأخرى.
</p>

للوصول إلى رمز QR الخاص بك:

1. انتقل إلى قائمة **المشاريع** واختر المشروع الذي تريد نسخه.
2. انقر على **الإعدادات**.
3. اختر **إدارة المشروع**.
4. انقر على **إعادة التكوين باستخدام رمز QR**.
5. اختر **رمز QR**. سيظهر رمز QR الخاص بك على الشاشة.
6. **التقط لقطة شاشة** لرمز QR لمشاركته لإعداد الأجهزة الأخرى. يمكنك أيضاً العودة إلى هذه القائمة في أي وقت للوصول إلى رمز QR مرة أخرى.

لتكوين الأجهزة الأخرى باستخدام رمز QR:

1. افتح **KoboCollect** على الجهاز الذي تريد إعداده.
2. انقر على **التكوين باستخدام رمز QR**.
3. امسح رمز QR باستخدام كاميرا الجهاز، أو انقر على <i class="k-icon-more"></i> **النقاط الثلاث** في الزاوية العلوية اليمنى واختر **استيراد رمز QR** لاستخدام لقطة شاشة محفوظة على جهازك.

إذا نجح الإعداد، سيتم تكوين التطبيق تلقائياً.

<p class="note">
    <strong>ملاحظة:</strong> يحتوي رمز QR على بيانات اعتماد حسابك، بما في ذلك كلمة المرور الخاصة بك. سيكون لأي شخص يمسحه نفس أذونات الوصول الخاصة بالحساب الذي تم إنشاؤه منه. إذا كنت تريد فقط أن يقوم شخص ما بجمع البيانات (على سبيل المثال، جامع بيانات)، <strong>تأكد من أن الحساب المستخدم لإنشاء رمز QR لا يحتوي على أذونات لعرض البيانات أو تحريرها أو حذفها.</strong> للحفاظ على أمان بياناتك، تجنب مشاركة رموز QR من الحسابات ذات الوصول الكامل.
</p>

### إعداد مشاريع متعددة في KoboCollect

يمكن للمستخدمين ربط حسابات KoboToolbox متعددة والتبديل بسهولة بين المشاريع المختلفة داخل نفس تطبيق KoboCollect، بغض النظر عما إذا كانت على نفس الخادم أو على خوادم مختلفة.

لإعداد مشاريع إضافية في KoboCollect:

1. انقر على **أيقونة المشروع** الموجودة في الزاوية العلوية اليمنى.
2. في قائمة **المشاريع**، انقر على **إضافة مشروع**.
3. قم بإعداد مشروع جديد باستخدام الطريقة اليدوية أو عن طريق مسح رمز QR.
4. عند اكتمال التكوين، ستظهر القائمة الرئيسية.
5. انقر على **أيقونة المشروع** لفتح القائمة. يجب أن يكون كلا المشروعين مرئيين الآن.

يمكن إضافة مشاريع إضافية عن طريق تكرار نفس العملية. سيتم إدراج المشروع النشط أولاً في قائمة **المشاريع**. للتبديل إلى مشروع مختلف، ما عليك سوى النقر على أيقونته.

<p class="note">
    لمعرفة المزيد حول تغيير كيفية عرض المشاريع لسهولة التعرف عليها والتبديل بينها، راجع <a href="https://support.kobotoolbox.org/kobocollect_settings.html#project-display-settings">إعدادات عرض المشروع</a>.
</p>

### إعداد مشروع في KoboCollect بدون مصادقة

من الممكن أيضاً الوصول إلى المشاريع في KoboCollect بدون كلمة مرور. يعد هذا مفيداً للمشاريع التي تضم العديد من جامعي البيانات، حيث يتجنب الحاجة إلى إنشاء حسابات فردية أو مشاركة بيانات الاعتماد.

<p class="note">
    <strong>ملاحظة:</strong> يتطلب هذا النهج تمكين "السماح بالإرسالات إلى هذا النموذج بدون اسم مستخدم وكلمة مرور" لنماذجك. لمعرفة المزيد حول إعدادات المشاركة على مستوى المشروع، راجع <a href="https://support.kobotoolbox.org/project_sharing_settings.html">مشاركة المشاريع باستخدام إعدادات مستوى المشروع</a>.
</p>

للاتصال بـ KoboCollect بدون مصادقة:
1. قم بتمكين "السماح بالإرسالات إلى هذا النموذج بدون اسم مستخدم وكلمة مرور" لنماذجك.
2. [اختياري] أنشئ حساب KoboToolbox مخصصاً لجامعي البيانات و[شارك نماذجك](https://support.kobotoolbox.org/managing_permissions.html) مع هذا الحساب.
3. اتصل بـ KoboCollect باستخدام بيانات الاعتماد التالية:
    - **الرابط**: رابط KoboCollect متبوعاً باسم مستخدم الحساب (`https://[kobocollect_url]/[username]`)
    - **اسم المستخدم**: (اتركه فارغاً)
    - **كلمة المرور**: (اتركها فارغة)

يتيح هذا النهج للمستخدمين تنزيل وإرسال البيانات إلى أي نماذج مشتركة مع `username` التي لا [تتطلب مصادقة](https://support.kobotoolbox.org/project_sharing_settings.html).

للتمييز بين جامعي البيانات وتتبع الإرسالات، يمكنك أن تطلب من جامعي البيانات إدخال اسم مستخدم مخصص ورقم هاتف وعنوان بريد إلكتروني في [إعدادات هوية المستخدم والجهاز](https://support.kobotoolbox.org/kobocollect_settings.html#user-and-device-identity-settings).

<p class="note">
    <strong>ملاحظة:</strong> يمكن أن يكون هذا النهج مفيداً عندما يستخدم حسابك <a href="https://support.kobotoolbox.org/two_factor_authentication.html">المصادقة الثنائية</a>، حيث لن تتمكن من تنزيل النماذج أو إرسال البيانات باستخدام الطريقة العادية.
</p>