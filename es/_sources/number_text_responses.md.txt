# Límites en respuestas de tipo Número y Texto

Existen restricciones técnicas subyacentes en la longitud de la respuesta en una pregunta de tipo **Número** o **Texto**.

Las **preguntas de tipo Número** pueden guardar hasta 17 dígitos (número positivo o negativo). Para ser exactos, el número más grande que se puede ingresar es 2147483647 y el más pequeño -2147483648.

Si necesitas una respuesta numérica pero con más de 9 dígitos (es decir, mayor al número indicado anteriormente) —por ejemplo, para números de teléfono largos en algunos países— puedes hacerlo con un truco. En lugar de una pregunta de tipo Número, añade una pregunta de tipo Texto a tu formulario. Luego, en la configuración de Apariencia de la pregunta, configúrala como numbers. Esto mostrará el teclado numérico en lugar del teclado de texto estándar.

Las **preguntas de tipo Texto** (así como las preguntas de tipo Código de barras) son prácticamente ilimitadas en cuanto a los caracteres que se pueden ingresar. (La longitud total del texto debe ser inferior a 1 MB, lo que equivale a más de 300 páginas de texto, más de lo que se puede esperar en una respuesta a una pregunta).