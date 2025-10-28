# Agregar Varios Tipos de Medios (imagen, audio, video) a un Formulario
<a href="../media.html">Read in English</a> | <a href="../fr/media.html">Lire en français</a> | <a href="../ar/media.html">اقرأ باللغة العربية</a>

**Última actualización:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/media.md" class="reference">15
Feb 2022</a>

Además de preguntas de texto y opciones de texto, también puedes agregar varios tipos
de medios (como _imagen_, _audio_ y _video_) a tus formularios. Tener medios en
un formulario a veces puede ayudarte a expresar tus preguntas y opciones
de una manera mucho mejor.

Los medios en un formulario funcionan tanto en la **aplicación de Android de Collect** como en los **formularios web
(Enketo)**. Estos son los archivos de medios que actualmente son compatibles:

| Medios | Archivos                                                      |
| :----- | :------------------------------------------------------------ |
| Imagen | jpeg, png, svg                                                |
| Audio  | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Video  | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv    |

Este artículo de ayuda tiene como objetivo ilustrar cómo se pueden crear formularios con medios con
**KoboToolbox**. Sigue las instrucciones descritas a continuación para incluir medios en tu
proyecto de encuesta.

## Paso 1: Descargar el Formulario como XLSForm

Crea un proyecto de encuesta en la interfaz de usuario del editor de formularios de KoboToolbox (Formbuilder) y luego descarga tu formulario como XLS
para agregar configuraciones de medios. El editor de formularios actualmente no admite agregar
medios al formulario directamente, por lo que necesitarás editar el XLSForm descargado para
completar esta acción.

<video controls><source src="./_static/files/media/download_xlsform.mp4" type="video/mp4"></video>

## Paso 2: Agregar Columnas de Medios a tu XLSForm

<p class='note'>Los nombres de archivo agregados al XLSForm deben coincidir con los nombres de archivo que
diste a tus archivos de <em>imagen</em>, <em>audio</em> y
<em>video</em>.</p>

### Agregar Columnas de Medios de Imagen:

Si deseas agregar una **imagen** a una pregunta, entonces escribe `media::image` como
encabezado de columna en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de imagen
junto con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::image`.

De manera similar, si deseas agregar una **imagen** a una opción, entonces escribe
`media::image` como encabezado de columna en la pestaña **choices** de tu XLSForm. Una
vez más, escribe el nombre del archivo de imagen junto con una extensión en la opción correspondiente
justo debajo del encabezado de columna `media::image`.

<video controls><source src="./_static/files/media/adding_media_image.mp4" type="video/mp4"></video>

### Agregar Columnas de Medios de Audio:

Si deseas agregar **audio** a una pregunta, entonces escribe `media::audio` como
encabezado de columna en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de audio junto
con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::audio`.

De manera similar, si deseas agregar **audio** a una opción, entonces escribe `media::audio` como
encabezado de columna en la pestaña **choices** de tu XLSForm. Una vez más, escribe el
nombre del archivo de audio junto con una extensión en la opción correspondiente justo debajo del
encabezado de columna `media::audio`.

<video controls><source src="./_static/files/media/adding_media_audio.mp4" type="video/mp4"></video>

### Agregar Columnas de Medios de Video:

Si deseas agregar video a una pregunta, entonces escribe `media::video` como
encabezado de columna en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de video junto
con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::video`.

De manera similar, si deseas agregar video a una opción, entonces escribe `media::video` como
encabezado de columna en la pestaña **choices** de tu XLSForm. Una vez más, escribe el
nombre del archivo de video junto con una extensión en la opción correspondiente justo debajo del
encabezado de columna `media::video`.

<video controls><source src="./_static/files/media/adding_media_video.mp4" type="video/mp4"></video>

## Paso 3: Manejar Columnas de Medios para Múltiples Idiomas

<p class='note'>Este paso es para aquellos/as que tienen múltiples idiomas en su proyecto de
encuesta.</p>

Puedes tener una encuesta con múltiples idiomas y querer agregar varios tipos de
medios relevantes para idiomas específicos. En tales casos, podrías seguir las
ilustraciones proporcionadas a continuación.

### Manejar Columna de Medios para Medios de Imagen:

Si deseas agregar imagen a una pregunta, entonces escribe `media::image` como
encabezado de columna en la pestaña **survey** de tu XLSForm. Escribe el nombre del archivo de imagen junto
con una extensión en la pregunta correspondiente justo debajo del
encabezado de columna `media::image::Idioma (código de idioma)`.

De manera similar, si deseas agregar imagen a una opción, entonces escribe
`media::image::Idioma (código de idioma)` como encabezado de columna en la pestaña **choices**
de tu XLSForm. Una vez más, escribe el nombre del archivo de imagen junto con una extensión
en la opción correspondiente justo debajo del
encabezado de columna `media::image::Idioma (código de idioma)`.

<video controls><source src="./_static/files/media/adding_media_image_language.mp4" type="video/mp4"></video>

### Manejar Columna de Medios para Medios de Audio:

Si deseas agregar audio a una pregunta, entonces escribe
`media::audio::Idioma (código de idioma)` como encabezado de columna en la pestaña **survey**
de tu XLSForm. Escribe el nombre del archivo de audio junto con una extensión en la
pregunta correspondiente justo debajo del
encabezado de columna `media::audio::Idioma (código de idioma)`.

De manera similar, si deseas agregar audio a una opción, entonces escribe
`media::audio::Idioma (código de idioma)` como encabezado de columna en la pestaña **choices**
de tu XLSForm. Una vez más, escribe el nombre del archivo de audio junto con una extensión
en la opción correspondiente justo debajo del
encabezado de columna `media::audio::Idioma (código de idioma)`.

<video controls><source src="./_static/files/media/adding_media_audio_language.mp4" type="video/mp4"></video>

### Manejar Columna de Medios para Medios de Video:

Si deseas agregar video a una pregunta, entonces escribe
`media::video::Idioma (código de idioma)` como encabezado de columna en la pestaña **survey**
de tu XLSForm. Escribe el nombre del archivo de video junto con una extensión en la
pregunta correspondiente justo debajo del
encabezado de columna `media::video::Idioma (código de idioma)`.

De manera similar, si deseas agregar video a una opción, entonces escribe
`media::video::Idioma (código de idioma)` como encabezado de columna en la pestaña **choices**
de tu XLSForm. Una vez más, escribe el nombre del archivo de video junto con una extensión
en la opción correspondiente justo debajo del
encabezado de columna `media::video::Idioma (código de idioma)`.

<video controls><source src="./_static/files/media/adding_media_video_language.mp4" type="video/mp4"></video>

## Paso 4: Reemplazar XLSForm

Carga y reemplaza tu XLSForm en el proyecto existente o crea un nuevo
proyecto.

<video controls><source src="./_static/files/media/replacing_xlsform.mp4" type="video/mp4"></video>

## Paso 5: Cargar Archivos de Medios

Ve a **AJUSTES>Medios**. Carga todos los archivos de medios que han sido referenciados en
tu formulario.

<video controls><source src="./_static/files/media/uploading_media.mp4" type="video/mp4"></video>

<p class='note'><strong>Consejo:</strong> Reúne todos los archivos de medios que incluirás en tu proyecto de
encuesta. Proporciona un nombre de archivo corto para cada uno de los medios. Los nombres de archivo
con un espacio (por ejemplo, "libro rojo") no son compatibles con el sistema. Por lo tanto,
necesitarás eliminar el espacio entre los nombres (por ejemplo,
"librorojo") o usar '_' para un espacio (por ejemplo, "libro_rojo").</p>

## Paso 6: Desplegar Formulario

Una vez que hayas reemplazado el XLSForm y luego cargado todos los archivos de medios,
necesitarás desplegar tu encuesta.

<video controls><source src="./_static/files/media/deploying_form.mp4" type="video/mp4"></video>

<p class='note'>Cada vez que se agregan o cambian nuevos archivos de medios, necesitas
<strong>redesplegar</strong> tu proyecto para que el cambio surta efecto.
Puedes ver tus nuevos medios al previsualizar tu formulario
<em>antes</em> del redespliegue.</p>

## Paso 7: Recolectar Datos

Ahora puedes volver a **Formulario>Recolectar Datos**, y luego hacer clic en **Abrir** para verificar
si los medios se muestran correctamente.

<video controls><source src="./_static/files/media/collecting_data.mp4" type="video/mp4"></video>

<p class='note'>Los archivos GIF animados actualmente no son compatibles con Enketo o
la aplicación de Android de Collect. Alinear medios a una ubicación deseada del formulario (alineación izquierda,
alineación central o alineación derecha) tampoco es
posible.</p>

## Consejos y Trucos

### Identificar el nombre de archivo, extensión y tamaño de un archivo de medios en Windows

-   Selecciona un archivo de medios (imagen, audio o video).
-   Haz clic derecho con tu mouse cuando el archivo de medios aún esté seleccionado.

![Dropdown select properties](images/media/dropdown_select_properties.png)

-   Luego selecciona **Propiedades**.
-   Ahora deberías poder ver el *nombre de archivo* y la *extensión* del archivo de
    medios en la pestaña **General**.

![Image properties](images/media/image_properties.png)

-   También deberías poder identificar las dimensiones y el tamaño de los medios en la
    pestaña **Detalles**. Si deseas tener imágenes pequeñas en tu pregunta u
    opciones, necesitarás cargar medios con una dimensión más pequeña, o
    viceversa.

<p class='note'>Los medios en un formulario Enketo tomarán más tiempo en cargar si
tienes archivos grandes. Intenta reducir los tamaños de los archivos de imagen, video o audio
antes de cargarlos al servidor.</p>

![Image details](images/media/image_details.png)

<p class='note'>Puedes acceder al XLSForm <a download class='reference'
href='./_static/files/media/xlsform-example.xls'>aquí</a> y a los archivos de medios <a
download class='reference'
href='./_static/files/media/xlsform-example-media.zip'>aquí</a> que fueron utilizados
en este artículo.</p>