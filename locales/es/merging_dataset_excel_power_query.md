# Combinar datos individuales con datos de grupos de repetición a través de Power Query en Excel
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/73dbdbb56448bbfbdb62af8017b71582965291d2/source/merging_dataset_excel_power_query.md" class="reference">6 Apr 2022</a>


Como se ilustra en el artículo de ayuda
[Grupos y grupos de repetición en el Formbuilder](group_repeat.md), puedes usar
grupos de repetición para cumplir ciertos requisitos de una encuesta. También
puede ser necesario analizar los datos de los grupos de repetición que se
recolectaron. Al
[descargar los datos del servidor (en formato XLS)](export_download.md), deberías
ver los datos con la siguiente estructura:

![Dataset Sheets](/images/merging_dataset_excel_power_query/dataset_sheets.png)

La primera hoja con el nombre **Repeat Group (Merge)** que se ve en la imagen
anterior contiene los _datos individuales_ de la encuesta, mientras que la segunda
hoja con el nombre **CR** contiene los _datos del grupo de repetición_.

<p class="note">
  En los conjuntos de datos descargados, deberías tener una hoja más que el
  número de <em>grupos de repetición</em>. Por ejemplo, si incluiste un
  <em>grupo de repetición</em> en el formulario de encuesta, deberías tener dos
  hojas en tu conjunto de datos.
</p>

Este artículo de ayuda también ilustrará la diferencia entre los _datos
individuales_ y los _datos del grupo de repetición_. Luego mostrará los pasos
para combinarlos en un único conjunto de datos a través de **Power Query** en
**Excel**.

Combinar _datos individuales_ y _datos del grupo de repetición_ a través del
sistema no está disponible actualmente, pero es posible hacerlo a través de
**Power Query** en **Excel**. Se eligió Excel sobre otros programas porque es una
hoja de cálculo de uso generalizado y disponible en casi todas las computadoras.
Además, es relativamente fácil de usar.

## Diferencias entre datos individuales y datos del grupo de repetición:

Los _datos individuales_ son información que generalmente se captura una sola vez
en una entrevista. Los _datos del grupo de repetición_, en cambio, se capturan
más de una vez _(por ejemplo, los detalles de todos los miembros de una familia
que viven en un mismo hogar)_ dentro de la misma entrevista. El número de casos
en los _datos individuales_ puede ser igual al de los _datos del grupo de
repetición_, pero nunca puede superarlo, mientras que el número de casos en los
_datos del grupo de repetición_ generalmente supera al de los _datos
individuales_, aunque a veces puede ser igual (pero nunca menor).

Un formulario de encuesta completado, como se muestra a continuación, ilustra
visualmente las diferencias entre los _datos individuales_ y los _datos del grupo
de repetición_. _Ten en cuenta que todos los datos utilizados en este artículo de
ayuda son hipotéticos_.

![Form](/images/merging_dataset_excel_power_query/form.png)

<p class="note">
  Cualquier dato recolectado fuera del grupo de repetición es un
  <em>dato individual</em>, y cualquier dato recolectado dentro de un grupo de
  repetición es un <em>dato del grupo de repetición</em>.
</p>

Los datos descargados en formato XLS también muestran la diferencia entre
_datos individuales_ y _datos del grupo de repetición_.

Cada registro _(como se muestra en la imagen a continuación)_, bajo `Name of the household head`,
`Sex of the household head`, `Total family members in the household` y
`Total school going children (aged 6-16 years) in the household` de la primera
hoja **Repeat Group (Merge)** corresponde a _datos individuales_.

![Individual Data](/images/merging_dataset_excel_power_query/individual_data.png)

Este conjunto de datos de ejemplo tiene un total de 7 entrevistas como _datos individuales_.

De igual manera, cada registro _(como se muestra en la imagen a continuación)_,
bajo `Name of child`, `Age of child` y `Sex of child` de la segunda hoja, **CR**,
corresponde a _datos del grupo de repetición_.

![Roster Data](/images/merging_dataset_excel_power_query/roster_data.png)

