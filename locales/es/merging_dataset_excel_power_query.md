# Combinar datos individuales con datos de lista a través de Power Query en Excel
<a href="../merging_dataset_excel_power_query.html">Read in English</a> | <a href="../fr/merging_dataset_excel_power_query.html">Lire en français</a> | <a href="../ar/merging_dataset_excel_power_query.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/73dbdbb56448bbfbdb62af8017b71582965291d2/source/merging_dataset_excel_power_query.md" class="reference">6 abr 2022</a>

Como se ilustra en el artículo de ayuda,
[Agrupar preguntas y grupos repetidos](group_repeat.md), puedes usar
grupos repetidos para cumplir ciertos requisitos de encuesta. También puedes necesitar
analizar datos de los grupos repetidos que fueron recolectados. Al
[descargar los datos del servidor (en formato XLS)](export_download.md), deberías
ver los datos en la siguiente estructura:

![Dataset Sheets](/images/merging_dataset_excel_power_query/dataset_sheets.png)

La primera hoja con el nombre **Repeat Group (Merge)** que se ve en la imagen
anterior contiene los _datos individuales_ de la encuesta, mientras que la segunda hoja con
el nombre **CR** contiene los _datos de lista_.

<p class="note">
  Para conjuntos de datos descargados, deberías tener una hoja más que el número de
  <em>grupos repetidos</em>. Por ejemplo, si tuvieras un
  <em>grupo repetido</em> incluido en el formulario de encuesta, deberías tener dos hojas
  en tu conjunto de datos.
</p>

Este artículo de ayuda también ilustrará la diferencia entre _datos
individuales_ y _datos de lista_. Luego mostrará los pasos para combinarlos en
un solo conjunto de datos a través de **Power Query** en **Excel**.

Combinar _datos individuales_ y _datos de lista_ a través del sistema actualmente no está
disponible, pero es posible a través de **Power Query** en **Excel**. Se eligió Excel sobre otro software porque es una hoja de cálculo ampliamente utilizada y disponible
para casi todas las PCs. También es relativamente fácil de usar.

## Diferencias entre datos individuales y datos de lista:

Los _datos individuales_ son información que generalmente se captura solo una vez en una
entrevista. Los _datos de lista_, por otro lado, se capturan más de una vez _(por ejemplo,
detalles de todos los miembros de la familia que viven dentro de un hogar)_ de la misma
persona en una entrevista. El número de casos en _datos individuales_ puede ser igual
a los _datos de lista_ pero nunca puede excederlos, mientras que el número de casos en _datos
de lista_ generalmente excede los _datos individuales_ pero a veces puede ser igual (pero
nunca menor).

Un formulario de encuesta completado, como se muestra a continuación, debería mostrar en una imagen las
diferencias entre _datos individuales_ y _datos de lista_. _Ten en cuenta que todos los datos
utilizados en este artículo de ayuda son hipotéticos_.

![Form](/images/merging_dataset_excel_power_query/form.png)

<p class="note">
  Cualquier dato que se recolecta fuera del grupo repetido es
  <em>datos individuales</em> y cualquier dato que se recolecta dentro de un grupo repetido
  es <em>datos de lista</em>.
</p>

Los datos descargados en formato XLS también deberían mostrar la diferencia entre
_datos individuales_ y _datos de lista_.

Cada registro _(como se muestra en la imagen a continuación)_, bajo `Name of the household head`,
`Sex of the household head`, `Total family members in the household`, y
`Total school going children (aged 6-16 years) in the household` de la primera
hoja **Repeat Group (Merge)** son _datos individuales_.

![Individual Data](/images/merging_dataset_excel_power_query/individual_data.png)

Este conjunto de datos de ejemplo tiene un total de 7 entrevistas como sus _datos individuales_.

De manera similar, cada registro _(como se muestra en la imagen a continuación)_, bajo `Name of child`,
`Age of child`, y `Sex of child` de la segunda hoja, **CR**, son _datos
de lista_.

![Roster Data](/images/merging_dataset_excel_power_query/roster_data.png)

