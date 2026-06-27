# Apariencia de preguntas en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/9c69366d98a834d18d0284e5cc12bafde903278f/source/appearances_xls.md" class="reference">6 de mayo de 2026</a>

Los aspectos de las preguntas te permiten personalizar cómo se muestran las preguntas en el formulario y el tipo de respuestas que recolectan. Este artículo explica cómo agregar aspectos de preguntas en un XLSForm y lista los aspectos más comunes por tipo de pregunta.

Es importante tener en cuenta que algunos aspectos solo funcionan en [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html), mientras que otros solo son compatibles con [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html). Ten en cuenta tu método de recolección de datos al seleccionar los aspectos.

<p class="note">
  <b>Nota:</b> Este artículo se centra en configurar los aspectos de las preguntas en <a href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">XLSForm</a>. Para aprender a configurar los aspectos en el editor de formularios de KoboToolbox (Formbuilder), consulta la documentación <a href="https://support.kobotoolbox.org/es/using-formbuilder.html">Usar el Formbuilder</a>.
<br><br>
Para practicar con los aspectos de preguntas en XLSForm, consulta el <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals</a> de la KoboToolbox Academy.
</p>

## Agregar aspectos de preguntas

Para agregar aspectos de preguntas en un XLSForm:
1. En la **hoja survey**, añade una columna `appearance`.
2. Ingresa el nombre del aspecto en la columna `appearance`. Asegúrate de usar la ortografía y puntuación exactas del nombre del aspecto.
3. Algunos aspectos se pueden combinar y aplicar a la misma pregunta. Para combinar aspectos, ingrésalos en la misma celda separados por un espacio.

**hoja survey**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| text | description | Describe the project. | multiline |
| select_one country_list | country | Which country is this project taking place in? | autocomplete minimal |
| survey |


## Aspectos de preguntas disponibles en XLSForm
Las tablas a continuación listan los aspectos de preguntas más comunes por tipo de pregunta e indican cuáles son compatibles con formularios web y KoboCollect.

