# Implementar formularios para la recolección de datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/deploy_form_new_project.md" class="reference">23 abr 2026</a>

Antes de poder recolectar datos en KoboToolbox, tu formulario debe estar **implementado**. La implementación hace que el formulario esté activo y disponible para envíos. Puedes **volver a implementar** un formulario cada vez que hagas cambios y desees que esos cambios entren en vigencia.

Este artículo explica cómo implementar y volver a implementar formularios en KoboToolbox, cómo las actualizaciones afectan los formularios web y KoboCollect, qué verificar antes de activar un formulario y qué cambios evitar una vez que la recolección de datos haya comenzado.

<p class="note">
Para obtener más información sobre la recolección de datos con KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/data-collection-tools.html">Recolección de datos con KoboToolbox</a>. 
</p>

## Implementar un formulario para la recolección de datos

Cuando tu formulario esté listo para recibir datos, abre el proyecto y haz clic en **IMPLEMENTAR** en la página **FORMULARIO** para activarlo.

![Implementar un formulario](images/deploy_form_new_project/deploy.png)

Una vez que hayas implementado un formulario, puedes comenzar a [recolectar datos](https://support.kobotoolbox.org/es/data-collection-tools.html) con él.

Después de que un formulario ya ha sido implementado, se te pedirá **VOLVER A IMPLEMENTAR** cada vez que hagas cambios que aún no sean públicos. Aparecerá un banner amarillo que dice "Si deseas publicar estos cambios, debes implementar este formulario".

<p class="note">
<strong>Nota:</strong>
    Siempre vuelve a implementar los formularios después de realizar cambios en los archivos multimedia del formulario, las traducciones o los títulos del formulario, incluso si KoboToolbox no te solicita volver a implementar.
</p>

## Actualizar formularios después de que los cambios se hayan vuelto a implementar

Después de volver a implementar un formulario, los usuarios deberán actualizar o descargar la versión actualizada para ver los cambios.

### Formularios web

Cuando uses **formularios web**, las actualizaciones pueden tardar unos segundos en aparecer. Una vez que la nueva versión esté lista, aparecerá un banner amarillo en la parte superior del formulario que dice: "Se ha descargado una nueva versión de este formulario. Actualiza esta página para cargar la versión actualizada". Actualiza la página para cargar la última versión.

![El banner muestra: Se ha descargado una nueva versión de este formulario. Actualiza esta página para cargar la versión actualizada.](images/deploy_form_new_project/banner.png)

Si alguien ya ha comenzado a ingresar datos, aún puede actualizar. KoboToolbox le pedirá que descarte los datos ya ingresados o que los cargue en la nueva versión del formulario.

![Mensaje de registro no guardado encontrado](images/deploy_form_new_project/unsaved.png)

### KoboCollect

Cuando uses **KoboCollect**, los usuarios deben descargar la última versión del formulario para recibir actualizaciones. Esto requiere una conexión a Internet.

La recuperación de la última versión de un formulario se puede [hacer manualmente](https://support.kobotoolbox.org/es/data_collection_kobocollect.html#downloading-forms) cada vez que el formulario cambie, o se puede configurar para que suceda automáticamente con una frecuencia establecida a través de la [configuración de actualización de formularios](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings) en KoboCollect.

<p class="note">
<strong>Nota:</strong>
    Después de volver a implementar un formulario, asegúrate de que todos los recolectores de datos actualicen a la última versión. De lo contrario, algunos usuarios pueden continuar enviando datos con una versión desactualizada, lo que puede generar errores o inconsistencias en los datos recolectados.
</p>

## Mejores prácticas para implementar y volver a implementar formularios

Se recomiendan los siguientes pasos antes de iniciar la recolección de datos:

1. **Prueba la vista previa del formulario antes de la implementación.** Solo implementa un nuevo formulario, o vuelve a implementar cambios en un formulario existente, después de probarlo exhaustivamente en la vista previa del formulario. Esto ayuda a evitar que los formularios defectuosos se activen.
2. **Prueba el formulario implementado activo.** Después de la implementación, abre el formulario y envía datos de prueba para confirmar que los envíos funcionan correctamente y que los datos aparecen en la tabla de datos según lo previsto.
3. **Si es relevante, prueba el formulario en KoboCollect.** Siempre prueba los mismos métodos de recolección de datos que se utilizarán para la recolección de datos real, ya sean formularios web, KoboCollect o ambos. Esto es especialmente importante para KoboCollect, ya que no se puede probar completamente hasta que el formulario haya sido implementado.
4. **Comparte tu formulario usando el modo Solo lectura para pruebas externas.** Una vez que se haya implementado un formulario, también puedes compartirlo con otros para realizar pruebas utilizando el [modo de formulario web](https://support.kobotoolbox.org/es/data_through_webforms.html#data-collection-modes) **Solo lectura**.

Una vez que hayas probado exhaustivamente tu formulario, puedes comenzar la recolección de datos. Probar exhaustivamente antes del lanzamiento ayuda a reducir la necesidad de realizar cambios después de que la recolección de datos haya comenzado.

### Consideraciones importantes al volver a implementar un formulario

Si realizas cambios en un formulario después de que la recolección de datos ya haya comenzado, esos cambios pueden afectar tanto tu estructura de datos como tu capacidad para revisar o editar envíos anteriores. Debido a esto, es mejor **evitar cambios estructurales importantes** una vez que la recolección de datos en vivo esté en curso, a menos que sean absolutamente necesarios.

Los cambios que pueden afectar tu estructura de datos incluyen:

- **Cambiar el [nombre de columna de datos](https://support.kobotoolbox.org/es/glossary.html#data-column-name) de una pregunta**: KoboToolbox lo tratará como una nueva variable y creará una nueva columna en la tabla de datos.
- **Cambiar un tipo de pregunta manteniendo el mismo nombre de columna de datos**: Esto puede crear datos inconsistentes en la misma columna y generar errores (por ejemplo, en la vista **DATOS > Informes**).
- **Mover preguntas dentro o fuera de grupos**: KoboToolbox tratará estas preguntas como nuevas variables y creará nuevas columnas en la tabla de datos.
- **Eliminar opciones de una lista de opciones**: Los envíos anteriores aún pueden contener esos valores de opción, pero es posible que ya no tengan una etiqueta asociada en el formulario.
- **Agregar nuevas opciones a una pregunta Seleccionar una o Seleccionar varias**: Asegúrate de que cada nueva opción tenga un [valor XML](https://support.kobotoolbox.org/es/glossary.html#xml-value) único dentro de una lista de opciones determinada.
- **Eliminar una pregunta que se usa en otra parte del formulario**: Si la pregunta se hace referencia en un cálculo, condición de relevancia, restricción u otra expresión, también deberás actualizar esas referencias.
- **Cambiar etiquetas de preguntas u opciones**: No afecta la estructura de datos si el nombre de columna de datos o el valor XML permanece igual, pero los datos recolectados previamente usarán la etiqueta actualizada.
- **Cambiar el significado de los valores de opción existentes**: Cambiar los nombres o etiquetas de las opciones puede hacer que los datos sean inconsistentes en las versiones del formulario y generar una mala interpretación. Por ejemplo, esto puede suceder si inviertes el significado de valores como `1 = Sí` y `0 = No`, o cambias la dirección de una escala Likert.

<p class="note">
<strong>Nota:</strong>
    Si tu formulario usa varios idiomas, recuerda también <a href="https://support.kobotoolbox.org/es/language_dashboard.html">actualizar las traducciones</a> cada vez que cambies el formulario. Esto es fácil de pasar por alto después de la reimplementación.
</p>

Los cambios en un formulario también pueden afectar cómo se comportan los envíos anteriores cuando los editas, porque un envío creado con una versión anterior del formulario puede que ya no coincida con la versión actual. Por ejemplo:

- **Agregar nuevas preguntas obligatorias**: Los envíos anteriores pueden requerir nuevas respuestas antes de que puedan enviarse nuevamente.
- **Eliminar preguntas o agregar lógica de omisión**: Los envíos anteriores pueden perder datos recolectados previamente en esas preguntas cuando se editan.
- **Agregar nuevas reglas de validación o restricciones**: Las respuestas anteriores pueden que ya no cumplan con las reglas actualizadas y es posible que no se envíen nuevamente.

## Solución de problemas

<details>
<summary><strong>Error al implementar: Los nombres de las opciones deben ser únicos para cada lista de opciones</strong></summary>
Este error significa que dos o más opciones en la misma lista de opciones tienen el mismo <a href="https://support.kobotoolbox.org/es/glossary.html#xml-value">valor XML (o nombre de opción)</a>.
<br><br>
Si estás usando el <strong>Formbuilder</strong>, verifica los <a href="https://support.kobotoolbox.org/es/question_types.html#setting-xml-values-for-option-choices">valores XML</a> que has establecido manualmente para cada opción para asegurarte de que cada valor XML sea único dentro de una lista de opciones determinada.
<br><br>
Si no puedes identificar qué opción está causando el problema, <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox">descarga el formulario</a> como un <strong>XLSForm</strong> y verifica la hoja <code>choices</code> para encontrar el valor duplicado más fácilmente. El mensaje de error generalmente proporcionará el número de fila en la hoja <code>choices</code> que está causando el error.
</details>

<br>

<details>
<summary><strong>Error al implementar: No se puede encontrar external_file.csv
</strong></summary>
Este error significa que tu formulario hace referencia a un archivo adjunto externo, como un archivo usado con <code>pulldata()</code>, pero ese archivo no se ha cargado al proyecto.
<br><br>
Carga el archivo adjunto faltante a la configuración de <a href="https://support.kobotoolbox.org/es/upload_media.html">archivos multimedia del formulario</a>, luego intenta implementar nuevamente.
</details>

<br>

<details>
<summary><strong>Error al implementar: No se puede encontrar survey.xml</strong></summary>
Este error generalmente significa que los <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">archivos adjuntos de datos dinámicos</a> no se han configurado correctamente en la configuración del proyecto.
<br><br>
Verifica que los archivos adjuntos de datos dinámicos se hayan agregado y configurado correctamente, luego intenta implementar el formulario nuevamente.
</details>

<br>