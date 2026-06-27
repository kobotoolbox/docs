# Grupos repetidos en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/3256884be21cabd4238e7470299b347a34510d49/source/repeat_groups_xls.md" class="reference">23 Jun 2026</a>

Los grupos repetidos en XLSForm te permiten hacer el mismo conjunto de preguntas varias veces dentro de un formulario. Esto es especialmente útil cuando recolectas información similar sobre varias personas, elementos o eventos.

Por ejemplo, si estás recopilando datos sobre cada miembro de un hogar, puedes usar un grupo de repetición para hacer las mismas preguntas demográficas a cada individuo.

Este artículo cubre los siguientes temas:
- Crear un grupo de repetición
- Configurar conteos de repetición para limitar el número de repeticiones
- Contar el número de repeticiones dentro de un grupo de repetición
- Recuperar valores de grupos repetidos

<p class="note">
<strong>Nota:</strong> Este artículo se centra en los grupos repetidos en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender sobre los grupos repetidos en el editor de formularios de KoboToolbox (Formbuilder) y ver ejemplos de grupos repetidos en acción, consulta <a href="https://support.kobotoolbox.org/es/group_repeat.html">Grupos y grupos de repetición en el Formbuilder</a>.
</p>

## Crear un grupo de repetición

Para crear un grupo de repetición en XLSForm:

1. En la columna `type` de la hoja survey, ingresa `begin_repeat` para indicar el inicio del grupo de repetición.
2. En la columna `name` de la fila `begin_repeat`, ingresa el identificador único del grupo.
3. En la columna `label`, ingresa el título del grupo tal como quieres que aparezca en el formulario. La etiqueta es opcional y puede dejarse en blanco.
4. Ingresa cada pregunta del grupo en su propia fila, como lo harías normalmente.
5. En una nueva fila después de las preguntas repetidas, ingresa `end_repeat` en la columna `type` para indicar el fin del grupo de repetición.
    - En la fila `end_repeat`, deja en blanco las columnas `name` y `label`.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| **begin_repeat** | household_members | Household Members |
| text | name | What is the person's name? |
| integer | age | How old are they? |
| select_one yn | married | Are they married? |
| **end_repeat** | | |
| survey |

Los grupos repetidos funcionan de manera similar a los grupos de preguntas. Con los grupos repetidos, puedes:

