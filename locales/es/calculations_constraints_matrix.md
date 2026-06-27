# Agregar cálculos y restricciones a una matriz de preguntas

Cuando se trabaja en el Formbuilder, es sencillo
[agregar cálculos](calculate_questions.md) o
[restricciones](validation_criteria.md) a casi cualquier tipo de pregunta. Si bien
el Formbuilder no admite actualmente agregar estas funcionalidades a una matriz de
preguntas, puedes usar XLSForm para hacerlo. Los pasos que se describen a continuación en este
artículo ilustran cómo agregar cálculos y restricciones a una matriz de
preguntas usando XLSForm.

## Configurar la pregunta y los campos

**Paso 1: Crear una matriz de preguntas en el Formbuilder**

El primer paso es crear una matriz de preguntas en el Formbuilder (como se describe en
el artículo [Agregar una matriz de preguntas usando el Formbuilder](matrix_response.md)). Simplemente
agrega filas y columnas con las variables necesarias para la recolección de datos.

**Paso 2: Descargar el formulario como XLSForm**

Una vez creada la matriz de preguntas, **GUARDA** el formulario y
[descárgalo como XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Paso 3: Agregar lógica a la matriz de preguntas**

Abre el XLSForm y agrega los encabezados de columna `calculation`, `constraint` y `constraint_message`.
Con estos encabezados de columna, podrás agregar las expresiones de _total de columna_
y _total de fila_ bajo el encabezado de columna `calculation`. También
puedes agregar las _restricciones_ correspondientes bajo el encabezado de columna `constraint` y
el _mensaje de restricción_ bajo el encabezado `constraint_message` según sea necesario.

Además, también puedes agregar un encabezado de columna `read_only` para impedir que los
encuestadores editen las respuestas durante la recolección de datos en ciertas
preguntas (por ejemplo, el _total de fila_ y el _total de columna_ que se
calculan automáticamente).

![Hoja survey](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  En la imagen anterior, es posible que notes que los valores de <code>name</code> son
  más cortos. En este ejemplo, se han renombrado respecto a los generados automáticamente
  en el Formbuilder para poder capturar la pantalla completa de la hoja survey. Si
  decides renombrar los tuyos, asegúrate de usar los nuevos nombres de variables en los
  encabezados de columna <code>calculation</code> y <code>constraint</code>. Si el
  formulario ya ha sido implementado y se han recolectado datos, se recomienda
  que <em>no</em> cambies el nombre de las variables existentes.
</p>

**Paso 4: Reemplazar el formulario**

Carga y reemplaza tu XLSForm en el proyecto existente, o crea un nuevo
proyecto (si es necesario).

**Paso 5: Implementar el formulario**

**Paso 6: Recolectar datos**

Después de implementar el formulario, puedes ir a **FORMULARIO>Recolectar datos>ABRIR** para comenzar
a recolectar datos con el formulario web.

## Ver el resultado

Las siguientes imágenes ilustran cómo se verá y funcionará el formulario en
el formulario web Enketo una vez seguidos los pasos anteriores:

**No se han ingresado datos:**

![Enketo sin datos ingresados](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Se ha cometido un error de ingreso:**

![Enketo con datos incorrectos ingresados](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Aquí verás que hay un total de cinco miembros del hogar. Si un
encuestador ingresa 6 como número de hombres (0-14 años), la restricción
mostrará un mensaje de error.

**Sin errores de ingreso:**

![Enketo con datos correctos ingresados](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Aquí, al ingresar valores en una tabla de matriz, las filas y columnas se
calculan automáticamente.

<p class="note">
  Puedes descargar el XLSForm utilizado en este artículo
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >aquí</a
  >.
</p>

## Resolución de problemas

-   La matriz de preguntas solo funciona con **formularios web Enketo**. No es
    compatible con la **aplicación Android KoboCollect**.

-   La tabla de matriz aparecerá distorsionada si no configuras el diseño como
    **Grid-theme**. Para más información sobre los estilos de formularios web, puedes consultar
    [Diseñar formularios web usando el Formbuilder](alternative_enketo.md).