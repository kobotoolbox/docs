# Importar archivos multimedia a un proyecto
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/d9b44de6b0f7192771a9f7bf86edf271321f398b/source/upload_media.md" class="reference">27 Jan 2026</a>

KoboToolbox te permite cargar archivos multimedia y archivos de datos externos para usarlos en formularios durante la recolección de datos. Este artículo describe los tipos de archivos compatibles y explica cómo cargar archivos multimedia y archivos de datos externos a tu proyecto desde tu dispositivo local o mediante una URL.

<p class="note">
  Para obtener más información sobre los archivos y multimedia de los proyectos, consulta <a href="../es/project_files_media.html">Introducción a archivos y multimedia en los proyectos</a>.
</p>

## Tipos de archivos compatibles

KoboToolbox permite cargar los siguientes archivos:
- **Archivos multimedia**, como imágenes, grabaciones de audio y videos, para ayudar a los encuestados a comprender mejor las preguntas y enriquecer tu formulario.

<p class="note">
  Para aprender a incluir imágenes, videos o grabaciones de audio en XLSForm, consulta <a href="../es/media.html">Agregar archivos multimedia a un XLSForm</a>.
</p>

- **Archivos de datos externos**, como archivos CSV o XML, para gestionar listas de opciones extensas o dar soporte a la lógica del formulario. El uso de archivos externos facilita la reutilización y actualización de conjuntos de datos sin necesidad de editar el formulario, lo que reduce el mantenimiento continuo del formulario y favorece una recolección de datos consistente y de alta calidad.

<p class="note">
Para aprender a adjuntar conjuntos de datos externos a tu formulario, consulta <a href="../es/pull_data_kobotoolbox.html">Extraer datos de un archivo CSV externo</a> y <a href="../es/select_from_file_xls.html">Seleccionar opciones de un archivo externo en XLSForm</a>.
</p>

Actualmente se admiten los siguientes archivos para cargar en KoboToolbox:
| Tipo  | Extensiones de archivo |
|:-----|:----------------|
| Imagen | .jpeg, .png, .svg |
| Audio | .aac, .aacp, .flac, .mp3, .mp4, .mpeg, .ogg, .wav, .webm, .x-m4a, .x-wav |
| Video | .3gpp, .avi, .flv, .mov, .mp4, .ogg, .qtff, .webm, .wmv |
| Archivo  | .csv, .xml, .zip, .geojson |

## Cargar archivos desde tu dispositivo local

Después de agregar referencias a archivos multimedia o archivos externos en tu formulario, debes cargar esos archivos en tu proyecto. Esto se hace en la página **CONFIGURACIÓN > Archivos multimedia** de tu proyecto.

Para cargar archivos y multimedia desde tu dispositivo local:
1. Inicia sesión en tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Abre tu proyecto y ve a la página **CONFIGURACIÓN**.
3. Abre la pestaña <i class="k-icon-file-image"></i> **Archivos multimedia**.
4. Carga los archivos que usa tu formulario. Los nombres de los archivos deben coincidir exactamente con los nombres referenciados en el formulario.
5. Implementa o reimplementa el formulario para aplicar los cambios.

![Upload media](images/upload_media/upload_media.png)

<p class="note">
<strong>Nota:</strong> El tamaño máximo de archivo para las cargas es de 100 MB. Los archivos que superen este tamaño deben reducirse antes de cargarlos.
</p>

## Cargar archivos mediante URL

<iframe src="https://www.youtube.com/embed/MBU77LUrflA?si=_BRYlIlojJGOqnuT&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

También puedes cargar un archivo en KoboToolbox proporcionando una URL directa al archivo. Esto puede ser útil si tu archivo está alojado en línea, como un archivo CSV almacenado en un repositorio de GitHub.

Para cargar archivos y multimedia mediante URL:
1. Inicia sesión en tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. Abre tu proyecto y ve a la página **CONFIGURACIÓN**.
3. Abre la pestaña <i class="k-icon-file-image"></i> **Archivos multimedia**.
4. Pega una URL válida en el campo "También se pueden agregar archivos usando una URL" (consulta los requisitos a continuación). Haz clic en **Agregar**.
5. Implementa o reimplementa el formulario para aplicar los cambios.

![Upload image URL](images/upload_media/upload_url.png)

<p class="note">
<strong>Nota:</strong> El nombre del archivo al final de la URL debe coincidir exactamente con el nombre del archivo referenciado en el formulario.
</p>

### Requisitos de la URL

La URL debe cumplir los dos requisitos siguientes:

- La URL debe terminar con una extensión de archivo compatible (por ejemplo, `.png`, `.jpg` o `.csv`).
- La URL debe abrir el archivo directamente en tu navegador, no una página web que contenga el archivo. La URL no funcionará si apunta a una página de un servicio como Google Drive, GitHub o Dropbox.

<p class="note">
<strong>Nota:</strong> Si el archivo se elimina o deja de estar disponible, dejará de funcionar en KoboToolbox.
</p>

### Obtener una URL directa para imágenes

Para las imágenes, usa la dirección directa de la imagen desde el sitio web de origen.

Para obtener una URL de imagen utilizable:
1. Abre la página web que contiene la imagen.
2. Haz clic derecho sobre la imagen y selecciona **Copiar dirección de imagen** (o la opción equivalente en tu navegador).
- Confirma que la URL termina con una extensión de imagen (por ejemplo, `.png` o `.jpg`).
3. Pega la URL en tu navegador para confirmar que abre la imagen directamente.

### Obtener una URL directa para archivos CSV

Para los archivos `.csv`, la URL debe abrir el contenido CSV sin procesar directamente en tu navegador. Un método habitual es alojar el CSV en GitHub y usar el enlace Raw:

1. Sube o confirma tu archivo `.csv` en un repositorio de GitHub.
2. Abre el archivo CSV en GitHub.
3. Haz clic en **Raw**. El contenido del CSV debe mostrarse directamente en tu navegador.
4. Copia la URL de la barra de direcciones de tu navegador.

<p class="note">
<strong>Nota:</strong> Google Sheets publicado como CSV no es compatible con este flujo de trabajo, ya que KoboToolbox no acepta el formato que produce ese método.
</p>

Si actualizas el archivo CSV en la misma URL, KoboToolbox **reflejará el archivo actualizado tras un breve retraso.** Para obtener las actualizaciones de forma más consistente, recomendamos reimplementar el formulario con regularidad.

### Referenciar archivos cargados en tu formulario

Una vez que el archivo esté disponible en KoboToolbox, referencíalo de la misma manera que lo harías con otros archivos multimedia o archivos de opciones cargados:

- En preguntas de tipo `select_one_from_file` o `select_multiple_from_file`
- Dentro de la función `pulldata()`
- En las columnas de multimedia de tu XLSForm (`image`, `audio`, `video`)

Al hacer referencia a los archivos cargados, usa **únicamente el nombre del archivo y su extensión** al final de la URL (por ejemplo, `choices.csv` o `photo.jpg`). No incluyas la URL completa en estos campos.