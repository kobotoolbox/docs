# Tipos de preguntas Texto y Nota
<a href="../text_and_note.html">Read in English</a> | <a href="../fr/text_and_note.html">Lire en français</a> | <a href="../ar/text_and_note.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/4d3ba5b4639335723af5b5a376159a536c904323/source/text_and_note.md" class="reference">9 de mayo de 2022</a>

El tipo de pregunta "Texto" se utiliza mejor para preguntas que requieren respuestas indefinidas o abiertas, como nombres, comentarios, explicaciones o descripciones.

El tipo de pregunta "Nota" no permite un valor de respuesta, en su lugar se puede usar para agregar instrucciones o cualquier información adicional para hacer que la encuesta sea más clara o más fácil de navegar. Por ejemplo, puedes usarlo para informar al/a la encuestado/a o enumerador/a sobre lo que contiene la siguiente sección de preguntas, proporcionar contexto de fondo sobre por qué se está realizando la encuesta, [mostrar varios tipos de medios](media.md), o [mostrar los resultados de cálculos ocultos o respuestas a preguntas anteriores](responses_inside_question.md).

## Cómo configurar las preguntas

Configurar preguntas de tipo `texto` o `nota` es muy similar:

-   En el editor de formularios, haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
-   Escribe el texto de la pregunta. Por ejemplo, "¿Cuál es tu nombre?". Luego haz clic en **+ AGREGAR PREGUNTA** (o presiona Enter).
-   Elige el tipo de pregunta ("Texto" o "Nota")

![Configuración de preguntas de texto y nota](images/text_and_note/text_note_setup.gif)

## Apariencia en formularios web y KoboCollect

### Apariencia predeterminada

![Apariencia predeterminada de texto y nota](images/text_and_note/text_note_default_appearance.png)

<p class="note">
  El cuadro de texto predeterminado en Enketo Webform acepta solo una línea de texto. Sin embargo, en KoboCollect, el campo de texto se expande a medida que escribes. También puedes agregar saltos de línea para formar párrafos
</p>

### Apariencias avanzadas

Puedes cambiar la apariencia de las preguntas de "Texto" en su configuración.

![Configuración de apariencia](images/text_and_note/text_appearance_settings.png)

![Apariencias avanzadas para texto](images/text_and_note/text_advanced_appearance.png)

## Consideraciones al usar preguntas de "Texto"

Por el bien de la calidad de los datos, puede ser recomendable usar [tipos de preguntas "Seleccionar una" o "Seleccionar múltiples"](select_one_and_select_many.md) cuando puedas predefinir una lista de las respuestas. Limitar las respuestas puede agilizar la limpieza, el procesamiento y el análisis de datos.

El uso del tipo de pregunta "Texto" es más adecuado para preguntas abiertas, donde no puedes tener una lista predefinida de respuestas.

## Uso de lógica de preguntas

Dado que las respuestas a las preguntas de "Texto" son abiertas, usar lógica de preguntas puede ser más desafiante y se facilita mejor mediante el uso de "Expresiones Regulares".

Con RegEx, puedes implementar lógica de validación, como limitar la longitud de las respuestas de texto, restringir los caracteres y la secuencia (como un ID único) o permitir solo respuestas que estén en letras mayúsculas.

Para aprender más sobre la implementación de RegEx, lee el artículo de soporte [Restricción de respuestas de texto con expresiones regulares](restrict_responses.md)