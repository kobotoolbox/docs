# Grabar una Entrevista Completa con la Grabación de Audio de Fondo
<a href="../recording-interviews.html">Read in English</a> | <a href="../fr/recording-interviews.html">Lire en français</a> | <a href="../ar/recording-interviews.html">اقرأ باللغة العربية</a>

**Última actualización:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/recording-interviews.md" class="reference">15
Feb 2022</a>

**La grabación de audio de fondo** es una funcionalidad poderosa que permite a los/as usuarios/as grabar
una entrevista en segundo plano (cuando el formulario está abierto) y almacenar la grabación
como datos de audio. Esta funcionalidad mejora la recolección de datos cualitativos al permitir que
la información matizada se recolecte en su totalidad.

La grabación de audio de fondo también permite a los/as supervisores/as y gerentes/as de proyecto
saber cómo sus encuestadores/as realizaron la entrevista en términos de aseguramiento de calidad
de datos o si desean tener una grabación de respaldo de la entrevista transcrita.

Actualmente, los/as usuarios/as pueden grabar la entrevista completa con **La aplicación de Android de KoboCollect**
`v1.30` y superior. **Enketo** aún no soporta esta funcionalidad.

<p class="note">
  Si requieres una grabación de audio en lugar de la completa
  <strong>grabación de audio de fondo</strong>, consulta nuestro artículo de ayuda,
  <a class="reference" href="media.html"
    >Agregar Varios Tipos de Medios (imagen, audio, video) a un Formulario</a
  >.
</p>

## Activar la grabación de audio de fondo en el editor de formularios

Si estás diseñando tu formulario de encuesta a través del editor de formularios de KoboToolbox (Formbuilder) y deseas habilitar
la **grabación de audio de fondo**, sigue los pasos que se muestran en el video a continuación:

<video controls>
  <source
    src="./_static/files/recording_interviews/activating_background_audio_recording_UI.mp4"
    type="video/mp4"
  />
</video>

-   En la ventana **FORMULARIO**, selecciona el botón **Editar**. _(Este paso puede no ser
    necesario si ya estás en el editor de formularios)_
-   En la esquina superior derecha, selecciona **Diseño y Ajustes** y luego **Audio de
    fondo** debería ser visible.
-   Activa el botón **Habilitar grabación de audio en segundo plano**. Una
    notificación debería aparecer en la parte superior del editor de formularios.
-   **Solo voz** es la calidad de audio predeterminada para el **audio de fondo**.
    Puedes cambiar la calidad de audio a **Baja** o **Normal** según sea necesario (consulta
    la tabla a continuación para ver las diferencias en el tamaño del archivo).
-   Después de realizar todas las configuraciones necesarias, selecciona **GUARDAR** y **Salir**
    en el editor de formularios.
-   **DESPLEGAR** el formulario para ponerlo en funcionamiento.

## Incluir el tipo de pregunta de audio de fondo en XLSForm

Si estás diseñando tu formulario de encuesta a través de XLSForm y deseas incluir un
tipo de pregunta `background-audio`, sigue los pasos que se muestran en el video a continuación:

<video controls>
  <source
    src="./_static/files/recording_interviews/including_background_audio_question_type_xlsform.mp4"
    type="video/mp4"
  />
</video>

En tu XLSForm, agrega `background-audio` bajo la columna `type` de la
hoja **survey**. Este es el tipo de pregunta que grabará el audio en
segundo plano.

## Establecer una calidad de audio apropiada

La columna `parameters` es opcional pero es importante elegir el
parámetro apropiado. La calidad de audio está directamente relacionada con el tamaño del archivo que
se almacenará en el servidor. Ten en cuenta cuánto de tu espacio de almacenamiento total
deseas usar para tus archivos de audio. Consulta la tabla a continuación al elegir
el parámetro apropiado:

| Calidad    | Parámetros         | Extensión | Codificación | Tasa de bits | Tasa de muestreo | Tamaño del archivo |
| :--------- | :----------------- | :-------- | :----------- | :----------- | :--------------- | :----------------- |
| normal     | quality=normal     | .m4a      | AAC          | 64 kbps      | 32 kHz           | ~ 30 MB/hora       |
| low        | quality=low        | .m4a      | AAC          | 24 kbps      | 32 kHz           | ~ 11 MB/hora       |
| voice-only | quality=voice-only | .amr      | AMR          | 12.2 kbps    | 8 kHz            | ~ 5 MB/hora        |

