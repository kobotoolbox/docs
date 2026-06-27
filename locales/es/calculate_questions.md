# Agregar cálculos con el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/calculate_questions.md" class="reference">20 Mar 2026</a>

Los cálculos permiten derivar nuevas variables, crear lógica avanzada de formularios y mostrar resultados a los encuestados durante la recolección de datos. El tipo de pregunta **Cálculo** realiza operaciones matemáticas utilizando los valores ingresados en preguntas anteriores. Por defecto, el resultado está oculto, pero puede mostrarse en el formulario si es necesario.

Los cálculos se procesan dentro del formulario, lo que puede reducir la necesidad de manipular los datos después de la recolección. Los resultados se almacenan como nuevas variables en el conjunto de datos y pueden utilizarse en todo el formulario para aplicar [lógica de omisión](https://support.kobotoolbox.org/es/skip_logic.html), definir [criterios de validación](https://support.kobotoolbox.org/es/validation_criteria.html) o mostrar [contenido dinámico](https://support.kobotoolbox.org/es/form_logic.html#question-referencing) en etiquetas de preguntas y notas.

Este artículo explica cómo agregar cálculos en el Formbuilder, abarcando operaciones aritméticas básicas e introduciendo expresiones más avanzadas.

## Agregar cálculos con el Formbuilder

Para agregar un cálculo a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la expresión de cálculo en lugar de la etiqueta de la pregunta.
3. Haz clic en **+ AGREGAR PREGUNTA**.
4. Elige el tipo de pregunta <i class="k-icon-qt-calculate"></i> **Cálculo**.

![Pregunta de cálculo](images/calculate_questions/calculate.png)

Las expresiones de cálculo se construyen combinando referencias a preguntas, operadores matemáticos, funciones y constantes. Por ejemplo:
* `${usd_cost} * 0.87` convierte el valor ingresado en la pregunta `usd_cost` a otra moneda utilizando un tipo de cambio fijo.
* `${total_cost} div ${units_purchased}` divide el costo total entre el número de unidades compradas para calcular el costo unitario.

<p class="note">
Para obtener más información sobre cada uno de estos componentes, consulta <a href="https://support.kobotoolbox.org/es/form_logic.html">Introducción a la lógica de formularios en el Formbuilder</a>.
</p>

Para mostrar el resultado del cálculo en una nota, usa el formato de [referencia a preguntas](https://support.kobotoolbox.org/es/form_logic.html#question-referencing) `${nombre_de_columna_de_datos}`, reemplazando `nombre_de_columna_de_datos` con el [nombre de columna de datos](https://support.kobotoolbox.org/es/question_options.html#data-column-name) de la pregunta de Cálculo. También puedes usar este formato para referenciar el resultado del cálculo en la etiqueta de una pregunta o en la lógica de tu formulario.

![Referencia a pregunta](images/calculate_questions/reference.png)

## Cálculos aritméticos

Los cálculos pueden ir desde operaciones aritméticas simples hasta la derivación avanzada de variables.

Los cálculos aritméticos te permiten realizar operaciones básicas utilizando los siguientes **operadores**:

| Operador | Descripción |
|:---------:|:------------|
| <strong>+</strong>        | suma |
| <strong>-</strong>        | resta |
| <strong>*</strong>        | multiplicación |
| <strong>div</strong>      | división |
| <strong>mod</strong>      | módulo (calcula el resto de una división) |

Los cálculos en XLSForm siguen la regla **BODMAS** para el orden de las operaciones matemáticas: **P**aréntesis, **P**otencias, **D**ivisión, **M**ultiplicación, **A**dición y **S**ustracción. Esto significa que los cálculos dentro de paréntesis se realizan primero, seguidos de las potencias, luego las divisiones, multiplicaciones, y así sucesivamente. Usar los paréntesis correctamente garantiza que tus cálculos funcionen como se espera.

## Cálculos avanzados

Los cálculos avanzados en KoboToolbox suelen basarse en **funciones** y **expresiones regulares** para hacer los cálculos más eficientes.

- Las **funciones** son [operaciones predefinidas](https://support.kobotoolbox.org/es/functions_xls.html) que se utilizan para realizar automáticamente tareas complejas como redondear valores, calcular potencias o extraer la fecha actual.
- Las **expresiones regulares (regex)** son [patrones de búsqueda](https://support.kobotoolbox.org/es/restrict_responses.html) que se utilizan para identificar caracteres específicos dentro de una cadena de texto.

<p class="note">
  Para ver ejemplos de cálculos avanzados que puedes usar en tus formularios y sugerencias para la resolución de problemas, consulta <a href="https://support.kobotoolbox.org/es/calculations_xls.html#advanced-calculations">Agregar cálculos a un XLSForm</a>.
</p>