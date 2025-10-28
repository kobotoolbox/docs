# Adjuntos de datos dinámicos
<a href="../dynamic_data_attachment.html">Read in English</a> | <a href="../fr/dynamic_data_attachment.html">Lire en français</a> | <a href="../ar/dynamic_data_attachment.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/0c4cbe231491ab3ee9bd1e3a82967d30ac63e2c6/source/dynamic_data_attachment.md" class="reference">15 Oct 2025</a>

La vinculación dinámica te permite usar datos de un **proyecto principal** dentro de **proyectos secundarios**, simplificando el manejo de la recolección de datos longitudinales. Este artículo explica cómo vincular dinámicamente datos entre proyectos de KoboToolbox.

<p class="note">
    <strong>Nota:</strong> Los adjuntos de datos dinámicos funcionan de manera similar a la función <a href="https://support.kobotoolbox.org/es/pull_data_kobotoolbox.html"><code>pulldata()</code></a>, pero eliminan la necesidad de archivos CSV separados, ya que los datos de un proyecto principal vinculado sirven como fuente de datos.
</p>

Puedes recuperar varias **respuestas que no sean multimedia** de un proyecto principal y realizar cálculos sobre estos datos vinculados en un proyecto secundario. Esto puede ser útil para recuperar datos de línea base, información de contacto o registros de salud en estudios de cohorte, o para confirmar o verificar datos recolectados previamente.

