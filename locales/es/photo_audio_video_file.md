# Preguntas Multimedia en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/cfb4a1f8edd217a9c0ed64bd0bfc86e6fda70baa/source/photo_audio_video_file.md" class="reference">6 de mayo de 2026</a>

Muchos proyectos de recolección de datos requieren más que solo datos cuantitativos. KoboToolbox te permite capturar diversos archivos multimedia de los encuestados, incluyendo fotos, grabaciones de audio, videos y archivos, para proporcionar información cualitativa clave y añadir profundidad visual y auditiva a tus conjuntos de datos.

El método para capturar o cargar archivos multimedia depende de si usas [KoboCollect](../es/data_collection_kobocollect.html) o [formularios web](../es/data_through_webforms.html) para la recolección de datos. Al usar KoboCollect o formularios web en un dispositivo móvil, puedes capturar imágenes o videos directamente desde el dispositivo o cargar archivos. Al usar formularios web en una computadora, solo puedes cargar imágenes o videos. En todos los casos, puedes grabar audio directamente dentro del formulario.

Este artículo cubre los siguientes temas:
- Tipos de preguntas multimedia disponibles en KoboToolbox
- Agregar preguntas multimedia con el Formbuilder
- Aspectos predeterminados y avanzados de las preguntas multimedia
- Parámetros para preguntas multimedia

## Tipos de preguntas multimedia

Los siguientes tipos de preguntas multimedia están disponibles en el editor de formularios de KoboToolbox **(Formbuilder)**:

| Tipo de pregunta | Descripción |
|:-----------------|:------------|
| Foto | Capturar o cargar una imagen |
| Audio | Grabar o cargar un archivo de audio |
| Video | Grabar o cargar un archivo de video |
| Archivo | Adjuntar un archivo (p. ej., .pdf, .docx) |
| Código de barras / Código QR | Escanear códigos de barras y códigos QR usando la cámara del dispositivo |


<p class="note">
<strong>Nota:</strong> KoboToolbox también admite grabaciones de audio de fondo para entrevistas completas o grupos focales. Cuando la grabación de audio de fondo está activa en un formulario, los tipos de pregunta <strong>Audio</strong> <strong>en KoboCollect</strong> se desactivan, ya que no es posible grabar audio usando ambas funciones simultáneamente. Para más información, consulta <a href="../es/recording-interviews.html#recording-interviews-with-background-audio-recordings">Recolectar datos cualitativos con KoboToolbox</a>.
</p>

## Agregar preguntas multimedia con el Formbuilder

Para agregar una pregunta multimedia a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ AGREGAR PREGUNTA.**
4. Elige el tipo de pregunta adecuado.

![Agregar una pregunta multimedia al Formbuilder](images/photo_audio_video_file/media.png)

## Aspectos de las preguntas multimedia

Las preguntas multimedia pueden mostrarse de manera diferente dependiendo de si usas formularios web o KoboCollect. También puedes cambiar el aspecto predeterminado de las preguntas multimedia. Esta sección detalla cómo aparece cada tipo de pregunta en ambas plataformas, incluyendo las opciones de aspecto predeterminadas y avanzadas.

### Aspectos predeterminados

La tabla a continuación muestra cómo se muestran las preguntas multimedia de forma predeterminada en formularios web y KoboCollect.

![Aspectos predeterminados de las preguntas multimedia](images/photo_audio_video_file/table_updated.png)

<p class="note">
<strong>Nota:</strong> Las preguntas de Código de barras / Código QR solo son compatibles con <a href="../es/data_collection_kobocollect.html">KoboCollect</a> en dispositivos móviles. Cuando se escanea un código usando la cámara del dispositivo, el valor codificado en el código de barras o código QR se captura automáticamente. En los <a href="../es/data_through_webforms.html">formularios web</a>, este tipo de pregunta aparece como un campo de texto estándar, donde los encuestados deben ingresar el valor manualmente.
</p>

### Aspectos avanzados

Puedes aplicar aspectos avanzados a las preguntas de **Foto** y **Código de barras / Código QR** para modificar cómo se muestran y se comportan en tu formulario. Los aspectos avanzados para las preguntas de **Foto** permiten a los usuarios hacer más que simplemente cargar o capturar una imagen, incluyendo dibujar bocetos, agregar firmas, anotar imágenes y tomar selfies directamente dentro del formulario.

Para agregar un aspecto avanzado:

1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En **Aspecto (avanzado)**, elige el aspecto deseado.

    - Si el aspecto no aparece en la lista, selecciona **Otro** y escribe el nombre del aspecto en el cuadro de texto, exactamente como se indica arriba.

![Aspectos de preguntas](images/photo_audio_video_file/appearances.png)

Los aspectos disponibles para las preguntas de **Foto** incluyen:

