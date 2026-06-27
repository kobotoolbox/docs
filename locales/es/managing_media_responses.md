# Gestionar respuestas con archivos multimedia
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/b0d195136b7fb3fe51b687cc03a5e8dcde946309/source/managing_media_responses.md" class="reference">22 Jun 2026</a>

Los archivos multimedia recolectados de los encuestados suelen contener información contextual importante, como fotos, grabaciones o documentos que complementan y enriquecen los datos de la encuesta. Una vez que comienza la recolección de datos, **estos archivos pasan a formar parte de los datos de tu proyecto** y deben gestionarse con cuidado.

Este artículo explica cómo ver, descargar y eliminar archivos multimedia enviados por los encuestados, incluyendo imágenes, grabaciones de audio, videos y otros tipos de archivos.

## Ver archivos multimedia

Todos los archivos multimedia enviados por los encuestados se pueden ver desde la tabla de datos de tu proyecto. Para abrir archivos multimedia en envíos individuales:

1. Abre tu proyecto y ve a la página **DATOS**.
2. En la tabla de datos, ubica la celda que contiene el archivo.
3. Haz clic en el icono <i class="k-icon-qt-photo"></i> **imagen**, <i class="k-icon-qt-video"></i> **video** o <i class="k-icon-qt-file"></i> **archivo**. Para grabaciones de audio, haz clic en **Abrir**. <i class="k-icon-arrow-up-right"></i>

![Vista de galería para imágenes](images/managing_media_responses/table.png)

Las imágenes también se pueden ver en la vista de **Galería** de tu proyecto. Para ver todas las imágenes recolectadas en un solo proyecto:

1. Abre tu proyecto y ve a la página **DATOS**.
2. Abre la ventana <i class="k-icon-file-image"></i> **Galería** desde el menú lateral izquierdo.
3. La vista de **Galería** muestra todas las imágenes recolectadas en el proyecto. Puedes filtrar las imágenes por pregunta o por rango de fechas.

## Descargar archivos multimedia

Puedes descargar archivos multimedia de forma individual desde la tabla de datos, o en bloque desde la página de **Descargas**.

### Descargar archivos multimedia individuales

Para descargar un solo archivo:

1. Ve a la página **DATOS**.
2. En la tabla de datos, ubica la celda que contiene el archivo.
3. Haz clic en el icono <i class="k-icon-qt-photo"></i> **imagen**, <i class="k-icon-qt-video"></i> **video** o <i class="k-icon-qt-file"></i> **archivo**. Para grabaciones de audio, haz clic en **Abrir.** <i class="k-icon-arrow-up-right"></i>
4. Haz clic en los <i class="k-icon k-icon-more"></i> tres puntos en la parte superior de la vista previa.
5. Haz clic en <i class="k-icon-download"></i> **Descargar.**

![Descargar archivos multimedia](images/managing_media_responses/download.png)

### Descargar archivos multimedia en bloque

Para descargar archivos multimedia en bloque:

1. Ve a la página **DATOS**.
2. Abre la ventana <i class="k-icon-download"></i> **Descargas** desde el menú lateral izquierdo.
3. En **Seleccionar el tipo de exportación**, elige **Archivos multimedia adjuntos (ZIP)**.
4. Haz clic en **Nuevo exportable** y espera a que se complete la exportación.
5. Descarga el archivo `.zip` generado desde la tabla.

En la carpeta descargada, los archivos adjuntos están agrupados por envío. El nombre de cada carpeta corresponde al `_uuid` del envío, que también aparece como columna en el conjunto de datos.

<p class="note">
<strong>Nota:</strong> Las exportaciones de archivos multimedia incluyen únicamente las preguntas que están presentes en la versión más reciente del formulario.
</p>

Cuando exportas tus datos en formato CSV o XLS, el archivo exportado también incluye hipervínculos que abren los archivos multimedia asociados en un navegador web, siempre que la opción predeterminada **Incluir URL de archivos multimedia** esté seleccionada.

