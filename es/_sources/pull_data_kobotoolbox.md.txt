# Extraer datos de un archivo CSV externo
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/e1faceb429db5362522392101ee2d88578d98fc8/source/pull_data_kobotoolbox.md" class="reference">6 de mayo de 2026</a>

La función `pulldata()` en XLSForm te permite recuperar información de forma dinámica desde un archivo CSV externo mientras completas un formulario. Esto te permite hacer referencia a conjuntos de datos existentes y extraer automáticamente los detalles relacionados, evitando que los encuestadores tengan que volver a ingresar la misma información.

Por ejemplo, puedes usar `pulldata()` para:
- **Completar automáticamente información relacionada:** Cuando se ingresa un ID, código o clave, recuperar automáticamente los detalles vinculados, como un nombre, categoría o descripción.
- **Precargar datos de referencia:** Cargar información desde archivos externos para que los encuestadores solo necesiten recolectar datos nuevos o actualizados.

<p class="note">
    <strong>Nota:</strong> La función <code>pulldata()</code> usa archivos CSV externos como fuente de datos. Si quieres hacer referencia a datos de otro proyecto de KoboToolbox en lugar de un archivo CSV, puedes usar <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">conexión dinámica de proyectos</a>.
</p>

Usar `pulldata()` ayuda a reducir errores, ahorra tiempo durante la recolección de datos y garantiza que los formularios se mantengan coherentes con los conjuntos de datos de referencia externos. Esta función está disponible tanto en la <a href="https://support.kobotoolbox.org/es/data_collection_kobocollect.html">aplicación Android KoboCollect</a> como en los <a href="https://support.kobotoolbox.org/es/data_through_webforms.html">formularios web</a>. Recomendamos usar <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a> para configurar la función `pulldata()`.

Este artículo cubre los siguientes pasos para extraer datos de un archivo CSV externo:
- Configurar tu archivo CSV externo
- Configurar tu XLSForm
- Cargar tu archivo CSV externo en KoboToolbox

## Configurar tu archivo CSV externo

Para usar `pulldata()`, primero prepara un archivo CSV externo que contenga los datos de referencia que quieres recuperar. Cada fila debe representar un registro único (por ejemplo, un participante, una ubicación o un elemento), y el archivo debe incluir al menos dos columnas. Una columna debe contener la **variable índice** que coincida con los valores ingresados en tu formulario.