| Aspecto | Descripción |
|:--------|:------------|
| `signature` (firma) | Permite al usuario capturar una firma escribiéndola directamente en la pantalla del dispositivo (p. ej., para formularios que requieren una firma digital para verificación). |
| `draw` (dibujo) | Permite a los usuarios hacer bocetos o dibujos directamente en la pantalla del dispositivo (p. ej., para capturar ilustraciones o mapas dibujados a mano). |
| `annotate` (anotación) | Permite al usuario anotar una imagen dibujando o escribiendo sobre ella. |
| `new` (otro) | Solicita al usuario tomar una nueva foto usando la cámara del dispositivo (solo disponible al usar KoboCollect). |
| `new-front` (otro) | Solicita al usuario tomar una nueva foto usando la cámara frontal del dispositivo (solo disponible al usar KoboCollect). |

Para las preguntas de **Código de barras / Código QR**, solo hay un aspecto avanzado disponible:

| Aspecto | Descripción |
|:--------|:------------|
| `front` | Cambia de la cámara trasera predeterminada del dispositivo a la cámara frontal. |

## Parámetros para preguntas multimedia

Más allá de su función básica, las preguntas multimedia también ofrecen parámetros avanzados que te permiten gestionar el tamaño de los archivos y restringir los tipos de archivos aceptados.

<p class="note">
<strong>Nota:</strong> Cada archivo cargado por un encuestado puede tener un tamaño de hasta 10 MB, con un máximo total de 100 MB por envío.
</p>

### Reducir el tamaño de las imágenes

Si tu proyecto implica recolectar una cantidad significativa de archivos multimedia, es posible que encuentres dificultades para cargar archivos a KoboToolbox, dependiendo de la velocidad de tu conexión a internet. Los usuarios del [Community Plan](https://www.kobotoolbox.org/pricing/) también tienen un límite de 1 GB de almacenamiento de archivos gratuito. Por lo tanto, es recomendable gestionar el tamaño de los archivos multimedia que recolectas.

Para definir el tamaño máximo de las imágenes recolectadas usando el tipo de pregunta **Foto**:

1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. Configura el parámetro **max-pixels** con el valor de tu elección (p. ej., 1000).

![image](images/photo_audio_video_file/parameters.png)

<p class="note">
<strong>Nota:</strong> También puedes configurar la resolución de video y el tamaño de imagen en la <a href="../es/kobocollect_settings.html#form-management-settings">configuración de KoboCollect</a>.
</p>

### Restringir los tipos de archivos aceptados

De forma predeterminada, el tipo de pregunta **Archivo** acepta todos los tipos de archivos. Para restringir el tipo de archivos que acepta esta pregunta:

1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En el cuadro de texto **Archivos aceptados**, enumera las extensiones de archivo que deseas permitir, separadas por una coma (p. ej., .doc, .pdf, .xlsx).

![image](images/photo_audio_video_file/files.png)

## Resolución de problemas

<details>
  <summary><strong>Recolectar múltiples imágenes o archivos multimedia</strong></summary>
  Los tipos de preguntas multimedia solo admiten cargar un archivo a la vez. Para permitir que los usuarios carguen múltiples archivos, puedes colocar la pregunta multimedia dentro de un grupo de repetición, o duplicar la pregunta multimedia en el formulario tantas veces como sea necesario. Puedes usar <a href="../es/skip_logic.html">lógica de omisión</a> para mostrar las preguntas multimedia siguientes solo si la anterior no está en blanco.
</details>

<br>

<details>
  <summary><strong>La grabación de audio en formularios web impide el acceso a otras preguntas</strong></summary>
  Cuando un usuario graba una pregunta de audio en un formulario web, las demás preguntas se bloquean hasta que la grabación esté completa. Esto garantiza que el audio se capture completamente antes de que el usuario continúe con el resto del formulario.
</details>

<br>

<details>
  <summary><strong>Recolectar datos EXIF de imágenes cargadas</strong></summary>
  Cuando se cargan imágenes a través de formularios web o KoboToolbox, los datos EXIF no se conservan de forma predeterminada. Para conservar los datos EXIF, usa un tipo de pregunta <strong>Archivo</strong> y configura el parámetro <strong>Archivos aceptados</strong> (<code>body::accept</code> en XLSForm) como <code>.jpg, .jpeg, .png</code>.
</details>

<br>

<details>
  <summary><strong>Formatos de códigos de barras / códigos QR compatibles</strong></summary>
KoboCollect admite una amplia variedad de formatos de códigos de barras y códigos QR, incluyendo UPC-A, UPC-E, EAN-8, EAN-13, Code 39, Code 93, Code 128, Codabar, ITF, RSS-14, RSS-Expanded, QR Code, Data Matrix, Aztec, PDF 417 y MaxiCode. Si un código de barras no puede escanearse, verifica que use uno de estos formatos compatibles.
</details>