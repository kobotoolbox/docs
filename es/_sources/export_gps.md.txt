# Mapear datos GPS

Es posible que tu proyecto incluya una o más preguntas GPS en tu formulario. KoboToolbox incluirá los datos GPS (latitud, longitud, altitud, precisión) en el conjunto de datos que se puede descargar como XLS o CSV. También es posible ver las coordenadas GPS en un mapa en línea y descargar los puntos como un archivo KML para usarlo en otras aplicaciones.

## Ver tus puntos GPS

![image](/images/export_gps/view_gps.jpg)

Las dos opciones siguientes solo aparecen si tu formulario tiene preguntas GPS y tiene envíos con coordenadas GPS.

**Opción 1 - Ver puntos GPS en línea.**

Haz clic en el botón **Ver en el mapa**, que lleva a la vista de mapa en línea. Esta visualización también permite ver los envíos según las respuestas a ciertas preguntas. Al ver tus datos en un mapa, también puedes desagregar según las respuestas a las preguntas, como mostrar encuestados hombres y mujeres, u otros tipos de respuestas donde una distribución geográfica simple puede ser interesante. A continuación se muestra una lista completa de las funcionalidades actuales del mapa:

1. Configuración: carga superposiciones de datos y elige esquemas de colores para los marcadores.
2. Alternar capas: alterna entre múltiples opciones de fondo del mapa.
3. Alternar pantalla completa
4. Mostrar datos como puntos (predeterminado)
5. Mostrar datos como mapa de calor

**Opción 2 - Descargar puntos GPS como KML.**

Haz clic en el botón **Descargar puntos GPS**. Esto iniciará un nuevo proceso de exportación con los datos más recientes. Las exportaciones anteriores aparecerán en la lista según su fecha de creación, lo que te permite ver instantáneas de las coordenadas GPS en distintos momentos. Los archivos KML se pueden importar en una variedad de programas, incluidos Google Earth, Google Maps o software GIS profesional, como ArcMap.

![image](/images/export_gps/kml_exports.jpg)

Nota: En caso de que tu formulario use más de una pregunta GPS, solo se usará la primera en el mapa.

**Opción 3 - Exportar datos como CSV y cargar en software GIS.**

Como alternativa a exportar tus datos GPS como archivo KML, es posible y sencillo exportar y cargar tus datos como archivo CSV (que incluirá todos los atributos) directamente en software GIS como shapefile. Para una guía paso a paso, consulta este [artículo de ayuda](upload_to_gis.md).

## Cómo compartir datos del mapa

Para compartir un mapa con otras personas, ve a la Configuración de tu proyecto y activa Compartir datos. Esto significa que cualquier persona puede ver tus datos, es decir, en formato de mapa, tabla o descarga de archivos. No podrán editar nada, lo cual requeriría otorgar permisos de Puede editar a un usuario específico. Después de esto, puedes enviar la URL del mapa (ver más arriba).