<p class="note">
  Para obtener más información sobre cómo exportar tus datos, consulta <a href="https://support.kobotoolbox.org/es/export_download.html">Exportar y descargar datos</a>.
</p>

## Eliminar archivos multimedia

<iframe src="https://www.youtube.com/embed/J0-mh1R6dEs?si=9t0JFhEVdVcf21lk&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Es posible que necesites eliminar archivos multimedia de tu proyecto de KoboToolbox por diversas razones, como mantener la confidencialidad, gestionar el espacio de almacenamiento o corregir errores en los envíos. Puedes eliminar archivos multimedia de forma individual o en bloque.

### Eliminar archivos multimedia individuales

Hay dos formas de eliminar archivos multimedia individuales: directamente desde la tabla de datos o abriendo el envío. Una vez que se elimina un archivo, aparece marcado como _Eliminado_ en la tabla de datos y no se puede recuperar.

**Eliminar archivos multimedia individuales desde la tabla de datos**

Puedes eliminar imágenes, videos y archivos individuales directamente desde la tabla de datos siguiendo estos pasos:

1. En la tabla de datos, ubica la celda con el archivo multimedia que deseas eliminar.
2. Haz clic en el icono <i class="k-icon k-icon-qt-photo"></i> **imagen**, <i class="k-icon k-icon-qt-video"></i> **video** o <i class="k-icon k-icon-qt-file"></i> **archivo**.
3. Haz clic en los <i class="k-icon k-icon-more"></i> **tres puntos** en la parte superior de la vista previa del archivo.
4. Haz clic en <i class="k-icon k-icon-trash"></i> **Eliminar** y luego en **Eliminar** nuevamente para confirmar.

![Eliminar archivos multimedia desde la tabla](images/managing_media_responses/delete_from_table.png)

**Eliminar archivos multimedia individuales en la vista del envío**

También puedes eliminar archivos multimedia abriendo la vista del envío:

1. En la tabla de datos, ubica el envío con los archivos multimedia que deseas eliminar.
2. En el lado izquierdo del envío, haz clic en <i class="k-icon k-icon-view"></i> **Abrir**.
3. Desplázate hasta el archivo multimedia que deseas eliminar.
4. Haz clic en los <i class="k-icon k-icon-more"></i> **tres puntos** a la derecha del archivo multimedia.
5. Haz clic en <i class="k-icon k-icon-trash"></i> **Eliminar** y luego en **Eliminar** nuevamente para confirmar.

![Abrir la vista del envío](images/managing_media_responses/open_submission_view.png)

**Eliminar archivos de audio en la vista de pregunta de audio**

Puedes eliminar archivos de audio abriendo la vista de pregunta de audio para la transcripción, traducción y análisis de preguntas de audio:

1. En la tabla de datos, haz clic en **Abrir** <i class="k-icon k-icon-arrow-up-right"></i> para abrir la vista de pregunta de audio.
2. En la ventana **TRANSCRIPCIÓN**, **TRADUCCIONES** o **ANÁLISIS**, ubica el archivo de audio en la esquina superior derecha.
3. Haz clic en los <i class="k-icon k-icon-more"></i> **tres puntos** a la derecha del archivo de audio.
4. Haz clic en <i class="k-icon k-icon-trash"></i> **Eliminar** y luego en **Eliminar** nuevamente para confirmar.

![Eliminar audio](images/managing_media_responses/delete_audio.png)

### Eliminar archivos multimedia en bloque

Es posible que necesites eliminar archivos multimedia en bloque, por ejemplo, para gestionar el espacio de almacenamiento después de haberlos exportado. Puedes eliminar todos los archivos multimedia de los envíos seleccionados siguiendo estos pasos:

1. Selecciona los envíos cuyos archivos multimedia deseas eliminar.
2. Haz clic en **Eliminar solo archivos multimedia** encima de la tabla de datos.
   * Esta acción abre un modal que muestra el número y los tipos de archivos multimedia que se eliminarán con esta selección.
