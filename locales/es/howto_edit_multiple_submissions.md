# Editar respuestas en múltiples envíos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/509a98dad39e2899a5eff7e870481cf99749f321/source/howto_edit_multiple_submissions.md" class="reference">22 Sep 2022</a>

Los/as usuarios/as siempre han podido editar envíos como se describe en nuestro artículo de ayuda
[Editar o eliminar un solo envío](howto_edit_single_submissions.md).
¿Qué pasa si un/a usuario/a tiene que editar errores tipográficos repetidos o actualizar respuestas faltantes para
todos o la mayoría de los envíos de un proyecto de encuesta en particular? Seguir el
método descrito anteriormente consumiría mucho tiempo. Por lo tanto, KoboToolbox ha
desarrollado una funcionalidad que debería hacer que la edición sea más sencilla, ahorrando tiempo de edición.

## Limitaciones al editar respuestas para múltiples envíos

Existen varias limitaciones al realizar las acciones de edición masiva descritas en
este artículo. Este no es el caso al editar
[envíos individuales](howto_edit_single_submissions.md). Al usar este
método:

- La lógica de validación y los cálculos dentro de tu formulario no se vuelven a evaluar.
- Actualmente no se admite la edición de preguntas dentro de grupos repetidos.
- Los puntos de coordenadas deben seguir el patrón: `latitud longitud altitud precisión`.
  No hacerlo no causará un error, pero puede confundir tu análisis de datos.
- Las respuestas de selección múltiple deben consistir en los **nombres de opciones** correctos,
  separados por un espacio. No hacerlo no causará un error, pero
  resultará en que las etiquetas no se apliquen correctamente al exportar.

## Editar respuestas para múltiples envíos

La siguiente es una pantalla generalmente vista para **DATOS>Tabla**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_1.png)

La imagen compartida arriba muestra variación en la entrada de datos con la pregunta **País**
que va desde _America_, _U.S.A_, _US_, _United States of America_, _United
States_, _usa_ hasta _USA_. Esta sección del artículo de ayuda describirá _cómo
cambiar todos estos nombres de **País** variados a **USA**_.

**Paso 1:**

Para comenzar a editar respuestas para múltiples envíos, los/as usuarios/as deben seleccionar
un solo registro (marcado **1**) o seleccionar múltiples registros (marcado **2**).
Seleccionar como se muestra en la imagen a continuación debería activar las funcionalidades de edición junto
con otras funcionalidades.

![image](/images/howto_edit_multiple_submissions/edit_multiple_2.png)

- **1.** Los/as usuarios/as pueden seleccionar múltiples registros que requieren edición masiva.
- **2.** Como alternativa al enfoque descrito arriba (en **1**), los/as usuarios/as pueden seleccionar
  _todos los registros_ o _todos los registros visibles_ bajo **DATOS>Tabla**. _Todos los registros_
  se refiere a todos los registros que están presentes dentro del proyecto de encuesta mientras que
  _todos los registros visibles_ se refiere a los 30 registros que son visibles por defecto bajo
  **DATOS>Tabla**. Los/as usuarios/as deben distinguir claramente entre los dos cuando hay
  más de 30 registros (envíos) dentro del proyecto de encuesta.
- **3.** Muestra el número total de registros seleccionados para _cambiar/actualizar el
  estado de validación_, _edición masiva_ o _eliminación masiva_.
- **4.** Los/as usuarios/as pueden cambiar masivamente el estado de validación como se describe en nuestro
  artículo de ayuda [Validación de registros](record_validation.md).
- **5.** Los/as usuarios/as pueden editar masivamente las respuestas para múltiples envíos.
- **6.** Los/as usuarios/as pueden eliminar masivamente los registros.

**Paso 2:**

Los/as usuarios/as ahora tendrán que presionar **Editar** (**5** como se muestra en la imagen arriba) para
edición masiva después de seleccionar todos los registros que requieren modificaciones. El
siguiente cuadro de diálogo debería aparecer entonces.

![image](/images/howto_edit_multiple_submissions/edit_multiple_3.png)

