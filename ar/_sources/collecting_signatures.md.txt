# نوع سؤال التوقيع
<a href="../collecting_signatures.html">Read in English</a> | <a href="../fr/collecting_signatures.html">Lire en français</a> | <a href="../es/collecting_signatures.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/collecting_signatures.md" class="reference">29 يوليو 2025</a>

قد تتطلب بعض النماذج تضمين توقيعات معها. يمكنك استخدام المظهر `signature` على كل من تطبيق Collect Android وEnketo. أداة الرسم متاحة فقط عند استخدام Enketo لجمع البيانات.

## تطبيق Collect Android

يتيح Collect جمع توقيع رقمي مباشرة على شاشة الهاتف/الجهاز اللوحي.

لإضافة هذا إلى نموذجك:

1. افتح أو قم بتنزيل نسخة XLS من نموذجك.
2. أنشئ السؤال واضبط النوع على `image`
3. اضبط المظهر على `signature`

## Enketo

تعمل التوقيعات الرقمية أيضًا على نماذج الويب Enketo، حيث يتوفر لديك خيار إضافي لاستخدام أداة الرسم لجمع التوقيعات. في XLSForm الخاص بك، ما عليك سوى إضافة `signature` أو `draw` تحت عمود `appearance` لسؤال من نوع `image`.

**ورقة الاستبيان**

| type  | name | label       | appearance | hint                                        |
| :---- | :--- | :---------- | :--------- | :------------------------------------------ |
| image | draw | أداة الرسم  | draw       | نوع صورة مع مظهر الرسم                      |
| image | sign | أداة التوقيع | signature  | نوع صورة مع أداة التوقيع                    |
| survey |

[اتبع هذا الرابط](https://enke.to/draw) لاختبار الفرق بين أدوات الرسم والتوقيع.

## إنشاء نوع سؤال التوقيع في أداة إنشاء النماذج

1. أنشئ سؤالاً جديدًا واختر صورة كنوع السؤال.

![image](/images/collecting_signatures/new_question.jpg)

2. في الإعدادات تحت خيارات السؤال، انقر على القائمة المنسدلة المظهر واختر التوقيع.

![image](/images/collecting_signatures/signature.jpg)