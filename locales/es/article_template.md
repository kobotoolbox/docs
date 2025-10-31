# Título del artículo
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/2afa3a0c670fe98b296a79b798f33abf248d0273/source/article_template.md" class="reference">6 Sep 2025</a>

Aquí va tu introducción. Ten en cuenta que el código "Última actualización" que aparece arriba se actualizará automáticamente con el nombre del artículo y la fecha correctos cuando publiques, por lo que no es necesario realizar ningún cambio manual. Recuerda nombrar este archivo de acuerdo con el título del artículo y terminar el nombre del archivo con `.md`.

Este artículo incluye:

-   [Formato de texto en markdown](#this-is-a-header)
-   [Agregar archivos multimedia](#adding-media-files)
-   [Agregar tablas](#adding-tables)
-   [Formato HTML](#html-formatting)
-   [Crear una sección de solución de problemas](#troubleshooting)
-   [Lista de íconos](#list-of-icons)

Para obtener ayuda con el formato markdown o HTML, consulta [esta guía](https://www.markdownguide.org/basic-syntax/).

Después de crear un nuevo artículo, no olvides agregarlo al archivo [index.rst](https://github.com/kobotoolbox/docs/blob/master/source/index.rst).

<br/> 


## Este es un encabezado

- Esta es una lista desordenada
- en markdown

1. Esta es una lista numerada.
2. en markdown.
    - Con una sub viñeta.

Este es un **texto en negrita** en markdown.

Este es un *texto en cursiva* en markdown.

Este es un `código monoespaciado` en markdown.

> Esta es una cita en bloque (actualmente no se usa en la documentación)

Insertar enlaces: Para transferir la propiedad de tu Equipo a otro/a usuario/a, [por favor contacta a nuestro equipo de soporte](support@kobotoolbox.org).

Obtén más información sobre [nuestros servicios de capacitación](https://www.kobotoolbox.org/services/training/).

**Enlaces a otros artículos:** Para obtener más información, consulta [permisos a nivel de fila](row_level_permissions.md)

Enlace a [otra sección](#adding-media-files) dentro del artículo. Nota: solo un # para todos los tamaños de encabezado, sin espacio entre # y el nombre del ancla, los nombres de las etiquetas de ancla deben estar en minúsculas y delimitados por guiones si son de varias palabras.

Para convertir rápidamente una URL o dirección de correo electrónico en un enlace, enciérrala entre corchetes angulares.

<https://www.markdownguide.org>
<fake@example.com>

Agrega una línea para separar el contenido:

---

Agrega una línea en blanco...

...para comenzar un nuevo párrafo o salto de línea.

Para agregar un salto de línea completo, usa:

<br/> 



## Agregar archivos multimedia

### Agregar imágenes

![image](/images/getting_started_organization_feature/organizations_project_views.gif)

Almacena las imágenes en la [carpeta de imágenes](https://github.com/kobotoolbox/docs/tree/master/source/images), en una carpeta nombrada según el artículo de soporte. Incluye el nombre de la carpeta y el nombre del archivo de imagen en la ruta del archivo anterior.

### Agregar íconos
Haz clic en el ícono <i class="k-icon k-icon-more"></i> **Más acciones** para el/la usuario/a que deseas eliminar.

Haz clic en <i class="k-icon k-icon-replace"></i> **Reemplazar formulario**.

Para obtener una lista completa de todos los íconos, consulta [aquí](https://support.kobotoolbox.org/es/article_template.html#list-of-icons) y también [aquí](https://support.kobotoolbox.org/_static/kpi-icons/k-icons.html).

### Agregar un video de YouTube

Recomendamos publicar videos en YouTube e insertar un enlace usando iframes. 

<iframe src="https://www.youtube.com/embed/oKtMmBAlHho?si=OqS7-rewYMf-Rrw2" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Incluye el enlace del video de YouTube dentro del iframe.

También puedes incluir videos de la siguiente manera:

<video controls>
  <source
    src="./_static/files/getting_started_xlsform/getting_started_xlsform_v2.mp4"
    type="video/mp4"
  />
</video>


<br/> 

## Agregar tablas

### Tabla normal 

| **Nombre de columna**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| hint               | Sugerencia de pregunta                                  |
| guidance_hint      | Sugerencia de orientación                                  |
| required           | Opción para hacer una pregunta obligatoria            |
| relevant           | Condiciones de lógica de salto para la pregunta         |
| constraint         | Criterios de validación para la pregunta           |
| constraint_message | Mensaje de error cuando no se cumplen los criterios de validación |
| appearance         | Opciones de cómo se muestran las preguntas        |
| choice_filter      | Criterios para selección en cascada                  |
| parameters         | Configuraciones para tipos de preguntas específicas           |
| calculation        | Expresión matemática para pregunta de cálculo |
| default            | Respuesta predeterminada para una pregunta                |

### Tabla XLSForm

| type | name     | label              |
| :--- | :------- | :----------------- |
| text | yourname | ¿Cuál es tu nombre? |
| survey |

Ten en cuenta el `| survey |` en la parte inferior de la tabla.


### Fijar ancho de tabla

Si una de las columnas no es lo suficientemente grande, agrega espacios `&emsp;` para hacerla más ancha, como se muestra a continuación:

| **Configuración de exportación** | **Descripción**                                |
| :-------------------- | :------------------------------------ |
| Guardar selección como… &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;| Marca esta opción e ingresa un nombre para tu configuración de exportación. Cuando hagas clic en <strong>EXPORTAR</strong>, esta configuración se guardará y el nombre aparecerá en el cuadro <strong>Aplicar configuración de exportación guardada</strong>. | 


<br/> 

## Formato HTML

Dentro de cuadros de notas y tablas, **usa HTML** para dar formato a tu texto. Por ejemplo:

<p class="note">
  <b>Nota importante</b>: No es posible compartir proyectos y datos entre los dos servidores. Esto significa que todos/as los/as usuarios/as que trabajen en un proyecto compartido deben usar el mismo servidor para acceder al proyecto. <a href="https://www.kobotoolbox.org/about-us">Agrega un enlace en HTML de esta manera.</a></li>
</p>

<p class="note">
  <b>Nota:</b> Para obtener más información sobre los permisos a nivel de fila, consulta <a class="reference" href="row_level_permissions.html">acceso a nivel de fila</a>.
</p>

<p class="note">
  <b>Nota:</b> Para obtener más información sobre los tipos de preguntas en XLSForm, consulta <a class="reference external" href="https://xlsform.org/en/#question-types">Tipos de preguntas (XLSForm.org)</a>.
</p>

| Servidor                            | URL                                                                           |
| :-------------------------------- | :---------------------------------------------------------------------------- |
| Servidor Global         | <a href="https://kf.kobotoolbox.org" class="reference">kf.kobotoolbox.org</a> |
| Servidor con sede en la Unión Europea | <a href="https://eu.kobotoolbox.org" class="reference">eu.kobotoolbox.org</a> |


<p class='note'>Puedes descargar archivos <a download class='reference'
href='./_static/files/media/xlsform-example.xls'>aquí</a> y los archivos multimedia <a
download class='reference'
href='./_static/files/media/xlsform-example-media.zip'>aquí</a>. Los archivos están almacenados en ./_static/files/media/.</p>

Saltos de línea en HTML:
<p>Esta es la primera línea.<br>
Y esta es la segunda línea.</p>

Haz que tu texto esté en <strong>negrita</strong>, <em>cursiva</em>, o <code>código monoespaciado</code>.

Agrega una lista numerada:
<ol>
  <li>Primer elemento.</li>
  <li>Segundo elemento.</li>
  <li>Tercer elemento.</li>
  <li>Cuarto elemento.</li>
</ol>

Agrega una lista sin numerar:
<ul>
  <li>Primer elemento</li>
  <li>Segundo elemento</li>
  <li>Tercer elemento</li>
  <li>Cuarto elemento</li>
</ul>

<br/> 

## Solución de problemas

<details>
<summary><strong>Enketo vs KoboCollect</strong></summary>
<br>
    Usa este formato para configurar <strong>secciones de solución de problemas</strong> en tus artículos de soporte. Incluye un título corto que describa claramente el problema y propone soluciones aquí.
    <br><br>
    Para separar líneas dentro de un elemento de solución de problemas, agrega un doble salto de línea.
</details>

<details>
<summary><strong>Enketo vs KoboCollect</strong></summary>
<br>
Usa este formato para configurar <strong>secciones de solución de problemas</strong> en tus artículos de soporte. Incluye un título corto que describa claramente el problema y propone soluciones aquí.
</details>

<br/> 

## Lista de íconos

<details>
<summary><strong>Flechas</strong></summary>
<br>

k-icon-angle-bar-left	<i class="k-icon k-icon-angle-bar-left"></i>

k-icon-angle-bar-right	<i class="k-icon k-icon-angle-bar-right"></i>

k-icon-angle-down	<i class="k-icon k-icon-angle-down"></i>

k-icon-angle-left	<i class="k-icon k-icon-angle-left"></i>

k-icon-angle-right	<i class="k-icon k-icon-angle-right"></i>

k-icon-angle-up	<i class="k-icon k-icon-angle-up"></i>

k-icon-arrow-down-left	<i class="k-icon k-icon-arrow-down-left"></i>

k-icon-arrow-down-right	<i class="k-icon k-icon-arrow-down-right"></i>

k-icon-arrow-down	<i class="k-icon k-icon-arrow-down"></i>

k-icon-arrow-left	<i class="k-icon k-icon-arrow-left"></i>

k-icon-arrow-right	<i class="k-icon k-icon-arrow-right"></i>

k-icon-arrow-up-left	<i class="k-icon k-icon-arrow-up-left"></i>

k-icon-arrow-up-right	<i class="k-icon k-icon-arrow-up-right"></i>

k-icon-arrow-up	<i class="k-icon k-icon-arrow-up"></i>

k-icon-caret-down	<i class="k-icon k-icon-caret-down"></i>

k-icon-caret-left	<i class="k-icon k-icon-caret-left"></i>

k-icon-caret-right	<i class="k-icon k-icon-caret-right"></i>

k-icon-caret-up	<i class="k-icon k-icon-caret-up"></i>

    
</details>

<details>
<summary><strong>Editor de formularios</strong></summary>
<br>

k-icon-kobo 	<i class="k-icon k-icon-kobo"></i>

k-icon-cascading 	<i class="k-icon k-icon-cascading"></i>

k-icon-drag-handle 	<i class="k-icon k-icon-drag-handle"></i>

k-icon-duplicate 	<i class="k-icon k-icon-duplicate"></i>

k-icon-edit 	<i class="k-icon k-icon-edit"></i>

k-icon-expand-list 	<i class="k-icon k-icon-expand-list"></i>

k-icon-expand 	<i class="k-icon k-icon-expand"></i>

k-icon-file-audio 	<i class="k-icon k-icon-file-audio"></i>

k-icon-file-image 	<i class="k-icon k-icon-file-image"></i>

k-icon-file-video 	<i class="k-icon k-icon-file-video"></i>

k-icon-file-xls 	<i class="k-icon k-icon-file-xls"></i>

k-icon-file-xml 	<i class="k-icon k-icon-file-xml"></i>

k-icon-file	<i class="k-icon k-icon-file"></i>

k-icon-group-split 	<i class="k-icon k-icon-group-split"></i>

k-icon-group 	<i class="k-icon k-icon-group"></i>

k-icon-media-files	<i class="k-icon k-icon-media-files"></i>

k-icon-question 	<i class="k-icon k-icon-question"></i>

k-icon-settings 	<i class="k-icon k-icon-settings"></i>

k-icon-skip-logic 	<i class="k-icon k-icon-skip-logic"></i>

k-icon-view-all 	<i class="k-icon k-icon-view-all"></i>

k-icon-view 	<i class="k-icon k-icon-view"></i>
   
</details>

<details>
<summary><strong>Tipos de preguntas</strong></summary>
<br>

k-icon-qt-acknowledge-lock 	<i class="k-icon k-icon-qt-acknowledge-lock"></i>

k-icon-qt-acknowledge 	<i class="k-icon k-icon-qt-acknowledge"></i>

k-icon-qt-area-lock 	<i class="k-icon k-icon-qt-area-lock"></i>

k-icon-qt-area 	<i class="k-icon k-icon-qt-area"></i>

k-icon-qt-audio-lock 	<i class="k-icon k-icon-qt-audio-lock"></i>

k-icon-qt-audio 	<i class="k-icon k-icon-qt-audio"></i>

k-icon-qt-background-audio 	<i class="k-icon k-icon-qt-background-audio"></i>

k-icon-qt-barcode-lock 	<i class="k-icon k-icon-qt-barcode-lock"></i>

k-icon-qt-barcode 	<i class="k-icon k-icon-qt-barcode"></i>

k-icon-qt-calculate-lock 	<i class="k-icon k-icon-qt-calculate-lock"></i>

k-icon-qt-calculate 	<i class="k-icon k-icon-qt-calculate"></i>

k-icon-qt-date-lock 	<i class="k-icon k-icon-qt-date-lock"></i>

k-icon-qt-date-time-lock 	<i class="k-icon k-icon-qt-date-time-lock"></i>

k-icon-qt-date-time 	<i class="k-icon k-icon-qt-date-time"></i>

k-icon-qt-date 	<i class="k-icon k-icon-qt-date"></i>

k-icon-qt-decimal-lock 	<i class="k-icon k-icon-qt-decimal-lock"></i>

k-icon-qt-decimal k-icon-qt-external-xml-lock 	<i class="k-icon k-icon-qt-decimal k-icon-qt-external-xml-lock"></i>

k-icon-qt-external-xml 	<i class="k-icon k-icon-qt-external-xml"></i>

k-icon-qt-file-lock 	<i class="k-icon k-icon-qt-file-lock"></i>

k-icon-qt-file 	<i class="k-icon k-icon-qt-file"></i>

k-icon-qt-hidden-lock 	<i class="k-icon k-icon-qt-hidden-lock"></i>

k-icon-qt-hidden 	<i class="k-icon k-icon-qt-hidden"></i>

k-icon-qt-line-lock 	<i class="k-icon k-icon-qt-line-lock"></i>

k-icon-qt-line 	<i class="k-icon k-icon-qt-line"></i>

k-icon-qt-meta-default 	<i class="k-icon k-icon-qt-meta-default"></i>

k-icon-qt-note-lock 	<i class="k-icon k-icon-qt-note-lock"></i>

k-icon-qt-note 	<i class="k-icon k-icon-qt-note"></i>

k-icon-qt-number-lock 	<i class="k-icon k-icon-qt-number-lock"></i>

k-icon-qt-number 	<i class="k-icon k-icon-qt-number"></i>

k-icon-qt-photo-lock 	<i class="k-icon k-icon-qt-photo-lock"></i>

k-icon-qt-photo 	<i class="k-icon k-icon-qt-photo"></i>

k-icon-qt-point-lock 	<i class="k-icon k-icon-qt-point-lock"></i>

k-icon-qt-point 	<i class="k-icon k-icon-qt-point"></i>

k-icon-qt-question-matrix-lock 	<i class="k-icon k-icon-qt-question-matrix-lock"></i>

k-icon-qt-question-matrix 	<i class="k-icon k-icon-qt-question-matrix"></i>

k-icon-qt-range-lock 	<i class="k-icon k-icon-qt-range-lock"></i>

k-icon-qt-range 	<i class="k-icon k-icon-qt-range"></i>

k-icon-qt-ranking-lock 	<i class="k-icon k-icon-qt-ranking-lock"></i>

k-icon-qt-ranking 	<i class="k-icon k-icon-qt-ranking"></i>

k-icon-qt-rating-lock 	<i class="k-icon k-icon-qt-rating-lock"></i>

k-icon-qt-rating 	<i class="k-icon k-icon-qt-rating"></i>

k-icon-qt-select-many-from-file-lock 	<i class="k-icon k-icon-qt-select-many-from-file-lock"></i>

k-icon-qt-select-many-from-file 	<i class="k-icon k-icon-qt-select-many-from-file"></i>

k-icon-qt-select-many-lock 	<i class="k-icon k-icon-qt-select-many-lock"></i>

k-icon-qt-select-many 	<i class="k-icon k-icon-qt-select-many"></i>

k-icon-qt-select-one-from-file-lock 	<i class="k-icon k-icon-qt-select-one-from-file-lock"></i>

k-icon-qt-select-one-from-file 	<i class="k-icon k-icon-qt-select-one-from-file"></i>

k-icon-qt-select-one-lock 	<i class="k-icon k-icon-qt-select-one-lock"></i>

k-icon-qt-select-one 	<i class="k-icon k-icon-qt-select-one"></i>

k-icon-qt-text-lock 	<i class="k-icon k-icon-qt-text-lock"></i>

k-icon-qt-text 	<i class="k-icon k-icon-qt-text"></i>

k-icon-qt-time-lock 	<i class="k-icon k-icon-qt-time-lock"></i>

k-icon-qt-time 	<i class="k-icon k-icon-qt-time"></i>

k-icon-qt-video-lock 	<i class="k-icon k-icon-qt-video-lock"></i>

k-icon-qt-video	<i class="k-icon k-icon-qt-video"></i>

   
</details>

<details>
<summary><strong>Manejo de proyectos</strong></summary>
<br>
    
k-icon-archived 	<i class="k-icon k-icon-archived"></i>

k-icon-data-sync 	<i class="k-icon k-icon-data-sync"></i>

k-icon-deploy	<i class="k-icon k-icon-deploy"></i>

k-icon-document 	<i class="k-icon k-icon-document"></i>

k-icon-download 	<i class="k-icon k-icon-download"></i>

k-icon-drafts	<i class="k-icon k-icon-drafts"></i>

k-icon-language-alt 	<i class="k-icon k-icon-language-alt"></i>

k-icon-language-default 	<i class="k-icon k-icon-language-default"></i>

k-icon-language-settings 	<i class="k-icon k-icon-language-settings"></i>

k-icon-language 	<i class="k-icon k-icon-language"></i>

k-icon-logout 	<i class="k-icon k-icon-logout"></i>

k-icon-menu 	<i class="k-icon k-icon-menu"></i>

k-icon-project-archived 	<i class="k-icon k-icon-project-archived"></i>

k-icon-project-deployed 	<i class="k-icon k-icon-project-deployed"></i>

k-icon-project-draft 	<i class="k-icon k-icon-project-draft"></i>

k-icon-project-locked 	<i class="k-icon k-icon-project-locked"></i>

k-icon-project-overview 	<i class="k-icon k-icon-project-overview"></i>

k-icon-project 	<i class="k-icon k-icon-project"></i>

k-icon-projects 	<i class="k-icon k-icon-projects"></i>

k-icon-replace 	<i class="k-icon k-icon-replace"></i>

k-icon-upload 	<i class="k-icon k-icon-upload"></i>

k-icon-user-share 	<i class="k-icon k-icon-user-share"></i>

k-icon-user 	<i class="k-icon k-icon-user"></i>

k-icon-users	<i class="k-icon k-icon-users"></i>

   
</details>

<details>
<summary><strong>Datos</strong></summary>
<br>
    
k-icon-filter-arrows 	<i class="k-icon k-icon-filter-arrows"></i>

k-icon-filter 	<i class="k-icon k-icon-filter"></i>

k-icon-map-view 	<i class="k-icon k-icon-map-view"></i>

k-icon-gallery 	<i class="k-icon k-icon-gallery"></i>

k-icon-globe-alt	<i class="k-icon k-icon-globe-alt"></i>

k-icon-layer 	<i class="k-icon k-icon-layer"></i>

k-icon-hide 	<i class="k-icon k-icon-hide"></i>

k-icon-reports 	<i class="k-icon k-icon-reports"></i>

k-icon-sort-ascending 	<i class="k-icon k-icon-sort-ascending"></i>

k-icon-sort-default 	<i class="k-icon k-icon-sort-default"></i>

k-icon-sort-descending 	<i class="k-icon k-icon-sort-descending"></i>

k-icon-table 	<i class="k-icon k-icon-table"></i>

k-icon-unfreeze 	<i class="k-icon k-icon-unfreeze"></i>


 </details>

<details>
<summary><strong>Carpetas y biblioteca</strong></summary>
<br>

k-icon-folder-in 	<i class="k-icon k-icon-folder-in"></i>

k-icon-folder-out 	<i class="k-icon k-icon-folder-out"></i>

k-icon-folder-plus 	<i class="k-icon k-icon-folder-plus"></i>

k-icon-folder-public 	<i class="k-icon k-icon-folder-public"></i>

k-icon-folder-shared 	<i class="k-icon k-icon-folder-shared"></i>

k-icon-folder-subscribed 	<i class="k-icon k-icon-folder-subscribed"></i>

k-icon-folder 	<i class="k-icon k-icon-folder"></i>

k-icon-freeze 	<i class="k-icon k-icon-freeze"></i>

k-icon-block 	<i class="k-icon k-icon-block"></i>

k-icon-library-public 	<i class="k-icon k-icon-library-public"></i>

k-icon-library 	<i class="k-icon k-icon-library"></i>

k-icon-template-locked 	<i class="k-icon k-icon-template-locked"></i>

k-icon-template 	<i class="k-icon k-icon-template"></i>

 
</details>

<details>
<summary><strong>Símbolos</strong></summary>
<br>

k-icon-alert 	<i class="k-icon k-icon-alert"></i>

k-icon-check-circle 	<i class="k-icon k-icon-check-circle"></i>

k-icon-check 	<i class="k-icon k-icon-check"></i>

k-icon-close 	<i class="k-icon k-icon-close"></i>

k-icon-expand-arrow 	<i class="k-icon k-icon-expand-arrow"></i>

k-icon-flows 	<i class="k-icon k-icon-flows"></i>

k-icon-help-articles 	<i class="k-icon k-icon-help-articles"></i>

k-icon-help 	<i class="k-icon k-icon-help"></i>

k-icon-information 	<i class="k-icon k-icon-information"></i>

k-icon-link 	<i class="k-icon k-icon-link"></i>

k-icon-lock-alt 	<i class="k-icon k-icon-lock-alt"></i>

k-icon-lock 	<i class="k-icon k-icon-lock"></i>

k-icon-minus 	<i class="k-icon k-icon-minus"></i>

k-icon-more-vertical 	<i class="k-icon k-icon-more-vertical"></i>

k-icon-more 	<i class="k-icon k-icon-more"></i>

k-icon-notification 	<i class="k-icon k-icon-notification"></i>

k-icon-pause 	<i class="k-icon k-icon-pause"></i>

k-icon-play 	<i class="k-icon k-icon-play"></i>

k-icon-plus	<i class="k-icon k-icon-plus"></i>

k-icon-search 	<i class="k-icon k-icon-search"></i>

k-icon-spinner 	<i class="k-icon k-icon-spinner"></i>

k-icon-stop 	<i class="k-icon k-icon-stop"></i>

k-icon-trash 	<i class="k-icon k-icon-trash"></i>

k-icon-warning 	<i class="k-icon k-icon-warning"></i>

</details>

<details>
<summary><strong>Soporte y redes sociales</strong></summary>
<br>

k-icon-email 	<i class="k-icon k-icon-email"></i>

k-icon-help-academy 	<i class="k-icon k-icon-help-academy"></i>

k-icon-help-forum 	<i class="k-icon k-icon-help-forum"></i>

k-icon-logo-github 	<i class="k-icon k-icon-logo-github"></i>

k-icon-logo-instagram 	<i class="k-icon k-icon-logo-instagram"></i>

k-icon-logo-linkedin 	<i class="k-icon k-icon-logo-linkedin"></i>

k-icon-logo-twitter 	<i class="k-icon k-icon-logo-twitter"></i>

k-icon-mail 	<i class="k-icon k-icon-mail"></i>

k-icon-intercom 	<i class="k-icon k-icon-intercom"></i>

k-icon-subscribe 	<i class="k-icon k-icon-subscribe"></i>

k-icon-unsubscribe 	<i class="k-icon k-icon-unsubscribe"></i>

</details>

<details>
<summary><strong>Otros</strong></summary>
<br>

k-icon-attach 	<i class="k-icon k-icon-attach"></i>

k-icon-editor 	<i class="k-icon k-icon-editor"></i>

k-icon-heatmap 	<i class="k-icon k-icon-heatmap"></i>

k-icon-pdf 	<i class="k-icon k-icon-pdf"></i>

k-icon-pins 	<i class="k-icon k-icon-pins"></i>

k-icon-print 	<i class="k-icon k-icon-print"></i>

k-icon-spreadsheet 	<i class="k-icon k-icon-spreadsheet"></i>

</details>