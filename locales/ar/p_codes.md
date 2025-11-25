# تضمين الرموز الإدارية (P-Codes) في بيانات المخرجات
**آخر تحديث:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/p_codes.md" class="reference">29 يوليو 2025</a>

إذا كنت تستخدم القوائم المتتالية، يُرجى [اتباع التعليمات](cascading_select.md)
الخاصة بالاختيارات المتتالية.

عادةً، سيظهر "الاسم" (Name) فقط وليس "التسمية" (Label) في ملف Excel المُصدَّر،
مما يعني أن الرمز الإداري (P-code) أو اسم الموقع فقط سيظهر.

للحصول على **كل من الرمز الإداري والاسم** كجزء من بياناتك المُصدَّرة، قم بما يلي:

1. في جميع أعمدة "الاسم" (Name) في النموذج المُصدَّر، استخدم الرمز الإداري للموقع
2. في جميع أعمدة "التسمية" (Label) في النموذج المُصدَّر، استخدم اسم الموقع
3. لكل مستوى إداري تستخدمه، أضف سؤالاً من نوع "calculate"، باستخدام الصيغة التالية:

`if(string-length(${name_of_pcode_column}) != 0,jr:choice-name(${name_of_pcode_column},'${name_of_pcode_column}'),'(unspecified name_of_pcode_column)')`

<p class="note">ستقوم هذه الصيغة باستخراج "التسمية" (Label) (أي اسم الموقع) للإدخال، وستحصل في نتائجك المُصدَّرة على كل من الاسم والرمز الإداري.</p>

## مثال مع 3 مستويات إدارية، باستخدام القوائم المتتالية

**ورقة survey**

| type              | name         | label          | choice_filter                                    | calculation                                                                                                               |
| :---------------- | :----------- | :------------- | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| select_one admin1 | pcode_admin1 | المستوى الإداري 1 |                                                  |                                                                                                                           |
| select_one admin2 | pcode_admin2 | المستوى الإداري 2 | state=${pcode_admin1}                            |                                                                                                                           |
| select_one admin3 | pcode_admin3 | المستوى الإداري 3 | state=${pcode_admin1} and county=${pcode_admin2} |                                                                                                                           |
| calculate         | name_admin1  |                |                                                  | if(string-length(${pcode_admin1}) != 0, jr:choice-name(${pcode_admin1}, '${pcode_admin1}'), '(unspecified pcode_admin1)') |
| calculate         | name_admin2  |                |                                                  | if(string-length(${pcode_admin2}) != 0, jr:choice-name(${pcode_admin2}, '${pcode_admin2}'), '(unspecified pcode_admin2)') |
| calculate         | name_admin3  |                |                                                  | if(string-length(${pcode_admin3}) != 0, jr:choice-name(${pcode_admin3}, '${pcode_admin3}'), '(unspecified pcode_admin3)') |
| survey |

**ورقة choices**

| list_name | name | label       | state | county |
| :-------- | :--- | :---------- | :---- | :----- |
| admin1    | 11   | Texas       |       |        |
| admin1    | 12   | Washington  |       |        |
| admin2    | 13   | King        | 11    |        |
| admin2    | 14   | Pierce      | 11    |        |
| admin2    | 15   | Puyallup    | 12    |        |
| admin2    | 16   | Cameron     | 12    |        |
| admin3    | 17   | Dumont      | 11    | 13     |
| admin3    | 18   | Finney      | 11    | 13     |
| admin3    | 19   | Brownsville | 11    | 14     |
| admin3    | 20   | Harlingen   | 11    | 14     |
| admin3    | 21   | Seattle     | 12    | 15     |
| admin3    | 22   | Redmond     | 12    | 15     |
| admin3    | 23   | Tacoma      | 12    | 16     |
| admin3    | 24   | King        | 12    | 16     |
| choices |