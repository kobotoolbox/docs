# Preguntas de opción múltiple en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_one_and_select_many.md" class="reference">23 Apr 2026</a>

Las preguntas de selección permiten a los encuestados **elegir entre opciones de respuesta predefinidas.** Son útiles para estandarizar respuestas, mejorar la calidad de los datos y facilitar su limpieza, análisis y comparación.

Según tus necesidades, las preguntas de selección pueden usarse para elegir una o varias opciones, confirmar una declaración, ordenar elementos por rango, calificar elementos usando una escala común, o seleccionar opciones de un archivo externo.

Este artículo describe los diferentes tipos de preguntas de selección disponibles en KoboToolbox, explica cómo agregar preguntas de selección en el Formbuilder, describe las opciones de apariencia disponibles y señala consideraciones clave al usar estos tipos de preguntas.

## Tipos de preguntas de selección

Los siguientes tipos de preguntas están disponibles en el Formbuilder para que los encuestados seleccionen opciones:

| Tipo de pregunta | Descripción |
|:---|:---|
| <i class="k-icon-qt-select-one"></i> Seleccionar una | Permite a los encuestados seleccionar una opción de una lista predefinida. |
| <i class="k-icon-qt-select-many"></i> Seleccionar varias | Permite a los encuestados seleccionar múltiples opciones de una lista predefinida. |
| <i class="k-icon-qt-ranking"></i> Clasificación | Permite a los encuestados ordenar elementos u opciones de una lista de opciones. |
| <i class="k-icon-qt-rating"></i> Calificación | Permite a los encuestados evaluar múltiples elementos usando la misma escala de respuesta. |
| <i class="k-icon-qt-acknowledge"></i> Consentimiento | Permite a los encuestados confirmar su acuerdo con una declaración. |
| <i class="k-icon-qt-select-one-from-file"></i> Seleccionar una de un archivo | Permite a los encuestados seleccionar una opción de una lista predefinida almacenada en un archivo CSV externo. |
| <i class="k-icon-qt-select-many-from-file"></i> Seleccionar varias de un archivo | Permite a los encuestados seleccionar múltiples opciones de una lista predefinida almacenada en un archivo CSV externo. |

<p class="note"> Para obtener más información sobre los tipos de preguntas Seleccionar una de un archivo y Seleccionar varias de un archivo, consulta <a href="https://support.kobotoolbox.org/es/external_file.html">Seleccionar opciones de archivos externos en el Formbuilder</a>.
</p>

## Agregar una pregunta de selección en el Formbuilder

Para agregar una pregunta de selección a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ AGREGAR PREGUNTA.**
4. Elige el tipo de pregunta adecuado.
6. Ingresa las opciones de respuesta para la pregunta de selección.

![Tipos de preguntas en el Formbuilder](images/select_one_and_select_many/select.png)

<p class="note">
    Para obtener más información sobre cómo gestionar las opciones de respuesta para preguntas de selección en el Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/question_types.html#adding-option-choices">Agregar preguntas con el Formbuilder</a>.
</p>

### Configurar preguntas de Clasificación

Las preguntas de **Clasificación** se usan para pedir a los encuestados que ordenen elementos según su preferencia, importancia o secuencia.

Después de agregar una pregunta de **Clasificación** en el Formbuilder, configura los siguientes componentes:

1. **Etiqueta de la pregunta**: La instrucción general para la tarea de clasificación, por ejemplo: "Selecciona tu primera y segunda opción en orden de preferencia."
2. **Número de rangos**: De forma predeterminada, la pregunta incluye solo una primera opción. Haz clic en el signo <i class="k-icon-plus"></i> debajo del primer rango para agregar rangos adicionales. También puedes editar la etiqueta de cada rango.
3. **Elementos a clasificar**: La lista de elementos que los encuestados ordenarán. Haz clic en el signo <i class="k-icon-plus"></i> debajo del último elemento para agregar más opciones.
4. **Mensaje de restricción**: Cada elemento solo puede seleccionarse una vez. Si un encuestado selecciona el mismo elemento más de una vez, aparece un mensaje de error que indica "Items cannot be selected more than once." Puedes editar este mensaje de error predeterminado debajo de la lista de elementos.

![Tipo de pregunta de Clasificación](images/select_one_and_select_many/ranking.png)

<p class="note">
<strong>Nota:</strong> Puedes incluir más elementos que rangos, pero el número de rangos no puede superar el número de elementos.
</p>

### Configurar preguntas de Calificación

