# Mapear datos GPS
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/8a9cd82f1f57b9117b907018b8032085ab7f3682/source/mapping_gps.md" class="reference">5 Jun 2026</a>

<iframe src="https://www.youtube.com/embed/kefdxYOcgls?si=uY_tijozM5cpMVb3&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Las preguntas GPS en KoboToolbox te permiten recolectar información geográfica precisa como puntos individuales, o una colección de puntos que representan un camino o área durante la recolección de datos. Cada registro GPS incluye latitud, longitud, altitud y precisión, que puedes ver directamente en la tabla de datos. KoboToolbox también incluye una vista de <strong>Mapa</strong> integrada que ayuda a los usuarios a visualizar puntos GPS individuales, explorar patrones y comprender mejor dónde se recolectaron los envíos.

Este artículo explica cómo ver y mapear datos GPS en KoboToolbox, y describe los formatos de exportación disponibles para usar datos geoespaciales en otras herramientas y flujos de trabajo.

## Recolectar datos GPS en KoboToolbox

KoboToolbox te permite recolectar tres tipos de datos GPS en tus formularios:

| Tipo de pregunta en el Formbuilder | Tipo de pregunta en XLSForm | Tipo de dato GPS                              |
|:-----------------------------------|:----------------------------|:----------------------------------------------|
| Point                              | `geopoint`                  | Un punto individual                           |
| Line                               | `geotrace`                  | Un camino formado por múltiples puntos        |
| Area                               | `geoshape`                  | Un área formada por múltiples puntos          |

Todas las respuestas GPS aparecen en la tabla de datos y se incluyen en las exportaciones de datos. Solo los puntos individuales, denominados <strong>geopoints</strong> en la interfaz de usuario, pueden mostrarse en la vista de <strong>Mapa</strong> de KoboToolbox.

<p class="note">
<strong>Nota:</strong> También puedes recolectar la ubicación automáticamente en segundo plano usando <a href="https://support.kobotoolbox.org/es/form_meta.html">metadatos GPS</a>. Los puntos GPS recolectados a través de metadatos del formulario no pueden mostrarse en la vista de <strong>Mapa</strong>.
</p>

Los datos GPS pueden recolectarse tanto con formularios web como con KoboCollect.

<p class="note">
Para obtener más información sobre la recolección de datos GPS en tus formularios de KoboToolbox, consulta <a href="../es/collect_gps.html">Recolectar datos de GPS con KoboToolbox</a>.
</p>

## Mapear datos GPS en KoboToolbox

KoboToolbox incluye una vista de <strong>Mapa</strong> integrada que muestra los puntos GPS recolectados a través de tu formulario. Cualquier usuario con el permiso <strong>Ver envíos</strong> puede acceder al mapa.

Para abrir el mapa:

1. Abre tu proyecto y ve a la página <strong>DATOS</strong>.
2. En el menú de la izquierda, selecciona <i class="k-icon-map-view"></i> <strong>Mapa</strong>.
3. Si tu formulario incluye al menos una pregunta geopoint, las ubicaciones recolectadas aparecen en el mapa.

![Mapa del mundo con geopuntos naranja en diferentes países](images/mapping_gps/map.png)

Puedes acercar o alejar la vista usando los botones <i class="k-icon-plus"></i> y <i class="k-icon-minus"></i> en la esquina superior izquierda del mapa. Para ver el mapa en pantalla completa, haz clic en <i class="k-icon-expand"></i> <strong>Alternar pantalla completa</strong> en la esquina superior derecha.

Cuando varios puntos GPS están muy próximos entre sí, aparecen como un único punto agrupado con un número que indica cuántos envíos están agrupados allí. Acerca la vista para ver los puntos individuales.

<p class="note">
<strong>Nota:</strong> Solo las preguntas geopoint se muestran en el mapa. Los datos de geotrace y geoshape no se muestran.
</p>

### Seleccionar qué pregunta ver en el mapa

De forma predeterminada, el mapa muestra los datos de la primera pregunta geopoint de tu formulario. Si tu formulario incluye varias preguntas geopoint, puedes elegir cuál mostrar.

Para seleccionar una pregunta diferente:

1. Haz clic en <i class="k-icon-settings"></i> <strong>Configuración de la visualización del mapa</strong>.
2. En **GEOPOINT QUESTION**, selecciona una pregunta geopoint diferente de la lista.

![Ventana de configuración del mapa para elegir la pregunta geopoint](images/mapping_gps/select.png)

