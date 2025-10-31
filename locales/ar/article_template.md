# عنوان المقالة
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/2afa3a0c670fe98b296a79b798f33abf248d0273/source/article_template.md" class="reference">6 سبتمبر 2025</a>

هنا يتم وضع المقدمة. لاحظ أعلاه أن كود "آخر تحديث" سيتم تحديثه تلقائيًا باسم المقالة والتاريخ الصحيحين عند النشر، لذا لا حاجة لتغيير يدوي. تذكر تسمية هذا الملف وفقًا لعنوان المقالة، وإنهاء اسم الملف بـ `.md`.

تتضمن هذه المقالة:

-   [تنسيق النص في markdown](#this-is-a-header)
-   [إضافة ملفات الوسائط](#adding-media-files)
-   [إضافة الجداول](#adding-tables)
-   [تنسيق HTML](#html-formatting)
-   [إنشاء قسم استكشاف الأخطاء وإصلاحها](#troubleshooting)
-   [قائمة الأيقونات](#list-of-icons)

للحصول على مساعدة بشأن تنسيق markdown أو HTML، راجع [هذا الدليل](https://www.markdownguide.org/basic-syntax/).

بعد إنشاء مقالة جديدة، لا تنسَ إضافتها إلى ملف [index.rst](https://github.com/kobotoolbox/docs/blob/master/source/index.rst).

<br/> 


## هذا عنوان

- هذه قائمة غير مرتبة
- في markdown

1. هذه قائمة مرقمة.
2. في markdown.
    - مع نقطة فرعية.

هذا **نص غامق** في markdown.

هذا *نص مائل* في markdown.

هذا `كود أحادي المسافة` في markdown.

> هذا اقتباس كتلة (غير مستخدم حاليًا في التوثيق)

تضمين الروابط: لنقل ملكية فريقك إلى مستخدم آخر، [يرجى الاتصال بفريق الدعم لدينا](support@kobotoolbox.org).

تعرف على المزيد حول [خدمات التدريب لدينا](https://www.kobotoolbox.org/services/training/).

**روابط لمقالات أخرى:** لمزيد من المعلومات، راجع [أذونات مستوى الصف](row_level_permissions.md)

رابط إلى [قسم آخر](#adding-media-files) داخل المقالة. ملاحظة: علامة # واحدة فقط لجميع أحجام العناوين، بدون مسافة بين # واسم الرابط، يجب أن تكون أسماء علامات الربط بأحرف صغيرة، ومفصولة بشرطات إذا كانت متعددة الكلمات.

لتحويل عنوان URL أو عنوان بريد إلكتروني بسرعة إلى رابط، ضعه بين أقواس زاوية.

<https://www.markdownguide.org>
<fake@example.com>

أضف خطًا لفصل المحتوى:

---

أضف سطرًا فارغًا...

...لبدء فقرة جديدة أو فاصل سطر.

لإضافة فاصل سطر كامل، استخدم:

<br/> 



## إضافة ملفات الوسائط

### إضافة الصور

![image](/images/getting_started_organization_feature/organizations_project_views.gif)

قم بتخزين الصور في [مجلد الصور](https://github.com/kobotoolbox/docs/tree/master/source/images)، في مجلد يحمل اسم مقالة الدعم. قم بتضمين اسم المجلد واسم ملف الصورة في مسار الملف أعلاه.

### إضافة الأيقونات
انقر على أيقونة <i class="k-icon k-icon-more"></i> **المزيد من الإجراءات** للمستخدم الذي تريد إزالته.

انقر على <i class="k-icon k-icon-replace"></i> **استبدال النموذج**.

للحصول على قائمة كاملة بجميع الأيقونات، راجع [هنا](https://support.kobotoolbox.org/ar/article_template.html#list-of-icons) وأيضًا [هنا](https://support.kobotoolbox.org/_static/kpi-icons/k-icons.html).

### إضافة فيديو YouTube

نوصي بنشر مقاطع الفيديو على YouTube وتضمين رابط باستخدام iframes. 

<iframe src="https://www.youtube.com/embed/oKtMmBAlHho?si=OqS7-rewYMf-Rrw2" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

قم بتضمين رابط فيديو YouTube داخل iframe.

يمكنك أيضًا تضمين مقاطع الفيديو بالطريقة التالية:

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_xlsform_v2.mp4"
    type="video/mp4"
  />
</video>


<br/> 

## إضافة الجداول

### جدول عادي 

| **اسم العمود**    | **الوصف**                                |
| :----------------- | :--------------------------------------------- |
| hint               | تلميح السؤال                                  |
| guidance_hint      | تلميح الإرشاد                                  |
| required           | خيار لجعل السؤال إلزاميًا            |
| relevant           | شروط منطق التخطي للسؤال         |
| constraint         | معايير التحقق للسؤال           |
| constraint_message | رسالة الخطأ عند عدم استيفاء معايير التحقق |
| appearance         | خيارات كيفية عرض الأسئلة        |
| choice_filter      | معايير التحديد المتتالي                  |
| parameters         | إعدادات لأنواع أسئلة محددة           |
| calculation        | تعبير رياضي لسؤال الحساب |
| default            | الاستجابة الافتراضية للسؤال                |

### جدول XLSForm

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | ما اسمك؟ |
| survey |

لاحظ `| survey |` في أسفل الجدول.


### إصلاح عرض الجدول

إذا لم يكن أحد الأعمدة كبيرًا بما يكفي، أضف مسافات `&emsp;` لجعله أوسع، كما هو موضح أدناه:

| **إعداد التصدير** | **الوصف**                                |
| :-------------------- | :------------------------------------ |
| حفظ التحديد باسم… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| حدد هذا الخيار وأدخل اسمًا لإعدادات التصدير الخاصة بك. عند النقر على <strong>تصدير</strong>، سيتم حفظ هذه الإعدادات وسيظهر الاسم في مربع <strong>تطبيق إعدادات التصدير المحفوظة</strong>. | 


<br/> 

## تنسيق HTML

داخل صناديق الملاحظات والجداول، **استخدم HTML** لتنسيق النص. على سبيل المثال:

<p class="note">
  <b>ملاحظة مهمة</b>: لا يمكن مشاركة المشاريع والبيانات بين الخادمين. هذا يعني أن جميع المستخدمين الذين يعملون على مشروع مشترك يجب أن يستخدموا نفس الخادم للوصول إلى المشروع. <a href="https://www.kobotoolbox.org/about-us">أضف رابطًا في HTML بهذه الطريقة.</a></li>
</p>

<p class="note">
  <b>ملاحظة:</b> لمعرفة المزيد حول أذونات مستوى الصف، راجع <a class="reference" href="row_level_permissions.html">الوصول على مستوى الصف</a>.
</p>

<p class="note">
  <b>ملاحظة:</b> لمعرفة المزيد حول أنواع الأسئلة في XLSForm، راجع <a class="reference external" href="https://xlsform.org/en/#question-types">أنواع الأسئلة (XLSForm.org)</a>.
</p>

| الخادم                            | عنوان URL                                                                           |
| :-------------------------------- | :---------------------------------------------------------------------------- |
| الخادم العالمي لـ KoboToolbox         | <a href="https://kf.kobotoolbox.org" class="reference">kf.kobotoolbox.org</a> |
| خادم الاتحاد الأوروبي لـ KoboToolbox | <a href="https://eu.kobotoolbox.org" class="reference">eu.kobotoolbox.org</a> |


<p class='note'>يمكنك تنزيل الملفات <a download class='reference'
href='./_static/files/media/xlsform-example.xls'>هنا</a> وملفات الوسائط <a
download class='reference'
href='./_static/files/media/xlsform-example-media.zip'>هنا</a>. يتم تخزين الملفات في ./_static/files/media/.</p>

فواصل الأسطر في HTML:
<p>هذا هو السطر الأول.<br>
وهذا هو السطر الثاني.</p>

اجعل نصك <strong>غامقًا</strong>، أو <em>مائلًا</em>، أو <code>كود أحادي المسافة</code>.

أضف قائمة مرقمة:
<ol>
  <li>العنصر الأول.</li>
  <li>العنصر الثاني.</li>
  <li>العنصر الثالث.</li>
  <li>العنصر الرابع.</li>
</ol>

أضف قائمة غير مرقمة:
<ul>
  <li>العنصر الأول</li>
  <li>العنصر الثاني</li>
  <li>العنصر الثالث</li>
  <li>العنصر الرابع</li>
</ul>

<br/> 

## استكشاف الأخطاء وإصلاحها

<details>
<summary><strong>Enketo مقابل KoboCollect</strong></summary>
<br>
    استخدم هذا التنسيق لإعداد <strong>أقسام استكشاف الأخطاء وإصلاحها</strong> في مقالات الدعم الخاصة بك. قم بتضمين عنوان قصير يصف المشكلة بوضوح، واقترح الحلول هنا.
    <br><br>
    لفصل الأسطر داخل عنصر استكشاف الأخطاء وإصلاحها، أضف فاصل سطر مزدوج.
</details>

<details>
<summary><strong>Enketo مقابل KoboCollect</strong></summary>
<br>
استخدم هذا التنسيق لإعداد <strong>أقسام استكشاف الأخطاء وإصلاحها</strong> في مقالات الدعم الخاصة بك. قم بتضمين عنوان قصير يصف المشكلة بوضوح، واقترح الحلول هنا.
</details>

<br/> 

## قائمة الأيقونات

<details>
<summary><strong>الأسهم</strong></summary>
<br>

k-icon-angle-bar-left	<i class="k-icon k-icon-angle-bar-left"></i>

k-icon-angle-bar-right	<i class="k-icon k-icon-angle-bar-right"></i>

k-icon-angle-down	<i class="k-icon k-icon-angle-down"></i>

k-icon-angle-left	<i class="k-icon k-icon-angle-left"></i>

k-icon-angle-right	<i class="k-icon k-icon-angle-right"></i>

k-icon-angle-up	<i class="k-icon k-icon-angle-up"></i>

k-icon-arrow-down-left	<i class="k-icon k-icon-arrow-down-left"></i>

k-icon-arrow-down-right	<i class="k-icon k-icon-arrow-down-right"></i>

k-icon-arrow-down	<i class="k-icon k-icon-arrow-down"></i>

k-icon-arrow-left	<i class="k-icon k-icon-arrow-left"></i>

k-icon-arrow-right	<i class="k-icon k-icon-arrow-right"></i>

k-icon-arrow-up-left	<i class="k-icon k-icon-arrow-up-left"></i>

k-icon-arrow-up-right	<i class="k-icon k-icon-arrow-up-right"></i>

k-icon-arrow-up	<i class="k-icon k-icon-arrow-up"></i>

k-icon-caret-down	<i class="k-icon k-icon-caret-down"></i>

k-icon-caret-left	<i class="k-icon k-icon-caret-left"></i>

k-icon-caret-right	<i class="k-icon k-icon-caret-right"></i>

k-icon-caret-up	<i class="k-icon k-icon-caret-up"></i>

    
</details>

<details>
<summary><strong>أداة إنشاء النماذج</strong></summary>
<br>

k-icon-kobo 	<i class="k-icon k-icon-kobo"></i>

k-icon-cascading 	<i class="k-icon k-icon-cascading"></i>

k-icon-drag-handle 	<i class="k-icon k-icon-drag-handle"></i>

k-icon-duplicate 	<i class="k-icon k-icon-duplicate"></i>

k-icon-edit 	<i class="k-icon k-icon-edit"></i>

k-icon-expand-list 	<i class="k-icon k-icon-expand-list"></i>

k-icon-expand 	<i class="k-icon k-icon-expand"></i>

k-icon-file-audio 	<i class="k-icon k-icon-file-audio"></i>

k-icon-file-image 	<i class="k-icon k-icon-file-image"></i>

k-icon-file-video 	<i class="k-icon k-icon-file-video"></i>

k-icon-file-xls 	<i class="k-icon k-icon-file-xls"></i>

k-icon-file-xml 	<i class="k-icon k-icon-file-xml"></i>

k-icon-file	<i class="k-icon k-icon-file"></i>

k-icon-group-split 	<i class="k-icon k-icon-group-split"></i>

k-icon-group 	<i class="k-icon k-icon-group"></i>

k-icon-media-files	<i class="k-icon k-icon-media-files"></i>

k-icon-question 	<i class="k-icon k-icon-question"></i>

k-icon-settings 	<i class="k-icon k-icon-settings"></i>

k-icon-skip-logic 	<i class="k-icon k-icon-skip-logic"></i>

k-icon-view-all 	<i class="k-icon k-icon-view-all"></i>

k-icon-view 	<i class="k-icon k-icon-view"></i>
   
</details>

<details>
<summary><strong>أنواع الأسئلة</strong></summary>
<br>

k-icon-qt-acknowledge-lock 	<i class="k-icon k-icon-qt-acknowledge-lock"></i>

k-icon-qt-acknowledge 	<i class="k-icon k-icon-qt-acknowledge"></i>

k-icon-qt-area-lock 	<i class="k-icon k-icon-qt-area-lock"></i>

k-icon-qt-area 	<i class="k-icon k-icon-qt-area"></i>

k-icon-qt-audio-lock 	<i class="k-icon k-icon-qt-audio-lock"></i>

k-icon-qt-audio 	<i class="k-icon k-icon-qt-audio"></i>

k-icon-qt-background-audio 	<i class="k-icon k-icon-qt-background-audio"></i>

k-icon-qt-barcode-lock 	<i class="k-icon k-icon-qt-barcode-lock"></i>

k-icon-qt-barcode 	<i class="k-icon k-icon-qt-barcode"></i>

k-icon-qt-calculate-lock 	<i class="k-icon k-icon-qt-calculate-lock"></i>

k-icon-qt-calculate 	<i class="k-icon k-icon-qt-calculate"></i>

k-icon-qt-date-lock 	<i class="k-icon k-icon-qt-date-lock"></i>

k-icon-qt-date-time-lock 	<i class="k-icon k-icon-qt-date-time-lock"></i>

k-icon-qt-date-time 	<i class="k-icon k-icon-qt-date-time"></i>

k-icon-qt-date 	<i class="k-icon k-icon-qt-date"></i>

k-icon-qt-decimal-lock 	<i class="k-icon k-icon-qt-decimal-lock"></i>

k-icon-qt-decimal k-icon-qt-external-xml-lock 	<i class="k-icon k-icon-qt-decimal k-icon-qt-external-xml-lock"></i>

k-icon-qt-external-xml 	<i class="k-icon k-icon-qt-external-xml"></i>

k-icon-qt-file-lock 	<i class="k-icon k-icon-qt-file-lock"></i>

k-icon-qt-file 	<i class="k-icon k-icon-qt-file"></i>

k-icon-qt-hidden-lock 	<i class="k-icon k-icon-qt-hidden-lock"></i>

k-icon-qt-hidden 	<i class="k-icon k-icon-qt-hidden"></i>

k-icon-qt-line-lock 	<i class="k-icon k-icon-qt-line-lock"></i>

k-icon-qt-line 	<i class="k-icon k-icon-qt-line"></i>

k-icon-qt-meta-default 	<i class="k-icon k-icon-qt-meta-default"></i>

k-icon-qt-note-lock 	<i class="k-icon k-icon-qt-note-lock"></i>

k-icon-qt-note 	<i class="k-icon k-icon-qt-note"></i>

k-icon-qt-number-lock 	<i class="k-icon k-icon-qt-number-lock"></i>

k-icon-qt-number 	<i class="k-icon k-icon-qt-number"></i>

k-icon-qt-photo-lock 	<i class="k-icon k-icon-qt-photo-lock"></i>

k-icon-qt-photo 	<i class="k-icon k-icon-qt-photo"></i>

k-icon-qt-point-lock 	<i class="k-icon k-icon-qt-point-lock"></i>

k-icon-qt-point 	<i class="k-icon k-icon-qt-point"></i>

k-icon-qt-question-matrix-lock 	<i class="k-icon k-icon-qt-question-matrix-lock"></i>

k-icon-qt-question-matrix 	<i class="k-icon k-icon-qt-question-matrix"></i>

k-icon-qt-range-lock 	<i class="k-icon k-icon-qt-range-lock"></i>

k-icon-qt-range 	<i class="k-icon k-icon-qt-range"></i>

k-icon-qt-ranking-lock 	<i class="k-icon k-icon-qt-ranking-lock"></i>

k-icon-qt-ranking 	<i class="k-icon k-icon-qt-ranking"></i>

k-icon-qt-rating-lock 	<i class="k-icon k-icon-qt-rating-lock"></i>

k-icon-qt-rating 	<i class="k-icon k-icon-qt-rating"></i>

k-icon-qt-select-many-from-file-lock 	<i class="k-icon k-icon-qt-select-many-from-file-lock"></i>

k-icon-qt-select-many-from-file 	<i class="k-icon k-icon-qt-select-many-from-file"></i>

k-icon-qt-select-many-lock 	<i class="k-icon k-icon-qt-select-many-lock"></i>

k-icon-qt-select-many 	<i class="k-icon k-icon-qt-select-many"></i>

k-icon-qt-select-one-from-file-lock 	<i class="k-icon k-icon-qt-select-one-from-file-lock"></i>

k-icon-qt-select-one-from-file 	<i class="k-icon k-icon-qt-select-one-from-file"></i>

k-icon-qt-select-one-lock 	<i class="k-icon k-icon-qt-select-one-lock"></i>

k-icon-qt-select-one 	<i class="k-icon k-icon-qt-select-one"></i>

k-icon-qt-text-lock 	<i class="k-icon k-icon-qt-text-lock"></i>

k-icon-qt-text 	<i class="k-icon k-icon-qt-text"></i>

k-icon-qt-time-lock 	<i class="k-icon k-icon-qt-time-lock"></i>

k-icon-qt-time 	<i class="k-icon k-icon-qt-time"></i>

k-icon-qt-video-lock 	<i class="k-icon k-icon-qt-video-lock"></i>

k-icon-qt-video	<i class="k-icon k-icon-qt-video"></i>

   
</details>

<details>
<summary><strong>إدارة المشاريع</strong></summary>
<br>
    
k-icon-archived 	<i class="k-icon k-icon-archived"></i>

k-icon-data-sync 	<i class="k-icon k-icon-data-sync"></i>

k-icon-deploy	<i class="k-icon k-icon-deploy"></i>

k-icon-document 	<i class="k-icon k-icon-document"></i>

k-icon-download 	<i class="k-icon k-icon-download"></i>

k-icon-drafts	<i class="k-icon k-icon-drafts"></i>

k-icon-language-alt 	<i class="k-icon k-icon-language-alt"></i>

k-icon-language-default 	<i class="k-icon k-icon-language-default"></i>

k-icon-language-settings 	<i class="k-icon k-icon-language-settings"></i>

k-icon-language 	<i class="k-icon k-icon-language"></i>

k-icon-logout 	<i class="k-icon k-icon-logout"></i>

k-icon-menu 	<i class="k-icon k-icon-menu"></i>

k-icon-project-archived 	<i class="k-icon k-icon-project-archived"></i>

k-icon-project-deployed 	<i class="k-icon k-icon-project-deployed"></i>

k-icon-project-draft 	<i class="k-icon k-icon-project-draft"></i>

k-icon-project-locked 	<i class="k-icon k-icon-project-locked"></i>

k-icon-project-overview 	<i class="k-icon k-icon-project-overview"></i>

k-icon-project 	<i class="k-icon k-icon-project"></i>

k-icon-projects 	<i class="k-icon k-icon-projects"></i>

k-icon-replace 	<i class="k-icon k-icon-replace"></i>

k-icon-upload 	<i class="k-icon k-icon-upload"></i>

k-icon-user-share 	<i class="k-icon k-icon-user-share"></i>

k-icon-user 	<i class="k-icon k-icon-user"></i>

k-icon-users	<i class="k-icon k-icon-users"></i>

   
</details>

<details>
<summary><strong>البيانات</strong></summary>
<br>
    
k-icon-filter-arrows 	<i class="k-icon k-icon-filter-arrows"></i>

k-icon-filter 	<i class="k-icon k-icon-filter"></i>

k-icon-map-view 	<i class="k-icon k-icon-map-view"></i>

k-icon-gallery 	<i class="k-icon k-icon-gallery"></i>

k-icon-globe-alt	<i class="k-icon k-icon-globe-alt"></i>

k-icon-layer 	<i class="k-icon k-icon-layer"></i>

k-icon-hide 	<i class="k-icon k-icon-hide"></i>

k-icon-reports 	<i class="k-icon k-icon-reports"></i>

k-icon-sort-ascending 	<i class="k-icon k-icon-sort-ascending"></i>

k-icon-sort-default 	<i class="k-icon k-icon-sort-default"></i>

k-icon-sort-descending 	<i class="k-icon k-icon-sort-descending"></i>

k-icon-table 	<i class="k-icon k-icon-table"></i>

k-icon-unfreeze 	<i class="k-icon k-icon-unfreeze"></i>


 </details>

<details>
<summary><strong>المجلدات والمكتبة</strong></summary>
<br>

k-icon-folder-in 	<i class="k-icon k-icon-folder-in"></i>

k-icon-folder-out 	<i class="k-icon k-icon-folder-out"></i>

k-icon-folder-plus 	<i class="k-icon k-icon-folder-plus"></i>

k-icon-folder-public 	<i class="k-icon k-icon-folder-public"></i>

k-icon-folder-shared 	<i class="k-icon k-icon-folder-shared"></i>

k-icon-folder-subscribed 	<i class="k-icon k-icon-folder-subscribed"></i>

k-icon-folder 	<i class="k-icon k-icon-folder"></i>

k-icon-freeze 	<i class="k-icon k-icon-freeze"></i>

k-icon-block 	<i class="k-icon k-icon-block"></i>

k-icon-library-public 	<i class="k-icon k-icon-library-public"></i>

k-icon-library 	<i class="k-icon k-icon-library"></i>

k-icon-template-locked 	<i class="k-icon k-icon-template-locked"></i>

k-icon-template 	<i class="k-icon k-icon-template"></i>

 
</details>

<details>
<summary><strong>الرموز</strong></summary>
<br>

k-icon-alert 	<i class="k-icon k-icon-alert"></i>

k-icon-check-circle 	<i class="k-icon k-icon-check-circle"></i>

k-icon-check 	<i class="k-icon k-icon-check"></i>

k-icon-close 	<i class="k-icon k-icon-close"></i>

k-icon-expand-arrow 	<i class="k-icon k-icon-expand-arrow"></i>

k-icon-flows 	<i class="k-icon k-icon-flows"></i>

k-icon-help-articles 	<i class="k-icon k-icon-help-articles"></i>

k-icon-help 	<i class="k-icon k-icon-help"></i>

k-icon-information 	<i class="k-icon k-icon-information"></i>

k-icon-link 	<i class="k-icon k-icon-link"></i>

k-icon-lock-alt 	<i class="k-icon k-icon-lock-alt"></i>

k-icon-lock 	<i class="k-icon k-icon-lock"></i>

k-icon-minus 	<i class="k-icon k-icon-minus"></i>

k-icon-more-vertical 	<i class="k-icon k-icon-more-vertical"></i>

k-icon-more 	<i class="k-icon k-icon-more"></i>

k-icon-notification 	<i class="k-icon k-icon-notification"></i>

k-icon-pause 	<i class="k-icon k-icon-pause"></i>

k-icon-play 	<i class="k-icon k-icon-play"></i>

k-icon-plus	<i class="k-icon k-icon-plus"></i>

k-icon-search 	<i class="k-icon k-icon-search"></i>

k-icon-spinner 	<i class="k-icon k-icon-spinner"></i>

k-icon-stop 	<i class="k-icon k-icon-stop"></i>

k-icon-trash 	<i class="k-icon k-icon-trash"></i>

k-icon-warning 	<i class="k-icon k-icon-warning"></i>

</details>

<details>
<summary><strong>الدعم ووسائل التواصل الاجتماعي</strong></summary>
<br>

k-icon-email 	<i class="k-icon k-icon-email"></i>

k-icon-help-academy 	<i class="k-icon k-icon-help-academy"></i>

k-icon-help-forum 	<i class="k-icon k-icon-help-forum"></i>

k-icon-logo-github 	<i class="k-icon k-icon-logo-github"></i>

k-icon-logo-instagram 	<i class="k-icon k-icon-logo-instagram"></i>

k-icon-logo-linkedin 	<i class="k-icon k-icon-logo-linkedin"></i>

k-icon-logo-twitter 	<i class="k-icon k-icon-logo-twitter"></i>

k-icon-mail 	<i class="k-icon k-icon-mail"></i>

k-icon-intercom 	<i class="k-icon k-icon-intercom"></i>

k-icon-subscribe 	<i class="k-icon k-icon-subscribe"></i>

k-icon-unsubscribe 	<i class="k-icon k-icon-unsubscribe"></i>

</details>

<details>
<summary><strong>أخرى</strong></summary>
<br>

k-icon-attach 	<i class="k-icon k-icon-attach"></i>

k-icon-editor 	<i class="k-icon k-icon-editor"></i>

k-icon-heatmap 	<i class="k-icon k-icon-heatmap"></i>

k-icon-pdf 	<i class="k-icon k-icon-pdf"></i>

k-icon-pins 	<i class="k-icon k-icon-pins"></i>

k-icon-print 	<i class="k-icon k-icon-print"></i>

k-icon-spreadsheet 	<i class="k-icon k-icon-spreadsheet"></i>

</details>