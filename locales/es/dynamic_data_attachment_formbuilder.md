# Conexión dinámica de proyectos en el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/dynamic_data_attachment_formbuilder.md" class="reference">23 abr 2026</a>

La conexión dinámica te permite recuperar datos de un **proyecto primario** dentro de **proyectos secundarios**, simplificando la gestión de la recolección de datos longitudinales. 

Puedes recuperar varias **respuestas sin multimedia** de un proyecto primario y realizar cálculos sobre estos datos vinculados en un proyecto secundario. Esto puede ser útil para recuperar datos de referencia, información de contacto o registros de salud en estudios de cohortes, o para confirmar o verificar datos recolectados previamente. 

Este artículo explica cómo vincular dinámicamente datos entre proyectos de KoboToolbox dentro del editor de formularios de KoboToolbox (Formbuilder). 

<p class="note">
<strong>Nota:</strong> Puede ser más fácil usar XLSForm para configurar la conexión dinámica de proyectos. Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">Conexión dinámica de proyectos usando XLSForms</a>.
</p>

## Vincular proyectos dinámicamente en el Formbuilder

Vincular proyectos dinámicamente requiere un **proyecto primario** y al menos un **proyecto secundario.** El **proyecto primario** no requiere modificación respecto a un formulario normal de KoboToolbox. Sin embargo, configurar el **proyecto secundario** implica los siguientes pasos:

Primero, agrega una pregunta **XML externo** a tu formulario secundario. Esto vincula el formulario primario con el formulario secundario. Para hacerlo:

1. Haz clic en el botón <i class="k-icon-plus"></i>. 
2. Haz clic en **+ AGREGAR PREGUNTA.**
3. Elige el tipo de pregunta <i class="k-icon-qt-external-xml"></i> **XML externo**.
4. En lugar de la etiqueta de la pregunta, proporciona un nombre corto para el formulario primario. Este nombre puede consistir en caracteres del alfabeto latino, guiones bajos y números.

![Seleccionar pregunta XML externo](images/dynamic_data_attachment_formbuilder/external_xml.png)

Luego, a lo largo del formulario, puedes recuperar valores del proyecto primario usando preguntas **Cálculo**: 

