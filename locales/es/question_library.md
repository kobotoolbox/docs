# Usar la biblioteca de preguntas de KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/26da17c7c8203fb51267183a3c44789ce7576a47/source/question_library.md" class="reference">25 Mar 2026</a>

La **biblioteca de preguntas** de KoboToolbox te permite guardar, reutilizar y compartir preguntas en múltiples formularios. En lugar de recrear preguntas y opciones de uso frecuente, puedes almacenarlas en la biblioteca e insertarlas rápidamente en nuevos formularios.

La biblioteca de preguntas puede almacenar **preguntas individuales, bloques de preguntas** y **plantillas de formularios completos.** También puedes organizar tu contenido usando **colecciones** para agrupar elementos relacionados por proyecto, tema, país u organización.

Usar la biblioteca de preguntas ayuda a mantener la coherencia entre proyectos, simplifica el proceso de diseño de formularios y facilita compartir contenido estandarizado con otros miembros de tu equipo. Puedes acceder a la biblioteca de preguntas desde el menú lateral izquierdo del sitio web de KoboToolbox.

![Acceder a la biblioteca de preguntas](images/question_library/access.png)

<p class="note">
<strong>Nota:</strong> La biblioteca de preguntas de KoboToolbox puede contener contenido público y privado. Este artículo se centra en <strong>Mi biblioteca</strong>, donde puedes guardar, organizar, reutilizar y compartir tus propias preguntas, bloques de preguntas y plantillas de formularios. Para obtener más información sobre cómo hacer público el contenido de la biblioteca, consulta <a href="https://support.kobotoolbox.org/es/using_public_collections.html#">Colecciones públicas en la biblioteca de KoboToolbox</a>.
</p>

Este artículo cubre los siguientes temas:
- Agregar preguntas a la biblioteca de preguntas y usarlas en tus formularios
- Agregar plantillas a tu biblioteca de preguntas y crear formularios a partir de plantillas
- Trabajar con colecciones para organizar tu contenido

## Agregar preguntas a la biblioteca de preguntas

### Agregar preguntas desde el Formbuilder

