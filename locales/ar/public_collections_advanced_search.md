# البحث المتقدم في المجموعات العامة

**آخر تحديث:**
<a href="https://github.com/kobotoolbox/docs/blob/a6ae76d4d566c1139914f03ba8452fdbf122cf11/source/public_collections_advanced_search.md" class="reference">4
مارس 2021</a>

**_يرجى ملاحظة أن إمكانية البحث قيد التطوير، ونخطط لإضافة صيغة أكثر سهولة في الاستخدام في الإصدارات المستقبلية._**

## سلوك البحث الافتراضي

عندما تدخل مصطلحاً في شريط البحث دون تحديد حقل، سيعرض استعلامك نتائج حيث يمكن العثور على هذا المصطلح، بغض النظر عن الأحرف الكبيرة أو الصغيرة، في:

-   اسم الاستبيان أو المجموعة أو السؤال أو الكتلة أو القالب؛
-   اسم المستخدم للمالك؛
-   الوصف؛
-   الملخص، الذي يحتوي على جميع تسميات الأسئلة واللغات؛
-   اسم أي وسم مُعيّن؛
-   المعرّف الفريد للكائن (UID).

على سبيل المثال، البحث الافتراضي بالمصطلح: "_examples_"، سينتج عنه ما يلي:

```
name__icontains:examples OR owner__username__icontains:examples OR
settings__description__icontains:examples OR summary__icontains:examples OR
tags__name__icontains:examples OR uid__icontains:examples
```

![examples](/images/public_collections_advanced_search/advanced_search_1.png)

## عوامل تشغيل حقول البحث الصالحة

عامل تشغيل الحقل هو القيمة بعد آخر شرطة سفلية مزدوجة في حقل البحث، أي `__icontains`.

-   لعمليات البحث **النصية** _الحساسة لحالة الأحرف_، يمكن استخدام عوامل التشغيل التالية:
    `contains`، `exact`، `startswith`
-   لعمليات البحث **النصية** _غير الحساسة لحالة الأحرف_: `icontains`، `iexact`،
    `istartswith`
-   للبحث **الرقمي**، عوامل التشغيل التالية صالحة: `exact`، `lt`،
    `lte`، `gt`، `gte`

لاحظ أنه افتراضياً يتم تعيين عامل التشغيل `exact`، لذلك `name:foo` يعادل `name__exact:foo`

## فهم صيغة حقل البحث

تحاكي صيغة الشرطة السفلية المزدوجة سلوك
[صيغة تصفية كائنات Django](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields)
وتسمح بالتنقل عبر علاقات الكائنات المرتبطة والتسلسلات الهرمية لـ JSON،
مثل تلك الموجودة في نقطة النهاية:

`https://kf.kobotoolbox.org/api/v2/assets/`

على سبيل المثال، إذا كان لأحد الأصول الإعدادات التالية:

```
{
    ...
    "settings": {
        ...
        "country": {
            "label": "United States",
            "value": "USA"
        }
        ...
    },
    ...
}
```

يمكن البحث عن الكائن من خلال الطرق التالية:

```
settings__country__value:USA
```

![examples](/images/public_collections_advanced_search/advanced_search_2.png)

أو بشكل أكثر مرونة:

```
settings__country__value__icontains:usa
```

![examples](/images/public_collections_advanced_search/advanced_search_3.png)

## استخدام محلل الاستعلام

أخيراً، يمكن دمج حقول البحث الموضحة أعلاه باستخدام صيغة
[محلل الاستعلام](https://github.com/kobotoolbox/kpi#searching) لعمليات بحث أكثر دقة. على سبيل المثال:

```
owner__username__icontains:foo AND tags__name__icontains:bar
```

أو:

```
owner__username__icontains:foo AND NOT tags__name__icontains:bar
```

![examples](/images/public_collections_advanced_search/advanced_search_4.png)