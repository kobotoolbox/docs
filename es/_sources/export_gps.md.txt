# Mapeo, Compartir y Exportar Datos GPS
<a href="../export_gps.html">Read in English</a> | <a href="../fr/export_gps.html">Lire en français</a> | <a href="../ar/export_gps.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/export_gps.md" class="reference">15 Feb 2022</a>

Tu proyecto puede incluir una o más preguntas GPS en su formulario. KoboToolbox
incluirá los datos GPS (latitud, longitud, altitud, precisión) en el
conjunto de datos que se puede descargar como XLS o CSV. También es posible ver las
coordenadas GPS en un mapa en línea y descargar los puntos como un archivo KML para
usar en otras aplicaciones.

## Ver tus puntos GPS

![image](/images/export_gps/view_gps.jpg)

Ambas opciones siguientes solo aparecen si tu formulario tiene preguntas GPS y
tiene envíos con coordenadas GPS.

**Opción 1 - Ver puntos GPS en línea.**

Haz clic en el botón **View on Map**, que te lleva a la vista de mapa en línea. Esta
visualización también te permite ver los envíos basados en ciertas respuestas de preguntas.
Cuando veas tus datos en un mapa, también puedes desagregar por
respuestas de preguntas, como mostrar encuestados/as masculinos/as y femeninos/as, u otros
tipos de respuestas donde una distribución geográfica simple podría ser interesante.
Una lista completa de las funcionalidades actuales del mapa se encuentra a continuación:

1. Settings: Sube superposiciones de datos y elige esquemas de color de marcadores.
2. Toggle layers: Alterna entre múltiples opciones de fondo de mapa.
3. Toggle fullscreen
4. Show data as points (predeterminado)
5. Show data as heat map

**Opción 2 - Descargar puntos GPS como KML.**

Haz clic en el botón **Download GPS Points**. Esto iniciará un nuevo proceso de exportación
con los datos más recientes. Las exportaciones anteriores se listarán por su fecha de
creación, permitiéndote ver instantáneas de coordenadas GPS en varios puntos en el
tiempo. Los archivos KML se pueden importar en una variedad de software, incluyendo Google
Earth, Google Maps, o software GIS profesional, como ArcMap.

![image](/images/export_gps/kml_exports.jpg)

Nota: En caso de que tu formulario use más de una pregunta GPS, solo la primera se
usará en el mapa.

**Opción 3 - Exportar datos como CSV y subir a software GIS.**

Como alternativa a exportar tus datos GPS como un archivo KML, es posible y
fácil exportar y subir tus datos como un archivo CSV (que incluirá todos los
atributos) directamente en software GIS como un shapefile. Para una guía paso a paso,
consulta este [artículo de ayuda](upload_to_gis.md).

## Cómo compartir datos del mapa

Puedes compartir un mapa con otros/as yendo a la Configuración de tu Proyecto y habilitando
Compartir Datos. Esto significa que cualquiera puede ver tus datos - es decir, en formato de mapa, tabla, o
descarga de archivos. No podrán editar nada, lo que requeriría
otorgar permisos de Puede Editar a un/a usuario/a en particular. Después de esto puedes enviar la
URL del mapa (ver arriba).