Puedes dejar la columna en blanco para que el parámetro se establezca en `voice-only`, que
capturará el audio bien en un entorno de entrevista silencioso. Si estás grabando audio
donde podría haber múltiples personas hablando simultáneamente, `low` sería más
adecuado. `normal` es la opción de mayor calidad y usará la mayor cantidad
de espacio de almacenamiento.

## Recolectar audio de fondo con la aplicación de Android de KoboCollect

Revisa nuestro artículo de ayuda,
[Recolección de Datos en la Aplicación de KoboCollect](kobocollect_on_android_latest.md), para aprender
en detalle sobre la recolección de datos en **La aplicación de Android de KoboCollect**.

<video controls>
  <source
    src="./_static/files/recording_interviews/collecting_data_with_background_audio_in_collect_app.mp4"
    type="video/mp4"
  />
</video>

Mientras grabas activamente audio de fondo con **La aplicación de Android de KoboCollect**, deberías
poder ver un micrófono en la parte superior de tu formulario.

![Pantalla de audio de fondo](/images/recording_interviews/background_audio_screen.jpg)

## Ver archivos de audio que fueron grabados como audio de fondo

Cuando tienes `background-audio` configurado para tu proyecto, puedes ver el
archivo de audio grabado en **DATOS>Tabla** como se muestra en la imagen a continuación.

![Vista de tabla de datos](/images/recording_interviews/data_table_view.png)

## Descargar archivos de audio

Puedes descargar todos los archivos de audio de fondo como un archivo ZIP desde
**DATOS>Descargas>Archivos Adjuntos Multimedia (ZIP)** como se muestra en el video a continuación.

<video controls>
  <source
    src="./_static/files/recording_interviews/downloading_audio_files_that_were_recorded_as_background_audio.mp4"
    type="video/mp4"
  />
</video>

## Consideraciones éticas

Al recolectar datos, es ético tener el consentimiento informado de los/as
encuestados/as antes de la recolección de datos, en este caso grabando audio de
fondo.

<p class="note">
  Alentamos a todos/as los/as usuarios/as a considerar las implicaciones éticas de su recolección
  de datos y a cumplir con la legislación aplicable de protección de datos dentro
  de la jurisdicción de su trabajo.
</p>

## Solución de problemas

-   Esta funcionalidad es compatible con **La aplicación de Android de KoboCollect** `v1.30` y
    superior.
-   Esta funcionalidad actualmente no es compatible con los **formularios web de Enketo**.
-   Tu dispositivo debe tener una grabadora de audio incorporada para que esta funcionalidad funcione
    sin problemas. Puedes descargar
    [Audio Recorder](https://play.google.com/store/apps/details?id=com.github.axet.audiorecorder)
    desde Google Play Store si es necesario.
-   Antes de comenzar la recolección de datos, asegúrate de que tu dispositivo tenga suficiente
    espacio para almacenar las grabaciones de audio de fondo.
-   Si editas tu archivo de audio en **Editar Formulario Guardado**, tendrás ambas
    versiones (el archivo de audio original y el archivo editado) en un solo archivo.
    Por ejemplo, si tienes un audio de fondo de _'Prueba de muestra'_ y editaste
    la grabación, cambiándola a _'Muestra para re-prueba'_, cuando
    descargues tu archivo de audio de fondo, consistirá del audio de fondo combinado
    de _'Prueba de muestra'_ y _'Muestra para re-prueba'_.
-   Si tus archivos de audio de fondo ocupan suficiente espacio de almacenamiento para llevar tu
    almacenamiento total por encima de tu cantidad asignada (5GB para todas las cuentas gratuitas), puedes
    solicitar espacio adicional (por un costo) contactando a
    [info@kobotoolbox.org](mailto:info@kobotoolbox.org). El pago se utiliza para
    cubrir los costos adicionales asociados con proyectos de recolección de datos grandes
    y asegura que el servidor siga funcionando bien para nuestros/as usuarios/as.
-   Cuando tienes archivos de audio de fondo grandes y/o largos en tu cuenta, puedes
    tener problemas al descargarlos como **Archivos Adjuntos Multimedia (ZIP)**. En tal
    caso, sigue nuestro artículo de ayuda
    [Descargar Fotos y Otros Medios](photo_download.md), que debería ayudarte
    a descargar archivos multimedia grandes del sistema.