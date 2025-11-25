# Límites en las respuestas de Número y Texto
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/0c5dd6987a26369bd16e779f6ee2ad77e2243b26/source/number_text_responses.md" class="reference">21 Jun 2020</a>

Existen limitaciones técnicas subyacentes en la longitud de la respuesta en una pregunta de **Número** o **Texto**.
 
**Las preguntas de número** pueden guardar hasta 17 dígitos (número positivo o negativo). Para ser exactos, el número más grande que se puede ingresar es 2147483647 y el más pequeño -2147483648.
 
Si deseas una respuesta numérica pero necesitas un número con más de 9 dígitos (es decir, más grande que el indicado arriba) - por ejemplo, para números de teléfono largos en algunos países - puedes hacerlo con un truco. En lugar de una pregunta de Número, agrega una pregunta de Texto a tu formulario. Luego, en la configuración de Apariencia de la pregunta, configúrala como números. Esto mostrará el teclado numérico en lugar del teclado de texto estándar.

**Las preguntas de texto** (así como las preguntas de Código de barras) son casi ilimitadas en términos de los caracteres que se pueden ingresar. (La longitud total del texto debe ser menor a 1MB de tamaño, lo cual es más de 300 páginas de texto - más de lo que se puede esperar en una respuesta a una pregunta.