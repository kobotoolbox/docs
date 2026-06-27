# Usar expresiones regulares en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/d7c5254864f652f34ecb1d4bfe52ef2ddb1247e1/source/restrict_responses.md" class="reference">6 May 2026</a>

Una **expresión regular**, o regex, es un patrón de búsqueda que se utiliza para identificar caracteres específicos o rangos de caracteres dentro de un texto. Las expresiones regulares se usan comúnmente para validar, buscar, extraer o restringir la entrada de texto.

En KoboToolbox, las expresiones regulares se utilizan principalmente para controlar cómo los usuarios ingresan datos. Por ejemplo, puedes restringir un número de teléfono a exactamente 10 dígitos, aplicar un formato de identificación específico o limitar el texto solo a letras mayúsculas.

Este artículo ofrece una descripción general de los componentes más comunes de las expresiones regulares y ejemplos prácticos que puedes usar para validar y restringir la entrada de texto en tus formularios.

<p class="note">
   Para obtener más información sobre el uso de expresiones regulares en tus formularios, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a> y <a href="https://support.kobotoolbox.org/es/form_logic.html">Introducción a la lógica de formularios en el Formbuilder</a>.
</p>

## Componentes comunes de regex

Las expresiones regulares en KoboToolbox se escriben dentro de la función `regex()`. Por ejemplo, `regex(., '^[0-9]{10}$')` restringe una entrada a exactamente 10 dígitos.

Las siguientes tablas describen los elementos de regex más utilizados.

### Anclajes y agrupaciones

| Regex | Descripción |
|:---|:---|
| <code>^</code> | Coincide con el inicio de una cadena |
| <code>$</code> | Coincide con el final de una cadena |
| <code>( )</code> | Agrupa caracteres |
| <code>\|</code> | Coincide con un patrón u otro (OR lógico) |

### Clases de caracteres

| Regex | Descripción |
|:---|:---|
| <code>[abc]</code> | Coincide con a, b o c |
| <code>[a-z]</code> | Coincide con cualquier letra minúscula |
| <code>[A-Z]</code> | Coincide con cualquier letra mayúscula |
| <code>[0-9]</code> | Coincide con cualquier dígito del 0 al 9 |
| <code>[a-zA-Z0-9]</code> | Coincide con letras o dígitos |
| <code>\[^abc]</code> | Coincide con cualquier carácter excepto a, b o c |
| <code>\[^A-Z]</code> | Coincide con cualquier carácter excepto letras mayúsculas |

### Atajos de caracteres especiales

| Regex | Descripción |
|:---|:---|
| <code>\d</code> | Coincide con cualquier dígito (equivalente a [0-9]) |
| <code>\D</code> | Coincide con cualquier carácter que no sea un dígito |
| <code>\w</code> | Coincide con cualquier letra, número o guión bajo (`_`) |
| <code>\W</code> | Coincide con cualquier carácter excepto letras, números y guiones bajos (`_`) |
| <code>\s</code> | Coincide con un espacio o tabulación |
| <code>\b</code> | Coincide con un límite de palabra |
| `\.` | Coincide con un punto literal (<code>.</code>) |
| <code>\\@</code> | Coincide con un <code>@</code> literal |
| <code>\\$</code> | Coincide con un <code>$</code> literal |
| `\\` | Coincide con una barra invertida literal (<code>\\</code>) |
| <code>\number</code> | Hace referencia a un grupo previamente identificado |

### Cuantificadores

| Regex | Descripción |
|:---|:---|
| <code>?</code> | Coincide con cero o una ocurrencia |
| <code>*</code> | Coincide con cero o más ocurrencias |
| <code>+</code> | Coincide con una o más ocurrencias |
| <code>{x}</code> | Coincide con exactamente x ocurrencias |
| <code>{x,}</code> | Coincide con al menos x ocurrencias |
| <code>{x,y}</code> | Coincide con entre x e y ocurrencias |

## Ejemplos comunes

Los siguientes ejemplos pueden usarse como [restricciones](https://support.kobotoolbox.org/es/constraints_xls.html) o [criterios de validación](https://support.kobotoolbox.org/es/validation_criteria.html) en tus formularios.

### Expresiones regex comunes con números

| Regex | Descripción |
|:---|:---|
| <code>regex(., '^\d+$')</code> | Limitar la entrada a números |
| <code>regex(., '^\d{2}$')</code> | Limitar la entrada a 2 dígitos |
| <code>regex(., '^\d{2,4}$')</code> | Limitar la entrada a 2-4 dígitos |
| <code>regex(., '^\d{10}$')</code> | Limitar la entrada a 10 dígitos |
| <code>regex(., '^[1-9][0-9]?$&#124;^100$')</code> | Limitar la entrada a un número entre 1 y 100 (por ejemplo, para un porcentaje) |
| <code>regex(., '^[1-9][0-9]{8}$')</code> | Limitar la entrada a 9 dígitos; el primer dígito no puede ser 0 |
| <code>regex(., '^\d{2}\\.\d{3}$')</code> | Limitar la entrada a un número con formato 12.345 |
| <code>regex(., '^(\d{10}&#124;\d{13}&#124;\d{17})$')</code> | Limitar la entrada a 10, 13 o 17 dígitos |
| <code>regex(., '^(12&#124;345)$')</code> | La entrada debe ser 12 o 345 |
| `regex(., '^[0-9+]{7,15}$')` | Limitar la entrada a un número de teléfono (incluido el signo `+` opcional) |

### Expresiones regex comunes con letras

| Regex | Descripción |
|:---|:---|
| <code>regex(., '^\D*$')</code> | Limitar la entrada a letras, espacios y símbolos (sin números) |
| <code>regex(., '^[A-Za-z]+$')</code> | Limitar la entrada a letras |
| <code>regex(., '^[A-Za-z\s]+$')</code> | Limitar la entrada a letras y espacios |
| <code>regex(., '^[a-z]{1,6}$')</code> | Limitar la entrada a entre 1 y 6 letras minúsculas |
| <code>regex(., '^[A-Z]{1,10}$')</code> | Limitar la entrada a entre 1 y 10 letras mayúsculas |
| <code>regex(., '^(Apple&#124;Orange&#124;Banana)$')</code> | La entrada debe coincidir con una palabra de la lista |
| <code>regex(., '^colou?r$')</code> | Permite color o colour |
| <code>regex(., '^[A-Z\s]+$')</code> | Limitar la entrada solo a letras mayúsculas y espacios |
| <code>regex(., '^[a-z_]+$')</code> | Limitar la entrada a letras minúsculas y guiones bajos (<code>_</code>) |

### Expresiones regex comunes con letras y números

| Regex | Descripción |
|:---|:---|
| <code>regex(., '^\w{3}$')</code> | Limitar la entrada a exactamente 3 letras, dígitos o guiones bajos (<code>_</code>) |
| <code>regex(., '^[A-Z]{1}[0-9]{8}$')</code> | Limitar la entrada a una letra y ocho números |
| <code>regex(., '^CAR-PRC-2020-\d{4}$')</code> | Limitar la entrada a un formato de ID específico |
| <code>regex(., '^\W*(\w+\b\W*){3}$')</code> | Limitar la entrada a exactamente 3 palabras |
| <code>regex(., '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)&#42;(\\&#92;.[a-zA-Z0-9]+(-[a-zA-Z0-9]+)&#42;)&#42;\\&#92;.[a-zA-Z]{2,}$')</code> | Limitar la entrada a un formato de correo electrónico común |

<p class="note">
  Para obtener ayuda adicional para construir y probar patrones, visita: <a href="http://www.regexr.com/">http://www.regexr.com/</a>
</p>