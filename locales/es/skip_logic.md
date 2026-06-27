# Añadir lógica de salto al Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/e562a3b12a843642706dec4700529f57fee501f5/source/skip_logic.md" class="reference">5 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/uLSnoG0mqV4?si=63o4YeQUZWOsZmfF&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La lógica de omisión, también conocida como ramificación o condiciones de relevancia, controla qué preguntas se muestran en un formulario. De forma predeterminada, todas las preguntas son visibles. La lógica de omisión determina bajo qué condición o condiciones debe aparecer una pregunta. Las condiciones de lógica de omisión siempre se aplican a la pregunta o grupo que debe mostrarse de forma condicional.

<p class="note">
    <strong>Nota:</strong> Puedes aplicar lógica de omisión a <a href="group_repeat.html">grupos de preguntas</a> completos, así como a preguntas individuales. Esto puede simplificar la lógica del formulario y facilitar la gestión de cuestionarios complejos.
</p>

Hay dos métodos para agregar lógica de omisión en el Formbuilder: agregar una condición mediante el **generador de lógica de omisión**, o ingresar manualmente la lógica de omisión en **código XLSForm**.

## Agregar una condición

Este primer método te permite usar el generador de lógica de omisión para agregar tus condiciones. Se recomienda para principiantes. Para agregar una condición de lógica de omisión, sigue estos pasos:

1. Abre <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta o grupo que se mostrará de forma condicional.
2. Selecciona **Lógica de omisión** y haz clic en **Añadir una condición**.
3. Selecciona la pregunta del formulario que determinará si la pregunta actual se muestra o no.
4. Elige el operador lógico adecuado para tu condición (por ejemplo, >, =, !=).
5. En el campo **valor de la respuesta**, selecciona o escribe la respuesta que se requiere para que se cumpla la condición.

La pregunta se mostrará únicamente cuando se cumpla la condición especificada.

Para agregar múltiples condiciones, agrega tu primera condición y luego haz clic en el botón **Añadir otra condición**. Cuando uses múltiples condiciones, especifica si se debe cumplir al menos una de ellas o todas.

<p class="note">
    <strong>Nota:</strong> Puedes eliminar las condiciones de lógica de omisión haciendo clic en el <i class="k-icon-trash"></i> ícono de papelera.
</p>

## Ingresar manualmente la lógica de omisión en código XLSForm

Para usuarios avanzados, la lógica de omisión se puede ingresar directamente en código XLSForm. La estructura básica de las condiciones no cambia: deberás identificar la pregunta de control, elegir un operador lógico e ingresar el valor de respuesta requerido.

Para ingresar manualmente la lógica de omisión en código XLSForm, sigue estos pasos:

1. Abre <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta o grupo que se mostrará de forma condicional.
2. Selecciona **Lógica de omisión** y haz clic en **Ingresar manualmente la lógica de omisión en el código XLSForm**.
3. Ingresa la condición en código XLSForm.

En código XLSForm, las preguntas se identifican por su **nombre de pregunta** (nombre de columna de datos) usando el formato `${question_name}`. Por ejemplo, si Q2 debe mostrarse solo si la respuesta a Q1 es "Sí", la condición de lógica de omisión para Q2 sería `${Q1} = 'yes'`.

<p class="note">
    Para obtener más información sobre el código XLSForm y los operadores, consulta <a href="https://support.kobotoolbox.org/es/form_logic.html">Introducción a la lógica de formularios en el Formbuilder</a>.
</p>