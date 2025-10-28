# Añadir Cálculos y Restricciones en una Pregunta de Matriz
<a href="../calculations_constraints_matrix.html">Read in English</a> | <a href="../fr/calculations_constraints_matrix.html">Lire en français</a> | <a href="../ar/calculations_constraints_matrix.html">اقرأ باللغة العربية</a>

**Última actualización:**
<a href="https://github.com/kobotoolbox/docs/blob/aaabdac8ec257d3157ec2ab2ceae65130e8c12d4/source/calculations_constraints_matrix.md" class="reference">14
Abr 2022</a>

Cuando trabajas en el editor de formularios de KoboToolbox (Formbuilder), es sencillo
[añadir cálculos](calculate_questions.md) o
[restricciones](validation_criteria.md) a casi cualquier tipo de pregunta. Si bien el
editor de formularios actualmente no admite añadir estas funcionalidades a una pregunta
de matriz, puedes usar XLSForm para hacerlo. Los pasos que se enumeran a continuación en este artículo de ayuda
ilustrarán cómo puedes añadir cálculos y restricciones a una pregunta de matriz
usando XLSForm.

## Configurar la pregunta y los campos

**Paso 1: Crear una pregunta de matriz en el editor de formularios**

El primer paso es crear una pregunta de matriz en el editor de formularios (como se describe en
el artículo de ayuda [Tipo de Respuesta de Matriz de Preguntas](matrix_response.md)). Simplemente
añade filas y columnas con las variables necesarias para la recolección de datos.

**Paso 2: Descargar el formulario como XLSForm**

Una vez que se haya creado la pregunta de matriz, **GUARDA** el formulario y
[descárgalo como XLSForm](getting_started_xlsform.md#downloading-an-xlsform-from-kobotoolbox).

**Paso 3: Añadir lógica a la pregunta de matriz**

Abre el XLSForm y añade los encabezados de columna `calculation`, `constraint` y `constraint_message`. Con estos encabezados de columna, podrás añadir las expresiones de _total de columna_ y _total de fila_ bajo el encabezado de columna `calculation`. También
puedes añadir _restricciones_ apropiadas bajo el encabezado de columna `constraint` y
_mensaje de restricción_ bajo el encabezado `constraint_message` según sea necesario.

Además, también puedes optar por añadir un encabezado de columna `read_only` para restringir
que los/as encuestadores/as editen las respuestas mientras recolectan datos de ciertas
preguntas (por ejemplo, el _total de fila_ y _total de columna_ que se
calculan).

![Survey Tab](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">
  En la imagen anterior, puedes notar que las entradas de <code>name</code> son
  más cortas. En este ejemplo, se han renombrado de las generadas automáticamente
  en el editor de formularios para capturar la captura de pantalla completa de la pestaña survey. Si
  decides renombrar las tuyas, asegúrate de usar tus nuevos nombres de variables en los
  encabezados de columna <code>calculation</code> y <code>constraint</code>. Si el
  formulario ya ha sido desplegado y se han recolectado datos, se recomienda
  que <em>no</em> renombres las variables existentes.
</p>

**Paso 4: Reemplazar formulario**

Carga y reemplaza tu XLSForm dentro del proyecto existente, o crea un nuevo
proyecto (si es necesario).

**Paso 5: Desplegar formulario**

**Paso 6: Recolectar datos**

Después de desplegar el formulario, puedes ir a **FORMULARIO>Recolectar Datos>ABRIR** para comenzar
a recolectar datos con el formulario web.

## Ver el resultado

Las siguientes imágenes ilustran cómo se verá y funcionará el formulario en el
formulario web Enketo después de haber seguido los pasos anteriores:

**No se ingresan datos:**

![Enketo Nothing Entered](images/calculations_constraints_matrix/enketo_nothing_entered.png)

**Se comete un error de entrada:**

![Enketo Wrong Inputs Entered](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Aquí verás que hay solo cinco miembros totales del hogar. Si un/a
encuestador/a ingresa 6 para el número de hombres (0-14 Años), la restricción mostrará
un mensaje de error.

**Sin errores de entrada:**

![Enketo Correct Inputs Entered](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Aquí, cuando ingresas valores en una tabla de matriz, las filas y columnas se
calculan automáticamente.

<p class="note">
  Puedes descargar el XLSForm que se usó para este artículo
  <a
    download
    class="reference"
    href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx"
    >aquí</a
  >.
</p>

## Solución de problemas

-   La pregunta de matriz solo funciona con **formularios web Enketo**. No es
    compatible con **La aplicación de Android de KoboCollect**.

-   La tabla de matriz aparecerá distorsionada si no configuras el diseño como
    **Grid-theme**. Para más detalles sobre las apariencias de formularios web, puedes consultar
    [Usar Estilos Alternativos de Formularios Web Enketo](alternative_enketo.md).