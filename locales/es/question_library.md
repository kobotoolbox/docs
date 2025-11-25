# Uso de La biblioteca de preguntas
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/385b471fb227f28575b67a450696cc8e4f4a3779/source/question_library.md" class="reference">2 Jul 2025</a>

## Agregar preguntas a tu biblioteca

Las preguntas que previamente se han agregado a tu biblioteca pueden añadirse a cualquier otro formulario arrastrándolas y soltándolas desde la barra lateral de La biblioteca de preguntas dentro del editor de formularios de KoboToolbox (Formbuilder).

Para acceder a la barra lateral de La biblioteca de preguntas, haz clic en el botón **Add from Library** en la esquina superior derecha de la barra de herramientas del editor de formularios.

![image](/images/question_library/library.jpg)

Si es necesario, puedes buscar la pregunta que estás buscando utilizando la función de búsqueda para buscar por palabra clave o etiqueta.

Para agregar la pregunta a tu formulario, **arrástrala y suéltala** en la posición deseada. Una pregunta puede agregarse varias veces si es necesario, por ejemplo, cuando reutilizas una escala específica para diferentes preguntas.

## Manejo de preguntas en tu biblioteca

La biblioteca de preguntas te permite guardar y reutilizar preguntas de uso frecuente.

Para manejar La biblioteca de preguntas, haz clic en el botón del menú de biblioteca en la barra lateral superior izquierda. Por defecto, la biblioteca mostrará todas tus preguntas. Puedes **visualizar** o editar cada pregunta individual haciendo clic en la etiqueta de la colección.

Para **clonar** o **descargar** la colección, coloca el cursor del ratón sobre la etiqueta de la colección y los íconos aparecerán en el lado derecho.

También puedes **agregar nuevas preguntas** desde dentro de la biblioteca. Solo haz clic en **New** y podrás crear una nueva pregunta que se guarda en la biblioteca.

Para **eliminar preguntas** en tu biblioteca, simplemente haz clic en **Delete** después de hacer clic en el ícono **More Actions**.

![image](/images/question_library/delete.jpg)

## Importar colecciones

Además de crear colecciones en la interfaz, también puedes importar grandes conjuntos de preguntas y bloques desde Excel, basados en el formato estándar XLSForm. Los/as usuarios/as avanzados/as encontrarán más práctico comenzar desde XLSForms existentes que copiar el contenido de preguntas existentes en la herramienta uno por uno.

![image](/images/question_library/import_collection.png)

Por defecto, cada archivo XLS se importará como una nueva colección. Si tu archivo solo contiene una pregunta o un bloque, importará solo esa pregunta o ese bloque en lugar de crear una colección. El nombre de la colección se toma del nombre del archivo (se permiten duplicados de colecciones existentes). Pero es fácil renombrar la colección después de importarla: solo haz clic en el nombre de la colección en la barra lateral izquierda, luego haz clic en el ícono de configuración.

Usa <a download class="reference" href="./_static/files/question_library/collection_import_sample.xlsx">este archivo de Excel como plantilla</a>.
El archivo generalmente sigue el formato XLSForm. Hay algunas diferencias:

* La hoja principal que contiene las preguntas debe llamarse **library** cuando se carguen múltiples bloques.
* (Opcional) Los bloques de preguntas deben definirse en la columna adicional llamada **block**, escribiendo el mismo título de bloque en cada fila de la tabla que debe incluirse en el bloque. La etiqueta del bloque no tiene limitaciones en términos de caracteres, pero debe tener exactamente la misma ortografía para evitar romper el bloque ('Household questions' es diferente de 'household questions'). Usa un título de bloque que facilite identificar el contenido más adelante.
* Cualquier fila en la hoja de plantilla que no tenga un valor en la columna de bloque se importará como una pregunta separada.
* (Opcional) Define cualquier etiqueta para la pregunta o bloque agregando una columna **tag:[nombre de tu etiqueta]** para cada etiqueta, luego escribiendo '1' en cada fila que deba usar la etiqueta. En el caso de bloques, es suficiente escribir '1' en cualquiera de las filas del bloque sin importar cuál. Es suficiente marcar una de las preguntas en el bloque, aunque no importa si varias preguntas están etiquetadas.

Algunas otras sugerencias:

* Puedes incluir grupos en bloques. Solo asegúrate de que la línea 'begin group' tenga un ID de 'name' único (como en todos los XLSForms) y que la apertura (begin group) y el cierre (end group) estén incluidos en el bloque. Agregar el nombre del bloque como etiqueta del grupo podría ser una buena idea para que veas la etiqueta del bloque después de importarlo al editor de formularios.
* Puedes incluir lógica de salto y reglas de validación dentro de bloques que importes. Eso es muy útil cuando importas bloques completos de preguntas en nuevos borradores de formularios sin tener que reconstruir estas configuraciones avanzadas.
* Puedes agregar múltiples idiomas a las etiquetas de preguntas y respuestas con la sintaxis habitual de XLSForm (label::English (en), label::Español (es), etc.)