Entonces, este conjunto de datos de muestra de ejemplo tiene un total de 12 registros como sus _datos de lista_.

<p class="note">
  <strong>Nota:</strong> Al descargar un conjunto de datos del servidor, también deberías
  poder ver otras variables (variables de metadatos) si no han sido
  filtradas. Han sido eliminadas de este conjunto de datos de ejemplo por simplicidad.
</p>

## Combinar datos individuales con datos de lista:

Si observas detenidamente las imágenes compartidas anteriormente, puedes ver la columna `_index` con
valor "1" en la primera hoja **Repeat Group (Merge)**. De manera similar, también hay
una columna `_parent_index` con valor "1" en la segunda hoja **CR**. `_index` y
`_parent_index` son variables adicionales creadas por el sistema para manejar grupos
repetidos. Son variables coincidentes necesarias para combinar _datos individuales_ y
_datos de lista_ juntos en uno.

A continuación se presentan dos enfoques para combinar _datos individuales_ y _datos de lista_ en un
solo conjunto de datos a través de **Power Query** en **Excel**. Puedes usar cualquiera de los
siguientes enfoques:

### Primer enfoque: Combinar datos individuales con datos de lista (cuando el conjunto de datos ya está abierto)

Para el primer enfoque, debes tener abierto tu conjunto de datos XLS. Para más detalles,
consulta el video a continuación:

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/xls_dataset_open.mp4"
    type="video/mp4"
  />
</video>

-   Abre el conjunto de datos que tiene tanto los _datos individuales_ como los _datos de lista_.

-   Selecciona todos los datos de la primera hoja _(datos individuales)_.

-   En la pestaña **Datos**, selecciona **Desde tabla/rango**.

-   Aparecerá un cuadro de diálogo **(Crear tabla)**. Selecciona **Aceptar**.

-   Selecciona el ícono **Cerrar y cargar** que se encuentra en la esquina superior izquierda de
    la pantalla. Ahora deberías ver dos opciones desplegables: **Cerrar y cargar** y
    **Cerrar y cargar en…**.

-   Selecciona **Cerrar y cargar en…**.

-   Aparecerá un cuadro de diálogo **(Importar datos)**. Selecciona **Solo crear
    conexión** y luego presiona **Aceptar**.

-   Ahora has creado una tabla de consulta para los _(datos individuales)_.

-   Ahora puedes ir a la segunda hoja, _(datos de lista)_, y seguir los mismos
    pasos que realizaste anteriormente.

-   Con esto has creado una tabla de consulta para los _(datos de lista)_.

-   En la pestaña **Datos**, selecciona **Obtener datos**. Desde allí, selecciona **Combinar
    consultas** y luego **Combinar**.

-   Se ve un cuadro de diálogo **Combinar**.

-   Carga ambas tablas de consulta. Una vez que ambas tablas estén cargadas, selecciona la
    variable coincidente `_index` de la primera tabla. De manera similar, selecciona la
    variable coincidente `_parent_index` de la segunda tabla. Tan pronto como
    selecciones ambas variables coincidentes deberías poder ver **La selección
    coincide con … de … filas de la primera tabla**. La tabla de consulta ahora debería estar
    combinada.

-   Para expandir la tabla combinada, marca todas las variables que desees tener en
    el conjunto de datos combinado. También puedes desmarcar **Usar nombre de columna original como
    prefijo** para tener el nombre de variable original en el conjunto de datos combinado. Cuando
    todo esté listo, selecciona **Aceptar**.

-   Ahora deberías tener el conjunto de datos combinado final.

-   Una vez más, selecciona el ícono **Cerrar y cargar** que se encuentra en la esquina superior izquierda
    de la pantalla. Deberías ver dos opciones desplegables: **Cerrar y cargar**
    y **Cerrar y cargar en…**.

-   Selecciona **Cerrar y cargar**. Con este clic final has combinado tus
    _datos individuales_ y _datos de lista_ en un solo conjunto de datos.

### Segundo enfoque: Combinar datos individuales con datos de lista (cuando el conjunto de datos aún no está abierto)

