# Transcripción y traducción de respuestas de audio
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/eaaa0a122cb15511b64a66babaa5dad10f6aa7a9/source/transcription-translation.md" class="reference">6 oct 2026</a>


<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Las herramientas de procesamiento del lenguaje natural de KoboToolbox te ayudan a recolectar, manejar y analizar datos cualitativos de manera más eficaz. Estas herramientas incluyen la transcripción automática de voz a texto y la traducción automática, que pueden preparar las respuestas de audio para el [análisis cualitativo automatizado](https://support.kobotoolbox.org/qualitative_analysis.html).

Puedes transcribir y traducir respuestas individuales o procesar varios envíos de forma masiva desde la tabla de datos. Este artículo explica cómo transcribir respuestas de audio y traducir transcripciones de forma individual o masiva, e incluye los idiomas compatibles y los límites de uso de las opciones automáticas.

<p class="note">
    <strong>Nota</strong>: Es posible que la transcripción y la traducción automáticas no estén disponibles para <a href="#supported-languages-for-transcription-and-translation">todos los idiomas</a>. Para esos idiomas, solo es posible la transcripción y la traducción manuales.
</p>

## Recolectar respuestas de audio
Antes de transcribir o traducir respuestas de audio, debes recolectar datos de audio en tu proyecto.

1. Agrega una [pregunta de tipo Audio](https://support.kobotoolbox.org/photo_audio_video_file.html) a tu formulario o activa las [grabaciones de sonido de fondo](https://support.kobotoolbox.org/qualitative_data.html#recording-interviews-with-background-audio-recordings).
2. Implementa el formulario y recolecta envíos que contengan grabaciones de audio.

<p class="note">
    <strong>Nota</strong>: Para algunos idiomas compatibles, es posible que la transcripción automática no funcione con archivos de audio de más de 50 minutos. Para entrevistas largas, considera usar varias preguntas de tipo Audio individuales en lugar de una sola grabación de sonido de fondo.
</p>

Después de transcribir y traducir las respuestas de audio, la transcripción original de tus archivos de audio y todos los textos traducidos se agregan como nuevas columnas de datos en la tabla de datos y se pueden [descargar](https://support.kobotoolbox.org/export_download.html) junto con los datos de tu encuesta.


## Transcribir archivos de audio de forma individual

![Adding automatic transcriptions example](images/transcription_translation/transcription.png)

Para comenzar a transcribir respuestas de audio de forma individual:

1. Abre tu proyecto y ve a **DATOS > Tabla**.
2. Haz clic en el botón <i class="ti-outline ti-pencil-star"></i> **Abrir** junto a la respuesta de audio que deseas transcribir.
3. En la pestaña **TRANSCRIPCIÓN**, haz clic en **comenzar**.
    - Selecciona el idioma original del archivo de audio.
    - Si está disponible, selecciona la opción **automática**. La opción **manual** te permitirá transcribir manualmente la grabación de audio en cualquier idioma.
    - Haz clic en **crear transcripción** para iniciar la transcripción automática.
4. Una vez completada la transcripción, puedes editarla manualmente. Puedes reproducir la grabación de audio en la esquina superior derecha para ayudarte a verificar la exactitud de la transcripción.
    - Después de editar la transcripción, haz clic en el botón **Guardar** para asegurarte de que tu trabajo quede almacenado de forma segura.
5. Cuando termines, haz clic en **REALIZADO** para salir, pasa al siguiente envío con las flechas junto al botón **REALIZADO**, o continúa a la pestaña **TRADUCCIONES**.
    - Si haces clic en **REALIZADO**, volverás a la vista de la tabla de datos, donde se habrá agregado una nueva columna con la transcripción.

<p class="note">
    <strong>Nota</strong>: Las transcripciones y traducciones generadas automáticamente deben guardarse para evitar la pérdida de datos. Si sales de la página sin guardar, es posible que pierdas los datos.
</p>

## Transcribir archivos de audio de forma masiva

Puedes transcribir automáticamente las grabaciones de audio de varios envíos a la vez desde la tabla de datos.

Para transcribir respuestas de audio de forma masiva:

1. Abre tu proyecto y ve a **DATOS > Tabla.**
2. Selecciona los envíos que deseas transcribir con las casillas de la izquierda.
3. En la columna que contiene las grabaciones de audio que deseas transcribir, haz clic en la flecha del encabezado de la columna.
4. Haz clic en **Transcribir archivos de audio seleccionados.**
5. Selecciona el idioma y la región, y luego haz clic en **Iniciar transcripción.**

![Bulk transcribe audio files](images/transcription_translation/bulk_transcribe_files.png)

Las transcripciones completadas se agregan a una nueva columna en la tabla de datos y se marcan como listas para su revisión.

### Revisar y aprobar transcripciones

Revisar las transcripciones automáticas para confirmar que reflejan con exactitud las grabaciones de audio ayuda a garantizar que los datos sean confiables y estén listos para el análisis o la traducción.

Para revisar y aprobar una transcripción individual:

1. Haz clic en **Revisar.**
2. Realiza las ediciones necesarias.
3. Guarda la transcripción y pasa a la siguiente.

Para aprobar varias transcripciones a la vez:

1. Selecciona los envíos correspondientes con las casillas de la izquierda.
2. En la columna de transcripción, haz clic en la flecha del encabezado de la columna.
3. Haz clic en **Aprobar todos los seleccionados.**

![Bulk approve transcriptions](images/transcription_translation/bulk_approve_transcripts.png)

## Traducir transcripciones de forma individual

![Adding automatic translations example](images/transcription_translation/translation.png)

Una vez que tengas una transcripción completa de tu respuesta de audio, puedes agregar traducciones a varios idiomas:

1. Desde la pestaña **TRANSCRIPCIÓN**, ve a la pestaña **TRADUCCIONES**.
    - La opción de traducción solo está disponible una vez que se ha completado una transcripción.
2. Haz clic en **comenzar** y elige el idioma de la traducción.
    - Si está disponible, selecciona **automática** para la traducción automática. La opción **manual** te permitirá traducir manualmente la transcripción a cualquier idioma.
    - Haz clic en **crear traducción** para iniciar la traducción automática.
3. Una vez completada la traducción, puedes editarla manualmente. La transcripción original aparece en la parte derecha de la pantalla y el audio original aparece debajo.
    - Después de editar la traducción, haz clic en el botón **Guardar** para asegurarte de que tu trabajo quede almacenado de forma segura.
4. Cuando la traducción esté completa, puedes agregar otra traducción haciendo clic en <i class="k-icon-plus"></i> **nueva traducción**, pasar al siguiente envío con las flechas junto al número del elemento en la esquina superior derecha, o hacer clic en **REALIZADO** para volver a la tabla de datos.

<p class="note">
    <strong>Nota</strong>: Los archivos de audio solo pueden tener una transcripción, pero cada transcripción puede tener varias traducciones.
</p>

## Traducir transcripciones de forma masiva

También puedes traducir automáticamente varias transcripciones a la vez desde la tabla de datos.

Para traducir transcripciones de forma masiva:

1. Asegúrate de que tu proyecto contenga transcripciones de audio completas.
2. Abre tu proyecto y ve a **DATOS > Tabla.**
3. Selecciona los envíos que contienen las transcripciones que deseas traducir con las casillas de la izquierda.
4. En la columna de transcripción que deseas traducir, haz clic en la flecha del encabezado de la columna.
5. Haz clic en **Traducir transcripciones seleccionadas.**
6. Busca y selecciona el idioma de destino, y luego haz clic en **Crear traducciones.**

![Bulk translate transcriptions](images/transcription_translation/bulk_translate_transcriptions.png)

Las traducciones completadas se agregan a una nueva columna en la tabla de datos y se marcan como listas para su revisión.

### Revisar y aprobar traducciones

Para revisar y aprobar una traducción individual:

1. Haz clic en **Revisar.**
2. Realiza las ediciones necesarias.
3. Guarda la traducción y pasa a la siguiente.

Para aprobar varias traducciones a la vez:

1. Selecciona los envíos correspondientes con las casillas de la izquierda.
2. En la columna de traducción, haz clic en la flecha del encabezado de la columna.
3. Haz clic en **Aprobar todos los seleccionados.**


## Idiomas compatibles con la transcripción y la traducción

Las funciones de procesamiento del lenguaje natural de KoboToolbox integran capacidades de reconocimiento automático de voz (ASR) y traducción automática (MT) proporcionadas por Google Cloud Compute, que actualmente ofrece **transcripción automática en 112 idiomas** (con 142 variantes regionales) y **traducción automática en 129 idiomas**.

<p class="note">
<strong>Nota:</strong> Los archivos de audio y las transcripciones solo se envían a Google Cloud Compute durante el tiempo necesario para completar la transcripción y la traducción. El servicio externo no los almacena después del procesamiento ni los utiliza para mejorar el servicio.
</p>

Para la transcripción o la traducción manual, puedes elegir entre aproximadamente 7000 idiomas de la lista completa ISO 639-3, mantenida por SIL International (filtrada para "idiomas vivos"). Si un idioma admite ASR o MT, puedes elegir entre los métodos **manual** y **automático**. Para los demás idiomas, solo está disponible el método **manual**.

<p class="note">
    Para ver la lista completa de idiomas compatibles, consulta <a href="https://docs.google.com/spreadsheets/d/1_QDcORZd9qXgfq1OBb61U6ondYfjwmHXOv4XZPjxVVw/edit?usp=sharing">Languages supported for automatic transcription and translation</a>.
</p>

Si no encuentras un idioma en la lista, prueba con grafías o nombres alternativos. Actualmente, todos los nombres de idiomas aparecen con su nombre y ortografía en inglés (por ejemplo, Spanish en lugar de Español). Para los idiomas con menos hablantes, puede haber nombres alternativos. Por ejemplo, el idioma bura en el norte de Nigeria aparece como Bura-Pabir, pero también se conoce como Bourrah o Babir.

<p class="note">
    <strong>Nota</strong>: Al transcribir manualmente respuestas de audio, es importante seleccionar el idioma correcto. Si la transcripción generada manualmente no coincide con precisión con el idioma o la región elegidos, las traducciones automáticas posteriores que usen esa transcripción pueden ser incorrectas y contener imprecisiones.
</p>

## Límites de uso de la transcripción y la traducción automáticas
Los usuarios del Community Plan (Plan Comunitario) pueden usar hasta **10 minutos de transcripción automática de voz a texto** al mes y hasta **6000 caracteres de traducción automática de transcripciones** al mes.

<p class="note">
<strong>Nota:</strong> El procesamiento automático cuenta para estos límites independientemente de si los archivos se procesan de forma individual o masiva.
</p>

Si necesitas más capacidad de transcripción o traducción, puedes [subir de categoría de plan](https://www.kobotoolbox.org/pricing/) a uno con una cuota mayor o [comprar](https://support.kobotoolbox.org/account_settings.html#add-ons) el complemento **Paquete NLP** (Natural Language Processing). Los complementos están disponibles según tus necesidades de procesamiento de datos, desde $9.95 por 100 minutos adicionales de transcripción y 60 000 caracteres adicionales de traducción. Siempre puedes seguir transcribiendo y traduciendo respuestas de audio manualmente sin límite de uso.


## Resolución de problemas

<details>
    <summary><strong>La traducción no se carga</strong></summary>
    A veces, la segunda traducción puede quedarse bloqueada con un ícono de carga. Si esto sucede, actualiza la página y la traducción debería aparecer. Estamos trabajando para solucionar este problema.
</details>

<br>

<details>
<summary><strong>Los archivos de audio largos no se transcriben</strong></summary>
Para algunos idiomas compatibles, es posible que la transcripción automática no funcione con archivos de audio de más de 50 minutos.<br><br>
Para entrevistas largas, considera usar varias preguntas de tipo Audio individuales en lugar de una sola grabación de sonido de fondo. Dividir una entrevista en grabaciones más cortas puede facilitar la carga y el manejo de los archivos, y hace más sencillo ubicar y transcribir secciones específicas de la entrevista.<br><br>
Si ya tienes una grabación larga, también puedes descargar el archivo de audio, dividirlo en archivos más cortos y volver a cargarlos en KoboToolbox para su transcripción.
</details>