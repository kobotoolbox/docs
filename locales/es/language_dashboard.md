# Agregar traducciones en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/55b3ab6258a25c2b16c1d954b282f02918937598/source/language_dashboard.md" class="reference">5 Jun 2026</a>

<iframe src="https://www.youtube.com/embed/3O2K78F7DCA?si=lt-ZlSRoAjFuSMl1&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Agregar traducciones a un formulario permite a los usuarios **elegir su idioma preferido** durante la recolección de datos sin necesidad de crear formularios separados. Se puede agregar cualquier número de traducciones. Tanto [KoboCollect](../es/data_collection_kobocollect.html) como los [formularios web](../es/data_through_webforms.html) son compatibles con las traducciones de formularios.

Puedes agregar traducciones a tu formulario directamente en la interfaz de KoboToolbox o usando [XLSForm](../es/language_xls.html). KoboToolbox ofrece una **interfaz intuitiva** que no requiere conocimientos técnicos y te permite agregar fácilmente múltiples traducciones a tus formularios. Este enfoque es útil cuando trabajas con un número reducido de preguntas o cuando quieres hacer ajustes rápidos.

<p class="note">
   <strong>Nota:</strong> Para formularios multilingües más grandes o complejos, XLSForm suele ser la opción más eficiente. Permite gestionar las traducciones de forma masiva, lo que puede ahorrar tiempo cuando se trabaja con muchas preguntas o varios idiomas. Para obtener más información sobre cómo configurar traducciones en XLSForm, consulta <a href="../es/language_xls.html">Añadir traducciones en XLSForm</a>.
</p>

Este artículo se centra en agregar traducciones desde la plataforma KoboToolbox y abarca los siguientes temas:
- Configurar el idioma predeterminado del formulario
- Agregar idiomas y traducciones
- Cambiar el idioma predeterminado

<p class="note">
    Para obtener más información sobre la recolección y gestión de datos de formularios traducidos, consulta <a href="../es/collecting_data_multiple_languages.html">Recolectar datos en diferentes idiomas</a>.
</p>

## Configurar el idioma predeterminado

El idioma predeterminado de un formulario suele ser el idioma en el que se diseñó el cuestionario y el idioma en el que se abre el formulario por defecto durante la recolección de datos. Solo es necesario configurar un idioma predeterminado si se agregan traducciones adicionales, y no es obligatorio cuando el formulario está disponible en un único idioma.

Para configurar el idioma predeterminado:

1. Crea tu formulario en el idioma predeterminado.
2. Una vez creado el formulario, ve a la página **FORMULARIO** de tu proyecto.
3. Debajo del botón **IMPLEMENTAR** o **REIMPLEMENTAR**, haz clic en <i class="k-icon-language"></i> **Gestionar**.
4. Agrega el nombre del idioma (por ejemplo, "English") y el código de idioma (por ejemplo, "en") para tu idioma predeterminado.

![Gestionar idiomas](images/language_dashboard/manage_languages.png)

<p class="note">
    <strong>Nota:</strong> Los códigos de idioma se pueden encontrar en el <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">Registro de subetiquetas de idioma de la IANA</a>. En el sitio web de la IANA, <strong>Description</strong> hace referencia al nombre del idioma y <strong>Subtag</strong> al código de idioma (por ejemplo, <strong>Description</strong>: French, <strong>Subtag</strong>: fr).
</p>

## Agregar idiomas y traducciones

Una vez que hayas configurado tu idioma predeterminado, puedes agregar más idiomas y traducir el texto de tu formulario:

1. En la ventana <i class="k-icon-language"></i> **Gestionar idiomas**, haz clic en **Agregar idioma**.
2. Ingresa el nombre y el código del idioma y, a continuación, haz clic en **Agregar**.
3. Junto al idioma que agregaste, haz clic en <i class="k-icon-language-settings"></i> **Actualizar traducciones**.
    - Aparecerá una tabla con todos los elementos traducibles de tu formulario, incluidas las etiquetas de preguntas, etiquetas de grupos, sugerencias, sugerencias adicionales, mensajes de restricción, archivos multimedia y etiquetas de opciones.
    - Cada idioma tiene su propia tabla de traducciones.
4. Ingresa las traducciones y haz clic en **Guardar cambios**.
    - Si omites el texto de un elemento traducido, aparecerá como un campo en blanco en el formulario.
5. Cierra la ventana y previsualiza tu formulario para verificar las traducciones.
6. Implementa o reimplementa tu formulario para aplicar los cambios.

Puedes volver a esta ventana en cualquier momento para actualizar las traducciones existentes o agregar nuevas. Recuerda actualizar las traducciones cada vez que agregues nuevas preguntas u opciones de respuesta.

![Agregar un nuevo idioma](images/language_dashboard/add_language.png)


## Cambiar el idioma predeterminado

Para cambiar el idioma predeterminado del formulario:

1. En la página **FORMULARIO**, haz clic en <i class="k-icon-language"></i> **Gestionar**.
2. Haz clic en <i class="k-icon-language-default"></i> **Establecer como predeterminado** junto al idioma que quieres configurar como predeterminado.

![Cambiar el idioma predeterminado](images/language_dashboard/change_default.png)

## Resolución de problemas

<details>
  <summary><strong>Error loading survey: There is an unnamed translation in your form definition</strong></summary>
  Este error significa que al menos un elemento de tu formulario (por ejemplo, una sugerencia o un mensaje) no está asignado a ningún idioma.
<br><br>
Para solucionar este problema:

<ol>
<li>Descarga tu formulario como <a href="../es/xlsform_with_kobotoolbox.html">XLSForm</a></li>
<li>Busca una columna <code>label</code>, <code>hint</code>, <code>guidance_hint</code>, multimedia, <code>constraint_message</code> o <code>required_message</code> en tu formulario que no esté asignada a ningún idioma (por ejemplo, <code>label</code> en lugar de <code>label::English (en)</code>).</li>
<li>Según el problema, agrega un <a href="../es/language_xls.html">nombre de idioma y código</a> al nombre de la columna sin asignar, o copia su contenido en una columna existente para ese idioma y elimina la columna sin asignar.</li>
</ol>

</details>

<br>

<details>
  <summary><strong>Problema al mostrar textos de derecha a izquierda</strong></summary>
  Al agregar un idioma que utiliza un sistema de escritura de derecha a izquierda (RTL), como el árabe, el hebreo o el urdu, es importante usar el <strong>código de idioma correcto</strong> y asegurarse de que el <strong>primer texto visible en la traducción</strong> (por ejemplo, una etiqueta de pregunta, sugerencia o nota) esté escrito en el idioma RTL. Esto garantizará que el diseño del formulario no adopte por defecto el formato de izquierda a derecha (LTR).
</details>