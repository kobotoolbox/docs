# Recolectar datos de GPS con KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/75a01d18e539cff0694a03ac2ffe032abb6a14d5/source/collect_gps.md" class="reference">23 Apr 2026</a>

KoboToolbox te permite recolectar datos de GPS en tus formularios, incluso cuando trabajas sin conexión a internet. Las preguntas GPS pueden capturar **una sola ubicación, una ruta o un área** durante la recolección de datos. Esto es útil para tareas como mapear infraestructura, hacer seguimiento de visitas de campo, monitorear sitios ambientales o registrar ubicaciones de servicios. Los datos de GPS se pueden recolectar tanto con [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html) como con [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html).

Este artículo explica cómo recolectar datos de GPS en KoboToolbox, incluyendo los tipos de preguntas GPS disponibles, cómo se recolectan los datos de GPS en formularios web y en KoboCollect, cómo usar datos de GPS en lógica avanzada de formularios, cómo gestionar datos de GPS en KoboToolbox y cómo resolver problemas comunes de GPS.

## Configurar tu formulario para recolectar datos de GPS

KoboToolbox admite tres tipos de preguntas GPS para recolectar datos geográficos directamente en un formulario, varias opciones de metadatos que recolectan información de ubicación automáticamente en segundo plano, y preguntas de selección basadas en mapas en XLSForm.

### Tipos de preguntas GPS

Las preguntas GPS son visibles para los encuestados. Permiten que los encuestados recolecten coordenadas GPS seleccionando manualmente o registrando automáticamente un punto, una línea o un área. Los siguientes tipos de preguntas GPS están disponibles en KoboToolbox:

| Formbuilder | XLSForm | Descripción |
| :--- | :--- | :--- |
| Point | `geopoint` | Recolecta una sola ubicación geográfica, como las coordenadas de una escuela, clínica o vivienda. |
| Line | `geotrace` | Recolecta múltiples puntos GPS que forman una línea, como un camino, carretera o ruta. |
| Area | `geoshape` | Recolecta múltiples puntos GPS que forman un área cerrada, como una parcela de tierra o un campo. |

<p class="note">
Para obtener más información sobre cómo agregar preguntas GPS a tus formularios, consulta <a href="https://support.kobotoolbox.org/es/gps_questions.html">Preguntas GPS en KoboToolbox</a> y <a href="https://support.kobotoolbox.org/es/question_types_xls.html#gps-question-types">Tipos de preguntas en XLSForm</a>.
</p>

### Preguntas de metadatos GPS

Las preguntas de metadatos GPS no son visibles para los encuestados. Cuando se activan, recolectan datos de GPS automáticamente en segundo plano durante el llenado del formulario. Los siguientes tipos de preguntas de metadatos están disponibles en KoboToolbox:

| Formbuilder | XLSForm | Descripción |
| :--- | :--- | :--- |
| audit | `audit` | Registra la ubicación GPS detallada y otra información de auditoría durante el llenado del formulario, incluyendo información de ubicación para cada pregunta a medida que se completa el formulario. |
| start geopoint early | `start-geopoint` | Captura automáticamente una sola ubicación en segundo plano cuando se abre el formulario. |
| *No disponible* | `background-geopoint` | Captura automáticamente una sola ubicación en segundo plano después de que los encuestados responden una pregunta específica. |

<p class="note">
Para obtener más información sobre cómo agregar metadatos GPS a tus formularios, consulta <a href="https://support.kobotoolbox.org/es/form_meta.html#">Agregar metadatos en el Formbuilder</a> y <a href="https://support.kobotoolbox.org/es/metadata_xls.html#">Metadatos en XLSForm</a>.
</p>

### Seleccionar opciones de un mapa

Además de recolectar coordenadas GPS, también puedes permitir que los encuestados seleccionen ubicaciones predefinidas en un mapa en XLSForm. Esto se configura usando una **pregunta de selección** con la apariencia `map` o `quick map`, junto con una columna `geometry` en la hoja choices que almacena las coordenadas de cada opción.

