# Usar funciones en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/3e68d0f83165ae0b4339daef4fd4090b2efeeb46/source/functions_xls.md" class="reference">15 Feb 2026</a>

Las funciones son operaciones predefinidas que se utilizan para realizar cálculos o manipular datos en XLSForm. Son esenciales para automatizar tareas y obtener información clave en tus formularios, ya que te permiten calcular indicadores de proyecto, crear sistemas de puntuación y gestionar fechas de manera eficiente.

Este artículo enumera las funciones más comunes utilizadas en XLSForm, incluyendo funciones para manipular números, cadenas de texto, fechas y puntos GPS.

<p class="note">
  Para obtener más información sobre la lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>. Para conocer las funciones utilizadas específicamente en grupos repetidos, consulta <a href="https://support.kobotoolbox.org/es/repeat_groups_xls.html">Grupos repetidos en XLSForm</a>.
</p>

## Funciones de uso frecuente en XLSForm

Las siguientes funciones son algunas de las más utilizadas en XLSForm. Ayudan a controlar el comportamiento del formulario, gestionar respuestas y realizar cálculos básicos u operaciones lógicas entre preguntas. Estas funciones se pueden aplicar en cálculos, restricciones, condiciones de relevancia y otras expresiones a lo largo del formulario.

| Función | Descripción |
|:-----------|:-------------|
| `if(expression, then, else)` | Si la expresión es TRUE, devuelve `then`. Si no, devuelve `else`. |
| `selected(${question_name}, option_name)` | Se utiliza para determinar si se seleccionó una opción específica en una pregunta `select_multiple`. |
| `random()` | Devuelve un número aleatorio entre 0.0 (inclusive) y 1.0 (exclusive). |
| `count-selected(${question_name})` | Devuelve el número de opciones seleccionadas en una pregunta `select_multiple`. |
| `coalesce(${question1}, ${question2})` | Devuelve el primer valor no vacío de los dos argumentos. Devuelve una cadena vacía si ambos están vacíos o no existen. |
| `jr:choice-name(choice_name, '${question_name}')` | Devuelve el valor de la etiqueta, en el idioma activo, asociada con `choice_name` en la lista de opciones de una pregunta de tipo selección. Para recuperar la etiqueta de la respuesta seleccionada, usa `jr:choice-name(${question_name}, '${question_name}')`. |
| `selected-at(${question_name}, n)` | Devuelve la opción seleccionada en una pregunta `select_multiple` en la posición **n+1**. Por ejemplo, `selected-at(${question_name}, 2)` devuelve la tercera opción seleccionada en una pregunta `select_multiple`. |
| `once(expression)` | Evalúa una expresión solo una vez (por ejemplo, para garantizar que un número aleatorio se genere una sola vez, o para almacenar el primer valor ingresado en una pregunta aunque la respuesta se cambie posteriormente). |
| `instance('list_name')/root/item[name = ${question}]/column_name` | Recupera un valor de la hoja choices. Busca en la lista de opciones llamada `list_name`, encuentra la fila donde el `name` de la opción coincide con la respuesta a `${question}` y devuelve el valor de la columna especificada como `column_name`. |

## Funciones para manipular números

Las siguientes funciones se utilizan para realizar operaciones matemáticas o transformar valores numéricos en XLSForm. Pueden ayudarte a calcular, redondear o convertir números, así como aplicar expresiones matemáticas más avanzadas cuando sea necesario.

| Función | Descripción |
|:---------|:------------|
| `int(number)` | Transforma un número decimal en un entero sin redondear. |
| `round(number, places)` | Redondea un valor decimal a un número predeterminado de decimales. |
| `pow(number, power)` | Calcula la potencia de un número. |
| `number(x)` | Convierte x (una cadena de texto o expresión booleana) en un valor numérico. |
| `log(number)` <br> `log10(number)` | Devuelve el logaritmo natural o el logaritmo en base 10 de un número. |
| `abs(number)` | Devuelve el valor absoluto de un número. |
| `sin(number)` <br> `asin(number)` <br> `cos(number)` <br> `acos(number)` <br> `tan(number)` <br> `atan(number)` | Devuelve el seno/arcoseno, coseno/arcocoseno o tangente/arcotangente de un número. |
| `sqrt(number)` | Devuelve la raíz cuadrada de un número. |
| `exp(x)` <br> `exp10(x)` | Devuelve e^x o 10^x. |
| `pi()` | Devuelve una aproximación de la constante matemática π. |

<p class="note">
  <strong>Nota:</strong> Dentro de estas funciones se pueden incluir constantes o <a href="https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing">referencias a preguntas</a>.
</p>

## Funciones para manipular cadenas de texto

Las siguientes funciones se utilizan para crear, modificar o analizar cadenas de texto en XLSForm. Son útiles para combinar texto, verificar patrones o caracteres específicos, y limpiar o dar formato a entradas de texto.

