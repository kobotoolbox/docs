# Tipos de preguntas "Seleccionar Uno" y "Seleccionar Varios"
<a href="../select_one_and_select_many.html">Read in English</a> | <a href="../fr/select_one_and_select_many.html">Lire en français</a> | <a href="../ar/select_one_and_select_many.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/0d49d3448e1794b63e051d20df2421b33f5274fc/source/select_one_and_select_many.md" class="reference">28 Mar 2022</a>

Cuando tienes una pregunta categórica con una lista de opciones predefinidas para que los/as encuestados/as elijan, debes elegir el tipo de pregunta "Seleccionar Uno" o "Seleccionar Varios" en KoboToolbox. Un tipo de pregunta "Seleccionar Uno", también conocido como pregunta de "respuesta única", significa que un/a encuestado/a solo puede seleccionar una única respuesta de una lista de opciones. De manera similar, un tipo de pregunta "Seleccionar Varios" también se conoce como pregunta de "respuesta múltiple" donde un/a encuestado/a puede seleccionar múltiples respuestas de una lista de opciones.

Los tipos de preguntas "Seleccionar Uno" y "Seleccionar Varios" pueden ser mejores opciones para mantener la calidad de los datos cuando la pregunta tiene un alcance limitado y definido. Esto se debe a que, a diferencia de la naturaleza abierta del tipo de pregunta "Texto", los dos tipos de preguntas de selección limitan al/a la usuario/a a las opciones enumeradas.

## Cuándo usarlas

Usa el tipo de pregunta "Seleccionar Uno" cuando una pregunta tiene una lista de opciones y el/la encuestado/a está limitado/a a solo una opción de la lista. Los ejemplos incluyen estado civil, sexo o religión.

Usa el tipo de pregunta "Seleccionar Varios" si hay una lista de opciones y el/la encuestado/a puede considerar apropiado seleccionar más de una opción. Los ejemplos incluyen fuentes de ingresos del hogar o una lista de activos del hogar.

## Configurar la pregunta y las opciones

Sigue los mismos pasos para configurar una pregunta "Seleccionar Uno" o "Seleccionar Varios":

-   En el editor de formularios, haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
-   Escribe la etiqueta de la pregunta, por ejemplo, "¿Cuál es tu estado civil?". Luego haz clic en **+ Agregar Pregunta** (o presiona **Enter**).
-   Elige el tipo de pregunta ("Seleccionar Uno" o "Seleccionar Varios")
-   Escribe las etiquetas de respuesta donde dice "Opción 1", "Opción 2". Agrega más opciones si es necesario.

<p class="note">
  Puedes reordenar tu lista de opciones haciendo clic y arrastrando cada elemento a una nueva posición en la lista.
</p>

Haz clic en el ícono de papelera <i class="k-icon k-icon-trash"></i> a la izquierda de la etiqueta de la opción para eliminarla.

## Traducir etiquetas de preguntas y opciones

Para traducir preguntas de tipo selección y sus etiquetas a otros idiomas a través de la interfaz de usuario de KoboToolbox, consulta el artículo de ayuda [Agregar Otro Idioma en el Panel del Proyecto](language_dashboard.md), o [aquí](language_xls.md) si estás creando tu formulario usando XLSForm.

## Valores XML

Al configurar las respuestas de preguntas "Seleccionar Uno" y "Seleccionar Varios", tienes la opción de especificar los valores XML o dejar que KoboToolbox los genere automáticamente.

<p class="note">
  Se recomienda encarecidamente que especifiques valores XML para <strong>todas las preguntas y opciones</strong> antes de desplegar tu formulario, <em>especialmente</em> si las etiquetas están en idiomas con caracteres no latinos como chino, árabe o nepalí.
</p>

Los valores XML son los valores que se guardan en el envío cuando un/a usuario/a elige la respuesta, no la etiqueta. En el editor de formularios, escribe los valores donde dice "AUTOMÁTICO" como se muestra a continuación.

![Valores XML](/images/select_one_and_select_many/xml_values.png)

Las opciones predefinidas para preguntas "Seleccionar Uno" y "Seleccionar Varios" pueden ser a veces insuficientes al recolectar datos. Es posible incluir la opción de una respuesta de texto en ese caso, como se describe en nuestro artículo de ayuda [Respuestas "Otro" Especificadas por el/la Usuario/a para Preguntas de Opción Múltiple](user_specified_other.md).

## Cómo se muestran por defecto en formularios web y KoboCollect

![Comparación de seleccionar uno y seleccionar varios en Enketo y KoboCollect](/images/select_one_and_select_many/select_one_select_many_comparison.png)

Puedes diferenciar fácilmente entre una pregunta "Seleccionar Uno" y "Seleccionar Varios" en un formulario de entrada de datos. La pregunta "Seleccionar Uno" tiene opciones con un botón de radio (aparece un punto sólido después de seleccionar un elemento) mientras que la pregunta "Seleccionar Varios" tiene opciones con una casilla de verificación cuadrada (aparecen marcas de verificación después de seleccionar elementos).

## Opciones de exportación

Al exportar preguntas "Seleccionar Varios", puedes elegir entre exportar todas las respuestas seleccionadas en una sola columna o tener las opciones en columnas separadas o ambas. Lee más sobre la exportación y descarga de datos en [este artículo de ayuda](export_download.md).

## Apariencias avanzadas

Al agregar preguntas "Seleccionar Uno" y "Seleccionar Varios", puedes elegir entre una amplia gama de apariencias. Las apariencias cambian la forma en que se muestra la pregunta en los formularios web o KoboCollect.

![Apariencias](/images/select_one_and_select_many/appearances.png)

<p class="note">
  La opción "otro" te proporciona un espacio donde puedes escribir una apariencia diferente que no se muestra en la lista.
</p>

La siguiente tabla muestra las diferentes apariencias disponibles y cómo se muestran tanto en los formularios web como en KoboCollect.

![Apariencias](/images/select_one_and_select_many/select_one_select_many_table.png)

<p class="note">
  Las apariencias "quick", "likert" y "quickcompact" solo son aplicables a preguntas "Seleccionar Uno".
</p>