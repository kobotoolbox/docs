# Recolectar datos en diferentes idiomas
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/collecting_data_multiple_languages.md" class="reference">23 Apr 2026</a>

KoboToolbox permite recolectar datos en **tantos idiomas como necesites** dentro de un solo formulario, incluyendo idiomas que usan escrituras no latinas. Puedes diseñar tu formulario con múltiples traducciones, permitir que los encuestados cambien al idioma de su preferencia durante la recolección de datos, y luego ver o exportar los datos en cualquier idioma del formulario.

Agregar traducciones a un solo formulario elimina la necesidad de crear formularios separados para cada idioma, lo que facilita la gestión de proyectos multilingües y **mantiene la consistencia de tus datos en todos los idiomas.** Tanto [KoboCollect](../es/data_collection_kobocollect.html) como los [formularios web](../es/data_through_webforms.html) admiten traducciones de formularios.

Este artículo ofrece una descripción general de las diferentes opciones para preparar formularios con traducciones, cómo recolectar datos en múltiples idiomas (incluyendo la configuración de enlaces específicos por idioma para formularios web), y cómo gestionar y exportar datos multilingües en KoboToolbox.

## Configurar tus formularios con traducciones

Puedes agregar traducciones a tu formulario **directamente en la interfaz de KoboToolbox** o usando **XLSForm.** KoboToolbox ofrece una interfaz intuitiva que no requiere conocimientos técnicos y te permite agregar fácilmente múltiples traducciones a tus formularios. Este enfoque es útil cuando trabajas con un número reducido de preguntas o cuando quieres hacer ajustes rápidos.

<p class="note">
  Para obtener más información sobre cómo configurar traducciones desde la interfaz de KoboToolbox, consulta <a href="../es/language_dashboard.html">Agregar traducciones en KoboToolbox</a>.
</p>

Para formularios multilingües más grandes o complejos, XLSForm suele ser la opción más eficiente. Permite gestionar las traducciones de forma masiva, lo que puede ahorrar tiempo cuando se trabaja con muchas preguntas o varios idiomas.

<p class="note">
  Para obtener más información sobre cómo configurar traducciones en XLSForm, consulta <a href="../es/language_xls.html">Añadir traducciones en XLSForm</a>.
</p>

