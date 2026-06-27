# Ver y validar datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/54acbc6a5e616ccc3a13d7a6fcb1c3f2f29d9243/source/viewing_validating_data.md" class="reference">5 Jun 2026</a>

<iframe src="https://www.youtube.com/embed/X5W6nv9gYUo?si=n3eniC0Uq_PzFsbT&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La vista **Tabla** en la sección **DATOS** de tu proyecto KoboToolbox ofrece una descripción general completa y personalizable de todos los envíos del proyecto. De forma predeterminada, se muestran todos los registros, con los envíos más recientes primero. Esta vista es el espacio de trabajo principal para explorar datos, supervisar la calidad de los datos, validar envíos y realizar ediciones.

Este artículo explica cómo:

- Configurar la tabla de datos en la vista **Tabla**
- Filtrar y ordenar tus datos
- Ver y validar envíos

<p class="note">
Para obtener más información sobre cómo realizar cambios en tus datos, consulta <a href="https://support.kobotoolbox.org/es/editing_deleting_data.html">Modificar y eliminar datos</a>.
</p>

Los propietarios del proyecto pueden controlar el acceso a los datos asignando permisos independientes para ver, editar, validar y eliminar envíos. Por ejemplo, pueden permitir que algunos miembros del equipo vean y validen datos mientras restringen los permisos de edición y eliminación.

<p class="note">
Para obtener más información sobre los permisos a nivel de usuario para ver, validar y editar datos, consulta <a href="https://support.kobotoolbox.org/es/managing_permissions.html">Compartir proyectos con permisos a nivel de usuario/a</a>.
</p>

## Configurar la tabla de datos

La tabla de datos en la vista **Tabla** muestra todos los envíos y campos de datos de forma predeterminada. En muchos proyectos, se necesita una vista más enfocada. Ajustar lo que aparece en la tabla te ayuda a trabajar de manera más eficiente, especialmente en formularios con muchas preguntas o grupos anidados. Puedes elegir qué campos mostrar y cómo se presentan los datos para adaptarlos mejor a tu flujo de trabajo.

![Elegir campos para mostrar en la tabla de datos](images/viewing_validating_data/table_view.png)

### Personalizar la tabla de datos

Encima de la tabla de datos, puedes configurar los siguientes ajustes:

- **Ocultar campos:** Haz clic en <i class="k-icon-qt-hidden"></i> **ocultar campos** para ver una lista de todas las preguntas y campos de tu formulario. Todos los campos están seleccionados de forma predeterminada. Desmarca la casilla de cualquier campo que quieras ocultar y luego haz clic en **Aplicar** para guardar los cambios.
- **Alternar pantalla completa:** Haz clic en <i class="k-icon-expand"></i> **Alternar pantalla completa** para expandir la tabla de datos y que ocupe toda la ventana del navegador.
- **Opciones de visualización:** Haz clic en <i class="k-icon-settings"></i> **Opciones de visualización** para controlar cómo se muestran las etiquetas, los grupos y las etiquetas HXL en la tabla. Se pueden configurar las siguientes opciones de visualización:

| Opción de visualización | Descripción |
|:-------------------------------|:---------------------------------------------------------------------------------------------|
| ¿Mostrar etiquetas o valores XML? | Elige si mostrar <a href="https://support.kobotoolbox.org/es/glossary.html#xml-value">valores XML</a> o las etiquetas completas de preguntas y opciones en <a href="https://support.kobotoolbox.org/es/collecting_data_multiple_languages.html">cualquier idioma del formulario</a> en tu tabla. |
| Mostrar nombres de grupo en los encabezados de tabla | Decide si los encabezados de columna de la tabla incluyen el nombre del grupo de preguntas (por ejemplo, `demographics / age`). |
| Mostrar etiquetas HXL | Muestra las etiquetas del <a href="https://support.kobotoolbox.org/es/question_options.html#hxl">Lenguaje de Intercambio Humanitario</a> (HXL) si se agregaron a tu formulario. |

Dentro de la tabla de datos, puedes hacer clic en el encabezado de una columna y seleccionar <i class="k-icon-qt-hidden"></i> **Ocultar campo** para eliminar los campos que no necesitas, o <i class="k-icon-freeze"></i> **Inmovilizar campo** para mantener visible un campo de uso frecuente mientras te desplazas.

<p class="note">
<strong>Nota:</strong> Estas configuraciones afectan a la vista <strong>Tabla</strong> para todos los usuarios del proyecto.
</p>

### Navegar por la tabla de datos

