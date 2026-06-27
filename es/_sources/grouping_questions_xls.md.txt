# Grupos de preguntas en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/grouping_questions_xls.md" class="reference">23 Apr 2026</a>

Agrupar preguntas en XLSForm ayuda a organizar el contenido relacionado en secciones claras y estructuradas, lo que mejora el diseño y la navegación del formulario. Por ejemplo, puedes agrupar todas las preguntas demográficas en una sola sección.

XLSForm facilita la creación de grupos y [subgrupos](https://support.kobotoolbox.org/es/grouping_questions_xls.html#nested-groups), y la aplicación de [lógica de omisión](https://support.kobotoolbox.org/es/grouping_questions_xls.html#applying-skip-logic-to-question-groups) a grupos de preguntas completos. La lógica de omisión a nivel de grupo simplifica la experiencia del encuestado al mostrar solo las secciones relevantes según las respuestas anteriores.

Este artículo cubre los siguientes temas:

- Crear grupos de preguntas y subgrupos en XLSForm
- Mostrar todas las preguntas agrupadas en una sola página
- Agregar lógica de omisión a grupos de preguntas

<p class="note">
<strong>Nota:</strong> Este artículo se centra en agrupar preguntas en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agrupar preguntas en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/group_repeat.html">Grupos y grupos de repetición en el Formbuilder</a>.
</p>

## Crear un grupo de preguntas

Para crear un grupo de preguntas en XLSForm:

1.  En la columna `type` de la hoja survey, ingresa `begin_group` para indicar el inicio del grupo.
2.  En la columna `name` de la fila `begin_group`, ingresa el identificador único del grupo.
3.  En la columna `label`, ingresa el título del grupo tal como quieres que aparezca en el formulario. La etiqueta es opcional y puede dejarse en blanco.
4.  Ingresa cada pregunta del grupo en su propia fila, como lo harías normalmente.
5.  En una nueva fila después de las preguntas agrupadas, ingresa `end_group` en la columna `type` para indicar el fin del grupo.
    - En la fila `end_group`, deja las columnas `name` y `label` en blanco.

<p class="note">
<strong>Nota:</strong> Los nombres de los grupos en la columna <code>name</code> deben ser únicos y no pueden duplicar ningún nombre de pregunta.
</p>

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Sección A: Información personal |
| text | name | ¿Cuál es tu nombre? |
| integer | age | ¿Cuántos años tienes? |
| select_one yn | married | ¿Estás casado/a? |
| **end_group** | | |
| survey |

### Subgrupos

Los subgrupos son grupos de preguntas dentro de otro grupo de preguntas. Los subgrupos pueden usarse para crear una estructura jerárquica dentro de tu XLSForm. Por ejemplo, puedes incluir un grupo de preguntas sobre un niño dentro de un grupo más amplio de preguntas sobre el hogar.

Al crear varios grupos, asegúrate de que cada fila `begin_group` tenga una fila `end_group` correspondiente. Si el número de filas `begin_group` no coincide con el número de filas `end_group`, el formulario generará un error que impedirá su correcto funcionamiento durante la vista previa o la implementación.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_group** | personal_info | Sección A: Información personal |
| text | name | ¿Cuál es tu nombre? |
| integer | age | ¿Cuántos años tienes? |
| select_one yn | married | ¿Estás casado/a? |
| **begin_group** | education | Educación |
| select_one yn | student | ¿Eres estudiante actualmente? |
| select_one edu | education_level | ¿Cuál es el nivel educativo más alto que has completado? |
| **end_group** | | |
| **end_group** | | |
| survey |

### Grupos de repetición

En XLSForm, los grupos de preguntas pueden repetirse para recolectar el mismo conjunto de respuestas varias veces dentro de un formulario. Esto es útil cuando se recopila información similar sobre varias personas, elementos o eventos. Los grupos que se repiten se denominan **grupos de repetición**.

<p class="note">
  Para obtener más información sobre cómo configurar grupos de repetición en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/repeat_groups_xls.html">Grupos repetidos en XLSForm</a>.
</p>

## Configuración de apariencia para grupos de preguntas

Una razón habitual para agrupar preguntas es mostrarlas juntas en una sola página. Puedes ajustar la configuración de apariencia del grupo para controlar cómo se muestran las preguntas agrupadas durante la recolección de datos. Los pasos varían según si usas [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html) o [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html).

<p class="note">
<strong>Nota:</strong> La configuración de apariencia para mostrar grupos en una sola página funciona tanto para grupos de preguntas como para <a href="https://support.kobotoolbox.org/es/repeat_groups_xls.html">grupos de repetición</a>.
</p>

### Usar KoboCollect para recolectar datos

De forma predeterminada, KoboCollect muestra cada pregunta en una pantalla separada. Los usuarios deben avanzar manualmente de una pregunta a la siguiente.

Para **mostrar todas las preguntas agrupadas en la misma pantalla** en KoboCollect:
1.  En la hoja `survey`, agrega una columna `appearance`.
2.  En la columna `appearance`, ingresa `field-list` en la fila `begin_group`.
    * Cada grupo de preguntas aparecerá ahora en su propia página.

**hoja survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Sección A: Información personal | **field-list** |
| text | name | ¿Cuál es tu nombre? | |
| integer | age | ¿Cuántos años tienes? | |
| select_one yn | married | ¿Estás casado/a? | |
| end_group | | | |
| survey |

### Usar formularios web para recolectar datos

De forma predeterminada, los formularios web muestran todas las preguntas en una sola página.

Para mostrar cada grupo de preguntas en su propia página en formularios web:
1.  En la hoja `settings`, agrega una columna `style`.
2.  En la segunda celda de la columna `style`, ingresa `pages`.
    * Esto aplica el [tema de páginas](https://support.kobotoolbox.org/es/form_style_xls.html) a tu formulario web, dividiéndolo en páginas separadas de forma similar a KoboCollect.

**hoja settings**

| style |
| :--- |
| pages |
| settings |

3.  En la hoja `survey`, agrega una columna `appearance`.
4.  En la columna `appearance`, ingresa `field-list` en la fila `begin_group`.
    * Cada grupo de preguntas aparecerá ahora en su propia página.

**hoja survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| begin_group | personal_info | Sección A: Información personal | **field-list** |
| text | name | ¿Cuál es tu nombre? | |
| integer | age | ¿Cuántos años tienes? | |
| select_one yn | married | ¿Estás casado/a? | |
| end_group | | | |
| survey |


## Aplicar lógica de omisión a grupos de preguntas

Aplicar lógica de omisión a grupos de preguntas garantiza que solo aparezcan las secciones relevantes según las respuestas anteriores. Por ejemplo, en una encuesta de hogares, puedes usar la lógica de omisión para mostrar un grupo de preguntas destinado al jefe del hogar únicamente cuando una pregunta anterior identifica al encuestado como tal. Esto facilita la navegación del formulario y lo hace más adaptable a las respuestas del usuario.

Para [aplicar lógica de omisión](https://support.kobotoolbox.org/es/skip_logic_xls.html) a grupos de preguntas en XLSForm, usa el mismo enfoque que aplicarías a preguntas individuales:
1.  Agrega una columna `relevant` a la hoja `survey`.
2.  En la columna `relevant` de la fila `begin_group`, ingresa la condición que determina cuándo debe mostrarse el grupo.
3.  Si se cumple la condición, se mostrará el grupo completo. Si no, el grupo quedará oculto.

Esto permite controlar el flujo del formulario de modo que solo aparezcan las secciones relevantes según las respuestas anteriores, haciendo el formulario más ágil y adaptable a las respuestas del usuario.

<p class="note">
<strong>Nota:</strong> La lógica de omisión puede aplicarse tanto a grupos de preguntas como a <a href="https://support.kobotoolbox.org/es/repeat_groups_xls.html">grupos de repetición</a>. Para obtener más información sobre la lógica de omisión en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/skip_logic_xls.html">Añadir lógica de salto a un XLSForm</a>.
</p>