# Modificar y eliminar datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/93bd2f1869f8d0d9b512b5ba42f05d5cf68ca56b/source/editing_deleting_data.md" class="reference">6 de mayo de 2026</a>

Modificar y eliminar datos ayuda a **mantener la calidad de los datos** después de recolectar los envíos. Es posible que necesites corregir respuestas individuales, actualizar múltiples registros a la vez, duplicar un envío o eliminar registros que ya no son necesarios. KoboToolbox ofrece varias formas de gestionar estas tareas, entre ellas **editar envíos a través de un formulario web, editar datos sin procesar directamente y aplicar actualizaciones masivas.** Este artículo explica cada método y cuándo utilizarlo.

<p class="note">
<strong>Nota:</strong> Los envíos recolectados con la <a href="https://support.kobotoolbox.org/es/data_collection_kobocollect.html">aplicación Android KoboCollect</a> no pueden editarse ni eliminarse <strong>en KoboCollect</strong> después de ser enviados. Todos los cambios posteriores al envío deben realizarse en KoboToolbox.
</p>

Los propietarios del proyecto pueden controlar el acceso a los datos asignando permisos independientes para ver, editar, validar y eliminar envíos. Por ejemplo, pueden permitir que algunos miembros del equipo editen datos mientras restringen los permisos de eliminación.

<p class="note">
Para obtener más información sobre los permisos a nivel de usuario para editar y eliminar datos, consulta <a href="https://support.kobotoolbox.org/es/managing_permissions.html">Compartir proyectos con permisos a nivel de usuario</a>.
</p>

## Editar envíos individuales

KoboToolbox ofrece dos métodos de edición, cada uno diseñado para diferentes casos de uso. Entender en qué se diferencian te ayuda a elegir el método más seguro y adecuado para actualizar los datos.

Los dos métodos para editar envíos en KoboToolbox son:

- **Editar envíos a través de un formulario web:** Abre el envío como un [formulario web](https://support.kobotoolbox.org/es/glossary.html#enketo-web-forms) para que puedas corregir las respuestas y reenviar el formulario. Este método es recomendable cuando es necesario aplicar la lógica del formulario.
- **Editar datos sin procesar directamente en KoboToolbox:** Abre un editor de datos que te permite modificar respuestas específicas directamente. Este método es recomendable cuando necesitas un control preciso sobre las ediciones y no necesitas que se aplique la lógica del formulario.

Cada método tiene sus ventajas y limitaciones:

![Editing data](images/editing_deleting_data/table.png)

<p class="note">
<strong>Nota:</strong> Al editar datos con cualquiera de los dos métodos, el campo de metadatos <code>_uuid</code> se actualiza cada vez que se guarda un cambio. Al editar a través de un formulario web, el campo <code>end</code> también se actualiza. Todos los demás campos de metadatos permanecen sin cambios, incluidos <code>_id</code>, <code>rootUuid</code>, <code>start</code>, <code>today</code>, <code>_submission_time</code> y <code>_submitted_by</code>.
</p>

### Editar envíos a través de un formulario web

Este método abre un envío como un formulario web para que puedas corregir las respuestas.

Para editar un envío a través de un formulario web:

1. En la fila del envío, junto a la casilla de verificación, haz clic en <i class="k-icon-edit"></i> **Editar.** El envío se abre como un [formulario web](https://support.kobotoolbox.org/es/glossary.html#enketo-web-forms).
2. Realiza los cambios necesarios.
3. Haz clic en **Enviar.**

Todas las actualizaciones, incluidos los campos recalculados y los metadatos actualizados, aparecen en la tabla de datos.

![Resubmit data](images/editing_deleting_data/resubmit.png)

<p class="note">
<strong>Nota:</strong> Dado que este método vuelve a abrir y reenviar el formulario, puede <strong>modificar involuntariamente otros campos</strong>, en particular los afectados por la lógica de omisión o los cálculos. También utiliza la versión más reciente del formulario. Como resultado, es posible que necesites <strong>proporcionar respuestas para preguntas recién añadidas</strong>, y las respuestas a preguntas que han sido eliminadas del formulario <strong>se borrarán.</strong>
</p>

### Editar datos sin procesar en KoboToolbox

Este método te permite omitir la lógica del formulario y editar las respuestas almacenadas directamente sin volver a abrir el formulario. Es útil cuando los cambios no se pueden realizar a través de un formulario web, por ejemplo, si la lógica del formulario impide el reenvío o si preguntas recién marcadas como obligatorias requieren respuestas.

Para editar datos sin procesar en KoboToolbox:

1. Selecciona el envío usando la casilla de verificación.
2. Haz clic en <i class="k-icon-edit"></i> **Editar** encima de la tabla de datos.
3. En la ventana de edición, haz clic en **Editar** junto al campo que deseas cambiar e ingresa el nuevo valor.
    - Para preguntas de tipo selección múltiple, ingresa uno o más [valores XML](https://support.kobotoolbox.org/es/glossary.html#xml-value) válidos, separados por espacios.
4. Haz clic en **Guardar** y luego en **Confirmar y cerrar.**

![Edit your data](images/editing_deleting_data/edit.png)

<p class="note">
<strong>Nota:</strong> Se recomienda registrar las ediciones de datos en un registro externo o en un campo de comentarios dedicado. Las ediciones no se pueden deshacer, pero pueden modificarse nuevamente más adelante.
</p>

## Editar múltiples envíos de forma masiva

Cuando se trabaja con conjuntos de datos grandes, es posible que necesites actualizar múltiples registros al mismo tiempo. La edición masiva ayuda a corregir errores sistemáticos, completar información faltante y estandarizar respuestas en muchos envíos. Este método reduce el trabajo repetitivo y acelera el proceso de limpieza de datos.

Puedes editar múltiples envíos de forma masiva usando el método de edición de datos sin procesar en KoboToolbox:

1. Selecciona los envíos que deseas editar usando las casillas de verificación.
2. Haz clic en <i class="k-icon-edit"></i> **Editar** encima de la tabla. Se abre una ventana que muestra las respuestas de todos los envíos seleccionados.
3. Haz clic en **Editar** junto al campo que deseas actualizar.
4. Ingresa un nuevo valor, o haz clic en **Seleccionar** para aplicar un valor existente a todos los envíos seleccionados.
5. Haz clic en **Guardar** y luego en **Confirmar y cerrar.**

![Bulk edit data](images/editing_deleting_data/bulk_edit.png)

<p class="note">
<strong>Nota:</strong> Puedes seleccionar todos los envíos de la página actual haciendo clic en la casilla de verificación del encabezado de la tabla. Para seleccionar todos los envíos del proyecto en todas las páginas, haz clic en la flecha junto a la casilla de verificación y elige <strong>Seleccionar todos los resultados.</strong>
</p>

## Duplicar envíos

Puedes duplicar un envío siguiendo estos pasos:

1. En la fila del envío, junto a la casilla de verificación, haz clic en <i class="k-icon-view"></i> **Ver.**
2. En la esquina superior derecha de la ventana del envío, haz clic en **Duplicar.**
3. El envío duplicado se abre en una nueva ventana, donde puedes **Editar** o **Descartar** según sea necesario.

![Duplicate submissions](images/editing_deleting_data/duplicate.png)

<p class="note">
<strong>Nota:</strong> Al duplicar un envío, los datos de respuesta se copian, pero el estado de validación se restablece. Los campos de metadatos se actualizan para reflejar el nuevo envío, incluidos <code>start</code>, <code>end</code>, <code>today</code>, <code>_id</code>, <code>_uuid</code>, <code>_submission_time</code> y <code>_submitted_by</code>.
</p>

## Eliminar datos

Eliminar datos borra registros de forma permanente de tu proyecto y debe hacerse con cuidado. Es posible que necesites eliminar envíos para quitar duplicados, limpiar datos de prueba o resolver problemas de calidad de datos. KoboToolbox te permite eliminar envíos individuales o múltiples envíos a la vez.

### Eliminar envíos

1. Selecciona el o los envíos que deseas eliminar.
2. Haz clic en <i class="k-icon-trash"></i> **Eliminar** encima de la tabla de datos.
3. Confirma la eliminación.

Los envíos eliminados se borran de forma permanente y no pueden recuperarse.

![Delete submissions](images/editing_deleting_data/delete.png)

<p class="note">
<strong>Nota:</strong> Puedes usar los <strong>registros del historial de la actividad del proyecto</strong> para <a href="https://support.kobotoolbox.org/es/activity_logs.html">hacer seguimiento a las ediciones y eliminaciones</a> realizadas por los usuarios del proyecto.
</p>

### Eliminar la respuesta de un campo específico

En algunos casos, es posible que desees eliminar las respuestas de un solo campo sin eliminar el envío completo. Esto puede ser útil para la anonimización de datos, por ejemplo, cuando se elimina información de identificación personal después de haberla almacenado de forma segura.

No existe una opción dedicada para eliminar el valor de un solo campo. En su lugar, puedes borrar o reemplazar el valor siguiendo este método:

1. Selecciona el o los envíos que deseas actualizar.
2. Haz clic en <i class="k-icon-edit"></i> **Editar** encima de la tabla de datos.
3. Haz clic en **Editar** junto al campo que deseas borrar, luego ingresa un espacio o un valor de reemplazo como "deleted" o "N/A".
4. Haz clic en **Guardar** y luego en **Confirmar y cerrar.**

<p class="note">
<strong>Nota:</strong> Puedes eliminar <strong>archivos multimedia adjuntos</strong> de tus datos, ya sea de forma individual o masiva. Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/managing_media_responses.html#deleting-media-files">Gestionar respuestas con archivos multimedia</a>.
</p>

## Resolución de problemas

<details>
  <summary><strong>La edición a través de un formulario web modifica o elimina datos</strong></summary>
  Cuando vuelves a abrir formularios complejos como formulario web, los campos afectados por la lógica de omisión, los cálculos o las conexiones dinámicas de proyectos pueden cambiar. Estos comportamientos pueden impedir que el formulario se reenvíe o eliminar datos que ya no cumplen las condiciones de la lógica. Si no puedes reenviar el formulario, puedes salir del formulario web y no se guardarán los cambios. Para evitar estos efectos, edita los datos sin procesar directamente.
</details>

<br>

<details>
  <summary><strong>Editar a través de un formulario web después de añadir nuevas preguntas</strong></summary>
  Si editas un envío antiguo a través de un formulario web después de actualizar y volver a implementar el formulario, el envío se abre en la versión más reciente del formulario. Esto puede causar problemas cuando se han añadido nuevas preguntas obligatorias, ya que debes proporcionar respuestas válidas a esas preguntas para poder guardar las ediciones del envío original.
</details>

<br>

<details>
  <summary><strong>Los datos editados no aparecen en las exportaciones</strong></summary>
  Si editas un envío y añades datos a una pregunta que solo existe en una versión más reciente del formulario, es posible que esos datos no aparezcan en las exportaciones cuando se selecciona <strong>Incluye campos de las versiones</strong> en la <a href="https://support.kobotoolbox.org/es/advanced_export.html#selecting-data-fields-for-export">configuración de exportación</a>.
<br><br>
Para resolver esto, desmarca <strong>Incluye campos de las versiones</strong> en la configuración de exportación. Los datos añadidos a preguntas de versiones más recientes del formulario se incluirán entonces en la exportación.
</details>

<br>

<details>
  <summary><strong>Las geoformas con autointersección bloquean las ediciones en los formularios web</strong></summary>
  KoboCollect puede registrar geoformas con autointersección cuando las coordenadas GPS fluctúan mientras el recolector de datos está quieto. Estos polígonos pueden enviarse correctamente desde KoboCollect, pero volver a abrir el mismo envío a través de un formulario web puede generar un error de geometría. Los formularios web no permiten guardar el formulario hasta que se corrija el polígono, lo que puede ser difícil de corregir manualmente.
    <br><br>
En esta situación, usa la edición de datos sin procesar en KoboToolbox para actualizar los campos necesarios sin volver a abrir el envío a través de un formulario web. Esto evita el error de validación de geometría.
</details>

<br>

<details>
  <summary><strong>Las ediciones de coordenadas no se guardan si no se usa el formato requerido</strong></summary>
  Al editar coordenadas usando el método de edición de datos sin procesar, los valores deben seguir el formato exacto de KoboToolbox: <code>latitud longitud altitud precisión</code>. Por ejemplo, las coordenadas de París serían <code>48.8566 2.3522 0 0</code>. <br><br>
Si falta alguna parte o el formato es incorrecto, es posible que la edición no se guarde o cause problemas durante la exportación. Asegúrate de que los cuatro valores estén incluidos y separados por espacios antes de guardar.
</details>

<br>

<details>
  <summary><strong>Los formularios que usan conexiones dinámicas de proyectos para evitar envíos duplicados no pueden editarse a través de un formulario web</strong></summary>
  Si tu formulario usa conexiones dinámicas de proyectos para <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html#dynamically-linking-a-form-to-itself">evitar envíos duplicados</a>, volver a abrir un envío a través de un formulario web bloqueará el reenvío porque se detecta como duplicado. En este caso, usa la edición de datos sin procesar en KoboToolbox en lugar de editar a través de un formulario web.
</details>

<br>

<details>
  <summary><strong>Verificar si un envío ha sido editado</strong></summary>
  Para verificar si un envío ha sido editado, generalmente puedes comparar el campo <code>_uuid</code> con el campo <code>rootUuid</code> en la tabla de datos o en los datos exportados. El valor de <code>rootUuid</code> permanece igual para el envío original, mientras que el valor de <code>_uuid</code> cambia cada vez que se edita el envío. Si los valores son diferentes, es probable que el envío haya sido editado.
</details>

<br>