Así, este conjunto de datos de ejemplo tiene un total de 12 registros como _datos del grupo de repetición_.

<p class="note">
  <strong>Nota:</strong> Al descargar un conjunto de datos del servidor, también
  deberías poder ver otras variables (variables de metadatos) si no han sido
  filtradas. Se han eliminado de este conjunto de datos de ejemplo para
  simplificar.
</p>

## Combinar datos individuales con datos del grupo de repetición:

Si observas detenidamente las imágenes compartidas anteriormente, puedes ver la
columna `_index` con el valor "1" en la primera hoja **Repeat Group (Merge)**.
De igual manera, también hay una columna `_parent_index` con el valor "1" en la
segunda hoja **CR**. `_index` y `_parent_index` son variables adicionales creadas
por el sistema para gestionar los grupos de repetición. Son las variables de
coincidencia necesarias para combinar los _datos individuales_ y los _datos del
grupo de repetición_ en uno solo.

A continuación se presentan dos enfoques para combinar _datos individuales_ y
_datos del grupo de repetición_ en un único conjunto de datos a través de
**Power Query** en **Excel**. Puedes usar cualquiera de los siguientes enfoques:

### Primer enfoque: Combinar datos individuales con datos del grupo de repetición (cuando el conjunto de datos ya está abierto)

Para el primer enfoque, debes tener abierto tu conjunto de datos XLS. Para más
detalles, consulta el video a continuación:

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/xls_dataset_open.mp4"
    type="video/mp4"
  />
</video>

-   Abre el conjunto de datos que contiene tanto los _datos individuales_ como
    los _datos del grupo de repetición_.

-   Selecciona todos los datos de la primera hoja _(datos individuales)_.

-   En la ventana **Datos**, selecciona **Desde tabla o rango**.

-   Aparecerá una caja de diálogo **(Crear tabla)**. Selecciona **Aceptar**.

-   Selecciona el icono **Cerrar y cargar** que se encuentra en la esquina
    superior izquierda de la pantalla. Deberías ver dos opciones en el menú
    desplegable: **Cerrar y cargar** y **Cerrar y cargar en…**.

-   Selecciona **Cerrar y cargar en…**.

-   Aparecerá una caja de diálogo **(Importar datos)**. Selecciona **Solo crear
    conexión** y luego haz clic en **Aceptar**.

-   Has creado una tabla de consulta para los _(datos individuales)_.

-   Ahora puedes ir a la segunda hoja, _(datos del grupo de repetición)_, y
    seguir exactamente los mismos pasos que realizaste anteriormente.

-   Con esto has creado una tabla de consulta para los _(datos del grupo de
    repetición)_.

-   En la ventana **Datos**, selecciona **Obtener datos**. Desde allí, selecciona
    **Combinar consultas** y luego **Combinar**.

-   Aparecerá una caja de diálogo **Combinar**.

-   Carga ambas tablas de consulta. Una vez cargadas las dos tablas, selecciona
    la variable de coincidencia `_index` de la primera tabla. De igual manera,
    selecciona la variable de coincidencia `_parent_index` de la segunda tabla.
    En cuanto selecciones ambas variables de coincidencia, deberías poder ver
    **La selección coincide con … de … filas de la primera tabla**. La tabla de
    consulta debería estar combinada ahora.

-   Para expandir la tabla combinada, marca todas las variables que deseas incluir
    en el conjunto de datos combinado. También puedes desmarcar **Usar el nombre
    de columna original como prefijo** para conservar el nombre de variable
    original en el conjunto de datos combinado. Cuando hayas terminado, selecciona
    **Aceptar**.

-   Ahora deberías tener el conjunto de datos combinado final.

-   Una vez más, selecciona el icono **Cerrar y cargar** que se encuentra en la
    esquina superior izquierda de la pantalla. Deberías ver dos opciones en el
    menú desplegable: **Cerrar y cargar** y **Cerrar y cargar en…**.

