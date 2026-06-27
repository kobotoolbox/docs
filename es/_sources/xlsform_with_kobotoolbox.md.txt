# Usar XLSForm con KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/2766eac60a2cfda9bee74f5ec77308dd80bfd029/source/xlsform_with_kobotoolbox.md" class="reference">6 de mayo de 2026</a>

XLSForm se integra fácilmente con KoboToolbox para crear, previsualizar, editar e implementar formularios para la recolección de datos. Por ejemplo, puedes comenzar a construir un formulario en el editor de formularios de KoboToolbox **(Formbuilder)** y luego descargarlo como XLSForm para personalizarlo con más detalle. Esto proporciona una base estructurada, útil para proyectos nuevos o para usuarios con menos experiencia en la elaboración de formularios.

Una vez personalizados, los formularios creados en XLSForm pueden cargarse en KoboToolbox para su revisión, modificación e implementación.

Este artículo cubre los siguientes temas:
- Descargar un XLSForm desde KoboToolbox
- Cargar y previsualizar un XLSForm en KoboToolbox
- Reemplazar un formulario existente con un XLSForm
- Importar un XLSForm a través de una URL
- Probar y validar tu XLSForm

## Descargar un XLSForm desde KoboToolbox

Al trabajar en KoboToolbox, es posible que necesites descargar tu formulario como XLSForm para hacer cambios de manera más eficiente, como duplicar muchas preguntas, editar listas de opciones extensas, agregar traducciones o usar funcionalidades avanzadas no disponibles en el Formbuilder. Además, descargar tu formulario como XLSForm te permite construir formularios sin conexión, compartirlos como archivos `.xlsx` para colaboración y manejo de versiones, y compartirlos con el equipo de soporte de KoboToolbox o en el Foro de la comunidad para solicitar asistencia.

Cualquier formulario creado con el Formbuilder de KoboToolbox puede descargarse como archivo XLSForm:

1. Ve a la página **FORMULARIO** de tu proyecto en KoboToolbox.
2. Haz clic en el icono <i class="k-icon k-icon-more"></i> **Otras acciones**.
3. Selecciona <i class="k-icon k-icon-xls-file"></i> **Download XLS**.

![Menú Download XLS](images/xlsform_with_kobotoolbox/download_xls.png)

## Cargar un XLSForm en KoboToolbox

También es posible que necesites crear un nuevo proyecto a partir de un XLSForm que hayas creado desde cero o que te hayan compartido.

Para cargar y previsualizar un XLSForm en un nuevo proyecto en KoboToolbox:

1. Ve a la página de proyectos en KoboToolbox y haz clic en **NUEVO**.
2. Selecciona **Cargar un XLSForm** y carga tu archivo Excel.
3. Ingresa los detalles del proyecto y haz clic en **Crear proyecto**.
4. Haz clic en el botón <i class="k-icon k-icon-view"></i> **Vista previa** para previsualizar tu formulario.

![Cuadro de diálogo para cargar XLSForm](images/xlsform_with_kobotoolbox/upload_xls.png)

## Reemplazar un formulario con un XLSForm

Una vez creado un proyecto, puedes reemplazar cualquier formulario existente con un XLSForm actualizado:

1. Ve a la página **FORMULARIO** de tu proyecto en KoboToolbox.
2. Haz clic en <i class="k-icon k-icon-replace"></i> **Reemplazar formulario** en la esquina superior derecha.
3. Selecciona **Cargar un XLSForm** y carga tu archivo Excel.

![Cuadro de diálogo para reemplazar el formulario](images/xlsform_with_kobotoolbox/replace_form.png)

## Importar un XLSForm a través de una URL

Si usas Google Sheets o almacenas el archivo en Dropbox, puedes importar un XLSForm a través de una URL. La URL debe ser de acceso público e iniciar una descarga del archivo al abrirse en un navegador para que la importación funcione. Los XLSForms también pueden importarse desde software similar, como Excel Web y OneDrive.

<details><summary><strong>Obtener un enlace desde Google Sheets</strong></summary>

