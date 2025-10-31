# Exportar y cargar datos en software GIS
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/upload_to_gis.md" class="reference">15 Feb 2022</a>

**Proceso simple paso a paso para exportar y cargar tus datos como un shapefile en
software GIS, como ArcMap.**

Existen múltiples formas de importar datos basados en ubicación recolectados a través de
KoboToolbox en software GIS. Este artículo describirá un procedimiento recomendado
para descargar datos de KoboToolbox como un archivo CSV y cargarlo en ArcMap como un
shapefile. Si bien este ejemplo usa ArcMap, el proceso es similar al de
otros softwares geoespaciales, incluyendo QGIS (gratuito).

1. En la pestaña **DESCARGAS** de la página de tu proyecto en KoboToolbox, exporta y
   descarga tus datos como un archivo CSV.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    _Nota: Puedes editar el conjunto de datos una vez que esté en el software GIS, sin embargo puede
    ser más fácil editarlo primero en Excel o un programa similar. En Excel, usa la
    función [Texto en columnas](https://support.office.com/en-us/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23)
    para dividir tus datos CSV en celdas individuales._

2. Abre un proyecto nuevo o existente en ArcMap, ve a **Add Data** y luego vincula
   la carpeta donde tu archivo CSV está guardado en tu computadora.

    ![image](/images/upload_to_gis/find_file.jpg)

3. Abre la ventana **Catalog** y haz clic en **Folder Connections**. Encuentra tu
   archivo CSV, haz clic derecho sobre él, luego selecciona **Create Feature Class** > **From XY
   Table**.

4. En el modal, haz clic en el menú desplegable **X Field** y elige tu opción
   question_Longitude de GPS. Además, asegúrate de elegir tu **Coordinate System
   of Input Coordinates**... (WGS 1984 es una buena opción, si no estás usando uno
   ya) y asegúrate de que tu **Output** esté configurado en la carpeta apropiada, luego
   haz clic en **OK**.

    ![image](/images/upload_to_gis/create_feature.jpg)

5. De vuelta en la ventana **Catalog**, haz clic y arrastra tu nuevo shapefile hacia
   la ventana **Data View** o **Table of Contents**.

6. Ahora deberías ver tus puntos en la pantalla y si abres la **Attributes
   Table**, verás todos los datos asociados con cada punto. Desde este
   punto, ahora puedes visualizar y ejecutar varios análisis espaciales con tus datos.

    ![image](/images/upload_to_gis/dataview_table.jpg)