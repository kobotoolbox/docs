Looking at the issues:

1. **Issue on line 3** (`es_gender_inclusive`, rule_id): The suggestion says to *change* "los usuarios" to "los/as usuarios/as" — but the rule `es_gender_inclusive` explicitly requires **avoiding** slash forms and using **standard masculine plural** instead. The suggestion in the issue is backwards (it proposes the wrong form as the fix). Since applying this suggestion would introduce a violation of the very rule it cites, I skip this fix.

2. **Issue on line 11**: The explanation itself says "Skipping." — no change needed.

# Añadir traducciones en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/26219c3ff68ab5e06bc080c11ae388324a894200/source/language_xls.md" class="reference">5 Jun 2026</a>

Agregar traducciones a un formulario permite a los usuarios cambiar a su idioma preferido durante la recolección de datos sin necesidad de crear formularios separados. Se puede agregar cualquier número de traducciones. Tanto [KoboCollect](../es/data_collection_kobocollect.html) como los [formularios web](../es/data_through_webforms.html) admiten traducciones de formularios.

La mayoría de los elementos que se muestran en el formulario pueden traducirse, como las **etiquetas de preguntas**, las **sugerencias**, las **etiquetas de opciones**, los **mensajes de restricción** y los **mensajes obligatorios**. Los elementos utilizados para la estructura del formulario, como los nombres de preguntas, los nombres de opciones y los nombres de listas, no pueden traducirse y deben permanecer en el idioma utilizado para el desarrollo del formulario y el análisis de datos.

<p class="note">
  <strong>Nota:</strong> Agregar traducciones en XLSForm es más rápido y eficiente que <a href="../es/language_dashboard.html">usar la interfaz de KoboToolbox</a>, especialmente para formularios más extensos. Para aprender a descargar tu formulario en XLSForm y agregar traducciones, consulta <a href="xlsform_with_kobotoolbox.html">Usar XLSForm con KoboToolbox</a>.
<br><br>
Para practicar la adición de traducciones en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

Cuando tu formulario incluye varias traducciones, KoboCollect y los formularios web mostrarán un selector de idioma en la **esquina superior derecha del formulario**, lo que permite a los encuestados elegir su idioma preferido.

<p class="note">
    Para obtener más información sobre la recolección y gestión de datos de formularios traducidos, consulta <a href="../es/collecting_data_multiple_languages.html">Recolectar datos en diferentes idiomas</a>.
</p>

## Códigos de idioma en XLSForm

Al hacer referencia a diferentes idiomas en XLSForm, debes usar el formato `idioma (código)` en los encabezados de columna. Por ejemplo, la referencia de idioma para inglés es `English (en)` y la referencia de idioma para francés es `French (fr)`. Cada traducción debe usar el mismo nombre de idioma y código de manera consistente en todo el formulario.

Los códigos de idioma se pueden encontrar en el <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">registro de subetiquetas de idioma de la IANA</a>. En el sitio web de la IANA, **Description** hace referencia al nombre del idioma y **Subtag** hace referencia al código de idioma (por ejemplo, **Description:** French, **Subtag:** fr).


## Configurar el idioma predeterminado del formulario

Para agregar traducciones a un XLSForm, primero debes definir el idioma predeterminado. Este es el idioma en el que se abrirá el formulario por defecto.

Para definir el idioma predeterminado de tu formulario:
1. En la **hoja settings**, agrega una columna `default_language`.
2. En la columna `default_language`, ingresa el idioma predeterminado usando el formato `idioma (código)`.
    - Por ejemplo: `English (en)`.

**hoja settings**

| default_language |
| :---------------- |
| English (en)      |
| settings |

Para configurar la **hoja survey**:

1. Renombra la columna `label` usando el formato `label::idioma (código)`.
    - Por ejemplo: `label::English (en)`.
2. Si tu formulario incluye columnas `hint`, `required_message`, `constraint_message` o `media` en la **hoja survey**, renombra las columnas existentes usando el formato `nombre_columna::idioma (código)`.
    - Por ejemplo: `hint::English (en)`.

**hoja survey**

