# Seleccionar opciones de un mapa
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/select_from_map_xls.md" class="reference">23 Apr 2026</a>

Con los tipos de pregunta `select_one` y `select_one_from_file`, puedes configurar tu XLSForm para que los usuarios seleccionen una opción directamente desde un mapa en lugar de una lista. Cuando se abre el mapa, muestra todos los puntos, líneas o polígonos disponibles según las opciones proporcionadas. Los usuarios pueden tocar un elemento en el mapa para registrar su selección. Esta funcionalidad está disponible **únicamente en KoboCollect.**

Este artículo explica cómo configurar tu XLSForm para permitir la selección de opciones desde un mapa, cómo personalizar opciones de estilo como colores, símbolos y anchos de línea, y cómo se muestran y seleccionan las opciones en el mapa.

<p class="note">
<strong>Nota:</strong> El editor de formularios de KoboToolbox (Formbuilder) no admite la selección basada en mapas para el tipo de pregunta <code>select_one</code>. Para usar esta funcionalidad, configúrala en un XLSForm y carga el formulario en KoboToolbox.
  <br><br>
  Para obtener más información sobre cómo descargar y editar tu formulario como XLSForm, consulta <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html">Usar XLSForm con KoboToolbox</a>.
</p>

## Configurar tu XLSForm

Para configurar una pregunta de **selección desde un mapa** en XLSForm:
1. En la **hoja survey**, agrega una pregunta de tipo `select_one` o `select_one_from_file`.
2. Añade una columna `appearance`.
3. En la columna `appearance` de la pregunta de selección, escribe `map` o `quick map`.
    - La **apariencia map** permite a los encuestados hacer clic en diferentes ubicaciones y ver información sobre cada una antes de confirmar su selección.
    - La **apariencia quick map** registra automáticamente la primera ubicación seleccionada sin mostrar información adicional.

**hoja survey**

| type        | name     | label                       | appearance |
|:------------|:---------|:----------------------------|:-----------|
| select_one  | location | ¿Dónde estás ubicado actualmente? | map       |
| survey |

