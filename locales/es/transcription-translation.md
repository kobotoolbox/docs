# Transcripción y traducción de respuestas de audio
<a href="../transcription-translation.html">Read in English</a> | <a href="../fr/transcription-translation.html">Lire en français</a> | <a href="../ar/transcription-translation.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/81ea68d620feb190d5829be9521d3f913e88de91/source/transcription-translation.md" class="reference">13 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Las herramientas de procesamiento de lenguaje natural de KoboToolbox te ayudan a recolectar, manejar y analizar datos cualitativos de manera más efectiva. Estas herramientas incluyen transcripción automática de voz a texto y traducción automática, con análisis cualitativo automatizado próximamente disponible. La transcripción original de tus archivos de audio y todo el texto traducido se agregan como nuevas columnas de datos en la tabla de datos y pueden ser [descargados](https://support.kobotoolbox.org/export_download.html) junto con los datos de tu encuesta.

Para usar estas funcionalidades, primero recolecta respuestas de audio en tu formulario usando el [tipo de pregunta de Audio](https://support.kobotoolbox.org/photo_audio_video_file.html) o [grabaciones de audio de fondo](https://support.kobotoolbox.org/recording-interviews.html).


<p class="note">
    <strong>Nota</strong>: La transcripción y traducción automáticas pueden no estar disponibles para <a href="#language-list">todos los idiomas</a>. Para estos idiomas, solo son posibles la transcripción y traducción manuales.
</p>

## Agregar transcripciones automáticas

![Ejemplo de agregar transcripciones automáticas](images/transcription_translation/transcription.png)

Para comenzar a transcribir tus respuestas de audio:

1. Abre tu proyecto y navega a **DATOS > Tabla**.
2. Haz clic en el botón **Abrir** junto a la respuesta de audio que deseas transcribir.
3. En la ventana **TRANSCRIPCIÓN**, haz clic en **comenzar**.
    - Selecciona el idioma original del archivo de audio y la opción **automática** (la opción **manual** te permitirá transcribir manualmente la grabación de audio).
    - Haz clic en **crear transcripción** para comenzar la transcripción automática.
4. Una vez que la transcripción esté completa, puedes editarla manualmente. Puedes reproducir la grabación de audio en la esquina superior derecha para ayudar a verificar la precisión de la transcripción.
    - Después de editar la transcripción, haz clic en el botón **Guardar** para asegurar que tu trabajo se almacene de forma segura.
5. Cuando esté completa, haz clic en **LISTO** para salir, navega a la siguiente presentación haciendo clic en las flechas junto al botón **LISTO**, o procede a la ventana **TRADUCCIONES**.
    - Si haces clic en **LISTO**, regresarás a la vista de tabla de datos, donde se habrá agregado una nueva columna que contiene la transcripción.

<p class="note">
    <strong>Nota</strong>: Las transcripciones y traducciones generadas automáticamente deben guardarse para prevenir la pérdida de datos. Navegar fuera de la página sin guardar resultará en la pérdida de los datos.
</p>

## Agregar traducciones automáticas

![Ejemplo de agregar traducciones automáticas](images/transcription_translation/translation.png)

Una vez que tengas una transcripción completa para tu respuesta de audio, puedes agregar traducciones a múltiples idiomas:

1. Procede a la ventana **TRADUCCIONES**.
    - La opción de traducción solo está disponible una vez que se ha completado una transcripción.
2. Haz clic en **comenzar** y elige el idioma de la traducción.
    - Haz clic en **automática** para traducción automática (la opción **manual** te permitirá traducir manualmente la transcripción)
    - Haz clic en **crear traducción** para comenzar la traducción automática
3. Una vez que la traducción esté completa, puedes editarla manualmente. La transcripción original aparece a la derecha de la pantalla, y el audio original aparece debajo.
    - Después de editar la traducción, haz clic en el botón **Guardar** para asegurar que tu trabajo se almacene de forma segura.
4. Cuando la traducción esté completa, puedes agregar otra traducción haciendo clic en <i class="k-icon-plus"></i> **nueva traducción**, moverte a la siguiente presentación haciendo clic en las flechas junto al número de elemento en la esquina superior derecha, o hacer clic en **LISTO** para navegar de regreso a la tabla de datos.

<p class="note">
    <strong>Nota</strong>: Los archivos de audio solo pueden contener una única transcripción, pero cada transcripción puede tener múltiples traducciones.
</p>

## Lista de idiomas

Estas funcionalidades de procesamiento de lenguaje natural integran capacidades de reconocimiento automático de voz (ASR) y traducción automática (MT) proporcionadas por Google Cloud Compute, que actualmente ofrece transcripción automática en 72 idiomas (con 138 variantes regionales) y traducción automática en 106 idiomas. Para transcripción o traducción manual, puedes seleccionar de aproximadamente 7,000 idiomas basados en la lista completa ISO 639-3, mantenida por SIL International (filtrada para "idiomas vivos"). Si un idioma admite ASR o MT, puedes elegir entre los métodos **manual** y **automático**. Para otros idiomas, solo está disponible el método **manual**.

Si no puedes encontrar un idioma en la lista, considera ortografías o nombres alternativos. Todos los nombres de idiomas están actualmente listados usando sus nombres y ortografía en inglés (por ejemplo, Spanish en lugar de Español). Para idiomas con menos hablantes, puede haber nombres alternativos. Por ejemplo, el idioma Bura del norte de Nigeria está listado como Bura-Pabir pero también se conoce como Bourrah o Babir.

<p class="note">
    <strong>Nota</strong>: Al transcribir manualmente respuestas de audio, es importante seleccionar el idioma correcto. Si la transcripción generada manualmente no coincide con precisión con el idioma o región elegidos, las traducciones automáticas posteriores que usen esa transcripción pueden ser incorrectas y producir inexactitudes.
</p>

## Solución de problemas

<details>
    <summary><strong>La traducción no se carga</strong></summary>
    A veces, la segunda traducción puede quedarse atascada con un ícono de carga. Si esto sucede, actualiza la página y la traducción debería aparecer. Este es un problema en el que estamos trabajando para solucionar.
</details>