Los/as usuarios/as pueden filtrar la pregunta requerida escribiéndola en el filtro de búsqueda
ubicado justo debajo del encabezado **Pregunta**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_4.png)

Los/as usuarios/as deberían ver _Múltiples respuestas_ bajo el encabezado **Respuesta** (mostrado en
la imagen arriba) si se ingresaron diferentes valores. Aquí tenemos un rango de entradas
desde _America_, _U.S.A_, _US_, _United States of America_, _United States_,
_usa_ hasta _USA_. Sin embargo, si los/as usuarios/as seleccionan un solo registro y presionan **Editar**,
verían el siguiente cuadro de diálogo.

![image](/images/howto_edit_multiple_submissions/edit_multiple_5.png)

Los/as usuarios/as ahora pueden filtrar la respuesta requerida escribiéndola en el filtro de búsqueda
ubicado justo debajo del encabezado **Respuesta**. Este enfoque es útil cuando un/a usuario/a
desea editar un solo registro.

![image](/images/howto_edit_multiple_submissions/edit_multiple_6.png)

**Paso 3:**

Los/as usuarios/as pueden presionar el botón **EDITAR** una vez que se sepa _qué editar y dónde
editar_.

![image](/images/howto_edit_multiple_submissions/edit_multiple_7.png)

**Paso 4:**

Entonces ahora, hay dos enfoques para hacer ediciones masivas. _Enfoque 1_ es cuando los/as usuarios/as
escriben el texto requerido (**USA** en nuestro caso) en el cuadro en blanco (marcado
**1.1**) y luego presionan **GUARDAR** (marcado **2**). _Enfoque 2_ es cuando los/as usuarios/as
presionan **SELECCIONAR** (marcado **1.2**) para un texto apropiado y luego presionan
**GUARDAR** (marcado **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_8.png)

**Paso 5:**

Ahora aparece un cuadro de diálogo. Los/as usuarios/as ahora tendrán que presionar **CONFIRMAR Y CERRAR** para
guardar los cambios realizados.

![image](/images/howto_edit_multiple_submissions/edit_multiple_9.png)

Los/as usuarios/as siempre pueden volver a **DATOS>Tabla** y verificar si las ediciones masivas fueron
exitosas.

![image](/images/howto_edit_multiple_submissions/edit_multiple_10.png)

## Editar respuestas en blanco para múltiples envíos

A veces, puede haber un escenario cuando los/as usuarios/as tienen que agregar una pregunta en el
medio o al final de la encuesta. En tal caso, los datos de la encuesta desde la
ventana **DATOS>Tabla** deberían verse, como se muestra en la imagen a continuación.

![image](/images/howto_edit_multiple_submissions/edit_multiple_11.png)

Esta sección del artículo de ayuda debería describir _cómo cambiar todos estos
estados vacíos a **Alabama**_.

**Paso 1:**

Para comenzar a editar respuestas en blanco para múltiples envíos, los/as usuarios/as deben seleccionar
múltiples registros (marcado **1**) y luego presionar **Editar** (marcado **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_12.png)

**Paso 2:**

Los/as usuarios/as ahora tendrán que presionar **Editar** (como se muestra en la imagen a continuación), que está en
una línea paralela directa a _Estado_ ya que estamos actualizando los estados vacíos para todos
los registros.

![image](/images/howto_edit_multiple_submissions/edit_multiple_13.png)

**Paso 3:**

En este caso, los/as usuarios/as deben escribir el texto requerido (**Alabama** en nuestro caso)
en el cuadro en blanco (marcado **1**) y luego presionar **GUARDAR** (marcado **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_14.png)

**Paso 4:**

Aparece un cuadro de diálogo. Los/as usuarios/as ahora tendrán que presionar **CONFIRMAR Y CERRAR** para guardar
los cambios realizados.

![image](/images/howto_edit_multiple_submissions/edit_multiple_15.png)

Los/as usuarios/as siempre pueden volver a **DATOS>Tabla** y verificar si las ediciones masivas fueron
exitosas.

![image](/images/howto_edit_multiple_submissions/edit_multiple_16.png)