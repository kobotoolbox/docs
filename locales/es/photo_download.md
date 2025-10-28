# Descargando fotos y otros medios
<a href="../photo_download.html">Read in English</a> | <a href="../fr/photo_download.html">Lire en français</a> | <a href="../ar/photo_download.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/photo_download.md" class="reference">29 Jul 2025</a>

Si tu formulario [incluye](question_types.md) una pregunta de foto, video o grabación de audio, estos archivos se cargarán al servidor junto con tus otros datos. Al exportar tu conjunto de datos a XLS o CSV, estos archivos incluirán referencias a los nombres de los archivos adjuntos multimedia, pero no los archivos en sí. Para descargar todos tus archivos multimedia en bloque, elige la opción **Archivos adjuntos multimedia (ZIP)** en **DATOS>Descargas>Seleccionar tipo de exportación**.

Lo siguiente explica otras opciones para descargar y acceder a tus archivos multimedia recolectados.

<p class='note'>La exportación ZIP puede fallar para proyectos muy grandes debido a que se alcanza un límite de tiempo de espera del servidor de 30 minutos. Si ese es el caso, por favor sigue los métodos a continuación para extraer tus archivos multimedia del servidor de <strong>KoboToolbox</strong>.</p>

## Incluyendo hipervínculos directos a medios recolectados en la exportación XLS

1. Navega a **DATOS>Descargas** y expande la sección **Opciones avanzadas**
2. Asegúrate de que la opción _Incluir URLs de medios_ esté marcada (habilitada por defecto)

![Incluir URLs de medios](/images/photo_download/include_media_urls.png)

3. Haz clic en **EXPORTAR**

Si tu encuesta tenía la siguiente pregunta:

**hoja survey**

| type  | name    | label              |
| :---- | :------ | :----------------- |
| image | image_1 | Envía una imagen   |
| survey |

Y una presentación a esa pregunta con el nombre de archivo "image.jpg", la exportación tendrá el siguiente resultado:

| image_1   | image_1_URL               |
| :-------- | :------------------------ |
| image.jpg | https://link/to/image.jpg |

## Para conexiones lentas o proyectos muy grandes: Usando DownThemAll

El método de descarga ZIP siempre incluirá todos los archivos multimedia de tu proyecto. Esto puede tomar mucho tiempo para descargar en caso de un gran número de imágenes o videos recolectados o en caso de una conexión lenta. Aquí hay una solución alternativa para descargar todos (o una selección de) medios usando el popular gestor de descargas **DownThemAll** (solo compatible con el navegador Firefox):

1. Guarda tu archivo de Excel con los hipervínculos agregados (ver instrucciones arriba) como un archivo HTML en tu Escritorio, usando la opción Archivo > Guardar como... (elige 'Página web')

2. Inicia sesión en tu cuenta de KoboToolbox donde están alojadas tus fotos usando el navegador Firefox

3. En Firefox instala la [extensión DownThemAll](https://addons.mozilla.org/en-CA/firefox/addon/downthemall)

4. Aún en Firefox, abre la página web HTML guardada del **Paso 1**

5. Haz clic derecho en algún lugar de esa página y elige _DownThemAll!_, o haz clic en el botón de la extensión en la barra de herramientas de Firefox

6. En la ventana de la extensión que se abre haz clic en **Descargar**. Por defecto, Firefox guardará todos los archivos en la carpeta de Descargas de tu computadora (lo cual puede cambiarse)

7. Opcional: En la ventana que se abre, establece un límite de velocidad de descarga para evitar usar todo el ancho de banda disponible. La configuración también te permite establecer el número de intentos que deben hacerse para cada archivo en caso de problemas de conexión.

Si tienes muchos archivos multimedia esto tomará un tiempo para descargar. Pero el gestor de descargas **DownThemAll** se asegurará de que hayas descargado todas las imágenes y te informará en caso de que alguna de ellas no se haya descargado para que puedas intentarlo de nuevo.

![Extensión DownThemAll](/images/photo_download/downthemall_extension.jpg)

![Enlaces DownThemAll](/images/photo_download/downthemall_links.jpg)