# Tipos de preguntas de Número, Decimal y Rango
<a href="../number_decimal_range.html">Read in English</a> | <a href="../fr/number_decimal_range.html">Lire en français</a> | <a href="../ar/number_decimal_range.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/ddc7265c83c14464689447dd16d7ddde9a084f75/source/number_decimal_range.md" class="reference">2 de abril de 2025</a>

Al crear preguntas con respuestas numéricas, puedes elegir entre los tipos de preguntas "Número", "Decimal" y "Rango" en KoboToolbox.

Este artículo describe estos tipos de preguntas y cómo usarlos.

## Cuándo usarlos

**Número:** El tipo de pregunta "Número" en el editor de formularios es equivalente al tipo de pregunta `integer` en XLSForm. Usa el tipo de pregunta "Número" cuando las respuestas a una pregunta sean en forma de números enteros, como el número de niños/as (1, 3, 5, etc.).

**Decimal:** Usa el tipo de pregunta "Decimal" cuando la respuesta de una pregunta sea en forma de números decimales, como el ingreso mensual (1.2, 34.5, 42.42, etc.).

**Rango:** El tipo de pregunta "Rango" puede recolectar valores enteros y decimales. De forma predeterminada, el tipo de pregunta "Rango" muestra una escala deslizante que permite a los/as usuarios/as elegir un número. Al configurarlo, debes definir los valores de `inicio` y `fin` del rango, así como el `paso` entre ellos.

## Configuración en el editor de formularios

Para configurar los tipos de preguntas "Número" y "Decimal":

- En el editor de formularios, haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
- Escribe la etiqueta de la pregunta. Por ejemplo, "¿Cuántas personas viven en este hogar?". Luego haz clic en "+ AGREGAR PREGUNTA" (o presiona Enter).
- Elige el tipo de pregunta ("Número" o "Decimal").

![Configuración de preguntas de número](/images/number_decimal_range/setup_number_question.gif)

Para agregar un tipo de pregunta "Rango":

- En el editor de formularios, haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
- Escribe el texto de la pregunta. Por ejemplo, "Califica la efectividad del proyecto del 1 al 5 (siendo 5 el más efectivo)". Luego haz clic en "<i class="k-icon k-icon-plus"></i> AGREGAR PREGUNTA" (o presiona Enter).
- Elige el tipo de pregunta "Rango".
- Escribe el valor de `inicio` (en este ejemplo, 1).
- Escribe el valor de `fin` (en este ejemplo, 5).
- Escribe el `paso`, el número de pasos de un valor al siguiente. (En este ejemplo, 1, lo que significa que las opciones en la escala deslizante son 1, 2, 3, 4, 5).

![Configuración de preguntas de rango](/images/number_decimal_range/setup_range_question.gif)

<p class="note">
  Se recomienda encarecidamente que especifiques nombres para
  <strong>todas las preguntas</strong> antes de desplegar tu formulario,
  <em>especialmente</em> si las etiquetas están en idiomas con caracteres no latinos como
  chino, árabe o nepalí.
</p>

## Configuración en XLSForm

En XLSForm, puedes agregar preguntas de "Número", "Decimal" y "Rango" usando los tipos de pregunta `integer`, `decimal` y `range` respectivamente:

| type    | name     | label                                             | parameters           |
| :------ | :------- | :------------------------------------------------ | :------------------- |
| integer | hhsize   | ¿Cuántas personas viven en este hogar?            |                      |
| decimal | landsize | ¿Qué tan grande es tu tierra? (en hectáreas)      |                      |
| range   | rating   | Califica la efectividad del proyecto del 1 al 5   | start=1 end=5 step=1 |
| survey  |

<p class="note">
  Al agregar una pregunta <code>range</code> a un XLSForm, los parámetros
  <code>start</code>, <code>end</code> y <code>step</code> se agregan en la
  columna <code>parameters</code>.
</p>

## Apariencia predeterminada en formularios web y KoboCollect

![Preguntas de Número, Decimal y Rango](/images/number_decimal_range/number_decimal_range_default.png)

## Apariencias avanzadas

Al agregar las preguntas "número", "decimal" y "rango", puedes especificar diferentes apariencias (en la configuración de la pregunta). Las apariencias cambian la forma en que se muestra la pregunta en formularios web o en KoboCollect.

![Apariencias avanzadas de Número, Decimal y Rango](/images/number_decimal_range/number_decimal_range_advanced_appearance.png)

![Apariencias avanzadas de Número, Decimal y Rango](/images/number_decimal_range/number_decimal_range_advanced.png)

### Apariencias avanzadas en XLSForm

Puedes especificar apariencias avanzadas de las preguntas "Número", "Decimal" y "Rango" en XLSForm bajo la columna de apariencias como en los siguientes ejemplos:

| type    | name            | label                                                         | appearance    | parameters           |
| :------ | :-------------- | :------------------------------------------------------------ | :------------ | :------------------- |
| integer | income          | ¿Cuál fue el ingreso total que obtuviste en los últimos 12 meses? | thousands-sep |                      |
| decimal | bearing         | Capturar orientación                                          | bearing       |                      |
| range   | vertical_rating | Califica la efectividad del proyecto del 1 al 5               | vertical      | start=1 end=5 step=1 |
| range   | picker_rating   | Califica la efectividad del proyecto del 1 al 5               | picker        | start=1 end=5 step=1 |
| range   | star_rating     | Califica la efectividad del proyecto del 1 al 5               | rating        | start=1 end=5 step=1 |
| survey  |

## Límites en las preguntas "Número" y "Decimal"

### KoboCollect

El tipo de pregunta "Número" está limitado a un máximo de 9 caracteres y el tipo de pregunta "Decimal" está limitado a un máximo de 15 caracteres.

<p class="note">
  Los signos negativos y los puntos decimales cuentan para el límite de caracteres.
</p>

### Enketo

Tanto el tipo de pregunta "Número" como "Decimal" están limitados a un máximo de 16 cifras significativas.

Si se ingresa un número entero positivo o negativo de 22 cifras significativas, el formulario registrará un número de 16 dígitos con notación científica. Por ejemplo, el número `±9845284926482357445633` se registraría como `±9.845284926482358e+21`.

Si se ingresa un decimal positivo o negativo de 22 cifras significativas, el formulario registrará un número truncado de 16 dígitos, redondeado al dígito 16. Por ejemplo, el número `±9845284926.482357445633` se registrará como `±9845284926.482357`.

### Tipo de pregunta de texto como número

Si tu encuesta requiere respuestas numéricas que excedan los 15 dígitos, puedes usar una solución alternativa con el tipo de pregunta "Texto":

- Agrega una pregunta de "Texto" a tu formulario.
- Ve a la configuración de **Apariencia** y selecciona "numbers". Ahora aparecerá un teclado de dígitos al completar esta pregunta.
- Finalmente, se puede incluir una [restricción `regex()`](restrict_responses.md) para restringir aún más la entrada si es necesario.

Aquí hay un ejemplo de XLSForm para ilustrar esto:

| type    | name    | label                      | appearance  | constraint             | constraint_message            |
| :------ | :------ | :------------------------- | :---------- | :--------------------- | :---------------------------- |
| text    | number  | Ingresa un número largo    | numbers     | regex(., '^[0-9]\*$')  | El valor debe ser un número   |
| survey  |

<p class="note">
  Puedes descargar un XLSForm con ejemplos de este artículo
  <a
    download
    class="reference"
    href="./_static/files/number_decimal_range/number_decimal_range_question_types.xlsx"
    >aquí</a
  >.
</p>