# Seleccionar opciones de archivos externos en el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/a476e76f62e857ee7dd45ee394421eb4bf7dd22a/source/external_file.md" class="reference">21 Mar 2026</a>

Las preguntas de tipo **Seleccionar de un archivo** te permiten usar una lista de opciones almacenada en un archivo externo en lugar de definirlas directamente en tu formulario. Existen dos tipos:
* **Seleccionar una de un archivo** para seleccionar una sola opción
* **Seleccionar varias de un archivo** para seleccionar múltiples opciones

Usar un archivo separado para tu lista de opciones facilita el uso y la gestión de listas largas en el Formbuilder. Los formatos de archivo compatibles incluyen CSV, XML y GeoJSON.

Este artículo explica cómo dar formato a tu archivo externo, cargarlo en KoboToolbox y configurar preguntas de tipo **seleccionar de un archivo** en el Formbuilder.

## Dar formato a listas de opciones externas

Para comenzar, crea tu lista de opciones en un archivo externo separado. La estructura requerida de este archivo depende del formato que elijas (CSV, XML o GeoJSON). Usa un archivo separado para cada lista de opciones.

<p class="note">
Para obtener más información sobre cómo dar formato a archivos XML o GeoJSON, consulta la documentación de <a href="https://xlsform.org/en/#multiple-choice-from-file">XLSForm</a> y <a href="https://docs.getodk.org/form-datasets/#building-selects-from-geojson-files">ODK</a>. Los archivos GeoJSON se usan principalmente para <a href="https://support.kobotoolbox.org/es/select_from_map_xls.html">seleccionar opciones de un mapa</a>.
</p>

Si usas un archivo CSV para tus opciones de respuesta, debe contener al menos dos columnas: `name` y `label`.
* La columna `name` representa el [valor XML](https://support.kobotoolbox.org/es/question_types.html#setting-xml-values-for-option-choices) de tu opción de respuesta.
* La columna `label` representa la etiqueta de la opción tal como se muestra en tu formulario.

**Archivo CSV externo**

| name    | label    |
|:--------|:---------|
| option1 | Option 1 |
| option2 | Option 2 |
| option3 | Option 3 |

Si tu archivo usa nombres diferentes para el nombre y la etiqueta de la opción, puedes [especificarlo](https://support.kobotoolbox.org/es/select_from_file_xls.html#configuring-choice-name-and-label-columns) [descargando tu archivo como XLSForm](https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) y añadiendo una columna `parameters`.

<p class="note">
<strong>Nota:</strong> Usa nombres de archivo cortos y simples para tus archivos externos, evitando espacios o caracteres especiales. El nombre del archivo se usará para vincular las preguntas con sus listas de opciones. Si usas varios archivos externos, asegúrate de que cada uno tenga un nombre único, aunque usen diferentes tipos de archivo.
</p>

## Cargar el archivo externo en KoboToolbox

Antes de crear una pregunta de tipo **seleccionar de un archivo** en el Formbuilder, debes cargar el archivo externo que contiene tu lista de opciones:

1. En KoboToolbox, ve a la página **CONFIGURACIÓN** del proyecto.
2. En la ventana **Media**, carga el archivo externo. Asegúrate de que el nombre del archivo coincida exactamente con el nombre especificado en el XLSForm.

Para actualizar tu lista de opciones, edita el archivo externo según sea necesario, vuelve a cargarlo en KoboToolbox y vuelve a implementar tu formulario.

![Upload media](images/external_file/upload_media.png)

<p class="note">
  Para obtener más información sobre cómo cargar archivos multimedia, consulta <a href="https://support.kobotoolbox.org/es/upload_media.html">Importar archivos multimedia a un proyecto</a>.
</p>

## Configurar la pregunta en el Formbuilder

Después de cargar tu archivo CSV externo en KoboToolbox, puedes añadir una pregunta de tipo **Seleccionar una de un archivo** o **Seleccionar varias de un archivo** en el Formbuilder.

Para añadir una pregunta de tipo seleccionar de un archivo:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ AGREGAR PREGUNTA**.
4. Elige <i class="k-icon-qt-select-one-from-file"></i> **Seleccionar una de un archivo** o <i class="k-icon-qt-select-many-from-file"></i> **Seleccionar varias de un archivo** como tipo de pregunta.

![Select questions](images/external_file/select.png)

<p class="note">
<strong>Nota:</strong> Los tipos de pregunta <strong>Seleccionar una de un archivo</strong> y <strong>Seleccionar varias de un archivo</strong> solo aparecen como opciones en el Formbuilder si se ha cargado un archivo de opciones externo en KoboToolbox.
</p>

Si solo se ha cargado un archivo externo en tu proyecto, se vinculará automáticamente a la pregunta. Si se han cargado varios archivos, abre la <i class="k-icon-settings"></i> **Configuración** de la pregunta y selecciona el archivo apropiado en el menú desplegable <i class=""></i> **Archivo de opciones**.

![Choices file](images/external_file/choices_file.png)

<p class="note">
Para aprender a configurar preguntas de tipo seleccionar de un archivo en XLSForm y obtener ayuda adicional para la resolución de problemas, consulta <a href="https://support.kobotoolbox.org/es/select_from_file_xls.html#">Seleccionar opciones de un archivo externo en XLSForm</a>.
</p>