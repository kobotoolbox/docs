# Personalizar formularios usando XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/8e8a733c7bdc3e6479696bfba96ce397c1425ab4/source/form_style_xls.md" class="reference">22 Jun 2026</a>

Con KoboToolbox, puedes personalizar la apariencia de tus formularios y preguntas para resaltar información clave y adaptar el diseño a tus necesidades de recolección de datos. Esto incluye aplicar temas a formularios web, agregar encabezados y listas en preguntas de tipo nota, y usar color o formato en negrita para dar énfasis.

Este artículo cubre los temas para formularios web, así como las opciones de estilo para notas y preguntas dentro de un formulario.

<p class="note">
<strong>Nota:</strong> Este artículo se centra en el estilo de formularios en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a configurar temas de formularios web en el KoboToolbox Formbuilder, consulta <a href="https://support.kobotoolbox.org/es/alternative_enketo.html">Diseñar formularios web usando el Formbuilder</a>.
</p>

## Temas para formularios web

Los temas de formularios web te permiten personalizar la apariencia y el diseño de los [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html). Los temas se aplican únicamente a formularios web y no son visibles en KoboCollect.

### Agregar temas en XLSForm

Para agregar un tema en XLSForm:
1. Añade una columna `style` en tu **hoja settings**.
2. Especifica el tema que deseas usar con el nombre exacto que aparece en la tabla a continuación.

**hoja settings**

| style       |
|:------------|
| theme-grid  |
| settings |

<p class="note">
<strong>Nota:</strong> Los temas se pueden combinar ingresando ambos temas en la misma celda de la columna <code>style</code>, separados por un espacio (por ejemplo, <code>theme-grid pages</code>).
</p>

### Temas disponibles para formularios web

Los siguientes temas están disponibles para personalizar tus formularios:

| Tema XLSForm                | Descripción                                                                 | Vista previa |
|:----------------------------|:----------------------------------------------------------------------------|:-------------|
| Tema predeterminado          | Muestra las preguntas una tras otra en una sola página.                     | ![Estilo predeterminado](images/form_style_xls/theme_default.png) |
| <code>pages</code>           | Muestra una pregunta por pantalla o un <a href="https://support.kobotoolbox.org/es/grouping_questions_xls.html">grupo de preguntas</a> juntas en la misma pantalla, similar al diseño de KoboCollect. | ![Estilo pages](images/form_style_xls/theme_pages.png) |
| <code>theme-grid</code>      | Una visualización alternativa más compacta, similar a los formularios en papel, que usa el espacio de manera eficiente y organiza varias preguntas por fila. Las preguntas aparecen en mayúsculas de forma predeterminada. Requiere <a href="https://support.kobotoolbox.org/es/form_style_xls.html#setting-up-an-xlsform-for-theme-grid">configurar tu XLSForm</a>. | ![Theme-grid](images/form_style_xls/theme_grid.png) |
| <code>theme-grid no-text-transform</code> | Igual que theme-grid, pero sin capitalización automática de las preguntas. | ![Theme-grid no-text-transform](images/form_style_xls/theme_grid_no_text_transform.png) |

### Configurar un XLSForm para theme_grid

En los formularios web, el diseño `theme_grid` te permite mostrar preguntas en varias columnas, haciendo que tu formulario sea más compacto y visualmente organizado. La configuración de estas columnas, incluyendo cuántas hay y qué tan anchas deben ser, se controla asignando `w-values` a cada pregunta dentro de la columna `appearance` de tu XLSForm.

<p class="note">
  Para una descripción completa del uso de <code>theme_grid</code> en XLSForm, consulta este <a href="https://ee.kobotoolbox.org/n41GqUkf">tutorial de tema de cuadrícula</a> y el <a href="https://docs.google.com/spreadsheets/d/1qKmxPTA4B0vihU6GsKgi1CJE2Db2FfE7KZpOig4nTEI/edit?gid=0#gid=0">XLSForm de ejemplo</a>.
</p>