3. Marca la casilla que dice "Estás a punto de eliminar permanentemente los siguientes archivos multimedia de los envíos seleccionados:".
   * Este paso confirma que los archivos se eliminarán de forma permanente y no se podrán recuperar.
4. Haz clic en **Eliminar**.

<p class="note">
  <strong>Nota:</strong> Con este método, se eliminarán todos los archivos multimedia de cada envío seleccionado; actualmente no es posible elegir solo los archivos de una pregunta específica.
</p>

![Eliminar archivos multimedia en bloque](images/managing_media_responses/bulk_delete.png)

## Resolución de problemas

<details>
  <summary><strong>La descarga como Archivos multimedia adjuntos (ZIP) queda en estado pendiente</strong></summary>
  Si una exportación de <strong>Archivos multimedia adjuntos (ZIP)</strong> permanece en el estado <strong>Pendiente... Haz clic para actualizar</strong> durante un período prolongado, actualiza la página o sal de la página de <strong>Descargas</strong> y vuelve a ella. No hagas clic repetidamente en <strong>Haz clic para actualizar.</strong>
</details>

<br>

<details>
  <summary><strong>La exportación ZIP de archivos multimedia adjuntos falla</strong></summary>
Si tu proyecto tiene muchos archivos multimedia o una conexión a internet lenta, es posible que la exportación de todos los archivos multimedia adjuntos como archivo ZIP falle o tarde demasiado. Hay dos opciones alternativas: descargar los archivos multimedia usando la extensión <a href="https://www.downthemall.net">DownThemAll</a>, o usar el script de descarga <a href="https://github.com/joshuaberetta/kobomedia">Kobo media</a> disponible en GitHub.
<br><br>
Para descargar archivos multimedia usando la extensión DownThemAll:
<ol>
  <li><a href="https://www.downthemall.net">Instala</a> la extensión DownThemAll en Firefox, Chrome o Edge.</li>
  <li><a href="https://support.kobotoolbox.org/es/export_download.html">Exporta tus datos</a> en formato XLS. Asegúrate de <a href="https://support.kobotoolbox.org/es/advanced_export.html#additional-data-format-options">incluir las URL de archivos multimedia</a>.</li>
  <li>Abre el archivo descargado en Excel, luego haz clic en <strong>Archivo > Guardar como</strong> y elige <strong>Página web (.htm o .html)</strong> como tipo de archivo.</li>
  <li>Abre el archivo HTML guardado en Firefox, Chrome o Edge, con la sesión iniciada en la cuenta de KoboToolbox donde están almacenados los archivos multimedia.</li>
  <li>Abre la extensión DownThemAll desde la página HTML e inicia la descarga.</li>
</ol>

Puedes ajustar la configuración de la extensión para limitar la velocidad de descarga o reintentar las descargas fallidas. Este método permite descargar todos los archivos multimedia, o solo los seleccionados, sin depender de la exportación ZIP.
</details>

<br>

<details>
  <summary><strong>Las URL de archivos multimedia de exportaciones anteriores ya no funcionan</strong></summary>
Los usuarios que dependen de las URL de archivos multimedia de exportaciones antiguas de Excel o CSV pueden notar que estos enlaces ya no funcionan desde que <a href="https://support.kobotoolbox.org/es/migrating_api.html">se deprecó la API v1</a>.
<br><br>
Las URL afectadas usan el formato antiguo:
<code>https://kc.kobotoolbox.org/media/original?media_file=...</code>
<br><br>
Para solucionar este problema, vuelve a exportar tus datos con la opción <strong>Incluir URL de archivos multimedia</strong> seleccionada. La nueva exportación incluirá las URL de archivos multimedia actualizadas.
<br><br>
Los usuarios avanzados también pueden recrear la exportación mediante <a href="https://support.kobotoolbox.org/es/synchronous_exports.html">exportaciones sincrónicas</a> o reconstruir las URL manualmente usando el formato actual de la API v2:
<code>https://kf.kobotoolbox.org/api/v2/assets/{asset_uid}/data/{submission_id}/attachments/{attachment_uid}/</code>
</details>