| Función | Descripción |
|:---------|:------------|
| `concat()` | Concatena uno o más argumentos (separados por comas) en una sola cadena de texto. |
| `regex(string, expression)` | Devuelve `TRUE` si la cadena de texto es una coincidencia exacta y completa con una <a href="https://support.kobotoolbox.org/es/restrict_responses.html">expresión regular</a>. |
| `contains(string, substring)` | Devuelve `TRUE` si la cadena de texto contiene la subcadena. |
| `starts-with(string, substring)` | Devuelve `TRUE` si la cadena de texto comienza con la subcadena. |
| `ends-with(string, substring)` | Devuelve `TRUE` si la cadena de texto termina con la subcadena. |
| `substr(string, start, end)` | Devuelve la subcadena de `string` que comienza en el índice `start` y se extiende hasta (sin incluir) el índice `end` (o hasta el final de `string` si no se proporciona `end`). |
| `substring-before(string, target)` | Devuelve la subcadena de `string` que precede a la primera aparición de la subcadena objetivo. Si no se encuentra el objetivo, o si `string` comienza con la subcadena objetivo, devuelve una cadena vacía. |
| `substring-after(string, target)` | Devuelve la subcadena de `string` que sigue a la primera aparición de la subcadena objetivo. Si no se encuentra el objetivo, devuelve una cadena vacía. |
| `translate(string, fromchars, tochars)` | Devuelve una copia de la cadena de texto en la que cada aparición de un carácter de `fromchars` es reemplazada por el carácter correspondiente en `tochars` (por ejemplo, reemplazando todas las letras minúsculas por mayúsculas). <br><br> <strong>Nota:</strong> Si `fromchars` es más largo que `tochars`, cada aparición de un carácter de `fromchars` que no tenga un carácter correspondiente en `tochars` será eliminada. |
| `string-length(string)` | Devuelve el número de caracteres de `string` (por ejemplo, para agregar un límite de palabras a una pregunta de texto). |
| `normalize-space(string)` | Devuelve una cadena de texto en la que se eliminan los espacios en blanco al inicio y al final, y las secuencias de espacios en blanco se reemplazan por un único espacio. |

## Funciones para manipular fechas y horas

Las siguientes funciones se utilizan para registrar, dar formato y calcular valores de fecha y hora en XLSForm. Pueden ayudarte a capturar la fecha u hora actual, convertir texto en formato de fecha, o mostrar fechas y horas en un formato específico.

| Función | Descripción |
|:---------|:------------|
| `today()` | Devuelve la fecha actual sin componente de hora. |
| `now()` | Devuelve la fecha y hora actuales en formato ISO 8601, incluyendo la zona horaria. |
| `date('YYYY-MM-DD')` | Fuerza las fechas al formato de fecha correcto (especialmente para fechas anteriores a 1970). |
| `format-date(date, format)` | Devuelve `date` como una cadena de texto con el formato definido por <code>format</code>. Los formatos más comunes incluyen: <ul><li><code>%Y</code>: año de 4 dígitos</li><li><code>%y</code>: año de 2 dígitos</li><li><code>%m</code>: mes con cero inicial</li><li><code>%n</code>: mes numérico</li><li><code>%b</code>: mes abreviado en texto (Jan, Feb, Mar…)</li><li><code>%d</code>: día del mes con cero inicial</li><li><code>%e</code>: día del mes</li><li><code>%a</code>: día abreviado en texto (Sun, Mon, Tue…).</li></ul> |
| `format-date-time(datetime, format)` | Devuelve `datetime` como una cadena de texto con el formato definido por <code>format</code>. Los formatos más comunes incluyen: <ul><li><code>%H</code>: hora con cero inicial (formato de 24 horas)</li><li><code>%h</code>: hora (formato de 24 horas)</li><li><code>%M</code>: minutos con cero inicial</li><li><code>%S</code>: segundos con cero inicial</li><li><code>%3</code>: milisegundos con cero inicial.</li></ul> |
| `decimal-time()` | Convierte una hora en un valor decimal (por ejemplo, las 12:00 pm se convierte en 0.5), lo que facilita la lógica del formulario basada en el tiempo. |

## Funciones para manipular datos GPS

Las siguientes funciones se utilizan para trabajar con datos geográficos recolectados mediante preguntas GPS en XLSForm. Permiten calcular distancias, perímetros o áreas a partir de respuestas de tipo geopoint, geotrace o geoshape.

| Función | Descripción |
|:---------|:------------|
| `area(${geoshape})` | Devuelve el área, en metros cuadrados, de un valor `geoshape`. |
| `distance(geo)` | Devuelve la distancia, en metros, de: <ul><li>el perímetro de un valor `geoshape`</li><li>la longitud de un valor `geotrace`</li><li>una lista de geopoints especificados como cadenas de texto o referencias a otros campos (incluyendo los de grupos repetidos), separados por comas</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Devuelve `TRUE` si el `${geopoint}` especificado se encuentra dentro del `${geoshape}` especificado; `FALSE` en caso contrario. Solo disponible en KoboCollect. |