# Transcripción y traducción de respuestas de audio
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/9d20774e6b199308c43703b5914468dd34bb8c70/source/transcription-translation.md" class="reference">14 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Las herramientas de procesamiento de lenguaje natural de KoboToolbox te ayudan a recolectar, gestionar y analizar datos cualitativos de manera más eficaz. Estas herramientas incluyen la transcripción automática de voz a texto y la traducción automática, que pueden preparar las respuestas de audio para el [análisis cualitativo automatizado](../es/qualitative_analysis.md).

Este artículo explica cómo transcribir respuestas de audio y traducir transcripciones, incluyendo los idiomas compatibles y los límites de uso para las opciones automáticas.

<p class="note">
    <strong>Nota</strong>: Es posible que la transcripción y la traducción automáticas no estén disponibles para <a href="#language-list">todos los idiomas</a>. Para estos idiomas, solo es posible la transcripción y la traducción manual.
</p>

Para usar las funcionalidades de transcripción y traducción de KoboToolbox, comienza por recolectar respuestas de audio en tu formulario usando el [tipo de pregunta Audio](../es/photo_audio_video_file.md) o las [grabaciones de audio de fondo](../es/recording-interviews.md#recording-interviews-with-background-audio-recordings). Después de transcribir y traducir las respuestas de audio, la transcripción original de tus archivos de audio y todo el texto traducido se agregan como nuevas columnas de datos en la tabla de datos y se pueden [descargar](../es/export_download.md) junto con los datos de tu encuesta.


## Agregar transcripciones de audio

![Ejemplo de cómo agregar transcripciones automáticas](images/transcription_translation/transcription.png)

Para comenzar a transcribir tus respuestas de audio:

1. Abre tu proyecto y navega a **DATOS > Tabla**.
2. Haz clic en el botón **Abrir** junto a la respuesta de audio que deseas transcribir.
3. En la ventana **TRANSCRIPT**, haz clic en **begin**.
    - Selecciona el idioma original del archivo de audio.
    - Si está disponible, selecciona la opción **automatic**. La opción **manual** te permitirá transcribir manualmente la grabación de audio en cualquier idioma.
    - Haz clic en **create transcript** para iniciar la transcripción automática.
4. Una vez completada la transcripción, puedes editarla manualmente. Puedes reproducir la grabación de audio en la esquina superior derecha para verificar la precisión de la transcripción.
    - Después de editar la transcripción, haz clic en el botón **Guardar** para asegurarte de que tu trabajo quede almacenado correctamente.
5. Cuando hayas terminado, haz clic en **DONE** para salir, navega al siguiente envío haciendo clic en las flechas junto al botón **DONE**, o continúa a la ventana **TRANSLATIONS**.
    - Si haces clic en **DONE**, volverás a la vista de la tabla de datos, donde se habrá agregado una nueva columna con la transcripción.

<p class="note">
    <strong>Nota</strong>: Las transcripciones y traducciones generadas automáticamente deben guardarse para evitar la pérdida de datos. Si navegas fuera de la página sin guardar, perderás los datos.
</p>

## Agregar traducciones

![Ejemplo de cómo agregar traducciones automáticas](images/transcription_translation/translation.png)

Una vez que tengas una transcripción completa de tu respuesta de audio, puedes agregar traducciones en varios idiomas:

1. Ve a la ventana **TRANSLATIONS**.
    - La opción de traducción solo está disponible una vez que se ha completado una transcripción.
2. Haz clic en **begin** y elige el idioma de la traducción.
    - Si está disponible, selecciona **automatic** para la traducción automática. La opción **manual** te permitirá traducir manualmente la transcripción en cualquier idioma.
    - Haz clic en **create translation** para iniciar la traducción automática.
3. Una vez completada la traducción, puedes editarla manualmente. La transcripción original aparece a la derecha de la pantalla y el audio original aparece debajo.
    - Después de editar la traducción, haz clic en el botón **Guardar** para asegurarte de que tu trabajo quede almacenado correctamente.
4. Cuando la traducción esté completa, puedes agregar otra traducción haciendo clic en <i class="k-icon-plus"></i> **new translation**, moverte al siguiente envío haciendo clic en las flechas junto al número de elemento en la esquina superior derecha, o hacer clic en **DONE** para volver a la tabla de datos.

<p class="note">
    <strong>Nota</strong>: Los archivos de audio solo pueden contener una única transcripción, pero cada transcripción puede tener varias traducciones.
</p>

## Lista de idiomas

Las funcionalidades de procesamiento de lenguaje natural de KoboToolbox integran capacidades de reconocimiento automático de voz (ASR) y traducción automática (MT) proporcionadas por Google Cloud Compute, que actualmente ofrece **transcripción automática en 80 idiomas** (con 145 variantes regionales) y **traducción automática en 129 idiomas**.

Para la transcripción o traducción manual, puedes seleccionar entre aproximadamente 7.000 idiomas basados en la lista exhaustiva ISO 639-3, mantenida por SIL International (filtrada para "idiomas vivos"). Si un idioma es compatible con ASR o MT, puedes elegir entre los métodos **manual** y **automatic**. Para otros idiomas, solo está disponible el método **manual**.

<p class="note">
    Para ver la lista completa de idiomas compatibles, consulta <a href="https://docs.google.com/spreadsheets/d/1_QDcORZd9qXgfq1OBb61U6ondYfjwmHXOv4XZPjxVVw/edit?usp=sharing">Idiomas compatibles con la transcripción y traducción automáticas</a>.
</p>

Si no encuentras un idioma en la lista, considera grafías o nombres alternativos. Actualmente, todos los nombres de idiomas aparecen en inglés (por ejemplo, Spanish en lugar de Español). Para los idiomas con menos hablantes, puede haber nombres alternativos. Por ejemplo, el idioma Bura del norte de Nigeria aparece como Bura-Pabir, pero también se conoce como Bourrah o Babir.

<p class="note">
    <strong>Nota</strong>: Al transcribir manualmente respuestas de audio, es importante seleccionar el idioma correcto. Si la transcripción generada manualmente no coincide con precisión con el idioma o la región elegidos, las traducciones automáticas posteriores que usen esa transcripción pueden ser incorrectas y producir inexactitudes.
</p>

## Límites de uso para la transcripción y traducción automáticas

Los usuarios del Community Plan pueden usar hasta **10 minutos de transcripción automática de voz a texto** por mes y hasta **6.000 caracteres de traducción automática de transcripciones** por mes.

Si necesitas mayor capacidad de transcripción o traducción, puedes [subir de categoría de plan](https://www.kobotoolbox.org/pricing/) a uno con una cuota más alta o [adquirir](../es/account_settings.md#add-ons) un complemento del **Paquete de Procesamiento de Lenguaje Natural (NLP)**. Los complementos están disponibles según tus necesidades de procesamiento de datos, a partir de $9,95 por 100 minutos adicionales de transcripción y 60.000 caracteres adicionales de traducción. Siempre puedes continuar transcribiendo y traduciendo respuestas de audio manualmente sin límite de uso.

## Resolución de problemas

<details>
    <summary><strong>La traducción no carga</strong></summary>
    En ocasiones, la segunda traducción puede quedarse bloqueada con un ícono de carga. Si esto ocurre, actualiza la página y la traducción debería aparecer. Este es un problema en el que estamos trabajando para solucionar.
</details>