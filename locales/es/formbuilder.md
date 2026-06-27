# Comenzar con el editor de formularios

**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/b4dddc39234bcb1960d654dc36c30ad9c31e1fb9/source/formbuilder.md" class="reference">6 May 2026</a>


<iframe src="https://www.youtube.com/embed/PFL1_rBB5Q8?si=RkwB2XGHppAK-RRF&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

El editor de formularios de KoboToolbox **(Formbuilder)** es una herramienta de uso amigable para diseñar e implementar formularios de recolección de datos. Este artículo ofrece una descripción general básica de sus funciones, desde agregar y gestionar preguntas hasta organizar tu formulario.

<p class="note">
    Para aprender a crear un nuevo formulario en KoboToolbox, consulta la <a href="https://support.kobotoolbox.org/es/quick_start.html">Guía de inicio rápido</a> de KoboToolbox. Para una introducción completa al desarrollo de formularios con KoboToolbox, recomendamos el <a href="https://academy.kobotoolbox.org/courses/esenciales">Curso Esenciales de KoboToolbox</a>, un curso en línea de aprendizaje autónomo de la KoboToolbox Academy.
</p>

## Agregar una pregunta

Para agregar una pregunta a tu formulario, haz clic en el botón <i class="k-icon k-icon-plus"></i> que aparece debajo de cada pregunta. Escribe la etiqueta de tu pregunta y haz clic en **Agregar pregunta**. Luego, [elige el tipo de pregunta](question_types.md).

Para los tipos de pregunta [Seleccionar una o Seleccionar varias](https://support.kobotoolbox.org/es/select_one_and_select_many.html), agrega las opciones de respuesta debajo de la pregunta.

<p class="note">
<strong>Nota</strong>: Una vez seleccionado el tipo de pregunta, no es posible cambiarlo en el Formbuilder. Para cambiar el tipo de una pregunta existente, elimina la pregunta y crea una nueva con la misma etiqueta.
</p>

## Agregar una sugerencia de pregunta

Una sugerencia de pregunta proporciona instrucciones adicionales debajo del texto de la pregunta en el formulario. Para agregar una sugerencia de pregunta, haz clic en **Sugerencia de pregunta** debajo de la pregunta y escribe tu sugerencia.

## Duplicar una pregunta

Para duplicar una pregunta, haz clic en <i class="k-icon-duplicate"></i> **Pregunta duplicada** en el menú de la pregunta a la derecha. Una copia exacta aparecerá directamente debajo de la original.

## Eliminar una pregunta

Para eliminar una pregunta, haz clic en <i class="k-icon-trash"></i> **Eliminar pregunta** en el menú de la pregunta a la derecha. Se te pedirá que confirmes antes de que se elimine definitivamente de tu formulario.

<p class="note">
<strong>Nota</strong>: Para eliminar varias preguntas a la vez en el Formbuilder, agrúpalas y luego elimina el grupo.
</p>

## Cambiar la configuración de una pregunta

Para acceder a la configuración avanzada de una pregunta, haz clic en <i class="k-icon-settings"></i> **Configuración** en el menú de la pregunta a la derecha. Aquí puedes agregar lógica de omisión, criterios de validación, sugerencias adicionales y hacer que una pregunta sea obligatoria.

<p class="note">
Para obtener más información sobre la configuración de preguntas, consulta <a href="https://support.kobotoolbox.org/es/question_options.html">Opciones de preguntas en el Formbuilder</a>, <a href="https://support.kobotoolbox.org/es/skip_logic.html">Añadir lógica de salto al Formbuilder</a> y <a href="https://support.kobotoolbox.org/es/validation_criteria.html">Añadir criterios de validación en el Formbuilder</a>.
</p>

## Agregar preguntas a la biblioteca

Para guardar una pregunta y reutilizarla en formularios futuros, haz clic en <i class="k-icon-folder-plus"></i> **Agregar pregunta a la biblioteca**. Se guardará como una copia en tu [biblioteca de preguntas](https://support.kobotoolbox.org/es/question_library.html). Puedes modificar o eliminar la pregunta original en tu formulario sin que esto afecte la copia guardada en la biblioteca.

## Agrupar preguntas

Las preguntas pueden [agruparse](https://support.kobotoolbox.org/es/group_repeat.html) para organizar tu formulario. Selecciona las preguntas con la tecla **CTRL** (Windows) o **Command** (Mac) y luego haz clic en <i class="k-icon k-icon-group"></i> **Crear grupo con las preguntas seleccionadas** en la barra de menú superior izquierda.

## Cambiar el orden de las preguntas

Las preguntas y los grupos pueden moverse a cualquier posición del formulario. Arrastra y suelta una pregunta o grupo desde su posición actual hasta donde deseas colocarlo.

<p class="note">
<strong>Nota</strong>: Para mover varias preguntas a la vez en el Formbuilder, agrúpalas y luego mueve el grupo. Después puedes <a href="https://support.kobotoolbox.org/es/group_repeat.html#removing-a-question-group">desagrupar</a> las preguntas.
</p>

## Previsualizar el formulario

Después de agregar todas las preguntas a tu formulario, haz clic en <i class="k-icon k-icon-view"></i> **Previsualizar el formulario** para ver cómo se verá una vez implementado.

## Guardar el formulario

Mientras editas tu formulario, haz clic regularmente en **SAVE** en la esquina superior derecha de la pantalla para asegurarte de que tu trabajo quede guardado. Aparecerá un asterisco (*) junto al botón **SAVE** cuando tengas cambios sin guardar.