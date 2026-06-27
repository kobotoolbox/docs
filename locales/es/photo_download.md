# Descargar fotos y otros archivos multimedia

Si tu formulario [incluye](question_types.md) una pregunta de foto, video o grabación de audio, estos archivos se cargarán al servidor junto con el resto de tus datos. Al exportar tu conjunto de datos a XLS o CSV, estos archivos incluirán referencias a los nombres de los archivos multimedia adjuntos, pero no los archivos en sí. Para descargar todos tus archivos multimedia de forma masiva, elige la opción **Archivos multimedia adjuntos (ZIP)** en **DATOS>Descargas>Seleccionar el tipo de exportación**.

A continuación se explican otras opciones para descargar y acceder a los archivos multimedia recolectados.

<p class='note'>La exportación ZIP puede fallar en proyectos muy grandes debido a que se alcanza el límite de tiempo del servidor de 30 minutos. En ese caso, sigue los métodos que se describen a continuación para extraer tus archivos multimedia del servidor de <strong>KoboToolbox</strong>.</p>

## Incluir hipervínculos directos a los archivos multimedia recolectados en la exportación XLS

1. Ve a **DATOS>Descargas** y expande la sección **Opciones avanzadas**
2. Asegúrate de que la opción _Incluir URL de archivos multimedia_ esté marcada (activada por defecto)

![Incluir URL de archivos multimedia](/images/photo_download/include_media_urls.png)

3. Haz clic en **EXPORTAR**

Si tu encuesta tenía la siguiente pregunta:

**hoja survey**

| type  | name    | label           |
| :---- | :------ | :-------------- |
| image | image_1 | Submit an image |
| survey |

Y un envío a esa pregunta con el nombre de archivo "image.jpg", la exportación tendrá el siguiente resultado:

| image_1   | image_1_URL               |
| :-------- | :------------------------ |
| image.jpg | https://link/to/image.jpg |

## Para conexiones lentas o proyectos muy grandes: usar DownThemAll

El método de descarga ZIP siempre incluirá todos los archivos multimedia de tu proyecto. Esto puede tardar mucho tiempo en descargarse en caso de un gran número de imágenes o videos recolectados, o en caso de una conexión lenta. A continuación se presenta una solución alternativa para descargar todos (o una selección de) los archivos multimedia usando el popular gestor de descargas **DownThemAll** (compatible únicamente con el navegador Firefox):

1. Guarda tu archivo Excel con los hipervínculos añadidos (consulta las instrucciones anteriores) como un archivo HTML en tu escritorio, usando la opción Archivo > Guardar como... (elige 'Página web')

2. Inicia sesión en tu cuenta de KoboToolbox donde están alojadas tus fotos usando el navegador Firefox

3. En Firefox, instala la [extensión DownThemAll](https://addons.mozilla.org/en-CA/firefox/addon/downthemall)

4. Aún en Firefox, abre la página web HTML guardada en el **Paso 1**

5. Haz clic derecho en algún lugar de esa página y elige _DownThemAll!_, o haz clic en el botón de la extensión en la barra de herramientas de Firefox

6. En la ventana de la extensión que se abre, haz clic en **Descargar**. Por defecto, Firefox guardará todos los archivos en la carpeta de Descargas de tu computadora (lo cual se puede cambiar)

7. Opcional: en la ventana que se abre, establece un límite de velocidad de descarga para evitar usar todo el ancho de banda disponible. La configuración también te permite establecer el número de intentos que se deben realizar para cada archivo en caso de problemas de conexión.

Si tienes muchos archivos multimedia, la descarga tardará un tiempo. Sin embargo, el gestor de descargas **DownThemAll** se asegurará de que hayas descargado todas las imágenes y te notificará en caso de que alguna no se haya descargado, para que puedas intentarlo de nuevo.

![Extensión DownThemAll](/images/photo_download/downthemall_extension.jpg)

![Enlaces DownThemAll](/images/photo_download/downthemall_links.jpg)