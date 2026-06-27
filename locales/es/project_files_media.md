# Introducción a archivos y multimedia en los proyectos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/project_files_media.md" class="reference">23 Apr 2026</a>

Un proyecto de KoboToolbox puede incluir archivos y multimedia añadidos en diferentes etapas del proceso de recolección de datos.

Durante el desarrollo del formulario, puedes:

- **Adjuntar archivos multimedia** para enriquecer tu formulario con imágenes, audio o video.
- **Adjuntar archivos de datos externos** para gestionar listas de opciones extensas o extraer datos en tu formulario.

Durante la recolección de datos, los encuestados pueden **enviar sus propios archivos y multimedia** como parte de sus respuestas.

Estas dos categorías se gestionan de manera diferente dentro de un proyecto.

<p class="note">
<strong>Nota:</strong> Solo los archivos multimedia enviados por los encuestados cuentan para los límites de almacenamiento de tu plan.
</p>

Este artículo ofrece una descripción general de los siguientes temas:
- Agregar archivos multimedia y archivos de datos a tu formulario
- Cargar archivos y multimedia en KoboToolbox
- Recolectar archivos y multimedia de los encuestados
- Ver, descargar y eliminar archivos multimedia de los encuestados

## Adjuntar archivos externos y multimedia a tu formulario

KoboToolbox te permite **cargar archivos multimedia** en tu formulario, como imágenes, grabaciones de audio y videos, para ayudar a los encuestados a comprender mejor las preguntas y reducir la necesidad de aclaraciones posteriores.

KoboToolbox también te permite **adjuntar archivos CSV externos** a tu formulario para gestionar listas de opciones extensas o respaldar la lógica del formulario. El uso de archivos externos facilita la reutilización y actualización de conjuntos de datos sin necesidad de editar el formulario, lo que reduce el mantenimiento continuo del formulario y favorece la obtención de datos consistentes y de alta calidad.

Las secciones a continuación ofrecen una descripción general de estas funcionalidades y enlazan a los artículos de ayuda correspondientes.

### Agregar multimedia a tu formulario

Incluir imágenes, videos o grabaciones de audio en las notas, preguntas y opciones de tu formulario puede hacer que los formularios sean **más atractivos y accesibles.** Esto puede ser especialmente útil para usuarios con discapacidades visuales o barreras de alfabetización.

![Formulario con multimedia](images/project_files_media/form.png)

Para incluir multimedia en tu formulario, debes usar XLSForm y luego [cargar el XLSForm](https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html) en KoboToolbox. El Formbuilder de KoboToolbox no permite actualmente agregar archivos multimedia directamente en el editor de formularios.

<p class="note">
  Para aprender a incluir imágenes, videos o grabaciones de audio en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/media.html">Agregar archivos multimedia a un XLSForm</a>.
</p>

### Adjuntar archivos de datos externos a tu formulario

Además de cargar archivos multimedia, KoboToolbox permite adjuntar archivos de datos externos a tus formularios para recuperar o referenciar datos externos durante la recolección de datos.

Hay dos formas principales de conectar tu formulario a archivos externos:

- La función `pulldata()` **extrae información de un archivo de datos externo** mientras se completa un formulario. Esto es útil para referenciar conjuntos de datos existentes y reducir la entrada repetida de datos por parte de los encuestadores.

<p class="note">
<strong>Nota:</strong> La función <code>pulldata()</code> utiliza archivos externos como fuente de datos. Si deseas referenciar datos de otro proyecto de KoboToolbox en lugar de un archivo CSV, puedes usar <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">conexión dinámica de proyectos</a>.
</p>

- Los tipos de pregunta `select_one_from_file` y `select_multiple_from_file` te permiten **definir listas de opciones en un archivo externo** en lugar de directamente en el formulario. El uso de archivos externos para las listas de opciones facilita la gestión de listas extensas, su reutilización en varios formularios y su actualización con el tiempo.

Los formatos de archivo compatibles con estas funcionalidades incluyen CSV, XML y GeoJSON.

<p class="note">
  Para aprender a adjuntar conjuntos de datos externos a tu formulario, consulta <a href="https://support.kobotoolbox.org/es/pull_data_kobotoolbox.html">Extraer datos de un archivo CSV externo</a> y <a href="https://support.kobotoolbox.org/es/external_file.html">Seleccionar opciones de archivos externos en el Formbuilder</a>.
</p>

### Cargar archivos y multimedia en KoboToolbox

