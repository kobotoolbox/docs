# Seleccionar opciones de un archivo externo en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_from_file_xls.md" class="reference">23 Apr 2026</a>

Las preguntas de **selección desde archivo** te permiten usar una lista de opciones almacenada en un archivo externo en lugar de definirlas directamente en tu formulario. Hay dos tipos: `select_one_from_file` para seleccionar una **única opción**, y `select_multiple_from_file` para seleccionar **múltiples opciones**.

Usar un archivo separado para tu lista de opciones facilita la gestión de listas largas, su reutilización en múltiples formularios y la actualización de opciones cuando sea necesario. Los formatos de archivo compatibles incluyen CSV, XML y GeoJSON.

Este artículo explica cómo formatear tu archivo externo, configurar tu XLSForm para usar preguntas de **selección desde archivo** y cargar tu archivo externo en KoboToolbox.

<p class="note">
<strong>Nota:</strong> Este artículo se centra en agregar preguntas de selección desde archivo en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agregar preguntas de selección desde archivo en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/external_file.html">Seleccionar opciones de archivos externos en el Formbuilder</a>.
<br><br>
Para practicar con preguntas de selección desde archivo en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Formatear listas de opciones externas

Para comenzar, crea tu lista de opciones en un archivo externo separado. La estructura requerida de este archivo depende del formato que elijas (CSV, XML o GeoJSON). Usa un archivo separado para cada lista de opciones.

<p class="note">
Para obtener más información sobre cómo formatear archivos XML o GeoJSON, consulta la documentación de <a href="https://xlsform.org/en/#multiple-choice-from-file">XLSForm</a> y de <a href="https://docs.getodk.org/form-datasets/#building-selects-from-geojson-files">ODK</a>. Los archivos GeoJSON se usan principalmente para <a href="https://support.kobotoolbox.org/es/select_from_map_xls.html">seleccionar opciones de un mapa</a>.
</p>

Para archivos CSV, la estructura es similar a la **hoja choices** en un XLSForm. Debe incluir las columnas `name` y `label`, pero la columna `list_name` no es necesaria.

**Archivo CSV externo**

| name    | label     |
|:--------|:----------|
| option1 | Option 1  |
| option2 | Option 2  |
| option3 | Option 3  |

Si tu archivo usa nombres diferentes para el nombre y la etiqueta de la opción, puedes especificarlo en tu XLSForm (consulta las instrucciones [a continuación](https://support.kobotoolbox.org/es/select_from_file_xls.html#configuring-choice-name-and-label-columns)).

<p class="note">
<strong>Nota:</strong> Usa nombres de archivo cortos y simples para tus archivos externos, evitando espacios o caracteres especiales. El nombre del archivo se usará en tu XLSForm para vincular las preguntas con sus listas de opciones. Si usas varios archivos externos, asegúrate de que cada uno tenga un nombre único, incluso si usan diferentes tipos de archivo.
</p>

## Configurar tu XLSForm

Para agregar una pregunta de selección desde archivo a tu XLSForm:
1. En la columna `type` de la **hoja survey**, ingresa el tipo de pregunta de selección desde archivo (`select_one_from_file` o `select_multiple_from_file`).
2. En la misma celda, en lugar del `list_name` de las opciones, agrega un espacio y el nombre del archivo externo, incluyendo la extensión del archivo.
    - Por ejemplo: `select_one_from_file households.csv`

**hoja survey**

| type                     | name | label           |
|:-------------------------|:-----|:----------------|
| select_one_from_file households.csv | hh   | Select household |
| survey |

### Configurar las columnas de nombre y etiqueta de las opciones

Si tu archivo externo usa nombres de columna diferentes en lugar de `name` y `label`:
1. Agrega una columna `parameters` a la **hoja survey**
2. En la fila de la pregunta de selección desde archivo, especifica los nombres personalizados con los parámetros `value` y `label`.
    - `value` representa el `name` de la opción.
    - `label` representa el `label` de la opción.

**hoja survey**

| type                     | name | label            | parameters                   |
|:-------------------------|:-----|:-----------------|:-----------------------------|
| select_one_from_file households.csv | hh   | Select household | value=housenum label=housename |
| survey |

## Cargar el archivo externo en KoboToolbox

Al cargar tu XLSForm en KoboToolbox, también debes cargar el archivo externo que contiene tu lista de opciones:
1. En KoboToolbox, ve a la página **CONFIGURACIÓN** del proyecto.
2. En la ventana **Media**, carga el archivo externo. Asegúrate de que el nombre del archivo coincida exactamente con el nombre especificado en el XLSForm.

Para actualizar tu lista de opciones, edita el archivo externo según sea necesario, vuelve a cargarlo en KoboToolbox y vuelve a implementar tu formulario.

![Upload media](images/select_from_file_xls/upload_media.png)

<p class="note">
Para obtener más información sobre cómo cargar archivos multimedia, consulta <a href="https://support.kobotoolbox.org/es/upload_media.html">Importar archivos multimedia a un proyecto</a>.
</p>

## Resolución de problemas

<details>
  <summary><strong>Listas de opciones traducidas</strong></summary>
  Las preguntas de selección desde archivo no admiten actualmente <a href="https://support.kobotoolbox.org/es/language_xls.html">listas de opciones traducidas</a>. Tu archivo de opciones externo solo puede incluir una única columna <code>label</code>. Las columnas <code>label</code> adicionales con traducciones serán ignoradas en los formularios web o causarán un error en KoboCollect. Para formularios que incluyan traducciones, usa listas de opciones internas, o configura múltiples preguntas de <strong>selección desde archivo</strong> usando lógica de omisión para extraer opciones de diferentes archivos según el idioma del formulario.
</details>

<br>

<details>
  <summary><strong>CSV no encontrado</strong></summary>
  Si ves un error al abrir tu formulario que indica que no se puede encontrar el archivo CSV, verifica que el archivo comience con las columnas <code>name</code> y <code>label</code>. Si las columnas tienen nombres diferentes, asegúrate de que la columna <code>parameters</code> incluya los parámetros <code>value</code> y <code>label</code>.
</details>