Puedes cambiar cuántas filas se muestran por página usando la lista desplegable en la parte inferior de la tabla. De forma predeterminada, la tabla muestra 30 filas.

<p class="note">
<strong>Nota:</strong> Mostrar muchas filas a la vez puede ralentizar tu navegador.
</p>

Usa las flechas <i class="k-icon-caret-left"></i> **PREV** y **NEXT** <i class="k-icon-caret-right"></i>, o ingresa un número de página, para moverte por la tabla de datos.

### Campos de envío generados por el sistema

Cada envío en la tabla de datos incluye campos generados por el sistema que ayudan a identificar registros y rastrear los detalles del envío. Estos campos aparecen como columnas separadas al final de la tabla y no se pueden editar.

| Campo | Descripción |
|:---|:---|
| `__version__` | Un identificador único para la versión del formulario utilizada en el envío. Esto es útil si tu formulario cambió con el tiempo y necesitas saber qué versión recopiló los datos. |
| <code>_id</code> | Un número de ID generado por el servidor para el envío. Se asigna después de que el envío llega a KoboToolbox y es único en ese servidor de KoboToolbox. |
| <code>_uuid</code> | Un identificador generado automáticamente para el envío. Puede ayudar a identificar un registro, pero puede cambiar si el envío se edita, por lo que no es el campo más confiable para el seguimiento a largo plazo. |
| <code>_submission_time</code> | La fecha y hora en que el servidor de KoboToolbox recibió el envío. En las exportaciones, este valor se almacena en UTC. En la tabla de datos, se muestra en la zona horaria del usuario. |
| <code>_submitted_by</code> | El nombre de usuario de la persona que envió los datos. Siempre se registra en los envíos de KoboCollect, y se registra en los envíos de formularios web solo cuando se <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requiere autenticación</a>. |
| <code>rootUuid</code> | Un identificador estable para el envío dentro del proyecto. Se toma del <code>_uuid</code> original del envío cuando el registro se envía por primera vez, y no cambia cuando el envío se edita, por lo que es el campo más confiable para rastrear un envío específico a lo largo del tiempo. |

<p class="note">
<strong>Nota:</strong> Estos campos son distintos de los <a href="https://support.kobotoolbox.org/es/form_meta.html">metadatos del formulario</a> habilitados por el usuario, ya que se generan automáticamente para cada envío. No es necesario agregarlos durante el desarrollo del formulario.
</p>

## Filtrar y ordenar tus datos

De forma predeterminada, los envíos en KoboToolbox aparecen en la tabla de datos en orden de envío, con las entradas más recientes en la parte superior. En proyectos grandes, filtrar y ordenar son funciones esenciales para explorar, revisar y limpiar datos. Te ayudan a encontrar rápidamente encuestados específicos, examinar patrones e identificar registros que requieren atención.

<p class="note">
<strong>Nota:</strong> La vista <strong>Tabla</strong> en KoboToolbox ofrece filtrado y ordenación básicos para el seguimiento y la edición de datos. Para un análisis de datos más avanzado, incluido el filtrado con múltiples condiciones, recomendamos <a href="https://support.kobotoolbox.org/es/export_download.html">exportar tu conjunto de datos</a> y usar software de hojas de cálculo o análisis.
</p>

Para cada columna de la tabla de datos, puedes usar las siguientes funciones:

- **Buscar:** Usa la barra de búsqueda encima de los campos de texto, número y fecha para filtrar resultados. Por ejemplo, puedes buscar un ID único o filtrar por una edad específica.
- **Filtrar:** Para los campos basados en preguntas de tipo selección, haz clic en **Mostrar todo** en el encabezado de la columna para abrir una lista de opciones de respuesta. Selecciona una opción para filtrar las respuestas.
- **Ordenar:** Haz clic en el encabezado de una columna y elige **Ordenar A → Z** o **Ordenar Z → A** para cambiar el orden de los envíos.

<p class="note">
<strong>Nota:</strong> Ordenar la tabla se aplica a todos los usuarios y persiste después de salir de la vista <strong>Tabla</strong>. La búsqueda y el filtrado se aplican solo a ti mientras estás en la vista <strong>Tabla</strong> y se restablecen automáticamente cuando la abandonas.
</p>

## Ver envíos individuales

Abrir un envío individual te permite revisar todos los datos de un solo encuestado. La vista de envío individual incluye herramientas para examinar y gestionar un registro individual.

Para abrir un envío, haz clic en <i class="k-icon-view"></i> **Ver** en la fila correspondiente.

