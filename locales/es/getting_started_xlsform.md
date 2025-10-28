# Primeros pasos con XLSForm
<a href="../getting_started_xlsform.html">Read in English</a> | <a href="../fr/getting_started_xlsform.html">Lire en français</a> | <a href="../ar/getting_started_xlsform.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/8d0c50778ae17aa78829bafa85b7bf16ef00c45c/source/getting_started_xlsform.md" class="reference">10 Jun 2025</a>

Al crear formularios de encuesta para KoboToolbox, puedes construir tu formulario con el editor de formularios de KoboToolbox (Formbuilder) o en XLSForm. XLSForm es muy efectivo para crear formularios tanto básicos como avanzados en un formato fácil de usar.

Este artículo explica cómo:

-   Configurar un XLSForm usando Microsoft Excel
-   Cargar y previsualizar un XLSForm en KoboToolbox
-   Descargar un formulario creado con el editor de formularios de KoboToolbox como un XLSForm

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_xlsform_v2.mp4"
    type="video/mp4"
  />
</video>

<br/>

<p class="note">
  <b>Nota:</b> Algunas funcionalidades de XLSForm no están actualmente disponibles en el Formbuilder, pero pueden ser usadas para la construcción de formularios en XLSForm y luego cargarse a KoboToolbox. Esto puede ser especialmente útil para formularios complejos.
</p>

## Qué es XLSForm

XLSForm es un estándar para desarrollar formularios usando Microsoft Excel y otros programas de hojas de cálculo. Los XLSForms pueden luego cargarse a KoboToolbox para generar un formulario de recolección de datos.

Hay muchas ventajas al usar XLSForm, especialmente para construir formularios complejos con funcionalidades más avanzadas, incluyendo condiciones de relevancia, cálculos y restricciones. XLSForm también te permite colaborar en la construcción de formularios usando el mismo archivo de Excel o en tiempo real usando Google Sheets.

<p class="note">
  <b>Nota:</b> Para una introducción completa al desarrollo de formularios usando XLSForm, recomendamos el curso en línea a tu propio ritmo <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a> de KoboToolbox Academy.
</p>

## Configurar un XLSForm

Para configurar la estructura básica de un XLSForm:

1. Crea un libro de trabajo en Microsoft Excel o Google Sheets.
2. Crea tres hojas de trabajo: **survey**, **choices** y **settings**.
   - Los nombres de las hojas de trabajo deben estar en minúsculas.
3. En la hoja de trabajo **survey**, crea tres columnas con los encabezados: `type`,
   `name` y `label`.
4. En la hoja de trabajo **choices**, crea tres columnas con los encabezados:
   `list_name`, `name` y `label`.
5. La hoja de trabajo **settings** es opcional. Puede usarse para incluir especificaciones y personalizaciones adicionales del formulario.
   - Por ejemplo: `form_title`, `style` y `default_language`.

### Columnas obligatorias en XLSForm

#### Hoja de trabajo survey

| Nombre de columna | Descripción |
| :--- | :--- |
| type | Define el tipo de pregunta (por ejemplo, text, integer, select_one) |
| name | Define un nombre corto y único para referirse a cada pregunta |
| label | Define el texto de la pregunta tal como se mostrará en el formulario |

#### Hoja de trabajo choices

| Nombre de columna | Descripción |
| :--- | :--- |
| list_name | Define el identificador único para una lista de opciones de respuesta |
| name | Define un nombre corto y único para referirse a cada opción de respuesta |
| label | Define el texto de la opción tal como se mostrará en el formulario |

## Agregar preguntas

En XLSForm, las preguntas se agregan en la hoja de trabajo **survey**. El proceso paso a paso a continuación explica cómo agregar las siguientes preguntas de ejemplo: **¿Cuál es tu nombre?**, **¿Cuál es el sexo de tu bebé?** y **¿Cuántos años tienes?**

