# Agregar filtros de selección a un XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/1b55b2580defd73765e9c2ad608141a3428ee504/source/choice_filters_xls.md" class="reference">4 Jan 2026</a>

Los filtros de selección crean formularios dinámicos en los que las opciones de una pregunta dependen de la respuesta a una pregunta anterior. Esto simplifica la recolección de datos al presentar solo las opciones relevantes, mejorando la eficiencia y precisión de la encuesta.

Los filtros de selección se pueden usar en diversas aplicaciones, entre ellas:
- **Listas jerárquicas**, como continentes y países, donde la lista de países depende del continente seleccionado (también conocidas como **selecciones en cascada**).
- **Eliminar una o varias opciones de una lista** si no son relevantes para un encuestado según sus respuestas anteriores.
- **Reutilizar una lista de opciones** en XLSForm para varias preguntas, donde la lista varía ligeramente de una pregunta a la siguiente.
- Reutilizar una lista de opciones de una pregunta anterior, incluyendo **solo las opciones que fueron seleccionadas por el encuestado.**

Este artículo explica cómo agregar filtros de selección en XLSForm e incluye ejemplos para diferentes casos de uso. Los filtros de selección se definen en la columna `choice_filter` de la **hoja survey**, y se operacionalizan en la **hoja choices**.

<p class="note">
<strong>Nota:</strong> Este artículo se centra en agregar filtros de selección en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a agregar preguntas de selección en cascada en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/cascading_select.html">Agregar preguntas de selección en cascada en el Formbuilder</a>.
<br><br>
Para practicar con filtros de selección en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar filtros de selección estáticos

Los **filtros de selección estáticos** aplican las mismas condiciones de filtrado para todos los encuestados. Al usar filtros de selección estáticos, se filtra una lista de opciones, pero esta no varía según las respuestas anteriores. Esto puede ser útil cuando quieres reutilizar una lista de opciones en varias preguntas de tu formulario con variaciones menores, sin duplicar la lista de opciones varias veces en tu **hoja choices**.

