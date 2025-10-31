# Tipos de preguntas "Foto", "Audio", "Video" y "Archivo"
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/27c3e37a283d79de0cbecebbf3a41d5b6ba6d7df/source/photo_audio_video_file.md" class="reference">11 Sep 2023</a>

Con KoboToolbox, puedes recolectar diferentes tipos de medios como parte de tu
proyecto de recolección de datos.

Cuando quieras capturar imágenes como parte de tus envíos, usa el tipo de
pregunta "Foto".

Si una pregunta requiere que grabes o adjuntes un archivo de audio, como cuando
se espera una explicación larga del/la encuestado/a, usa el tipo de pregunta "Audio".
La última versión de KoboCollect te permite grabar audio dentro de la aplicación
misma sin abrir una aplicación separada.

Con el tipo de pregunta "Video", podrás grabar un video usando la
cámara del dispositivo o adjuntar un archivo de video.

Si una pregunta requiere que adjuntes un archivo como un PDF, puedes usar el
tipo de pregunta "Archivo".

## Cómo configurar los tipos de preguntas "Foto", "Audio", "Video" y "Archivo"

### Configuración en el editor de formularios

Agregar preguntas de medios es simple:

- Haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "Toma una foto de la unidad de vivienda", luego
  haz clic en **AGREGAR PREGUNTA** o presiona ENTER en tu teclado
- Elige el tipo de pregunta

![Agregar pregunta de medios](images/photo_audio_video_file/add.gif)

### Configuración en XLSForm

Para agregar preguntas de medios en XLSForm, usa los tipos de pregunta `image`, `audio`, `video` o `file`
como se muestra en el siguiente ejemplo:

| type   | name        | label                                                       | hint            |
| :----- | :---------- | :---------------------------------------------------------- | :-------------- |
| image  | house_photo | Toma una foto de la unidad de vivienda                      |                 |
| audio  | impact      | ¿Cuál ha sido el impacto del proyecto en tu hogar?          | Grabar como audio |
| video  | preparation | Graba un video del/la encuestado/a mientras prepara el VitaMeal |                 |
| file   | CV          | Adjunta tu CV                                               |                 |
| survey |

## Apariencia de los tipos de preguntas "Foto", "Audio", "Video" y "Archivo"

### Apariencia predeterminada

![Apariencias predeterminadas](images/photo_audio_video_file/default_appearances.png)

### Apariencias avanzadas para el tipo de pregunta "Foto"

Al agregar el tipo de pregunta "Foto", puedes elegir entre varias
apariencias (en la configuración de la pregunta). Las apariencias cambian la forma en que la
pregunta se muestra en los formularios web y KoboCollect.

![Apariencias avanzadas para el tipo de pregunta foto](images/photo_audio_video_file/advanced_appearances_photo.png)

![Apariencias avanzadas](images/photo_audio_video_file/advanced_appearances.png)

### Agregar apariencias avanzadas en XLSForm

Puedes especificar apariencias avanzadas de la pregunta "Foto" en XLSForm bajo
la columna appearance como se muestra en el siguiente ejemplo:

| type   | name       | label                      | appearance |
| :----- | :--------- | :------------------------- | :--------- |
| image  | sign       | Firma aquí                 | signature  |
| image  | drawing    | Dibuja aquí                | draw       |
| image  | annotation | Toma una imagen y anota    | annotate   |
| survey |

## Grabación de audio de fondo

Puedes grabar audio en segundo plano cuando abres el formulario en KoboCollect.
Esto puede ser útil en varios escenarios de recolección de datos, incluyendo grupos focales
de discusión y entrevistas con informantes clave.

Activa la grabación de audio de fondo en el editor de formularios haciendo clic en **Diseño y
Configuración** y habilitando la función.

![Audio de fondo](images/photo_audio_video_file/background_audio.png)

<p class="note">
  La grabación de audio de fondo solo está disponible en KoboCollect y
  <strong>no</strong> en los formularios web de Enketo.
</p>

En XLSForm, puedes habilitar la grabación de fondo con el tipo de pregunta `background-audio`.
Este se considera un tipo de pregunta "meta" y por lo tanto no se requiere
`label`, solo un `name`. La calidad del audio se puede configurar bajo la
columna `parameters`, como se explica [aquí](recording-interviews.md).

| type             | name             | label |
| :--------------- | :--------------- | :---- |
| background-audio | background_audio |       |
| survey           |

<p class="note">
  No es posible grabar audio usando el tipo de pregunta "Audio" mientras
  la grabación de audio de fondo está en curso en el formulario. Cuando la grabación de audio de
  fondo está activada, todos los tipos de pregunta "Audio" se desactivan.
</p>

Puedes leer más sobre la grabación de audio de fondo
[aquí](recording-interviews.md).

## Reducir el tamaño de archivo de los medios recolectados

Si estás recolectando muchos medios en tu proyecto, podrías tener dificultades
para subirlos a KoboToolbox dependiendo de la velocidad de tu conexión a
internet. Si estás usando el [Servidor Global o el Servidor con sede en la Unión Europea](creating_account.md), entonces también
estás limitado/a a solo 1GB de almacenamiento gratuito. Es una buena idea manejar los
tamaños de archivo de los archivos de medios recolectados como imágenes, audio y videos.

Puedes definir el tamaño máximo de las imágenes que recolectas usando el tipo de pregunta "Foto"
yendo a la configuración de la pregunta y estableciendo la configuración "max-pixels" en
el editor de formularios.

![Píxeles máximos](images/photo_audio_video_file/max-pixels.png)

En XLSForm, puedes hacer lo mismo agregando "max-pixels" en la columna `parameters`
de la siguiente manera:

| type   | name  | label         | parameters     |
| :----- | :---- | :------------ | :------------- |
| image  | photo | Capturar foto | max-pixels=480 |
| survey |

En KoboCollect, también puedes elegir la calidad del video y el tamaño de la foto a través de la
sección de Manejo de Formularios de la configuración del proyecto.

Puedes leer más sobre cómo reducir los tamaños de archivo [aquí](lower_file_size.md).

## Limitar los tipos de archivo aceptados para el tipo de pregunta "Archivo"

Todos los tipos de archivo son aceptados por defecto para el tipo de pregunta "Archivo". En el
editor de formularios puedes restringir esto haciendo lo siguiente:

- Ve a la configuración de la pregunta "Archivo"
- En el cuadro "Archivos Aceptados", ingresa las extensiones de archivo de los archivos que
  te gustaría permitir, separadas por una coma, por ejemplo ".doc, .pdf, .xlsx"

![Tipos de archivo](images/photo_audio_video_file/file_types.png)

En XLSForm, puedes limitar los tipos de archivo aceptados especificando extensiones de archivo
en la columna `body::accept` de la siguiente manera:

| type   | name | label          | body::accept |
| :----- | :--- | :------------- | :----------- |
| file   | CV   | Adjunta tu CV  | .pdf, .doc   |
| survey |

<p class="note">
  Descarga un XLSForm con ejemplos de este artículo
  <a
    download
    class="reference"
    href="./_static/files/photo_audio_video_file/media_question_types.xlsx"
    >aquí</a
  >.
</p>