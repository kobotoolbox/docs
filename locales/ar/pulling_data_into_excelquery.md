# ربط KoboToolbox بـ Microsoft Excel
<a href="../pulling_data_into_excelquery.html">Read in English</a> | <a href="../fr/pulling_data_into_excelquery.html">Lire en français</a> | <a href="../es/pulling_data_into_excelquery.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/df082614a0ae0bce8543b0c1474a9567fea7293e/source/pulling_data_into_excelquery.md" class="reference">23 آب/أغسطس 2022</a>

يتيح لك KoboToolbox ربط مشروع جمع البيانات الخاص بك ببرامج خارجية
مثل Microsoft Excel أو Power BI أو Google Sheets وهو ما يتم من خلال
واجهة برمجة التطبيقات (API).

يرشدك هذا المقال خلال عملية ربط مشروعك بـ Excel.
إذا كنت ترغب في الربط بـ Power BI، يُرجى الرجوع إلى المقال
[هنا](pulling_data_into_powerbi.md).

## الخطوة 1: الحصول على رابط التصدير المتزامن

لإدخال البيانات إلى Excel، تحتاج أولاً إلى الحصول على رابط التصدير المتزامن
من خلال واجهة برمجة التطبيقات الخاصة بـ KoboToolbox. العملية خطوة بخطوة للقيام بذلك موضحة
في المقال [هنا](synchronous_exports.md).

## الخطوة 2: إضافة مصدر البيانات

<p class="note">تعمل هذه الخطوات فقط في Excel 2016 والإصدارات الأحدث.</p>

- افتح Excel وأنشئ مصنفاً فارغاً. يمكنك أيضاً العمل ضمن مصنف
  موجود، حتى لو كان يحتوي بالفعل على بيانات.
- انقر على علامة التبويب **Data**، واختر **Get Data -> From Other Sources -> From Web**.
- الصق رابط التصدير المتزامن الذي نسخته وانقر على **OK**.

![Get data](images/pulling_data_excelquery/get_data.gif)

- ضمن مربع الحوار "Access Web content"، انقر على **Basic** لإضافة تفاصيل
  المصادقة الخاصة بك.
- أدخل اسم المستخدم وكلمة المرور الخاصة بك في KoboToolbox وانقر على **CONNECT**.

![Authentication](images/pulling_data_excelquery/authentication.gif)

<p class="note">
  إذا جعلت بيانات مشروعك عامة، يمكنك الاتصال دون مصادقة
  عن طريق اختيار "Anonymous" في مربع الحوار "Access Web content". تعرّف على المزيد
  حول أذونات المشروع
  <a href="managing_permissions.html" class="reference">هنا</a>.
</p>

ستظهر قائمة بالبيانات الموجودة في مشروعك في Navigator.

<p class="note">
  إذا كان نموذجك يحتوي على مجموعات متكررة، ستظهر كل مجموعة كورقة عمل منفصلة
  في Navigator. تأكد من استخدام رابط "data_url_xlsx" حيث أن
  تصدير CSV <em>لا يتضمن</em> المجموعات المتكررة.
</p>

- اختر البيانات التي ترغب في استيرادها. لاستيراد جداول متعددة دفعة واحدة،
  انقر على "Select multiple items"، ثم اختر العناصر من القائمة.
- انقر على **Load** لإدخال البيانات أو انقر على **Transform Data** لفتح
  Power Query Editor الذي يمكنك استخدامه لتنظيف البيانات وتحويلها قبل
  تحميلها.

![Choosing tables](images/pulling_data_excelquery/navigator.gif)

<p class="note">
  يمكنك ربط مشاريع متعددة في مصنف Excel واحد. كرر العملية
  أعلاه لكل مشروع، باستخدام رابط التصدير المتزامن الخاص به. في معظم الحالات
  التي يكون لديك فيها جداول متعددة، قد يكون من الضروري إعداد علاقات بين الجداول
  قبل أن تتمكن من استخدام الحقول لإنشاء التقارير ولوحات المعلومات.
  أعد إعداد العلاقات بالانتقال إلى
  <strong>Data -> Data Tools -> Relationships</strong>. تعرّف على المزيد حول
  إنشاء علاقات الجداول
  <a
    href="https://support.microsoft.com/en-us/office/create-a-relationship-between-tables-in-excel-fe1b6be7-1d85-4add-a629-8a3848820be3"
    class="reference"
    >هنا</a
  >.
