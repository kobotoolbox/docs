# Exportar y descargar datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/43efdbb222e3213fa548509bb34819c5238f7e83/source/export_download.md" class="reference">6 de mayo de 2026</a>


<iframe src="https://www.youtube.com/embed/bXzwvvnhj7U?cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Al usar KoboToolbox, puedes descargar los datos recolectados en varios formatos y personalizar la configuración de exportación. Este artículo explica cómo descargar los datos recolectados, incluida una descripción general de los tipos de exportación y los formatos disponibles.

## Descargar los datos

Para descargar los datos:

1. Abre tu proyecto y navega a **DATOS > Descargas**.
2. Elige la configuración de exportación (detallada a continuación).
3. Haz clic en **EXPORTAR**. Esto generará una exportación que se mostrará en una tabla debajo de la configuración de exportación.
4. Haz clic en **DESCARGAR** para descargar el archivo exportado.

![Ejemplo de exportación de datos](images/export_download/export.png)

<p class="note">
    <strong>Nota:</strong> Una exportación puede tardar desde unos pocos segundos hasta varios minutos en generarse, según el número de envíos, el tamaño del formulario y la carga del servidor. Una vez creada, aparecerá en la sección <strong>Exportaciones</strong> de la página.
</p>

## Tipos de exportación

Puedes elegir entre los siguientes tipos de exportación:

| **Tipo de exportación** | **Descripción** |
| :----------------- | :--------------------------------------------- |
| XLS | Archivo de Microsoft Excel (formato .xlsx). Este tipo de archivo es el recomendado para recolectar datos de grupos de repetición. |
| CSV | Archivo de valores separados por comas. Este tipo de archivo es ideal para importar en la mayoría de los programas de manejo de datos, incluidas las bases de datos. |
| GeoJSON | Es un formato abierto estándar de intercambio de datos geoespaciales, ideal para integrarse con software GIS como ArcGIS. Este tipo de archivo es el recomendado para <a href="https://support.kobotoolbox.org/es/mapping_gps.html#exporting-as-geojson">analizar datos GPS</a>. |
| Etiquetas SPSS | Genera un <a href="https://support.kobotoolbox.org/es/converting_to_spss_and_stata.html">archivo de sintaxis SPSS</a> que aplica etiquetas de preguntas y etiquetas de valores a las variables de los datos de KoboToolbox importados en SPSS. |
| Coordenadas GPS (KML) | Genera un <a href="https://support.kobotoolbox.org/es/mapping_gps.html#exporting-as-kml">archivo KML</a> para trabajar con los datos en software GIS, como Google Earth. Este formato de exportación no tendrá soporte en el futuro. Recomendamos usar uno de los otros tipos de exportación disponibles. |
| Archivos multimedia adjuntos (ZIP) | Descarga un archivo ZIP que contiene todos los <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#downloading-media-files">archivos multimedia</a> recolectados a través del formulario. |
| XLS (anterior/legacy) | Genera un archivo .xlsx (Microsoft Excel) usando una interfaz anterior de KoboToolbox. Usa esta opción solo en caso de problemas ocasionales con las exportaciones estándar de XLS y CSV, ya que se eliminará en una actualización futura. |
| CSV (anterior/legacy) | Genera un archivo CSV usando una interfaz anterior de KoboToolbox. Usa esta opción solo en caso de problemas ocasionales con las exportaciones estándar de XLS y CSV, ya que se eliminará en una actualización futura. |

<p class="note">
    Para obtener más información sobre los tipos de exportación, consulta <a href="https://support.kobotoolbox.org/es/mapping_gps.html#exporting-gps-data">Mapear datos GPS</a> y <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#downloading-media-files">Gestionar respuestas con archivos multimedia</a>.
</p>

## Formato de valores y encabezados

Al usar los formatos de exportación estándar (XLS, CSV, GeoJSON y Etiquetas SPSS), puedes seleccionar el formato de los valores y encabezados de los datos:

| **Formato** | **Descripción** |
| :----------------- | :--------------------------------------------- |
| Etiquetas (predeterminado) | El archivo exportado usa <strong>etiquetas de preguntas</strong> (texto de la pregunta) como encabezados de columna y <strong>etiquetas de opciones</strong> para las respuestas a preguntas de Seleccionar una y Seleccionar varias. |
| Valores y encabezados XML | El archivo exportado usa <strong>nombres de preguntas</strong> (nombres de columnas de datos) como encabezados de columna y <strong>nombres de opciones</strong> (valores XML) para las respuestas. Esta configuración de exportación es la recomendada para importar los datos en software de análisis de datos. |
| Etiquetas en cualquiera de los idiomas definidos | El archivo exportado usa <strong>etiquetas de preguntas y opciones</strong> en cualquiera de los idiomas configurados en el formulario. |

## Opciones avanzadas

