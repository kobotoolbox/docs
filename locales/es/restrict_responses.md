# Restringir Respuestas de Texto con Expresiones Regulares
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/restrict_responses.md" class="reference">29 Jul 2025</a>

Una expresión regular, o regex, es un patrón de búsqueda utilizado para hacer coincidir caracteres específicos y rangos de caracteres dentro de una cadena. Se utiliza ampliamente para validar, buscar, extraer y restringir texto en la mayoría de los lenguajes de programación. KoboToolbox admite regex para controlar la longitud y los caracteres durante la entrada de datos a una pregunta en particular _(por ejemplo, controlar la entrada de un número de teléfono móvil a exactamente 10 dígitos, controlar la entrada de un correo electrónico válido, etc.)_.

## Para usar un regex en KoboToolbox, sigue estos pasos

1. Prepara una pregunta de tipo _Texto_.

2. Ve a la _Configuración_ de la pregunta.

3. Ve a _Criterios de Validación_ y elige la opción _Introducir manualmente tu lógica de validación en código XLSForm_.

4. En el cuadro _Código de Validación_, ingresa tu fórmula regex entre las comillas `(' ')` del formato `regex(., ' ')`. Como referencia, el punto (`.`) se refiere a _'esta pregunta'_, mientras que la expresión regular dentro de las comillas (`' '`) debe cumplir con las reglas establecidas de regex.

5. (Opcional) Agrega un _Mensaje de Error_ personalizado para que la persona que ingresa datos lo vea cuando no cumpla con los criterios de regex.

![image](/images/restrict_responses/regrex.jpg)

Regex también se puede codificar en XLSForm, bajo la columna _constraint_:

**hoja survey**

| type | name | label                          | appearance | constraint              | constraint_message                         |
| :--- | :--- | :----------------------------- | :--------- | :---------------------- | :----------------------------------------- |
| text | q1   | Número de teléfono móvil del/a encuestado/a | numbers    | regex(., '^[0-9]{10}$') | Este valor debe tener solo 10 dígitos |
| survey |

Alternativamente, puedes crear una pregunta de tipo `calculate` y luego definir el código regex bajo la columna _calculation_. Luego podrías usar esta variable tantas veces como sea necesario en la encuesta:

**hoja survey**

| type      | name | label                  | calculation                              | constraint      | constraint_message                  |
| :-------- | :--- | :--------------------- | :--------------------------------------- | :-------------- | :---------------------------------- |
| calculate | q0   |                        | '^[A-Z]{1}[a-z]{1,}\s[A-Z]{1}[a-z]{1,}$' |                 |                                     |
| text      | q1   | Nombre del/a Encuestador/a |                                          | regex(., ${q0}) | Por favor usa este formato: Kobe Bryant |
| text      | q2   | Nombre del/a Encuestado/a |                                          | regex(., ${q0}) | Por favor usa este formato: Kobe Bryant |
| integer   | q3   | Edad del/a Encuestado/a  |                                          |                 |                                     |
| survey |

## ¿Cómo construyo el regex que necesito?