<p class="note">
<strong>Nota:</strong> Esta opción solo está disponible si tu formulario incluye más de una pregunta geopoint.
</p>

### Personalizar el mapa

Puedes cambiar cómo se muestran los datos GPS en el mapa usando los controles disponibles.

Para cambiar el tipo de visualización:

- Haz clic en <i class="k-icon-heatmap"></i> <strong>Mostrar en forma de mapa de calor</strong> en la esquina superior derecha para ver los datos como un mapa de calor.
- Haz clic en <i class="k-icon-pins"></i> <strong>Mostrar en forma de puntos</strong> para volver a los marcadores de puntos individuales.

<p class="note">
<strong>Nota:</strong> Un <strong>mapa de calor</strong> es una visualización que muestra la concentración de envíos según sus coordenadas geográficas. Las áreas con puntos de datos más agrupados aparecen con mayor intensidad, mientras que las áreas con menos envíos aparecen más claras. Los mapas de calor ayudan a identificar patrones geográficos y zonas de alta concentración sin mostrar puntos individuales.
</p>

Para cambiar la capa base del mapa:

- Haz clic en <i class="k-icon-layer"></i> <strong>Alternar capas</strong> en la esquina superior derecha.
- Selecciona una capa base, como OpenStreetMap, OpenTopoMap, ESRI World Imagery o Humanitarian. La capa base predeterminada es OpenStreetMap.

![La capa base del mapa del mundo](images/mapping_gps/base_layer.png)

También puedes agregar capas personalizadas adicionales sobre tu mapa:

1. Abre <i class="k-icon-settings"></i> <strong>Configuración de la visualización del mapa</strong>.
2. Ve a <strong>OVERLAYS</strong>.
3. Ingresa una etiqueta para la capa y carga un archivo en formato CSV, KML, KMZ, WKT o GeoJSON.

Los archivos cargados aparecen como capas opcionales que puedes activar o desactivar desde el mapa.

<p class="note">
<strong>Nota:</strong> Solo los propietarios del proyecto o los usuarios con permisos de <strong>Gestionar el proyecto</strong> pueden agregar capas personalizadas a un mapa.
</p>

### Desagregar puntos según respuestas de la encuesta

Puedes agrupar los puntos GPS en el mapa según las respuestas a otras preguntas de tu formulario. Esto te ayuda a comprender cómo se distribuyen geográficamente los diferentes grupos de encuestados.

Para desagregar puntos:

1. Haz clic en <strong>Desagregar según respuestas de la encuesta</strong> en la esquina inferior izquierda del mapa.
2. Selecciona la pregunta que deseas usar para categorizar los puntos. También puedes cambiar el idioma de visualización.

![Mapa del mundo con marcadores geopoint desagregados en tonos de azul](images/mapping_gps/disaggregate.png)

Para cambiar el conjunto de colores usado para los puntos desagregados:

1. Abre <i class="k-icon-settings"></i> <strong>Configuración de la visualización del mapa</strong>.
2. Selecciona <strong>MARKER COLORS</strong>.
3. Elige un conjunto de colores diferente.

Para eliminar la desagregación:

1. Haz clic en <strong>Desagregar utilizando: [etiqueta de la pregunta]</strong>.
2. Selecciona <strong>-- Ver todos los datos --</strong> de la lista.

### Mostrar un gran número de envíos en el mapa

Si tu proyecto tiene más de 1.000 envíos, el mapa mostrará solo 1.000 puntos GPS de forma predeterminada. Puedes aumentar el número de puntos mostrados desde la configuración del mapa.

Para cambiar el número de puntos mostrados:

1. Abre <i class="k-icon-settings"></i> **Configuración de la visualización del mapa**.
2. Selecciona **QUERY LIMIT**.
3. Ajusta el control deslizante para elegir cuántos envíos mostrar en el mapa.

Mostrar un gran número de puntos GPS puede ralentizar tu navegador, especialmente con conjuntos de datos más grandes. Aumentar el límite es temporal y se restablece cada vez que vuelves a abrir el mapa.

## Exportar datos GPS

KoboToolbox ofrece varias opciones para exportar datos GPS. Cada formato es compatible con diferentes flujos de trabajo, incluyendo la revisión de datos, el mapeo y el análisis geoespacial.

### Exportar como CSV o XLS

Al exportar datos como <strong>CSV</strong> o <strong>XLS</strong>, las coordenadas GPS se incluyen en varias columnas:

- Una columna con el conjunto completo de coordenadas.
- Solo para preguntas <strong>geopoint</strong>, columnas separadas para latitud, longitud, altitud y precisión.

