# Grupos y grupos de repetición en el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/group_repeat.md" class="reference">23 Apr 2026</a>


<iframe src="https://www.youtube.com/embed/nmPACLvYnUI?si=mkUi9RBLNHObj9ei&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Agrupar preguntas ayuda a organizar preguntas relacionadas en secciones, añade estructura al formulario y facilita la navegación. Por ejemplo, todas las preguntas demográficas pueden agruparse en una sola sección del formulario.

Los usuarios pueden necesitar agrupar preguntas por diversas razones:
-   **Estructurar el cuestionario:** Las preguntas con temas o atributos comunes pueden agruparse en una sola sección.
-   **Mostrar un conjunto de preguntas por página:** Las preguntas agrupadas pueden mostrarse en páginas o pantallas separadas durante la recolección de datos.
-   **Omitir un grupo de preguntas:** La lógica de omisión puede aplicarse a todo el grupo en lugar de añadirla a cada pregunta individualmente.
-   **Crear un grupo:** Los grupos de preguntas pueden repetirse, por ejemplo en encuestas de hogares o seguimiento de indicadores.

Este artículo explica cómo:
* Crear, añadir, eliminar y reordenar preguntas en un grupo desde el editor de formularios de KoboToolbox (Formbuilder)
* Usar subgrupos y [grupos de repetición](#repetir-un-grupo-de-preguntas)
* Ajustar la [configuración del grupo](#configuración-del-grupo-de-preguntas), como las opciones de visualización y la lógica de omisión


## Crear y gestionar grupos de preguntas

El Formbuilder facilita agrupar preguntas, añadir preguntas a grupos, eliminar preguntas de grupos y reordenar preguntas dentro de un grupo.

### Agrupar un conjunto de preguntas

Para crear un grupo de preguntas, sigue los pasos a continuación:

1. Elabora un conjunto de preguntas que desees agrupar.
2. Selecciona las preguntas usando la tecla **CTRL** (Windows) o la tecla **Command** (Mac).
3. Haz clic en <i class="k-icon-group"></i> **Crear grupo con las preguntas seleccionadas** en la barra de menú superior izquierda.

![image](/images/group_repeat/grouping_questions.png)

El nuevo grupo aparecerá dentro de un recuadro sombreado, diferenciándolo de las preguntas estándar. También puedes cambiar la etiqueta del grupo, que se mostrará en la parte superior del grupo en el formulario.

<p class="note">
    <b>Nota:</b> También puedes crear una sola pregunta, seleccionarla y hacer clic en <b>Agregar grupo</b>. Luego puedes añadir más preguntas dentro del grupo, como se describe a continuación.
</p>

### Añadir preguntas dentro de un grupo

Coloca el cursor en cualquier lugar dentro del grupo donde desees añadir una nueva pregunta. Haz clic en el <i class="k-icon-plus"></i> **signo más** dentro del grupo para añadir una nueva pregunta.

<p class="note">
    <b>Nota:</b> Si haces clic en el <i class="k-icon-plus"> </i><b>signo más</b> que está fuera del grupo, añadirás una pregunta fuera del grupo.
</p>

También puedes arrastrar y soltar cualquier pregunta existente dentro de un grupo de preguntas.

### Eliminar preguntas de un grupo

Para eliminar una pregunta de un grupo pero conservarla en el formulario, selecciona la pregunta y arrástrala fuera del grupo.

Para eliminar permanentemente una pregunta del formulario, haz clic en <i class="k-icon-trash"></i> **Eliminar pregunta** en el menú de la pregunta a la derecha y luego haz clic en **OK**.

### Reordenar una pregunta dentro de un grupo

Puedes reordenar las preguntas dentro de un grupo seleccionando la pregunta y arrastrándola a la posición deseada (hacia arriba o hacia abajo).

### Eliminar un grupo de preguntas
Si ya no necesitas un grupo de preguntas, puedes desagruparlas o eliminar el grupo completo. Para hacerlo, haz clic en el botón <i class="k-icon-trash"></i> **Eliminar** en el encabezado del grupo.

Aparecerá un cuadro de diálogo preguntándote si deseas dividir el grupo o eliminar todo.

- Haz clic en **DESAGRUPAR** para eliminar el grupo conservando las preguntas en el formulario.
- Haz clic en **ELIMINAR TODO** para eliminar tanto el grupo como todas sus preguntas.

<p class="note">
    <b>Nota:</b> Un grupo de preguntas puede crearse o colocarse dentro de otro grupo. Esto se conoce como <b>subgrupos</b>. Los <a href="https://support.kobotoolbox.org/es/group_repeat.html#repeating-a-question-group">grupos de repetición</a> también pueden anidarse.
</p>

## Configuración del grupo de preguntas

Después de crear un grupo de preguntas, puedes personalizar su comportamiento y apariencia. Por ejemplo, puedes mostrar todas las preguntas del grupo en la misma pantalla, aplicar lógica de omisión a todo el grupo o configurar el grupo para que se repita.

### Mostrar preguntas agrupadas en la misma pantalla

En KoboCollect, las preguntas aparecen de una en una de forma predeterminada. En los formularios web, todas las preguntas aparecen en la misma pantalla.

Para mostrar las preguntas por grupo en la misma pantalla durante la recolección de datos, haz clic en el icono <i class="k-icon-settings"></i> **Configuración** a la derecha del nombre del grupo. Luego, en **Aspecto (avanzado)**, selecciona **field-list** (Mostrar todas las preguntas de este grupo en la misma pantalla).

<p class="note">
    <b>Nota:</b> Si planeas recolectar datos usando formularios web, también deberás activar el tema <b>Múltiples páginas</b> en el menú <b>Estilo del formulario</b> (<b>Diseño y configuración</b>). Para más información sobre los estilos de formularios web, consulta <a href="https://support.kobotoolbox.org/es/alternative_enketo.html">Diseñar formularios web usando el Formbuilder</a>.
</p>

### Omitir un grupo de preguntas
Para omitir un grupo de preguntas, asegúrate de tener al menos una pregunta de control ubicada antes de las preguntas agrupadas. Haz clic en el icono <i class="k-icon-settings"></i> **Configuración** del grupo de preguntas, luego selecciona **Lógica de omisión** y configura las condiciones de omisión como lo harías para una pregunta individual.

<p class="note">
    Para obtener más información sobre cómo añadir condiciones de lógica de omisión, consulta <a href="https://support.kobotoolbox.org/es/skip_logic.html">Añadir lógica de salto al Formbuilder</a>.
</p>

### Repetir un grupo de preguntas
Un grupo de repetición permite que un conjunto de preguntas se responda varias veces dentro de un formulario. Por ejemplo, en una encuesta de hogares, puedes usar un grupo de repetición para recolectar el nombre, la edad, el género y el nivel educativo de cada miembro del hogar.

Para crear un grupo de repetición:
1. Crea todas las preguntas que desees incluir y luego agrúpalas.
2. En la <i class="k-icon-settings"></i> **Configuración** del grupo, activa la opción **Repetir este grupo si es necesario**.

![image](/images/group_repeat/repeating_groups.png)

Durante la recolección de datos, los encuestadores podrán ingresar respuestas para estas preguntas agrupadas tantas veces como sea necesario.

<p class="note">
    <b>Nota:</b> Añadir grupos de repetición a tu formulario crea una estructura de datos diferente en comparación con las variables o grupos estándar. Cuando descargues tus datos en formato .xlsx, encontrarás una hoja separada para cada grupo de repetición. Para más información sobre cómo exportar y usar datos de grupos de repetición, consulta <a href="https://support.kobotoolbox.org/es/managing_repeat_groups.html">Gestión de datos de grupos repetidos</a>.
</p>

### Configuración avanzada para grupos de repetición
Configuraciones y funcionalidades adicionales para los grupos de repetición están disponibles a través de XLSForm, pero no directamente en el Formbuilder. Estas incluyen establecer un número fijo o dinámico de repeticiones y usar información de grupos de repetición en otras partes del formulario.

<p class="note">
    Para más información sobre la configuración avanzada de grupos de repetición, consulta <a href="https://support.kobotoolbox.org/es/repeat_groups_xls.html">Grupos repetidos en XLSForm</a>.
</p>