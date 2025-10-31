# خدمات REST
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/7ca46b8455887292b012aeb709e7e244245bf6b9/source/rest_services.md" class="reference">7 يوليو 2023</a>

**كيفية ربط بياناتك بخوادم أو خدمات أخرى باستخدام خدمات REST**

يحتوي KoboToolbox على عدد من الخصائص المتقدمة المدمجة بناءً على مكتباتنا مفتوحة المصدر، والتي تتضمن إضافات مفيدة لحالات الاستخدام المتقدمة.

يمكنك ربط البيانات التي تم جمعها باستخدام KoboToolbox بخوادم أو خدمات أخرى قد تمتلكها من خلال خدمات REST. تدعم خدمات REST تنسيقات JSON أو XML، والمصادقة الأساسية. علاوة على ذلك، من الممكن إرسال مجموعة فرعية فقط من الحقول.

في حالة الفشل، ستحاول المهمة في الخلفية إرسال البيانات 3 مرات (المرة الأولى بعد 60 ثانية، والمرة الثانية بعد 600 ثانية، والمرة الثالثة بعد 6000 ثانية). يمكن تفعيل إشعارات البريد الإلكتروني لتلقي تقرير الفشل.

يرجى ملاحظة أن بياناتك يتم إرسالها إلى الخادم الخارجي فقط عند الإنشاء. لا يتم إرسال أي شيء عند تحرير البيانات.

فيما يلي بعض مقاطع الفيديو التعليمية لاستخدام خدمات REST:

1. الإنشاء

    [![الإنشاء](/images/rest_services/thumbnail_1.jpg)](https://fast.wistia.net/embed/iframe/6i2hw2gcr1 "Creation")

2. مجموعة فرعية من الحقول (تتم إضافة الحقول بالضغط على "Enter" أو "Tab")

    [![مجموعة فرعية من الحقول](/images/rest_services/thumbnail_2.jpg)](https://fast.wistia.net/embed/iframe/u6su0atm2w "Subset of fields")

3. الفشل/إعادة المحاولة

    [![الفشل / إعادة المحاولة](/images/rest_services/thumbnail_3.jpg)](https://fast.wistia.net/embed/iframe/7my5eab5lm "Failure / Retry")

4. غلاف مخصص (متاح فقط مع تنسيق JSON)

    [![غلاف مخصص](/images/rest_services/thumbnail_4.jpg)](https://fast.wistia.net/embed/iframe/pd0czyksbx "Custom Wrapper")