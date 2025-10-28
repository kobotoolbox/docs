# Uso de las opciones de preguntas
<a href="../question_options.html">Read in English</a> | <a href="../fr/question_options.html">Lire en français</a> | <a href="../ar/question_options.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/43a3384fad535287d1c7820457ab2d25a86877fc/source/question_options.md" class="reference">24 Sep 2025</a>

Después de agregar una pregunta, hay muchas personalizaciones diferentes que puedes hacerle usando las opciones de preguntas. Para acceder a la pantalla de opciones de preguntas de una pregunta, haz clic en su botón <i class="k-icon k-icon-settings"></i> Configuración.

![Opciones de preguntas](/images/question_options/options2.png)

## Nombre de la columna de datos

El **Nombre de la columna de datos** es el identificador único (ID) de tu pregunta.

Este campo es obligatorio para cada pregunta. Solo se permiten letras, números y guiones bajos en este campo, y el campo debe comenzar con una letra o un guión bajo. Puedes ingresar lo que desees, como `what_is_your_name` o `age`.

El Nombre de la columna de datos es importante porque se utiliza en los encabezados de columna de tablas y hojas de cálculo después de que se hayan recolectado tus datos. Si deseas que tu hoja de cálculo siga una convención de nomenclatura específica, debes especificar el nombre para cada una de tus preguntas antes de desplegar el formulario como un proyecto de recolección de datos.

## Sugerencia de orientación (opcional)

Las **Sugerencias de orientación** son instrucciones adicionales que puedes agregar a tus preguntas como notas. De forma predeterminada en los formularios web de Enketo, las sugerencias de orientación se muestran bajo un acordeón que se puede expandir y contraer como se muestra a continuación.

![Sugerencia de orientación en formularios web de Enketo](/images/question_options/guidance_hint_enketo.gif)

En [KoboCollect](kobocollect_on_android_latest.md), las sugerencias de orientación no se muestran de forma predeterminada. Puedes [elegir cómo deben mostrarse las sugerencias de orientación](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings) en tus formularios yendo a Ajustes -> Manejo de formularios -> Mostrar orientación para preguntas. Aquí tienes 3 opciones: No, Sí - siempre mostrado y Sí - siempre contraído.

![Sugerencia de orientación en KoboCollect](/images/question_options/guidance_hint_kobocollect.gif)

Las sugerencias de orientación se pueden usar como notas internas cuando colaboras con otros/as en el desarrollo del formulario. También puedes mostrarlas en impresiones o instrucciones adicionales durante la capacitación para encuestadores/as.

## Respuesta obligatoria

Esta configuración te permite especificar si la pregunta debe responderse en todo momento o no. En XLSForm, esto se llama `required`.

En KoboToolbox, hay tres opciones para respuesta obligatoria:

1. Sí - La pregunta debe responderse en todo momento. Si no se proporciona una respuesta, el/la usuario/a no podrá pasar a la siguiente pregunta o guardar el formulario.
2. No - La pregunta no es obligatoria y, por lo tanto, puede omitirse manualmente.
3. Lógica personalizada - Puedes definir lógica usando código XLSForm que definirá cuándo la pregunta será obligatoria. Por ejemplo, si estableces la siguiente lógica personalizada `${age} > 18`, la pregunta será obligatoria cuando una pregunta anterior con el nombre de columna de datos `age` sea mayor que 18.

## Respuesta predeterminada (opcional)

Esto permite especificar una respuesta predeterminada que el/la entrevistador/a puede aceptar o cambiar.

En la mayoría de los estudios esto no sería recomendable ya que podría crear un sesgo accidental, pero puede ser útil para preguntas de fecha u hora donde las respuestas tienden a estar alrededor de un cierto punto conocido.

Para preguntas de <i class="k-icon k-icon-qt-date"></i> Fecha, la respuesta predeterminada debe escribirse en el formato `YYYY-MM-DD` por ejemplo `1974-12-31`).

Para preguntas de <i class="k-icon k-icon-qt-select-one"></i> Seleccionar una o <i class="k-icon k-icon-qt-select-many"></i> Seleccionar varias, la respuesta debe escribirse usando el Valor único (valor xml) - no la etiqueta (por ejemplo, `first_grade` en lugar de `First grade`).

## Apariencia (opcional)

Esta configuración avanzada permite mostrar la pregunta de una manera modificada. Ciertas opciones de apariencia solo estarán disponibles dependiendo del [Tipo de pregunta](question_types.md).

Para obtener una lista completa de valores de apariencia, visita [la documentación de apariencia de ODK](http://xlsform.org/en/#appearance).

![Opciones de apariencia de preguntas](/images/question_options/appearance.png)