| type | name | label::English (en) | hint::English (en) |
| :--- | :--- | :------------------ | :----------------- |
| integer | age | How old are you? | In years |
| select_one yn | student | Are you currently a student? | |
| survey |

Por último, para configurar la **hoja choices**, renombra la columna `label` usando el formato `label::idioma (código)`.

**hoja choices**

| list_name | name | label::English (en) |
| :--------- | :--- | :------------------ |
| yn | yes | Yes |
| yn | no | No |
| choices |

## Agregar traducciones

Una vez que hayas definido tu idioma predeterminado, puedes agregar traducciones para cada elemento visible de tu formulario. Puedes agregar tantas columnas de traducción como desees.

<p class="note">
  <strong>Nota:</strong> Si omites el texto de un elemento traducido, aparecerá como un campo en blanco en el formulario.
</p>

Para agregar traducciones a la **hoja survey**:
1. Agrega una nueva columna `label` para cada idioma de traducción usando el formato `label::idioma (código)`.
    - Por ejemplo: `label::Spanish (es)`.
2. Si tu formulario incluye columnas `hint`, `required_message`, `constraint_message` o `media` en la **hoja survey**, configura las columnas de traducción correspondientes usando el formato `nombre_columna::idioma (código)`.
    - Por ejemplo: `hint::French (fr)` o `required_message::Chichewa (ny)`.
3. Ingresa las traducciones de todos los elementos del formulario en las columnas correspondientes.

<p class="note">
  Para obtener más información sobre la gestión de archivos multimedia en formularios traducidos, consulta <a href="../es/media.html#adding-media-to-translations">Agregar archivos multimedia a un XLSForm</a>.
</p>

**hoja survey**

| type | name | label::English (en) | label::Chichewa (ny) | hint::English (en) | hint::Chichewa (ny) |
| :--- | :--- | :------------------ | :------------------- | :----------------- | :------------------ |
| integer | age | How old are you? | Muli ndi zaka zingati? | In years | M'zaka |
| select_one yn | student | Are you currently a student? | Kodi panopa ndinu wophunzira? | | |
| survey |

Para agregar traducciones a la **hoja choices**:
1. Agrega una nueva columna `label` para cada idioma de traducción usando el formato `label::idioma (código)`.
    - Por ejemplo: `label::Spanish (es)`.
2. Ingresa la traducción de cada etiqueta de opción en la columna de traducción correspondiente.
3. Si tu **hoja choices** incluye columnas de multimedia, configura las columnas de traducción correspondientes usando el formato `nombre_columna::idioma (código)`.

<p class="note">
  <strong>Nota:</strong> Para obtener más información sobre la gestión de archivos multimedia en formularios traducidos, consulta <a href="../es/media.html#adding-media-to-translations">Agregar archivos multimedia a un XLSForm</a>.
</p>

**hoja choices**

| list_name | name | label::English (en) | label::Chichewa (ny) |
| :--------- | :--- | :------------------ | :------------------- |
| yn | yes | Yes | Inde |
| yn | no | No | Ayi |
| choices |


## Pautas para las traducciones

### Usar funciones de hojas de cálculo para traducciones en bloque

XLSForm facilita la traducción de elementos del formulario en bloque, en lugar de ingresar las traducciones una por una. Por ejemplo, puedes copiar una columna completa en un sistema de traducción para traducirla en bloque y luego pegarla de nuevo en tu XLSForm. Si usas Google Sheets para crear tu XLSForm, puedes usar la fórmula `GOOGLETRANSLATE()` para automatizar el proceso de traducción.

Las traducciones automáticas siempre deben ser revisadas y validadas por una persona con dominio del idioma para garantizar la precisión, la adecuación cultural y el contexto apropiado. Este paso ayuda a mantener la calidad y confiabilidad del contenido traducido.

### Traducir a escrituras no latinas

Las escrituras no latinas, como el árabe, el cirílico, el tamil, el nepalés o el hindi, son totalmente compatibles con KoboToolbox y pueden usarse como idiomas predeterminados o como traducciones.