La **variable índice** actúa como la [clave primaria](https://en.wikipedia.org/wiki/Primary_key) que vincula tu XLSForm con el archivo CSV externo. Debe ser un identificador único que exista en ambos archivos, como un ID de participante, el nombre de un distrito u otro código de coincidencia.

Las columnas restantes pueden incluir cualquier detalle adicional que quieras recuperar, como nombres, categorías o descripciones. Asegúrate de que el archivo CSV esté limpio, con un formato consistente y guardado con la extensión `.csv`.

**Ejemplo: eligibility.csv**

| ID           | status          | age             |
|:-----------  |:----------------|:----------------|
| AH784N       | eligible        | 19              |
| DB839K       | ineligible      | 37              |
| SH849T       | eligible        | 42              |

<p class="note">
<strong>Nota:</strong> Para usar <code>pulldata()</code> con preguntas <code>select_one</code> o <code>select_multiple</code>, el valor en el archivo externo debe coincidir con el <strong>nombre de la opción</strong>, no con la etiqueta de la opción. Para preguntas <code>select_multiple</code>, enumera varios nombres de opciones separados por un espacio.
</p>

## Configurar tu XLSForm

Una vez que hayas configurado tu archivo CSV externo, configura tu XLSForm de la siguiente manera:

1. Asegúrate de que tu XLSForm incluya una pregunta que sirva como **variable índice**.
2. Agrega una nueva pregunta a tu formulario para recuperar datos del archivo externo, usando uno de los dos enfoques siguientes:
    * Agrega una pregunta `calculate` para recuperar y almacenar valores para usarlos posteriormente en el formulario o en el conjunto de datos. Por ejemplo, puedes usarla para mostrar un valor en una nota o en la etiqueta de una pregunta, o para usar el valor en cálculos y lógica de omisión.
    * Agrega una pregunta de tipo `text`, `integer`, `decimal`, `date`, `select_one` o `select_multiple` para incluir los valores recuperados como respuestas predeterminadas en campos editables.
3. En la columna `calculation` de tu nueva pregunta, usa la función **pulldata()** para especificar qué campo del CSV extraer. Usa la siguiente sintaxis: `pulldata('csv','pull_from', 'csv_index', ${survey_index})`.
    - `csv` es el nombre del archivo CSV, sin la extensión.
    - `pull_from` hace referencia a la columna de tu archivo CSV que contiene los datos que quieres importar a tu formulario.
- `csv_index` es la columna de tu archivo CSV que contiene la **variable índice**.
    - `survey_index` es el nombre de la pregunta en tu encuesta que contiene la **variable índice**.

  **hoja survey**

  | type      | name               | label                                      | calculation |
|:-----------|:------------------|:-------------------------------------------|:-------------|
| text       | respondent_id      | Respondent ID                              |              |
| calculate  | eligibility_status |                                            | pulldata('eligibility', 'status', 'ID', ${respondent_id}) |
| note       | eligibility_note   | Respondent is ${eligibility_status} for the study. |              |
| integer    | respondent_age     | Respondent age | pulldata('eligibility', 'age', 'ID', ${respondent_id}) |
| survey | 

En el ejemplo anterior, el cálculo recupera el valor de la columna `status` del archivo `eligibility.csv`, en la fila donde el `ID` del CSV coincide con el ID ingresado en la pregunta `respondent_id` de tu formulario. Luego, recupera y muestra la edad del encuestado desde la columna `age` del archivo `eligibility.csv`.

<p class="note">
<strong>Nota:</strong> Después de usar la función <code>pulldata()</code> para recuperar datos de un CSV externo, puedes hacer referencia a ese campo en condiciones de lógica de omisión, restricciones y etiquetas posteriores, igual que cualquier otro campo o cálculo.
</p>

## Cargar tu archivo CSV externo en KoboToolbox

El último paso para vincular tu archivo CSV externo a tu formulario es cargarlo en KoboToolbox. Para hacerlo:
1. Ve a **CONFIGURACIÓN** de tu proyecto y abre la ventana **Media**.
2. Carga el o los archivos CSV con el nombre exacto que usaste en tu XLSForm.
3. Implementa o reimplementa el formulario.

![Upload media](images/pull_data_kobotoolbox/upload_media.png)

<p class="note">
    Para obtener más información sobre cómo cargar archivos multimedia, consulta <a href="https://support.kobotoolbox.org/es/upload_media.html">Importar archivos multimedia a un proyecto</a>.
</p>

## Resolución de problemas

<details>
  <summary><strong>Las fuentes no latinas o los caracteres especiales no se muestran correctamente</strong></summary>
  Guarda tu archivo CSV en <strong>formato UTF-8</strong>. Esto garantiza que los dispositivos Android puedan mostrar correctamente texto no latino o caracteres especiales.
</details>

<br>

<details>
  <summary><strong>Los valores numéricos no funcionan como se espera</strong></summary>
  Todos los datos extraídos de un archivo CSV se tratan como texto. Para usar estos valores como números, aplica las <a href="https://support.kobotoolbox.org/es/functions_xls.html">funciones</a> <code>int()</code> o <code>number()</code> al valor recuperado en tu XLSForm.
</details>

<br>

<details>
  <summary><strong>Proteger datos sensibles</strong></summary>
  Si tu CSV contiene información sensible que no quieres cargar en el servidor, carga un archivo CSV en blanco con tu formulario. Luego reemplázalo manualmente en cada dispositivo con el archivo CSV real. Este enfoque solo funciona con la aplicación KoboCollect.
</details>

<br>

<details>
  <summary><strong>Carga lenta del formulario con archivos grandes</strong></summary>
    Si usas archivos CSV muy grandes, es posible que experimentes una carga lenta del formulario en KoboCollect o en los formularios web. Para mejorar el rendimiento, incluye solo los datos necesarios para el formulario y considera dividir un formulario grande en varios formularios, cada uno con su propio archivo CSV. También puedes dividir los archivos CSV grandes en archivos más pequeños cuando sea posible, y/o usar la columna <a href="https://support.kobotoolbox.org/es/question_options_xls.html#additional-question-options">trigger</a> para extraer datos solo del archivo relevante y solo cuando sea necesario.
</details>

<br>

<details>
  <summary><strong>Extraer fechas de archivos CSV externos</strong></summary>
  Si almacenas fechas en un archivo CSV externo y quieres extraerlas a un formulario, asegúrate de que estén en el formato AAAA-MM-DD. Si editas tu CSV en Excel, agrega una comilla simple <code>'</code> delante de la fecha para evitar el formato automático de fechas en Excel.
</details>

<br>

<details>
  <summary><strong>La función pulldata() no funciona correctamente</strong></summary>
  Si la función pulldata() no funciona correctamente, prueba lo siguiente:
  <ul>
  <li>Cambia el nombre de tu archivo CSV para eliminar guiones bajos o símbolos especiales.</li>
  <li>Verifica que tu archivo CSV esté correctamente configurado con una variable por columna (consulta la publicación del <a href="https://community.kobotoolbox.org/t/pulldata-is-not-working-on-kobocollect-android/6462/39">Foro de la comunidad</a>).</li>
  <li>Verifica que estés usando la ortografía exacta para los nombres de archivos y de columnas.</li>
  <li>Verifica que las celdas de tu archivo CSV no incluyan espacios adicionales antes o después del valor.</li>
</ul>
</details>

<br>