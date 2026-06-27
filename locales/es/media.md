# Agregar archivos multimedia a un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/media.md" class="reference">23 Apr 2026</a>

<iframe src="https://www.youtube.com/embed/7TrVmKIuCa8?si=QCr1IzvDXaASEZg7&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


KoboToolbox te permite agregar archivos multimedia, incluyendo **imágenes**, **archivos de audio** y **videos**, a notas, preguntas y opciones de tu formulario. Agregar archivos multimedia puede aumentar el compromiso de los usuarios y hacer que los formularios sean más accesibles para personas con discapacidades visuales o barreras de alfabetización.

Los archivos multimedia del formulario funcionan tanto con [KoboCollect](../es/data_collection_kobocollect.md) como con [formularios web](../es/data_through_webforms.md). Los siguientes tipos de archivos multimedia son compatibles actualmente:

| Multimedia | Archivos |
| :--- | :--- |
| Imagen | jpeg, png, svg |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Video | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv |

Este artículo cubre los siguientes temas:
- Agregar archivos multimedia a preguntas de la encuesta
- Agregar archivos multimedia a opciones de respuesta
- Agregar archivos multimedia a traducciones del formulario
- Cargar archivos multimedia a KoboToolbox

<p class="note">
    <strong>Nota:</strong> El <a href="../es/formbuilder.md">editor de formularios de KoboToolbox (Formbuilder)</a> no admite actualmente agregar archivos multimedia dentro de tus formularios. Para agregar archivos multimedia, debes usar XLSForm y luego cargarlo en KoboToolbox. Para obtener más información sobre cómo descargar y editar tu formulario como XLSForm, consulta <a href="../es/xlsform_with_kobotoolbox.md">Usar XLSForm con KoboToolbox</a>.
<br><br>
Para practicar con la adición de archivos multimedia en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar archivos multimedia a preguntas en XLSForm

Para agregar archivos multimedia a preguntas o notas en tu XLSForm:
1. Agrega una nueva pregunta en la **hoja survey**, especificando el `type`, `name` y `label` (opcional).
    - Utiliza un tipo de pregunta `note` si deseas mostrar el archivo multimedia sin recolectar datos (por ejemplo, el logotipo de una organización o un video de introducción).
    - Agregar una etiqueta es opcional cuando se incluye un archivo multimedia.
2. Agrega una columna para el tipo de multimedia que deseas incluir. Nómbrala `image`, `video` o `audio`, según el tipo de archivo multimedia.
3. En la columna de multimedia, en la fila de la pregunta que has agregado, ingresa el nombre exacto del archivo multimedia **incluyendo la extensión**.
    - Por ejemplo: `logo.png` o `intro.mp4`.

**hoja survey**

| type | name | label | image |
| :--- | :--- | :--- | :--- |
| text | Q1 | In your own words, how would you describe the image above? | q1.png |
| survey |

<p class="note">
    <strong>Nota:</strong> Anteriormente, el formato <code>media::file_type</code> se usaba para los nombres de columnas de multimedia (por ejemplo, <code>media::image</code>, <code>media::video</code>, <code>media::audio</code>). El formato simplificado que usa solo el tipo de multimedia sin el prefijo <code>media::</code> es ahora el más adoptado (por ejemplo, <code>image</code>, <code>video</code>, <code>audio</code>).
</p>

### Cargar archivos multimedia a KoboToolbox

Para cargar los archivos multimedia a KoboToolbox:
1. Ve a tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. En tu proyecto de KoboToolbox, navega a **CONFIGURACIÓN > Multimedia**.
3. Carga los archivos multimedia que has agregado a tu XLSForm, asegurándote de que el nombre del archivo sea exactamente el mismo.
4. Implementa o reimplementa tu formulario para ver los cambios en los archivos multimedia.

![Cargar archivos multimedia](images/media/upload_media.png)

<p class="note">
    Para obtener más información sobre cómo cargar archivos multimedia, consulta <a href="../es/upload_media.md">Importar archivos multimedia a un proyecto</a>.
</p>

## Agregar archivos multimedia a opciones de respuesta en XLSForm