Para obtener la URL correcta de una hoja de cálculo de Google Sheets:

1. Haz clic en **Archivo > Compartir > Publicar en la web**.
2. En el menú desplegable **Página web**, selecciona **Microsoft Excel (.xlsx)**. Mantén seleccionado **Documento completo** en el primer menú desplegable.
3. Haz clic en **Publicar**.
4. Copia el enlace del documento resultante.

<p class="note">
Para más información, consulta la <a href="https://support.google.com/docs/answer/183965?hl=en&co=GENIE.Platform%3DDesktop">documentación de Google Sheets</a>.
</p>

</details>

<br>

<details><summary><strong>Obtener un enlace desde Dropbox</strong></summary>

Para obtener la URL correcta de una hoja de cálculo almacenada en Dropbox:

1. Copia el enlace del archivo en Dropbox haciendo clic en <i class="k-icon k-icon-link"></i> **Copiar enlace**.
2. Al final del enlace, reemplaza el sufijo ``dl=0`` por ``dl=1``. Esta será la URL para importar en KoboToolbox.

</details>

<br>

Una vez obtenida la URL del archivo, puedes importar tu XLSForm en KoboToolbox:

1. Ve a la página de proyectos en KoboToolbox y haz clic en **NUEVO**.
2. Selecciona **Importar un XLSForm a través de URL**.
3. Pega tu URL y haz clic en **Importar**.
4. Ingresa los detalles del proyecto y haz clic en **Crear proyecto**.

![Cuadro de diálogo para importar XLSForm a través de URL](images/xlsform_with_kobotoolbox/import_via_url.png)

<p class="note">
    <b>Nota:</b> Los cambios realizados en un archivo en Dropbox o Google Sheets no se actualizan automáticamente en KoboToolbox. Debes volver a importar el XLSForm a través de la URL y volver a implementar los cambios del formulario.
</p>

## Probar y validar tu XLSForm

Validar, previsualizar y probar tu XLSForm es fundamental para garantizar su integridad estructural, funcionalidad y experiencia de usuario. Cada uno de estos pasos ayuda a identificar errores o problemas que podrían impedir que el formulario funcione correctamente.

| Paso | Descripción |
| :--- | :--- |
| Validar | Consiste en cargar el formulario y verificar si hay errores (por ejemplo, errores ortográficos o de capitalización, expresiones de lógica de formulario incorrectas, referencias a preguntas incorrectas, etiquetas faltantes). Los mensajes de error del formulario suelen aparecer al cargarlo, implementarlo o abrirlo. |
| Previsualizar | Permite visualizar el formulario tal como se mostrará a los encuestados y verificar que todos los elementos funcionen correctamente antes de la implementación (por ejemplo, el diseño del formulario, las etiquetas de preguntas y opciones). |
| Probar | Consiste en ingresar datos para probar la funcionalidad del formulario (por ejemplo, verificar los aspectos de las preguntas, las opciones de respuesta y la lógica del formulario). Las pruebas pueden realizarse en el modo **VISTA PREVIA** antes de la implementación. |

Validar y probar continuamente tu XLSForm a medida que realizas cambios simplificará la resolución de problemas y ayudará a identificar la causa de cualquier inconveniente. Es fundamental asegurarse de que el formulario funcione como se espera antes de iniciar la recolección de datos.

Al previsualizar y probar tu formulario, usa la misma plataforma que utilizarás para la recolección de datos: [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html), [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html), o ambos.

<p class="note">
Para obtener más información sobre cómo configurar KoboCollect para previsualizar y probar tus formularios, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html">Configurar la aplicación KoboCollect</a>.
</p>

