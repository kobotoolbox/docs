# تصدير البيانات ورفعها إلى برامج نظم المعلومات الجغرافية
<a href="../upload_to_gis.html">Read in English</a> | <a href="../fr/upload_to_gis.html">Lire en français</a> | <a href="../es/upload_to_gis.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/upload_to_gis.md" class="reference">15 فبراير 2022</a>

**عملية بسيطة خطوة بخطوة لتصدير ورفع بياناتكم كملف shapefile إلى برامج نظم المعلومات الجغرافية، مثل ArcMap.**

هناك طرق متعددة لاستيراد البيانات القائمة على الموقع الجغرافي التي تم جمعها عبر KoboToolbox إلى برامج نظم المعلومات الجغرافية. ستوضح هذه المقالة إجراءً موصى به لتنزيل البيانات من KoboToolbox كملف CSV ورفعه إلى ArcMap كملف shapefile. بينما يستخدم هذا المثال ArcMap، فإن العملية مشابهة لتلك الموجودة في برامج جغرافية مكانية أخرى، بما في ذلك QGIS (مجاني).

1. في تبويب **التنزيلات** الخاص بصفحة مشروعكم في KoboToolbox، قوموا بتصدير وتنزيل بياناتكم كملف CSV.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    _ملاحظة: يمكنكم تحرير مجموعة البيانات بمجرد وجودها في برنامج نظم المعلومات الجغرافية، ومع ذلك قد يكون من الأسهل التحرير أولاً في Excel أو برنامج مشابه. في Excel، استخدموا وظيفة [Text to Columns](https://support.office.com/en-us/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23) لتقسيم بيانات CSV إلى خلايا فردية._

2. افتحوا مشروعاً جديداً أو موجوداً في ArcMap، انتقلوا إلى **Add Data**، ثم اربطوا المجلد الذي تم حفظ ملف CSV الخاص بكم فيه على جهاز الكمبيوتر.

    ![image](/images/upload_to_gis/find_file.jpg)

3. افتحوا نافذة **Catalog** وانقروا على **Folder Connections**. ابحثوا عن ملف CSV الخاص بكم، انقروا عليه بزر الماوس الأيمن، ثم اختاروا **Create Feature Class** > **From XY Table**.

4. في النافذة المنبثقة، انقروا على القائمة المنسدلة **X Field** واختاروا خيار question_Longitude الخاص بنظام تحديد المواقع GPS. تأكدوا أيضاً من اختيار **Coordinate System of Input Coordinates** الخاص بكم... (WGS 1984 خيار جيد، إذا لم تكونوا تستخدمون نظاماً بالفعل) وتأكدوا من ضبط **Output** على المجلد المناسب، ثم انقروا على **OK**.

    ![image](/images/upload_to_gis/create_feature.jpg)

5. عودة إلى نافذة **Catalog**، انقروا واسحبوا ملف shapefile الجديد الخاص بكم إلى نافذة **Data View** أو **Table of Contents**.

6. يجب أن تروا الآن نقاطكم على الشاشة، وإذا فتحتم **Attributes Table**، سترون جميع البيانات المرتبطة بكل نقطة. من هذه النقطة، يمكنكم الآن تصور وإجراء تحليلات مكانية مختلفة مع بياناتكم.

    ![image](/images/upload_to_gis/dataview_table.jpg)