Al crear un formulario en el [editor de formularios de KoboToolbox (Formbuilder)](https://support.kobotoolbox.org/es/formbuilder.html), puedes guardar cualquier pregunta en tu biblioteca de preguntas haciendo clic en <i class="k-icon-folder-plus"></i> **Agregar pregunta a la biblioteca** en el menú lateral derecho de la pregunta.

![Agregar pregunta a la biblioteca](images/question_library/add_to_library.png)

Este método conserva todos los componentes de tu pregunta, incluidas las opciones de respuesta, las [traducciones](https://support.kobotoolbox.org/es/language_dashboard.html), las [opciones de pregunta](https://support.kobotoolbox.org/es/question_options.html), la [lógica de omisión](https://support.kobotoolbox.org/es/skip_logic.html) y los [criterios de validación](https://support.kobotoolbox.org/es/validation_criteria.html).

<p class="note">
<strong>Nota:</strong> Al agregar una pregunta a tu biblioteca, se guarda una copia de la pregunta, y los cambios realizados en la pregunta original no afectan a la versión guardada.
</p>

También puedes agregar un [grupo de múltiples preguntas](https://support.kobotoolbox.org/es/group_repeat.html) a la biblioteca de preguntas haciendo clic en <i class="k-icon-folder-plus"></i> **Agregar pregunta a la biblioteca** a nivel del grupo. El grupo se guarda como un **bloque de preguntas.**

![Agregar múltiples preguntas a la biblioteca](images/question_library/add_group.png)

### Agregar preguntas desde la biblioteca

También puedes crear preguntas de biblioteca directamente desde la biblioteca de preguntas:

1. Haz clic en <i class="k-icon-library"></i> **Biblioteca** en el menú lateral izquierdo para abrir la biblioteca.
2. Haz clic en **NUEVO** en la esquina superior izquierda.
3. Selecciona <i class="k-icon-block"></i> **Bloque de preguntas**. Esto abre el Formbuilder de KoboToolbox, donde puedes agregar la pregunta o el grupo de preguntas que deseas guardar.
4. Haz clic en **Crear** en la esquina superior derecha para guardar el bloque de preguntas en tu biblioteca.

![Crear elemento en la biblioteca](images/question_library/new.png)

Puedes cargar preguntas o bloques de preguntas desde un [XLSForm](https://support.kobotoolbox.org/es/edit_forms_excel.html) haciendo clic en <i class="k-icon-upload"></i> **Cargar** en **Crear elemento en la biblioteca** y cargando un XLSForm.

### Gestionar preguntas en la biblioteca de preguntas

En la vista **Mi biblioteca**, puedes ver todas las preguntas y bloques de preguntas guardados. Para cada elemento, puedes ver detalles como el número de preguntas incluidas, el propietario, los idiomas disponibles y la fecha de última modificación.

Para cada elemento guardado, puedes pasar el cursor sobre él para:

- <i class="k-icon-edit"></i> **Editar** la(s) pregunta(s) en el Formbuilder
- <i class="k-icon-tag"></i> **Agregar etiquetas** para ayudar a organizar y categorizar elementos y facilitar la búsqueda
- <i class="k-icon-user-share"></i> **Compartir** con otros usuarios, asignando permisos para ver, editar o gestionar el elemento
- <i class="k-icon-duplicate"></i> **Clonar** para crear un duplicado que puedes modificar de forma independiente
- <i class="k-icon-more"></i> Hacer clic en **Otras acciones** para gestionar las [traducciones](https://support.kobotoolbox.org/es/language_dashboard.html), descargar el elemento como XLS o XML, o eliminarlo

![Gestionar la biblioteca de preguntas](images/question_library/manage_library.png)

También puedes hacer clic en cualquier elemento guardado para ver sus detalles completos, incluidas todas las preguntas contenidas en un bloque de preguntas.

## Agregar preguntas a un formulario desde la biblioteca de preguntas

Una vez que hayas agregado preguntas a tu biblioteca, puedes usarlas en futuros formularios. Para usar preguntas de la biblioteca en tu formulario:

1. Abre tu formulario en el [editor de formularios de KoboToolbox (Formbuilder)](https://support.kobotoolbox.org/es/formbuilder.html).
2. Haz clic en <i class="k-icon-library"></i> **Agregar desde la biblioteca** en la esquina superior derecha.
3. Selecciona la pregunta o el bloque de preguntas que deseas agregar y arrástralo y suéltalo en la ubicación deseada dentro de tu formulario.
4. Si tu biblioteca de preguntas contiene muchos elementos, puedes usar la función **Buscar** para localizar rápidamente la pregunta o el bloque que necesitas.

![Agregar pregunta al formulario desde la biblioteca](images/question_library/add_from_library.png)

<p class="note">
<strong>Nota:</strong> Cuando agregas una pregunta de tu biblioteca de preguntas a un formulario, los cambios que realices en el formulario no afectarán a la versión original guardada en la biblioteca.
</p>

## Agregar plantillas a tu biblioteca de preguntas

<iframe src="https://www.youtube.com/embed/k-2jnfd3DrE?si=wR1zkjMjgM2Dq9mT&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Además de guardar preguntas individuales o bloques de preguntas, puedes crear plantillas de formularios completos que se pueden convertir en proyectos de KoboToolbox. Las plantillas son útiles para estandarizar formularios completos que se pueden reutilizar entre equipos, proyectos o países.

<p class="note">
<strong>Nota:</strong> Un <strong>bloque de preguntas</strong> es un grupo de preguntas que se puede insertar en cualquier parte de un formulario, mientras que una <strong>plantilla</strong> contiene un formulario completo que puede convertirse en un proyecto.
</p>

### Crear una plantilla

Puedes crear una plantilla desde tu biblioteca de preguntas o desde un formulario de KoboToolbox existente.

Desde tu **biblioteca de preguntas**, puedes:

- Hacer clic en **NUEVO > <i class="k-icon-template"></i> Plantilla.** Se te llevará al Formbuilder para diseñar el formulario después de ingresar los detalles de la plantilla.
- Hacer clic en **NUEVO > <i class="k-icon-upload"></i> Cargar**, cargar un XLSForm y seleccionar **Cargar como plantilla.**

![Cargar plantilla en la biblioteca](images/question_library/upload_as_template.png)

<p class="note">
<strong>Nota:</strong> Si usas XLSForm, puedes crear plantillas bloqueadas que impidan que otros usuarios editen partes específicas del formulario. Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/library_locking.html">Bloquear cuestionarios para la biblioteca usando XLSForms</a>.
</p>

Para crear una plantilla a partir de un **formulario de KoboToolbox existente:**

1. Abre la página **FORMULARIO** del proyecto.
2. Haz clic en <i class="k-icon-more"></i> **Otras acciones** en la esquina superior derecha.
3. Selecciona <i class="k-icon-template"></i> **Crear plantilla.**

![Crear plantilla](images/question_library/create_template.png)

Desde la página **Mi biblioteca**, puedes gestionar las plantillas de la misma manera que las preguntas o los bloques de preguntas. Puedes compartirlas con otros usuarios, agregar etiquetas, editar detalles o eliminarlas.

### Crear un proyecto a partir de una plantilla

Puedes usar una plantilla para crear un nuevo proyecto de formulario desde tu biblioteca de preguntas o desde tu **Página de proyectos.**

Desde la **biblioteca de preguntas:**

1. Pasa el cursor sobre la plantilla y haz clic en <i class="k-icon-projects"></i> **Crear proyecto** a la derecha.
2. Ingresa un nombre para el nuevo proyecto.

![Crear plantilla](images/question_library/create_project.png)

Desde la **Página de proyectos:**

1. Haz clic en **NUEVO** y selecciona <i class="k-icon-template"></i> **Usar una plantilla.**
2. Elige una plantilla guardada y haz clic en **Siguiente.**
3. Ingresa los detalles del proyecto y haz clic en **Crear proyecto.**

En ambos casos, se creará un nuevo proyecto de KoboToolbox que puedes editar e implementar.

![Usar una plantilla](images/question_library/use_template.png)

<p class="note">
<strong>Nota:</strong> Editar un proyecto creado a partir de una plantilla no modifica la plantilla original.
</p>

## Usar colecciones en la biblioteca de preguntas

<iframe src="https://www.youtube.com/embed/EfnyQh-awqk?si=7Hhb499SgsEL9pg4&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Una **colección** es un grupo de preguntas, bloques de preguntas y/o plantillas organizados juntos porque están relacionados con el mismo proyecto, tema, país u otro contexto compartido. Las colecciones te ayudan a estructurar y gestionar el contenido reutilizable en tu biblioteca de preguntas.

### Crear una colección

Para crear una colección:

1. Desde tu biblioteca de preguntas, haz clic en **NUEVO** y selecciona <i class="k-icon-folder"></i> **Colección.**
2. Ingresa un nombre y, si lo deseas, agrega una breve descripción, organización, sector principal y país. Estos campos son opcionales.
3. Agrega etiquetas para ayudar a categorizar y organizar tu colección.
4. Haz clic en **Crear.**

![Crear colección](images/question_library/create_collection.png)

<p class="note">
<strong>Nota:</strong> Si deseas importar un gran número de preguntas o bloques de preguntas a tu biblioteca como una sola colección, puedes hacerlo usando un <a href="https://support.kobotoolbox.org/es/edit_forms_excel.html">XLSForm</a>. Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/import_collection.html">Importar una colección con XLSForm</a>.
</p>

Después de crear la colección, se te llevará a la página principal de la colección, que mostrará el mensaje: "No hay recursos para mostrar."

### Agregar elementos a una colección

Puedes agregar preguntas, bloques de preguntas o plantillas a una colección de varias maneras:

- Desde la **página de la colección:**
    - Haz clic en **NUEVO > <i class="k-icon-block"></i> Bloque de preguntas** para crear una nueva pregunta o bloque en el Formbuilder y guardarlo en la colección.
    - Haz clic en **NUEVO > <i class="k-icon-template"></i> Plantilla** para crear una plantilla y guardarla en la colección.
- Desde **Mi biblioteca**, pasa el cursor sobre un elemento existente, haz clic en <i class="k-icon-more"></i> **Otras acciones** y elige el nombre de tu colección en <i class="k-icon-folder-in"></i> **Mover a.**

![Agregar a la colección](images/question_library/add_to_collection.png)

<p class="note">
<strong>Nota:</strong> No puedes crear colecciones anidadas. Si creas una colección dentro de otra colección, se guardará como una colección separada.
</p>

Para eliminar un elemento de una colección, haz clic en <i class="k-icon-more"></i> **Otras acciones** en la fila del elemento y selecciona <i class="k-icon-folder-out"></i> **Eliminar de la recolección.**

### Gestionar colecciones

Puedes gestionar tu colección desde la página **Mi biblioteca** pasando el cursor sobre ella y seleccionando las opciones disponibles para <i class="k-icon-edit"></i> modificar sus detalles, <i class="k-icon-tag"></i> agregar etiquetas, <i class="k-icon-user-share"></i> compartirla con otros usuarios o <i class="k-icon-trash"></i> eliminarla. También puedes realizar estas acciones directamente desde la página de la colección.

<p class="note">
<strong>Nota:</strong> Eliminar una colección elimina permanentemente todos los elementos que contiene.
</p>

Para **hacer pública una colección**, abre la colección y haz clic en el botón <i class="k-icon-globe-alt"></i> **Publicar** en la esquina superior derecha. Ten en cuenta que los campos **nombre, organización** y **sector** deben estar completados antes de que una colección pueda hacerse pública.

<p class="note"> Para obtener más información sobre las colecciones públicas, consulta <a href="https://support.kobotoolbox.org/es/using_public_collections.html">Colecciones públicas en la biblioteca KoboToolbox</a>.
</p>