Usa el segundo enfoque cuando aún no hayas abierto tu conjunto de datos XLS y solo
hayas abierto tu nuevo libro de Excel. Para más detalles, consulta el video a continuación:

<video controls>
  <source
    src="./_static/files/merging_dataset_excel_power_query/new_excel_workbook.mp4"
    type="video/mp4"
  />
</video>

-   Abre un nuevo libro de Excel.

-   En la pestaña **Datos**, selecciona **Obtener datos**. Desde allí selecciona **Desde archivo**
    y luego **Desde libro**.

-   Busca el archivo en tu PC. Una vez que lo veas, selecciona el archivo y luego
    presiona **Importar**.

-   Se ve un cuadro de diálogo **Navegador**. Aquí, marca **Seleccionar varios elementos**
    y los nombres de hoja **CR** y **Repeat Group (Merge)** que son visibles.
    Una vez que estén marcados, el botón **Cargar** en la parte inferior del cuadro de diálogo
    se activa.

-   Selecciona el botón **Cargar**. Deberías ver dos opciones desplegables: **Cargar**
    y **Cargar en…**. Selecciona **Cargar**.

-   Con esto, has creado tablas de consulta para los _(datos individuales)_ y los
    _(datos de lista)_.

-   En la pestaña **Datos**, selecciona **Obtener datos**. Desde allí, selecciona **Combinar
    consultas** y luego selecciona **Combinar**.

-   Se ve un cuadro de diálogo **Combinar**.

-   Carga ambas tablas de consulta. Una vez que ambas tablas estén cargadas, selecciona la
    variable coincidente `_index` de la primera tabla. De manera similar, selecciona la
    variable coincidente `_parent_index` de la segunda tabla. Tan pronto como
    selecciones ambas variables coincidentes deberías poder ver **La selección
    coincide con … de … filas de la primera tabla**. La tabla de consulta ahora debería estar
    combinada.

-   Para expandir la tabla combinada, marca todas las variables que desees tener en
    el conjunto de datos combinado. También puedes desmarcar **Usar nombre de columna original como
    prefijo** para tener el nombre de variable original en el conjunto de datos combinado. Cuando
    todo esté listo, selecciona **Aceptar**.

-   Ahora deberías tener el conjunto de datos combinado final.

-   Una vez más, selecciona el ícono **Cerrar y cargar** que se encuentra en la esquina superior izquierda
    de la pantalla. Deberías ver dos opciones desplegables: **Cerrar y cargar**
    y **Cerrar y cargar en…**.

-   Selecciona **Cerrar y cargar**. Con este clic final has combinado tus
    _datos individuales_ y _datos de lista_ en un solo conjunto de datos.

<p class="note">
  Las diferencias en los dos enfoques están en la carga de la tabla de consulta. Una vez
  que las tablas de consulta estén cargadas, necesitarás seguir los mismos pasos para combinar
  los <em>datos individuales</em> y los <em>datos de lista</em>.
</p>

## Solución de problemas:

-   Exportar _grupos repetidos_ no es compatible con el formato CSV. Necesitarás
    descargar los datos en formato XLS.

-   Microsoft Power Query para Excel es un complemento de Excel. Puedes descargarlo
    a través de este
    [sitio de descarga de Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=39379).
    Debería funcionar mejor en _Excel para Microsoft 365_ o _Excel 2021_, _Excel
    2019_, _Excel 2016_, _Excel 2013_, y _Excel 2010_. Para más detalles,
    consulta el
    [sitio de soporte de Microsoft](https://support.microsoft.com/en-us/office/about-power-query-in-excel-7104fbee-9e62-4cb9-a02e-5bfb1a6c536a).

<p class="note">
  Para practicar, puedes acceder al XLSForm
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge).xlsx"
    >aquí</a
  >
  y al conjunto de datos de muestra de ejemplo
  <a
    download
    class="reference"
    href="./_static/files/merging_dataset_excel_power_query/repeat_group_(merge)_dataset.xlsx"
    >aquí</a
  >
  que se utilizaron en este artículo.
</p>