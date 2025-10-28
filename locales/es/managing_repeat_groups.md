# Manejo de datos de grupos repetidos
<a href="../managing_repeat_groups.html">Read in English</a> | <a href="../fr/managing_repeat_groups.html">Lire en français</a> | <a href="../ar/managing_repeat_groups.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/cb137e68b19147fcd0331a6f7919f5563dcebeca/source/managing_repeat_groups.md" class="reference">21 ago 2025</a>

KoboToolbox te permite recolectar datos repetidos dentro de un formulario, por ejemplo, al realizar una encuesta de hogares donde se hacen las mismas preguntas a todos/as los/as miembros/as. Este artículo explica cómo visualizar, editar y exportar datos de grupos repetidos, y cómo vincular los datos de grupos repetidos con los datos principales.

<p class="note">
  Para aprender más sobre cómo configurar grupos repetidos en tus formularios, consulta <a href="https://support.kobotoolbox.org/group_repeat.html">Agrupar preguntas y repetir grupos</a>.
</p>

## Visualizar y editar datos de grupos repetidos
Puedes visualizar datos repetidos en la tabla de datos, que puedes encontrar en la vista **Tabla** de la ventana **DATOS** en la interfaz del proyecto de KoboToolbox. Las respuestas a preguntas repetidas aparecen en una sola columna por pregunta, con respuestas separadas por una coma, como se muestra a continuación.

 ![image](/images/managing_repeat_groups/data_table.png) 

También puedes visualizar los datos completos de cualquier envío dado, incluyendo cada repetición de grupos repetidos, haciendo clic en el botón <i class="k-icon-view"></i>**Abrir** a la izquierda de cada envío.

Para editar datos de grupos repetidos, haz clic en el botón <i class="k-icon-edit"></i>**Editar**. Esto abrirá el formulario y te permitirá [editar los datos del formulario](https://support.kobotoolbox.org/howto_edit_single_submissions.html) antes de volver a enviar. La [edición masiva](https://support.kobotoolbox.org/howto_edit_multiple_submissions.html) de datos de grupos repetidos no está actualmente disponible.

<p class="note">
  <b>Nota</b>: Los datos de grupos repetidos no se pueden mostrar en las vistas de <b>Informes</b> o <b>Mapa</b> debido a la estructura de datos de los grupos repetidos.
</p>

## Exportar datos de grupos repetidos
Para exportar datos de un formulario con grupos repetidos, debes descargar tus datos en **formato XLS**. Cada grupo repetido se exportará **como una hoja separada** en el archivo exportado. La descarga en CSV solo proporcionará datos de los datos principales.

![image](/images/managing_repeat_groups/download.png)

<p class="note"> 
    Para aprender más sobre cómo exportar tus datos, consulta <a href="https://support.kobotoolbox.org/export_download.html">Exportar y descargar tus datos</a>.
</p>

## Vincular datos de grupos repetidos
En archivos XLS exportados, los datos de grupos repetidos se almacenan **en una hoja separada**. La primera hoja del archivo XLS contiene los datos de respuesta principales, y los datos de cada grupo repetido se almacenan en su propia hoja. Los grupos repetidos anidados también se almacenan en hojas separadas.

Los datos de grupos repetidos se pueden vincular a los datos principales usando la columna **_index** de la hoja de datos principales y la columna **_parent_index** de la hoja de datos del grupo repetido.

En el ejemplo a continuación, la primera hoja incluye una columna **_index**, en verde, que identifica el primer envío. La segunda hoja, mostrada en la segunda imagen, contiene una columna **_parent_index**, también resaltada en verde, que se vincula de vuelta a la primera hoja. En este ejemplo, ambas filas de los datos repetidos provienen del primer envío de datos.

![image](/images/managing_repeat_groups/main_data.png)

![image](/images/managing_repeat_groups/repeat_group_data.png)

<p class="note">
  <b>Nota</b>: La hoja de datos del grupo repetido también incluye una <b>columna _index</b>. Esta columna se usa para vincular a <b>grupos repetidos anidados</b>, siguiendo la misma configuración descrita anteriormente, con el grupo repetido como los datos principales y el grupo repetido anidado como los datos vinculados.
</p>

Los datos de grupos repetidos se pueden combinar con los datos principales usando diferentes herramientas para análisis de datos. Por ejemplo, en Excel y Power BI, puedes usar [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) o [VLOOKUP()](https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1) para combinar datos. En SQL, R, SAS y otros lenguajes de manejo de bases de datos, puedes combinar los conjuntos de datos usando un [left join](https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins?view=sql-server-ver17).

<p class="note">
  Para aprender más sobre cómo combinar datos de grupos repetidos usando Power Query, consulta <a href="https://support.kobotoolbox.org/merging_dataset_excel_power_query.html?highlight=power+query">Combinar datos individuales con datos de lista a través de Power Query en Excel</a>.<br><br>Para aprender más sobre cómo combinar conjuntos de datos en R, consulta <a href="https://dplyr.tidyverse.org/reference/mutate-joins.html">Mutating joins</a>.
</p>