# دليل البدء السريع
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/72921cfe4ac9cd4ad75c1d57664c89478f26c71a/source/quick_start.md" class="reference">30 سبتمبر 2025</a>

يقدم هذا المقال دليلاً سريعاً للبدء في استخدام KoboToolbox. يشرح كيفية إنشاء حساب، وبناء ونشر نموذج، والبدء في جمع البيانات.

<iframe src="https://www.youtube.com/embed/CYJ-Ob_7Ql8?si=SDjFjZF4zQBE-thP" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>



## إنشاء حساب وتسجيل الدخول
للبدء، انتقل إلى [صفحة التسجيل](https://www.kobotoolbox.org/sign-up/) وأنشئ حساباً على أحد خوادمنا العامة. يقوم معظم المستخدمين بالتسجيل للحصول على حساب على [Le serveur KoboToolbox mondial](https://kf.kobotoolbox.org/). يمكن للمستخدمين والمؤسسات التي تتطلب أو تفضل استضافة البيانات في الاتحاد الأوروبي التسجيل للحصول على حساب على [Le serveur KoboToolbox Union européenne](https://eu.kobotoolbox.org/).

قم بتفعيل حسابك باستخدام الرابط المرسل عبر البريد الإلكتروني، ثم سجل الدخول عبر رابط الخادم أو [صفحة التسجيل](https://www.kobotoolbox.org/sign-up/). 

<p class="note">
    لمزيد من المعلومات حول إنشاء حساب، راجع <a href="https://support.kobotoolbox.org/creating_account.html">إنشاء حساب على KoboToolbox</a>.
</p>


## إنشاء مشروعك الأول

لإنشاء نموذجك الأول:
1. انقر على **جديد**. ستتم مطالبتك باختيار مصدر المشروع.

| الخيار                    | الوصف                                                                                                           |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| البناء من الصفر        | بناء نموذج باستخدام <a href="formbuilder.html" class="reference">أداة بناء النماذج في KoboToolbox</a>.                   |
| استخدام قالب            | بناء نموذج باستخدام قالب من <a href="question_library.html" class="reference">مكتبة الأسئلة</a>.   |
| تحميل XLSForm            | تحميل ملف <a href="edit_forms_excel.html" class="reference">XLSForm</a> حيث قمت بتحديد أسئلتك.     |
| استيراد XLSForm عبر رابط URL | تحميل ملف XLSForm <a href="xls_url.html" class="reference">من مصدر عبر الإنترنت</a> مثل Google Drive أو Dropbox. |


2. حدد **البناء من الصفر** لإنشاء نموذج جديد باستخدام أداة بناء النماذج في KoboToolbox.
3. في مربع حوار **تفاصيل المشروع**، أدخل المعلومات ذات الصلة بمشروعك ثم انقر على **إنشاء مشروع**.

## بناء نموذج باستخدام أداة بناء النماذج

1. بمجرد الدخول إلى أداة بناء النماذج، انقر على زر <i class="k-icon-plus"></i> لإضافة سؤالك الأول. أدخل تسمية السؤال واختر [نوع السؤال](question_types.md).
2. لتحديد معاملات السؤال، انقر على أيقونة <i class="k-icon-settings"></i> **الإعدادات**. على سبيل المثال، يمكنك جعل السؤال إلزامياً، أو تغيير مظهره، أو إضافة شروط [منطق التخطي](skip_logic.md).
3. انقر على <i class="k-icon-view"></i> **معاينة النموذج** لعرض واختبار نموذجك.
4. لحفظ النموذج، انقر على **حفظ** في الزاوية العلوية اليمنى، ثم انقر على <i class="k-icon-close"></i> لإغلاق النموذج.

<p class="note">
    لمعرفة المزيد حول استخدام أداة بناء النماذج، راجع <a href="https://support.kobotoolbox.org/formbuilder.html">البدء في استخدام أداة بناء النماذج في KoboToolbox</a> و <a href="https://support.kobotoolbox.org/question_options.html">استخدام خيارات الأسئلة</a>.
</p>


## نشر نموذجك لجمع البيانات

1. لبدء جمع البيانات، انقر على **نشر** في صفحة **النموذج** [لنشر نموذجك المسودة](deploy_form_new_project.md) كمشروع جديد لجمع البيانات.
2. ضمن **جمع البيانات**، انقر على **نسخ** لمشاركة رابط النموذج لإدخال البيانات [من المتصفح](data_through_webforms.md) على أي جهاز (كمبيوتر، iPhone، Android).
3. بدلاً من ذلك، قم بتنزيل وإعداد تطبيق [KoboCollect](kobocollect_on_android_latest.md) لنظام Android لجمع البيانات عبر الهاتف المحمول.


<p class="note">
    <strong>ملاحظة:</strong> <a href="project_sharing_settings.html">لمشاركة نموذجك</a> مع أي شخص لديه رابط النموذج، قم بتفعيل "السماح بإرسال البيانات إلى هذا النموذج بدون اسم مستخدم وكلمة مرور" في صفحة <strong>النموذج</strong>، ضمن <strong>جمع البيانات</strong>.
</p>


بمجرد جمع البيانات، يمكنك عرضها وتحريرها وتنزيلها من صفحة **البيانات** الخاصة بمشروعك. لمعرفة المزيد حول إدارة بياناتك، راجع قسم الدعم [إدارة المشاريع والبيانات](https://support.kobotoolbox.org/managing-projects.html).