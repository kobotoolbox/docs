# Preguntas GPS en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/gps_questions.md" class="reference">23 Apr 2026</a>

Las preguntas GPS se utilizan para **recolectar coordenadas geográficas y datos espaciales** durante la recolección de datos. Te permiten capturar ubicaciones precisas, trazar rutas o definir áreas directamente en tu formulario. Estos tipos de preguntas son útiles para actividades como el mapeo de infraestructura, el seguimiento de visitas de campo, el monitoreo de sitios ambientales o el registro de ubicaciones de servicios.

Este artículo explica los tipos de preguntas GPS disponibles en el Formbuilder, cómo agregarlos y configurarlos, las diferencias de comportamiento entre los formularios web y KoboCollect, y las opciones de aspecto avanzadas disponibles para la recolección de datos de ubicación.

<p class="note">
<strong>Nota:</strong> El registro de coordenadas GPS no requiere conexión a internet y es compatible con la recolección de datos sin conexión.
</p>

## Tipos de preguntas GPS

Los siguientes tipos de preguntas están disponibles en el Formbuilder para que los encuestados registren datos GPS:

| Tipo de pregunta | Descripción |
|:---|:---|
| <i class="k-icon-qt-point"></i> Punto | Recolecta una única ubicación geográfica, como las coordenadas de una escuela, clínica o vivienda específica. |
| <i class="k-icon-qt-line"></i> Línea | Registra múltiples puntos GPS que forman una línea, por ejemplo para rastrear un camino, trazar una ruta o mapear un drenaje. |
| <i class="k-icon-qt-area"></i> Área | Recolecta puntos que forman un área cerrada, como una parcela de tierra o un campo. |

<p class="note">
<strong>Nota:</strong> También puedes recolectar la ubicación automáticamente usando <a href="https://support.kobotoolbox.org/es/form_meta.html">preguntas de metadatos</a>. Las opciones <strong>start geopoint early</strong> y <strong>audit</strong> están disponibles en el Formbuilder, mientras que <code>background-geopoint</code> solo está disponible al crear tu formulario <a href="https://support.kobotoolbox.org/es/metadata_xls.html">en XLSForm</a>.
</p>

## Agregar una pregunta GPS en el Formbuilder

Para agregar una pregunta GPS a tu formulario:
1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ AGREGAR PREGUNTA.**
4. Elige el tipo de pregunta adecuado.

![Pregunta GPS](images/gps_questions/gps.png)

## Aspectos de las preguntas GPS

La siguiente tabla muestra los aspectos predeterminados de las preguntas GPS:

![Aspectos predeterminados de las preguntas GPS](images/gps_questions/table.png)

En los **formularios web**, los encuestados pueden seleccionar una ubicación directamente en el mapa, buscar una dirección o ingresar coordenadas GPS manualmente.

En **KoboCollect**, la ubicación actual del dispositivo se registra automáticamente, y la selección manual o el ingreso de coordenadas no están disponibles de forma predeterminada.

<p class="note">
<strong>Nota:</strong> Para obtener más información sobre los comportamientos de recolección de datos GPS en formularios web y KoboCollect, consulta <a href="https://support.kobotoolbox.org/es/collect_gps.html">Recolectar datos de GPS con KoboToolbox</a>.
</p>

### Aspectos avanzados

Puedes aplicar aspectos avanzados a las preguntas GPS para modificar cómo se muestran y se comportan en tu formulario.

Para agregar un aspecto avanzado:
1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En **Aspecto (avanzado)**, escribe el nombre del aspecto en el cuadro de texto, exactamente como se indica a continuación.

![Aspecto avanzado de pregunta GPS](images/gps_questions/appearance.png)

Los siguientes aspectos avanzados están disponibles para las preguntas GPS:

| Aspecto | Descripción | Compatibilidad |
|:---|:---|:---|
| <code>maps</code> | Muestra un mapa para que los usuarios visualicen la ubicación que se está registrando automáticamente (solo **Punto**). | Solo KoboCollect (incluido en el aspecto predeterminado de los formularios web) |
| <code>placement-map</code> | Permite la selección manual de una ubicación en un mapa (solo **Punto**). | Solo KoboCollect (incluido en el aspecto predeterminado de los formularios web) |
| <code>hide-input</code> | Muestra un mapa más grande y oculta los demás campos de entrada (latitud, longitud, altitud, precisión).<br>![Aspecto avanzado hide-input](images/gps_questions/hide-input.png) | Solo formularios web |

<p class="note">
<strong>Nota:</strong> Si usas formularios web y quieres registrar la ubicación GPS automáticamente sin permitir que los encuestados seleccionen o ingresen coordenadas manualmente, considera usar la <a href="https://support.kobotoolbox.org/es/metadata_xls.html">pregunta de metadatos</a> <code>background-geopoint</code>.
</p>