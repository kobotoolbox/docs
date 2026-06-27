# Preguntas de tipo Texto en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/text_questions.md" class="reference">23 Apr 2026</a>

El tipo de pregunta **Texto** en KoboToolbox permite a los encuestados ingresar respuestas abiertas con sus propias palabras. Es ideal cuando el rango de posibles respuestas no está predefinido, como al recolectar nombres, descripciones, explicaciones o comentarios generales.

Este artículo explica cómo agregar una pregunta de texto en el editor de formularios de KoboToolbox **(Formbuilder)**, describe las opciones de apariencia disponibles y destaca consideraciones clave a tener en cuenta al usar este tipo de pregunta.

<p class="note">
<strong>Nota:</strong> Las preguntas de texto pueden aceptar hasta 1 MB de texto, lo que equivale a aproximadamente 300 páginas.
</p>

## Agregar una pregunta de texto en el Formbuilder

Para agregar una pregunta de texto a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ ADD QUESTION**.
4. Elige el tipo de pregunta <i class="k-icon-qt-text"></i> **Texto**.

![Seleccionar el tipo de pregunta Texto](images/text_questions/text.png)

## Apariencias de las preguntas de texto

De forma predeterminada, las preguntas de texto aparecen como un cuadro de texto de una sola línea.

- En los [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html), el cuadro de texto mantiene el mismo tamaño independientemente de la cantidad de texto ingresado. No admite saltos de línea.
- En [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html), el cuadro de texto se expande a medida que escribes y admite saltos de línea, lo que permite a los encuestados ingresar párrafos.

![Apariencia de la pregunta de texto en formularios web vs KoboCollect](images/text_questions/table.png)

### Apariencias avanzadas

Puedes aplicar apariencias avanzadas a las preguntas de texto para modificar cómo se muestran y se comportan en tu formulario.

Para agregar una apariencia avanzada:
1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En **Aspecto (avanzado)**, elige la apariencia deseada.
    - Si la apariencia no aparece en la lista, selecciona **other** y escribe el nombre de la apariencia en el cuadro de texto, exactamente como se indica a continuación.

![Elegir la apariencia de la pregunta de texto](images/text_questions/appearance.png)

Las siguientes apariencias están disponibles para las preguntas de texto:

| Apariencia | Descripción | Compatibilidad |
|:---|:---|:---|
| `multiline` | Muestra un cuadro de texto más grande para respuestas de texto más extensas.<br>![Apariencia multiline](images/text_questions/multiline.png) | Formularios web y KoboCollect |
| `numbers` | Muestra un teclado numérico en lugar de un teclado de texto (por ejemplo, para recolectar números de teléfono).<br>![Apariencia numbers](images/text_questions/numbers.png) | Solo KoboCollect |
| `url` (other) | Muestra una URL en la que se puede hacer clic (formularios web) o un botón **Open URL** (KoboCollect) debajo del texto de la pregunta, y convierte la pregunta en solo lectura. Ingresa la URL en la configuración de **Respuesta predeterminada** de la pregunta.<br>![Apariencia url](images/text_questions/url.png) | Formularios web y KoboCollect |
| `masked` (other) | Oculta el texto ingresado por el encuestado (por ejemplo, una contraseña o información confidencial).<br>![Apariencia masked](images/text_questions/masked.png) | Solo KoboCollect |

<p class="note">
<strong>Nota:</strong> Usa la apariencia <code>numbers</code> cuando ingreses valores numéricos que deban almacenarse como texto. Esto es especialmente importante para valores que comienzan con cero, como números de teléfono o números de cuenta bancaria, para asegurarte de que el cero inicial se conserve.
</p>

## Buenas prácticas para el uso de preguntas de texto

Las preguntas de texto deben usarse para respuestas abiertas, cuando no es posible proporcionar una lista predefinida de opciones de respuesta. Si puedes definir un conjunto fijo de respuestas, considera usar los tipos de pregunta **Seleccionar una** o **Seleccionar varias**. Limitar las respuestas puede mejorar la calidad de los datos y facilitar su limpieza, procesamiento y análisis.

<p class="note">
  Para más información, consulta <a href="https://support.kobotoolbox.org/es/select_one_and_select_many.html">Preguntas de opción múltiple en KoboToolbox</a>.
</p>

### Uso de preguntas de texto en la lógica del formulario

Dado que las respuestas de texto son abiertas, aplicar [lógica de omisión](https://support.kobotoolbox.org/es/skip_logic.html) o [criterios de validación](https://support.kobotoolbox.org/es/validation_criteria.html) puede ser más complejo.

Puedes usar **expresiones regulares** para validar y controlar el texto ingresado. Por ejemplo, puedes:

- Limitar el número de caracteres en una respuesta
- Restringir los caracteres a números o letras mayúsculas
- Aplicar un formato específico, como un ID único

<p class="note">
  Para más información, consulta <a href="https://support.kobotoolbox.org/es/restrict_responses.html">Usar expresiones regulares en XLSForm</a>.
</p>

También puedes usar **funciones de cadena de texto** en cálculos para manipular valores de texto, incluyendo:

- Combinar varias cadenas de texto
- Convertir caracteres en minúsculas a mayúsculas
- Extraer una parte específica de una cadena
- Obtener la longitud en caracteres de una cadena

<p class="note">
  Para más información, consulta <a href="https://support.kobotoolbox.org/es/functions_xls.html#functions-to-manipulate-strings">Funciones para manipular cadenas de texto</a>.
</p>