Las preguntas de **Calificación** se usan cuando tienes múltiples preguntas de **Seleccionar una** que comparten el mismo conjunto de opciones de respuesta, como una escala de "Totalmente en desacuerdo" a "Totalmente de acuerdo."

Después de agregar una pregunta de **Calificación** en el Formbuilder, configura los siguientes componentes:

- **Etiqueta de la pregunta**: La instrucción general para el conjunto de preguntas, por ejemplo: "Califica los siguientes elementos en una escala del 1 al 5."
- **Filas**: Los elementos, afirmaciones o preguntas individuales que los encuestados calificarán. Haz clic en el signo <i class="k-icon-plus"></i> en la parte inferior de la tabla para agregar filas.
- **Columnas**: Las opciones de respuesta que conforman la escala de calificación, como "Totalmente en desacuerdo" a "Totalmente de acuerdo." Haz clic en el signo <i class="k-icon-plus"></i> a la derecha de la tabla para agregar columnas.

![Tipo de pregunta de Calificación](images/select_one_and_select_many/rating.png)

## Apariencias de las preguntas de selección

La tabla a continuación muestra las apariencias predeterminadas para los tipos de preguntas de selección:

![Apariencias de preguntas en el Formbuilder](images/select_one_and_select_many/table.png)

<p class="note">
<strong>Nota:</strong> Los tipos de preguntas <strong>Clasificación</strong> y <strong>Calificación</strong> solo están disponibles en el KoboToolbox Formbuilder. Si estás creando formularios con XLSForm, la apariencia y el comportamiento del tipo de pregunta <code>rank</code> serán diferentes a la versión del Formbuilder. Para crear una pregunta de <strong>Calificación</strong> en XLSForm, agrega preguntas de selección con las <a href="https://support.kobotoolbox.org/es/appearances_xls.html#select-question-types">apariencias</a> <code>label</code> y <code>list-nolabel</code>.
</p>

### Apariencias avanzadas

Puedes aplicar apariencias avanzadas a las preguntas de **Seleccionar una, Seleccionar varias, Seleccionar una de un archivo** y **Seleccionar varias de un archivo** para modificar cómo se muestran y se comportan en tu formulario.

Para agregar una apariencia avanzada:

1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En **Aspecto (avanzado)**, elige la apariencia deseada.
    - Si la apariencia no aparece en la lista, selecciona **other** y escribe el nombre de la apariencia en el cuadro de texto, exactamente como se indica a continuación.

![Apariencia avanzada](images/select_one_and_select_many/appearance.png)

Las siguientes apariencias avanzadas están disponibles para las preguntas de **Seleccionar una, Seleccionar varias, Seleccionar una de un archivo** y **Seleccionar varias de un archivo**:

| Apariencia | Descripción | Compatibilidad |
|:---|:---|:---|
| `minimal` | Muestra las opciones en un menú desplegable.<br>![Apariencia minimal](images/select_one_and_select_many/minimal.png) | Formularios web y KoboCollect |
| `autocomplete` | Agrega una barra de búsqueda en la parte superior de la lista de opciones.<br> ![Apariencia autocomplete](images/select_one_and_select_many/autocomplete.png) | Formularios web y KoboCollect (combinar con la apariencia `minimal`) |
| `likert` | Muestra las opciones de respuesta como una escala Likert (solo **Seleccionar una**).<br>![Escala Likert](images/select_one_and_select_many/likert.png) | Formularios web y KoboCollect |
| `compact` | Muestra las opciones una al lado de la otra con un espaciado mínimo y sin casillas de selección visibles. El número de opciones por fila puede variar según la longitud de cada etiqueta de opción.<br>![Apariencia compact](images/select_one_and_select_many/compact.png) | Formularios web y KoboCollect |
| `quick` | Avanza automáticamente el formulario a la siguiente pregunta después de seleccionar una respuesta (solo **Seleccionar una**). | Solo KoboCollect |
| `quickcompact` | Muestra las opciones una al lado de la otra con un espaciado mínimo y sin casillas de selección, y avanza automáticamente a la siguiente pregunta después de seleccionar una respuesta (solo **Seleccionar una**). <br>![Apariencia quick compact](images/select_one_and_select_many/compact.png) | Solo KoboCollect |
| `horizontal` | Muestra las opciones en columnas de tamaño uniforme, con el mismo número de opciones en cada fila. <br>![Apariencia horizontal](images/select_one_and_select_many/horizontal_columns.png) | Solo formularios web. Usa `columns` para compatibilidad con KoboCollect. |
| `columns` (other) | Muestra las opciones en columnas de tamaño uniforme, con el mismo número de opciones en cada fila.<br>![Apariencia columns other](images/select_one_and_select_many/horizontal_columns.png) | Formularios web y KoboCollect. |
| `horizontal-compact` | Muestra las opciones en columnas con casillas de selección visibles. El número de columnas puede variar por fila según la longitud de cada etiqueta de opción.<br>![Apariencia horizontal compact](images/select_one_and_select_many/horizontal-compact_columns-pack.png) | Solo formularios web. Usa `columns-pack` para compatibilidad con KoboCollect. |
| `columns-pack` (other) | Muestra las opciones en columnas con casillas de selección visibles. El número de columnas puede variar por fila según la longitud de cada etiqueta de opción.<br>![Apariencia columns pack](images/select_one_and_select_many/horizontal-compact_columns-pack.png) | Formularios web y KoboCollect |
| `columns-n` (other) | Muestra las opciones disponibles en el número (n) de columnas especificado.<br>![Apariencia columns-n](images/select_one_and_select_many/columns_n.png) | Formularios web y KoboCollect |
| `label` | Muestra las etiquetas de las opciones sin las casillas de selección. | Formularios web y KoboCollect |
| `list-nolabel` | Muestra las casillas de selección de las opciones sin las etiquetas. | Formularios web y KoboCollect |