- Usar la apariencia `field-list` para [mostrar todas las preguntas](https://support.kobotoolbox.org/es/grouping_questions_xls.html#appearance-settings-for-question-groups) en la misma página.
- Agregar [lógica de omisión](https://support.kobotoolbox.org/es/grouping_questions_xls.html#applying-skip-logic-to-question-groups) a los grupos repetidos en la columna `relevant`.
- Crear **grupos repetidos anidados**, donde un grupo de repetición se agrega [dentro de otro](https://support.kobotoolbox.org/es/grouping_questions_xls.html#nested-groups).

<p class="note">
  <strong>Nota:</strong> Agregar grupos repetidos a tu formulario crea una estructura de datos diferente en comparación con las variables o grupos estándar. Cuando descargues tus datos en formato <code>.xlsx</code>, encontrarás una hoja separada para cada grupo de repetición. Para más información sobre cómo exportar y usar datos de grupos repetidos, consulta <a href="https://support.kobotoolbox.org/es/managing_repeat_groups.html">Gestión de datos de grupos repetidos</a>.
</p>

## Configurar conteos de repetición

De forma predeterminada, los grupos repetidos pueden repetirse tantas veces como sea necesario. Para limitar el número de veces que un grupo de repetición se repite en el formulario, puedes configurar un conteo de repetición. El **conteo de repetición** puede ser un número fijo o determinarse dinámicamente en función de una respuesta anterior.

Para configurar un número fijo de repeticiones:

1. Añade una columna `repeat_count` en la hoja survey.
2. Ingresa un número en la columna `repeat_count`.

**hoja survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| begin_repeat | participant_profile | Participant profile | 3 |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| survey |

Para determinar dinámicamente el número de repeticiones en función de una respuesta anterior:

1. Añade una columna `repeat_count` en la hoja survey.
2. Ingresa la referencia a la pregunta en la columna `repeat_count`.
    - La pregunta referenciada debe ser del tipo de pregunta `integer`.

  **hoja survey**

| type | name | label | repeat_count |
| :--- | :--- | :--- | :--- |
| integer | participants | Total number of training participants | |
| begin_repeat | participant_profile | Participant profile | ${participants} |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| survey |

<p class="note">
  <strong>Nota:</strong> Dentro de la columna <code>repeat_count</code>, también puedes incluir declaraciones condicionales avanzadas para determinar si las repeticiones continuarán. Para más información, consulta la <a href="https://docs.getodk.org/form-logic/#repeating-as-long-as-a-condition-is-met">documentación de ODK</a>.
</p>

## Contar el número de repeticiones dentro de un grupo de repetición

Cuando usas grupos repetidos, es posible que necesites un campo que cuente cuántas veces se ha repetido el grupo. Esto puede ser útil para cálculos o lógica del formulario. Por ejemplo, puedes aplicar lógica de omisión después de una repetición específica o incluir dinámicamente el número de repetición en la etiqueta de una pregunta (por ejemplo, Niño 1, Niño 2).

Para contar cuántas veces se ha repetido un grupo de repetición:
1. Añade una pregunta `calculate` dentro del grupo de repetición.
2. Escribe `position(..)` en la columna `calculation`.

Esta variable almacena el índice de repetición actual. Puedes usarla en la lógica del formulario o para crear etiquetas de preguntas dinámicas.

**hoja survey**

| type | name | label | calculation | relevant |
| :--- | :--- | :--- | :--- | :--- |
| begin_repeat | profile | Participant profile | | |
| calculate | number | | **position(..)** | |
| note | instructions | Answer the questions below for each participant. | | **${number} = 1** |
| text | name | Name of participant **${number}** | | |
| select_one gender | gender | Gender of participant **${number}** | | |
| integer | age | Age of participant **${number}** | | |
| end_repeat | | | | |
| survey |

## Contar el número total de repeticiones de un grupo de repetición

También puedes añadir una pregunta separada fuera del grupo de repetición para contar el número total de repeticiones. Esto es útil, por ejemplo, para confirmar el número de participantes o niños incluidos en el grupo de repetición.

Para contar cuántas veces se completó un grupo de repetición:
1. Añade una pregunta `calculate` después del grupo de repetición.
2. En la columna `calculation`, ingresa `count(${repeat_group_name})`, donde `repeat_group_name` es el nombre del grupo de repetición.

Esta variable almacena el número total de repeticiones del grupo. Puedes usarla en cálculos o para crear etiquetas de preguntas dinámicas en tu formulario.

**hoja survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Children roster | |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| calculate | count_children | | **count(${children})** |
| acknowledge | confirm_children | Confirm that there are **${count_children}** children in the household. | |
| survey |

## Recuperar valores de grupos repetidos

Los formularios avanzados suelen usar [referencias a preguntas](https://support.kobotoolbox.org/es/form_logic_xls.html#question-referencing) para incluir respuestas de preguntas anteriores en etiquetas de preguntas, cálculos o lógica de omisión. También puedes usar referencias a preguntas **dentro de grupos repetidos** o para hacer referencia a datos repetidos en otras partes del formulario.

Dentro de un grupo de repetición, puedes hacer referencia a una respuesta de otra pregunta en la misma repetición usando referencias a preguntas, como se muestra a continuación.

**hoja survey**

| type | name | label |
| :--- | :--- | :--- |
| begin_repeat | children | Children roster |
| text | name | What is the child's name? |
| integer | age | How old is ${name}? |
| select_one gender | married | What is ${name}'s gender? |
| end_repeat | | |
| survey |

Fuera de un grupo de repetición, puedes recuperar datos del grupo de repetición para usarlos en la lógica del formulario o en etiquetas de preguntas:

1. Añade una pregunta `calculate` después de tu grupo de repetición.
2. Incluye una de las fórmulas que se indican a continuación en la columna `calculation`.
3. La pregunta `calculate` almacena el valor recuperado, que luego puedes usar en la lógica del formulario o en etiquetas de preguntas.

**Fórmulas para recuperar datos de grupos repetidos**

| Fórmula | Descripción |
| :--- | :--- |
| `max(${question-name})` | Recupera el valor máximo ingresado para una pregunta en el grupo de repetición. |
| `min(${question-name})` | Recupera el valor mínimo ingresado para una pregunta en el grupo de repetición. |
| `sum(${question-name})` | Calcula la suma de los valores numéricos ingresados para una pregunta en el grupo de repetición. |
| `join('; ', ${question-name})` | Lista todas las respuestas a una pregunta determinada dentro de un grupo de repetición, separadas por punto y coma. |
| `indexed-repeat(${question-name}, ${repeat-name}, n)` | Recupera el valor de `${question-name}`, en el grupo de repetición llamado `${repeat-name}`, en la n<sup>ª</sup> repetición. |

**hoja survey**

| type | name | label | calculation |
| :--- | :--- | :--- | :--- |
| begin_repeat | children | Children roster | |
| text | name | Name | |
| select_one gender | gender | Gender | |
| integer | age | Age | |
| end_repeat | | | |
| calculate | max_age | | **max(${age})** |
| acknowledge | confirm_age | Confirm that the oldest child in the household is **${max_age}** years old. | |
| survey |

## Resolución de problemas

<details>
<summary><strong>Error en KoboCollect: "Repeats in 'field-list' groups are not supported"</strong></summary>
Este error ocurre en KoboCollect cuando un grupo de repetición está anidado dentro de un grupo más amplio que usa la apariencia <code>field-list</code>. KoboCollect no admite grupos repetidos dentro de grupos con apariencia <code>field-list</code>. Los grupos repetidos deben aparecer en su propia página.
<br><br>
Para resolver este problema, mueve el grupo de repetición fuera del grupo principal, o elimina la apariencia <code>field-list</code> del grupo principal.
<br><br>
Este problema solo ocurre en KoboCollect y no afecta a los formularios web.
</details>