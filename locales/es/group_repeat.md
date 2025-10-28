# Agrupar preguntas y grupos repetidos
<a href="../group_repeat.html">Read in English</a> | <a href="../fr/group_repeat.html">Lire en français</a> | <a href="../ar/group_repeat.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/a4227085bc495cc72c9380430577b0e092d101bb/source/group_repeat.md" class="reference">25 ago 2025</a>

<iframe src="https://www.youtube.com/embed/nmPACLvYnUI?si=mkUi9RBLNHObj9ei" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Agrupar preguntas ayuda a organizar preguntas relacionadas en secciones, añade estructura a tu formulario y facilita la navegación. Por ejemplo, todas las preguntas demográficas pueden agruparse juntas en una sección del formulario.

Los/as usuarios/as pueden necesitar agrupar preguntas por varias razones:
-   **Estructurar el cuestionario:** Las preguntas con temas o atributos comunes pueden agruparse juntas en una sola sección.
-   **Mostrar un conjunto de preguntas por página:** Las preguntas agrupadas pueden mostrarse en páginas o pantallas separadas durante la recolección de datos.
-   **Omitir un grupo de preguntas:** Se puede añadir lógica de salto a todo el grupo en lugar de añadirla a cada pregunta individual.
-   **Crear un listado:** Los grupos de preguntas pueden repetirse, por ejemplo para encuestas de hogares o seguimiento de indicadores.