4. En la **hoja choices** o en tu [lista externa de opciones](https://support.kobotoolbox.org/es/select_from_file_xls.html), ingresa las opciones como lo harías normalmente.
5. Junto a tu lista de opciones, agrega una columna `geometry`.
6. Para cada opción, ingresa las coordenadas GPS correspondientes en la columna `geometry`.
    - Este campo puede incluir coordenadas GPS únicas o múltiples para definir un punto, una línea o un polígono.

**hoja choices**

| list_name | name | label  | geometry           |
|:----------|:-----|:-------|:------------------|
| cities    | 1    | Warsaw | 52.2297 21.0122 0 0 |
| cities    | 2    | Berlin | 52.5200 13.4050 0 0 |
| cities    | 3    | Paris  | 48.8566 2.3522 0 0  |
| cities    | 4    | Kyiv   | 50.4501 30.5234 0 0 |
| cities    | 5    | Prague | 50.0755 14.4378 0 0 |
| choices |

### Formato de las coordenadas GPS

Al ingresar coordenadas GPS en la **hoja choices** o en un archivo CSV o XML externo, se debe usar el siguiente formato: `longitud latitud altitud precisión`.

- Por ejemplo, las coordenadas GPS de París serían `48.8566 2.3522 0 0`.

Cuando se proporcionan múltiples coordenadas GPS (por ejemplo, para una línea o polígono), las coordenadas se separan con un punto y coma.
- Por ejemplo, las coordenadas GPS de una línea que va de París a Madrid serían `48.8566 2.3522 0 0;40.4637 -3.6556 0 0`.
- Para un polígono, las coordenadas GPS deben comenzar y terminar con las mismas coordenadas.

<p class="note">
<strong>Nota:</strong> Para obtener tus coordenadas GPS en el formato correcto, puedes usar este <a href="https://ee.kobotoolbox.org/preview/7OmWg7pD">formulario de KoboToolbox</a>. Te permite seleccionar puntos en un mapa y genera automáticamente las coordenadas GPS correspondientes en formato ODK.
</p>

Si usas un archivo GeoJSON para proporcionar coordenadas GPS, sigue el [formato GeoJSON](https://docs.getodk.org/form-datasets/#selects-from-geojson) para especificar la `geometry` del elemento.

<p class="note">
  Para ver un ejemplo de preguntas de selección basadas en mapas, consulta este <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/SelectFromMap.xlsx">XLSForm de ejemplo</a>. Los archivos de opciones externas para cargar en KoboToolbox están disponibles <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities1.csv">aquí</a> (CSV), <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities2.geojson">aquí</a> (GeoJSON) y <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities3.xml">aquí</a> (XML). Para obtener más información sobre el uso de archivos de opciones externas, consulta <a href="https://support.kobotoolbox.org/es/select_from_file_xls.html">Seleccionar opciones de un archivo externo en XLSForm</a>.
</p>

## Agregar propiedades a las opciones

Puedes personalizar aún más tu mapa agregando propiedades a las opciones en la **hoja choices** o en el archivo de opciones externo.

Las propiedades de opciones disponibles son:

| Propiedad de opción | Descripción |
|:----------------|:------------|
| `info`            | Descripción de texto de la opción. |
| `marker-color`    | Color HEX para el marcador de geopunto. |
| `marker-symbol`   | Carácter, símbolo o emoji que se muestra en el marcador de geopunto. |
| `stroke`          | Color HEX para la línea de geotrazado o el contorno del polígono de geoforma. |
| `stroke-width`    | Ancho de la línea de geotrazado o el contorno del polígono de geoforma (por ejemplo, 5 o 6.5). |
| `fill`            | Color HEX para el interior del polígono. El color de relleno se muestra con transparencia fija. |

Para agregar propiedades en la **hoja choices** de tu XLSForm:

1. Agrega una columna con el nombre de propiedad correspondiente (por ejemplo, `info`, `stroke` o `fill`).
2. Para cada opción, ingresa el valor correspondiente (por ejemplo, una descripción de texto o un código HEX).

**hoja choices**

| list_name | name | label  | geometry           | info                       |
|:----------|:-----|:-------|:------------------|:---------------------------|
| cities    | 1    | Warsaw | 52.2297 21.0122 0 0 | Capital de Polonia          |
| cities    | 2    | Berlin | 52.5200 13.4050 0 0 | Capital de Alemania         |
| cities    | 3    | Paris  | 48.8566 2.3522 0 0  | Capital de Francia          |
| cities    | 4    | Kyiv   | 50.4501 30.5234 0 0 | Capital de Ucrania         |
| cities    | 5    | Prague | 50.0755 14.4378 0 0 | Capital de la República Checa  |
| choices |

Si usas un archivo GeoJSON para proporcionar coordenadas GPS, sigue el [formato GeoJSON](https://docs.getodk.org/form-datasets/#selects-from-geojson) para especificar las `properties` del elemento.

## Selección en el mapa con KoboCollect

<iframe src="https://www.youtube.com/embed/C7o9rCKmCeo?si=h9y-meFvNwury_mI&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<p class="note">
<strong>Nota:</strong> La selección de opciones desde un mapa está <strong>disponible únicamente en KoboCollect.</strong> En los formularios web, las opciones aparecerán como una lista normal de opciones.
</p>

En KoboCollect, agregar una **pregunta de tipo selección** con la apariencia `map` o `quick map` permite a los usuarios elegir una opción directamente desde un mapa en lugar de una lista. Cuando se abre el mapa, se centra en la ubicación actual del dispositivo. Los botones de la derecha permiten volver a centrar el mapa en la ubicación del usuario o mostrar todos los puntos disponibles en el mapa.

Las opciones de tipo punto se muestran como marcadores en el mapa. Al tocar un marcador, este aumenta de tamaño.
Las opciones de tipo línea y polígono se muestran como contornos rojos, con los polígonos sombreados en rojo. Los usuarios pueden tocar una línea o polígono para seleccionarlo. Cuando se selecciona una ubicación, sus [propiedades](https://support.kobotoolbox.org/es/select_from_map_xls.html#adding-choice-properties) aparecen en la parte inferior de la pantalla, a menos que se use la apariencia `quick map`.

Debajo de la etiqueta de la opción, aparece un botón **Seleccionar** para confirmar y guardar la ubicación seleccionada en el formulario, a menos que se use la apariencia `quick map`.

<p class="note">
<strong>Nota:</strong> Las apariencias <code>map</code> y <code>quick map</code> se pueden combinar con <a href="https://support.kobotoolbox.org/es/choice_filters_xls.html">filtros de selección</a> para mostrar opciones en el mapa según una selección previa.
</p>