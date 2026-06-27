# Recolectar datos cualitativos con KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/recording-interviews.md" class="reference">23 abr 2026</a>

Los datos cualitativos te ayudan a **comprender experiencias, prioridades y contexto** que las preguntas cerradas pueden pasar por alto. Pueden revelar por qué las personas responden de ciertas maneras, cómo describen sus necesidades y qué detalles son más importantes en un contexto local.

En la práctica, los datos cualitativos suelen ser más difíciles de recolectar y analizar a gran escala. Escribir respuestas abiertas, revisar imágenes y transcribir entrevistas de audio puede llevar mucho tiempo. Debido a esto, los equipos a menudo recolectan menos datos cualitativos de los que les gustaría, o tienen dificultades para usar todo lo que recolectan.

KoboToolbox incluye funcionalidades que **hacen que la recolección de datos cualitativos sea más práctica.** Puedes recolectar texto, imágenes, audio, video y grabaciones de audio de fondo en tus formularios, y luego revisarlos y gestionarlos directamente en KoboToolbox. Para respuestas de audio, KoboToolbox también incluye herramientas integradas para [transcripción, traducción](https://support.kobotoolbox.org/es/transcription-translation.html) y [análisis](https://support.kobotoolbox.org/es/qualitative_analysis.html).

Este artículo cubre las principales formas de recolectar datos cualitativos con KoboToolbox, incluidos los tipos de preguntas relevantes, las grabaciones de audio de fondo y las opciones para gestionar y analizar datos cualitativos después de la recolección.

## Tipos de preguntas para la recolección de datos cualitativos

KoboToolbox admite varios tipos de preguntas que son útiles para la investigación cualitativa y la recolección de datos abiertos.

- **Texto:** Las preguntas de texto se pueden usar para respuestas escritas cortas o largas. Para respuestas más largas, puedes usar el [aspecto](https://support.kobotoolbox.org/es/text_questions.html#advanced-appearances) `multiline` (múltiples líneas) para dar a los encuestados un cuadro de texto más grande.
- **Imagen:** Las preguntas de imagen se pueden usar para recolectar fotos, bocetos o imágenes anotadas. Esto puede ser útil para documentación visual, mapeo participativo, observaciones de sitio o recolección de evidencia fotográfica. Usa el [aspecto](https://support.kobotoolbox.org/es/photo_audio_video_file.html#advanced-appearances) `draw` (dibujo) con preguntas de imagen para crear un dibujo, y usa el aspecto `annotate` (anotación) para marcar una imagen.
- **Video:** Las preguntas de video se pueden usar para recolectar archivos de video. Esto puede ser útil cuando el contexto visual, el movimiento o las demostraciones son importantes.
- **Audio:** Las preguntas de audio permiten a los encuestados o encuestadores grabar respuestas habladas o cargar archivos de audio. Son útiles para entrevistas abiertas y otros casos donde el tono y la redacción exacta importan, y reducen la necesidad de que los encuestadores resuman las respuestas en el momento.
- **Grabación de audio de fondo:** La grabación de audio de fondo captura audio continuamente mientras el formulario está abierto. Esto puede ser útil para grabar una entrevista completa en lugar de grabar respuestas separadas pregunta por pregunta.

<p class="note">
Para obtener más información sobre los tipos de preguntas cualitativas, consulta <a href="https://support.kobotoolbox.org/es/text_questions.html">Preguntas de tipo Texto en KoboToolbox</a>, <a href="https://support.kobotoolbox.org/es/photo_audio_video_file.html#">Preguntas Multimedia en KoboToolbox</a> y <a href="https://support.kobotoolbox.org/es/form_meta.html#enabling-background-audio-recording">Habilitar la grabación de audio de fondo</a>.
</p>

## Recolectar datos cualitativos con KoboCollect vs formularios web

Los tipos de preguntas cualitativas pueden comportarse de manera diferente dependiendo de si los datos se recolectan en [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html) o [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html), y de si los encuestados están usando una computadora o un dispositivo móvil.

La siguiente tabla describe cómo se comporta cada tipo de pregunta cualitativa en KoboCollect y en formularios web.

| Tipo de pregunta | Comportamiento en KoboCollect | Comportamiento en formularios web |
|:---|:---|:---|
| Texto | Los encuestados pueden escribir su respuesta en un cuadro de texto. | Los encuestados pueden escribir su respuesta en un cuadro de texto. |
| Imagen | Los encuestados pueden tomar fotos desde el dispositivo o cargar un archivo de imagen. | En una computadora, los encuestados **solo pueden cargar** un archivo de imagen.<br><br>Cuando usan dispositivos móviles, los encuestados también pueden tener la opción de tomar una foto desde el dispositivo. |
| Video | Los encuestados pueden grabar un video desde el dispositivo o cargar un archivo de video. | En una computadora, los encuestados **solo pueden cargar** un archivo de video.<br><br>Cuando usan dispositivos móviles, los encuestados también pueden tener la opción de grabar un video desde el dispositivo. |
| Audio | Los encuestados pueden grabar una respuesta de audio o cargar un archivo de audio. | Los encuestados pueden grabar una respuesta de audio (incluso desde una computadora) o cargar un archivo de audio. |
| Grabación de audio de fondo | Graba continuamente mientras el formulario está abierto, siempre que se haya otorgado permiso para grabar. | Graba continuamente mientras el formulario está abierto (incluso desde una computadora), siempre que se haya otorgado permiso para grabar. |

<p class="note">
<strong>Nota:</strong>
Cuando la grabación de audio de fondo está activa en un formulario, los tipos de pregunta de <strong>Audio</strong> en <strong>KoboCollect</strong> se desactivan, ya que no es posible grabar audio usando ambas funcionalidades simultáneamente.
</p>

## Grabar entrevistas con grabaciones de audio de fondo

La grabación de audio de fondo es útil cuando quieres **capturar una entrevista completa** en lugar de clips de audio separados para preguntas individuales. Comienza cuando se abre el formulario y continúa hasta que se cierra el formulario.

El audio de fondo se puede grabar en la aplicación KoboCollect y en formularios web.

- En formularios web, aparece un aviso al comienzo del formulario para informar a los encuestados que se está grabando audio de fondo.
- Tanto en formularios web como en KoboCollect, aparece un ícono de micrófono en la parte superior del formulario mientras la grabación está activa y muestra la duración de la grabación.

<p class="note">
<strong>Nota:</strong>
La grabación de audio de fondo se recolecta como metadatos del formulario. Para obtener más información sobre cómo configurar grabaciones de audio de fondo en tu formulario, consulta <a href="https://support.kobotoolbox.org/es/form_meta.html#enabling-background-audio-recording">Agregar metadatos en el Formbuilder</a> o <a href="https://support.kobotoolbox.org/es/metadata_xls.html">Metadatos en XLSForm</a>.
</p>

### Consideraciones éticas para la grabación de audio

Antes de grabar audio, **asegúrate de que los encuestados den su consentimiento informado.** Deben entender que se está grabando audio, por qué se está recolectando, cómo se usará, quién tendrá acceso a él y cuánto tiempo se almacenará.

Los datos de audio pueden ser especialmente sensibles. Antes de usar la grabación de audio de fondo, considera si las grabaciones completas de entrevistas son necesarias para tu proyecto y si crean **riesgos adicionales de privacidad o protección.** Kobo recomienda encarecidamente el cumplimiento de todos los requisitos aplicables de protección de datos y privacidad en el lugar donde se realiza la recolección de datos.

## Gestionar y analizar datos cualitativos

KoboToolbox incluye funcionalidades integradas para ayudarte a revisar datos cualitativos después de la recolección.

- **Texto:** Puedes revisar todas las respuestas a una pregunta de texto en **DATOS > Informes.** Esto es útil para leer rápidamente respuestas abiertas juntas e identificar temas comunes.
- **Imágenes:** Puedes revisar las imágenes recolectadas en **DATOS > Galería.** Esto facilita la exploración de respuestas visuales en todos los envíos.
- **Video:** Los archivos de video se pueden ver dentro de envíos individuales. Esto es útil cuando necesitas revisar el contexto visual junto con otras respuestas del mismo envío.
- **Audio:** Las respuestas de audio, incluidas las grabaciones de audio de fondo, se pueden abrir en su propia vista para revisión, transcripción, traducción y análisis.

<p class="note">
Para obtener más información sobre cómo transcribir, traducir y analizar respuestas de audio, consulta <a href="https://support.kobotoolbox.org/es/transcription-translation.html">Transcripción y traducción de respuestas de audio</a> y <a href="https://support.kobotoolbox.org/es/qualitative_analysis.html">Análisis cualitativo de respuestas de audio</a>.
</p>

Los datos cualitativos se incluyen en tu conjunto de datos cuando lo [exportas](https://support.kobotoolbox.org/es/export_download.html), incluidos los enlaces a archivos multimedia para cada envío, cualquier dato de transcripción, traducción y análisis, y cualquier respuesta de texto. Los archivos multimedia también se pueden [descargar por separado](https://support.kobotoolbox.org/es/managing_media_responses.html#downloading-media-files), ya sea individualmente o en masa.

## Solución de problemas

<details>
  <summary><strong>No hay suficiente almacenamiento en el dispositivo</strong></summary>
Antes de recolectar datos cualitativos (por ejemplo, imágenes o grabaciones de audio de fondo), asegúrate de que tu dispositivo tenga suficiente espacio de almacenamiento para guardar los archivos.
</details>

<br>

<details>
  <summary><strong>No hay suficiente almacenamiento en el servidor de KoboToolbox</strong></summary>
Los archivos multimedia pueden ser grandes y pueden hacer que tu cuenta exceda su límite de almacenamiento (1 GB para cuentas gratuitas). Si necesitas más espacio, puedes <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#deleting-media-files">eliminar archivos multimedia</a> de los envíos, <a href="https://www.kobotoolbox.org/pricing/">subir de categoría de plan</a>, o comprar un <strong>complemento de almacenamiento</strong> en <strong>Configuraciones > Complementos.</strong>
</details>

<br>

<details>
  <summary><strong>La grabación de audio de fondo no funciona</strong></summary>
  Tu dispositivo debe tener una grabadora de audio integrada para que esta funcionalidad funcione. Si tu dispositivo no incluye una, puedes descargar <a href="https://play.google.com/store/apps/details?id=com.media.bestrecorder.audiorecorder&pcampaignid=web_share">Voice Recorder</a> o cualquier otra aplicación de grabación de audio en tu dispositivo.
</details>

<br>

<details>
  <summary><strong>Editar envíos con grabación de audio de fondo</strong></summary>
Si editas un formulario que incluye audio de fondo desde la plataforma KoboToolbox, la grabación inicial no será reemplazada. Un mensaje en la parte superior del formulario dirá "Este envío tiene una grabación de audio de fondo."
</details>

<br>

<details>
  <summary><strong>Formularios con grabación de audio de fondo guardados como borradores</strong></summary>
Si un formulario con grabación de audio de fondo se guarda como borrador en <strong>formularios web</strong>, solo se conservará la grabación inicial. La grabación no se reanudará ni será reemplazada cuando se vuelva a abrir el formulario borrador. <br><br>
Si un formulario con grabación de audio de fondo se guarda como borrador en <strong>KoboCollect</strong>, la grabación se reanudará cuando se vuelva a abrir el formulario borrador. Ambas grabaciones se almacenarán juntas en un solo archivo.
</details>

<br>