<p class="note">
Para obtener más información sobre cómo configurar preguntas de selección desde un mapa, consulta <a href="https://support.kobotoolbox.org/es/select_from_map_xls.html">Seleccionar opciones de un mapa</a>.
</p>

## Recolectar datos de GPS

Los datos de GPS se pueden recolectar tanto en [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html) como en la aplicación [KoboCollect](https://support.kobotoolbox.org/es/data_collection_kobocollect.html), pero el proceso de recolección difiere entre ellos.

### Formularios web

Al usar formularios web, los encuestados pueden ingresar datos de GPS de varias maneras:

- Detectar la ubicación actual del dispositivo
- Seleccionar una ubicación directamente en el mapa
- Buscar una dirección
- Ingresar coordenadas GPS manualmente

Para preguntas de línea y área, los encuestados pueden agregar múltiples puntos en el mapa para crear una ruta o polígono.

![Ubicación GPS](images/collect_gps/webform.png)

<p class="note">
<strong>Nota:</strong>
Puedes detectar la ubicación actual del dispositivo haciendo clic en el <strong>botón de ubicación</strong> en la esquina superior derecha, junto a la barra de búsqueda.
</p>

Puedes usar [apariencias](https://support.kobotoolbox.org/es/gps_questions.html#advanced-appearances) para cambiar cómo se muestra la pregunta GPS en los formularios web, específicamente para ocultar los campos de entrada de coordenadas GPS. Sin embargo, los formularios web no te permiten impedir completamente la selección manual de ubicación. Si quieres recolectar una ubicación automáticamente sin permitir la selección manual, usa **background-geopoint** en su lugar.

### KoboCollect

<iframe src="https://www.youtube.com/embed/akG0_cESv6U?si=vB9ByYkcP74Neu8x&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

En KoboCollect, los datos de GPS se capturan automáticamente desde la ubicación actual del dispositivo cuando el usuario toca un botón. La selección manual de ubicación no está activada por defecto para las preguntas de punto, aunque las [apariencias](https://support.kobotoolbox.org/es/gps_questions.html#advanced-appearances) adicionales pueden cambiar el comportamiento de las preguntas GPS.

El método de captura en KoboCollect varía según el tipo de pregunta:

| Tipo de pregunta | Captura de datos GPS |
| :--- | :--- |
| Point / `geopoint` | Toca **Get point** para comenzar a capturar la ubicación del dispositivo. <br><ul><li>Una vez que el dispositivo alcanza la precisión objetivo predeterminada de **5 metros o mejor**, el punto se registra automáticamente.</li><li>El encuestador también puede tocar **Save** para registrar la ubicación actual manualmente antes de alcanzar esa precisión.</li></ul> |
| Line / `geotrace` | Toca **Get line** y haz clic en <i class="k-icon-qt-point"></i> para elegir un método de entrada. Los métodos disponibles son: <br><ul><li><strong>Placement by tapping (ubicación con toque):</strong> El encuestador toca puntos manualmente en el mapa para trazar la línea.</li><li><strong>Manual location recording (registro de localización manual):</strong> El encuestador se desplaza a cada ubicación y toca Record a Point para capturar cada punto desde la posición actual del dispositivo.</li><li><strong>Automatic location recording (registro de localización automática):</strong> La aplicación registra puntos automáticamente mientras el encuestador se desplaza, según un intervalo de tiempo seleccionado y la precisión requerida.</li></ul>Una línea requiere al menos dos puntos. Después de registrar los puntos, haz clic en el botón **Save** en la esquina inferior izquierda. |
| Area / `geoshape` | Toca **Get polygon** y haz clic en <i class="k-icon-qt-point"></i> para elegir un método de entrada. Los mismos métodos de entrada descritos anteriormente están disponibles, pero para crear un área cerrada en lugar de una línea. Un área requiere al menos tres puntos. |

Más allá del comportamiento predeterminado, puedes usar [apariencias](https://support.kobotoolbox.org/es/gps_questions.html#advanced-appearances) para cambiar cómo funcionan las preguntas GPS en KoboCollect. Por ejemplo, puedes usar apariencias para:

- Mostrar un mapa de la ubicación seleccionada automáticamente
- Activar la selección manual de ubicación

<p class="note">
Para obtener más información sobre las apariencias de preguntas GPS, consulta <a href="https://support.kobotoolbox.org/es/gps_questions.html#advanced-appearances">Preguntas GPS en KoboToolbox</a>.
</p>

También puedes configurar los ajustes de mapa de KoboCollect para controlar cómo se muestran los mapas en las preguntas basadas en GPS, incluyendo la definición de la fuente del mapa, la selección de un estilo de mapa y la adición de [capas de mapas sin conexión](https://docs.getodk.org/collect-offline-maps/).

<p class="note">
Para obtener más información sobre los ajustes de mapa de KoboCollect, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#maps-settings">Personalizar la configuración de KoboCollect</a>.
</p>

## Mejorar la precisión del GPS

La precisión del GPS depende tanto del dispositivo como del entorno. Puede verse afectada por factores como si el dispositivo tiene el GPS activado y un sensor GPS integrado, cuándo fue la última vez que determinó su ubicación, si está usando servicios de ubicación por satélite o por red, y las condiciones ambientales como la nubosidad o los edificios y árboles cercanos.

### Parámetros GPS

Al crear formularios en XLSForm, puedes usar [parámetros](https://support.kobotoolbox.org/es/question_options_xls.html#question-parameters) para controlar la precisión del GPS con mayor detalle.

Los parámetros más comunes son:

| Parámetro | Ejemplo | Descripción |
| :--- | :--- | :--- |
| `capture-accuracy` | `capture-accuracy=15` | Captura automáticamente el punto una vez que el dispositivo alcanza la precisión objetivo. Si se configura como 0, el encuestador debe aceptar el punto explícitamente. El valor predeterminado es 5 metros. |
| `warning-accuracy` | `warning-accuracy=30` | Activa un mensaje de advertencia si la precisión del GPS no está dentro del umbral de precisión especificado. Esto no impide guardar el punto. El valor predeterminado es 100 metros. |

<p class="note">
<strong>Nota:</strong>
Para la mayoría de los flujos de trabajo, un <strong>capture-accuracy</strong> de alrededor de <strong>5 metros</strong> es un objetivo práctico. En general, no se recomienda establecer el objetivo por debajo de <strong>3 metros</strong> a menos que estés usando un dispositivo GPS externo, ya que el GPS integrado de los dispositivos a menudo no es suficientemente preciso para alcanzar ese nivel de manera confiable.
</p>

### Recomendaciones para mejorar la precisión del GPS

Para mejorar la precisión del GPS:

- Recolecta datos al aire libre en un área abierta con vista despejada del cielo
- Aléjate de edificios, árboles y otras obstrucciones
- Asegúrate de que tu cuerpo no esté bloqueando la vista del cielo del dispositivo
- Precalienta el GPS del dispositivo incluyendo `start-geopoint` al inicio de tu formulario
- Activa el GPS asistido en el dispositivo si está disponible

## Lógica avanzada de formularios con datos de GPS

KoboToolbox admite lógica avanzada de formularios con datos de GPS en XLSForm. Por ejemplo, puedes usar funciones GPS en cálculos, restricciones y lógica de omisión para medir distancias, perímetros o áreas, o para verificar si una ubicación se encuentra dentro de un límite definido.

![Calcular distancia de ruta](images/collect_gps/calculate.png)

Las funciones GPS más comunes son:

| Función | Descripción |
| :--- | :--- |
| `area(${geoshape})` | Devuelve el área, en metros cuadrados, de un valor `geoshape`. |
| `distance(geo)` | Devuelve la distancia, en metros, de: <ul><li>el perímetro de un valor `geoshape`</li><li>la longitud de un valor `geotrace`</li><li>una lista de geopoints especificados como cadenas de texto o referencias a otros campos (incluyendo los de grupos de repetición), separados por comas</li></ul> |
| `geofence(${geopoint}, ${geoshape})` | Devuelve `TRUE` si el `${geopoint}` especificado está dentro del `${geoshape}` especificado, `FALSE` en caso contrario. Compatible únicamente con KoboCollect. |

<p class="note">
Para obtener más información sobre las funciones para manipular datos de GPS en XLSForm, consulta <a href="https://support.kobotoolbox.org/es/functions_xls.html#functions-to-manipulate-gps-data">Usar funciones en XLSForm</a>.
</p>

## Gestionar datos de GPS

Después de la recolección, los datos de GPS se pueden revisar, mapear y exportar en KoboToolbox.

### Ver datos de GPS en la tabla de datos

Las respuestas GPS aparecen en la tabla de datos como otras respuestas del formulario. Un punto GPS único se almacena como cuatro valores separados por espacios en este formato: `latitud longitud altitud precisión`.

Para preguntas de línea y área, múltiples puntos GPS se almacenan en el mismo formato y se separan por punto y coma.

<p class="note">
Para obtener más información sobre cómo ver tus datos en la tabla de datos, consulta <a href="https://support.kobotoolbox.org/es/viewing_validating_data.html">Ver y validar datos</a>.
</p>

### Mapear datos de GPS en KoboToolbox

KoboToolbox ofrece una vista de **Mapa** integrada para visualizar puntos GPS individuales. Esto facilita revisar dónde se recolectaron los envíos, explorar patrones espaciales y comprender mejor la distribución geográfica de tus datos.

<p class="note">
Para obtener más información sobre la vista de <strong>Mapa</strong> en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/mapping_gps.html">Mapear datos GPS</a>.
</p>

### Exportar datos de GPS

También puedes exportar datos de GPS desde KoboToolbox para usarlos en software externo. Los formatos de exportación disponibles admiten diferentes flujos de trabajo, desde la revisión y limpieza de datos hasta el mapeo y el análisis geoespacial:

- Las **exportaciones CSV y XLS** son útiles para trabajar con datos de GPS en software de hojas de cálculo y también se pueden importar en muchas herramientas GIS, aunque a menudo requieren configuración adicional, como definir los campos de coordenadas o un sistema de referencia de coordenadas.
- Para flujos de trabajo GIS, **GeoJSON** es generalmente el formato recomendado porque es ampliamente compatible con herramientas como ArcGIS y QGIS.
- **KML** está pensado principalmente para la visualización en aplicaciones como Google Earth y admite estilos básicos de mapa, pero es más limitado y se recomienda usarlo solo cuando sea necesario para un flujo de trabajo específico.

<p class="note">
Para obtener más información sobre cómo exportar tus datos de GPS para análisis externo, consulta <a href="https://support.kobotoolbox.org/es/mapping_gps.html#exporting-gps-data">Exportar datos GPS</a>.
</p>

## Resolución de problemas

<details>
<summary><strong>No se está capturando la ubicación GPS</strong></summary>
Verifica que los servicios de ubicación y el GPS estén activados en el dispositivo y que el dispositivo tenga un sensor GPS. También puedes probar el GPS con otra aplicación para confirmar que el dispositivo puede determinar una ubicación. Para obtener mejores resultados, sal al exterior, espera a que la señal sea más fuerte, aléjate de edificios, árboles y otras obstrucciones, y dale tiempo adicional al dispositivo para obtener su primera señal GPS.
</details>

<br>

<details>
<summary><strong>La ubicación GPS es incorrecta</strong></summary>
Si la ubicación registrada parece incorrecta, es posible que el dispositivo esté usando la ubicación basada en red en lugar del GPS por satélite. En algunos casos, desactivar la ubicación por red en la configuración del dispositivo puede ayudar a forzar a KoboCollect a esperar la ubicación GPS real.
</details>

<br>

<details>
<summary><strong>La precisión del GPS no alcanza el umbral objetivo</strong></summary>
Si un punto nunca alcanza la precisión deseada, es posible que el umbral de <code>capture-accuracy</code> sea demasiado estricto para el dispositivo o las condiciones de campo.
</details>

<br>