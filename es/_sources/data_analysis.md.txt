# Análisis de datos con KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/977b859244796b0c30002db811ee84f02bf98dee/source/data_analysis.md" class="reference">15 Jun 2026</a>

KoboToolbox ofrece **herramientas integradas** para ayudarte a revisar, visualizar y analizar los datos recolectados. Estas herramientas pueden utilizarse para estadísticas descriptivas, mapeo y análisis cualitativo.

Además de las herramientas integradas, también puedes **exportar tus datos** o **conectarlos a plataformas externas** para realizar una limpieza, procesamiento, análisis y visualización más avanzados.

Este artículo describe las opciones de análisis de datos de KoboToolbox, desde informes integrados, mapas y herramientas de análisis cualitativo hasta exportaciones de datos, exportaciones sincrónicas y prácticas de diseño de formularios que facilitan un análisis más limpio.

## Analizar y visualizar datos en KoboToolbox

KoboToolbox incluye varias herramientas que te ayudan a comprender tus datos directamente en la plataforma.

### Informes de datos

KoboToolbox incluye una herramienta de informes y visualización que puedes usar para **monitorear los datos entrantes** y ver **estadísticas descriptivas simples**.

Puedes usar los informes para mostrar gráficos, revisar el recuento de respuestas, comparar respuestas por subgrupo, y compartir o imprimir un resumen de las preguntas seleccionadas del formulario.

![Informe de datos](images/data_analysis/report.png)

Los informes son útiles para revisar tus datos rápidamente, pero no reemplazan la limpieza, el procesamiento, el análisis ni la visualización en profundidad en herramientas externas.

<p class="note">
  Para obtener más información sobre los informes de datos, consulta <a href="https://support.kobotoolbox.org/es/creating_custom_reports.html">Visualizar datos utilizando informes personalizados</a>.
</p>

### Vista de Mapa

KoboToolbox también ofrece una **vista de Mapa** integrada para los envíos que incluyen datos GPS. La vista de Mapa te ayuda a visualizar puntos GPS individuales, explorar patrones geográficos y comprender mejor dónde se recolectaron los envíos.

![Mapeo de datos GPS](images/data_analysis/map.png)

<p class="note">
  Para obtener más información sobre el mapeo de datos GPS con KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/mapping_gps.html#">Mapear datos GPS</a>.
</p>

### Transcripción de audio, traducción y análisis cualitativo

Las herramientas de procesamiento de lenguaje natural de KoboToolbox te ayudan a **transcribir, traducir y analizar datos cualitativos**. Esto puede ayudar a convertir respuestas de audio abiertas en resultados más claros y utilizables.

Puedes procesar y analizar las respuestas de audio directamente en la interfaz de usuario y, luego, guardar transcripciones, traducciones, resúmenes, categorías y otros resultados de análisis como nuevas columnas en tu conjunto de datos.

![Análisis de datos cualitativos](images/data_analysis/qual.png)

<p class="note">
  Para obtener más información sobre el análisis de datos cualitativos en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/transcription-translation.html">Transcripción y traducción de respuestas de audio</a> y <a href="https://support.kobotoolbox.org/es/qualitative_analysis.html">Análisis cualitativo de respuestas de audio</a>.
</p>

## Exportar y conectar datos para análisis externo

Las herramientas integradas de KoboToolbox pueden utilizarse para análisis descriptivo simple, mapeo y análisis cualitativo. Sin embargo, muchos proyectos requieren herramientas externas para una limpieza, procesamiento, análisis y visualización de datos más avanzados. Para ello, puedes usar **exportaciones de datos clásicas** o **exportaciones sincrónicas** para trabajar con tus datos de KoboToolbox fuera de la plataforma.

### Exportaciones de datos

Puedes exportar tus datos de KoboToolbox en varios formatos, según cómo planees utilizarlos.

- Para el análisis general, puedes **exportar tus datos en formato Excel o CSV**. Estos formatos pueden usarse para limpiar y procesar datos, o para importarlos a software de análisis como R, Stata, SPSS o Python.
- Para el mapeo y el análisis geoespacial, puedes **exportar datos GPS en formatos como CSV, XLS, GeoJSON o KML**. Estos formatos pueden usarse en herramientas de mapeo y software GIS.

<p class="note">
  Para obtener más información sobre la exportación de datos de KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/export_download.html">Exportar y descargar datos</a>.
</p>

Al exportar datos para su análisis en software externo, se recomienda exportarlos como **valores XML y encabezados**, y **separar las respuestas de opción múltiple** en columnas separadas. Estas configuraciones facilitan el procesamiento y el análisis de los datos exportados.

Si vas a compartir datos sin procesar con audiencias no técnicas, **exportar etiquetas** en lugar de **valores XML y encabezados** puede ser más fácil de usar. Las etiquetas también pueden exportarse en varios idiomas.

Otras configuraciones de exportación, como almacenar las respuestas de fechas y números como texto o incluir datos de todas las versiones del formulario, dependen de tus necesidades y preferencias de análisis.

<p class="note">
  Para obtener más información sobre las opciones avanzadas para exportar datos, consulta <a href="https://support.kobotoolbox.org/es/advanced_export.html#">Opciones avanzadas para la exportación de datos</a>.
</p>

### Exportaciones sincrónicas

Para proyectos en curso, es posible que quieras **conectar tus datos de KoboToolbox a herramientas externas** en lugar de descargar una nueva exportación cada vez que cambien tus datos.

Las **exportaciones sincrónicas** te permiten conectar automáticamente los datos de KoboToolbox con aplicaciones externas como Microsoft Power BI, Excel o Google Sheets. Esto puede ser útil para informes interactivos, monitoreo de proyectos, procesamiento avanzado o flujos de trabajo de informes compartidos.

Con las exportaciones sincrónicas, los datos conectados se actualizan a medida que se reciben nuevos envíos, lo que reduce la necesidad de descargas y actualizaciones manuales.

<p class="note">
  Para obtener más información sobre cómo conectar tus datos a herramientas externas, consulta <a href="https://support.kobotoolbox.org/es/synchronous_exports.html">Usar la API para exportaciones sincrónicas</a>.
</p>

## Prepararse para el análisis de datos con KoboToolbox

Muchos problemas de calidad de datos no comienzan durante el análisis, sino durante la recolección de datos. Las decisiones que se toman al crear un formulario, como la estructura de las preguntas, los nombres de las opciones de respuesta y el manejo de los datos faltantes, pueden afectar la cantidad de limpieza y preparación que se necesitará más adelante.

KoboToolbox incluye varias herramientas que **favorecen la recolección de datos de alta calidad** y ayudan a preparar tus datos para el análisis a largo plazo.

<p class="note">
  Para obtener más información sobre las mejores prácticas de diseño de formularios, consulta <a href="https://support.kobotoolbox.org/es/preparing_for_analysis.html">Prepararse para el análisis de datos</a>.
</p>