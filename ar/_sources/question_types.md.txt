# قائمة أنواع الأسئلة
<a href="../question_types.html">Read in English</a> | <a href="../fr/question_types.html">Lire en français</a> | <a href="../es/question_types.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/3993133bcf0aafda0b0978709534175cb583e049/source/question_types.md" class="reference">28 أكتوبر 2024</a>

يقدم الجدول أدناه ملخصًا عامًا لكل نوع من أنواع الإجابات المتاحة للاستخدام في XLSForm وأداة إنشاء النماذج:

| نوع السؤال                       | الأيقونة                                          | إدخال الإجابة                                                                                 |
| :------------------------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------- |
| integer                          | <i class="k-icon k-icon-qt-number"></i>       | إدخال عدد صحيح (أي رقم كامل).                                                          |
| decimal                          | <i class="k-icon k-icon-qt-decimal"></i>      | إدخال عدد عشري.                                                                               |
| range                            | <i class="k-icon k-icon-qt-range"></i>        | إدخال نطاق (بما في ذلك التقييم).                                                              |
| text                             | <i class="k-icon k-icon-qt-text"></i>         | إجابة نصية حرة.                                                                          |
| select_one [options]             | <i class="k-icon k-icon-qt-select-one"></i>   | سؤال متعدد الخيارات؛ يمكن اختيار إجابة واحدة فقط.                                   |
| select_multiple [options]        | <i class="k-icon k-icon-qt-select-many"></i>  | سؤال متعدد الخيارات؛ يمكن اختيار إجابات متعددة.                                  |
| select_one_from_file [file]      | <i class="k-icon k-icon-qt-select-one"></i>   | اختيار متعدد من ملف؛ يمكن اختيار إجابة واحدة فقط.                                  |
| select_multiple_from_file [file] | <i class="k-icon k-icon-qt-select-many"></i>  | اختيار متعدد من ملف؛ يمكن اختيار إجابات متعددة.                                 |
| rank [options]                   | n/a                                           | سؤال ترتيب؛ ترتيب قائمة.                                                                 |
| note                             | <i class="k-icon k-icon-qt-note"></i>         | عرض ملاحظة على الشاشة، لا يتطلب إدخالاً. اختصار لـ type=text مع readonly=true.    |
| geopoint                         | <i class="k-icon k-icon-qt-point"></i>        | جمع إحداثيات GPS واحدة.                                                             |
| geotrace                         | <i class="k-icon k-icon-qt-line"></i>         | تسجيل خط من إحداثيتي GPS أو أكثر.                                                |
| geoshape                         | <i class="k-icon k-icon-qt-area"></i>         | تسجيل مضلع من إحداثيات GPS متعددة؛ النقطة الأخيرة هي نفسها النقطة الأولى. |
| date                             | <i class="k-icon k-icon-qt-date"></i>         | إدخال تاريخ.                                                                                  |
| time                             | <i class="k-icon k-icon-qt-time"></i>         | إدخال وقت.                                                                                  |
| datetime                         | <i class="k-icon k-icon-qt-date-time"></i>    | يقبل إدخال تاريخ ووقت.                                                             |
| image                            | <i class="k-icon k-icon-qt-photo"></i>        | التقاط صورة أو تحميل ملف صورة.                                                      |
| audio                            | <i class="k-icon k-icon-qt-audio"></i>        | إجراء تسجيل صوتي أو تحميل ملف صوتي.                                             |
| background-audio                 | <i class="k-icon k-icon-background-rec"></i>  | يتم تسجيل الصوت في الخلفية أثناء ملء النموذج.                                  |
| video                            | <i class="k-icon k-icon-qt-video"></i>        | إجراء تسجيل فيديو أو تحميل ملف فيديو.                                               |
| file                             | <i class="k-icon k-icon-qt-file"></i>         | إدخال ملف عام (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                          | <i class="k-icon k-icon-qt-barcode"></i>      | مسح رمز شريطي أو رمز QR                            |
| calculate                        | <i class="k-icon k-icon-qt-calculate"></i>    | إجراء عملية حسابية؛ راجع قسم الحساب أدناه.                                    |
| acknowledge                      | <i class="k-icon k-icon-qt-acknowledge"></i>  | مطالبة بالإقرار تحدد القيمة على "OK" إذا تم تحديدها.                                      |
| hidden                           | <i class="k-icon k-icon-qt-hidden"></i>       | حقل بدون عنصر واجهة مستخدم مرتبط يمكن استخدامه لتخزين ثابت.                 |
| xml-external                     | <i class="k-icon k-icon-qt-external-xml"></i> | يضيف مرجعًا إلى ملف بيانات XML خارجي.                                               |

لمزيد من المعلومات حول أنواع الإجابات، يرجى زيارة
[xlsform.org](http://xlsform.org/).

بالإضافة إلى ذلك، يمكن أيضًا استخدام الأنواع الخاصة بـ KoboToolbox من داخل
أداة إنشاء النماذج:

| نوع السؤال في أداة إنشاء النماذج | الأيقونة                                             | إدخال الإجابة                                                 |
| :------------------------ | :----------------------------------------------- | :----------------------------------------------------------- |
| Rating                    | <i class="k-icon k-icon-qt-rating"></i>          | مقارنة عناصر مختلفة باستخدام مقياس مشترك.                |
| Ranking                   | <i class="k-icon k-icon-qt-ranking"></i>         | مقارنة قائمة من الأشياء المختلفة مع بعضها البعض.          |
| Question Matrix           | <i class="k-icon k-icon-qt-question-matrix"></i> | إنشاء مجموعة من الأسئلة التي تُعرض بتنسيق مصفوفة. |

<p class="note"><a class="reference" href="/calculate_questions.html">أسئلة الحساب</a> لا تُعرض في النموذج الخاص بك، ولكن يتم تنفيذها تلقائيًا أثناء الإجابة على النموذج.</p>

<p class="note"><a class="reference" href="matrix_response.html">نوع مصفوفة الأسئلة</a> مدعوم فقط في Enketo ومع تعيين سمة الشبكة. </p>