Este artículo cubre cómo crear y manejar grupos de preguntas y [grupos repetidos](#repeating-a-question-group) en el editor de formularios de KoboToolbox (Formbuilder).

## Crear y manejar grupos de preguntas

El editor de formularios facilita agrupar preguntas, añadir preguntas a grupos, eliminar preguntas de grupos y reordenar preguntas dentro de un grupo.

### Agrupar un conjunto de preguntas

Para crear un grupo de preguntas, sigue los pasos a continuación:

1. Crea un conjunto de preguntas que te gustaría agrupar juntas.
2. Selecciona las preguntas usando la tecla **CTRL** (Windows) o la tecla **Command** (Mac).
3. Haz clic en <i class="k-icon-group"></i> **Crear grupo con las preguntas seleccionadas** en la barra de menú superior izquierda.

![image](/images/group_repeat/grouping_questions.png)

Tu nuevo grupo aparecerá encerrado dentro de un cuadro sombreado, distinguiéndolo de las preguntas estándar. También puedes cambiar la etiqueta del grupo, que se mostrará en la parte superior del grupo en el formulario.

<p class="note">
    <b>Nota:</b> Alternativamente, puedes crear una sola pregunta, seleccionar la pregunta y hacer clic en <b>Crear grupo</b>. Luego, puedes añadir más preguntas dentro del grupo, como se describe a continuación.
</p>

### Añadir preguntas dentro de un grupo

Coloca el cursor en cualquier lugar dentro del grupo donde quieras añadir una nueva pregunta. Haz clic en un <i class="k-icon-plus"></i> **signo** dentro del grupo para añadir una nueva pregunta.

<p class="note">
    <b>Nota:</b> Si haces clic en el <i class="k-icon-plus"> </i><b>signo</b> que está ubicado fuera del grupo, estarás añadiendo una pregunta fuera del grupo.
</p>

También puedes arrastrar y soltar cualquier pregunta existente dentro de un grupo de preguntas.

### Eliminar preguntas de un grupo

Para eliminar una pregunta de un grupo pero mantenerla en el formulario, selecciona la pregunta y arrástrala fuera del grupo.

Para eliminar permanentemente una pregunta del formulario, haz clic en <i class="k-icon-trash"></i> **Eliminar pregunta** desde el menú de la pregunta a la derecha, luego haz clic en **OK**.

### Reordenar una pregunta dentro de un grupo

Puedes reordenar preguntas dentro de un grupo seleccionando la pregunta y arrastrándola a la posición deseada (arriba o abajo).

### Eliminar un grupo de preguntas
Si ya no necesitas un grupo de preguntas, puedes desagruparlas o eliminar el grupo completo. Para hacer esto, haz clic en el botón <i class="k-icon-trash"></i> **Eliminar** del encabezado del grupo.

Aparecerá un cuadro de diálogo pidiéndote que confirmes si deseas separar el grupo o eliminar todo.

- Haz clic en **DESAGRUPAR** para eliminar el grupo manteniendo las preguntas en el formulario.
- Haz clic en **ELIMINAR TODO** para eliminar tanto el grupo como todas sus preguntas.

### Grupos anidados

Un grupo de preguntas puede crearse o colocarse dentro de otro grupo. Esto se conoce como **grupos anidados**. Los [grupos repetidos](#repeating-a-question-group) también pueden anidarse.

---

## Configuración de grupos de preguntas

Después de crear un grupo de preguntas, puedes personalizar su comportamiento y apariencia. Por ejemplo, puedes mostrar todas las preguntas del grupo en la misma pantalla, aplicar lógica de salto a todo el grupo o configurar el grupo para que se repita.

### Mostrar preguntas agrupadas en la misma pantalla

En KoboCollect, las preguntas aparecen de una en una por defecto. En los formularios web de Enketo, todas las preguntas aparecen en la misma pantalla.

Para mostrar preguntas por grupo en la misma pantalla durante la recolección de datos, haz clic en el ícono <i class="k-icon-settings"></i> **Configuración** a la derecha del nombre del grupo. Luego, en **Apariencia (Avanzado)**, selecciona **field-list** (Mostrar todas las preguntas de este grupo en la misma pantalla).

<p class="note">
    <b>Nota:</b> Si planeas recolectar datos usando formularios web de Enketo, también necesitarás habilitar el tema <b>Múltiples páginas</b> en el menú <b>Estilo del formulario</b> (<b>Diseño y configuración</b>). Para más información sobre los estilos de formularios web de Enketo, consulta <a href="https://support.kobotoolbox.org/alternative_enketo.html">Usar estilos alternativos de formularios web de Enketo</a>.
</p>

### Omitir un grupo de preguntas
Para omitir un grupo de preguntas, asegúrate de tener al menos una pregunta de control posicionada antes de las preguntas agrupadas. Haz clic en el ícono <i class="k-icon-settings"></i> **Configuración** para la pregunta agrupada, luego selecciona **Lógica de salto** y configura las condiciones de lógica de salto como lo harías para una pregunta individual.

<p class="note">
    Para aprender más sobre cómo añadir condiciones de lógica de salto, consulta <a href="https://support.kobotoolbox.org/skip_logic.html">Añadir lógica de salto en el editor de formularios</a>.
</p>

### Repetir un grupo de preguntas
Un grupo repetido permite que un conjunto de preguntas se responda múltiples veces dentro de un formulario. Por ejemplo, en una encuesta de hogares, podrías usar un grupo repetido para recolectar el nombre, edad, género y nivel educativo de cada miembro del hogar.

Para crear un grupo de preguntas:
1. Crea todas las preguntas que deseas incluir, luego agrúpalas.
2. En la <i class="k-icon-settings"></i> **Configuración** del grupo, activa la opción **Repetir este grupo si es necesario**.

![image](/images/group_repeat/repeating_groups.png)

Durante la recolección de datos, los/as encuestadores/as podrán ingresar respuestas para estas preguntas agrupadas tantas veces como sea necesario.

<p class="note">
    <b>Nota:</b> Añadir grupos repetidos a tu formulario crea una estructura de datos diferente en comparación con variables o grupos estándar. Cuando descargues tus datos en formato .xlsx, encontrarás una hoja separada para cada grupo repetido. Para más información sobre cómo exportar y usar datos de grupos repetidos, consulta <a href="https://support.kobotoolbox.org/managing_repeat_groups.html">Manejar datos de grupos repetidos</a>.
</p>

### Configuración avanzada para grupos repetidos
Configuraciones y funcionalidades adicionales para grupos repetidos están disponibles a través de XLSForm, pero no directamente dentro del editor de formularios. Estas incluyen establecer un número fijo o dinámico de repeticiones, y usar información de grupos repetidos en otras partes de tu formulario.

<p class="note">
    Para más información sobre configuración avanzada para grupos repetidos, consulta la <a href="https://docs.getodk.org/form-logic/#controlling-the-number-of-repetitions">documentación de XLSForm</a>.  
</p>