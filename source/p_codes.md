# Including P-Codes in the Output Data
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/p_codes.md" class="reference">29 Jul 2025</a>


If using cascading lists, please [follow the instructions](cascading_select.md)
for cascading selects.

Normally, only the "Name" and NOT the "Label" will appear in your exported Excel
file, which means that only the P-code OR the name of the location will appear.

In order to get **both P-code and name** as part of your exported data, do the
following:

1. In all "Name" columns of your exported form, use the P-code of the location
2. In all "Label' columns of your exported form, use the name of the location
3. For each Admin level you use, add a question with type "calculate", using the
   syntax:

`if(string-length(${name_of_pcode_column}) != 0,jr:choice-name(${name_of_pcode_column},'${name_of_pcode_column}'),'(unspecified name_of_pcode_column)')`

<p class="note">This formula will extract the "Label" (i.e. the name of the location) of the entry, and you will in your exported results get both the name and the p-code.</p>

## Example with 3 admin levels, using cascading lists

**survey sheet**

| type              | name         | label   | choice_filter                                    | calculation                                                                                                               |
| :---------------- | :----------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| select_one admin1 | pcode_admin1 | Admin 1 |                                                  |                                                                                                                           |
| select_one admin2 | pcode_admin2 | Admin 2 | state=${pcode_admin1}                            |                                                                                                                           |
| select_one admin3 | pcode_admin3 | Admin 3 | state=${pcode_admin1} and county=${pcode_admin2} |                                                                                                                           |
| calculate         | name_admin1  |         |                                                  | if(string-length(${pcode_admin1}) != 0, jr:choice-name(${pcode_admin1}, '${pcode_admin1}'), '(unspecified pcode_admin1)') |
| calculate         | name_admin2  |         |                                                  | if(string-length(${pcode_admin2}) != 0, jr:choice-name(${pcode_admin2}, '${pcode_admin2}'), '(unspecified pcode_admin2)') |
| calculate         | name_admin3  |         |                                                  | if(string-length(${pcode_admin3}) != 0, jr:choice-name(${pcode_admin3}, '${pcode_admin3}'), '(unspecified pcode_admin3)') |
| survey |

**choices sheet**

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
