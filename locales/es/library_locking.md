# Bloqueo de biblioteca
<a href="../library_locking.html">Read in English</a> | <a href="../fr/library_locking.html">Lire en français</a> | <a href="../ar/library_locking.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/de5e7dcfcec534ba447ee21ff65cf9fff07723f2/source/library_locking.md" class="reference">30 Sep 2025</a>

"Bloqueo de biblioteca" se refiere a la funcionalidad que permite que varios aspectos de una encuesta sean "[bloqueados](#locked)" cuando se crean a partir de una plantilla que contiene
[atributos de bloqueo](#restrictions). Todos los aspectos de la edición de un formulario están
disponibles para ser bloqueados mediante la asignación de "[perfiles de bloqueo](#profile)"
a nivel de formulario, pregunta o grupo. Estos perfiles de bloqueo pueden tener asignadas
"[restricciones](#restriction)" granulares que agrupan funcionalidades de bloqueo. Alternativamente, el formulario puede ser completamente bloqueado, evitando
todos los aspectos de edición.

<p class="note">
  Actualmente, solo se admite el bloqueo establecido dentro del propio XLSForm, pero se
  incorporará al editor de formularios de KoboToolbox (Formbuilder) en algún momento en el futuro.
</p>

Esta funcionalidad puede ser útil en un entorno de equipo grande y distribuido donde se usa una plantilla
estándar, con algunas funcionalidades bloqueadas, y cada equipo puede hacer los ajustes locales necesarios para sus necesidades. El/la creador/a de la plantilla puede continuar
haciendo actualizaciones, pero los bloqueos restringirán cambios a aspectos específicos del
formulario para quienes [creen un proyecto basado en la plantilla](quick_start.md).

<p class="note">
  Bloquear aspectos de un formulario es independiente de
  <a class="reference" href="https://support.kobotoolbox.org/managing_permissions.html">manejar permisos del proyecto</a>.
</p>

## Restricciones

Hay tres niveles de restricciones que se pueden establecer:

1. [Pregunta](#question-level-restrictions),
2. [Grupo](#group-level-restrictions), y
3. [Formulario](#form-level-restrictions)

Además, hay un booleano `kobo--lock_all` que se puede establecer en la hoja `settings`
que hará que la encuesta esté completamente bloqueada.

### Booleano `kobo--lock_all`

Si `kobo--lock_all` se establece en `True`, entonces todas las restricciones granulares adicionales
son redundantes ya que el formulario está _completamente_ bloqueado. Si se establece en `False` _o_
se omite de la hoja `settings`, entonces se pueden usar perfiles de bloqueo definidos para
controlar el comportamiento de bloqueo:

**hoja settings**

| kobo--lock_all |
| :------------- |
| true           |
| settings |

Los valores aceptados para `kobo--lock_all` son los mismos que en la hoja `survey` que
[pyxform admite](https://github.com/XLSForm/pyxform/blob/43ea039250f44cff23b3ad10740fca54dfa12383/pyxform/aliases.py#L127-L142).
No se generará ningún error si se usa un valor no válido, solo que el formulario no
funcionará como se espera desde la perspectiva del/de la usuario/a.

<p class="note">
  Ten en cuenta que el nombre de la restricción, como <code>choice_add</code> a continuación, está
  <strong>predefinido</strong> y solo las restricciones enumeradas a continuación son opciones válidas.
</p>

### Restricciones a nivel de pregunta

| Nombre                     | Descripción                                                        |
| :------------------------- | :----------------------------------------------------------------- |
| `choice_add`               | Agregar nuevas opciones a una pregunta `select_*`                  |
| `choice_delete`            | Eliminar una opción existente de una pregunta `select_*`           |
| `choice_value_edit`        | Editar un `name` de opción                                         |
| `choice_label_edit`        | Editar una `label` de opción                                       |
| `choice_order_edit`        | Reordenar las opciones de una pregunta `select_*`                  |
| `question_delete`          | Eliminar una pregunta dada                                         |
| `question_label_edit`      | Editar una `label` o `hint` existente                              |
| `question_settings_edit`   | Editar la configuración de una pregunta (aparte de `constraint` o `relevant`) |
| `question_skip_logic_edit` | Editar la configuración de lógica de salto de una pregunta (`relevant`) |
| `question_validation_edit` | Editar la configuración de criterios de validación de una pregunta (`constraint`) |

### Restricciones a nivel de grupo

| Nombre                      | Descripción                                                                                            |
| :-------------------------- | :----------------------------------------------------------------------------------------------------- |
| `group_delete`              | Botón **Eliminar todo** del modal de eliminar grupo (o botón de eliminar grupo si se combina con `group_split`)  |
| `group_split`               | Botón **Desagrupar preguntas** del modal de eliminar grupo (o botón de eliminar grupo si se combina con `group_delete`) |
| `group_label_edit`          | Editar una `label` de grupo                                                                            |
| `group_question_add`        | Agregar o clonar preguntas dentro del grupo dado (grupos hijos incluidos)                              |
| `group_question_delete`     | Eliminar cualquier pregunta del grupo dado (preguntas de grupos hijos incluidas)                       |
| `group_question_order_edit` | Cambiar el orden de las preguntas dentro del grupo dado (grupos hijos incluidos)                       |
| `group_settings_edit`       | Cambiar **Toda la configuración del grupo** desde la **Configuración** del grupo dado                  |
| `group_skip_logic_edit`     | Cambiar **Lógica de salto** desde la **Configuración** del grupo dado                                  |

### Restricciones a nivel de formulario

| Nombre                | Descripción                                                                                      |
| :-------------------- | :----------------------------------------------------------------------------------------------- |
| `form_appearance`     | Cambiar la apariencia del formulario desde **Diseño y Configuración**                           |
| `form_replace`        | Reemplazar formulario usando el modal **Reemplazar formulario**                                  |
| `group_add`           | Botón para agrupar preguntas                                                                     |
| `question_add`        | Usar la opción **Insertar selección en cascada** y cada botón **Agregar pregunta** y **Clonar pregunta** |
| `question_order_edit` | Cambiar el orden de cualquier pregunta                                                           |
| `language_edit`       | Editar idiomas en el **Modal de traducciones**                                                   |
| `form_meta_edit`      | Editar preguntas meta desde **Diseño y Configuración**                                           |

## Configuración de XLSForm

Hay tres hojas donde se definen y establecen los perfiles de bloqueo: `survey`,
`settings` y `kobo--locking-profiles`. La hoja `kobo--locking-profiles`
no está oficialmente admitida por [pyxform](https://github.com/XLSForm/pyxform) y
es específica de KoboToolbox.

Las restricciones a nivel de formulario se definen en la hoja `settings` y las restricciones a nivel de pregunta y
grupo se definen en la hoja `survey`.

Desde la hoja `kobo--locking-profiles`, todos los perfiles de bloqueo se
definen en una estructura de matriz, usando la palabra clave "[locked](#locked)" para asignar una
"[restricción](#restriction)" a un "[perfil](#profile)" específico. Por ejemplo:

**kobo--locking-profiles**

Define los perfiles y asígnales restricciones. No hay límite en el
número de perfiles que se pueden definir (`profile_1`, ..., `profile_n`) pero hay
**solo tres** colores que diferencian su apariencia de bloqueo en el
editor de formularios.

| restriction       | profile_1 | profile_2 | profile_3 |
| :---------------- | :-------- | :-------- | :-------- |
| choice_add        | locked    |           |           |
| choice_delete     |           | locked    |           |
| choice_label_edit | locked    |           |           |
| choice_order_edit | locked    | locked    |           |
| form_appearance   |           |           | locked    |
| kobo--locking-profiles |

<p class="note">
  Ten en cuenta que no todas las restricciones válidas necesitan incluirse en la
  columna <code>restriction</code>, pero se generará un error si se incluye una
  restricción no válida.
</p>

**hoja settings**

Establece restricciones a nivel de formulario y el booleano `kobo--lock_all`.

| kobo--locking-profile | kobo--lock_all |
| :-------------------- | :------------- |
| profile_3             | false          |
| settings |

<p class="note">
  Ten en cuenta que omitir <code>kobo--lock_all</code> de la
  hoja <code>settings</code> es equivalente a establecerlo en <code>False</code>.
</p>

**hoja survey**

Establece restricciones a nivel de pregunta y grupo.

| type                 | name    | label                 | kobo--locking-profile |
| :------------------- | :------ | :-------------------- | :-------------------- |
| select_one countries | country | Selecciona tu país    | profile_1             |
| select_one cities    | city    | Selecciona tu ciudad  | profile_2             |
| survey |

**hoja choices**

No se pueden establecer restricciones en la hoja `choices`.

| list_name | name      | label                    |
| :-------- | :-------- | :----------------------- |
| countries | canada    | Canadá                   |
| countries | usa       | Estados Unidos de América |
| cities    | vancouver | Vancouver                |
| cities    | toronto   | Toronto                  |
| cities    | baltimore | Baltimore                |
| cities    | boston    | Boston                   |
| choices |

<i>Este ejemplo de XLSForm se puede descargar
<a download class="reference" href="/_static/files/library_locking/library-locking-example.xlsx">aquí</a>.</i>

### Importar XLSForms bloqueados

Importa tu XLSForm como una `template` a través de la interfaz de usuario de KoboToolbox navegando a
tu **Biblioteca** y haciendo clic en **NUEVO** y luego en **Cargar**. Asegúrate de
seleccionar `template` del menú desplegable **Elegir el tipo deseado** y luego
importa tu XLSForm.

![elegir tipo de plantilla](/images/library_locking/import-template.png)

La plantilla bloqueada ahora se mostrará en la vista de lista de tu biblioteca con un símbolo de candado.

![lista de biblioteca](/images/library_locking/library-list-view.png)

### Crear proyecto desde plantilla bloqueada

Una vez que se ha agregado una plantilla bloqueada a tu biblioteca -- ya sea directamente mediante
la importación de un XLSForm como plantilla, creando una plantilla basada en una encuesta bloqueada
o agregando una plantilla bloqueada desde las colecciones públicas -- puedes crear un nuevo
proyecto. En la sección **Proyectos** de la interfaz de usuario, haz clic en **NUEVO** y luego en **Usar
una plantilla**.

![crear proyecto desde plantilla](/images/library_locking/create-project-from-template.png)

-   Elige la plantilla bloqueada que deseas usar para crear el nuevo proyecto.

![seleccionar plantilla](/images/library_locking/select-template-for-new-project.png)

-   Desde ahí, continúa para crear el proyecto.

![crear proyecto](/images/library_locking/create-project.png)

Cuando se usa esta plantilla bloqueada de ejemplo para crear un nuevo proyecto, el
editor de formularios se verá de la siguiente manera:

-   Las áreas en gris son aquellas que se han deshabilitado mediante las
    restricciones.

![vista general](/images/library_locking/formbuilder.png)

-   Un cuadro de diálogo encima de la primera pregunta mostrará una descripción general de algunas de las
    restricciones del formulario.

![cuadro de diálogo](/images/library_locking/formbuilder-dialogue-box.png)

-   Cada pregunta con perfiles de bloqueo mostrará, en su configuración, qué
    restricciones se han establecido.

![restricciones de pregunta](/images/library_locking/formbuilder-question-settings.png)

-   Algunas configuraciones a nivel de formulario también estarán en gris.

![restricciones a nivel de formulario](/images/library_locking/form-style.png)

### Validación de formulario

Los siguientes casos actualmente generarán un `FormPackLibraryLockingError`:

-   Si un nombre de perfil de bloqueo (encabezado de columna en la hoja `kobo--locking-profiles`) es "locked" (igual que la palabra clave de bloqueo)
-   Si una restricción enumerada en `kobo--locking-profiles` no es válida (no está en la
    lista de [restricciones predefinidas](#restrictions))
-   Si hay una hoja llamada `kobo--locking-profiles` pero no hay columna `restriction`
-   Si no se definen perfiles de bloqueo (encabezados de columna en la
    hoja `kobo--locking-profiles`)

<p class="note">
  La validación de las funcionalidades de bloqueo de biblioteca de XLSForm se ampliará en el
  futuro.
</p>

### Advertencias

En algunos editores de hojas de cálculo, dos guiones simples (`--`) se convierten automáticamente
en un guion largo (—), lo que dificulta escribir `kobo--` en
una celda. Por lo tanto, convertimos todas las instancias de guiones cortos y largos en dos guiones simples (cuando tienen el prefijo `kobo`). Un XLSForm con el nombre de hoja
"kobo—locking-profiles" se convertirá en `kobo--locking-profiles` y
de manera similar para los encabezados de columna.

## Representación JSON

Hay dos atributos del activo donde se puede acceder
y modificar la información de bloqueo: `asset.summary` y `asset.content`.

Si `kobo--locking-profile` es un nombre de columna en la hoja `survey`, también
se enumerará en el arreglo `asset.summary.columns`.

En `asset.summary`, los siguientes dos atributos booleanos describen una descripción general de
la estructura de bloqueo del formulario:

-   `lock_all`, y
-   `lock_any`

La lógica por la cual se establece cada uno de esos booleanos es la siguiente:

-   `lock_all` es `True` _solo_ si `kobo--lock_all` se establece en `True` en la
    hoja `settings`, de lo contrario es `False`
-   `lock_any` se establece en `True` si _cualquiera_ de los siguientes casos es `True`:
    -   `lock_all` es `True`,
    -   Se establece un `kobo--locking-profile` en la hoja `settings`, o
    -   _Al menos un_ `kobo--locking-profile` se establece en la hoja `survey`

En el ejemplo anterior, lo siguiente estará presente en `asset.summary`:

```
{
  ...,
  "columns": [
    ...,
    "kobo--locking-profile"
  ],
  "lock_all": false,
  "lock_any": true,
  ...
}
```

En `asset.content`, existe un atributo `content.kobo--locking-profiles` como
un arreglo de objetos JSON con la siguiente estructura:

```
[
  {
    "name": "profile_1",
    "restrictions": [
      "choice_add",
      "choice_label_edit",
      "choice_order_edit"
    ]
  },
  ...
]
```

En `content.settings`, lo siguiente estará presente en un objeto JSON:

```
{
  "kobo--locking-profile": "profile_3",
  "kobo--lock_all": false
}
```

Y finalmente en `content.survey`, cada pregunta a la que se le ha asignado un perfil de bloqueo
tendrá un atributo `kobo--locking-profile` de la siguiente manera:

```
[
  {
    "name": "country",
    "type": "select_one",
    ...
    "kobo--locking-profile": "profile_1"
  },
  {
    "name": "city",
    "type": "select_one",
    ...
    "kobo--locking-profile": "profile_2"
  },
  ...
]
```

## Perfiles de bloqueo y tipos de activos

De los cuatro tipos de activos (`survey`, `template`, `question` y `block`), solo
las `template`s y las `survey`s manejan funcionalidades de bloqueo de biblioteca y los bloqueos se
aplican _solo_ en las encuestas. Prácticamente, esto significa lo siguiente:

Supongamos que se importa un XLSForm que contiene funcionalidades de bloqueo válidas:

-   Si se importa como un `block`, entonces todos los rastros de bloqueo se excluyen y/o
    eliminan del activo. Esto resulta en un activo `block` que será
    equivalente al mismo formulario cargado sin ninguna funcionalidad de bloqueo;
-   Si se importa como una `survey` (importada a través de la sección **Proyectos**) o
    `template`, entonces todos los bloqueos están intactos:
    -   Si, desde el editor de formularios:
        -   se agrega una pregunta a la biblioteca, entonces todos los bloqueos se eliminan del
            nuevo activo `question`
        -   se agrega un grupo de preguntas a la biblioteca como un `block`, entonces todos
            los bloqueos se eliminan
    -   Si se crea una `template` _desde_ el activo `survey` bloqueado, entonces esa
        `template` heredará todos los bloqueos que tenía la `survey` (pero como es
        una plantilla, puedes editar el contenido en el editor de formularios),
    -   Si se crea una `survey` _desde_ una `template` bloqueada, la encuesta
        heredará todos los bloqueos que tenía la `template`

| Tipo de activo original | Proceso/acción                                     | Estado del `asset` resultante |
| :---------------------- | :------------------------------------------------- | :---------------------------- |
| `survey`                | importar archivo XLSForm de `survey` bloqueada     | bloqueado                     |
| `survey`                | crear `template` desde `survey` bloqueada          | bloqueado                     |
| `survey`                | crear `question` desde `survey` bloqueada※         | no bloqueado                  |
| `survey`                | crear `block` desde `survey` bloqueada※            | no bloqueado                  |
| `template`              | importar archivo XLSForm de `template` bloqueada   | bloqueado                     |
| `template`              | crear `survey` desde `template` bloqueada          | bloqueado                     |
| `template`              | crear `question` desde `template` bloqueada※       | no bloqueado                  |
| `template`              | crear `block` desde `template` bloqueada※          | no bloqueado                  |
| `block`                 | importar archivo XLSForm de `block` bloqueado※     | no bloqueado                  |
| `block`                 | agregar `block` bloqueado desde Biblioteca a `survey` | no bloqueado               |
| `block`                 | agregar `block` bloqueado desde Biblioteca a `template` | no bloqueado             |
| `block`                 | crear `question` desde `block` bloqueado※          | no bloqueado                  |
| `question`              | importar archivo XLSForm de `block` bloqueado※     | no bloqueado                  |
| `question`              | agregar `question` bloqueada desde Biblioteca a `survey` | no bloqueado            |
| `question`              | agregar `question` bloqueada desde Biblioteca a `template` | no bloqueado          |
| `question`              | crear `block` desde `question` bloqueada※          | no bloqueado                  |

※ Estas acciones no son posibles en la interfaz de usuario.

## Terminología

### `kobo--lock_all`

Atributo que contiene un valor booleano, establecido en la hoja `settings` y aplica
todas las restricciones de bloqueo al formulario y a todas las preguntas y grupos (haciendo
redundantes los perfiles de bloqueo granulares).

### `kobo--locking-profile`

Nombre de columna en las hojas `survey` y `settings` donde se asigna el perfil de bloqueo
a una pregunta o grupo (en `survey`) o al formulario (en `settings`).

### `kobo--locking-profiles`

Nombre de hoja donde se asignan restricciones a perfiles.

### `locked`

Palabra clave utilizada para asignar una restricción a un perfil en la
hoja `kobo--locking-profiles`.

### Perfil

El nombre asignado a un grupo de restricciones, definido en la
hoja `kobo--locking-profiles`. Se asigna a preguntas y grupos en la
hoja `survey` y al formulario en la hoja `settings`.

### Restricción

Un atributo de bloqueo granular que se puede asignar a un perfil y controlar el
comportamiento de bloqueo a nivel de pregunta, grupo o formulario.

### Desbloqueado

Un formulario que no contiene atributos de bloqueo.