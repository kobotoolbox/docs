# Agregar cálculos a un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/calculations_xls.md" class="reference">23 Apr 2026</a>

Los cálculos se pueden usar dentro de tu formulario para derivar nuevas variables, crear lógica de formulario avanzada y mostrar resultados a los encuestados durante la recolección de datos.

Los cálculos se procesan dentro del formulario, lo que ayuda a ahorrar tiempo durante el análisis de datos. Los resultados se almacenan como nuevas columnas en el conjunto de datos final y se pueden usar en todo el formulario para aplicar [lógica de omisión](https://support.kobotoolbox.org/es/skip_logic_xls.html), establecer [restricciones](https://support.kobotoolbox.org/es/constraints_xls.html) o mostrar [contenido dinámico](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing) en etiquetas de preguntas y notas.

Este artículo explica cómo agregar cálculos en un XLSForm, abarcando tanto la aritmética básica como las expresiones más avanzadas.

<p class="note">
<strong>Nota:</strong> Este artículo se centra en agregar cálculos en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agregar cálculos en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/calculate_questions.html">Agregar cálculos con el Formbuilder</a>.
<br><br>
Para practicar con cálculos en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar cálculos en un XLSForm

Las expresiones de cálculo se construyen usando una combinación de [referencias a preguntas](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing), [operadores matemáticos](https://support.kobotoolbox.org/es/form_logic_xls.html#mathematical-and-comparison-operators), [funciones](https://support.kobotoolbox.org/es/functions_xls.html) y constantes.

Para agregar un cálculo en tu XLSForm:
1. En la columna `type` de la **hoja survey**, ingresa `calculate` para agregar un tipo de pregunta de cálculo.
2. Ingresa un `name` para la pregunta `calculate`.
    - Como el cálculo no se muestra en el formulario, la pregunta `calculate` **no requiere una etiqueta**.
3. Agrega una columna `calculation` en la **hoja survey**.
4. En la columna `calculation`, ingresa la **expresión de cálculo.**
    - Los cálculos pueden ir desde [cálculos aritméticos básicos](https://support.kobotoolbox.org/es/calculations_xls.html#arithmetic-calculations) hasta [cálculos avanzados](https://support.kobotoolbox.org/es/calculations_xls.html#advanced-calculations) que usan funciones y expresiones regulares.

Para hacer referencia al resultado del cálculo en el resto del formulario (por ejemplo, dentro de una pregunta de tipo nota, en la etiqueta de una pregunta o en la lógica del formulario), usa el formato de [referencia a preguntas](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing) `${question_name}`, donde `question_name` es el nombre de la pregunta `calculate`.

**hoja survey**

| type      | name          | label                          | calculation           |
|:----------|:--------------|:-------------------------------|:----------------------|
| integer   | bags          | Total number of bags sold       |                       |
| decimal   | price         | Price per bag                   |                       |
| calculate | total_amount  |                                | ${bags} * ${price}    |
| note      | display_total | The total is ${total_amount}    |                       |
| survey | 

## Cálculos aritméticos

Los cálculos en XLSForm pueden ir desde cálculos aritméticos simples hasta la derivación avanzada de variables.

Los cálculos aritméticos permiten realizar operaciones básicas usando los siguientes **operadores**:

| Operador | Descripción |
|:----------|:-------------|
| <strong>+</strong>   | Suma |
| <strong>-</strong>   | Resta |
| <strong>*</strong>   | Multiplicación |
| <strong>div</strong> | División |
| <strong>mod</strong> | Módulo (calcula el resto de una división) |

Los cálculos en XLSForm siguen la regla **BODMAS** para el orden de las operaciones matemáticas: **P**aréntesis, **P**otencias, **D**ivisión, **M**ultiplicación, **A**dición y **S**ustracción. Esto significa que los cálculos dentro de paréntesis se realizan primero, seguidos de las potencias, luego las divisiones, multiplicaciones, y así sucesivamente. Usar los paréntesis correctamente garantiza que los cálculos funcionen como se espera.

## Cálculos avanzados

Los cálculos avanzados en XLSForm suelen basarse en **funciones** y **expresiones regulares** para hacer los cálculos más eficientes.
* Las **funciones** son operaciones predefinidas que se usan para realizar automáticamente tareas complejas, como redondear valores, calcular potencias o extraer la fecha actual.
* Las **expresiones regulares (regex)** son patrones de búsqueda que se usan para encontrar caracteres específicos dentro de una cadena de texto.

<p class="note">
  Para una lista completa de las funciones disponibles en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/functions_xls.html">Usar funciones en XLSForm</a>. Para aprender más sobre las expresiones regulares, consulta <a href="https://support.kobotoolbox.org/es/restrict_responses.html">Usar expresiones regulares en XLSForm</a>.
</p>

Algunos ejemplos de cálculos más avanzados incluyen:

| Cálculo | Descripción |
|:-------------|:-------------|
| `int((today()-${DOB}) div 365.25)` | Calcular la edad a partir de la fecha de nacimiento. |
| `int(today()-${date})` | Calcular los días transcurridos desde una fecha. |
| `format-date(${date}, '%b')` | Devolver solo el mes de una fecha. |
| `concat(${first}, " ", ${middle}, " ", ${last})` | Crear una cadena de texto con el nombre completo del encuestado. |
| `jr:choice-name(${question1}, '${question1}')` | Devolver la etiqueta de una opción, en el idioma actual, desde la lista de opciones. |
| `translate(${full_name}, "ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "abcdefghijklmnopqrstuvwxyz_")` | Convertir letras mayúsculas a minúsculas y espacios en guiones bajos. |
| `substr(${question}, 1, 2)` | Conservar solo la primera letra o número de una cadena de texto. |
| `int(random()*10)` | Generar un número aleatorio entre 0 y 10. |
| `selected-at(${gps}, 0)` | Aislar la latitud de las coordenadas GPS. |
| `selected-at(${gps}, 1)` | Aislar la longitud de las coordenadas GPS. |
| `if(regex(${id}, '^ML-'), 'yes', 'no')` | Crear una variable binaria que toma el valor `yes` si el ID del encuestado comienza con "ML-". |

### Configurar respuestas predeterminadas dinámicas

El campo `calculation` también se puede usar para configurar **respuestas predeterminadas dinámicas.** Las respuestas predeterminadas dinámicas permiten mostrar una respuesta predeterminada dentro de una pregunta basada en una respuesta anterior.

Para configurar una respuesta predeterminada dinámica:
1. En la columna `calculation`, ingresa la **referencia a la pregunta** que completará dinámicamente la respuesta predeterminada.
2. En la columna `trigger`, ingresa la pregunta que activará el cálculo.
    - Por lo general, esta sería la misma pregunta referenciada en la columna `calculation`, de modo que cualquier cambio en la pregunta de activación también actualice la respuesta predeterminada.

**hoja survey**

| type | name       | label                     | calculation | trigger     |
|:------|:-----------|:--------------------------|:-------------|:-------------|
| text  | hh_name    | Name of the head of household |             |              |
| text  | phone      | Household phone number     |              |              |
| text  | phone_name | Name of the phone owner    | ${hh_name}   | ${hh_name}   |
| survey | 

<p class="note">
<strong>Nota:</strong> Si quieres evitar que los usuarios editen el campo, configura la columna <code>read_only</code> como <code>TRUE</code>.
</p>

## Resolución de problemas

<details>
  <summary><strong>Recomendaciones para la resolución de problemas</strong></summary>
  Para facilitar la resolución de problemas, muestra los resultados de los cálculos en una nota mientras desarrollas el formulario. Esto ayuda a determinar si el cálculo se está evaluando correctamente y facilita la identificación de errores. También puedes dividir las expresiones largas en expresiones más pequeñas y mostrar el resultado de cada una para identificar los problemas con mayor precisión.
</details>

<br>

<details>
  <summary><strong>Los cálculos no funcionan correctamente</strong></summary>
  Si los cálculos no funcionan, verifica lo siguiente:
  <ul>
  <li><strong>Sintaxis:</strong> todos los paréntesis abiertos están cerrados, se usan comillas simples rectas <code>'</code> y se incluyen comas donde sea necesario.</li>
  <li><strong>Referencias:</strong> las referencias a preguntas coinciden correctamente con el nombre de la pregunta, sin espacios ni errores tipográficos, y sin referencias circulares (es decir, el cálculo no depende de sí mismo).</li>
  <li><strong>Tipos de datos:</strong> los cálculos numéricos y de cadenas de texto no se combinan dentro de la misma pregunta, y los tipos de datos se usan correctamente.</li>
</ul>
</details>

<br>

<details>
  <summary><strong>Manejo de campos vacíos</strong></summary>
  Las preguntas sin respuesta se tratan como cadenas de texto vacías y no se convierten automáticamente a cero. Cuando se usa un valor vacío en un cálculo, el resultado es "Not a Number" (NaN). Para convertir valores vacíos a cero en los cálculos, usa las <a href="https://support.kobotoolbox.org/es/functions_xls.html">funciones</a> <code>coalesce()</code> o <code>if()</code>. Por ejemplo:
  <ul>
  <li><code>coalesce(${potentially_empty_value}, 0)</code></li>
  <li><code>if(${potentially_empty_value}="", 0, ${potentially_empty_value})</code></li>
</ul>
  Otra opción es establecer valores predeterminados de 0 para cada una de las variables numéricas en la columna <code>default</code>.
</details>

<br>

<details>
  <summary><strong>División por cero</strong></summary>
  Si un cálculo incluye una división y el divisor es igual a cero, el resultado se maneja de forma diferente en los formularios web y en KoboCollect. En los formularios web, una división por cero se ignora. En KoboCollect, el valor calculado será <code>Infinity</code>, lo que puede causar problemas en los informes de datos y al procesar los datos exportados. Para evitar esto, agrega lógica de omisión para que el cálculo no se ejecute cuando el divisor sea igual a cero, o aplica una restricción para evitar que la variable del divisor sea igual a cero.
</details>

<br>

<details>
  <summary><strong>Los cálculos siguen cambiando en el formulario</strong></summary>
  Las expresiones se vuelven a evaluar a medida que el encuestador avanza por el formulario. Esto es especialmente importante para las <a href="https://support.kobotoolbox.org/es/functions_xls.html">funciones</a> que no están vinculadas a campos del formulario, como <code>random()</code> o <code>now()</code>, ya que sus valores pueden cambiar bajo estas condiciones.
<br><br>
Las expresiones se vuelven a evaluar cuando:
  <ul>
  <li>Se abre un formulario</li>
  <li>Cambia el valor de cualquier pregunta incluida en el cálculo</li>
  <li>Se agrega o elimina un grupo de repetición</li>
  <li>Se guarda o finaliza un formulario</li>
</ul>
  Para controlar cuándo se evalúa una expresión, establece un <a href="https://support.kobotoolbox.org/es/question_options_xls.html#additional-question-options">trigger</a> para que se evalúe solo cuando se responda una pregunta determinada, o usa la función <code>once()</code> para garantizar que la expresión se evalúe solo una vez (por ejemplo, <code>once(random())</code> o <code>once(today())</code>).
</details>