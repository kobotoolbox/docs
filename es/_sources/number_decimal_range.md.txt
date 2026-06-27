# Preguntas digitales en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/number_decimal_range.md" class="reference">23 Apr 2026</a>

Las preguntas numéricas se utilizan para recolectar datos cuantitativos, como conteos, mediciones, precios o calificaciones. Ayudan a garantizar que las respuestas se ingresen en formato numérico, lo que facilita cálculos precisos, validaciones y análisis.

KoboToolbox ofrece varios tipos de preguntas numéricas para adaptarse a diferentes necesidades de recolección de datos, incluyendo **números enteros, valores decimales** y **respuestas dentro de un rango definido.**

Este artículo explica los tipos de preguntas numéricas disponibles, cómo agregarlos y configurarlos en el Formbuilder, las opciones de apariencia que puedes aplicar y los límites específicos de cada plataforma que debes tener en cuenta al recolectar datos numéricos.

## Tipos de preguntas numéricas

Los siguientes tipos de preguntas están disponibles en el Formbuilder para que los encuestados ingresen datos numéricos:

| Tipo de pregunta | Descripción |
|:---|:---|
| <i class="k-icon-qt-number"></i> Número &emsp; &emsp; | Permite a los encuestados ingresar números enteros (por ejemplo, edad o número de participantes). |
| <i class="k-icon-qt-decimal"></i> Decimal | Permite a los encuestados ingresar números que pueden contener decimales (por ejemplo, tamaño de terreno, precio). |
| <i class="k-icon-qt-range"></i> Rango | Permite a los encuestados seleccionar un valor numérico dentro de un rango definido por valores mínimo y máximo. |

## Agregar una pregunta numérica en el Formbuilder

Para agregar una pregunta numérica a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
4. Haz clic en **+ AGREGAR PREGUNTA.**
5. Elige el tipo de pregunta adecuado.

![Tipos de preguntas numéricas](images/number_decimal_range/numeric.png)

### Configurar preguntas de Rango

Las preguntas de **Rango** se utilizan para recolectar respuestas numéricas dentro de un intervalo definido. Muestran una escala deslizante numerada que permite a los encuestados seleccionar valores entre un mínimo y un máximo.

Este tipo de pregunta es útil para recolectar respuestas en escala, como calificaciones de satisfacción del 1 al 5 o puntuaciones dentro de un rango fijo.

Después de agregar una pregunta de **Rango** en el Formbuilder, configura los siguientes componentes:
- **start**: El valor numérico mínimo del rango.
- **end**: El valor numérico máximo del rango.
- **step**: El intervalo entre cada número del rango.

![Pregunta de rango](images/number_decimal_range/range.png)

## Apariencias de las preguntas numéricas

La tabla a continuación muestra las apariencias predeterminadas para las preguntas numéricas:

![Apariencias de preguntas numéricas](images/number_decimal_range/table.png)

### Apariencias avanzadas

Puedes aplicar apariencias avanzadas a las preguntas numéricas para modificar cómo se muestran y se comportan en tu formulario.

Para agregar una apariencia avanzada:
1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En **Aspecto (avanzado)**, escribe el nombre de la apariencia en el cuadro de texto, exactamente como se indica a continuación.

![Apariencia de pregunta](images/number_decimal_range/appearance.png)

Las siguientes apariencias avanzadas están disponibles para preguntas numéricas:
![Apariencia de pregunta](images/number_decimal_range/table1.png)
![Apariencia de pregunta](images/number_decimal_range/table2.png)

## Límites para preguntas numéricas

Las preguntas numéricas tienen límites específicos según la plataforma que pueden afectar la forma en que se ingresan, almacenan y exportan las respuestas. Es importante tener en cuenta estos límites al diseñar tu formulario, especialmente si esperas números grandes o códigos de identificación.

### Límites numéricos en KoboCollect

En KoboCollect:

- Las preguntas de tipo **Número** están limitadas a 9 caracteres.
- Las preguntas de tipo **Decimal** están limitadas a 15 caracteres.
- Los signos negativos y los puntos decimales cuentan dentro del límite de caracteres.

Si un valor supera estos límites, no se puede ingresar. Esta restricción se aplica en el momento del ingreso de datos e impide guardar números más largos.

### Límites numéricos en formularios web

Los formularios web de KoboToolbox permiten a los encuestados ingresar números más largos, pero existen límites en cuanto a cómo se almacenan:

- Hasta **17 dígitos** se registran de forma completa.
- De **18 a 21 dígitos**, los dígitos adicionales se reemplazan con ceros y se elimina cualquier parte decimal.
- Con **22 dígitos o más**, el valor se almacena automáticamente en notación científica.
- Los signos negativos no cuentan dentro del límite de dígitos.

### Recolectar valores numéricos largos

Si necesitas recolectar valores numéricos que superen estos límites, usa una pregunta de tipo **Texto** en lugar de una pregunta de tipo Número o Decimal.

En la configuración **Aspecto (avanzado)** de la pregunta de Texto, selecciona `numbers`. Esto muestra un teclado numérico en KoboCollect durante la recolección de datos, mientras que el valor se almacena como texto.

Usa este enfoque cuando:

- El número pueda superar los límites de la plataforma
- El valor no deba modificarse ni redondearse
- El número comience con un cero, como un número de teléfono o de cuenta bancaria

Almacenar valores numéricos largos como texto garantiza que todos los dígitos, incluidos los ceros iniciales, se conserven exactamente como fueron ingresados.

<p class="note">
   Para obtener más información sobre el uso de preguntas de Texto con la apariencia <code>numbers</code>, consulta <a href="https://support.kobotoolbox.org/es/text_questions.html#advanced-appearances">Preguntas de tipo Texto en KoboToolbox</a>.
</p>