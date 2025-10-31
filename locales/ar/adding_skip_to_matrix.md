# إضافة منطق التخطي إلى سؤال المصفوفة

**آخر تحديث:**
<a href="https://github.com/kobotoolbox/docs/blob/83d9dadfcc132d75f99e2705f77c425c2fee6d70/source/adding_skip_to_matrix.md" class="reference">11
مارس 2022</a>

في معظم الحالات، يمكنك إضافة منطق التخطي إلى أي نوع من الأسئلة كما هو موضح في
مقالة الدعم **[إضافة منطق التخطي](skip_logic.md)**. ومع ذلك، عند
العمل ضمن أداة إنشاء النماذج، فإن إضافة منطق التخطي إلى سؤال `matrix` غير
ممكنة بعد. بدلاً من ذلك، يمكن استخدام XLSForm لتطبيق منطق التخطي لهذا
النوع من الأسئلة. توضح مقالة الدعم هذه كيف يمكنك إضافة منطق التخطي إلى
سؤال `matrix` باستخدام XLSForm.

إذا كنت قد اطلعت على مقالة الدعم
**[نوع استجابة مصفوفة الأسئلة](matrix_response.md)**، فستعرف بالفعل
أن هناك طريقتين لإنشاء سؤال `matrix` في KoboToolbox:
_طريقة أداة إنشاء النماذج_ و _طريقة `kobo--matrix_list`_. توفر مقالة الدعم
هذه نظرة عامة على الخطوات اللازمة لإضافة منطق التخطي إلى
سؤال `matrix` عند استخدام أي من هاتين الطريقتين.

## طريقة أداة إنشاء النماذج:

تعمل هذه الطريقة مع **Enketo**، المعروف أيضاً باسم **نماذج الويب**، باستخدام
**تخطيط نمط الشبكة**. قد لا تعمل كما هو متوقع إذا تجاهلت
إعدادات **تخطيط نمط الشبكة** كما هو موضح في مقالة الدعم
**[استخدام أنماط نماذج Enketo البديلة](alternative_enketo.md)**.

اتبع الخطوات الموضحة أدناه لإضافة منطق التخطي إلى سؤال `matrix` باستخدام
طريقة أداة إنشاء النماذج.

**الخطوة 1:** إنشاء سؤال `matrix` في أداة إنشاء النماذج:

الخطوة الأولى هي إنشاء سؤال `matrix` في أداة إنشاء النماذج كما هو موضح
في مقالة الدعم **[نوع استجابة مصفوفة الأسئلة](matrix_response.md)**.
ما عليك سوى إضافة صفوف وأعمدة مع المتغيرات التي تنوي جمع البيانات لها.

**الخطوة 2:** تنزيل النموذج كـ XLSForm:

بمجرد أن يصبح سؤال `matrix` جاهزاً، **احفظ** النموذج ثم
[قم بتنزيله كـ XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**الخطوة 3:** إضافة رأس عمود relevant ومنطق التخطي إلى XLSForm الخاص بك:

الآن افتح XLSForm ثم أضف رأس العمود `relevant` إلى XLSForm.
بمجرد أن يكون لديك رأس العمود `relevant`، ستتمكن من إضافة منطق التخطي
إلى جميع الأسئلة حسب الحاجة.

لتحسين الطريقة التي يتم بها عرض أسئلة `matrix` عند
الاستجابة، يُنصح بإضافة نوع سؤال `note` (مميز باللون الأصفر
في الصورة أدناه) ثم تضمين منطق التخطي له حسب الاقتضاء. هذا
اختياري تماماً لأنه سيؤثر ببساطة على تنسيق سؤال
`matrix`. يتم توضيح الفرق بين _استخدام_ و _عدم استخدام_ نوع سؤال `note`
أدناه في **الخطوة 6: جمع البيانات**.

![XLSForm formbuilder Approach](images/adding_skip_to_matrix/formbuilder_xlsform.png)

**الخطوة 4:** استبدال XLSForm:

قم بتحميل واستبدال XLSForm الخاص بك في المشروع الحالي، أو أنشئ مشروعاً جديداً
(إذا لزم الأمر).

**الخطوة 5:** نشر النموذج:

بمجرد استبدال XLSForm (أو تحميل XLSForm كمشروع جديد)،
ستحتاج إلى نشر النموذج الخاص بك.

**الخطوة 6:** جمع البيانات:

بعد نشر النموذج، يمكنك الانتقال إلى **FORM>Collect Data>OPEN** لبدء
جمع البيانات باستخدام نموذج الويب.

**شاشة إدخال البيانات كما تظهر في Enketo (نموذج الويب): _عندما لا يتم إدخال أي شيء_.**

![Empty Enketo Form formbuilder Approach](images/adding_skip_to_matrix/formbuilder_enketo_form_empty.png)

**شاشة إدخال البيانات كما تظهر في Enketo (نموذج الويب) مع إضافة نوع سؤال `note`:
_عندما يتم ملء سؤال `matrix`_.**

![Filledup Enketo Form formbuilder Approach](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_no_issue.png)

كما ترى في الصورة أعلاه، لم يتم تشويه تنسيق سؤال `matrix`. هذه هي الطريقة التي سيتم بها عرض جدول `matrix` عندما تستخدم
نوع سؤال `note` الذي تم تمييزه في الصورة المشتركة سابقاً.

**شاشة إدخال البيانات كما تظهر في Enketo (نموذج الويب) بدون إضافة نوع سؤال `note`:
_عندما يتم ملء سؤال `matrix`_.**

![Filledup Enketo Form formbuilder Approach](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_with_issue.png)

في هذه الحالة، تم تشويه تنسيق سؤال `matrix`. هذا هو
جدول `matrix` الذي سيتم عرضه عندما لا يتم استخدام نوع سؤال `note`.

<p class="note">
  يمكنك الوصول إلى XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls"
    >هنا</a
  >
  الذي تم استخدامه لهذه الطريقة
  <em
    >(إضافة منطق التخطي إلى سؤال <code>matrix</code> باستخدام طريقة
    أداة إنشاء النماذج)</em
  >.
</p>

## طريقة `kobo--matrix_list`:

تماماً كما هو الحال مع طريقة أداة إنشاء النماذج، تعمل هذه الطريقة لإضافة منطق التخطي باستخدام
XLSForm مع **Enketo** باستخدام **تخطيط نمط الشبكة**.

اتبع الخطوات أدناه لإضافة منطق التخطي إلى سؤال `matrix` باستخدام XLSForm
باستخدام طريقة `kobo--matrix_list`.

**الخطوة 1:** إنشاء سؤال `matrix` في XLSForm:

أنشئ سؤال `matrix` في XLSForm، كما هو موضح في مقالة الدعم
**[نوع استجابة مصفوفة الأسئلة](matrix_response.md)**.

**الخطوة 2:** إضافة رأس عمود `relevant` ومنطق التخطي إلى XLSForm الخاص بك:

بمجرد أن يصبح سؤال `matrix` جاهزاً، يجب عليك إضافة رأس العمود `relevant`.
يمكنك الآن إضافة منطق التخطي إلى جميع الأسئلة تحت رأس العمود
`relevant`.

![XLSForm kobo_matrix Approach](images/adding_skip_to_matrix/kobo_matrix_xlsform.png)

**الخطوة 3:** تحميل XLSForm:

إذا كان XLSForm الخاص بك جاهزاً، قم بتحميله كمشروع جديد.

**الخطوة 4:** نشر النموذج:

بمجرد تحميل XLSForm، ستحتاج إلى نشر النموذج الخاص بك.

**الخطوة 5:** جمع البيانات:

يمكنك الآن الانتقال إلى **FORM>Collect Data>OPEN** لبدء جمع البيانات.

**شاشة إدخال البيانات كما تظهر في Enketo (نموذج الويب): _عندما لا يتم إدخال أي شيء_.**

![Empty Enketo Form kobo_matrix Approach](images/adding_skip_to_matrix/kobo_matrix_enketo_form_empty.png)

**شاشة إدخال البيانات كما تظهر في Enketo (نموذج الويب): _عندما يتم ملء سؤال `matrix`_.**

![Filledup Enketo Form kobo_matrix Approach](images/adding_skip_to_matrix/kobo_matrix_enketo_form_filled.png)

كما ترى في الصورة الثانية، تم تشويه تنسيق سؤال `matrix`. في طريقة `kobo--matrix_list` ليس لديك المساحة لإصلاح
جدول `matrix` كما كان لديك مع طريقة أداة إنشاء النماذج.

<p class="note">
  يمكنك الوصول إلى XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question_kobo_matrix.xls"
    >هنا</a
  >
  الذي تم استخدامه لهذه الطريقة
  <em
    >(إضافة منطق التخطي إلى سؤال <code>matrix</code> باستخدام
    طريقة <code>kobo--matrix_list</code>)</em
  >.
</p>