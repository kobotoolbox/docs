# Tipo de pregunta Cálculo avanzado

Algunos formularios avanzados pueden requerir que se realice un cálculo interno como parte del formulario (en lugar de hacerlo después durante el análisis). Esto se puede hacer agregando un **Cálculo** y escribiendo la expresión matemática en el campo de etiqueta de la pregunta.

Este artículo proporciona instrucciones paso a paso sobre cómo agregar cálculos usando el editor de formularios de KoboToolbox **(Formbuilder)** o descargando el formulario y agregándolos directamente al XLSForm.

Para ver una lista completa y detallada de todas las funciones, visita la excelente [documentación de funciones XPath de ODK](https://getodk.github.io/xforms-spec).

## Métodos para agregar preguntas de cálculo:

### Usando el Formbuilder

Paso 1: Agrega una pregunta de tipo Cálculo.

![image](/images/advanced_calculate/calculate_question.jpg)

Paso 2: Escribe la fórmula de cálculo donde normalmente escribirías tu pregunta.

![image](/images/advanced_calculate/formulas.jpg)

Nota:

* Tu pregunta de cálculo no se mostrará durante la recolección de datos, ya sea en KoboCollect o en Enketo. Sin embargo, sí aparecerá al visualizar los datos en la vista de tabla o en la versión descargada.
* Debes seguir reglas similares a las de los XLSForms (consulta la sección de reglas a continuación).

### Usando XLSForms

Recomendamos este método cuando se trabaja con funciones de cálculo más avanzadas.

Los XLSForms permiten usar la función de cálculo en diferentes tipos de preguntas.

* Puedes imitar el método usado en el Formbuilder, donde la pregunta no se mostrará durante la recolección de datos, simplemente definiendo el tipo de pregunta como `calculate` y escribiendo tu cálculo en la columna `calculate`.
* Puedes usar `calculate` para diferentes tipos de preguntas; en ese caso, la pregunta sí se mostrará durante la recolección de datos. Puedes configurar esa pregunta como de solo lectura para que nadie pueda modificar el valor. Los tipos de preguntas que hemos probado con este método incluyen:

    a. `integer` (solo acepta funciones de cálculo numéricas)
    b. `text` (solo acepta funciones de cálculo de cadenas de texto)
    c. `note` (solo acepta referencias a preguntas, no funciones de cálculo)
    d. `date` (solo acepta funciones de cálculo de fechas)
    e. `time` (solo acepta funciones de cálculo de hora)

    ![image](/images/advanced_calculate/xls.png)

## Reglas al trabajar con preguntas de cálculo:

### Estas reglas aplican tanto al Formbuilder como a los XLSForms

1. No puedes usar cálculos numéricos y de cadenas de texto dentro de la misma pregunta.
2. Los cálculos numéricos seguirán la regla BODMAS para aplicar las operaciones, es decir, el orden de ejecución será: Paréntesis, Divisiones, Multiplicaciones, Adiciones y luego Sustracciones (ten siempre esto en cuenta al ordenar las preguntas).
3. Las preguntas de cálculo que hacen referencia a otras preguntas no deben colocarse en el mismo grupo que las preguntas referenciadas, ya que el cálculo no aparecerá hasta que salgas del grupo.
4. Cuando hagas referencia a una pregunta en un cálculo, debes indicarla como `${Pregunta}`, donde `Pregunta` es el nombre de la pregunta.
5. Puedes "forzar" la evaluación de un cálculo configurando `required` como `TRUE`.

### Lista de funciones de cálculo probadas

_(No dudes en sugerir funciones adicionales y las agregaremos)_

![image](/images/advanced_calculate/list.png)

### Uso del comando IF en cálculos

![image](/images/advanced_calculate/if_command.png)

### Soluciones alternativas para cálculos

_Recomendadas para usuarios avanzados_

#### Solución alternativa 1: Crear preguntas ficticias para calcular la puntuación final en una serie de preguntas

Supongamos que tienes una pregunta como `QN1 ¿Tienes una pregunta?` con respuestas `Sí=1 No=2 No sé=999`.

En este caso, puede que quieras crear una pregunta ficticia QN1 justo después de QN1 para tener en cuenta las diferencias en la codificación y definir el equivalente matemático. Para ello, crearás una pregunta de cálculo QN1d (_nota: esta es mi propia convención de nombres; la "d" significa "dummy" o ficticia_) y definirás el valor predeterminado como 0, pero escribirás la fórmula como **If(${QN1}=1,1,0)**.

Como se puede ver en el formulario de prueba, se logró crear esta situación y los datos aparecen codificados para QN1 y calculados con su significado matemático para QN1d. Este debe ser el significado que tu puntuación pretende expresar. _Puedes hacer esto para cálculos como índices de riqueza, donde Sí y No pueden tener valores diferentes según el país._

Una vez que hagas esto para todas tus preguntas, puedes agregar una pregunta de cálculo que sume todos los valores ficticios de la siguiente manera:

`${QN1d}+${QN2d}+ etc`