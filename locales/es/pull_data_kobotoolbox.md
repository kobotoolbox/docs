# Funcionalidad de extracción de datos en KoboToolbox
<a href="../pull_data_kobotoolbox.html">Read in English</a> | <a href="../fr/pull_data_kobotoolbox.html">Lire en français</a> | <a href="../ar/pull_data_kobotoolbox.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/202f8e0e134d0695913bf6c5d5b52449c5e61e5d/source/pull_data_kobotoolbox.md" class="reference">18 ago 2025</a>

Esto se hace mejor en la versión xls del formulario.

-   En el lado de encuesta del formulario, agrega un campo de cálculo a tu encuesta.
-   Dale a ese campo el nombre que desees
-   Luego, en su columna de cálculo, llama a la función pulldata(), indicando
    qué campo extraer de qué fila de qué archivo .csv. Esto se puede lograr
    escribiendo lo siguiente
    `pulldata('nombredelcsv', 'encabezadodecolumnaparaextraerdatos', 'columnaparaverificarcoincidenciaTEXTO', 'TEXTOaverificar'`

    ![image](/images/pull_data_kobotoolbox/xls.png)

-   Ten en cuenta que tu CSV necesita tener al menos dos columnas y asegúrate de que la
    columnaparaverificarcoincidenciaTEXTO sea siempre la primera columna desde la izquierda
-   TEXTOaverificar también puede ser referenciado desde una pregunta de campo anterior
    usando `${Pregunta}` como en el ejemplo anterior
-   Una vez que hayas terminado de actualizar el xls, necesitarás cargar tu formulario
    desde xls (no lo edites en el editor de formularios), luego cargarás tu CSV
    de la misma manera que cargarías tus imágenes.
-   Cuando despliegues tu archivo, el csv se descargará a los archivos multimedia

**Cosas a tener en cuenta**

-   Esto funcionará tanto en la aplicación de Android de KoboCollect como en Enketo (formulario web).
-   Comprime un archivo .csv grande en un archivo .zip antes de cargarlo.
-   Guarda el archivo .csv en formato UTF-8 si los datos precargados contienen fuentes que no están en inglés
    o caracteres especiales; esto permite que tu dispositivo Android renderice el texto
    correctamente.
-   Los campos de datos extraídos de un archivo .csv se consideran cadenas de texto,
    por lo tanto, usa las funciones int() o number() para convertir un campo precargado
    en forma numérica.
-   Si el archivo .csv contiene datos sensibles que quizás no desees cargar al
    servidor, carga un archivo .csv en blanco como parte de tu formulario, luego reemplázalo
    con el archivo .csv real copiando manualmente el archivo en cada uno de tus dispositivos.
-   Si estás enfrentando mensajes de error al usar esta funcionalidad, intenta cambiar el nombre del archivo para eliminar guiones bajos o símbolos.