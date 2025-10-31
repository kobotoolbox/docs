# استخدام علامات HXL
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/hxl.md" class="reference">29 يوليو 2025</a>

## ما هي HXL بالضبط؟

HXL تعني **لغة التبادل الإنساني** (Humanitarian Exchange Language). الهدف من HXL هو تحسين تبادل المعلومات أثناء الأزمات الإنسانية من خلال إنشاء طريقة بسيطة لتعزيز قابلية التشغيل البيني للبيانات. تقوم بذلك من خلال ترميز البيانات عبر الوسوم (#) بشكل مشابه لـ Twitter. لمزيد من المعلومات حول HXL، يرجى [زيارة هنا](https://hxlstandard.org).

## كيفية استخدام ميزة HXL في أداة إنشاء النماذج

_الفضل لـ: [David Megginson](http://www.megginson.com)_ _رابط [دليل العرض التقديمي](https://docs.google.com/presentation/d/123bHSkNh4T30CNq0i37IxOLfrqSC-3V_Khtkf6bIdg0/edit#slide=id.p) خطوة بخطوة_

1. بعد بدء نموذج وإنشاء سؤال، انتقل إلى إعدادات السؤال وفي علامة تبويب خيارات السؤال، اختر علامة HXL الخاصة بك وأضف السمات.

    ![image](/images/hxl/hxl.gif)

2. بعد إنشاء النموذج ونشر المشروع وجمع البيانات، انتقل إلى علامة تبويب التنزيلات في صفحة البيانات. حدد نوع التصدير كـ XLS وتأكد من تحديد **قيم ورؤوس XML** لتنسيق القيمة والرأس. ثم قم بالتصدير.

    ![image](/images/hxl/xml_values.gif)

3. بمجرد تصدير البيانات وتنزيلها على جهاز الكمبيوتر الخاص بك، افتح ملف XLS لرؤية علامات HXL الخاصة بك. لا بأس أن تحتوي بيانات Kobo الوصفية على علامات لا تحتوي على وسوم HXL.

    ![image](/images/hxl/xls_affected.jpg)

<p class="note">الوسم قبل الاسم إلزامي ولا يُسمح بالمسافات.</p>

## كيفية استخدام HXL في XLSForm

عند إنشاء XLSForm، ما عليك سوى إدراج عمود إضافي واحد في أي جدول بيانات موجود وملؤه بوسوم HXL التي تحدد نوع المعلومات في كل عمود.

**ورقة الاستبيان**

| type                 | name     | label                            | hxl        |
| :------------------- | :------- | :------------------------------- | :--------- |
| select_one countries | country  | حدد البلد المتأثر                | #country   |
| select_one admin1    | province | يرجى تحديد المحافظة              | #adm1+code |
| select_one admin2    | county   | حدد المقاطعة                     | #adm2+name |
| select_one sector    | cluster  | القطاع                           | #sector    |
| integer              | affected | عدد الأشخاص المتأثرين            | #affected  |
| integer              | reached  | عدد الأشخاص الذين تم الوصول إليهم حتى الآن | #reached   |
| survey |