Para agregar archivos multimedia a opciones de respuesta en tu XLSForm:
1. Agrega una [pregunta de tipo selección](../es/question_types_xls.md#select-question-types) en la **hoja survey**.
2. En la **hoja choices**, agrega un `list_name`, `name` y `label` (opcional) para tus opciones.
    - Agregar una etiqueta es opcional cuando se incluye un archivo multimedia. Si deseas usar los archivos multimedia como etiqueta de las opciones, omite el texto de la etiqueta.
3. Agrega una columna para el tipo de multimedia que deseas incluir. Nómbrala `image`, `video` o `audio`, según el tipo de archivo multimedia.
4. En la columna de multimedia, en la fila de las opciones que has agregado, ingresa el nombre del archivo multimedia **incluyendo la extensión**.
    - Por ejemplo: `goat.png` o `fish.png`

**hoja survey**

| name | type | label |
| :--- | :--- | :--- |
| select_one animals | animals | Which of these is your favorite animal? |
| survey |

**hoja choices**

| list_name | name | label | image |
| :--- | :--- | :--- | :--- |
| animals | goats | Goats | goat.png |
| animals | cows | Cows | cow.png |
| animals | chicken | Chickens | chicken.png |
| animals | pigs | Pigs | pig.png |
| animals | fish | Fish | fish.png |
| choices |

### Cargar archivos multimedia a KoboToolbox

Para cargar los archivos multimedia a KoboToolbox:
1. Ve a tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. En tu proyecto de KoboToolbox, navega a **CONFIGURACIÓN > Multimedia**.
3. Carga los archivos multimedia que has agregado a tu XLSForm, asegurándote de que el nombre del archivo sea exactamente el mismo.
4. Implementa o reimplementa tu formulario para ver los cambios en los archivos multimedia.

## Agregar archivos multimedia a traducciones

En los XLSForms que están [traducidos a varios idiomas](../es/language_xls.md), puedes incluir diferentes archivos multimedia para cada idioma agregando nuevas columnas `image`, `audio` o `video`.

Para agregar archivos multimedia para diferentes idiomas en tu **hoja survey**:

1. Renombra tus columnas de multimedia usando el formato `tipo_multimedia::idioma (código)`, donde `tipo_multimedia` es el tipo de archivo multimedia e `idioma` es el idioma predeterminado.
    - Por ejemplo: `image::English (en)`
2. Agrega una nueva columna de multimedia para cada idioma de traducción usando el formato `tipo_multimedia::idioma (código)`.
    - Por ejemplo: `audio::Spanish (es)`
3. En la columna de multimedia para cada idioma, ingresa el nombre del archivo multimedia que deseas incluir, incluyendo la extensión.
    - Para usar el mismo archivo multimedia para cada idioma, ingresa el mismo nombre de archivo que el de la columna del idioma predeterminado.

<p class="note">
    <strong>Nota:</strong> Si un archivo multimedia no aparece en una columna de traducción, no se mostrará para ese idioma.
</p>

**hoja survey**

| type | name | label | video::English (en) | video::Chichewa (ny) |
| :--- | :--- | :--- | :--- | :--- |
| note | intro | Before you answer the form, watch the video below: | intro.mp4 | intro_ny.mp4 |
| survey |

### Cargar archivos multimedia a KoboToolbox

Para cargar los archivos multimedia traducidos a KoboToolbox:
1. Ve a tu [cuenta de KoboToolbox](https://www.kobotoolbox.org/sign-up/).
2. En tu proyecto de KoboToolbox, navega a **CONFIGURACIÓN > Multimedia**.
3. Carga los archivos multimedia que has agregado a tu XLSForm, asegurándote de que el nombre del archivo sea exactamente el mismo.
4. Implementa o reimplementa tu formulario para ver los cambios en los archivos multimedia.

<p class="note">
    Para obtener más información sobre cómo gestionar traducciones en XLSForm, consulta <a href="../es/language_xls.md">Añadir traducciones en XLSForm</a>.
</p>

## Resolución de problemas

<details>
<summary><strong>Error al implementar o visualizar el formulario</strong></summary>
Si encuentras un error al implementar o visualizar tu formulario, verifica lo siguiente:
    <ul>
      <li>El archivo multimedia ha sido cargado en KoboToolbox en la pestaña <strong>Multimedia</strong> de la página <strong>CONFIGURACIÓN</strong>.</li>
      <li>El nombre del archivo en tu XLSForm coincide exactamente con el nombre y la extensión del archivo multimedia.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Los archivos multimedia no aparecen en el formulario implementado</strong></summary>
Si los archivos multimedia no aparecen en tu formulario implementado, verifica lo siguiente:
    <ul>
      <li>El archivo multimedia ha sido cargado en KoboToolbox en la pestaña <strong>Multimedia</strong> de la página <strong>CONFIGURACIÓN</strong>.</li>
      <li>El nombre del archivo en tu XLSForm coincide exactamente con el nombre y la extensión del archivo multimedia.</li>
      <li>El formulario ha sido <strong>reimplementado</strong> después de haber cargado los archivos multimedia.</li>
      <li>Has incluido archivos multimedia para cada traducción del formulario, si corresponde.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Cambiar el tamaño de un archivo multimedia</strong></summary>
Para controlar el tamaño de las imágenes que se muestran en tus preguntas u opciones, debes cargar archivos multimedia con las dimensiones deseadas. Ten en cuenta que usar archivos muy grandes puede aumentar los tiempos de carga en los formularios web.
</details>

<br>

<details>
<summary><strong>El formulario tarda mucho en cargar</strong></summary>
Los formularios web cargarán lentamente si tus archivos multimedia son grandes. Reduce el tamaño de los archivos de imagen, video o audio antes de cargarlos al servidor para mejorar los tiempos de carga.
</details>

<br>

<details>
<summary><strong>Cambiar la alineación de los archivos multimedia</strong></summary>
Los archivos multimedia en los formularios de KoboToolbox están centrados de forma predeterminada, y no es posible personalizar la alineación (izquierda o derecha).
</details>

<br>

<details>
<summary><strong>Los archivos GIF animados no son compatibles</strong></summary>
Los archivos GIF animados no son compatibles actualmente ni con los formularios web ni con la aplicación Android KoboCollect.
</details>

<br>

<details>
<summary><strong>No se puede cargar el archivo multimedia</strong></summary>
El tamaño máximo para la carga de archivos multimedia es de 100 MB. Los archivos que superen este límite deben reducirse en tamaño antes de cargarlos.
</details>