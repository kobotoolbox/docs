# Opciones avanzadas para la exportación de datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/b0d195136b7fb3fe51b687cc03a5e8dcde946309/source/advanced_export.md" class="reference">22 Jun 2026</a>


Las opciones avanzadas ofrecen mayor control y flexibilidad al descargar y exportar tus datos. Este artículo te guiará a través de la personalización de tus exportaciones de datos, desde la selección de campos de datos y el manejo de distintos tipos de preguntas hasta la configuración de parámetros para diferentes necesidades de análisis.

<p class="note">
    Para obtener más información sobre la descarga de datos, incluida una descripción general de los tipos de exportación y los formatos disponibles, consulta <a href="https://support.kobotoolbox.org/es/export_download.html?highlight=export">Exportar y descargar datos.</a>
</p>

## Opciones de exportación para preguntas de selección múltiple

La opción **Exportar preguntas de Seleccionar varias como…** te permite elegir cómo exportar los datos de las preguntas de **Seleccionar varias** (también llamadas `select_multiple`). Puedes exportarlas como:

| **Opción de exportación**    | **Descripción**                                |
| :----------------- | :------------------------------------ |
| Columnas individuales y separadas &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Esta configuración predeterminada exporta una columna con todas las opciones seleccionadas de las preguntas de <strong>Seleccionar varias</strong>, más columnas individuales para cada respuesta, como se muestra a continuación.<br> ![How to select many columns](images/advanced_export/select_many_columns.png) |
| Columnas separadas  | Cada respuesta a las preguntas de <strong>Seleccionar varias</strong> se exportará en columnas separadas.|
| Columna individual   | Las respuestas a las preguntas de <strong>Seleccionar varias</strong> se exportarán en una sola columna.            |


Before applying any fix, I need to check the rules carefully.

**Issue 1** (`es_gender_inclusive`, high): The suggestion is to change `"el encuestado no eligió esa opción"` → `"el/la encuestado/a no eligió esa opción"`. But `es_gender_inclusive` targets plural article+noun patterns like `los/as usuarios/as` — it does not apply to singular forms. The suggestion itself even notes this belongs to `es_gender_slash_singular`. Skip this issue.

**Issue 2** (`es_gender_slash_singular`, medium): The suggestion is to change `"el encuestado no eligió esa opción"` → `"el encuestado/a no eligió esa opción"`. But the rule says to use the **standard masculine singular** form — i.e., remove slash constructions, not add them. The `example_correct` column shows `encuestado` (no slash). The suggestion here contradicts the rule: the rule requires `encuestado`, not `encuestado/a`. The original text `el encuestado` is already the correct standard masculine singular form. Skip this issue.

Both fixes would either duplicate another rule's scope or contradict the rule's own stated correction direction. The snippet is returned unchanged.

---SNIPPET---
<p class="note">
  <strong>Nota:</strong> En las columnas separadas, un valor de '1' indica que la opción fue seleccionada, mientras que '0' significa que el encuestado no eligió esa opción.
</p>

## Selección de campos de datos para exportar
---END SNIPPET---

Las opciones de exportación avanzadas te permiten refinar la descarga de datos incluyendo datos de todas las versiones del formulario o seleccionando preguntas específicas para exportar.

| **Configuración de exportación**    | **Descripción**                                |
| :----------------- | :------------------------------------ |
| Incluir campos de las […] versiones &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | De forma predeterminada, esta opción está activada. Te permite descargar datos de todas las versiones del formulario, incluidas las preguntas u opciones eliminadas. Si la desactivas, solo se descargarán los datos de la última versión implementada del formulario. |
| Seleccionar las preguntas que se exportarán | Para exportar datos de preguntas específicas, activa esta opción y selecciona las preguntas que deseas incluir. |
| Rango de fechas | Para exportar datos enviados dentro de un rango de fechas específico, activa esta opción y selecciona las fechas de **inicio** y/o **fin**. Los filtros de fecha se basan en la hora de envío y utilizan la zona horaria UTC. Los envíos realizados en las fechas de inicio y fin se incluyen en las exportaciones. |