Además de los ejemplos y consejos proporcionados a continuación, por favor visita
[este sitio web](http://www.regexr.com) para obtener más ayuda y ejemplos.

<p class="note">Regex en KoboToolbox siempre debe escribirse entre los apóstrofes <code>regex(., ' ')</code> como se muestra en los ejemplos.</p>

| Regex               | Descripción                                                                                                                                                                                 |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `^`                 | El símbolo de intercalación coincide con el inicio de una cadena sin consumir ningún carácter.                                                                                                             |
| `$`                 | El símbolo de dólar coincide con el final de una cadena sin consumir ningún carácter.                                                                                                              |
| `[abc]`             | Coincide con `a`, `b` o `c` desde dentro de los corchetes `[ ]`.                                                                                                                       |
| `[a-z]`             | Coincide con cualquier carácter en minúscula de `a` a `z`.                                                                                                                                            |
| `[A-Z]`             | Coincide con cualquier carácter en mayúscula de `A` a `Z`.                                                                                                                            |
| `[0-9]`             | Coincide con cualquier número entero de `0` a `9`.                                                                                                                                                  |
| `[a-zA-Z0-9]`       | Coincide con cualquier carácter de `a` a `z` o `A` a `Z` o `0` a `9`.                                                                                                                          |
| `[^abc]`            | Coincide con cualquier carácter _excepto_ `a`, `b` o `c`.                                                                                                                                             |
| `[^A-Z]`            | Coincide con cualquier carácter _excepto_ aquellos en el rango de `A` a `Z`.                                                                                                                              |
| `(apple)`           | El carácter de agrupación `( )` coincide con cualquier cosa que esté dentro del paréntesis.                                                                                                               |
| <code>&#x7c;</code> | Una barra vertical coincide con cualquier elemento separado.                                                                                                                                               |
| `\`                 | Una barra invertida se usa para coincidir con el valor literal de cualquier metacarácter (por ejemplo, intenta usar `\.` o `\@` o `\$` al construir regex).                                                            |
| `\number`           | Coincide con el mismo carácter que coincidió más recientemente con el n<sup>ésimo</sup> (número usado) grupo de captura.                                                                                    |
| `\s`                | Coincide con cualquier _espacio_ o _tabulación_.                                                                                                                                                               |
| `\b`                | Coincide, sin consumir ningún carácter, inmediatamente entre un carácter que coincide con `\w` y un carácter que no coincide con `\w` (en cualquier orden). `\b` también se conoce como el _límite de palabra_. |
| `\d`                | Coincide con cualquier número equivalente `[0-9]`                                                                                                                                                      |
| `\D`                | Coincide con cualquier cosa que no sean números `(0 a 9)`.                                                                                                                             |
| `\w`                | Coincide con cualquier carácter de palabra (es decir, `a` a `z` o `A` a `Z` o `0` a `9` o `_`).                                                                                                            |
| `\W`                | Coincide con cualquier cosa que no sea lo que coincide con `\w` (es decir, coincide con comodines y espacios).                                                                                                      |
| `?`                 | Un signo de interrogación usado justo detrás de un carácter coincide u omite (si no es necesario) una coincidencia de carácter.                                                                                          |
| `*`                 | Un símbolo de asterisco usado justo detrás de un carácter coincide con cero o más caracteres consecutivos.                                                                                                 |
| `+`                 | El símbolo de más usado justo detrás de un carácter coincide con uno o más caracteres consecutivos.                                                                                                     |
| `{x}`               | Coincide exactamente con `x` caracteres consecutivos.                                                                                                                                                 |
| `{x,}`              | Coincide con al menos `x` caracteres consecutivos (o más).                                                                                                                                      |
| `{x,y}`             | Coincide entre `x` e `y` caracteres consecutivos.                                                                                                                                         |

## Caracteres con acentos

| **Regex**           | **Descripción**                                                                                                |
| :------------------ | :------------------------------------------------------------------------------------------------------------- |
| `[A-zÀ-ú]`          | Acepta caracteres con acentos en minúsculas y mayúsculas                                                             |
| `[A-zÀ-ÿ]`          | Acepta caracteres con acentos en minúsculas y mayúsculas pero incluyendo letras con diéresis (incluye [ ] ^ \ × ÷) |
| `[A-Za-zÀ-ÿ]`       | Acepta caracteres con acentos en minúsculas y mayúsculas pero sin incluir [ ] ^ \                                   |
| `[A-Za-zÀ-ÖØ-öø-ÿ]` | Acepta caracteres con acentos en minúsculas y mayúsculas pero sin incluir [ ] ^ \ × ÷                               |

## Ejemplos relacionados con el uso de números

<p class="note">Para todas las preguntas de tipo <code>text</code> que usan números, no olvides escribir <code>numbers</code> bajo la columna <code>appearance</code>.</p>

| **Regex**                                                                                                                                                                                | **Descripción**                                                                                                  |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| `regex(., '^[0-9]{10}$')` o `regex(., '^\d{10}$')`                                                                                                                                      | Restringir número de teléfono móvil a diez dígitos                                                                             |
| `regex(., '^[0-9]{4}.[0-9]{2}.[0-9]{2}$')` o `regex(., '^\d{4}\.\d{2}\.\d{2}$')`                                                                                                        | Restringir una entrada a `1234.56.78`                                                                                |
| `regex(., '^[01-99]{2}$') and (. >= 01)`                                                                                                                                                 | Restringir una entrada entre `01` a `99` dígitos donde no se permite el formato de entrada de un solo número (como 1 o 2) |
| `regex(., '^(12\|345)$')`                                                                                                                                                                | Restringir una entrada a `12` o `345`                                                                     |
| `regex(., '^[1-9][0-9]{8}$')` o `regex(., '^[^0][0-9]{8}$')`                                                                                                                            | Restringir una entrada de nueve dígitos donde el primer número no puede ser `0`                                             |
| `regex(., '^\d$')`                                                                                                                                                                       | Restringir una entrada a un dígito entre `0` y `9`                                                             |
| `regex(., '^\d{5}$')`                                                                                                                                                                    | Restringir una entrada a cinco dígitos entre `0` y `9`                                                           |
| `regex(., '^\d{2}\.\d{3}$')`                                                                                                                                                             | Restringir una entrada a dos dígitos y tres decimales (por ejemplo, `12.345`)                                               |
| `regex(., '^\d{2}(\.\d{3})?$')`                                                                                                                                                          | Restringir una entrada a dos dígitos y tres decimales (mientras que los decimales son opcionales) (por ejemplo, `12` o `12.345`)     |
| `regex(., '^[0-9]{10}$') or regex(., '^[0-9]{13}$')` o `regex(., '^[0-9]{17}$')` o `regex(., '^([0-9]{10}\|[0-9]{13}\|[0-9]{17})$')` o `regex(., '^([\d]{10}\|[\d]{13}\|[\d]{17})$')` | Restringir una entrada solo a números de `10`, `13` o `17` dígitos                                                       |

## Ejemplos relacionados con el uso de letras

| **Regex**                                                                                               | **Descripción**                                                                                                                                                                                                                                                                                                                            |
| :------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex(., '^[a-z]{1,6}$')`                                                                              | Restringir una entrada a cualquier letra en minúscula (_hasta 6 caracteres de longitud_)                                                                                                                                                                                                                                                     |
| `regex(., '^[A-Z]{1,10}$')`                                                                             | Restringir una entrada a cualquier letra en mayúscula (_hasta 10 caracteres de longitud_)                                                                                                                                                                                                                                                    |
| `regex(., '^(Apple\|Orange\|Banana)$')`                                                                 | Restringir una entrada solo a `Apple` o `Orange` o `Banana`                                                                                                                                                                                                                                        |
| `regex(., '^p(ea\|ai)r$')`                                                                              | Restringir una entrada solo a `pear` o `pair`                                                                                                                                                                                                                                                                                                 |
| `regex(., '^[A-Z]{1}[a-z]{1,}[ ]{1}[A-Z]{1}[a-z]{1,}$')`                                                | Restringir una entrada del nombre de los/as beneficiarios/as donde las _iniciales del primer nombre y apellido están en mayúscula_ por ejemplo, `Kobe Bryant`                                                                                                                                                                                          |
| `regex(., '^\w{1,}\s(\w{1,})?(\s)?\w{1,}$')`                                                            | Restringir una entrada del nombre de los/as beneficiarios/as con _primer nombre, segundo nombre (si lo hay) y apellido_ por ejemplo, `Kobe Bean Bryant`                                                                                                                                                                                                  |
| `regex(., '^([A-Z]{1}[a-z]{1,}\s)([A-Z]{1}[a-z]{1,}\s?)+$')` o `regex(., '^([A-Z]{1}[a-z]{1,}\s?)+$')` | Restringir una entrada del nombre completo de los/as beneficiarios/as donde las _iniciales de los nombres están en mayúscula_ y el nombre es bastante largo (a menudo mayor a 3 palabras) por ejemplo, `Samayamantri Venkata Rama Naga Butchi Anjaneya Satya Krishna Vijay` (este es un ejemplo de nombres del sur de la India)                                                         |
| `regex(., '^(\D+)\s(\D+)\s?\1$')`                                                                       | Restringir una entrada del primer nombre de los/as beneficiarios/as (para que puedas capturar la ortografía exacta) donde _los/as encuestadores/as están obligados/as a ingresar el primer nombre de los/as beneficiarios/as dos veces_ por ejemplo, `Kobe Bryant Kobe`. (Esto podría ser útil cuando estás tratando de documentar detalles de beneficiarios/as donde un error tipográfico podría costarte mucho)      |
| `regex(., '^(\D+)\s(\D+)\s?\2$')`                                                                       | Restringir una entrada del apellido de los/as beneficiarios/as (para que puedas capturar la ortografía exacta) donde _los/as encuestadores/as están obligados/as a ingresar el apellido de los/as beneficiarios/as dos veces_ por ejemplo, `Kobe Bryant Bryant`. _(Esto podría ser útil cuando estás tratando de documentar detalles de beneficiarios/as donde un error tipográfico podría costarte mucho)_ \| |
| `regex(., '^colou?r$')`                                                                                 | Restringir un carácter dentro de una palabra usando el `?` (cuantificador) por ejemplo, permitir `color` o `colour` como entrada                                                                                                                                                                                                         |
| `regex(., '^ah*!$')`                                                                                    | Restringir un carácter dentro de una palabra usando el `*` (cuantificador) por ejemplo, permitir `a!` o `ah!` o `ahh!` o `ahhh!` y así sucesivamente como entrada                                                                                                                                                                                |
| `regex(., '^ah+!$')`                                                                                    | Restringir un carácter dentro de una palabra usando el `+` (cuantificador) por ejemplo, permitir `ah!` o `ahh!` o `ahhh!` y así sucesivamente como entrada                                                                                                                                                                                        |
| `regex(., '^\D$')`                                                                                      | Restringir una entrada a un _carácter que no sea dígito_ (por ejemplo, `a` o `c` o `!` o `#` o `%` etc.)                                                                                                                                                                                                                                   |
| `regex(., '^\D{5 }$')`                                                                                  | Restringir una entrada a _cinco caracteres que no sean dígitos_ (por ejemplo, `aZcB!#%` etc.)                                                                                                                                                                                                                                                      |
| `regex(., '^[A-Z\s]+$')`                                                                                | Restringir toda la entrada de texto a mayúsculas, excluyendo caracteres especiales (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                             |
| `regex(., '^[A-Z\W]+$')`                                                                                | Restringir toda la entrada de texto a mayúsculas, incluyendo caracteres especiales (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                             |
| `regex(., '^[a-z\s]+$')`                                                                                | Restringir toda la entrada de texto a minúsculas, excluyendo caracteres especiales (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                             |
| `regex(., '^[a-z\W]+$')`                                                                                | Restringir toda la entrada de texto a minúsculas, incluyendo caracteres especiales (! @ # $ % ^ & \* ( ) . , ? / " ' etc.)                                                                                                                                                                                             |

## Ejemplos relacionados con el uso de una combinación de letras y números

| XLSForm Regex                                             | Descripción                                                                                                                                                                                                     |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex(., '^\w$')`                                        | Restringir un carácter que coincida entre `a` y `z` o `A` y `Z` o `0` y `9` o `_` (es decir, coincidir un carácter de `[a-zA-Z0-9_]`)                                                                       |
| `regex(., '^\w{3}$')`                                     | Restringir tres caracteres que coincidan entre `a` y `z` o `A` y `Z` o `0` y `9` o `_` (es decir, coincidir un carácter de `[a-zA-Z0-9_]`)                                                                     |
| `regex(., '^[A-Z]{3}[_][A-Z]{3}[_][0-9]{4}[_][0-9]{4}$')` | Restringir tu ID de beneficiario/a a un formato específico por ejemplo, `CAR_PRC_2020_0048`                                                                                                                      |
| `regex(., '^CAR-PRC-2020-[0-9]{4}$')`                     | Restringir tu ID de beneficiario/a a un formato específico por ejemplo, `CAR-PRC-2020-0048` (_donde los/as encuestadores/as deben ingresar una coincidencia exacta de `CAR` a `-` es decir, `CAR-PRC-2020-` y pueden ingresar cualquier número de serie de 4 dígitos_) |
| <code>regex(., '^[\$&#x7c;\£]\d{3}$')</code>              | Restringir una entrada de moneda de _tres dígitos_ con un signo de moneda (ya sea `dólar` o `libra`) al frente (por ejemplo, `$999` o `£500`)                                                                                  |
| `regex(., '^\W*(\w+\b\W*){3}$')`                          | Restringir una entrada exacta del número de palabras (por ejemplo, para restringir exactamente 3 palabras `I love you.`)                                                                                                                     |
| `regex(., '^\W*(\w+\b\W*){3,5}$')`                        | Restringir una entrada del número de palabras (por ejemplo, para restringir un rango de palabras digamos de `3` a `5`)                                                                                                                         |

## Ejemplos relacionados con la restricción de entradas de correo electrónico válidas

<p class="note">Estos ejemplos son puramente ilustrativos y deben ajustarse
para tu caso de uso. Usar regex para restringir direcciones de correo electrónico no
garantiza que sean válidas, solo que siguen un patrón esperado.</p>

| **Regex**                                                                                                          | **Descripción**                                                          |
| :----------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| `regex(., '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*(\.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*)*\.[a-zA-Z]{2,}$')` | Restringir entrada a dirección de correo electrónico válida (por ejemplo, `example.domain.com` o `example.domain.com.np)`. |

## Ejemplos relacionados con el uso de entradas de tiempo

| **Regex**                                                | **Descripción**                           |
| :------------------------------------------------------- | :---------------------------------------- |
| `regex(., '^([00-23]{0,2}:[00-59]{0,2}:[00-59]{0,2})$')` | Restringir una entrada de tiempo en formato de `24` horas |
| `regex(., '^([00-12]{0,2}:[00-59]{0,2}:[00-59]{0,2})$')` | Restringir una entrada de tiempo en formato de `12` horas |

## Consideraciones al usar regex

- Si deseas usar una restricción regex en un número en una pregunta de tipo `text`,
  asegúrate de _siempre_ tener el valor `numbers` bajo la columna `appearance`.
  Esto restringe la visualización de letras, haciendo que solo los números sean visibles para
  las entradas.

- La aplicación de Android de KoboCollect y Enketo se comportan de manera diferente con su manejo de
  expresiones regex. KoboCollect se comporta como si hubieras usado los anclajes `^` y `$`
  alrededor de la expresión (incluso si no los has usado), mientras que Enketo requiere
  los anclajes como obligatorios para una coincidencia exacta.