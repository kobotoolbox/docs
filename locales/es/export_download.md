# Exportar y descargar tus datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/8a772b24abadb4e8d54f9716b798c5479432f0e6/source/export_download.md" class="reference">6 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/bXzwvvnhj7U" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Cuando usas KoboToolbox, puedes descargar tus datos recolectados en varios formatos y personalizar tus configuraciones de exportación. Este artículo explica cómo descargar tus datos recolectados, incluyendo una descripción general de los tipos de exportación y formatos disponibles.

## Descargar tus datos

Para descargar tus datos:

1. Abre tu proyecto y navega a **DATOS > Descargas**.
2. Elige tus configuraciones de exportación (detalladas a continuación).
3. Haz clic en **EXPORTAR**. Esto generará una exportación que se mostrará en una tabla debajo de las configuraciones de exportación.
4. Haz clic en **DESCARGAR** para descargar el archivo exportado.

![Exporting data example](images/export_download/export.png)

<p class="note">
    <strong>Nota:</strong> Una exportación puede tardar desde unos segundos hasta varios minutos en generarse, dependiendo del número de envíos, el tamaño del formulario y la carga del servidor. Una vez creada, aparecerá en la sección <strong>Exportaciones</strong> de la página.
</p>

## Tipos de exportación

Puedes elegir entre los siguientes tipos de exportación:

| **Tipo de exportación**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| XLS               | Archivo de Microsoft Excel (formato .xlsx). Este tipo de archivo es recomendado cuando recolectas datos de grupos repetidos.                                  |
| CSV      | Archivo de valores separados por comas. Este tipo de archivo es ideal para importar en la mayoría de software de manejo de datos, incluyendo bases de datos.                                  |
| GeoJSON           | Este es un formato de intercambio de datos geoespaciales de estándar abierto, ideal para integrar con software GIS como ArcGIS.            |
| SPSS Labels           | Genera un archivo de sintaxis SPSS que aplica etiquetas de preguntas y etiquetas de valores a las variables de datos de KoboToolbox importados en SPSS. Para más información, consulta <a href="converting_to_spss_and_stata.html">Convertir datos a SPSS y/o Stata</a>.         |
| GPS Coordinates (KML)               | Genera un archivo KML para trabajar con tus datos en software GIS, como Google Earth.                               |
| Media Attachments (ZIP)               |  Descarga un archivo ZIP que contiene todos los medios recolectados a través del formulario.                               |
| XLS (legacy)              | Genera un archivo .xlsx (Microsoft Excel) usando una interfaz heredada de KoboToolbox. Solo usa esta opción en caso de problemas ocasionales con las exportaciones estándar XLS y CSV, ya que será eliminada en una actualización futura.                                  |
| CSV (legacy)               | Genera un archivo CSV usando una interfaz heredada de KoboToolbox. Solo usa esta opción en caso de problemas ocasionales con las exportaciones estándar XLS y CSV, ya que será eliminada en una actualización futura.                                  |

## Formato de valores y encabezados

Cuando usas los formatos de exportación estándar (XLS, CSV, GeoJSON y SPSS Labels), puedes seleccionar el formato de tus valores de datos y encabezados:

| **Formato**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Labels (default)               | El archivo exportado usa <strong>etiquetas de preguntas</strong> (texto de la pregunta) como encabezados de columna y <strong>etiquetas de opciones</strong> para respuestas a preguntas de Selección Única y Selección Múltiple.                                  |
| XML values and headers      | El archivo exportado usa <strong>nombres de preguntas</strong> (Nombres de Columna de Datos) como encabezados de columna y <strong>nombres de opciones</strong> (valores XML) para respuestas. Esta configuración de exportación es recomendada para importar tus datos en software de análisis de datos.                                  |
| Labels in any of the defined languages           | El archivo exportado usa <strong>etiquetas de preguntas y opciones</strong> en cualquiera de los idiomas configurados dentro del formulario.            |

## Opciones avanzadas

Además de personalizar los formatos de valores y encabezados, los formatos de exportación no heredados también ofrecen otras opciones de personalización dentro de la sección **Opciones Avanzadas**. Para más información sobre opciones avanzadas, consulta [Opciones avanzadas para exportar datos](advanced_export.md).

## Solución de problemas

<details>
    <summary><strong>Exportaciones atascadas en estado pendiente o fallidas</strong></summary>
    
El tiempo de exportación depende del número de envíos, la complejidad del formulario y la carga actual del servidor. Si las exportaciones permanecen en estado pendiente durante un período prolongado:
- Elimina las exportaciones atascadas haciendo clic en el <i class="k-icon-trash"></i> <strong>ícono de papelera.</strong>
- Reintenta la exportación haciendo clic en el botón <strong>EXPORTAR</strong> nuevamente.
- Evita crear múltiples exportaciones rápidamente, ya que esto puede sobrecargar el servidor y reducir el rendimiento para todos/as los/as usuarios/as.

<p class="note">
    <strong>Nota:</strong> Las exportaciones agotarán el tiempo de espera y se mostrarán como <strong>fallidas</strong> después de 30 minutos. Este límite a nivel del servidor puede requerir que filtres el número de envíos incluidos en la exportación para completarla dentro del tiempo permitido. Un ejemplo de cómo hacer esto se discute en el <a href="https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4">Foro de la comunidad</a>.
</p>

Si continúas experimentando problemas al exportar tus datos, por favor publica en el <a href="https://community.kobotoolbox.org/">Foro de la comunidad</a>.
</details>

<br>

<details>
    <summary><strong>Datos de grupos repetidos no encontrados</strong></summary>
Solo el <b>formato XLS</b> soporta datos de grupos repetidos. Cada grupo repetido será exportado <strong>como una hoja separada</strong> en el archivo exportado. Las descargas CSV solo proporcionarán los datos principales, sin datos de grupos repetidos. 
<br><br>
Para más información sobre exportar y usar datos de grupos repetidos, consulta <a href="managing_repeat_groups.html">Manejo de datos de grupos repetidos</a>.    
</details>

<br>

<details>
    <summary><strong>Algunos datos no se están exportando</strong></summary>
    Si algunos de tus datos no se están exportando, verifica las <a href="advanced_export.html">opciones avanzadas</a>. Por ejemplo, asegúrate de que los datos de todas las versiones de tu formulario estén seleccionados para exportación.
</details>

<br>

<details>
    <summary><strong>Descargar datos de diferentes versiones</strong></summary>
    Cuando descargas datos que incluyen múltiples versiones del formulario, puedes encontrar cambios en el formato de tus archivos de datos. 
</details>

<br>

<details>
    <summary><strong>Datos de zona horaria se pierden en la exportación</strong></summary>
    Los formatos de tiempo de Excel no soportan datos de zona horaria. Por lo tanto, cualquier dato de zona horaria en el valor de respuesta será eliminado durante la exportación XLS. Para retener esta información, marca la opción de exportar fechas como valores de texto. 
<br><br>
Para más información sobre esta configuración, consulta <a href="advanced_export.html">Opciones avanzadas para exportar datos</a>.
</details>