## Buenas prácticas para el uso de preguntas de selección

Las siguientes recomendaciones destacan consideraciones importantes al usar preguntas de selección en tu formulario.

### Preguntas de Consentimiento

El tipo de pregunta **Consentimiento** permite a los encuestados indicar su acuerdo con una declaración mediante una única casilla de verificación. Sin embargo, este tipo de pregunta no distingue entre los encuestados que activamente están en desacuerdo y los que omiten la pregunta, lo que puede afectar la calidad de los datos. Además, la etiqueta predeterminada de la opción de Consentimiento no se puede editar.

Si necesitas más flexibilidad para etiquetar las opciones de respuesta, o si quieres incluir una opción clara de "No", usa una pregunta de **Seleccionar una** en su lugar.

### Definir valores XML para las opciones

Se recomienda definir los valores XML para todas las opciones en las preguntas de selección antes de implementar el formulario. Los valores XML garantizan la consistencia en tu conjunto de datos y evitan problemas durante la exportación y el análisis.

<p class="note"> Para obtener más información sobre cómo definir valores XML, consulta <a href="https://support.kobotoolbox.org/es/question_types.html#setting-xml-values-for-option-choices">Agregar preguntas con el Formbuilder</a>.
</p>

### Agregar una respuesta "Otro, especificar"

Si las opciones predefinidas no cubren todas las respuestas posibles, puedes agregar una opción "Otro" seguida de una [pregunta de Texto](https://support.kobotoolbox.org/es/text_questions.html) que permita a los encuestados especificar su respuesta. Usa la lógica de omisión para mostrar la pregunta de Texto solo cuando se seleccione la opción "Otro".

<p class="note">
    Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/skip_logic.html#">Añadir lógica de salto al Formbuilder</a>.
</p>

### Aleatorizar las opciones de respuesta

Para las preguntas de **Seleccionar una** y **Seleccionar varias**, puedes aleatorizar el orden de las opciones de respuesta yendo a **Configuración > Opciones de pregunta > Parámetros** de la pregunta y seleccionando **randomize.**

También puedes establecer una **semilla** (seed), lo que garantiza que la aleatorización siga un patrón consistente. Usar una semilla permite reproducir el mismo orden aleatorizado cuando sea necesario, por ejemplo al revisar envíos o probar el formulario, mientras se reduce el sesgo de orden durante la recolección de datos.

<p class="note">
    Para obtener más información sobre las opciones de preguntas, consulta <a href="https://support.kobotoolbox.org/es/question_options.html">Opciones de preguntas en el Formbuilder</a>.
</p>

### Opciones de exportación para preguntas de Seleccionar varias

Al exportar datos de preguntas de **Seleccionar varias**, puedes elegir cómo se estructuran las respuestas en tu conjunto de datos. Puedes optar por:

- Exportar todas las opciones seleccionadas en una sola columna
- Exportar cada opción como una columna separada
- Exportar ambos formatos

<p class="note">
    Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/advanced_export.html#export-options-for-multiple-select-questions">Opciones avanzadas para la exportación de datos</a>.
</p>