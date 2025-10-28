# Agregar un logotipo personalizado
<a href="../add_logo.html">Read in English</a> | <a href="../fr/add_logo.html">Lire en français</a> | <a href="../ar/add_logo.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/add_logo.md" class="reference">29 Jul 2025</a>

Agregar un logotipo personalizado en la parte superior de tu formulario es un proceso simple y principalmente
sigue los mismos pasos que [agregar contenido multimedia a tus formularios](media.md).

Para comenzar:

1. Comienza creando tu archivo de imagen del logotipo y guárdalo con un nombre de archivo corto.

2. En tu XLSForm, haz que la primera pregunta sea de tipo Nota, deja la
   etiqueta en blanco y agrega una columna titulada `media::image` con el nombre de tu archivo de logotipo
   en la celda. Como se muestra a continuación:

**hoja survey**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. Cuando termines de editar el formulario, carga el XLSForm en un proyecto nuevo o
   existente.

4. Despliega o vuelve a desplegar tu formulario, dependiendo de si es un proyecto nuevo o si está
   reemplazando un formulario existente.

5. En la página de tu proyecto ve a **CONFIGURACIÓN>MULTIMEDIA** y [carga](media.md) tu
   archivo `logo.jpg`.

## Consejos:

-   Mantén tu imagen pequeña.
-   Tu imagen de logotipo no aparecerá en la vista previa del formulario, solo cuando el formulario se
    abra.
-   Omitir el paso final significará que tu formulario se mostrará sin
    los archivos multimedia. Asegúrate de que los archivos multimedia estén cargados antes de descargar
    el formulario a tus dispositivos cuando uses la aplicación de Android.

<p class="note">Si abres el editor de formularios después de desplegar tu XLSForm con el archivo de imagen del logotipo, automáticamente le dará a la pregunta una etiqueta de texto y necesitarás eliminarla para que el texto automatizado no aparezca junto a tu logotipo en tu formulario.</p>

archivo `logo.jpg` arrastrando el archivo o seleccionándolo desde tu computadora.

- Los formatos de imagen recomendados son JPEG y PNG. Las imágenes SVG no son compatibles.
- Las dimensiones recomendadas para los logotipos son un ancho de 400 píxeles y una altura de 100 píxeles.

- Mantén tu imagen pequeña.
