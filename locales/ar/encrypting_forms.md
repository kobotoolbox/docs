# تشفير النماذج
<a href="../encrypting_forms.html">Read in English</a> | <a href="../fr/encrypting_forms.html">Lire en français</a> | <a href="../es/encrypting_forms.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/179faeb3c5a17b69406b0243ab9c22f7ca86aa44/source/encrypting_forms.md" class="reference">4 نوفمبر 2024</a>

_هذا الإجراء تقني للغاية وموجه للمستخدمين الذين لديهم خبرة في التعليمات التقنية المتقدمة ويتطلب اهتمامًا دقيقًا بالتفاصيل._

تعمل النماذج المشفرة عن طريق تشفير البيانات على الهاتف في اللحظة التي يتم فيها حفظها. يتم إرسال البيانات إلى KoboToolbox مشفرة ولا يمكن الوصول إليها بالكامل من قبل أي شخص لا يمتلك المفتاح الخاص. في هذه الحالة، يعمل KoboToolbox ببساطة كخزانة تخزين لملفاتك المشفرة - مكان لتحميلها ثم تنزيلها لاحقًا لفك التشفير محليًا
([باستخدام ODK Briefcase](http://blog.formhub.org/2013/06/27/formhub-supports-odk-briefcase/)).
نظرًا لأن إرسالات النماذج مشفرة، فهذا يعني أن أي شيء يتطلب الوصول إلى البيانات مثل عرض الخريطة أو تصدير البيانات لن يعمل داخل KoboToolbox. يجعل المستوى الإضافي من الأمان استخدام KoboToolbox بطريقة لجمع البيانات الحساسة مع تلبية بروتوكولات حماية البيانات المعينة ممكنًا.

## كيف يعمل

يدعم KoboCollect القدرة على تشفير محتوى النموذج في اللحظة التي يتم فيها وضع علامة عليه كمكتمل وجاهز للإرسال على الهاتف. للاستفادة من ذلك يتطلب استخدام مفتاح تشفير عام تقوم بتضمينه في XLSForm ومفتاح خاص (لا تشاركه أبدًا) يستخدمه ODK Briefcase لفك تشفير البيانات محليًا بعد تنزيلها من KoboToolbox. يُستخدم المفتاح العام لتشفير البيانات بينما يفك المفتاح الخاص تشفيرها. فقط الشخص الذي لديه المفتاح الخاص يمكنه فك تشفير البيانات المشفرة بالمفتاح العام. لفهم المزيد حول البنية التحتية للمفاتيح العامة والخاصة
[انظر هنا](https://en.wikipedia.org/wiki/Public-key_cryptography).

## كيفية تشفير نماذج XLS

1. أنشئ نموذجك في KoboToolbox كالمعتاد. قم بتنزيل النموذج من قائمة المسودات كملف XLS.

2. في الملف الذي تم تنزيله، انتقل إلى ورقة 'settings'.

3. أضف عمودًا _submission_url_ واكتب
   `https://kc.kobotoolbox.org/submission` أو
   `https://kc-eu.kobotoolbox.org/submission` (حسب
   الخادم الذي تستخدمه).

5. أضف عمودًا آخر _public_key_ (أي base64RsaPublicKey). الصق مفتاحك العام المتوافق.

    (يرجى الاطلاع على الصورة أدناه للمرجع)

    ![image](/images/encrypting_forms/column.png)

6. قم بتحميل ملف XLS مرة أخرى إلى KoboToolbox. يمكنك إما استيراده مرة أخرى إلى قائمة مسودات النماذج ثم نشره كمشروع استبيان جديد، أو استيراده مباشرة إلى قائمة المشاريع المنشورة. بمجرد النشر، يجب أن ترى تسمية بنص "مشفر" بجوار اسم نموذجك.

<p class="note">
  يرجى ملاحظة أن عنوان URL للمستخدم المصادق عليه لم يعد يتضمن **yourusername** وفقًا للتحديثات الأخيرة.
</p>

## كيفية فك تشفير النماذج

يُستخدم ODK Briefcase لتنزيل الملفات المشفرة من KoboToolbox وفك تشفيرها محليًا على جهاز الكمبيوتر الخاص بك باستخدام مفتاح خاص يضمن الوصول الفردي إلى البيانات. لكي يكون فك التشفير ناجحًا مع ODK Briefcase، تأكد من تنزيل وتثبيت _Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 6_ من
[موقع تنزيل Java](https://www.oracle.com/java/technologies/javase-jce-all-downloads.html).
هذا مطلوب لنجاح فك التشفير.

### لتثبيت JCE:

1. قم بفك ضغط الأرشيف المضغوط الذي تم تنزيله

2. انتقل إلى شجرة الدليل المستخرجة وانسخ ملفات local_policy.jar و US_export_policy.jar إلى دليل lib\security

3. الصق هذه الملفات داخل دليل التثبيت لبيئة تشغيل Java (JRE) على جهاز الكمبيوتر الخاص بك، مع استبدال الإصدارات السابقة من هذه الملفات.
    - على **Windows**، عادةً ما يتم تثبيت JRE هنا: C:\Program Files\Java\jre7\lib\security
    - على **OSX** الموقع هو /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/security

### لفك تشفير نماذجك:

1. قم بتنزيل وفتح [ODK Briefcase](https://docs.getodk.org/briefcase-intro/).

2. حدد **موقع التخزين** ضمن علامة التبويب **الإعدادات**.

3. افتح علامة التبويب **Pull** وانقر على **Configure**.  
   ![image](/images/encrypting_forms/configure.png)

4. ثم أدخل ما يلي:

    - `https://kc.kobotoolbox.org` أو
      `https://kc-eu.kobotoolbox.org` (حسب الخادم الذي تستخدمه)
    - اسم المستخدم الخاص بك
    - كلمة المرور الخاصة بك
    - اضغط على **Connect** عند الانتهاء  
      ![image](/images/encrypting_forms/connect.png)

<p class="note">
  يرجى ملاحظة أن عناوين URL للخادم أعلاه لم تعد بحاجة إلى تضمين **yourusername** وفقًا للتحديثات الأخيرة.
</p>

5. يتم عرض قائمة بالمشاريع. حدد مشروعًا ترغب في سحبه واضغط على **Pull**. ستتلقى رسالة **Success** ضمن **Pull Status**.

6. الآن انتقل إلى علامة التبويب **Export**.

7. اضغط على **Edit Default Configuration** للتأكد من أن لديك **مفتاح PEM الخاص** في **موقع ملف PEM**.  
   ![image](/images/encrypting_forms/private_key.png)  
   إذا لم يكن موجودًا، حدد **مفتاح PEM الخاص** من المجلد الذي قمت بتأمينه بشكل آمن. (_ملاحظة: سترى أيضًا جميع المشاريع هنا التي تم سحبها بنجاح._)

8. الآن حدد المشروع الذي ترغب في تصديره واضغط على **Export**.

9. يتم تصدير البيانات كملف CSV، يمكنك الآن عرض البيانات غير المشفرة.

## إنشاء مفاتيح تشفير RSA

لإنشاء أزواج المفاتيح العامة والخاصة RSA، يمكنك استخدام حزمة برامج OpenSSL، والتي تأتي مثبتة مسبقًا على OSX و Linux. على Windows يجب عليك تنزيل وتثبيت حزمة برامج OpenSSL من
[هذا الموقع](http://slproweb.com/products/Win32OpenSSL.md). (_ملاحظة: قم بتثبيت Win64 OpenSSL v1.1.1c في **C**: بدلاً من الموقع الافتراضي **C:\Program Files**_)

### كيفية إنشاء مفتاح RSA للاستخدام مع النماذج المشفرة على KoboToolbox

_ملاحظة: نوصي بشدة باستخدام OpenSSL كما هو موثق أدناه لإنشاء زوج المفاتيح العامة/الخاصة حيث قد لا تدعم البرامج الطرق الأخرى._

1. افتح نافذة 'cmd' في Windows.

2. اكتب الأمر التالي: `cd C:\OpenSSL-Win32\bin` للتغيير إلى دليل /bin في دليل OpenSSL.

    ![image](/images/encrypting_forms/openssl_1.png)

3. أنشئ مفتاحًا خاصًا بحجم 2048 بت واكتبه في ملف **MyPrivateKey.pem** عن طريق كتابة الأمر التالي، ثم اضغط على **Enter**:
   `openssl genpkey -out MyPrivateKey.pem -outform PEM -algorithm RSA -pkeyopt rsa_keygen_bits:2048`

    ![image](/images/encrypting_forms/openssl_2.png)

4. ثم، استخرج المفتاح العام للمفتاح الخاص أعلاه. اكتب الأمر التالي ثم اضغط على **Enter**:
   `openssl rsa -in MyPrivateKey.pem -inform PEM -out MyPublicKey.pem -outform PEM -pubout`

    ![image](/images/encrypting_forms/openssl_3.png)

5. لقد أنشأت الآن ملفين وهما:

    - **MyPrivateKey.pem** - مفتاحك الخاص الذي تحتاج إلى نقله إلى موقع آمن.
    - **MyPublicKey.pem** - مفتاحك العام، الذي يمكنك مشاركته مع أي شخص تريد مشاركة المعلومات معه بشكل آمن

6. افتح **MyPublicKey.pem** باستخدام Notepad أو محرر نصوص آخر، مفتاحك العام هو السلسلة الطويلة جدًا من الأحرف غير المنقطعة،

`مثال:Tjhfur1K9+BRQ2USezIPbtyahbfuNqviI5Suhm8maA3JoELRHj9psjf/oNWoG87aFtKNbLrRaCEDP oFMDC9NEzWlv5L49BygeieMu/wg/rtMT0M0kgDbKxw5weJJgyb9P41aMsrqAAAAB3NzaC1yc2EAAAADAQAB AAABAQDfNoFX7bh3bfdW6lGfDht1Ea8PUBLKYjugbHN5jS7j5fHV6dexM+kzvITVgoyjhhKPXeCbaT62vD/ saTqJFXJzlysnZ24fqxNkjreO5K5EQ9c3ggwqML06+AKrFUSP5jpnyJJH8btNwKl6D5pG4ZseHwDUKzZtae xtPTNQz67kdYIKdtCkCsQHVsy4xvy/A0jzfK3xyOkG6j+L`

هذه السلسلة هي ما ستحتاج إلى لصقه ضمن حقل public_key في ورقة الإعدادات الخاصة بك في ملف XLS الخاص بك.

**مهم**: تأكد من لصق سلسلة المفتاح العام فقط دون مسافات فارغة أو فواصل أسطر!

**MyPrivateKey.pem** هو الملف الذي ستستخدمه عند تصدير الإرسالات باستخدام ODK Briefcase.

ملاحظة: عند محاولة تحرير نموذج تم تشفيره، تتلقى رسالة "لا يمكن تحرير هذا النموذج بمجرد وضع علامة عليه كنهائي. قد يكون مشفرًا".