### Tipos de preguntas de selección múltiple
Las preguntas de selección múltiple permiten a los encuestados [elegir entre opciones predefinidas](https://support.kobotoolbox.org/es/question_types_xls.html#select-question-types).

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `minimal` | Muestra las opciones en un menú desplegable. | Formularios web y KoboCollect |
| `compact` | Muestra las opciones una al lado de la otra con un espaciado mínimo y sin casillas de selección. | Formularios web y KoboCollect |
| `label` | Muestra las etiquetas de las opciones sin las casillas de selección. | Formularios web y KoboCollect |
| `list-nolabel` | Muestra las casillas de selección sin las etiquetas. | Formularios web y KoboCollect |
| `autocomplete` | Agrega una barra de búsqueda en la parte superior de la lista de opciones. | Formularios web y KoboCollect (combinar con el aspecto `minimal`) |
| `likert` | Muestra las opciones de respuesta como una escala Likert (solo para `select_one`). | Formularios web y KoboCollect |
| `horizontal` | Muestra las opciones en columnas de igual tamaño, con el mismo número de opciones en cada fila. | Solo formularios web. Usa `columns` para compatibilidad con KoboCollect. |
| `columns` | Muestra las opciones en columnas de igual tamaño, con el mismo número de opciones en cada fila. | Formularios web y KoboCollect |
| `horizontal-compact` | Muestra las opciones en columnas con casillas de selección visibles. El número de columnas puede variar por fila según la longitud de cada etiqueta de opción. | Solo formularios web. Usa `columns-pack` para compatibilidad con KoboCollect. |
| `columns-pack` | Muestra las opciones en columnas con casillas de selección visibles. El número de columnas puede variar por fila según la longitud de cada etiqueta de opción. | Formularios web y KoboCollect |
| `columns-n` | Muestra las opciones disponibles en el número (n) de columnas especificado. | Formularios web y KoboCollect |
| `quick` | Avanza automáticamente el formulario a la siguiente pregunta después de seleccionar una respuesta (solo para `select_one`). | Solo KoboCollect |
| `quickcompact` | Muestra las opciones una al lado de la otra con un espaciado mínimo y sin casillas de selección, y avanza automáticamente a la siguiente pregunta después de seleccionar una respuesta (solo para `select_one`). | Solo KoboCollect |
| `map` | Muestra un mapa para seleccionar opciones. Requiere <a href="https://support.kobotoolbox.org/es/select_from_map_xls.html">definir coordenadas GPS</a> en la hoja `choices` (solo para `select_one`). | Solo KoboCollect |
| `quick map` | Muestra un mapa para seleccionar opciones y registra automáticamente la primera ubicación seleccionada sin mostrar información adicional. Requiere <a href="https://support.kobotoolbox.org/es/select_from_map_xls.html">definir coordenadas GPS</a> en la hoja `choices` (solo para `select_one`). | Solo KoboCollect |

<p class="note">
  <b>Nota:</b> Los aspectos para preguntas <code>select_one</code> y <code>select_multiple</code> también se pueden usar con preguntas de <a href="https://support.kobotoolbox.org/es/select_from_file_xls.html">selección desde archivo</a>.
</p>

### Tipos de preguntas numéricas
Las preguntas numéricas se usan para [recolectar números enteros o decimales](https://support.kobotoolbox.org/es/question_types_xls.html#numeric-question-types).

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `thousands-sep` | Formatea números grandes usando una coma como separador de miles. | Formularios web y KoboCollect |
| `bearing` | Registra una lectura de brújula en grados (solo para `decimal`), si el dispositivo cuenta con un acelerómetro o sensor de campo magnético. | Solo KoboCollect |
| `counter` | Muestra botones para aumentar y disminuir dígitos (solo para `integer`). | Solo KoboCollect |


### Tipo de pregunta rango
Las preguntas de rango se usan para [seleccionar valores dentro de un rango especificado](https://support.kobotoolbox.org/es/question_types_xls.html#numeric-question-types).

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `vertical` | Cambia la orientación de la línea numérica a una línea vertical. | Formularios web y KoboCollect |
| `picker` | En KoboCollect, muestra un selector emergente para elegir valores. En formularios web, muestra un menú desplegable. | Formularios web y KoboCollect |
| `rating` | Muestra estrellas en lugar de una línea numérica. | Formularios web y KoboCollect |
| `distress` | Muestra un termómetro en lugar de una línea numérica. | Solo formularios web |


### Tipo de pregunta texto
Las preguntas de texto permiten a los usuarios [recolectar respuestas abiertas](https://support.kobotoolbox.org/es/question_types_xls.html#text-and-note-question-types).

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `numbers` | Muestra un teclado numérico en lugar de un teclado de texto (por ejemplo, para recolectar números de teléfono). | Solo KoboCollect |
| `multiline` | Muestra un cuadro de texto más grande para respuestas de texto más largas. | Formularios web y KoboCollect |
| `url` | Muestra una URL en la que se puede hacer clic debajo del texto de la pregunta y hace que la pregunta sea de solo lectura. Requiere ingresar una URL en la columna `default` de la pregunta, o en la columna `calculation` si la URL incluye valores dinámicos. También funciona con preguntas de tipo `note`. | Formularios web y KoboCollect |
| `masked` | Oculta el texto ingresado por el encuestado (por ejemplo, una contraseña o información confidencial). | Solo KoboCollect |


### Tipo de pregunta fecha
Las preguntas de fecha se usan para [capturar fechas específicas del calendario](https://support.kobotoolbox.org/es/question_types_xls.html#date-and-time-question-types).

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `month-year` | Captura un mes y un año. | Formularios web y KoboCollect |
| `year` | Captura solo un año. | Formularios web y KoboCollect |
| `no-calendar` | Muestra un selector para elegir el día, mes y año, en lugar del selector de calendario predeterminado. | Solo KoboCollect |
| `coptic` | Muestra el calendario copto. | Solo KoboCollect |
| `ethiopian` | Muestra el calendario etíope. | Solo KoboCollect |
| `islamic` | Muestra el calendario islámico. | Solo KoboCollect |
| `bikram-sambat` | Muestra el calendario Bikram Sambat. | Solo KoboCollect |
| `myanmar` | Muestra el calendario de Myanmar. | Solo KoboCollect |
| `persian` | Muestra el calendario persa. | Solo KoboCollect |
| `buddhist` | Muestra el calendario budista. | Solo KoboCollect |


### Tipos de preguntas GPS
Las preguntas GPS se usan para [capturar las coordenadas geográficas](https://support.kobotoolbox.org/es/question_types_xls.html#gps-question-types) de una ubicación, trayecto o área directamente en tus formularios.

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `maps` | Muestra un mapa para que los usuarios visualicen la ubicación que se está registrando automáticamente (solo para `geopoint`). | Solo KoboCollect (incluido en el aspecto predeterminado de los formularios web) |
| `placement-map` | Permite seleccionar manualmente una ubicación en un mapa (solo para `geopoint`). | Solo KoboCollect (incluido en el aspecto predeterminado de los formularios web) |
| `hide-input` | Muestra un mapa más grande y oculta los demás campos de entrada (latitud, longitud, altitud, precisión). | Solo formularios web |


### Tipo de pregunta imagen
Las preguntas de imagen permiten a los usuarios [cargar o capturar imágenes](https://support.kobotoolbox.org/es/question_types_xls.html#media-question-types) directamente en sus formularios.

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `signature` | Permite a los usuarios dibujar su firma. | Formularios web y KoboCollect |
| `draw` | Permite a los usuarios hacer bocetos o dibujos. | Formularios web y KoboCollect |
| `annotate` | Permite a los usuarios anotar una imagen dibujando o escribiendo sobre ella. Los usuarios pueden cargar su propia imagen, o puedes establecer una imagen predeterminada para anotar ingresando el nombre del archivo de imagen en la columna `default` y [cargando](https://support.kobotoolbox.org/es/upload_media.html) el archivo a tu proyecto de KoboToolbox. | Formularios web y KoboCollect |
| `new` | Solicita a los usuarios que tomen una nueva foto con la cámara del dispositivo (sin carga de archivos). | Solo KoboCollect |
| `new-front` | Solicita a los usuarios que tomen una nueva foto con la cámara frontal del dispositivo. | Solo KoboCollect |


### Tipo de pregunta de código de barras
Las preguntas de código de barras permiten a los usuarios [escanear un código QR](https://support.kobotoolbox.org/es/question_types_xls.html#media-question-types) con la cámara del dispositivo en KoboCollect.

| Aspecto | Descripción | Compatibilidad |
| :--- | :--- | :--- |
| `hidden-answer` | Oculta el valor del código de barras escaneado. | Solo KoboCollect |