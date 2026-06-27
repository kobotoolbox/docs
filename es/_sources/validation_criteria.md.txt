# Añadir criterios de validación en el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/validation_criteria.md" class="reference">20 Mar 2026</a>


<iframe src="https://www.youtube.com/embed/ya9usVpEo9Q?si=-rDzXcCRazcY0Bws&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

La lógica de validación, también conocida como criterios de validación o restricciones, define las condiciones que debe cumplir una respuesta para ser aceptada. Esta funcionalidad ayuda a garantizar datos de alta calidad al evitar respuestas accidentales o no válidas.

Los criterios de validación se pueden aplicar a cualquier tipo de pregunta. Por ejemplo, puedes usarlos para asegurarte de que un participante tenga más de cierta edad, que una fecha esté dentro de un rango específico o que un texto ingresado coincida con un patrón determinado.

Hay dos métodos para añadir criterios de validación en el Formbuilder: añadir una condición mediante el **generador de criterios de validación**, o ingresar manualmente la lógica de validación en **código XLSForm**.


## Añadir una condición

El generador de criterios de validación permite añadir condiciones para preguntas de tipo **Texto**, **Número**, **Decimal** y **Fecha**. No es compatible con preguntas de tipo **Seleccionar una** ni **Seleccionar varias**. Para usar el generador:

1. Abre la <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta.
2. Selecciona **Criterios de validación** y haz clic en **Añadir una condición**.
3. Elige el operador lógico adecuado para tu condición (por ejemplo, >, =, !=).
4. En el campo **valor de la respuesta**, selecciona o escribe el valor que debe tener la respuesta para ser válida.

<p class="note">
    <strong>Nota:</strong> Para añadir criterios de validación a preguntas de tipo <strong>Fecha</strong>, el valor de la respuesta debe estar en formato <code>YYYY-MM-DD</code>. Por ejemplo, para establecer un criterio de validación que exija que una fecha sea anterior al 1 de enero de 2021, usa <code>< 2021-01-01</code>.
</p>

Para añadir múltiples condiciones (por ejemplo, un valor mínimo y un valor máximo), añade la primera condición y luego haz clic en **Añadir otra condición**. Cuando uses múltiples condiciones, especifica si se debe cumplir al menos una de ellas o todas. Puedes eliminar condiciones haciendo clic en el <i class="k-icon-trash"></i> ícono de papelera.

Si no se cumplen las condiciones de validación, la respuesta no será aceptada durante la recolección de datos. Se mostrará un [mensaje de error](#mensaje-de-error).


## Ingresar manualmente la lógica de validación en código XLSForm

Para usuarios avanzados y para preguntas de tipo **Seleccionar una** o **Seleccionar varias**, los criterios de validación se pueden ingresar directamente en código XLSForm.

Para ingresar manualmente la lógica de validación en código XLSForm, sigue estos pasos:

1. Abre la <i class="k-icon-settings"></i> **Configuración** en el menú lateral derecho de la pregunta.
2. Selecciona **Criterios de validación** y haz clic en **Ingresar manualmente la lógica de validación en el código XLSForm**.
3. Ingresa los criterios en código XLSForm.

En la sintaxis de XLSForm, el punto `.` se usa para hacer referencia a la pregunta actual, y `${question_name}` (${nombre_de_la_pregunta}) se usa para hacer referencia a otras preguntas. También debes incluir el operador lógico y el valor de la respuesta correspondientes.

### Ejemplos de criterios de validación

| Criterio | Descripción |
| :------------------- | :------------------------------------------- |
| `. > 17` | La respuesta debe ser mayor que 17 |
| `. >= 17 and . <= 130` | La respuesta debe ser igual o estar entre 17 y 130 |
| `not(${in_university} = 'yes' and . < 16)` | No se puede ingresar una respuesta menor que 16 si la respuesta a `in_university` es "Yes" |
| `not(selected(., 'none') and count-selected(.)>1)` | No se puede seleccionar "None" junto con otras opciones en una pregunta de tipo Seleccionar varias |


<p class="note">
    Para obtener más información sobre el código XLSForm y los operadores, consulta <a href="../es/form_logic.html">Introducción a la lógica de formularios en el Formbuilder</a>.
</p>

## Mensaje de error

El **mensaje de error** es un mensaje opcional que verá el entrevistador o el encuestado cuando ingrese una respuesta no válida. Se puede configurar tanto con el método del **generador de criterios de validación** como con el método de **código XLSForm**, en la parte inferior del cuadro.

Si no se especifica ningún mensaje de error, el mensaje predeterminado es "Value not allowed". Los mensajes de error personalizados suelen indicar los criterios de validación para ayudar al encuestado a corregir su respuesta (por ejemplo, "La edad debe ser mayor que 18").