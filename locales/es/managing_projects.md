# Gestión de proyectos en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/d66c12822969e6fa3db776489f574522bf03eebb/source/managing_projects.md" class="reference">19 Feb 2026</a>

Un **proyecto** en KoboToolbox corresponde a un formulario, su configuración y todos los datos enviados a ese formulario. La gestión de proyectos comienza en la **Página de proyectos**, donde puedes ver, ordenar, filtrar y organizar tus proyectos. También puedes crear nuevos proyectos, actualizar los existentes y gestionar cómo se comparten con colaboradores.

Este artículo explica cómo ver y gestionar proyectos, crear nuevos proyectos, trabajar con la configuración y los datos del proyecto, y archivar o eliminar proyectos que ya no están en uso.

## Descripción general de los proyectos existentes
La **Página de proyectos** muestra todos los proyectos que tienes o que se han compartido contigo. La tabla **Mis proyectos** muestra información clave como el nombre del proyecto, propietario, estado y número de envíos.

Los proyectos existen en tres estados:
* **Implementado:** Proyectos que han sido publicados y están listos para la recolección de datos, lo que permite a los usuarios abrir el formulario y enviar respuestas.
* **Borrador:** Proyectos que aún están siendo desarrollados o editados y que aún no han sido implementados, por lo que no pueden recibir envíos.
* **Archivado:** Proyectos que han sido eliminados de la lista de proyectos activos y que ya no aceptan nuevos envíos, pero que se conservan como referencia o para el mantenimiento de registros.

Puedes gestionar tus proyectos con las herramientas de esta página:
* **Filtrar:** Haz clic en <i class="k-icon-filter"></i> **filtrar** para filtrar proyectos por nombre, descripción, estado, propietario, fecha de última edición, fecha de última modificación, fecha de última implementación, sector, países e idiomas.
* **Seleccionar campos:** Haz clic en <i class="k-icon-spreadsheet"></i> **campos** para elegir qué campos se muestran en la tabla **Mis proyectos**.
* **Ordenar:** Haz clic en el encabezado de una columna para ordenar por ese campo.
* **Otras acciones:** Selecciona la casilla junto a un proyecto para realizar acciones sobre él.
    * En la esquina superior derecha, puedes <i class="k-icon-archived"></i> **archivar** un proyecto o actualizar sus <i class="k-icon-user-share"></i> **permisos de uso compartido**.
    * También puedes <i class="k-icon-trash"></i> **eliminar** varios proyectos a la vez.

![Projects](images/kobotoolbox_interface/projects.png)

