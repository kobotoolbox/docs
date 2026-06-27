# Agregar una matriz de preguntas usando el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/matrix_response.md" class="reference">23 Apr 2026</a>

El tipo de pregunta **Matriz de preguntas** te permite crear una tabla estructurada de preguntas, donde cada columna representa una pregunta y cada fila representa un elemento. En lugar de crear múltiples preguntas por separado, puedes agruparlas en una sola matriz para que tu formulario sea más organizado y eficiente para la recolección de datos.

Este artículo explica cómo agregar y configurar una matriz de preguntas en el Formbuilder, cómo se muestra durante la recolección de datos y cómo aplicar lógica avanzada usando XLSForm cuando sea necesario.

<p class="note">
<strong>Nota:</strong> Las matrices de preguntas solo son compatibles con los <a href="https://support.kobotoolbox.org/es/data_through_webforms.html">formularios web</a> con el tema <a href="https://support.kobotoolbox.org/es/alternative_enketo.html">Grid</a> activado. No son compatibles con KoboCollect.
</p>

## Agregar una matriz de preguntas en el Formbuilder

Para agregar una matriz de preguntas a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa una instrucción general como etiqueta de la pregunta.
3. Haz clic en **+ AGREGAR PREGUNTA.**
4. Elige el tipo de pregunta <i class="k-icon-qt-question-matrix"></i> **Matriz de preguntas**.

![Matriz de preguntas](images/matrix_response/matrix.png)

### Configurar la matriz de preguntas

En tu matriz de preguntas:

- Cada **columna** representa una pregunta independiente que se repetirá para cada elemento de las filas.
- Cada **fila** representa un elemento sobre el que se harán las preguntas de las columnas.

![Ejemplo de matriz de preguntas](images/matrix_response/example.png)

Para configurar tu matriz de preguntas, en cada columna:

1. Haz clic en el icono <i class="k-icon-settings"></i> **Configuración**.
2. Selecciona el **Tipo de respuesta.**
    - Los tipos disponibles incluyen **Seleccionar una**, **Seleccionar varias**, **Texto** y **Número.**
    - Puedes usar diferentes tipos de pregunta dentro de la misma matriz.
3. Ingresa una **Etiqueta de pregunta.**
4. Ingresa un **Sufijo de columna de datos.** Este sufijo se añadirá a los nombres de variable de cada elemento de las filas y debe seguir las [reglas estándar para nombres de columnas de datos](https://support.kobotoolbox.org/es/question_options.html#important-considerations-for-data-column-names).
5. Si usas **Seleccionar una** o **Seleccionar varias**, agrega las opciones de respuesta y sus [valores XML](https://support.kobotoolbox.org/es/question_types.html#setting-xml-values-for-option-choices).
6. Configura la pregunta como [obligatoria](https://support.kobotoolbox.org/es/question_options.html#mandatory-response), si es necesario.
7. Para agregar otra columna, haz clic en el icono <i class="k-icon-plus"></i> a la derecha de la última columna.

<p class="note">
<strong>Nota:</strong> Puedes agregar hasta 12 columnas a una matriz de preguntas. Sin embargo, cada columna adicional reduce el ancho disponible para las demás, lo que puede afectar la legibilidad en pantallas más pequeñas.
</p>

Para configurar cada fila:

1. Haz clic en el icono <i class="k-icon-settings"></i> **Configuración**.
2. Ingresa una **Etiqueta** para el elemento.
3. Ingresa un **Prefijo de columna de datos.** Este prefijo se añadirá a los nombres de variable de todas las preguntas de columna relacionadas con este elemento y debe seguir las [reglas estándar para nombres de columnas de datos](https://support.kobotoolbox.org/es/question_options.html#important-considerations-for-data-column-names).
4. Para agregar otra fila, haz clic en el icono <i class="k-icon-plus"></i> debajo de la última fila.

## Recolectar datos con una matriz de preguntas

Las matrices de preguntas solo son compatibles con formularios web y requieren que el tema [Grid](https://support.kobotoolbox.org/es/alternative_enketo.html) esté activado. No son compatibles con KoboCollect.

La matriz de preguntas se muestra como una tabla, donde cada columna representa una pregunta y cada fila representa un elemento.

![Matriz de preguntas](images/matrix_response/enketo.png)

<p class="note">
<strong>Nota:</strong> Al exportar datos o ver envíos en la tabla de datos, las variables de la matriz de preguntas se convierten a la estructura estándar de XLSForm. Cada celda de la matriz se convierte en una variable individual, y los nombres de variable finales se crean combinando el <strong>prefijo de columna de datos</strong> de la fila y el <strong>sufijo de columna de datos</strong> de la columna. Como resultado, los nombres de variable exportados pueden diferir ligeramente de cómo aparece la matriz en el Formbuilder.
</p>

## Matrices de preguntas avanzadas

No es posible agregar criterios de validación, cálculos ni ciertas opciones avanzadas de preguntas, como repetir una matriz de preguntas o definir un mensaje de restricción personalizado, directamente en una matriz de preguntas **usando el Formbuilder.**

Para aplicar estas configuraciones, [descarga tu formulario](https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) como XLSForm y agrega [restricciones](https://support.kobotoolbox.org/es/constraints_xls.html), [cálculos](https://support.kobotoolbox.org/es/calculations_xls.html) y otras [opciones de preguntas](https://support.kobotoolbox.org/es/question_options_xls.html) directamente en el XLSForm.

<p class="note">
Para ver un ejemplo de cómo agregar restricciones y cálculos a una matriz de preguntas, consulta este <a href="https://support.kobotoolbox.org/_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx">XLSForm de ejemplo</a>. Para ver un ejemplo de cómo repetir una matriz de preguntas como grupo de repetición, consulta este <a href="https://support.kobotoolbox.org/_static/files/calculations_constraints_matrix/repeating_matrix_question.xlsx">XLSForm de ejemplo</a>.
</p>

### Agregar lógica de omisión a una matriz de preguntas

De igual manera, no es posible agregar lógica de omisión directamente a una matriz de preguntas en el Formbuilder. Sin embargo, puedes [descargar tu formulario](https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) como XLSForm y agregar la lógica de omisión directamente en el XLSForm.

Al exportar a XLSForm, una matriz de preguntas se estructura como un grupo de preguntas usando [valores w](https://support.kobotoolbox.org/es/form_style_xls.html#setting-up-an-xlsform-for-theme-grid) del tema Grid. Puedes [aplicar lógica de omisión](https://support.kobotoolbox.org/es/skip_logic_xls.html) a toda la matriz añadiéndola al grupo completo, o aplicarla a filas individuales dentro de la matriz.

Ten en cuenta que agregar lógica de omisión a celdas individuales puede afectar el diseño visual de la matriz, ya que las preguntas ocultas pueden alterar la estructura de la tabla. Para preservar el formato, considera agregar preguntas de tipo **Nota** con lógica de omisión que muestren un mensaje en lugar de la pregunta oculta, como se hace en este [XLSForm de ejemplo](https://support.kobotoolbox.org/_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls). Este enfoque mantiene el diseño de la matriz y evita la entrada de datos en celdas específicas.

![Lógica de omisión en una matriz de preguntas](images/matrix_response/skip_matrix.png)