Antes de asignar `w-values` a cada pregunta, comienza colocando todas las preguntas en [grupos de preguntas](https://support.kobotoolbox.org/es/grouping_questions_xls.html). El ancho predeterminado para un grupo o grupo de repetición es de cuatro columnas (`w4`), por lo que un grupo con `w4` puede contener un máximo de cuatro preguntas `w1` en una sola fila. El `w-value` de una pregunta es relativo al `w-value` de su grupo.

Para especificar el ancho relativo de cada pregunta dentro de una fila:
1. Añade una columna `appearance` en tu **hoja survey**.
2. Para cada pregunta, asigna valores de apariencia (por ejemplo, `w1`, `w2`, `w3`) para especificar su ancho relativo dentro de una fila.
3. Modifica el ancho del grupo si es necesario usando el mismo método.

Las filas siempre se expandirán automáticamente al ancho completo de la página. Por ejemplo, una fila que contiene una pregunta con un valor de apariencia `w2` y otra con `w1` dividirá la fila en dos tercios y un tercio, respectivamente.

<p class="note">
<strong>Nota:</strong> Aplica los <code>w-values</code> únicamente a grupos o grupos de repetición de nivel superior. Aunque aplicarlos a subgrupos o grupos de repetición anidados es compatible, es posible que no se visualicen correctamente.
</p>

## Dar estilo al texto

Puedes usar Markdown y HTML en XLSForm para **dar estilo al texto**, **añadir énfasis** con negrita o cursiva, **crear encabezados** de diferentes tamaños, **cambiar fuentes y colores**, y **agregar enlaces web**. El estilo de texto se puede aplicar a preguntas, sugerencias y notas.

<p class="note">
<strong>Nota:</strong> Es posible que algunas funciones de estilo no sean compatibles con KoboCollect o con los formularios web. Se recomienda previsualizar tus formularios en el método de recolección de datos que vayas a usar para confirmar que todas las funciones de estilo son totalmente compatibles.
</p>

Las funciones de estilo de texto en XLSForm incluyen:

| Función        | Formato |
|:---------------|:--------|
| Cursiva        | `*cursiva*` o `_cursiva_` |
| Negrita        | `**negrita**` o `__negrita__` |
| Hipervínculo   | `[nombre del enlace](url)` |
| Correo electrónico | `[email@domain.org](mailto:email@domain.org)` |
| Encabezados    | `# Encabezado 1` (más grande) a `###### Encabezado 6` (más pequeño) |
| Listas con viñetas | - Este es un elemento de lista<br>- en markdown |
| Listas numeradas | 1. Este es un elemento numerado<br>2. en markdown |
| Emojis         | Por ejemplo, 🙂 😐 🙁 😦 😧 😩 😱 |
| Superíndice    | `100 m<sup>2</sup>` se convierte en 100 m² |
| Subíndice      | `H<sub>2</sub>O` se convierte en H₂O |
| Texto en color | `<span style="color:#f58a1f">naranja</span>` se convierte en <span style="color:#f58a1f">naranja</span> <br>`<span style="color:red">rojo</span>` se convierte en <span style="color:red">rojo</span> |
| Fuente         | `<span style="font-family:cursive">cursiva</span>` se convierte en <span style="font-family:cursive">cursiva</span> <br>`<span style="color:red; font-family:cursive">rojo y cursiva</span>` se convierte en <span style="color:red; font-family:cursive">rojo y cursiva</span> |
| Centrar texto  | `<p style="text-align:center">Etiqueta centrada</p>` centra el texto en la pantalla (solo en KoboCollect) |
| Ocultar etiqueta | `<span style="display:none">Etiqueta oculta</span>` omite la etiqueta de la pregunta (solo en formularios web) |
| Eliminar negrita | `<span style="font-weight: normal;">¿Cuál es tu edad?</span>` elimina la negrita de la etiqueta de la pregunta (solo en formularios web) |
| Subrayado      | `<span style="text-decoration: underline;">Este texto está subrayado</span>` subraya el texto (solo en formularios web) |

<p class="note">
<strong>Nota:</strong> Usa el carácter <code>\</code> antes de <code>#</code>, <code>*</code>, <code>_</code> y <code>\</code> para evitar que estos caracteres activen efectos de estilo especiales.
</p>