## Crear un proyecto
Para crear un nuevo proyecto en KoboToolbox:
1. Haz clic en **NUEVO** desde la **Página de proyectos**.
2. Elige una de las siguientes opciones:
    - <i class="k-icon-edit"></i> **Crear desde un borrador** para crear un formulario usando el [Formbuilder](https://support.kobotoolbox.org/es/formbuilder.html).
    - <i class="k-icon-template"></i> **Usar una plantilla** para seleccionar una plantilla de formulario de la [biblioteca de preguntas](https://support.kobotoolbox.org/es/question_library.html).
    - <i class="k-icon-upload"></i> **Cargar un XLSForm** para cargar un [XLSForm](https://support.kobotoolbox.org/es/getting_started_xlsform.html) existente.
    - <i class="k-icon-link"></i> **Importar un XLSForm a través de URL** para vincular a un XLSForm [almacenado en línea](https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#importing-an-xlsform-via-url).
3. Crea, prueba y previsualiza tu formulario.
4. Haz clic en **IMPLEMENTAR** desde la página **FORMULARIO** de tu proyecto para publicar el formulario para la recolección de datos.

![Create](images/managing_projects/create.png)

## Gestionar un proyecto existente
Cuando abres un proyecto, puedes gestionarlo a través de las ventanas en la parte superior de la página:
* **RESUMEN:** Descripción general de los metadatos del proyecto y los envíos.
* **FORMULARIO:** Edita el formulario, implementa cambios y copia el enlace del formulario.
* **DATOS:** Visualiza los datos enviados en diferentes formatos, genera informes y exporta datos.
* **CONFIGURACIÓN:** Actualiza la configuración del proyecto, incluyendo los [permisos para compartir](https://support.kobotoolbox.org/es/managing_permissions.html), los [archivos multimedia del formulario](https://support.kobotoolbox.org/es/upload_media.html) y la configuración general.

<p class="note">
  Para obtener más información sobre la gestión de tus datos en KoboToolbox, consulta <a href="https://support.kobotoolbox.org/es/viewing_validating_data.html">Ver y validar datos</a> y <a href="https://support.kobotoolbox.org/es/editing_deleting_data.html">Modificar y eliminar datos</a>.
</p>


## Archivar y eliminar proyectos
A medida que los proyectos quedan desactualizados o ya no son necesarios, puedes retirarlos del uso activo **archivándolos** o **eliminándolos**. Archivar detiene los nuevos envíos mientras mantiene el formulario y los datos existentes disponibles. Eliminar borra permanentemente el proyecto y todos sus datos de tu cuenta.

<p class="note">
  <strong>Nota:</strong> Dado que los proyectos eliminados no se pueden recuperar, elimina un proyecto solo cuando estés seguro de que ni el formulario ni sus datos serán necesarios. Antes de eliminar un proyecto, te recomendamos <a href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox">descargar el formulario</a> como XLSForm y <a href="https://support.kobotoolbox.org/es/export_download.html">exportar</a> todos los datos del proyecto.
</p>

### Archivar proyectos
Se recomienda archivar los formularios que ya no deben aceptar envíos pero que deben permanecer disponibles como referencia.

Hay dos formas de archivar un proyecto. Para archivar un proyecto desde la **Página de proyectos**:
1. En la **Página de proyectos**, selecciona la casilla del proyecto.
2. Haz clic en <i class="k-icon-archived"></i> **Archivar proyecto** en la esquina superior derecha.
3. Se te pedirá que confirmes que tu formulario no aceptará envíos mientras esté archivado. Haz clic en **ARCHIVAR** para confirmar.

![Archive](images/managing_projects/archive_home.png)

Para archivar un proyecto desde la **CONFIGURACIÓN** del proyecto:
1. Abre el proyecto y ve a la página **CONFIGURACIÓN**.
2. En la ventana <i class="k-icon-settings"></i> **General**, haz clic en **Archivar proyecto**.
3. Se te pedirá que confirmes que tu formulario no aceptará envíos mientras esté archivado. Haz clic en **ARCHIVAR** para confirmar.

![Archive](images/managing_projects/archive_settings.png)

Para desarchivar un proyecto, sigue los mismos pasos y haz clic en **Desarchivar proyecto**.

### Eliminar proyectos
Eliminar un proyecto borra permanentemente el formulario y todos los datos asociados. Esta acción no se puede revertir.

Hay dos formas de eliminar un proyecto. Para eliminar un proyecto desde la **Página de proyectos**:
1. En la **Página de proyectos**, selecciona la casilla junto al proyecto.
2. Haz clic en <i class="k-icon-trash"></i> **Eliminar 1 proyecto** en la esquina superior derecha.
3. Un cuadro de diálogo de confirmación te pedirá que confirmes lo siguiente:
    * Estás a punto de definitivamente eliminar este formulario.
    * Todos los datos recolectados en este formulario se eliminarán.
    * El formulario asociado con este proyecto se eliminará.

![Delete](images/managing_projects/delete_home.png)

Para eliminar un proyecto desde la **CONFIGURACIÓN** del proyecto:
1. Abre el proyecto y ve a la página **CONFIGURACIÓN**.
2. En la ventana <i class="k-icon-settings"></i> **General**, haz clic en **Eliminar Proyecto y datos**.
3. Un cuadro de diálogo de confirmación te pedirá que confirmes lo siguiente:
    * Estás a punto de definitivamente eliminar este formulario.
    * Todos los datos recolectados en este formulario se eliminarán.
    * El formulario asociado con este proyecto se eliminará.

![Delete](images/managing_projects/delete_settings.png)