-   Selecciona **Cerrar y cargar**. Con este último clic has combinado tus
    _datos individuales_ y _datos del grupo de repetición_ en un único conjunto
    de datos.

### Segundo enfoque: Combinar datos individuales con datos del grupo de repetición (cuando el conjunto de datos aún no está abierto)

Usa el segundo enfoque cuando aún no hayas abierto tu conjunto de datos XLS y
solo tengas abierto un nuevo libro de Excel. Para más detalles, consulta el video
a continuación:

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/new_excel_workbook.mp4"
    type="video/mp4"
  />
</video>

-   Abre un nuevo libro de Excel.

-   En la ventana **Datos**, selecciona **Obtener datos**. Desde allí, selecciona
    **Desde archivo** y luego **Desde libro**.

-   Busca el archivo en tu computadora. Una vez que lo encuentres, selecciona el
    archivo y haz clic en **Importar**.

-   Aparecerá una caja de diálogo **Navegador**. Aquí, marca **Seleccionar varios
    elementos** y los nombres de hoja **CR** y **Repeat Group (Merge)** que
    aparecen visibles. Una vez marcados, el botón **Cargar** en la parte inferior
    de la caja de diálogo se activará.

-   Selecciona el botón **Cargar**. Deberías ver dos opciones en el menú
    desplegable: **Cargar** y **Cargar en…**. Selecciona **Cargar**.

-   Con esto has creado tablas de consulta para los _(datos individuales)_ y los
    _(datos del grupo de repetición)_.

-   En la ventana **Datos**, selecciona **Obtener datos**. Desde allí, selecciona
    **Combinar consultas** y luego selecciona **Combinar**.

-   Aparecerá una caja de diálogo **Combinar**.

-   Carga ambas tablas de consulta. Una vez cargadas las dos tablas, selecciona
    la variable de coincidencia `_index` de la primera tabla. De igual manera,
    selecciona la variable de coincidencia `_parent_index` de la segunda tabla.
    En cuanto selecciones ambas variables de coincidencia, deberías poder ver
    **La selección coincide con … de … filas de la primera tabla**. La tabla de
    consulta debería estar combinada ahora.

-   Para expandir la tabla combinada, marca todas las variables que deseas incluir
    en el conjunto de datos combinado. También puedes desmarcar **Usar el nombre
    de columna original como prefijo** para conservar el nombre de variable
    original en el conjunto de datos combinado. Cuando hayas terminado, selecciona
    **Aceptar**.

-   Ahora deberías tener el conjunto de datos combinado final.

-   Una vez más, selecciona el icono **Cerrar y cargar** que se encuentra en la
    esquina superior izquierda de la pantalla. Deberías ver dos opciones en el
    menú desplegable: **Cerrar y cargar** y **Cerrar y cargar en…**.

-   Selecciona **Cerrar y cargar**. Con este último clic has combinado tus
    _datos individuales_ y _datos del grupo de repetición_ en un único conjunto
    de datos.

<p class="note">
  Las diferencias entre los dos enfoques están en la carga de la tabla de
  consulta. Una vez cargadas las tablas de consulta, deberás seguir los mismos
  pasos para combinar los <em>datos individuales</em> y los <em>datos del grupo
  de repetición</em>.
</p>

## Resolución de problemas:

-   La exportación de _grupos de repetición_ no está disponible en formato CSV.
    Deberás descargar los datos en formato XLS.

-   Microsoft Power Query para Excel es un complemento de Excel. Puedes
    descargarlo a través de este
    [sitio de descarga de Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=39379).
    Funciona mejor con _Excel para Microsoft 365_ o _Excel 2021_, _Excel 2019_,
    _Excel 2016_, _Excel 2013_ y _Excel 2010_. Para más detalles, consulta el
    [sitio de soporte de Microsoft](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a).

<p class="note">
  Para practicar, puedes acceder al XLSForm
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge).xlsx"
    >aquí</a
  >
  y al conjunto de datos de ejemplo
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge)_dataset.xlsx"
    >aquí</a
  >
  que se utilizaron en este artículo.
</p>