Después de agregar referencias multimedia o archivos externos a tu formulario, debes cargar esos archivos en tu proyecto. Esto se hace en la página **CONFIGURACIÓN > Multimedia** de tu proyecto.

<p class="note">
  Para aprender a cargar archivos y multimedia en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/upload_media.html">Importar archivos multimedia a un proyecto</a>.
</p>

Los siguientes tipos de archivos son compatibles actualmente para cargar en KoboToolbox:

| Multimedia | Tipos |
|:-----|:------|
| Imagen | .jpeg, .png, .svg |
| Audio | .aac, .aacp, .flac, .mp3, .mp4, .mpeg, .ogg, .wav, .webm, .x-m4a, .x-wav |
| Video | .3gpp, .avi, .flv, .mov, .mp4, .ogg, .qtff, .webm, .wmv |
| Archivo | .csv, .xml, .zip, .geojson |

<p class="note">
<strong>Nota:</strong> El tamaño máximo de archivo para cargas es de 100 MB. Los archivos que superen este tamaño deben reducirse antes de cargarlos.
</p>

## Recolectar archivos y multimedia de los encuestados

Además de incluir multimedia en tu formulario, puedes recolectar archivos y multimedia directamente de los encuestados durante la recolección de datos. Esto incluye **imágenes, grabaciones de audio, videos y otros tipos de archivos.** Recolectar multimedia te permite capturar información cualitativa que añade contexto visual o auditivo a tus datos.

<p class="note">
<strong>Nota:</strong> Cada archivo enviado por un encuestado puede tener un tamaño de hasta 10 MB, con un máximo total de 100 MB por envío.
</p>

Los siguientes tipos de preguntas multimedia están disponibles en KoboToolbox:

| Tipo de pregunta en el Formbuilder | Tipo de pregunta en XLSForm | Descripción |
|:--------------------------|:----------------------|:------------|
| Foto | `image` | Captura o carga una imagen. También se puede usar para recolectar [dibujos, imágenes anotadas y firmas](https://support.kobotoolbox.org/es/photo_audio_video_file.html#advanced-appearances). |
| Audio | `audio` | Graba o carga un archivo de audio. |
| Video | `video` | Graba o carga un archivo de video. |
| Archivo | `file` | Adjunta un archivo (por ejemplo, .pdf, .docx). |

KoboToolbox también permite la grabación de audio de fondo para entrevistas completas o grupos focales.

<p class="note">
  Para obtener más información sobre la recolección de multimedia de los encuestados, consulta <a href="https://support.kobotoolbox.org/es/photo_audio_video_file.html">Preguntas Multimedia en KoboToolbox</a>. Para obtener más información sobre la grabación de audio de fondo, consulta <a href="https://support.kobotoolbox.org/es/recording-interviews.html#recording-interviews-with-background-audio-recordings">Recolectar datos cualitativos con KoboToolbox</a>.
</p>

### Ver archivos multimedia de los encuestados

Todos los archivos multimedia enviados por los encuestados pueden verse desde la tabla de datos. Las imágenes también pueden verse en la vista de **Galería** de tu proyecto.

<p class="note">
  Para obtener más información sobre cómo ver los archivos multimedia de los encuestados, consulta <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#viewing-media-files">Gestionar respuestas con archivos multimedia</a>.
</p>

### Descargar archivos multimedia de los encuestados

Puedes descargar archivos multimedia de forma individual desde la tabla de datos, o de forma masiva desde la página de **Descargas**.

Cuando exportas tus datos en formato CSV o XLS, el archivo exportado también incluye hipervínculos que abren los archivos multimedia asociados en un navegador web, siempre que esté seleccionada la opción predeterminada **Incluir URL de archivos multimedia**.

<p class="note">
  Para obtener más información sobre cómo exportar tus archivos multimedia, consulta <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#downloading-media-files">Gestionar respuestas con archivos multimedia</a>.
</p>

### Eliminar archivos multimedia de los encuestados

Por último, es posible que necesites eliminar archivos multimedia para **gestionar el almacenamiento, proteger la confidencialidad o corregir errores en los envíos.** Los archivos multimedia pueden eliminarse de forma individual o de forma masiva.

Una vez eliminado un archivo, aparece marcado como *Eliminado* en la tabla de datos y no puede recuperarse.

<p class="note">
  Para obtener información sobre los diferentes métodos para eliminar archivos multimedia, consulta <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#deleting-media-files">Gestionar respuestas con archivos multimedia</a>.
</p>