# Añadir un logotipo personalizado
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/add_logo.md" class="reference">29 Jul 2025</a>


Añadir un logotipo personalizado en la parte superior de tu formulario es un proceso sencillo que sigue principalmente los mismos pasos que [agregar contenido multimedia a tus formularios](media.md).

Para comenzar:

1. Crea el archivo de imagen de tu logotipo y guárdalo con un nombre de archivo corto.

2. En tu XLSForm, configura la primera pregunta como tipo de pregunta Nota, deja la etiqueta en blanco y añade una columna titulada `media::image` con el nombre del archivo de tu logotipo en la celda. Como se muestra a continuación:

**hoja survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Cuando termines de editar el formulario, carga el XLSForm en un proyecto nuevo o en uno existente.

4. Implementa o reimplementa tu formulario, según sea un proyecto nuevo o esté reemplazando un formulario existente.

5. En la página de tu proyecto, ve a **CONFIGURACIONES>MULTIMEDIA** y [carga](media.md) tu archivo `logo.jpg`.

## Consejos:

-   Mantén tu imagen pequeña.
-   La imagen de tu logotipo no aparecerá en la vista previa del formulario, solo cuando el formulario esté abierto.
-   Si omites el último paso, tu formulario se mostrará sin los archivos multimedia. Asegúrate de que los archivos multimedia estén cargados antes de descargar el formulario en tus dispositivos cuando uses la aplicación Android.

<p class="note">Si abres el Formbuilder después de implementar tu XLSForm con el archivo de imagen del logotipo, automáticamente se le asignará una etiqueta de texto a la pregunta y tendrás que eliminarla para que el texto generado automáticamente no aparezca junto a tu logotipo en el formulario.</p>