# Agregar otro idioma a tu XLSForm
<a href="../language_xls.html">Read in English</a> | <a href="../fr/language_xls.html">Lire en français</a> | <a href="../ar/language_xls.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/language_xls.md" class="reference">29 Jul 2025</a>

Existen dos métodos para agregar múltiples idiomas a tu formulario. Puedes
agregarlos y manejarlos directamente a través del
[Panel de Control del Proyecto](language_dashboard.md) en línea o puedes agregarlos en un XLSForm y
subirlo a Kobo.

Aquí hay instrucciones detalladas sobre cómo puedes agregar otro idioma a tu formulario:

-   Crea tu formulario en el idioma predeterminado. Este debe ser el idioma con
    el que la persona responsable de diseñar el cuestionario se sienta más cómoda.
    Cuando hayas terminado, o cuando se haya creado una parte del formulario,
    guárdalo. Regresarás al panel de control del proyecto del formulario borrador.

-   Exporta el formulario a XLS.

-   Abre el archivo en Excel (Google Spreadsheet, Open Office Calc, etc., todos
    funcionarán) (Si estás en Excel es posible que tengas que sacar el archivo de
    Vista Protegida primero.
    [Ver aquí](https://support.office.com/en-us/article/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653?ocmsassetID=HA010355931&CorrelationId=04b441d5-5c7c-441a-bbac-8f34b3071869&ui=en-US&rs=en-US&ad=US).)
    Tu hoja de cálculo tendrá tres hojas (mira las pequeñas pestañas en la parte inferior):
    **survey**, **choices**, **settings**. Permanece en la hoja **survey** por ahora.

-   Encuentra la columna llamada `label`. Aquí es donde se almacenan las etiquetas
    de tus preguntas originales. Inserta otra columna a la derecha de label. En el encabezado
    (primera fila) de esta nueva columna, escribe `label::idioma (código)`, por ejemplo
    `label::Français (fr)` o `label::English (en)`.

<p class="note">Puedes cambiar el tamaño de tus columnas, agregar colores o cambiar el tamaño de la fuente, ninguno de estos afectará tu formulario.</p>

-   Luego, si tienes sugerencias en tu formulario, lo mismo debe aplicarse a la columna `hint`,
    por ejemplo `hint::Français (fr)` o `hint::English (en)`.

**hoja survey**

| type             | name           | label                          | relevant                  |
| :--------------- | :------------- | :----------------------------- | :------------------------ |
| text             | full_name      | What is your name?             |                           |
| select_one yesno | children_yesno | Do you have any children?      |                           |
| integer          | children_count | How many children do you have? | ${children_yesno} = 'yes' |
| survey |

-   Ahora agrega tus traducciones para cada fila dentro de la columna `label::idioma (código)`.
    Cuando hayas terminado, asegúrate de no haber omitido ninguna pregunta (para
    cada campo que tenga texto dentro de la columna label debe haber texto
    dentro de la columna `label::idioma (código)`). Puedes encontrar los códigos
    oficiales de idioma de 2 caracteres (subetiquetas)
    [aquí](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry).

<p class="note">Consejo: Copia y pega la columna label original y luego haz cambios a las traducciones para que no dejes nada en blanco por accidente: Es mejor tener algo mostrándose en el idioma incorrecto que tener una pregunta en blanco en algún idioma. <em>Puedes repetir este paso y agregar tantos idiomas como desees, cada uno en sus columnas separadas y con un nombre diferente dentro de <code>label::idioma (código)</code>.</em></p>

**hoja survey**

| type             | name           | label:English (en)             | label::Français (fr)           | relevant                  |
| :--------------- | :------------- | :----------------------------- | :----------------------------- | :------------------------ |
| text             | full_name      | What is your name?             | Quel est votre nom?            |                           |
| select_one yesno | children_yesno | Do you have any children?      | Avez-vous des enfants?         |                           |
| integer          | children_count | How many children do you have? | Combien des enfants avez-vous? | ${children_yesno} = 'yes' |
| survey |

-   Ahora cambia a la hoja **choices** de tu archivo, si tienes una.

-   En la hoja **choices** tienes otra columna llamada `label`. Repite
    los pasos 5 y 6. Asegúrate de usar exactamente la misma ortografía para
    `label::idioma (código)`. Por ejemplo, `label::Francais (fr)` y
    `label::Français (fr)` no son idénticos.

**hoja choices**

| list_name | name | label::English (en) | label::Français (fr) |
| :-------- | :--- | :------------------ | :------------------- |
| yesno     | yes  | Yes                 | Oui                  |
| yesno     | no   | No                  | Non                  |
| choices |

-   En la hoja **settings**, debajo de `form_title` edita el texto del
    título de tu formulario a algo como "Mi formulario (Inglés y Francés)" para que puedas
    identificarlo fácilmente más tarde.

**hoja settings**

| form_title                      |
| :------------------------------ |
| Mi formulario (Inglés y Francés) |
| settings |

-   Guarda tu archivo y cierra Excel.

-   Regresa a KoboToolbox y haz clic en **Reemplazar con XLS**, luego sube tu
    XLSForm actualizado. Elige el archivo que acabas de terminar de editar y haz clic en **OK**.

-   Abre el formulario que acabas de subir y haz clic en **Vista previa del formulario**. En la parte superior
    junto a **Elegir idioma** haz clic en el menú desplegable. Tendrá un predeterminado
    (tu idioma original) así como los nuevos idiomas que acabas de agregar.

## Traducir a escrituras Tamil, Nepalí, Hindi, etc.

Cuando traduzcas a escrituras no latinas, como Tamil, Nepalí, Hindi, etc., por favor
asegúrate de no usar una fuente llamada pseudo fuente. Cuando escribas en estos
idiomas asegúrate de usar solo los caracteres Unicode apropiados. Para escribir caracteres
Unicode apropiados no tienes que instalar ninguna fuente en particular. En su lugar, tú
(o tu traductor/a) necesitan configurar tu teclado para usar la escritura respectiva
(Tamil, Nepalí, etc.) y luego escribir normalmente. La configuración correcta del teclado
producirá las letras de escritura reales en Unicode en lugar de algunos equivalentes fonéticos
latinos. (Esta también sería la misma forma de escribir estos idiomas en un
correo electrónico, KoboToolbox o cualquier otra aplicación web.

Para obtener ayuda con la adición del teclado del sistema correcto,
[consulta este enlace](https://support.microsoft.com/en-us/help/17424/windows-change-keyboard-layout)
(solo Windows).

Las pseudo fuentes permiten escribir en estas escrituras y se usan comúnmente en muchos
países, particularmente en el sur de Asia. Pero aunque funcionan en la computadora que
tiene una fuente específica instalada, no funcionarán en ninguna otra computadora que
no use esa fuente en particular. Esto se debe a que estas fuentes solo disfrazan
caracteres y símbolos latinos regulares y los hacen aparecer en una forma diferente.
Por ejemplo, cuando se escribe "Hello" con la pseudo fuente nepalí 'Preeti', se
verá así: हेल्लो. Pero lo que realmente está escrito allí siguen siendo las letras H e
l l o. Para algunas personas que usan estas fuentes que a menudo usan equivalentes fonéticos al
inglés, puede ser más fácil. Otra razón por la que se usan ampliamente es que muchas
computadoras solían no tener soporte para estas escrituras y por lo tanto necesitaban pseudo
fuentes como un "truco". De cualquier manera, los caracteres Unicode son la mejor manera de hacerlo - y
la única manera para usar en KoboToolbox.

## Traducir escrituras de derecha a izquierda

Al agregar un idioma que usa escritura de derecha a izquierda es importante usar el
código de idioma correcto, sin embargo, incluso si se usa el código correcto, si la primera
pregunta, sugerencia o nota está escrita en una escritura de izquierda a derecha, el formulario
formateará automáticamente el resto de la traducción a un formato de izquierda a derecha.