# Inclure les P-Codes dans les données exportées
<a href="../p_codes.html">Read in English</a> | <a href="../es/p_codes.html">Leer en español</a> | <a href="../ar/p_codes.html">اقرأ باللغة العربية</a>
**Dernière mise à jour :** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/p_codes.md" class="reference">29 Jul 2025</a>

Si vous utilisez des listes en cascade, veuillez [suivre les instructions](cascading_select.md)
pour les sélections en cascade.

Normalement, seul le « Name » et NON le « Label » apparaîtra dans votre fichier Excel
exporté, ce qui signifie que seul le P-code OU le nom du lieu apparaîtra.

Afin d'obtenir **à la fois le P-code et le nom** dans vos données exportées, procédez
comme suit :

1. Dans toutes les colonnes « Name » de votre formulaire exporté, utilisez le P-code du lieu
2. Dans toutes les colonnes « Label » de votre formulaire exporté, utilisez le nom du lieu
3. Pour chaque niveau administratif que vous utilisez, ajoutez une question de type « calculate », en utilisant la
   syntaxe :

`if(string-length(${name_of_pcode_column}) != 0,jr:choice-name(${name_of_pcode_column},'${name_of_pcode_column}'),'(unspecified name_of_pcode_column)')`

<p class="note">Cette formule extraira le « Label » (c'est-à-dire le nom du lieu) de l'entrée, et vous obtiendrez dans vos résultats exportés à la fois le nom et le p-code.</p>

## Exemple avec 3 niveaux administratifs, utilisant des listes en cascade

**feuille survey**

| type              | name         | label   | choice_filter                                    | calculation                                                                                                               |
| :---------------- | :----------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| select_one admin1 | pcode_admin1 | Admin 1 |                                                  |                                                                                                                           |
| select_one admin2 | pcode_admin2 | Admin 2 | state=${pcode_admin1}                            |                                                                                                                           |
| select_one admin3 | pcode_admin3 | Admin 3 | state=${pcode_admin1} and county=${pcode_admin2} |                                                                                                                           |
| calculate         | name_admin1  |         |                                                  | if(string-length(${pcode_admin1}) != 0, jr:choice-name(${pcode_admin1}, '${pcode_admin1}'), '(unspecified pcode_admin1)') |
| calculate         | name_admin2  |         |                                                  | if(string-length(${pcode_admin2}) != 0, jr:choice-name(${pcode_admin2}, '${pcode_admin2}'), '(unspecified pcode_admin2)') |
| calculate         | name_admin3  |         |                                                  | if(string-length(${pcode_admin3}) != 0, jr:choice-name(${pcode_admin3}, '${pcode_admin3}'), '(unspecified pcode_admin3)') |
| survey |

**feuille choices**

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