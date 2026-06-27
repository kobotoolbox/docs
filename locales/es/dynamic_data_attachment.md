# Conexión dinámica de proyectos usando XLSForms
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/8f9a856ca94d358f333f60f6e563a9ecbb879202/source/dynamic_data_attachment.md" class="reference">6 de mayo de 2026</a>


La conexión dinámica te permite usar datos de un **proyecto primario** dentro de **proyectos secundarios**, lo que simplifica el manejo de la recolección de datos longitudinales. Este artículo explica cómo conectar dinámicamente datos entre proyectos de KoboToolbox.

<p class="note">
    <strong>Nota:</strong> Las conexiones dinámicas de proyectos funcionan de manera similar a la función <a href="https://support.kobotoolbox.org/es/pull_data_kobotoolbox.html"><code>pulldata()</code></a>, pero eliminan la necesidad de archivos CSV separados, ya que los datos del proyecto primario vinculado sirven como fuente de datos.
</p>

Puedes recuperar diversas **respuestas sin multimedia** de un proyecto primario y realizar cálculos sobre estos datos vinculados en un proyecto secundario. Esto puede ser útil para recuperar datos de referencia, información de contacto o registros de salud en estudios de cohorte, o para confirmar o verificar datos recolectados previamente.

Recomendamos usar [XLSForm](https://support.kobotoolbox.org/es/edit_forms_excel.html) para configurar las conexiones dinámicas de proyectos. Para ver ejemplos de proyectos primarios y secundarios, descarga los archivos de ejemplo [aquí](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) y [aquí](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx). Para aprender a configurar conexiones dinámicas de proyectos en el Formbuilder de KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment_formbuilder.html">Conexión dinámica de proyectos en el Formbuilder</a>.

## Conectar proyectos dinámicamente en XLSForm

La conexión dinámica de proyectos requiere un **proyecto primario** y al menos un **proyecto secundario**. El **proyecto primario** no requiere ninguna modificación respecto a un XLSForm normal. Sin embargo, la configuración del o los **proyectos secundarios** implica los siguientes pasos:
1. En la **hoja survey** de tu XLSForm, agrega una fila y define el tipo de pregunta como `xml-external`.
2. En la columna `name`, proporciona un nombre corto para el formulario primario. Este nombre puede contener caracteres del alfabeto latino, guiones bajos y números.

**hoja survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. A lo largo del formulario, puedes recuperar valores del proyecto primario creando una nueva pregunta e incluyendo la expresión adecuada en la columna `calculation` (consulta la tabla [a continuación](https://support.kobotoolbox.org/es/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). Puedes usar los siguientes tipos de preguntas para recuperar datos:
    - Usa el tipo de pregunta `calculate` para recuperar y almacenar valores para uso futuro dentro del formulario o conjunto de datos (por ejemplo, para cálculos o etiquetas de preguntas dinámicas).
    - Usa los tipos de pregunta `text`, `integer`, `decimal`, `date`, `select_one` o `select_multiple` para incluir los valores recuperados como respuestas predeterminadas en campos editables. Los datos editados en el proyecto secundario no modificarán los datos originales del proyecto primario.

**hoja survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | What is the participant's ID? |  |
| integer | age | Confirm the participant's age | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Nota:</strong> 
    Para mostrar datos vinculados sin permitir que los usuarios editen el campo, usa una pregunta <code>calculate</code> seguida de una pregunta <code>note</code> que muestre el valor calculado. También puedes usar preguntas <code>text</code>, <code>integer</code>, <code>decimal</code>, <code>select_one</code> o <code>select_multiple</code> con la columna <code>read_only</code> configurada como <code>TRUE</code>.
</p>

## Sintaxis de cálculo para conexiones dinámicas de proyectos

En la columna `calculation` de la fila donde se recuperarán los datos vinculados, incluye una de las expresiones de la tabla a continuación. Estas expresiones se denominan **XPaths**.

Para cada expresión de la tabla a continuación:

- `parent` es el nombre único asignado al **formulario primario** (por ejemplo, en la pregunta `xml-external` del **formulario secundario**).
- `parent_question` hace referencia al `name` de una pregunta del **formulario primario**.
- `child_question` hace referencia al `name` de una pregunta del **formulario secundario**.
- `parent_index_question` es la pregunta identificadora del **formulario primario** que lo vincula al **formulario secundario** (por ejemplo, un ID único o el nombre de la organización).
- `child_index_question` es la pregunta identificadora del **formulario secundario** que lo vincula al **formulario primario** (por ejemplo, un ID único o el nombre de la organización).
- `parent_group` hace referencia al `name` del grupo en el **formulario primario** en el que se encuentra `parent_question`.
- `parent_index_group` hace referencia al `name` del grupo en el **formulario primario** en el que se encuentra `parent_index_question`.

| **XPath**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Devuelve el número total de filas en el proyecto primario. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Devuelve el número total de filas en el proyecto primario donde `parent_question` (en `parent_group`) no está vacío. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question])` | Devuelve el recuento total de instancias donde el valor de `parent_question` (en `parent_group`) en el proyecto primario es igual al valor de `child_question` en el proyecto secundario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Devuelve el valor de `parent_question` (en `parent_group`) del proyecto primario donde `child_index_question` en el proyecto secundario es igual a `parent_index_question` en el proyecto primario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Igual que el anterior, pero especifica que solo se deben devolver los datos de la primera instancia de `parent_index_question`, usando el argumento `[position() = 1]`. Se usa en caso de posibles duplicados en el formulario primario. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Devuelve la suma de los valores de `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question must be numeric` |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Devuelve el valor máximo ingresado en `parent_questio`n (en parent_group) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérico.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Devuelve el valor mínimo ingresado en `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérico.     |   


<p class="note">
    <strong>Nota:</strong> Si la pregunta del formulario primario no está incluida en ningún grupo, omite <code>parent_group</code> de la expresión.
</p>

## Configurar proyectos para la conexión dinámica

Una vez que tus XLSForms estén configurados, inicia sesión en tu cuenta de KoboToolbox y sigue estos pasos:

1. Crea e implementa el **proyecto primario**, si aún no está implementado.
2. Activa el uso compartido de datos para el proyecto primario:
    - En la ventana **CONFIGURACIÓN > Conectar proyectos** del proyecto primario, activa el interruptor **Compartir datos** (desactivado por defecto) y haz clic en **CONFIRMAR Y CONTINUAR** en la ventana de confirmación.
    - Todos los datos se comparten por defecto, pero puedes restringir variables específicas para compartir con proyectos secundarios haciendo clic en "Seleccionar las preguntas específicas a compartir".

<p class="note">
    <strong>Nota:</strong> Si los proyectos tienen diferentes propietarios, el propietario del proyecto primario debe <a href="https://support.kobotoolbox.org/es/managing_permissions.html">compartir el proyecto</a> con el propietario del proyecto secundario. Los permisos mínimos requeridos para que las conexiones dinámicas de proyectos funcionen son <strong>Ver formulario</strong> y <strong>Ver envíos</strong>. Ten en cuenta que esto permite a los administradores del proyecto secundario ver todos los datos del proyecto primario.
</p>

3. Crea e implementa el **proyecto secundario**.
4. Conecta el proyecto secundario al proyecto primario:
    - En la ventana **CONFIGURACIÓN > Conectar proyectos** del proyecto secundario, haz clic en "Seleccionar un proyecto diferente desde el cual importar datos". Un menú desplegable te permitirá seleccionar un proyecto primario para vincular.
    - Cambia el nombre del proyecto primario vinculado al nombre de la pregunta `xml-external` definido en el XLSForm y haz clic en **IMPORTAR**.
    - Luego puedes seleccionar preguntas específicas del proyecto primario para compartir con el proyecto secundario (recomendado), o seleccionar todas las preguntas.
5. Si agregas nuevos campos al formulario primario y deseas usarlos en el proyecto secundario, vuelve a importar el proyecto primario en la configuración del proyecto secundario.

<p class="note">
    <strong>Nota:</strong> Los formularios solo pueden vincularse entre sí si están en el mismo servidor de KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Conectar un formulario consigo mismo dinámicamente

Es posible que un proyecto primario y un proyecto secundario sean el mismo proyecto. Los pasos son los mismos que los descritos anteriormente. Algunos ejemplos de casos de uso incluyen:

- **Monitoreo diario**: Si se usa un formulario para encuestar a la misma persona a lo largo del tiempo, puedes vincularlo consigo mismo para contar los envíos anteriores. Esto puede permitirte mostrar un mensaje (por ejemplo, "el monitoreo está completo") después de un cierto número de entradas, o informar al encuestador sobre el número de formularios enviados, como se muestra en el ejemplo a continuación.

**hoja survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | What is the participant's ID? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | This participant has been surveyed ${count} times. | |
| survey | 

- **Formulario de registro**: Al vincular un formulario de registro consigo mismo, puedes verificar si un usuario ya ha sido registrado. Esto puede permitirte generar un mensaje de error o agregar una restricción si ya está registrado, evitando registros duplicados, como se muestra en el ejemplo a continuación.

**hoja survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | What is the customer's ID number? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | This customer is already registered. Please close this form. | | ${count} > 0 |
| survey | 

## Recolectar y gestionar datos con conexión dinámica

Los datos de proyectos conectados dinámicamente pueden recolectarse usando la [aplicación Android KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html) o [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html).

Al recolectar datos, ten en cuenta lo siguiente:

- El proyecto primario debe tener al menos un envío para que el proyecto secundario funcione correctamente.
- Al recolectar datos en línea, hay un retraso de cinco minutos en la sincronización de los nuevos datos del proyecto primario con el proyecto secundario.
- En modo sin conexión, descarga el proyecto secundario con frecuencia para garantizar la sincronización de datos con el proyecto primario.

<p class="note">
    <strong>Nota:</strong> Puedes <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">configurar la aplicación Android KoboCollect</a> para que actualice automáticamente los datos del proyecto primario cuando haya conexión a internet disponible. Ve a <strong>Ajustes > Manejo de formularios > Modo de actualización de formulario en blanco</strong> y selecciona <strong>Solo formularios descargados previamente</strong> o <strong>Coincidencia exacta de servidor</strong>. Puedes configurar la frecuencia de descarga automática para que ocurra cada 15 minutos, cada hora, cada seis horas o cada 24 horas. Ten en cuenta que activar esta configuración puede aumentar el consumo de batería.
</p>

## Resolución de problemas

<details>
  <summary><strong>Error o fallo al vincular formularios</strong></summary>
Si la interfaz de usuario falla cuando intentas vincular formularios, verifica lo siguiente:
  <ul>
    <li>Tu XLSForm no incluye nombres de preguntas o grupos duplicados en la columna <code>name</code> de la <strong>hoja survey</strong>.</li>
    <li>Tu proyecto primario tiene al menos un envío.</li>
  </ul>
Si la interfaz de usuario sigue fallando, selecciona solo las preguntas que necesitas para conectar los formularios, en lugar de hacer clic en <strong>Seleccionar todo</strong>.
</details>

<br>

<details>
<summary><strong>Los datos del formulario primario no aparecen en el formulario secundario</strong></summary>
Verifica que la sintaxis de cálculo en el formulario secundario sea correcta y que las preguntas relevantes estén compartidas en ambos proyectos. Si tu pregunta del formulario primario está en un grupo de preguntas, asegúrate de incluir el nombre del grupo en la expresión XPath. Ten en cuenta que los nuevos datos del proyecto primario tardan hasta cinco minutos en sincronizarse cuando estás en línea. Si agregas nuevos campos al formulario primario y deseas usarlos en el proyecto secundario, abre la configuración del proyecto secundario, vuelve a importar el proyecto primario y vuelve a implementarlo.
</details>

<br>

<details>
<summary><strong>El formulario secundario carga lentamente</strong></summary>
Las conexiones dinámicas de proyectos de gran tamaño pueden ralentizar los formularios, especialmente al abrir un formulario web para un nuevo envío o al editar envíos existentes.<br><br>Si trabajas con un conjunto de datos grande, comparte solo las preguntas que el formulario secundario necesita en lugar de la lista completa de preguntas. También puedes considerar dividir el formulario primario en varios formularios, por ejemplo por distrito o región, o usar un enfoque diferente si el conjunto de datos es demasiado grande para las conexiones dinámicas de proyectos.
</details>

<br>

<details>
<summary><strong>Los datos dinámicos no se actualizan en KoboCollect</strong></summary>
Si usas KoboCollect y recolectas datos sin conexión, los datos primero deben enviarse al proyecto primario y luego descargarse en tu dispositivo de recolección de datos para que la conexión dinámica de proyectos funcione. Ambos pasos requieren conexión a internet. Descargar los datos del proyecto primario es similar a descargar una nueva versión de un formulario, y la aplicación KoboCollect puede configurarse para <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">descargar automáticamente nuevos datos</a> con una frecuencia determinada. No se recomienda depender de las conexiones dinámicas de proyectos para datos recolectados sin conexión en un período corto de tiempo.
</details>

<br>

<details>
<summary><strong>La conexión dinámica de proyectos no funciona dentro de grupos de preguntas</strong></summary>
Para extraer datos dinámicos de un formulario primario a un formulario secundario con grupos de preguntas, asegúrate de que la pregunta de índice (por ejemplo, el número de identificación) en el formulario secundario esté en el mismo grupo que el cálculo para los datos dinámicos. Consulta los archivos de ejemplo <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> y <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> para ver un ejemplo de conexiones dinámicas de proyectos dentro de grupos.
</details>

<br>

<details>
<summary><strong>Las conexiones dinámicas de proyectos no extraen valores de grupos de repetición</strong></summary>
Las conexiones dinámicas de proyectos no admiten actualmente la extracción directa de valores de grupos de repetición en un formulario primario. Si intentas recuperar un valor de un grupo de repetición, el formulario secundario puede devolver valores en blanco, recuperar solo la última entrada del grupo de repetición o no recuperar los datos esperados.<br><br>Como solución alternativa, puedes agregar una o más preguntas <code>calculate</code> fuera del grupo de repetición en el formulario primario y usarlas para <a href="https://support.kobotoolbox.org/es/repeat_groups_xls.html#retrieving-values-from-repeat-groups">almacenar los valores del grupo de repetición</a> necesarios en el formulario secundario. Luego, extrae estos valores calculados al formulario secundario en lugar de extraerlos directamente del grupo de repetición.<br><br>Para flujos de trabajo más complejos, puede que necesites reestructurar el formulario primario, dividir las entradas del grupo de repetición en envíos separados, o procesar los datos del formulario primario fuera de KoboToolbox y adjuntarlos como un <a href="https://support.kobotoolbox.org/es/pull_data_kobotoolbox.html">CSV externo</a>.
</details>

<br>

<details>
<summary><strong>La variable de índice del formulario primario está dentro de un grupo de repetición</strong></summary>
Las conexiones dinámicas de proyectos no admiten actualmente la vinculación de envíos desde grupos de repetición. Si la variable de índice en el formulario primario está dentro de un grupo de repetición, el formulario secundario no podrá hacer coincidir ni recuperar los datos esperados.<br><br>Para evitar este problema, coloca la variable de vinculación fuera del grupo de repetición siempre que sea posible. Si cada elemento repetido necesita vincularse a un formulario secundario, considera reestructurar el flujo de trabajo para que cada elemento se envíe como su propio envío del formulario primario, en lugar de como una entrada en un grupo de repetición.<br><br>Por ejemplo, en lugar de recolectar todos los miembros del hogar en un grupo de repetición dentro de un envío del hogar, podrías crear un formulario primario separado donde cada miembro del hogar se envíe como un envío individual con un ID único. El formulario secundario puede entonces usar ese ID para recuperar el envío correcto.
</details>

<br>

<details>
<summary><strong>Error al evaluar campos en KoboCollect</strong></summary>
Si tu formulario primario contiene envíos duplicados, es posible que recibas un mensaje de error en KoboCollect que indique "Error evaluating field / XPath evaluation: type mismatch /This field is repeated." Para resolver este problema y extraer datos solo del primer envío que contenga un valor de índice específico, usa el argumento <code>[position()=1]</code>, como se muestra a continuación:
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>

<br>

<details>
<summary><strong>No se pueden actualizar los valores recuperados de las conexiones dinámicas de proyectos</strong></summary>
Si estás extrayendo datos dinámicos a preguntas de tipo entero, texto o selección y deseas que estos campos permanezcan editables, agrega una columna <code>trigger</code> a tu XLSForm. En la fila que contiene la expresión de datos dinámicos, ingresa el `name` de la pregunta de índice del formulario secundario en la columna <code>trigger</code>.
<br><br>
Esto permite que el valor se edite manualmente. El valor se actualizará desde los datos del formulario primario solo cuando cambie la respuesta a la pregunta de índice.

</details>

<br>

<details>
<summary><strong>Aparecen nombres de opciones en lugar de etiquetas de opciones</strong></summary>
Al extraer datos de una pregunta <code>select_one</code> o <code>select_multiple</code>, las conexiones dinámicas de proyectos usarán el nombre de la opción, no la etiqueta de la opción.
Para mostrar la etiqueta de la opción en tu formulario secundario, usa uno de los siguientes enfoques:
      <ul>
<li>Extrae los datos a una pregunta de selección e incluye las etiquetas correspondientes en la ventana <code>choices</code>.</li>
<li>En el formulario primario, usa un <a href="https://support.kobotoolbox.org/es/calculations_xls.html#advanced-calculations">cálculo</a> <code>jr:choice-name()</code> para recuperar la etiqueta de la opción y luego extrae ese valor calculado al formulario secundario.</li>
  </ul>

</details>