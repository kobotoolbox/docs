# Importar una colección con XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/import_collection.md" class="reference">20 Mar 2026</a>

Una **colección** es un grupo de preguntas, bloques de preguntas y plantillas relacionadas, organizadas en tu [biblioteca de KoboToolbox](https://support.kobotoolbox.org/es/question_library.html). Las colecciones te ayudan a gestionar contenido reutilizable por proyecto, tema, país u organización.

Puedes importar varias preguntas o bloques de preguntas a la vez como una colección usando un [XLSForm](https://support.kobotoolbox.org/es/getting_started_xlsform.html). Este enfoque es útil cuando preparas conjuntos de preguntas estandarizadas fuera del Formbuilder de KoboToolbox o cuando migras contenido XLSForm existente a tu biblioteca.

Este artículo explica cómo estructurar y cargar un XLSForm para que se importe como una colección.

## Configurar tu XLSForm

Para que tu XLSForm se importe correctamente en la biblioteca de preguntas de KoboToolbox, debe seguir una estructura específica. Una vez que tengas un [XLSForm funcional](https://support.kobotoolbox.org/es/getting_started_xlsform.html), puedes adaptarlo para que funcione como una colección modificando su estructura:

1. **Renombra la hoja principal:** Reemplaza la **hoja survey** estándar por una hoja llamada `library`.
    - Esta hoja debe contener las mismas columnas que normalmente incluirías en una hoja survey, como `type`, `name`, `label`, [columnas de etiquetas traducidas](https://support.kobotoolbox.org/es/language_xls.html) y cualquier [opción de pregunta](https://support.kobotoolbox.org/es/question_options_xls.html) relevante.
2. **Incluye preguntas individuales o grupos de preguntas:** Puedes incluir preguntas independientes o grupos de preguntas completos en la hoja `library`.
3. **Define bloques de preguntas usando una columna `block`:** Añade una columna llamada `block` para agrupar preguntas relacionadas en un bloque de preguntas.
    - Ingresa el mismo título de bloque en cada fila que pertenezca a ese bloque.
    - Cualquier fila sin valor en la columna `block` se importará como una pregunta individual.
4. **Añade etiquetas (opcional):** Para asignar etiquetas a una pregunta o bloque, añade una columna con el formato `tag:[nombre de la etiqueta]` (por ejemplo, `tag:wash`).
    - Ingresa `1` en cada fila que deba recibir la etiqueta.
    - Dentro de los bloques, es suficiente marcar solo una fila del bloque, aunque marcar varias filas no causará problemas.

<p class="note">
  Para ver un ejemplo de la estructura requerida, consulta este <a href="https://support.kobotoolbox.org/_static/files/question_library/collection_import_sample.xlsx">XLSForm de ejemplo</a>.
</p>

## Cargar tu XLSForm

Una vez que tu XLSForm esté estructurado correctamente como una colección, puedes cargarlo en tu biblioteca de KoboToolbox.

Para cargar tu XLSForm:

1. Inicia sesión en tu cuenta de KoboToolbox.
2. Haz clic en <i class="k-icon-library"></i> **Library** en el menú de la izquierda para abrir la biblioteca.
3. Haz clic en **NEW** en la esquina superior izquierda.
4. Selecciona <i class="k-icon-upload"></i> **Upload** e importa tu XLSForm. Haz clic en **Upload**.

El archivo se importará como una colección en tu biblioteca de preguntas.

<p class="note">
  Para obtener más información sobre la biblioteca de KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/question_library.html">Usar la biblioteca de preguntas de KoboToolbox</a>.
</p>

## Consideraciones adicionales

### Grupos dentro de bloques

Puedes incluir filas `begin_group` y `end_group` dentro de un bloque. Asegúrate de que la fila `begin_group` tenga un valor `name` único, como se requiere en la estructura estándar de XLSForm. Las filas de apertura y cierre del grupo deben estar incluidas dentro del mismo bloque.

Usar el nombre del bloque como etiqueta del grupo puede ayudar a mantener la claridad después de la importación.

<p class="note">
  Para obtener más información sobre los grupos de preguntas en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/grouping_questions_xls.html">Grupos de preguntas en XLSForm</a>.
</p>

### Lógica de omisión y reglas de validación

Puedes incluir lógica de relevancia, restricciones y otra lógica de formulario en tu XLSForm. Estas configuraciones se conservarán durante la importación, lo cual es útil cuando reutilizas bloques de preguntas complejos sin tener que reconstruir la lógica avanzada.

<p class="note">
Para obtener más información sobre la lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

### Múltiples idiomas

Puedes incluir traducciones usando la sintaxis estándar de XLSForm, como `label::English (en)` o `label::Español (es)`. Las etiquetas traducidas y las etiquetas de opciones de respuesta se importarán junto con el bloque.

<p class="note">
  Para obtener más información sobre cómo añadir traducciones en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/language_xls.html#">Añadir traducciones en XLSForm</a>.
</p>