</p>

### استخدام البيانات المستوردة

يوفر لك Excel عدة طرق للعمل مع البيانات التي قمت باستيرادها للتو.

#### 1. إنشاء PivotTables وPivotCharts من Data Model

PivotTable هي أداة قوية تُستخدم لحساب البيانات وتلخيصها وتحليلها -
مما يتيح لك رؤية المقارنات والأنماط والاتجاهات في البيانات. يمكن تصور البيانات
الملخصة في PivotTables بطريقة بسيطة باستخدام
PivotCharts.

- انقر على علامة التبويب **Insert**، ثم انقر على السهم المنسدل على PivotTable
- اختر **From Data Model**
- اختر **New Worksheet**
- انقر على **OK**

![Creating a pivot table](images/pulling_data_excelquery/pivot.gif)

ستظهر الجداول المستوردة في اللوحة الجانبية **PivotTable Fields** حيث
يمكنك اختيار الحقول المطلوبة.

#### 2. تحميل البيانات في ورقة العمل

عند استيراد جدول واحد، كما هو الحال عندما لا يحتوي مشروعك على أي
مجموعات متكررة، يتم تحميل البيانات تلقائياً كجدول في ورقة العمل.
ومع ذلك، عندما تأتي بياناتك كجداول متعددة، يتم إدراج الجداول في
لوحة **Queries & Connections**.

لتحميل هذه البيانات في ورقة العمل الخاصة بك:

- انقر بزر الماوس الأيمن على جدول من لوحة **Queries and Connections** واختر
  **Load To**. (إذا لم تظهر لك اللوحة، انتقل إلى **Data -> Queries and
  Connections**.
- في مربع الحوار التالي، اختر **Table** وانقر على **OK**. يمكنك أيضاً
  اختيار الخيارات الأخرى المتاحة حسب حاجتك.

![Loading a table in Excel](images/pulling_data_excelquery/load_table.gif)

يمكنك القيام بذلك لجميع الجداول المدرجة في لوحة **Queries and Connections**.

## تحديث البيانات في تقاريرك

عندما يتم تحديث بيانات مشروعك على خادم KoboToolbox، كما هو الحال عندما يكون لديك
إرسالات جديدة، أو تغييرات في حالات التحقق، أو تعديلات، أو حذف، ستحتاج
إلى مزامنتها مع تقاريرك. في Excel:

- انتقل إلى علامة التبويب **Data**
- ضمن "Queries and connections"، انقر على **Refresh**

## استكشاف الأخطاء وإصلاحها

### فشل الاتصال بـ KoboToolbox

في بعض الأحيان، حتى بعد إدخال بيانات الاعتماد الصحيحة للاتصال بمشروعك،
قد تحصل على خطأ. قد يحدث هذا إذا تم تكوين Excel للاتصال
بحساب واحد من قبل، وأنت الآن تحاول الاتصال باستخدام
حساب مختلف من نفس خادم KoboToolbox، أي كلاهما من
الخادم الإنساني.

لإعادة تعيين إعدادات المصادقة:

- انتقل إلى **Data tab -> Get Data -> Data source settings**. حدد الأذونات
  الموجودة في مربع الحوار وانقر على **Clear Permissions**. أغلق وحاول
  إضافة الاتصال الجديد مرة أخرى.

![Clearing data source settings](images/pulling_data_excelquery/data_source_settings.gif)

### فشل تحديث البيانات

إذا كنت تحصل على خطأ عند تحديث البيانات، فقد يكون هناك عدد من
الأسباب:

- قد تكون تفاصيل المصادقة الخاصة بك قد تغيرت. ستحتاج إلى اتباع
  التعليمات أعلاه لتغيير **Data Source Settings** الخاصة بك.
- قد يكون حقل واحد أو أكثر في نموذجك قد تم حذفه أو إعادة تسميته.
  [ستحتاج إلى تحرير الاستعلام في Power Query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- قد يكون هناك عدم تطابق في نوع البيانات، خاصة إذا قمت بتغيير نوع البيانات
  لحقل واحد أو أكثر في Excel. يمكنك محاولة إعادة تعيين نوع البيانات قبل
  تحديث الاتصال.