1. En la columna `type` de la hoja de trabajo survey, escribe **text**. Este es el tipo de pregunta para la primera pregunta, **¿Cuál es tu nombre?**
2. En la columna `name`, escribe **yourname**. Este será el nombre único usado para identificar la primera pregunta. Cada pregunta debe tener un nombre único y no puede contener espacios o símbolos (excepto el guion bajo).
3. En la columna `label`, escribe **¿Cuál es tu nombre?**. Esta etiqueta se mostrará como el texto de la pregunta en el formulario durante la recolección de datos.

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | ¿Cuál es tu nombre? |
| survey |

4. Para la segunda pregunta, **¿Cuál es el sexo de tu bebé?**, ingresa **select_one sex** en la columna `type` de la hoja de trabajo survey.
   - **select_one** es el tipo de pregunta que permite a los/as usuarios/as seleccionar solo una opción de una lista de opciones de respuesta.
   - **sex** es el nombre de la lista de opciones de respuesta, que se define en la hoja de trabajo choices (ver [Agregar opciones de respuesta](https://support.kobotoolbox.org/getting_started_xlsform.html#adding-response-choices)).
5. En la columna `name`, escribe **baby_sex**.
6. En la columna `label`, escribe **¿Cuál es el sexo de tu bebé?**

| type           | name     | label                    |
| :------------- | :------- | :----------------------- |
| select_one sex | baby_sex | ¿Cuál es el sexo de tu bebé? |
| survey |


7. Para la pregunta **¿Cuántos años tienes?**, sigue el mismo proceso usando **integer** como el tipo de pregunta en la columna `type`.

| type    | name | label            |
| :------ | :--- | :--------------- |
| integer | age  | ¿Cuántos años tienes? |
| survey |

<p class="note">
  <b>Nota:</b> Para aprender más sobre los tipos de preguntas en XLSForm, consulta <a class="reference external" href="https://xlsform.org/en/#question-types">Question types (XLSForm.org)</a>.
</p>

## Agregar opciones de respuesta

Para preguntas de tipo select (**select_one** y **select_multiple**), las opciones de respuesta se agregan en la hoja de trabajo **choices**. El proceso paso a paso a continuación explica cómo agregar las opciones para la pregunta de ejemplo: **¿Cuál es el sexo de tu bebé?**

1. En la columna `list_name` en la hoja de trabajo choices, ingresa el list_name **sex**.
   - Este es el list_name previamente definido para la pregunta **baby_sex** en la hoja de trabajo survey.
   - El list_name es el identificador único para la lista de opciones de respuesta.
2. En la columna name, agrega el nombre de opción **male**.
   - El nombre de opción es el identificador único para cada opción.
3. En la columna label, ingresa la etiqueta de opción **Male**.
   - La etiqueta de opción se muestra en el formulario durante la recolección de datos.
4. Para agregar la segunda opción de respuesta para la pregunta **baby_sex**, ingresa **sex** en la columna `list_name`. Ingresa **female** como el nombre de opción y **Female** como la etiqueta de opción.

| list_name | name   | label  |
| :-------- | :----- | :----- |
| sex       | male   | Male   |
| sex       | female | Female |
| choices |

## Agregar configuraciones

Hay muchas configuraciones opcionales que pueden agregarse a la hoja de trabajo **settings** en XLSForm.

Las configuraciones comunes del formulario incluyen:

| Configuración del formulario     | Descripción                            |
| :--------------- | :------------------------------------- |
| form_title       | Título mostrado en la parte superior del formulario |
| default_language | Idioma predeterminado del formulario                  |
| style            | Temas para formularios web Enketo            |
| version          | ID de versión del formulario                        |
| settings |

Por ejemplo, para agregar un título de formulario:

1. Agrega una columna en la hoja de trabajo settings llamada `form_title`.
2. Ingresa el título del formulario en la columna `form_title`.
   - Si no defines un título de formulario en tu XLSForm, por defecto el nombre del archivo de Excel se usará como el nombre del proyecto en KoboToolbox. Esto puede editarse en KoboToolbox.

<p class="note">
  <b>Nota:</b> Para aprender más sobre la hoja de trabajo settings en XLSForm, consulta <a class="reference external" href="https://xlsform.org/en/#settings-worksheet">Settings worksheet (XLSForm.org)</a>.
</p>

## Agregar columnas opcionales a la hoja de trabajo survey

Para personalizar aún más tu XLSForm, puedes agregar columnas opcionales que incluyen lógica de formulario, opciones de preguntas y configuraciones avanzadas.

| **Nombre de columna**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| hint               | Sugerencia de pregunta                                  |
| guidance_hint      | Sugerencia de orientación                                  |
| required           | Opción para hacer una pregunta obligatoria            |
| relevant           | Condiciones de lógica de salto para la pregunta         |
| constraint         | Criterios de validación para la pregunta           |
| constraint_message | Mensaje de error cuando no se cumplen los criterios de validación |
| appearance         | Opciones para cómo se muestran las preguntas        |
| choice_filter      | Criterios para select en cascada                  |
| parameters         | Configuraciones para tipos de preguntas específicas           |
| calculation        | Expresión matemática para pregunta de cálculo |
| default            | Respuesta predeterminada para una pregunta                |

## Cargar y previsualizar el XLSForm en KoboToolbox

Para cargar y previsualizar tu XLSForm en KoboToolbox:

1. Ve a la vista **Lista de Proyectos** en KoboToolbox y haz clic en **NUEVO**.
2. Selecciona **Cargar un XLSForm** y carga tu archivo de **Excel**.
   - Si creaste tu XLSForm en **Google Sheets**, necesitarás descargar el archivo antes de cargarlo a KoboToolbox. En el menú de Google Sheets, haz clic en Archivo > Descargar > Microsoft Excel.
3. Ingresa los detalles del proyecto y haz clic en **CREAR PROYECTO**.
4. Haz clic en el botón <i class="k-icon k-icon-view"></i> **Previsualizar**.

<p class="note">
  <b>Nota:</b> Para aprender cómo importar tu XLSForm vía URL, consulta el artículo de ayuda <a class="reference" href="https://support.kobotoolbox.org/xls_url.html">Importar un XLSForm vía URL</a>.
</p>

## Descargar un XLSForm desde KoboToolbox

Los formularios creados usando el editor de formularios de KoboToolbox pueden descargarse fácilmente como un archivo XLSForm.

1. Ve a la ventana **FORMULARIO** de tu proyecto en KoboToolbox.
2. Haz clic en el ícono <i class="k-icon k-icon-more"></i> **Más acciones**.
3. Haz clic en <i class="k-icon k-icon-xls-file"></i>**Descargar XLS**.

Descargar tu formulario de KoboToolbox como un archivo XLSForm puede ser muy útil por muchas razones, incluyendo:

-   Agregar funcionalidades avanzadas a tu formulario que no están actualmente soportadas en el Formbuilder.
-   Hacer cambios al formulario que son más eficientes de hacer en XLSForm (por ejemplo, duplicar un gran número de preguntas o agregar traducciones).
-   Evitar velocidades lentas de computadora o internet que pueden afectar la construcción de formularios en el Formbuilder (por ejemplo, RAM limitada, conectividad de internet deficiente).
-   Compartir el formulario como un archivo de Excel para colaboración con miembros del equipo y manejo de versiones del formulario.
-   Compartir el formulario para solicitar asistencia del equipo de soporte de KoboToolbox o en el Foro de la comunidad.

## Reemplazar un formulario con un archivo XLSForm

Puedes reemplazar un formulario existente en el Formbuilder con una nueva versión usando un XLSForm. Por ejemplo, después de editar el formulario en Excel, debes cargar el archivo actualizado a KoboToolbox.

1. Ve a la ventana **FORMULARIO** de tu proyecto en KoboToolbox.
2. Haz clic en el ícono <i class="k-icon k-icon-more"></i> **Más acciones**.
3. Haz clic en <i class="k-icon k-icon-replace"></i> **Reemplazar formulario**.
4. Elige el archivo que deseas cargar.

## Más recursos de XLSForm

Para más información sobre el uso de XLSForm, consulta los siguientes recursos:

-   [Documentación oficial de XLSForm en XLSForm.org](https://xlsform.org)
-   [Documentación de construcción de formularios de ODK](https://docs.getodk.org/)