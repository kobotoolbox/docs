# تحويل البيانات إلى SPSS و/أو Stata
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/converting_to_spss_and_stata.md" class="reference">15 فبراير 2022</a>

<p class="note">
  تساعدك هذه المقالة في تحويل بياناتك إلى <strong>SPSS</strong> و
  <strong>Stata</strong>. يرجى ملاحظة أنك تحتاج إلى
  <strong>IBM SPSS</strong> أو <strong>Stata</strong> وهي تطبيقات من جهات خارجية.
</p>

نظرًا لأن **KoboToolbox** لا يصدّر البيانات مباشرة بتنسيق **SPSS** أو **Stata**،
ستكون هذه المقالة دليلاً لك لإجراء التحويل.

## التحويل إلى SPSS

1. قم بتنزيل بياناتك بصيغة XLS باستخدام التعليمات الواردة في
   [مقالة الدعم هذه](export_download.md) أو كما هو موضح في الصورة
   أدناه.

    ![تصدير XLS](/images/converting_to_spss_and_stata/export_xls.gif)

2. قم بتنزيل **SPSS Labels** من نفس تبويب **DATA** كما هو موضح في الصورة
   أدناه. ستنشئ هذه العملية مجلدًا مضغوطًا يحتوي على بناء جملة **SPSS**.

    ![تصدير SPSS Labels](/images/converting_to_spss_and_stata/export_spss_labels.gif)

3. ستحتاج الآن إلى **IBM SPSS** لاستيراد البيانات بصيغة XLS باستخدام الطريقة التالية
   المتوافقة مع جميع إصدارات **SPSS**.

    - داخل **SPSS**، انقر على **File -> Open -> Data** (كما هو موضح أدناه).
    - بمجرد النقر على تبويب **Data**، سيظهر مربع بيانات.
      في مربع **Files** من النوع، حدد **Excel**.
    - انتقل إلى المجلد الذي يحتوي على ملف **Excel** الخاص بك، وابحث عن
      ملف **Excel** الذي يحتوي على البيانات التي قمت بتنزيلها.
    - افتح الملف، وستحصل على مربع حوار **Read Excel File**.

    ![الاستيراد إلى SPSS](/images/converting_to_spss_and_stata/import_into_spss.gif)

4. الآن افتح بناء الجملة الذي قمت بتنزيله في _الخطوة 2_ وقم بتشغيل بناء الجملة.

    ![تشغيل بناء الجملة](/images/converting_to_spss_and_stata/run_syntax.jpg)

أنت الآن جاهز لمعالجة بياناتك في **SPSS**.

## تحويل ملف SPSS إلى ملف STATA

للأسف ليس لدينا خيار لتنزيل ملف **SPSS DO** مباشرة.
تحتاج إلى المرور بالعملية المذكورة أعلاه ثم حفظ البيانات النهائية كبيانات `.dta`
من **Stata**.

تأكد من اختيار حفظ جميع الخيارات التي تحتاجها عند الحفظ.

![بيانات dta](/images/converting_to_spss_and_stata/dta_data.jpg)