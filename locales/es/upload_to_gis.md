# Exportar y descargar datos a software GIS
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/upload_to_gis.md" class="reference">15 Feb 2022</a>


**Proceso sencillo paso a paso para exportar y cargar tus datos como un shapefile en software GIS, como ArcMap.**

Hay varias formas de importar datos de ubicación recolectados con KoboToolbox en software GIS. Este artículo describe un procedimiento recomendado para descargar datos de KoboToolbox como un archivo CSV y cargarlo en ArcMap como un shapefile. Aunque este ejemplo utiliza ArcMap, el proceso es similar al de otros programas geoespaciales, incluido QGIS (gratuito).

1. En la ventana **Descargas** de la página de tu proyecto en KoboToolbox, exporta y descarga tus datos como un archivo CSV.

    ![image](/images/upload_to_gis/saveas_csv.jpg)

    _Nota: Puedes editar el conjunto de datos una vez que esté en el software GIS; sin embargo, puede ser más fácil editarlo primero en Excel u otro programa similar. En Excel, usa la función [Texto en columnas](https://support.office.com/en-us/article/split-a-cell-f1804d0c-e180-4ed0-a2ae-973a0b7c6a23) para dividir tus datos CSV en celdas individuales._

2. Abre un proyecto nuevo o existente en ArcMap, ve a **Agregar datos** y luego vincula la carpeta donde está guardado tu archivo CSV en tu computadora.

    ![image](/images/upload_to_gis/find_file.jpg)

3. Abre la ventana **Catalog** y haz clic en **Folder Connections**. Busca tu archivo CSV, haz clic derecho sobre él y selecciona **Create Feature Class** > **From XY Table**.

4. En el cuadro de diálogo, haz clic en el menú desplegable **X Field** y elige la opción question_Longitude de tu pregunta GPS. Además, asegúrate de seleccionar tu **Coordinate System of Input Coordinates** (WGS 1984 es una buena opción si no estás usando ninguno) y verifica que tu **Output** esté configurado en la carpeta correcta; luego haz clic en **OK**.

    ![image](/images/upload_to_gis/create_feature.jpg)

5. De vuelta en la ventana **Catalog**, haz clic y arrastra tu nuevo shapefile a la ventana **Data View** o a la **Table of Contents**.

6. Ahora deberías ver tus puntos en la pantalla y, si abres la **Attributes Table**, verás todos los datos asociados a cada punto. A partir de este momento, puedes visualizar y ejecutar diversos análisis espaciales con tus datos.

    ![image](/images/upload_to_gis/dataview_table.jpg)