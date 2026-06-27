# Editar respuestas en múltiples envíos

Los usuarios siempre han podido editar envíos como se describe en nuestro artículo de ayuda [Modificar y eliminar datos](howto_edit_single_submissions.md). ¿Qué pasa si un usuario tiene que corregir errores tipográficos repetidos o actualizar respuestas faltantes en todos o la mayoría de los envíos de un proyecto de encuesta en particular? Seguir el método descrito anteriormente consumiría mucho tiempo. Por eso, KoboToolbox ha desarrollado una funcionalidad que facilita la edición y permite ahorrar tiempo.

## Limitaciones al editar respuestas en múltiples envíos

Existen varias limitaciones al realizar las acciones de edición masiva descritas en este artículo. Esto no ocurre al editar [envíos individuales](howto_edit_single_submissions.md). Al usar este método:

- La lógica de validación y los cálculos dentro del formulario no se vuelven a evaluar.
- La edición de preguntas dentro de grupos de repetición no está disponible actualmente.
- Los puntos de coordenadas deben seguir el patrón: `latitude longitude altitude accuracy`.
  No hacerlo no generará un error, pero puede dificultar el análisis de datos.
- Las respuestas de selección múltiple deben contener los **nombres de opciones** correctos,
  separados por un espacio. No hacerlo no generará un error, pero hará que las etiquetas no se apliquen correctamente al exportar.

## Editar respuestas en múltiples envíos

A continuación se muestra la pantalla que generalmente se ve en **DATOS>Tabla**.

![image](/images/howto_edit_multiple_submissions/edit_multiple_1.png)

La imagen anterior muestra variaciones en los datos ingresados para la pregunta **Country** (País), con valores como _America_, _U.S.A_, _US_, _United States of America_, _United States_, _usa_ y _USA_. Esta sección del artículo de ayuda describe _cómo cambiar todos estos valores distintos de **Country** a **USA**_.

**Paso 1:**

Para comenzar a editar respuestas en múltiples envíos, debes seleccionar un solo registro (marcado con **1**) o varios registros (marcado con **2**). Al seleccionar como se muestra en la imagen a continuación, se activarán las funciones de edición junto con otras funciones.

![image](/images/howto_edit_multiple_submissions/edit_multiple_2.png)

- **1.** Puedes seleccionar varios registros que requieran edición masiva.
- **2.** Como alternativa al método descrito en **1**, puedes seleccionar _todos los registros_ o _todos los registros visibles_ en **DATOS>Tabla**. _Todos los registros_ hace referencia a la totalidad de los registros presentes en el proyecto de encuesta, mientras que _todos los registros visibles_ hace referencia a los 30 registros que se muestran de forma predeterminada en **DATOS>Tabla**. Debes distinguir claramente entre ambas opciones cuando el proyecto de encuesta tiene más de 30 registros (envíos).
- **3.** Muestra el número total de registros seleccionados para _cambiar/actualizar el estado de validación_, _edición masiva_ o _eliminación masiva_.
- **4.** Puedes cambiar masivamente el estado de validación como se describe en nuestro artículo de ayuda [Ver y validar datos](record_validation.md).
- **5.** Puedes editar masivamente las respuestas de múltiples envíos.
- **6.** Puedes eliminar masivamente los registros.

**Paso 2:**

Ahora debes hacer clic en **Editar** (**5** como se muestra en la imagen anterior) para realizar la edición masiva después de seleccionar todos los registros que requieren modificaciones. A continuación aparecerá la siguiente caja de diálogo.

![image](/images/howto_edit_multiple_submissions/edit_multiple_3.png)

Puedes filtrar la pregunta requerida escribiéndola en el filtro de búsqueda ubicado justo debajo del encabezado **Question** (Pregunta).

![image](/images/howto_edit_multiple_submissions/edit_multiple_4.png)

Verás _Varias respuestas_ bajo el encabezado **Response** (Respuesta) (como se muestra en la imagen anterior) si se ingresaron valores distintos. En este caso, hay un rango de entradas que va desde _America_, _U.S.A_, _US_, _United States of America_, _United States_, _usa_ hasta _USA_. Sin embargo, si seleccionas un solo registro y haces clic en **Editar**, verás la siguiente caja de diálogo.

![image](/images/howto_edit_multiple_submissions/edit_multiple_5.png)

Ahora puedes filtrar la respuesta requerida escribiéndola en el filtro de búsqueda ubicado justo debajo del encabezado **Response** (Respuesta). Este método es útil cuando deseas editar un solo registro.

![image](/images/howto_edit_multiple_submissions/edit_multiple_6.png)

**Paso 3:**

Puedes hacer clic en el botón **EDITAR** una vez que sepas _qué editar y dónde editarlo_.

![image](/images/howto_edit_multiple_submissions/edit_multiple_7.png)

**Paso 4:**

Hay dos métodos para realizar ediciones masivas. El _Método 1_ consiste en escribir el texto requerido (**USA** en este caso) en el campo en blanco (marcado con **1.1**) y luego hacer clic en **GUARDAR** (marcado con **2**). El _Método 2_ consiste en hacer clic en **SELECCIONAR** (marcado con **1.2**) para elegir el texto apropiado y luego hacer clic en **GUARDAR** (marcado con **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_8.png)

**Paso 5:**

Aparece una caja de diálogo. Ahora debes hacer clic en **CONFIRMAR Y CERRAR** para guardar los cambios realizados.

![image](/images/howto_edit_multiple_submissions/edit_multiple_9.png)

Siempre puedes volver a **DATOS>Tabla** y verificar si las ediciones masivas se realizaron correctamente.

![image](/images/howto_edit_multiple_submissions/edit_multiple_10.png)

## Editar respuestas en blanco en múltiples envíos

En ocasiones, puede darse el caso de que tengas que agregar una pregunta en la mitad o al final de la encuesta. En ese caso, los datos de la encuesta en **DATOS>Tabla** se verán como se muestra en la imagen a continuación.

![image](/images/howto_edit_multiple_submissions/edit_multiple_11.png)

Esta sección del artículo de ayuda describe _cómo cambiar todos estos campos vacíos a **Alabama**_.

**Paso 1:**

Para comenzar a editar respuestas en blanco en múltiples envíos, debes seleccionar varios registros (marcado con **1**) y luego hacer clic en **Editar** (marcado con **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_12.png)

**Paso 2:**

Ahora debes hacer clic en **Editar** (como se muestra en la imagen a continuación), que está en la misma línea que _State_ (Estado), ya que estamos actualizando los campos vacíos de estado para todos los registros.

![image](/images/howto_edit_multiple_submissions/edit_multiple_13.png)

**Paso 3:**

En este caso, debes escribir el texto requerido (**Alabama** en este caso) en el campo en blanco (marcado con **1**) y luego hacer clic en **GUARDAR** (marcado con **2**).

![image](/images/howto_edit_multiple_submissions/edit_multiple_14.png)

**Paso 4:**

Aparece una caja de diálogo. Ahora debes hacer clic en **CONFIRMAR Y CERRAR** para guardar los cambios realizados.

![image](/images/howto_edit_multiple_submissions/edit_multiple_15.png)

Siempre puedes volver a **DATOS>Tabla** y verificar si las ediciones masivas se realizaron correctamente.

![image](/images/howto_edit_multiple_submissions/edit_multiple_16.png)