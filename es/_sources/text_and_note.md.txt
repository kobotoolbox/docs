# Preguntas de tipo Texto y Nota

El tipo de pregunta "Texto" es ideal para preguntas que requieren respuestas abiertas o no definidas, como nombres, comentarios, explicaciones o descripciones.

El tipo de pregunta "Nota" no permite ingresar un valor de respuesta; en cambio, se puede usar para agregar instrucciones o cualquier información adicional que haga la encuesta más clara o fácil de navegar. Por ejemplo, puedes usarla para informar al encuestado o encuestador sobre el contenido de la siguiente sección de preguntas, proporcionar contexto de fondo sobre el motivo de la encuesta, [mostrar distintos tipos de archivos multimedia](media.md) o [mostrar los resultados de cálculos ocultos o respuestas a preguntas anteriores](responses_inside_question.md).

## Cómo configurar las preguntas

Configurar preguntas de tipo `text` o `note` es muy similar:

-   En el editor de formularios de KoboToolbox **(Formbuilder)**, haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
-   Escribe el texto de la pregunta. Por ejemplo, "¿Cuál es tu nombre?". Luego haz clic en **+ ADD QUESTION** (o presiona Enter).
-   Elige el tipo de pregunta ("Texto" o "Nota").

![Configuración de preguntas de tipo Texto y Nota](images/text_and_note/text_note_setup.gif)

## Apariencia en formularios web y KoboCollect

### Apariencia predeterminada

![Apariencia predeterminada de Texto y Nota](images/text_and_note/text_note_default_appearance.png)

<p class="note">
  El cuadro de texto predeterminado en Enketo Webform acepta solo una línea de texto. Sin embargo, en KoboCollect, el campo de texto se expande a medida que escribes. También puedes agregar saltos de línea para formar párrafos.
</p>

### Apariencias avanzadas

Puedes cambiar la apariencia de las preguntas de tipo "Texto" en su configuración.

![Configuración de apariencia](images/text_and_note/text_appearance_settings.png)

![Apariencias avanzadas para Texto](images/text_and_note/text_advanced_appearance.png)

## Consideraciones al usar preguntas de tipo "Texto"

Para garantizar la calidad de los datos, puede ser recomendable usar las [Preguntas de opción múltiple en KoboToolbox](select_one_and_select_many.md) cuando es posible predefinir una lista de respuestas. Limitar las respuestas puede simplificar la limpieza, el procesamiento y el análisis de datos.

El uso del tipo de pregunta "Texto" es más adecuado para preguntas abiertas, en las que no es posible tener una lista predefinida de respuestas.

## Uso de la lógica de preguntas

Dado que las respuestas a las preguntas de tipo "Texto" son abiertas, aplicar lógica de preguntas puede ser más complejo y se facilita mejor mediante el uso de expresiones regulares (RegEx).

Con RegEx, puedes implementar lógica de validación, como limitar la longitud de las respuestas de texto, restringir los caracteres y la secuencia (como un ID único) o permitir únicamente respuestas en letras mayúsculas.

Para obtener más información sobre cómo implementar RegEx, consulta el artículo [Usar expresiones regulares en XLSForm](restrict_responses.md).