Además de personalizar los formatos de valores y encabezados, los formatos de exportación no heredados también ofrecen otras opciones de personalización en la sección **Opciones avanzadas**. Para obtener más información sobre las opciones avanzadas, consulta [Opciones avanzadas para la exportación de datos](https://support.kobotoolbox.org/es/advanced_export.html).

## Resolución de problemas

<details>
    <summary><strong>Exportar datos GPS</strong></summary>
Hay varias opciones para <a href="https://support.kobotoolbox.org/es/mapping_gps.html#exporting-gps-data">descargar datos GPS</a>. Al exportar los datos como CSV o XLS, las coordenadas aparecen en varias columnas: una columna con el conjunto completo de coordenadas y columnas adicionales para latitud, longitud, altitud y precisión. Para preparar los datos para su uso en software GIS como ArcGIS, usa la opción de exportación GeoJSON. El formato de exportación KML es limitado y no tendrá soporte en el futuro.
</details>

<br>

<details>
    <summary><strong>Exportaciones atascadas en estado pendiente o con error</strong></summary>

El tiempo de exportación depende del número de envíos, la complejidad del formulario y la carga actual del servidor. Si las exportaciones permanecen en estado pendiente durante un período prolongado:
- Elimina las exportaciones atascadas haciendo clic en el <i class="k-icon-trash"></i> <strong>icono de papelera.</strong>
- Vuelve a intentar la exportación haciendo clic en el botón <strong>EXPORTAR</strong> nuevamente.
- Evita crear varias exportaciones rápidamente, ya que esto puede sobrecargar el servidor y reducir el rendimiento para todos los usuarios.

<p class="note">
    <strong>Nota:</strong> Las exportaciones agotarán el tiempo de espera y se mostrarán como <strong>fallidas</strong> después de 30 minutos. Este límite a nivel de servidor puede requerir que filtres el número de envíos incluidos en la exportación para completarla dentro del tiempo permitido. En el <a href="https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4">Foro de la comunidad</a> se explica un ejemplo de cómo hacerlo.
</p>

Si continúas teniendo problemas para exportar los datos, publica tu consulta en el <a href="https://community.kobotoolbox.org/">Foro de la comunidad</a>.
</details>

<br>

<details>
    <summary><strong>No se encuentran los datos del grupo de repetición</strong></summary>
Solo el <b>formato XLS</b> admite datos de grupos de repetición. Cada grupo de repetición se exportará <strong>como una hoja separada</strong> en el archivo exportado. Las descargas en CSV solo proporcionarán los datos principales, sin los datos del grupo de repetición.
<br><br>
Para obtener más información sobre cómo exportar y usar datos de grupos de repetición, consulta <a href="https://support.kobotoolbox.org/es/managing_repeat_groups.html">Gestión de datos de grupos repetidos</a>.
</details>

<br>

<details>
    <summary><strong>Algunos datos no se exportan</strong></summary>
    Si algunos de los datos no se exportan, revisa las <a href="https://support.kobotoolbox.org/es/advanced_export.html">opciones avanzadas</a>. Por ejemplo, asegúrate de que todas las versiones del formulario estén seleccionadas para la exportación y de que todas las preguntas que deseas incluir hayan sido seleccionadas.
</details>

<br>

<details>
    <summary><strong>Descargar datos de diferentes versiones</strong></summary>
    Al descargar datos que incluyen varias versiones del formulario, es posible que encuentres cambios en el formato de los archivos de datos.
    <br><br>
Para obtener más información sobre los cambios esperados en la estructura de los datos al trabajar con diferentes versiones de un formulario, consulta <a href="https://support.kobotoolbox.org/es/deploy_form_new_project.html#important-considerations-when-redeploying-a-form">Implementar formularios para la recolección de datos</a>.
</details>

<br>

<details>
    <summary><strong>Pérdida de datos de zona horaria en la exportación</strong></summary>
    Los formatos de hora de Excel no admiten datos de zona horaria. Por lo tanto, cualquier dato de zona horaria en el valor de la respuesta se eliminará durante la exportación XLS. Para conservar esta información, activa la opción de exportar las fechas como valores de texto.
<br><br>
Para obtener más información sobre esta configuración, consulta <a href="https://support.kobotoolbox.org/es/advanced_export.html">Opciones avanzadas para la exportación de datos</a>.
</details>

<br>

<details>
    <summary><strong>Columnas adicionales en la exportación de datos</strong></summary>
     La exportación de datos puede incluir columnas adicionales que no se agregaron como preguntas en el formulario. KoboToolbox incluye <a href="https://support.kobotoolbox.org/es/viewing_validating_data.html#system-generated-submission-fields">campos generados por el sistema</a> para cada envío, como <code>_id</code>, <code>_uuid</code>, <code>_submission_time</code>, <code>_submitted_by</code> y <code>rootUuid</code>.
<br><br>
Además de los campos generados por el sistema que se muestran en la tabla de datos, es posible que se agreguen algunos campos adicionales al exportar los datos.
<br><br>

<ul>
    <li><code>_validation_status</code>: Muestra el <a href="https://support.kobotoolbox.org/es/viewing_validating_data.html#validating-your-data">estado de validación</a> del envío. Esto ayuda a hacer seguimiento de si un envío ha sido revisado y si está listo para usar. Los valores posibles son <strong>Aprobado</strong>, <strong>No aprobado</strong> y <strong>En espera</strong>.</li>
    <li><code>_index</code>: Un número de fila secuencial generado en el momento de la exportación. Se usa principalmente para vincular filas entre la hoja principal y las hojas de grupos de repetición en exportaciones de varias hojas. Como se crea durante la exportación, no debe usarse como identificador estable de un envío.
    </li>
    <li><code>_status</code>: Muestra cómo se envió el formulario. En muchas exportaciones, este campo no es muy útil porque puede contener el mismo valor para todos los registros.
    </li>
    <li>También es posible que veas <code>_notes</code> y <code>_tags</code> en algunas exportaciones. Estos campos están obsoletos, pero aún pueden aparecer en flujos de trabajo de exportación más antiguos o existentes.
    </li>
</ul>

Si no necesitas estas columnas para el análisis, puedes eliminarlas del archivo exportado después de la descarga o al configurar los <a href="https://support.kobotoolbox.org/es/advanced_export.html#selecting-data-fields-for-export">ajustes de exportación</a>.
</details>