Para agregar filtros de selección estáticos en XLSForm:
1. Agrega una pregunta `select_one` o `select_multiple` a tu XLSForm y [define las opciones de respuesta](https://support.kobotoolbox.org/es/option_choices_xls.html) en la **hoja choices**.
2. En la **hoja choices**, agrega una columna de filtro.
    - Puedes nombrar esta columna como quieras (por ejemplo, `q2`).
3. En la columna de filtro, escribe cualquier valor (por ejemplo, `yes`) junto a las opciones que quieras incluir en la lista de opciones para tu pregunta.
    - Este valor actuará como el filtro. Puede ser cualquier palabra o número.
4. En la **hoja survey**, agrega una columna `choice_filter`. Esta columna contendrá la **expresión de filtro de selección** utilizada para filtrar las opciones de respuesta.
    - La expresión de filtro de selección en su forma más básica tendrá el formato: `filter = 'value'`.
    - Por ejemplo, `q2 = 'yes'` conservará todas las opciones con **yes** en la columna `q2`.

### Ejemplo

En el ejemplo a continuación, la misma lista de opciones (`activities`) se usa para dos preguntas diferentes. Para la segunda pregunta, la lista se filtra para mostrar solo actividades al aire libre.

**hoja survey**

| type             | name               | label                                                   | choice_filter   |
|:-----------------|:------------------|:--------------------------------------------------------|:----------------|
| select_one activities | activities        | ¿Qué actividades disfrutas hacer en tu tiempo libre?  |                 |
| select_one activities | outdoors_activities | ¿Cuáles de estas actividades al aire libre están disponibles en tu ciudad? | <strong>filter = 'outdoors'</strong> |
| survey |

**hoja choices**

| list_name  | name       | label                 | filter   |
|:-----------|:-----------|:--------------------|:---------|
| activities | reading    | Lectura              |          |
| activities | swimming   | Natación             | outdoors |
| activities | running    | Correr               | outdoors |
| activities | television | Ver televisión       |          |
| activities | hiking     | Senderismo           | outdoors |
| choices |

## Agregar filtros de selección dinámicos

Los filtros de selección también se pueden usar para filtrar una lista de opciones según una respuesta anterior. En este caso, tendrás una **pregunta principal** con una **lista principal** de opciones correspondiente, y una **pregunta secundaria** con una **lista secundaria** de opciones correspondiente. La lista de opciones para la pregunta secundaria se filtra según la respuesta a la pregunta principal.

<p class="note">
Para ver un ejemplo de un XLSForm que usa filtros de selección dinámicos, consulta este <a href="https://docs.google.com/spreadsheets/d/10gpBV6YaYGx1i367hyW-w1Ms9tkUQnCx0V8YsdwYxmk/edit?gid=0#gid=0">formulario de ejemplo</a>.
</p>

Para agregar filtros de selección dinámicos en XLSForm:
1. Agrega la **pregunta principal** y la **pregunta secundaria** a tu XLSForm y [define sus opciones de respuesta](https://support.kobotoolbox.org/es/option_choices_xls.html) en la **hoja choices**.
    - Deben ser preguntas `select_one` o `select_multiple`.
2. En la **hoja choices**, agrega una columna de filtro.
    - Puede ser útil nombrar esta columna igual que la **pregunta principal**.
3. En la columna de filtro, ingresa el `name` de la opción de la lista principal que corresponde a cada opción de la lista secundaria.
4. En la **hoja survey**, agrega una columna `choice_filter`. Esta columna contendrá la **expresión de filtro de selección** utilizada para filtrar las opciones de respuesta.
    - Si la pregunta principal es `select_one`, la expresión de filtro de selección será `filter_column = ${question_name}`, donde `question_name` hace referencia a la pregunta principal.
    - Si la pregunta principal es `select_multiple`, la expresión de filtro de selección será `selected(${question_name}, filter_column)`.

Cuando un encuestado selecciona una opción en la pregunta principal, la lista de opciones para la pregunta secundaria se filtrará para incluir solo las opciones correspondientes.

### Ejemplo

En el ejemplo a continuación, `continent` es la **pregunta principal** y `country` es la **pregunta secundaria**. La lista de opciones para la pregunta `country` se filtrará según la respuesta a la pregunta `continent`.

**hoja survey**

| type              | name      | label      | choice_filter        |
|:------------------|:---------|:-----------|:--------------------|
| select_one continent | continent | Continente |                     |
| select_one country   | country   | País       | **continent = ${continent}** |
| survey |

**hoja choices**

| list_name  | name     | label    | continent |
|:-----------|:---------|:---------|:----------|
| continent  | africa   | África   |           |
| continent  | asia     | Asia     |           |
| country    | malawi   | Malawi   | africa    |
| country    | zambia   | Zambia   | africa    |
| country    | india    | India    | asia      |
| country    | pakistan | Pakistán | asia      |
| choices |

## Filtros de selección avanzados en XLSForm

Puedes crear filtros de selección más avanzados usando operadores lógicos, operadores matemáticos, funciones y expresiones regulares en tus expresiones de filtro de selección. Esto permite un filtrado de opciones altamente personalizado y preciso, adaptando el formulario a requisitos específicos de recolección de datos y características de los encuestados.

<p class="note">
<strong>Nota:</strong> En las expresiones de filtro de selección avanzadas, la columna <code>name</code> de la <strong>hoja choices</strong> se puede usar como columna de filtro.
</p>

Algunos ejemplos de expresiones de filtro de selección avanzadas en XLSForm incluyen:

| Filtro de selección | Descripción |
|:---------------|:------------|
| `selected(${parent_question}, name)` | Mostrar solo las respuestas que fueron seleccionadas en una `parent_question` anterior. |
| `filter = 'outdoors' and include = 'yes'` | Combinar expresiones de filtro de selección para que ambas condiciones deban cumplirse para que se muestre la opción. |
| `name != 'none'` | Excluir la opción <strong>Ninguno</strong> de una lista de opciones. |
| `selected(${Q1}, name) or name='none'` | Incluir las opciones seleccionadas en una pregunta anterior, así como una opción <strong>Ninguno</strong> (aunque no haya sido seleccionada anteriormente). |
| `filter=${Q1} or name='other'` | Incluir opciones basadas en una pregunta anterior, así como una opción <strong>Otro</strong>. |
| `filter=${Q1} or always_include='yes'` | Incluir opciones basadas en una pregunta anterior, así como un conjunto de opciones que siempre deben incluirse. |
| `filter <= ${product_count}` | Usar números en la columna de filtro en lugar de texto, y filtrar según un número de una pregunta o cálculo anterior. |
| `if(${relationship_status} = 'married', filter = 'married', filter = 'unmarried')` | Usar sentencias if para mostrar condicionalmente opciones según el perfil del encuestado. |

<p class="note">
  Para aprender más sobre cómo crear expresiones de lógica de formularios en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/form_logic_xls.html">Introducción a la lógica de formularios en XLSForm</a>.
</p>

### Ejemplo
En el ejemplo a continuación, la lista de opciones subyacente para `Q1` y `Q2` es la misma, pero solo las opciones seleccionadas en `Q1` se mostrarán a los encuestados al responder `Q2`.

**hoja survey**

| type               | name | label                                              | choice_filter            |
|:------------------|:-----|:--------------------------------------------------|:-------------------------|
| select_multiple item | Q1  | ¿Cuáles de estos artículos del hogar tienes actualmente?      |                          |
| select_multiple item | Q2  | ¿Cuáles de estos artículos considerarías actualizar en el futuro? | selected(${Q1}, name) |
| survey |

**hoja choices**

| list_name | name      | label            |
|:----------|:----------|:----------------|
| item      | fridge    | Refrigerador    |
| item      | tv        | Televisor       |
| item      | fan       | Ventilador de techo |
| item      | microwave | Horno microondas |
| item      | radio     | Radio           |
| item      | bike      | Bicicleta       |
| item      | phone     | Teléfono móvil  |
| item      | laptop    | Computadora portátil |
| choices |

En el formulario resultante, `Q2` mostrará solo las opciones elegidas en `Q1`, como se muestra a continuación.

![Filtros de selección](images/choice_filters_xls/choice_filters.png)

## Resolución de problemas

<details>
  <summary><strong>El formulario se ralentiza o falla con listas muy largas</strong></summary>
  Las listas de opciones grandes que incluyen miles de filas pueden funcionar en la vista previa pero fallar al implementarse. Esto ocurre porque la vista previa del navegador puede manejar listas grandes, mientras que la aplicación móvil o el analizador XLS no pueden. Para solucionar esto, mueve las listas grandes a un archivo CSV externo y usa <a href="https://support.kobotoolbox.org/es/select_from_file_xls.html">preguntas select_from_file</a> con filtros de selección. Este enfoque se recomienda para listas con más de 3.000 opciones.
</details>

<br>

<details>
  <summary><strong>Nombres de opciones duplicados en una lista</strong></summary>
  Si tu lista de opciones incluye nombres de opciones duplicados (por ejemplo, si el mismo nombre de barrio aparece en diferentes ciudades), <a href="https://support.kobotoolbox.org/es/form_settings_xls.html">habilita los duplicados de opciones</a> en la <strong>hoja settings</strong> configurando <code>allow_choice_duplicates</code> como <code>yes</code>.
</details>