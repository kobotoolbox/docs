# Eliminar archivos multimedia
<a href="../deleting_media.html">Read in English</a> | <a href="../fr/deleting_media.html">Lire en français</a> | <a href="../ar/deleting_media.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/32227ed7144b2a84f5774494d8d5ac4935ca0349/source/deleting_media.md" class="reference">4 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/J0-mh1R6dEs?si=I4Oe8NHX7Ks5rFza" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Puede que necesites eliminar archivos multimedia de tu proyecto de KoboToolbox por varias razones, como mantener la confidencialidad, manejar el espacio de almacenamiento o corregir errores en los envíos. Este artículo explica cómo eliminar archivos multimedia individuales o múltiples archivos de forma masiva, incluyendo imágenes, videos, archivos de audio y archivos de documentos.

## Eliminar archivos multimedia individuales

Hay dos formas de eliminar archivos multimedia individuales: directamente desde la tabla de datos o abriendo el envío. Una vez que se elimina un archivo, se marca como _Eliminado_ en la tabla de datos y no se puede recuperar.

### Eliminar archivos multimedia individuales desde la tabla de datos

Puedes eliminar imágenes, videos y archivos individuales directamente desde la tabla de datos, con los siguientes pasos:

1. En la tabla de datos, localiza la celda con el archivo multimedia que deseas eliminar.
2. Haz clic en el ícono de <i class="k-icon k-icon-qt-photo"></i> **imagen**, <i class="k-icon k-icon-qt-video"></i> **video** o <i class="k-icon k-icon-qt-file"></i> **archivo**.
3. Haz clic en los <i class="k-icon k-icon-more"></i> **tres puntos** en la parte superior de la vista previa del archivo.
4. Haz clic en <i class="k-icon k-icon-trash"></i> **Eliminar**, luego en **Eliminar** nuevamente para confirmar.

![image](/images/deleting_media/delete_from_table.png)

### Eliminar archivos multimedia individuales en la vista de envío

También puedes eliminar archivos multimedia abriendo la vista de envío:

1. En la tabla de datos, localiza el envío con los archivos multimedia que deseas eliminar.
2. En el lado izquierdo del envío, haz clic en <i class="k-icon k-icon-view"></i> **Abrir**.
3. Desplázate hacia abajo hasta el archivo multimedia que deseas eliminar.
4. Haz clic en los <i class="k-icon k-icon-more"></i> **tres puntos** a la derecha del archivo multimedia.
5. Haz clic en <i class="k-icon k-icon-trash"></i> **Eliminar**, luego en **Eliminar** nuevamente para confirmar.

![image](/images/deleting_media/open_submission_view.png)

### Eliminar archivos de audio en la vista de pregunta de audio
Puedes eliminar archivos de audio abriendo la vista de pregunta de audio para transcripción, traducción y análisis de preguntas de audio:

1. En la tabla de datos, haz clic en **Abrir** <i class="k-icon k-icon-arrow-up-right"></i> para abrir la vista de pregunta de audio.
2. En la ventana **TRANSCRIPCIÓN**, **TRADUCCIONES** o **ANÁLISIS**, localiza el archivo de audio en la esquina superior derecha.
3. Haz clic en los <i class="k-icon k-icon-more"></i> **tres puntos** a la derecha del archivo de audio.
4. Haz clic en <i class="k-icon k-icon-trash"></i> **Eliminar**, luego en **Eliminar** nuevamente para confirmar.

![image](/images/deleting_media/delete_audio.png)

## Eliminar archivos multimedia de forma masiva

Puede que necesites eliminar archivos multimedia de forma masiva, por ejemplo, para manejar el espacio de almacenamiento después de que hayan sido exportados. Puedes eliminar todos los archivos multimedia de los envíos seleccionados usando los siguientes pasos:

1. Selecciona los envíos de los cuales deseas eliminar archivos multimedia.
2. Haz clic en **Eliminar solo archivos multimedia** encima de la tabla de datos.
   * Esta acción abre una ventana modal que muestra el número y los tipos de archivos multimedia que se eliminarán con esta selección.
3. Marca la casilla que dice "Estás a punto de eliminar permanentemente los siguientes archivos multimedia de los envíos seleccionados:".
   * Este paso reconoce que los archivos se eliminarán permanentemente y no son recuperables.
4. Haz clic en **Eliminar**.

<p class="note">
  <b>Nota:</b> Con este enfoque, se eliminarán todos los archivos multimedia de cada envío seleccionado; actualmente no es posible elegir solo archivos de una pregunta determinada.
</p>

![image](/images/deleting_media/bulk_delete.png)