![Abrir detalles del envío](images/viewing_validating_data/open_submission.png)

La ventana del envío muestra todas las respuestas e incluye las siguientes opciones:

- Ver datos en [cualquier idioma del formulario](https://support.kobotoolbox.org/es/collecting_data_multiple_languages.html).
- Mostrar [valores XML](https://support.kobotoolbox.org/es/glossary.html#xml-value) junto a cada pregunta.
- **Ver** y **Editar** el envío como [formulario web](https://support.kobotoolbox.org/es/editing_deleting_data.html).
- **Duplicar** el envío.
- <i class="k-icon-print"></i> **Imprimir** el envío.
- <i class="k-icon-trash"></i> **Eliminar** el envío.
- Asignar un **Estado de validación.**

![Ventana de visualización del envío](images/viewing_validating_data/view_submission.png)

Dentro de la vista de envío individual, navega por los envíos usando **< Anterior** y **Siguiente >**.

## Validar tus datos

La validación de registros ayuda a los equipos del proyecto a mantener la calidad de los datos, rastrear el estado de revisión y marcar los problemas que requieren seguimiento. El estado de validación aparece como una columna dedicada en la vista **Tabla**, y los usuarios con los permisos adecuados pueden actualizarlo para envíos individuales o múltiples.

Los estados disponibles son:

- **Aprobado:** El envío ha sido revisado y confirmado como completo, preciso y adecuado para su uso en el análisis.
- **No aprobado:** El envío no cumple con los requisitos de calidad de datos y debe excluirse del análisis o eliminarse del conjunto de datos.
- **En espera:** El envío requiere revisión. Se necesita verificación adicional o seguimiento antes de que los datos puedan aceptarse o rechazarse.

La validación permite una revisión de datos estructurada en equipos colaborativos. Por ejemplo, los revisores pueden filtrar la tabla para mostrar solo los envíos que requieren revisión.

<p class="note">
<strong>Nota:</strong> El propietario del proyecto puede otorgar el permiso de <strong>Validar envíos</strong> <a href="https://support.kobotoolbox.org/es/managing_permissions.html">permiso</a> a otros usuarios de forma independiente al permiso de <strong>Editar envíos</strong>.
</p>

### Actualizar el estado de validación en bloque

El estado de validación se puede aplicar a varios envíos a la vez, lo que es útil para revisiones a gran escala o controles de calidad.

Para validar envíos en bloque:

1. Selecciona los envíos usando las casillas de verificación.
2. Haz clic en **Cambiar estado.**
3. Elige un estado de validación.

<p class="note">
<strong>Nota:</strong> Puedes seleccionar todos los envíos de la página actual haciendo clic en la casilla de verificación del encabezado de la tabla. Para seleccionar todos los envíos del proyecto en todas las páginas, haz clic en la flecha junto a la casilla y elige <strong>Seleccionar todos los resultados.</strong>
</p>

![Seleccionar envíos](images/viewing_validating_data/select.png)

## Resolución de problemas

<details>
  <summary><strong>Campos o preguntas que no aparecen en la tabla de datos</strong></summary>
Si agregaste nuevas preguntas después de que comenzó la recolección de datos, es posible que los campos permanezcan ocultos si la visibilidad de la tabla se configuró previamente. Haz clic en <i class="k-icon-qt-hidden"></i> <strong>ocultar campos</strong>, localiza y selecciona la nueva pregunta y luego haz clic en <strong>Aplicar.</strong>
</details>

<br>

<details>
  <summary><strong>Funcionalidad de búsqueda para tipos de preguntas Ocultas</strong></summary>
  La función de <strong>Búsqueda</strong> no está disponible actualmente para los tipos de preguntas <strong>Ocultas</strong>. Para localizar un valor específico en un campo <strong>Oculto</strong>, ordena la tabla por ese campo y desplázate hasta el valor en orden alfabético o numérico.
</details>

<br>

<details>
  <summary><strong>El campo _submitted_by está vacío</strong></summary>
  El campo <code>_submitted_by</code> se completa solo cuando un envío está vinculado a un nombre de usuario de KoboToolbox. En KoboCollect, este campo siempre se registra. En los formularios web, se registra solo cuando el proyecto <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requiere autenticación</a>. Si el formulario permite envíos sin nombre de usuario y contraseña, este campo estará vacío.<br><br>
Para registrar <code>_submitted_by</code> en los envíos de formularios web, ve a <strong>FORMULARIO > Recolectar datos</strong> y desactiva "Permitir envíos a este formulario sin nombre de usuario ni contraseña".
</details>

<br>