1. Haz clic en el botón <i class="k-icon-plus"></i>. 
2. Haz clic en **+ AGREGAR PREGUNTA.**
3. Elige el tipo de pregunta <i class="k-icon-qt-calculate"></i> **Cálculo**.
4. En lugar de la etiqueta de la pregunta, incluye una expresión de cálculo para recuperar los datos del proyecto primario (consulta la tabla [a continuación](#sintaxis-de-cálculo-para-la-conexión-dinámica-de-proyectos)).

Después de recuperar los datos del proyecto primario en una pregunta **Cálculo**, puedes hacer referencia a ellos en otras partes de tu formulario, incluyendo en etiquetas de preguntas, notas o lógica del formulario, usando el [formato de pregunta de referencia](https://support.kobotoolbox.org/es/form_logic.html#question-referencing) estándar.

![Recuperar datos de pregunta de cálculo](images/dynamic_data_attachment_formbuilder/example.png)

<p class="note">
Para obtener más información sobre cálculos en el Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/calculate_questions.html">Agregar cálculos con el Formbuilder</a>.
</p>

## Sintaxis de cálculo para la conexión dinámica de proyectos

En el campo **etiqueta de la pregunta** de la pregunta Cálculo donde se recuperarán los datos vinculados, incluye una de las expresiones de la tabla a continuación. Estas expresiones se llaman **XPaths.**

Para cada expresión en la tabla a continuación:

- `parent` es el nombre único asignado al **formulario primario** (en la pregunta XML externo del **formulario secundario**).
- `parent_question` se refiere al nombre de columna de datos de una pregunta del **formulario primario.**
- `child_question` se refiere al nombre de columna de datos de una pregunta del **formulario secundario.**
- `parent_index_question` es la pregunta de identificación del **formulario primario** que lo vincula con el **formulario secundario** (por ejemplo, ID único, nombre de la organización).
- `child_index_question` es la pregunta de identificación del **formulario secundario** que lo vincula con el **formulario primario** (por ejemplo, ID único, nombre de la organización).
- `parent_group` se refiere al nombre de columna de datos del grupo en el **formulario primario** en el que se encuentra `parent_question`.
- `parent_index_group` se refiere al nombre de columna de datos del grupo en el **formulario primario** en el que se encuentra `parent_index_question`.

| **XPath**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| `count(instance('parent')/root/data)` | Devuelve el número total de filas en el proyecto primario. |
| `count(instance('parent')/root/ data[parent_group/parent_question])`      | Devuelve el número total de filas en el proyecto primario donde `parent_question` (en `parent_group`) no está vacío. |
| `count(instance('parent')/root/ data[parent_group/parent_question= current()/../child_question])` | Devuelve el recuento total de instancias donde el valor de `parent_question` (en `parent_group`) en el proyecto primario es igual al valor de `child_question` en el proyecto secundario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question]/parent_group/ parent_question` | Devuelve el valor de `parent_question` (en `parent_group`) del proyecto primario donde `child_index_question` en el proyecto secundario es igual a `parent_index_question` en el proyecto primario. |
| `instance('parent')/root/ data[parent_index_group/parent_index_question= current()/../child_index_question][position()= 1]/parent_group/parent_question` | Igual que el anterior, pero especifica que solo se deben devolver datos de la primera instancia de `parent_index_question`, usando el argumento `[position() = 1]`. Se usa en caso de posibles duplicados en el formulario primario. |
| `sum(instance('parent')/root/ data/parent_group/parent_question)` | Devuelve la suma de valores de `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérico. |
| `max(instance('parent')/root/ data/parent_group/parent_question)`         | Devuelve el valor máximo ingresado en `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérico.     |
| `min(instance('parent')/root/ data/parent_group/parent_question)`      | Devuelve el valor mínimo ingresado en `parent_question` (en `parent_group`) del proyecto primario. Ten en cuenta que `parent_question` debe ser numérico.     |   

<p class="note">
<strong>Nota:</strong> Si la pregunta del proyecto primario no está incluida en ningún grupo, omite <code>parent_group/</code> de la expresión. 
</p>

## Configurar proyectos para la vinculación dinámica

<iframe src="https://www.youtube.com/embed/pBqEsFlxqE4?si=6BPiDgOzO4LPO7zv&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Una vez que tus proyectos primario y secundario estén configurados e implementados en KoboToolbox, sigue estos pasos:

1. Habilita el uso compartido de datos para el proyecto primario: 
    - En la ventana **CONFIGURACIÓN > Conectar proyectos** del proyecto primario, activa el interruptor **Compartir datos** (desactivado de forma predeterminada) y haz clic en **CONFIRMAR Y CONTINUAR** en la ventana de confirmación. 
    - Todos los datos se comparten de forma predeterminada, pero puedes restringir variables específicas para compartir con proyectos secundarios haciendo clic en "Seleccionar las preguntas específicas a compartir".

<p class="note">
    <strong>Nota:</strong> Si los proyectos tienen diferentes propietarios, el propietario del proyecto primario debe <a href="https://support.kobotoolbox.org/es/managing_permissions.html">compartir el proyecto</a> con el propietario del proyecto secundario. Los permisos mínimos requeridos para que la conexión dinámica de proyectos funcione son <strong>Visualizar el formulario</strong> y <strong>Ver envíos</strong>. Ten en cuenta que esto permite a los administradores del proyecto secundario ver todos los datos del proyecto primario.
</p>

2. Conecta el proyecto secundario al proyecto primario:
    - En la ventana **CONFIGURACIÓN > Conectar proyectos** del proyecto secundario, haz clic en "Seleccionar un proyecto diferente desde el cual importar datos". Un menú desplegable te permitirá seleccionar un proyecto primario para vincular.
    - Cambia el nombre del proyecto primario vinculado a la etiqueta de la pregunta XML externo definida en el Formbuilder y haz clic en **IMPORTAR.**
    - Luego puedes seleccionar preguntas específicas del proyecto primario para compartir con el proyecto secundario (recomendado), o seleccionar todas las preguntas.
3. Si agregas nuevos campos al formulario primario y deseas usarlos en el proyecto secundario, vuelve a importar el proyecto primario en la configuración del proyecto secundario.

<p class="note">
<strong>Nota:</strong> Los formularios solo se pueden vincular entre sí si están en el mismo servidor de KoboToolbox.
</p>

## Vincular dinámicamente un formulario consigo mismo

Es posible que un proyecto primario y un proyecto secundario sean el mismo proyecto. Los pasos son los mismos que los descritos anteriormente. Ejemplos de casos de uso incluyen: 

- **Seguimiento diario:** Si se usa un formulario para encuestar a la misma persona a lo largo del tiempo, puedes vincularlo consigo mismo para contar los envíos anteriores. Esto puede permitirte mostrar un mensaje (por ejemplo, "el seguimiento está completo") después de un cierto número de entradas o informar al encuestador del número de formularios enviados, como se muestra en el ejemplo a continuación.

![Seguimiento diario de una encuesta](images/dynamic_data_attachment_formbuilder/monitoring.png)

- **Formulario de registro:** Al vincular un formulario de registro consigo mismo, puedes verificar si un usuario ya ha sido registrado. Esto puede permitirte generar un mensaje de error o agregar [criterios de validación](https://support.kobotoolbox.org/es/validation_criteria.html) si ya están registrados, evitando registros duplicados.

## Recolectar y gestionar datos con vinculación dinámica

Los datos de proyectos vinculados dinámicamente se pueden recolectar usando la [aplicación Android KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html) o [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html).

Al recolectar datos, ten en cuenta lo siguiente:

- El proyecto primario debe tener al menos un envío para que el proyecto secundario funcione correctamente.
- Al recolectar datos en línea, hay un retraso de cinco minutos en la sincronización de nuevos datos del proyecto primario con el proyecto secundario.
- En modo sin conexión a internet, descarga con frecuencia el proyecto secundario para garantizar la sincronización de datos con el proyecto primario.

Puedes [configurar la aplicación Android KoboCollect](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings) para actualizar automáticamente los datos del proyecto primario cuando haya una conexión a Internet disponible:

1. Ve a **Ajustes > Manejo de formularios > Modo de actualización de formulario en blanco**
2. Selecciona **Solo formularios descargados previamente** o **Coincidencia exacta de servidor.**
3. Configura la frecuencia de descarga automática para que ocurra cada 15 minutos, cada hora, cada seis horas o cada 24 horas. Ten en cuenta que habilitar esta configuración puede aumentar el consumo de batería.

<p class="note">
<strong>Nota:</strong> Para aprender cómo configurar la conexión dinámica de proyectos en XLSForm y para obtener soporte adicional de solución de problemas, consulta <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">Conexión dinámica de proyectos usando XLSForms</a>.
</p>