Recomendamos usar [XLSForm](edit_forms_excel.md) para configurar adjuntos de datos dinámicos. Para ejemplos de proyectos principales y secundarios, descarga archivos de muestra [aquí](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/parent.xlsx) y [aquí](https://support.kobotoolbox.org/_static/files/dynamic_data_attachment/child.xlsx).

## Vincular proyectos dinámicamente en XLSForm

Vincular proyectos dinámicamente requiere un **proyecto principal** y al menos un **proyecto secundario**. El **proyecto principal** no requiere modificación de un XLSForm normal. Sin embargo, configurar el/los **proyecto(s) secundario(s)** implica los siguientes pasos:
1. En la hoja de cálculo `survey` de tu XLSForm, agrega una fila y establece el tipo de pregunta como `xml-external`.
2. En la columna `name`, proporciona un nombre corto para el formulario principal. Este nombre puede consistir en caracteres del alfabeto latino, guiones bajos y números.

**Hoja de cálculo survey**

| type | name     | label              |
| :--- | :------- | :----------------- |
| xml-external | parent |
| survey | 


3. A lo largo del formulario, puedes recuperar valores del proyecto principal creando una nueva pregunta e incluyendo la expresión apropiada en la columna `calculation` (ver tabla [a continuación](https://support.kobotoolbox.org/es/dynamic_data_attachment.html#calculation-syntax-for-dynamic-data-attachments)). Puedes usar los siguientes tipos de pregunta para recuperar datos:
    - Usa un tipo de pregunta **calculate** para recuperar y almacenar valores para uso futuro dentro del formulario o conjunto de datos (por ejemplo, para cálculos o etiquetas de preguntas dinámicas).
    - Usa tipos de pregunta **text**, **integer**, **decimal**, **select_one** o **select_multiple** para incluir valores recuperados como respuestas predeterminadas en campos editables. Los datos editados en el proyecto secundario no cambiarán los datos originales en el proyecto principal.
  
**Hoja de cálculo survey**
      
| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | parent |               |              |
| text | participant_id | ¿Cuál es el ID del/de la participante? |  |
| integer | age | Confirma la edad del/de la participante | instance('parent')/root/data[enrollment_id = current()/../participant_id]/age |
| survey | 

<p class="note">
   <strong>Nota:</strong> 
    Para mostrar datos vinculados sin permitir que los/as usuarios/as editen el campo, usa una pregunta <strong>calculate</strong> seguida de una pregunta <strong>note</strong> que muestre el valor calculado. Alternativamente, usa preguntas <strong>text</strong>, <strong>integer</strong>, <strong>decimal</strong>, <strong>select_one</strong> o <strong>select_multiple</strong> con la columna <code>read_only</code> establecida en <code>TRUE</code>.
</p>

## Sintaxis de cálculo para adjuntos de datos dinámicos

En la columna `calculation` de la fila donde se recuperarán los datos vinculados, incluye una de las expresiones en la tabla a continuación. Estas expresiones se llaman **XPaths**.

Para cada expresión en la tabla a continuación:

- `parent` es el nombre único asignado al **formulario principal** (por ejemplo, en la pregunta `xml-external` del **formulario secundario**).
- `parent_question` se refiere al `name` de una pregunta del **formulario principal**.
- `child_question` se refiere al `name` de una pregunta del **formulario secundario**.
- `parent_index_question` es la pregunta identificadora del **formulario principal** que lo vincula al **formulario secundario** (por ejemplo, ID único, nombre de organización).
- `child_index_question` es la pregunta identificadora del **formulario secundario** que lo vincula al **formulario principal** (por ejemplo, ID único, nombre de organización).
- `parent_group` se refiere al `name` del grupo en el **formulario principal** en el que se encuentra la `parent_question`.
- `parent_index_group` se refiere al `name` del grupo en el **formulario principal** en el que se encuentra la `parent_index_question`.

| **XPath**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Devuelve el número total de filas en el proyecto principal. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Devuelve el número total de filas en el proyecto principal donde `parent_question` (en `parent_group`) no está vacía. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question]` | Devuelve el recuento total de instancias donde el valor de `parent_question` (en `parent_group`) en el proyecto principal es igual al valor de `child_question` en el proyecto secundario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Devuelve el valor de `parent_question` (en `parent_group`) del proyecto principal donde `child_index_question` en el proyecto secundario es igual a `parent_index_question` en el proyecto principal. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Igual que arriba, pero especifica que solo se deben devolver datos de la primera instancia de `parent_index_question`, usando el argumento `[position() = 1]`. Se usa en caso de posibles duplicados en el formulario principal. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Devuelve la suma de valores de `parent_question` (en `parent_group`) del proyecto principal. Ten en cuenta que `parent_question` debe ser numérica. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Devuelve el valor máximo ingresado en `parent_question` (en `parent_group`) del proyecto principal. Ten en cuenta que `parent_question` debe ser numérica.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Devuelve el valor mínimo ingresado en `parent_question` (en `parent_group`) del proyecto principal. Ten en cuenta que `parent_question` debe ser numérica.     |   


<p class="note">
    <strong>Nota:</strong> Si la pregunta principal no está incluida en ningún grupo, omite <code>parent_group</code> de la expresión.
</p>

## Configurar proyectos para vinculación dinámica

Una vez que tus XLSForms estén configurados, inicia sesión en tu cuenta de KoboToolbox y sigue estos pasos:

1. Carga y despliega el **proyecto principal**, si aún no está desplegado. Asegúrate de que el proyecto principal tenga al menos un envío.
2. Habilita el intercambio de datos para el proyecto principal: 
    - En la pestaña **SETTINGS > Connect Projects** del proyecto principal, activa el interruptor **Data sharing** (deshabilitado por defecto) y haz clic en **ACKNOWLEDGE AND CONTINUE** en la ventana de confirmación. 
    - Todos los datos se comparten por defecto, pero puedes restringir variables específicas para compartir con proyectos secundarios haciendo clic en "Select specific questions to share".

<p class="note">
    <strong>Nota:</strong> Si los proyectos tienen diferentes propietarios/as, el/la propietario/a del proyecto principal debe <a href="managing_permissions.html">compartir el proyecto</a> con el/la propietario/a del proyecto secundario. Los permisos mínimos requeridos para que funcionen los adjuntos de datos dinámicos son <strong>View form</strong> y <strong>View submissions</strong>. Ten en cuenta que esto permite a los/as administradores/as del proyecto secundario ver todos los datos del proyecto principal.
</p>

3. Carga y despliega el **proyecto secundario**.
4. Conecta el proyecto secundario al proyecto principal: 
    - En la pestaña **SETTINGS > Connect Projects** del proyecto secundario, haz clic en "Select a different project to import data from". Un menú desplegable te permitirá seleccionar un proyecto principal para vincular. 
    - Renombra el proyecto principal vinculado al nombre de la pregunta `xml-external` definido en el XLSForm y haz clic en **IMPORT**. 
    - Luego puedes seleccionar preguntas específicas del proyecto principal para compartir con el proyecto secundario, o seleccionar todas las preguntas.
5. Si agregas nuevos campos al formulario principal y deseas usarlos en el proyecto secundario, vuelve a importar el proyecto principal en la configuración del proyecto secundario.

<p class="note">
    <strong>Nota:</strong> Los formularios solo pueden vincularse entre sí si están en el mismo servidor de KoboToolbox.
</p>

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzU4LPO7zv" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Vincular dinámicamente un formulario a sí mismo

Es posible que un proyecto principal y secundario sean el mismo proyecto. Los pasos son los mismos que los descritos anteriormente. Ejemplos de casos de uso incluyen:

- **Monitoreo diario**: Si un formulario se usa para encuestar a la misma persona a lo largo del tiempo, puedes vincularlo a sí mismo para contar envíos anteriores. Esto puede permitirte mostrar un mensaje (por ejemplo, "el monitoreo está completo") después de un cierto número de entradas o informar al/a la encuestador/a del número de formularios enviados, como se muestra en el ejemplo a continuación.

**Hoja de cálculo survey**

| type | name     | label              | calculation |
| :--- | :------- | :----------------- | :----------------- |
| xml-external | monitoring |               |              |
| text | participant_id | ¿Cuál es el ID del/de la participante? |  |
| calculate | count |  | count(instance('monitoring')/root/ data[monitoring/participant_id = current()/../participant_id]) |
| note | monitoring_note | Este/a participante ha sido encuestado/a ${count} veces. | |
| survey | 

- **Formulario de registro**: Al vincular un formulario de registro a sí mismo, puedes verificar si un/a usuario/a ya ha sido registrado/a. Esto puede permitirte generar un mensaje de error o agregar una restricción si ya está registrado/a, previniendo registros duplicados, como se muestra en el ejemplo a continuación.

**Hoja de cálculo survey**

| type | name     | label              | calculation | relevant | 
| :--- | :------- | :----------------- | :----------------- | :------------ |
| xml-external | registration |               |              | |
| text | customer_id | ¿Cuál es el número de ID del/de la cliente? |  | | 
| calculate | count |  | count(instance('registration')/root/ data[registration/customer_id = current()/../customer_id]) | |
| note | already_registered | Este/a cliente ya está registrado/a. Por favor cierra este formulario. | | ${count} > 0 |
| survey | 

## Recolectar y manejar datos con vinculación dinámica

Los datos para proyectos vinculados dinámicamente pueden recolectarse usando la [aplicación de Android de KoboCollect](kobocollect_on_android_latest.md) o [formularios web de Enketo](data_through_webforms.md).

Al recolectar datos, ten en cuenta lo siguiente:

- El proyecto principal debe tener al menos un envío para que el proyecto secundario funcione correctamente.
- Al recolectar datos en línea, hay un retraso de cinco minutos en la sincronización de nuevos datos del proyecto principal con el proyecto secundario.
- En modo sin conexión, descarga frecuentemente el proyecto secundario para asegurar la sincronización de datos con el proyecto principal.

<p class="note">
    <strong>Nota:</strong> Puedes <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">configurar la aplicación de Android de KoboCollect</a> para actualizar automáticamente los datos del proyecto principal cuando haya una conexión a internet disponible. Ve a <strong>Settings > Form management > Blank form update mode</strong> y selecciona <strong>Previously downloaded forms only</strong> o <strong>Exactly match server</strong>. Puedes establecer la frecuencia de descarga automática para que ocurra cada 15 minutos, cada hora, cada seis horas o cada 24 horas. Ten en cuenta que habilitar esta configuración puede aumentar el consumo de batería.
</p>

## Solución de problemas

<details>
<summary><strong>Error o falla al vincular formularios</strong></summary>
Los adjuntos de datos dinámicos no pueden conectarse a un proyecto principal vacío. Agrega al menos un envío al proyecto principal primero, luego vincula los formularios nuevamente.
</details>

<br>

<details>
<summary><strong>Los datos principales no se muestran en el formulario secundario</strong></summary>
Verifica que la sintaxis de cálculo en el formulario secundario sea correcta y que las preguntas relevantes estén compartidas en ambos proyectos. Si tu pregunta principal está en un grupo de preguntas, asegúrate de incluir el nombre del grupo en la expresión XPath. Ten en cuenta que los nuevos datos del proyecto principal tardan hasta cinco minutos en sincronizarse cuando estás en línea. Si agregas nuevos campos al formulario principal y deseas usarlos en el proyecto secundario, abre la configuración del proyecto secundario, vuelve a importar el proyecto principal y vuelve a desplegar.
</details>

<br>

<details>
<summary><strong>El formulario secundario carga lentamente</strong></summary>
Los adjuntos de datos dinámicos grandes pueden ralentizar la carga del formulario. Comparte solo las preguntas que el formulario secundario necesita en lugar de la lista completa de preguntas, luego vuelve a desplegar e intenta nuevamente.
</details>

<br>

<details>
<summary><strong>Los datos dinámicos no se actualizan en KoboCollect</strong></summary>
Si estás usando KoboCollect y recolectando datos sin conexión, los datos primero deben enviarse al proyecto principal y luego descargarse a tu dispositivo de recolección de datos para que funcione el adjunto de datos dinámicos. Ambos pasos requieren una conexión a internet. Descargar datos principales es similar a descargar una nueva versión de un formulario, y la aplicación de KoboCollect puede configurarse para <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">descargar automáticamente nuevos datos</a> con una frecuencia establecida. No se recomienda depender de adjuntos de datos dinámicos para datos recolectados sin conexión en un corto período de tiempo.
</details>

<br>

<details>
<summary><strong>El adjunto de datos dinámicos no funciona dentro de grupos de preguntas</strong></summary>
Para extraer datos dinámicos de un formulario principal a un formulario secundario con grupos de preguntas, asegúrate de que la pregunta índice (por ejemplo, el número de identificación) en el formulario secundario esté en el mismo grupo que el cálculo para los datos dinámicos. Consulta los archivos de muestra <a href="https://community.kobotoolbox.org/uploads/short-url/z5RpC1M3wj9716z9qQ8pWx9Pb4V.xlsx">Round 1 (Within Groups).xlsx</a> y <a href="https://community.kobotoolbox.org/uploads/short-url/8JZvWJcrCxzKBllQYglRyAVyk03.xlsx">Round 2 (Within Groups).xlsx</a> para un ejemplo de adjuntos de datos dinámicos dentro de grupos.
</details>

<br>

<details>
<summary><strong>Error al evaluar campos en KoboCollect</strong></summary>
Si tu formulario principal contiene envíos duplicados, puedes recibir un mensaje de error en KoboCollect que indica "Error evaluating field / XPath evaluation: type mismatch /This field is repeated". Para resolver este problema y extraer datos solo del primer envío que contenga un valor de índice específico, usa el argumento <code>[position()=1]</code>, como se muestra a continuación:
<br><br>
<code>instance('parent')/root/data[parent_index_group/parent_index_question = current()/../child_index_question][position()=1]/parent_group/parent_question</code>

</details>