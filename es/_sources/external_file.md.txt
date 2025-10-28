# Tipo de pregunta Seleccionar Uno o Varios de un Archivo Externo
<a href="../external_file.html">Read in English</a> | <a href="../fr/external_file.html">Lire en français</a> | <a href="../ar/external_file.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/87ff8377b846dacb801191e0b619126a563040a9/source/external_file.md" class="reference">28 ago 2025</a>

En algunos casos, puede ser deseable alojar una lista de opciones de respuesta en un
archivo externo, en lugar de directamente en el XLSForm del proyecto. Por ejemplo, una
lista larga de opciones (por ejemplo, cientos o miles) podría ralentizar la carga y
navegación del formulario, o agregar nuevas opciones de respuesta después de que la recolección de datos haya
comenzado podría ser problemático en ocasiones.

<p class="note"> <b>Nota:</b> Este artículo cubre los pasos para configurar preguntas de Seleccionar Uno o Varios de un Archivo Externo en XLSForm. Para configurar estas preguntas en el Formbuilder, primero debes cargar el archivo de opciones externas a KoboToolbox, en la pestaña <b>Medios</b> de la página <b>CONFIGURACIÓN</b>. Una vez que el archivo haya sido cargado, los tipos de pregunta Seleccionar Uno o Varios de un Archivo Externo aparecerán en el Formbuilder. </p>

![image](/images/external_file/select_from_file.png)

Este artículo proporciona un ejemplo detallado y un método para crear un tipo de pregunta
`select_one` o `select_many` con la lista de opciones en un archivo separado y externo. Consulta la
[documentación de XLSForm](https://xlsform.org/en/#multiple-choice-from-file) para
más información.

**1.** En el XLSForm, el tipo debe ser
`select_one_from_file [nombre del archivo]` o `select_multiple_from_file [nombre del archivo]`:

<p class="note">El tipo de archivo puede ser <code>CSV</code> o <code>XML</code></p>

**hoja survey**

| type                            | name   | label                         |
| :------------------------------ | :----- | :---------------------------- |
| text                            | name   | ¿Cuál es tu nombre?            |
| select_one sex                  | sex    | ¿Cuál es tu sexo?             |
| select_one_from_file fruits.csv | fruits | ¿Cuál es tu fruta favorita? |
| survey |

**hoja choices**

| list_name | name | label  |
| :-------- | :--- | :----- |
| sex       | 1    | Masculino   |
| sex       | 2    | Femenino |
| choices |

<p class="note">El <code>fruits.csv</code> es el nombre del archivo que contiene las opciones para la pregunta "¿Cuál es tu fruta favorita?".</p>

**2.** Crea un nuevo archivo `CSV` y estructúralo de la misma manera que la hoja `choices`
en el XLSForm:

**fruits.csv**

| list_name | name | label       |
| :-------- | :--- | :---------- |
| fruits    | 1    | Manzana       |
| fruits    | 2    | Sandía  |
| fruits    | 3    | Naranja      |
| fruits    | 4    | Pera        |
| fruits    | 5    | Cereza      |
| fruits    | 6    | Fresa  |
| fruits    | 7    | Nectarina   |
| fruits    | 8    | Uva       |
| fruits    | 9    | Mango       |
| fruits    | 10   | Arándano   |
| fruits    | 11   | Granada |

**3.** Carga y despliega el XLSForm en KoboToolbox.

**4.** Carga el archivo `CSV` de la misma manera que
[agregarías un archivo de medios al formulario](media.md)