Si tienes dificultades para encontrar el origen de un error en tu XLSForm, intenta cargar el formulario en [XLSForm Online](https://getodk.org/xlsform/) de ODK, que a menudo puede proporcionar mensajes de error y advertencias más detallados para ayudarte a identificar y corregir problemas antes de cargar el formulario en KoboToolbox.

## Resolución de problemas

<details>
<summary><strong>Mensaje de error al cargar, previsualizar o implementar un XLSForm</strong></summary>

Si tu XLSForm contiene un error, aparecerá un mensaje de error que generalmente indica la fila, pregunta o expresión exacta donde se encuentra el problema. Después de corregir el error en tu hoja de cálculo, deberás cargar el archivo nuevamente.

| Mensajes de error comunes | Explicación común |
| :--- | :--- |
| `The survey sheet is either empty or missing important column headers.` | Faltan encabezados de columna obligatorios o están mal escritos. |
| `The survey element named 'name' has no label or hint.` | Una de las preguntas del formulario no tiene etiqueta de pregunta. |
| `FormLogicError: Could not evaluate: [expression], message: The string did not match the expected pattern.` | Una expresión de lógica del formulario contiene errores, como una sintaxis incorrecta de referencia a preguntas o un paréntesis faltante. |
| `unable to deploy ODK Validate Errors: >> XForm is invalid` | Una expresión de lógica del formulario contiene errores, como una sintaxis incorrecta de referencia a preguntas o un paréntesis faltante. |
| `There has been a problem trying to replace ${question} with the XPath to the survey element named 'question'. There is no survey element with this name.` | Estás haciendo referencia a una pregunta del formulario que no existe o está mal escrita. Asegúrate de usar el nombre **exacto** de la pregunta en tus expresiones de lógica del formulario. |
| `'list_name'`<br>`​​List name not in choices sheet` | La lista de opciones de una pregunta no ha sido definida, o hay un error tipográfico en el `list_name`. |
| `Choice names must be unique for each choice list. If this is intentional, use the setting 'allow_choice_duplicates'.` | Se han usado nombres de opciones duplicados dentro de la misma lista de opciones. Elimina los nombres de opciones duplicados, o permite duplicados en la <a href="https://support.kobotoolbox.org/es/form_settings_xls.html#available-form-settings-in-xlsform">configuración del formulario</a>. |
| `Unmatched begin statement: group (group)` | Al grupo de preguntas le falta su fila `end_group` correspondiente. |
| `Can't find external_file.csv` <br> `Failed to load external_file.csv.` | Un <a href="https://support.kobotoolbox.org/es/pull_data_kobotoolbox.html">archivo adjunto externo</a> vinculado a tu formulario (por ejemplo, al usar `pulldata()`) no ha sido cargado en KoboToolbox. |
| `Can't find survey.xml` | Los <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">archivos adjuntos de datos dinámicos</a> no han sido configurados correctamente en los ajustes de tu proyecto. |
| `'select_from_list_name'` | Falta un nombre de lista en la columna `type` después de `select_one` o `select_multiple`. |

</details>

<br>

<details>
<summary><strong>Mensaje de error: Choice names must be unique for each choice list</strong></summary>
<br>

![Mensaje de error nombre inválido](images/xlsform_with_kobotoolbox/error-message-invalid-name.png)

Este error significa que hay al menos dos filas en la misma lista de <strong>choices</strong> que comparten el mismo valor en la columna <strong>name</strong>.

Por ejemplo:

| list_name | name | label |
|:---|:---|:---|
| yn | yes | Yes, always |
| yn | yes | Yes, sometimes |
| yn | no | No, never |
| choices |

Para corregir los nombres de opciones duplicados:
1. Abre tu XLSForm.
2. Ve a la hoja `choices`.
3. Encuentra el número de fila indicado en el mensaje de error.
4. Revisa la columna `name` para detectar valores duplicados dentro del mismo `list_name`.
5. Actualiza el valor `name` duplicado para que cada `name` en la lista sea único.
5. Guarda el archivo y luego <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#replacing-a-form-with-an-xlsform">cárgalo</a> y vuelve a implementar el formulario.

Si los valores `name` duplicados son intencionales (por ejemplo, al usar [Agregar filtros de selección a un XLSForm](https://support.kobotoolbox.org/es/choice_filters_xls.html)), puedes permitir duplicados en la [configuración del formulario](https://support.kobotoolbox.org/es/form_settings_xls.html#available-form-settings-in-xlsform).

</details>

<br>

<details>
<summary><strong>Mensaje de error: List name not in choices sheet</strong></summary>
<br>

![Mensaje de error nombre de lista](images/xlsform_with_kobotoolbox/error-message-list-name.png)

Este error ocurre cuando una pregunta usa una lista de opciones que no existe en la hoja `choices`, o el nombre de la lista en la columna `list_name` está mal escrito.

Por ejemplo:

**hoja survey**
| type | name | label |
|:---|:---|:---|
| select_one yes_no | service | Do you like the service at the supermarket? |
| survey |

**hoja choices**

| list_name | name | label |
|:---|:---|:---|
| yes_n | yes_always | Yes, always |
| yes_n | yes_sometimes | Yes, sometimes |
| yes_n | no | No, never |
| choices |

Para corregir el nombre de lista faltante o incorrecto:

<ol>
<li>Abre tu XLSForm.</li>
<li>Ve a la hoja <code>survey</code>.</li>
<li>Encuentra la pregunta que usa el nombre de lista indicado en el mensaje de error (por ejemplo, <code>select_one yes_no</code>).</li>
<li>Ve a la hoja <code>choices</code> y verifica la columna <code>list_name</code> para encontrar una coincidencia exacta con el nombre de lista indicado en el mensaje de error.</li>
<li>Realiza una de las siguientes acciones:
  <ul>
    <li><strong>Si falta el nombre de lista:</strong> Agrega una nueva lista de opciones para esa pregunta. Asegúrate de que el <code>list_name</code> esté escrito exactamente igual que en la hoja <code>survey</code>.</li>
    <li><strong>Si el nombre de lista existe pero está escrito de forma diferente:</strong> Corrige el error tipográfico para que el nombre de lista coincida exactamente en las hojas <code>survey</code> y <code>choices</code>.</li>
  </ul>
</li>
<li>Guarda el archivo y luego <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#replacing-a-form-with-an-xlsform">cárgalo</a> y vuelve a implementar el formulario.</li>
</ol>

</details>

<br>

<details>
<summary><strong>Dificultad para identificar el error en el XLSForm</strong></summary>
Si tienes dificultades para encontrar el origen de un error en tu XLSForm, intenta cargar el formulario en <a href="https://getodk.org/xlsform/">XLSForm Online</a> de ODK. Esta herramienta puede proporcionar mensajes de error y advertencias más detallados, lo que puede ayudarte a identificar y corregir problemas antes de cargar el formulario en KoboToolbox.

</details>

<br>

<details>
<summary><strong>Error al intentar importar un XLSForm a través de una URL</strong></summary>
Verifica que la URL que estás usando sea correcta. Al cargarse en un navegador, la URL debe iniciar una descarga del archivo, no abrir una página web.
</details>

<br>

<details>
<summary><strong>La importación a través de URL no carga la versión no implementada</strong></summary>
Si importaste un enlace y no ves la nueva versión del formulario, actualiza tu navegador.
</details>

<br>

<details>
<summary><strong>Fallo en el envío del formulario web</strong></summary>
Si falla el envío de un formulario web, verifica si tu formulario usa un <strong>término reservado de XLSForm</strong> en la columna <code>name</code>. Los términos reservados son palabras que no pueden usarse como nombres de preguntas porque el motor XForms subyacente los utiliza para estructura, lógica o análisis de datos (por ejemplo, type, label, start, today). El uso de estas palabras puede causar errores de validación del formulario, fallos en la publicación o problemas en la exportación de datos.<br><br>

Para corregir el problema, cambia el nombre de la pregunta afectada por otro valor y vuelve a implementar el formulario. Este problema generalmente afecta a los formularios web incluso cuando el formulario se abre con normalidad, mientras que KoboCollect puede seguir funcionando correctamente. Ten en cuenta que los envíos ya guardados con la versión anterior del formulario pueden quedar sin posibilidad de enviarse, por lo que es importante actualizar el formulario lo antes posible si estás recolectando datos a través de formularios web. Siempre <strong>prueba el envío del formulario antes de iniciar la recolección de datos</strong> para detectar problemas de nombres con anticipación.
</details>