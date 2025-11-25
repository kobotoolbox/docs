# Agregar lógica de salto en el editor de formularios de KoboToolbox (Formbuilder)
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/0d832566f7fb9d5e452c73468e52ec242eac992f/source/skip_logic.md" class="reference">30 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/uLSnoG0mqV4?si=63o4YeQUZWOsZmfF" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La lógica de salto, también conocida como ramificación o condiciones de relevancia, controla qué preguntas se muestran en un formulario. De forma predeterminada, todas las preguntas son visibles. La lógica de salto determina bajo qué condición(es) debe aparecer una pregunta. Las condiciones de lógica de salto siempre se aplican a la pregunta o grupo que debe ser visible condicionalmente.

<p class="note">
    <strong>Nota:</strong> Puedes aplicar lógica de salto a <a href="group_repeat.html">grupos de preguntas</a> completos, así como a preguntas individuales. Esto puede simplificar la lógica del formulario y facilitar el manejo de cuestionarios complejos.
</p>

Hay dos métodos para agregar lógica de salto en el editor de formularios: agregar una condición a través del **constructor de lógica de salto**, o ingresar manualmente la lógica de salto en **código XLSForm**.

## Agregar una condición

Este primer método te permite usar el constructor de lógica de salto para agregar tus condiciones. Se recomienda para principiantes. Para agregar una condición de lógica de salto, sigue estos pasos:

1. Abre la <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta o grupo que se mostrará condicionalmente.
2. Selecciona **Lógica de salto** y haz clic en **Agregar una condición**.
3. Selecciona la pregunta en el formulario que determinará si la pregunta actual se muestra o no.
4. Elige el operador lógico apropiado para tu condición (por ejemplo, >, =, !=).
5. En el campo **valor de respuesta**, selecciona o escribe la respuesta que se requiere para que se cumpla la condición.

La pregunta se mostrará solo cuando se cumpla la condición especificada.

Para agregar múltiples condiciones, agrega tu primera condición y luego haz clic en el botón **Agregar otra condición**. Cuando uses múltiples condiciones, especifica si al menos una de estas condiciones debe cumplirse o todas ellas.

<p class="note">
    <strong>Nota:</strong> Puedes eliminar condiciones de lógica de salto haciendo clic en el <i class="k-icon-trash"></i> ícono de papelera.
</p>

## Ingresar manualmente la lógica de salto en código XLSForm
Para usuarios/as avanzados/as, la lógica de salto se puede ingresar directamente en código XLSForm. La estructura básica de las condiciones permanece sin cambios: necesitarás identificar la pregunta de control, elegir un operador lógico y escribir el valor de respuesta requerido.

Para ingresar manualmente la lógica de salto en código XLSForm, sigue estos pasos:
1. Abre la <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta o grupo que se mostrará condicionalmente.
2. Selecciona **Lógica de salto** y haz clic en **Ingresar manualmente tu lógica de salto en código XLSForm**.
3. Ingresa la condición en código XLSForm.

En código XLSForm, las preguntas se identifican por su **nombre de pregunta** (Nombre de columna de datos) usando el formato `${nombre_pregunta}`. Por ejemplo, si P2 debe preguntarse solo si la respuesta a P1 es "Sí", la condición de lógica de salto para P2 sería `${P1} = 'sí'`.

<p class="note">
    Para obtener más información sobre el código XLSForm y los operadores, consulta la <a href="https://xlsform.org/en/#relevant">documentación de XLSForm</a>.
</p>