<p class="note">
  <strong>Nota:</strong> Se recomienda usar solo caracteres latinos para los <strong>nombres</strong> de preguntas y opciones, ya que las escrituras no latinas pueden causar errores o problemas de compatibilidad al exportar datos o trabajar con XLSForm. Sin embargo, las <strong>etiquetas</strong> de preguntas y opciones pueden usar cualquier escritura sin inconvenientes.
</p>

Al agregar traducciones en escrituras no latinas, es fundamental **usar caracteres Unicode correctos**. Unicode garantiza que el texto se muestre y se interprete correctamente en todos los dispositivos y plataformas.

Para ingresar texto en Unicode, no es necesario instalar fuentes especiales. En su lugar, configura el teclado del sistema en el idioma o escritura correspondiente y escribe con normalidad. Evita usar pseudofuentes (es decir, fuentes especiales que imitan visualmente escrituras no latinas reasignando caracteres latinos), ya que no son compatibles con KoboToolbox y pueden causar problemas graves de visualización e integridad de los datos. Si usas Windows y necesitas ayuda para configurar el teclado del sistema, consulta la [documentación de Microsoft](https://support.microsoft.com/en-us/windows/manage-the-language-and-keyboard-input-layout-settings-in-windows-12a10cb4-8626-9b77-0ccb-5013e0c7c7a2).

### Traducir escrituras de derecha a izquierda

Al agregar un idioma que usa una escritura de derecha a izquierda (RTL), como el árabe, el hebreo o el urdu, es importante **usar el código de idioma correcto** y asegurarse de que el **primer texto visible en la traducción** (por ejemplo, una etiqueta de pregunta, una sugerencia o una nota) esté escrito en el idioma RTL. Esto garantizará que el diseño del formulario no adopte por defecto el formato de izquierda a derecha (LTR).

Además, al incorporar referencias a preguntas dentro de las etiquetas de preguntas con escrituras RTL, ten en cuenta que la sintaxis de referencia a preguntas se invierte (es decir, `{nombre_pregunta}$`).

**hoja survey**

| type | name | label::English (en) | label::Arabic (ar) |
| :--- | :--- | :------------------ | :----------------- |
| begin\_group | profile | Respondent profile | ملف المستجيب |
| text | name | Respondent's name | اسم المدعى عليه |
| integer | age | How old is ${name}? | ؟{name}$ كم عمرك |
| end\_group | | | |
| survey |



## Resolución de problemas

<details>
<summary><b>Aparece un idioma sin nombre después de cargar un XLSForm</b></summary>
Es posible que aparezca un idioma sin nombre si en tu XLSForm faltan columnas de traducción para el contenido visible por los encuestados, como las columnas <code>hint</code>, <code>guidance_hint</code>, multimedia, <code>constraint_messages</code> o <code>required_message</code>. Hasta que esto se corrija, el texto de estas columnas aparecerá en blanco para todos los idiomas que no sean el idioma predeterminado.<br><br>También puede aparecer un idioma sin nombre si configuraste un <code>default_language</code> en la pestaña <code>settings</code>, como <code>English (en)</code>, pero tu formulario solo tiene un idioma y usa <code>label</code> en lugar de <code>label::English (en)</code>. Para corregir esto, elimina la configuración del idioma predeterminado en la pestaña <code>settings</code>.<br><br>Por último, puede aparecer un idioma sin nombre si cargas un XLSForm en un proyecto que antes tenía varios idiomas, pero ahora solo tiene un idioma sin especificar. Si tu formulario ahora tiene un solo idioma, abre la <a class="reference external" href="../es/language_dashboard.html">interfaz de traducciones</a>, establece el idioma sin nombre como idioma predeterminado y luego elimina los demás idiomas.
</details>

<br>

<details>
<summary><b>Quedan idiomas adicionales o innecesarios después de cargar un XLSForm</b></summary>
   Si cargas un XLSForm que tiene menos idiomas que una versión anterior del mismo proyecto, es posible que KoboToolbox siga mostrando los idiomas de la versión anterior. Para eliminar los idiomas que ya no se necesitan, abre la <a class="reference external" href="../es/language_dashboard.html">interfaz de traducciones</a> en KoboToolbox y elimina los idiomas que ya no se usan.
</details>