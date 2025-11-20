# نوع الاستجابة مصفوفة الأسئلة
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/matrix_response.md" class="reference">29 يوليو 2025</a>

يتيح نوع الاستجابة مصفوفة الأسئلة للمستخدمين إنشاء مجموعة من الأسئلة
التي تُعرض بتنسيق مصفوفة، حيث تمثل كل خلية داخل المصفوفة
سؤالاً منفصلاً. لاستخدام نوع الاستجابة هذا، حدد عدد الصفوف و
الأعمدة التي تريدها في مجموعة المصفوفة الخاصة بك وأعط كل صف وعمود تسمية أو
اسماً. يمكن أن يكون كل عمود نوع سؤال مختلف. في لقطة الشاشة أعلاه،
العمودان الأولان هما أسئلة اختيار واحد، والعمود الثالث هو سؤال
رقمي.

![image](/images/matrix_response/matrix_example.png)

<p class="note">نوع الاستجابة هذا <strong>يعمل فقط عند استخدام Enketo</strong>، باستخدام <strong>تخطيط Grid-theme</strong>. يتم تعيين النماذج إلى تخطيط صفحة واحدة بشكل افتراضي -- لتغييره، ابحث عن زر "layout" في شريط أدوات منشئ النماذج، اختر "grid-theme"، احفظ هذا التغيير، وأعد نشر النموذج الخاص بك لتفعيل هذه التغييرات.</p>

<p class='note'>يدعم Enketo ما يصل إلى <code>10</code> أعمدة فقط في الإصدارات الأقل من <code>2.8.0</code>، وحتى <code>13</code> عموداً في الإصدار <code>2.8.0</code> وما بعده.</p>

## إنشاء مصفوفة أسئلة في منشئ النماذج

1. انتقل إلى منشئ النماذج الخاص بك وانقر على "Add question"
2. اختر 'Question Matrix'

    ![image](/images/matrix_response/question_matrix.png)

3. انقر على أيقونة الترس في كل عمود لتعيين نوع السؤال.

    ![image](/images/matrix_response/question_type.png)

4. اختر نوع السؤال

5. أضف تسمية العمود وتسمية الاستجابة

    ![image](/images/matrix_response/label_response.png)

6. اختر أيقونة الترس داخل 'Row' لتحديد تسمية الصف

    ![image](/images/matrix_response/row.png)

## إنشاء مصفوفة أسئلة في XLSForm

بدلاً من ذلك، يمكنك أيضاً إنشاء سؤال مصفوفة في XLSForm باتباع
التعليمات الموضحة في الصور أدناه:

**ورقة survey**

| type             | name | label                                | required | `kobo--matrix_list` |
| :--------------- | :--- | :----------------------------------- | :------- | :----------------   |
| begin_kobomatrix | M1   | Items                                |          | assets              |
| select_one yn    | Q1   | Q1. Which assets do you have at home | TRUE     |                     |
| integer          | Q2   | Q2. Number of assets                 | TRUE     |                     |
| end_kobomatrix   |      |                                      |          |                     |
| survey |

**ورقة choices**

| list_name | name | label |
| :-------- | :--- | :---- |
| assets    | car  | Car   |
| assets    | bike | Bike  |
| assets    | tv   | TV    |
| yn        | yes  | Yes   |
| yn        | no   | No    |
| choices |

**ورقة settings**

| style                        |
| :--------------------------- |
| theme-grid no-text-transform |
| settings |

<p class="note">تستخدم هذه الطريقة <code>begin_kobomatrix</code> و
<code>end_kobomatrix</code> و <code>kobo--matrix_list</code>.</p>

باتباع الخطوات أعلاه، يجب أن ترى مصفوفة الأسئلة الموضحة في
لقطة الشاشة أدناه (في [Enketo](data_through_webforms.md) فقط):

![image](/images/matrix_response/preview.png)

من الممكن أيضاً تضمين شروط `relevant` و `constraint` داخل
المصفوفة على النحو التالي:

**ورقة survey**

| type             | name | label                                | required | `kobo--matrix_list` | relevant      | constraint |
| :--------------- | :--- | :----------------------------------- | :------- | :----------------   | :------------ | :--------- |
| begin_kobomatrix | M1   | Items                                |          | assets              |               |            |
| select_one yn    | Q1   | Q1. Which assets do you have at home | TRUE     |                     |               |            |
| integer          | Q2   | Q2. Number of assets                 | TRUE     |                     | ${Q1} = 'yes' | . > 2      |
| end_kobomatrix   |      |                                      |          |                     |               |            |
| survey |