![How to select data fields](images/advanced_export/select_data_fields.png)

## Opciones adicionales de formato de datos

KoboToolbox ofrece opciones adicionales de formato de datos para personalizar aún más tus exportaciones, como incluir nombres de grupos en los encabezados, almacenar respuestas de fecha y número como texto, o incluir URLs de archivos multimedia.

| **Configuración de exportación**    | **Descripción**                                |
| :----------------- | :------------------------------------ |
| Incluir grupos en los encabezados | Elige esta opción para agregar nombres de grupos a cada encabezado de pregunta, como se muestra en el ejemplo a continuación. ![Include groups in headers](images/advanced_export/group_headers2.png) | 
| Almacenar las respuestas de fechas y números como texto &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | De forma predeterminada, las preguntas de tipo <strong>Fecha, Fecha y hora, Número</strong> y <strong>Decimal</strong> se guardan con sus tipos de datos correspondientes al exportarlas a XLS. Activa esta opción si prefieres exportarlas como texto.<br><br><strong>Nota:</strong> Los formatos de hora de Excel no admiten datos de zona horaria; por lo tanto, cualquier dato de zona horaria en el valor de la respuesta se eliminará durante la exportación. Para conservar esta información, activa la opción de exportar fechas como valores de texto. |
| Incluir URL de archivos multimedia | Si tu formulario recopiló archivos multimedia (fotos, audio, videos o archivos), activa esta opción para asegurarte de que el archivo exportado incluya enlaces a estos archivos multimedia. |

## Guardar configuración de exportación

Puedes guardar la configuración de exportación definida para uso futuro o para generar un enlace de [exportación sincrónica](https://support.kobotoolbox.org/es/synchronous_exports.html) para software como PowerBI o Excel.

| **Configuración de exportación** | **Descripción**                                |
| :-------------------- | :------------------------------------ |
| Guardar selección como… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Activa esta opción e ingresa un nombre para tu configuración de exportación. Al hacer clic en <strong>EXPORTAR</strong>, esta configuración se guardará y el nombre aparecerá en el cuadro **Aplicar configuración de exportación guardada**. | 

Para usar la configuración de exportación guardada, haz clic en el menú desplegable bajo **Aplicar configuración de exportación guardada** y selecciona la configuración de exportación con el nombre de tu elección.

## Resolución de problemas

<details>
  <summary><strong>Faltan campos de versiones anteriores del formulario en la exportación de datos</strong></summary>
  Si faltan datos de preguntas renombradas o eliminadas en las exportaciones de datos después de que un formulario se edita y se vuelve a implementar, asegúrate de que la opción <strong>Incluir campos de todas las versiones implementadas</strong> esté seleccionada al descargar los datos. Si esta opción no está seleccionada, solo se incluirán los campos de la versión más reciente del formulario. Todos los envíos siempre se incluyen en la descarga; esta opción solo afecta qué campos se incluyen.
</details>

<br>

<details>
  <summary><strong>Las URLs de archivos multimedia de exportaciones anteriores ya no funcionan</strong></summary>
Los usuarios que dependen de URLs de archivos multimedia de exportaciones antiguas de Excel o CSV pueden notar que estos enlaces ya no funcionan desde que <a href="https://support.kobotoolbox.org/es/migrating_api.html">la API v1 fue discontinuada</a>.
<br><br> 
Las URLs afectadas utilizan el formato antiguo: 
<code>https://kc.kobotoolbox.org/media/original?media_file=...</code>
<br><br>
Para solucionar este problema, vuelve a exportar tus datos con la opción <strong>Incluir URL de archivos multimedia</strong> seleccionada. La nueva exportación incluirá URLs de archivos multimedia actualizadas.
</details>