![Mapa del mundo con marcadores geopoint desagregados en tonos de azul](images/mapping_gps/export.png)

<p class="note">
<strong>Nota:</strong> En este contexto, <strong>accuracy</strong> (exactitud) y <strong>precision</strong> (precisión) hacen referencia al mismo valor.
</p>

Las exportaciones en CSV y XLS son útiles para revisar y limpiar datos en software de hojas de cálculo. También pueden importarse en muchas herramientas GIS, aunque generalmente se requiere una preparación adicional. Esto puede incluir especificar los campos de coordenadas, definir un sistema de referencia de coordenadas o convertir los datos a otro formato geoespacial.

<p class="note">
<strong>Nota:</strong> Para preguntas de tipo <strong>geotrace</strong> y <strong>geoshape</strong>, las exportaciones en CSV y XLS incluyen una sola columna con las coordenadas GPS separadas por punto y coma. Generalmente se requiere un procesamiento adicional para extraer los puntos individuales o convertir los datos en geometrías de línea o polígono para su uso en software GIS.
</p>

### Exportar como GeoJSON

<strong>GeoJSON</strong> es el formato recomendado para preparar datos GPS para su uso en software GIS como ArcGIS o QGIS. Es ampliamente compatible y funciona bien con los flujos de trabajo geoespaciales más comunes.

Al exportar a GeoJSON, KoboToolbox convierte los tipos de preguntas GPS a tipos de geometría GeoJSON estándar, como se muestra a continuación:

| Formbuilder | XLSForm     | GeoJSON     |
|:------------|:------------|:------------|
| Point       | `geopoint`  | Point       |
| Line        | `geotrace`  | LineString  |
| Area        | `geoshape`  | Polygon     |

Durante la exportación, el valor de precisión incluido en las coordenadas GPS no se conserva, ya que GeoJSON no admite un campo de precisión. El orden de las coordenadas también cambia de `latitud longitud` en KoboToolbox a `longitud latitud` en GeoJSON.

De forma predeterminada, las exportaciones GeoJSON están estructuradas por envío. Para una mejor compatibilidad con las herramientas GIS, puedes activar la opción <strong>Aplanar GeoJSON</strong> en la configuración avanzada de exportación. Esto combina todas las respuestas GPS en una única [FeatureCollection](https://stevage.github.io/geojson-spec/#section-3.3).

<p class="note">
<strong>Nota:</strong> Cuando el GeoJSON está aplanado, puede ser más difícil identificar qué respuestas GPS provienen del mismo envío. Esto es más notable en formularios con más de una pregunta GPS por envío. En formularios con solo una pregunta GPS por envío, esto generalmente no representa un problema.
</p>

Si un envío no incluye un valor para una pregunta GPS, no aparecerá en la exportación GeoJSON. Si planeas exportar datos como GeoJSON, asegúrate de que al menos una pregunta GPS esté completada en cada envío.

Si tu formulario incluye varias preguntas GPS, es posible que quieras exportar solo la que planeas usar para el mapeo. Usa la opción <strong>Seleccionar las preguntas que se exportarán</strong> en la configuración avanzada de exportación para limitar qué campos GPS se incluyen.

### Exportar como KML

<strong>KML</strong> está pensado para su visualización en herramientas que admiten de forma nativa este formato, como Google Earth. Admite estilos básicos para una visualización rápida en mapas. Si bien las exportaciones KML siguen estando disponibles en KoboToolbox, este formato es limitado y solo debe usarse cuando lo requiera un flujo de trabajo específico.

Las exportaciones KML en KoboToolbox solo admiten preguntas de tipo <strong>geopoint</strong>. Si un formulario incluye preguntas geotrace o geoshape, esas geometrías no se incluyen en la exportación KML.

Si un formulario contiene varias preguntas geopoint, solo se incluye el primer geopoint del formulario en el archivo KML. Las preguntas geopoint adicionales se omiten. Además, las exportaciones KML incluyen únicamente la ubicación del geopoint y el ID del envío. Los demás campos del envío no se incluyen.

Por último, al igual que con GeoJSON, el orden de las coordenadas cambia de `latitud longitud` en KoboToolbox a `longitud latitud` en GeoJSON.

<p class="note">
<strong>Nota:</strong> Para obtener más información sobre cómo exportar tus datos GPS desde KoboToolbox, consulta <a href="../es/export_download.html">Exportar y descargar datos</a>.
</p>