La mayoría de los elementos que se muestran a los encuestados pueden traducirse. Estos incluyen **etiquetas de preguntas, sugerencias, etiquetas de opciones, mensajes de restricción** y **mensajes obligatorios.** Los elementos que definen la estructura del formulario, como los [nombres de columna de datos](../es/glossary.html#data-column-name) y los [valores XML](../es/glossary.html#xml-value), no pueden traducirse y deben permanecer en el idioma que uses para el desarrollo del formulario y el análisis de datos.

<p class="note">
  <strong>Nota:</strong> XLSForm facilita agregar traducciones de forma masiva mediante traducción automática o herramientas de traducción en línea. Las traducciones automáticas siempre deben ser revisadas por una persona con dominio del idioma para garantizar la precisión, la adecuación cultural y el contexto correcto. Esto ayuda a mantener la calidad y confiabilidad del contenido traducido.
</p>

## Recolectar datos en múltiples idiomas

<iframe src="https://www.youtube.com/embed/MWLlWtXYHig?si=nGuOVpt0tVR_ip7l&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Cuando tu formulario contiene traducciones, los encuestados pueden elegir su idioma preferido durante la recolección de datos y cambiar de idioma en cualquier momento antes de enviar sus respuestas.

Para cambiar el idioma del formulario en formularios web:

1. Abre el formulario en tu navegador.
2. En la esquina superior derecha del formulario, se muestra un menú desplegable **Seleccionar idioma** (solo en formularios con múltiples idiomas).
3. Abre el menú desplegable y elige entre la lista de traducciones disponibles.

Para cambiar el idioma del formulario en KoboCollect:

1. Abre el formulario en tu dispositivo.
2. Toca el botón <i class="k-icon-more-vertical"></i> **Más opciones** en la esquina superior derecha de la pantalla.
3. Selecciona <i class="k-icon-language"></i> **Cambiar idioma.**
4. Elige entre la lista de traducciones disponibles.

### URL del formulario específica por idioma

De forma predeterminada, los enlaces de formularios copiados desde KoboToolbox se abren en el idioma predeterminado del formulario. Para compartir un enlace que se abra en un idioma diferente, agrega el parámetro `lang` al final de la URL del formulario:

1. Copia el enlace de tu formulario en **FORMULARIO > Recolectar datos.**
2. Agrega `?lang=[código_de_idioma]` al final de la URL.
    - Por ejemplo: `https://ee.kobotoolbox.org/x/[form_id]?lang=fr`.
3. Comparte la URL específica del idioma con los encuestados.

<p class="note">
  <strong>Nota:</strong> Esto anula tanto la configuración de idioma del navegador como el idioma predeterminado del formulario. Esta funcionalidad aplica solo a formularios web, no a KoboCollect.
</p>

## Gestionar datos en múltiples idiomas

Después de recolectar datos en múltiples idiomas, KoboToolbox te permite ver y exportar tus datos en cualquier idioma incluido en tu formulario.

<p class="note">
  <strong>Nota:</strong> Si estás recolectando respuestas de audio en múltiples idiomas, puedes transcribir y traducir esas respuestas usando las funciones de transcripción y traducción automática de KoboToolbox. Para obtener más información, consulta <a href="../es/transcription-translation.html">Transcripción y traducción de respuestas de audio</a>.
</p>

### Ver datos en diferentes idiomas en la vista de Tabla

En la vista **DATOS > Tabla**, puedes cambiar el idioma usado para las etiquetas de preguntas y opciones.

Para ver tu tabla de datos en un idioma diferente:

1. En tu proyecto, ve a **DATOS > Tabla.**
2. En la esquina superior derecha, haz clic en <i class="k-icon-settings"></i> **Opciones de visualización.**
3. En **¿Mostrar etiquetas o valores XML?**, selecciona el idioma que deseas usar.

![Opciones de visualización en la vista de tabla](images/collecting_data_multiple_languages/table_view.png)

<p class="note">
  <strong>Nota:</strong> Todos los datos del formulario se muestran en el idioma seleccionado, independientemente del idioma usado durante la recolección de datos, excepto las respuestas de texto abierto.
</p>

### Ver datos en diferentes idiomas en la vista de Informes

En la vista **DATOS > Informes**, también puedes cambiar el idioma del informe.

Para ver tu informe de datos en un idioma diferente:

1. En tu proyecto, ve a **DATOS > Informes.**
2. Haz clic en <i class="k-icon-settings"></i> **Configurar estilo del informe.**
3. Ve a la ventana **TRANSLATION.**
4. Selecciona el idioma que deseas mostrar en el informe.

![Configurar estilo del informe](images/collecting_data_multiple_languages/reports.png)

<p class="note">
  <strong>Nota:</strong> Todos los datos del formulario se muestran en el idioma seleccionado, independientemente del idioma usado durante la recolección de datos, excepto las respuestas de texto abierto.
</p>

### Seleccionar un idioma al exportar datos

En la sección **DATOS > Descargas**, puedes elegir el idioma usado en tu conjunto de datos exportado.

Para exportar tu informe de datos en un idioma diferente:

1. En tu proyecto, ve a **DATOS > Descargas.**
2. Haz clic en el menú desplegable en **Formato de valores y encabezados.**
3. Selecciona el idioma en el que deseas exportar tus datos.
4. Haz clic en **Exportar** y descarga el archivo exportado.

![Seleccionar idioma de exportación](images/collecting_data_multiple_languages/exports.png)

<p class="note">
  <strong>Nota:</strong> Todos los datos del formulario se exportan en el idioma seleccionado, independientemente del idioma usado durante la recolección de datos, excepto las respuestas de texto abierto.
</p>

También puedes ver o exportar tus datos usando [valores XML](../es/glossary.html#xml-value). **Los valores XML no se traducen** y generalmente se generan en el idioma usado durante el desarrollo del formulario.

Se recomienda usar valores XML para el análisis, ya que proporcionan nombres de variables cortos y consistentes, y valores codificados que **se mantienen consistentes en todas las traducciones**, independientemente del idioma usado por los encuestados.