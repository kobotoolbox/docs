# Agregar lógica de omisión a una matriz de preguntas
En la mayoría de los casos, puedes agregar lógica de omisión a cualquier tipo de pregunta, como se describe en el artículo de ayuda **[Añadir lógica de salto al Formbuilder](skip_logic.md)**. Sin embargo, al trabajar en el editor de formularios (Formbuilder), aún no es posible agregar lógica de omisión a una pregunta de tipo `matrix`. En su lugar, puedes usar un XLSForm para implementar lógica de omisión en este tipo de pregunta. Este artículo de ayuda ilustra cómo agregar lógica de omisión a una pregunta `matrix` usando XLSForm.

Si has leído el artículo de ayuda **[Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)**, ya sabrás que existen 2 enfoques para crear una pregunta `matrix` en KoboToolbox: el _enfoque del Formbuilder_ y el _enfoque `kobo--matrix_list`_. Este artículo de ayuda ofrece una descripción general de los pasos necesarios para agregar lógica de omisión a una pregunta `matrix` con cualquiera de estos dos enfoques.

## Enfoque del Formbuilder:

Este enfoque funciona con **Enketo**, también conocido como **formularios web**, utilizando el diseño de **tema de cuadrícula (Grid-theme)**. Es posible que no funcione como se espera si no configuras el **tema de cuadrícula (Grid-theme)** según lo descrito en el artículo de ayuda **[Diseñar formularios web usando el Formbuilder](alternative_enketo.md)**.

Sigue los pasos que se describen a continuación para agregar lógica de omisión a una pregunta `matrix` usando el enfoque del Formbuilder.

**Paso 1:** Crea una pregunta `matrix` en el Formbuilder:

El primer paso es crear una pregunta `matrix` en el Formbuilder, como se describe en el artículo de ayuda **[Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)**. Simplemente agrega filas y columnas con las variables para las que deseas recolectar datos.

**Paso 2:** Descarga el formulario como XLSForm:

Una vez que la pregunta `matrix` esté lista, **GUARDA** el formulario y luego [descárgalo como XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Paso 3:** Agrega el encabezado de columna `relevant` y la lógica de omisión a tu XLSForm:

Abre el XLSForm y agrega el encabezado de columna `relevant`. Una vez que tengas el encabezado de columna `relevant`, podrás agregar lógica de omisión a todas las preguntas según sea necesario.

Para mejorar la forma en que se muestran las preguntas `matrix` al responder, se recomienda agregar un tipo de pregunta `note` (resaltado en amarillo en la imagen a continuación) e incluir lógica de omisión según corresponda. Esto es completamente opcional, ya que solo afectará el formato de la pregunta `matrix`. La diferencia entre _usar_ y _no usar_ el tipo de pregunta `note` se ilustra más adelante en el **Paso 6: Recolectar datos**.

![XLSForm enfoque Formbuilder](images/adding_skip_to_matrix/formbuilder_xlsform.png)

**Paso 4:** Reemplaza el XLSForm:

Carga y reemplaza tu XLSForm en el proyecto existente, o crea un nuevo proyecto (si es necesario).

**Paso 5:** Implementa el formulario:

Una vez que hayas reemplazado el XLSForm (o cargado el XLSForm como un nuevo proyecto), deberás implementar tu formulario.

**Paso 6:** Recolecta datos:

Después de implementar el formulario, puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar a recolectar datos con el formulario web.

**Pantalla de ingreso de datos en Enketo (formulario web): _cuando no se ha ingresado nada_.**

![Formulario Enketo vacío - enfoque Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_empty.png)

**Pantalla de ingreso de datos en Enketo (formulario web) con el tipo de pregunta `note` agregado: _cuando la pregunta `matrix` está completada_.**

![Formulario Enketo completado - enfoque Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_no_issue.png)

Como puedes ver en la imagen anterior, el formato de la pregunta `matrix` no se ha distorsionado. Así es como se mostrará la tabla `matrix` cuando uses el tipo de pregunta `note` que se resaltó en la imagen anterior.

**Pantalla de ingreso de datos en Enketo (formulario web) sin el tipo de pregunta `note` agregado: _cuando la pregunta `matrix` está completada_.**

![Formulario Enketo completado - enfoque Formbuilder](images/adding_skip_to_matrix/formbuilder_enketo_form_filled_with_issue.png)

En este caso, el formato de la pregunta `matrix` se ha distorsionado. Así es como se mostrará la tabla `matrix` cuando no se usa el tipo de pregunta `note`.

<p class="note">
  Puedes acceder al XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question.xls"
    >aquí</a
  >
  que se utilizó para este enfoque
  <em
    >(agregar lógica de omisión a una pregunta <code>matrix</code> usando el
    enfoque del Formbuilder)</em
  >.
</p>

## Enfoque `kobo--matrix_list`:

Al igual que con el enfoque del Formbuilder, este método para agregar lógica de omisión con un XLSForm funciona con **Enketo** usando el diseño de **tema de cuadrícula (Grid-theme)**.

Sigue los pasos a continuación para agregar lógica de omisión a una pregunta `matrix` con un XLSForm usando el enfoque `kobo--matrix_list`.

**Paso 1:** Crea una pregunta `matrix` en el XLSForm:

Crea una pregunta `matrix` en el XLSForm, como se describe en el artículo de ayuda **[Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)**.

**Paso 2:** Agrega el encabezado de columna `relevant` y la lógica de omisión a tu XLSForm:

Una vez que la pregunta `matrix` esté lista, debes agregar el encabezado de columna `relevant`. Ahora puedes agregar lógica de omisión a todas las preguntas bajo el encabezado de columna `relevant`.

![XLSForm enfoque kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_xlsform.png)

**Paso 3:** Carga el XLSForm:

Si tu XLSForm está listo, cárgalo como un nuevo proyecto.

**Paso 4:** Implementa el formulario:

Una vez que hayas cargado el XLSForm, deberás implementar tu formulario.

**Paso 5:** Recolecta datos:

Ahora puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar a recolectar datos.

**Pantalla de ingreso de datos en Enketo (formulario web): _cuando no se ha ingresado nada_.**

![Formulario Enketo vacío - enfoque kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_empty.png)

**Pantalla de ingreso de datos en Enketo (formulario web): _cuando la pregunta `matrix` está completada_.**

![Formulario Enketo completado - enfoque kobo_matrix](images/adding_skip_to_matrix/kobo_matrix_enketo_form_filled.png)

Como puedes ver en la segunda imagen, el formato de la pregunta `matrix` se ha distorsionado. Con el enfoque `kobo--matrix_list` no tienes la posibilidad de corregir la tabla `matrix` como sí la tenías con el enfoque del Formbuilder.

<p class="note">
  Puedes acceder al XLSForm
  <a
    download
    class="reference"
    href="./_static/files/adding_skip_to_matrix/adding_skip_to_a_matrix_question_kobo_matrix.xls"
    >aquí</a
  >
  que se utilizó para este enfoque
  <em
    >(agregar lógica de omisión a una pregunta <code>matrix</code> usando el
    enfoque <code>kobo--matrix_list</code>)</em
  >.
</p>