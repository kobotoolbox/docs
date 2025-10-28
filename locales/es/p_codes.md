# Incluir códigos P en los datos de salida
<a href="../p_codes.html">Read in English</a> | <a href="../fr/p_codes.html">Lire en français</a> | <a href="../ar/p_codes.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/p_codes.md" class="reference">29 Jul 2025</a>

Si utilizas listas en cascada, por favor [sigue las instrucciones](cascading_select.md)
para selecciones en cascada.

Normalmente, solo el "Name" y NO el "Label" aparecerá en tu archivo de Excel exportado,
lo que significa que solo el código P O el nombre de la ubicación aparecerá.

Para obtener **tanto el código P como el nombre** como parte de tus datos exportados, haz lo
siguiente:

1. En todas las columnas "Name" de tu formulario exportado, usa el código P de la ubicación
2. En todas las columnas "Label" de tu formulario exportado, usa el nombre de la ubicación
3. Para cada nivel administrativo que uses, agrega una pregunta con tipo "calculate", usando la
   sintaxis:

`if(string-length(${name_of_pcode_column}) != 0,jr:choice-name(${name_of_pcode_column},'${name_of_pcode_column}'),'(unspecified name_of_pcode_column)')`

<p class="note">Esta fórmula extraerá el "Label" (es decir, el nombre de la ubicación) de la entrada, y en tus resultados exportados obtendrás tanto el nombre como el código P.</p>

## Ejemplo con 3 niveles administrativos, usando listas en cascada

**hoja survey**

| type              | name         | label   | choice_filter                                    | calculation                                                                                                               |
| :---------------- | :----------- | :------ | :----------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| select_one admin1 | pcode_admin1 | Admin 1 |                                                  |                                                                                                                           |
| select_one admin2 | pcode_admin2 | Admin 2 | state=${pcode_admin1}                            |                                                                                                                           |
| select_one admin3 | pcode_admin3 | Admin 3 | state=${pcode_admin1} and county=${pcode_admin2} |                                                                                                                           |
| calculate         | name_admin1  |         |                                                  | if(string-length(${pcode_admin1}) != 0, jr:choice-name(${pcode_admin1}, '${pcode_admin1}'), '(unspecified pcode_admin1)') |
| calculate         | name_admin2  |         |                                                  | if(string-length(${pcode_admin2}) != 0, jr:choice-name(${pcode_admin2}, '${pcode_admin2}'), '(unspecified pcode_admin2)') |
| calculate         | name_admin3  |         |                                                  | if(string-length(${pcode_admin3}) != 0, jr:choice-name(${pcode_admin3}, '${pcode_admin3}'), '(unspecified pcode_admin3)') |
| survey |

**hoja choices**

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