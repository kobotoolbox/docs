# نوع سؤال الإقرار
<a href="../acknowledge.html">Read in English</a> | <a href="../fr/acknowledge.html">Lire en français</a> | <a href="../es/acknowledge.html">Leer en español</a>
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/cbfd264f05913df75ec184d5d9eb002f6e66f905/source/acknowledge.md" class="reference">17 يوليو 2025</a>

يعرض نوع سؤال "الإقرار" خيارًا واحدًا، لتحديد "موافق" في النموذج.

يمكنك استخدام نوع "الإقرار" للأسئلة التي تتطلب حالتين فقط من الاستجابة: تمت الإجابة ولم تتم الإجابة، أو مقبول وغير مقبول. يمكنك استخدام نوع السؤال هذا مع موافقة مستنيرة في نموذج الاستبيان الخاص بك، أو كوسيلة لضمان أن الشخص المُستجوَب قد قرأ ووافق على الشروط، والتي عادةً ما يتم توضيحها باستخدام [نوع سؤال "ملاحظة"](question_types.md).

## كيفية إعداد السؤال

1. في أداة إنشاء النماذج، انقر على زر <i class="k-icon k-icon-plus"></i> لإضافة سؤال جديد.
2. اكتب نص السؤال. على سبيل المثال، "إذا كنت توافق على المتابعة في الاستبيان، انقر على موافق."
3. انقر على "<i class="k-icon k-icon-plus"></i> إضافة سؤال" (أو اضغط على مفتاح Enter في لوحة المفاتيح).
4. اختر نوع السؤال "<i class="k-icon k-icon-qt-acknowledge"></i> إقرار".

![إضافة سؤال الإقرار](images/acknowledge/acknowledge_adding.gif)

## كيفية عرضه في النماذج الإلكترونية وتطبيق KoboCollect

يعرض سؤال "الإقرار" زر اختيار واحد بتسمية "موافق" كما هو موضح أدناه:

![أسئلة الإقرار في KoboCollect وEnketo](images/acknowledge/acknowledge.png)

## استخدام منطق التخطي ومعايير التحقق

سؤال "الإقرار" له حالتان فقط من الاستجابة: حالة تمت فيها الإجابة على السؤال، وحالة لم تتم فيها الإجابة، أي أن قيمة الاستجابة إما "موافق" أو _فارغة_.

![أسئلة الإقرار في منطق التخطي](images/acknowledge/acknowledge_skip.gif)

في المثال أعلاه، ستظهر مجموعة "الاستبيان" فقط إذا تمت الإجابة على سؤال "الإقرار" (نقر المستخدم على موافق).

فيما يلي منطق النموذج المكافئ بصيغة XLSForm:

**ورقة survey**

| type        | name    | label                                                       | relevant          |
| :---------- | :------ | :---------------------------------------------------------- | :---------------- |
| acknowledge | consent | إذا كنت توافق على المتابعة في الاستبيان، انقر على موافق     |                   |
| begin_group | survey  | الاستبيان                                                   | ${consent} = "OK" |
| text        | name    | ما اسمك؟                                                    |                   |
| integer     | age     | كم عمرك؟                                                    |                   |
| end_group   |         |                                                             |                   |
| survey |

<p class="note">
  يمكنك تنزيل نموذج XLSForm المثال
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >من هنا <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>