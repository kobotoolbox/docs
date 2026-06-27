# Reducir el tamaño de los archivos multimedia
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/lower_file_size.md" class="reference">15 Feb 2022</a>

Cuando tu formulario recolecta más de una imagen o estás recolectando decenas de miles de registros, podrías tener dificultades para generar el archivo ZIP de archivos adjuntos multimedia si no ajustas la configuración de calidad de imagen antes de comenzar la recolección de datos.

Open Camera es una aplicación de código abierto de terceros que puede ayudarte a hacer esto.

## Instrucciones

[Instala Open Camera](https://play.google.com/store/apps/details?id=net.sourceforge.opencamera&hl=en_US)
desde la tienda Android Play Store.

![image](/images/lower_file_size/open_cam.png)

## KoboCollect

En KoboCollect, cuando tomes una foto, se te preguntará qué aplicación debe usarse por defecto: elige Open Camera y selecciona 'Siempre' para que no se te vuelva a preguntar.

## Open Camera

En la configuración de Open Camera, ve a Configuración de fotos y luego:

1. Abre Resolución de la cámara y elige la resolución aceptable más baja.
2. Abre Calidad de imagen y elige un porcentaje: el 90% se verá casi perfecto; por debajo del 50%, la imagen será más difícil de reconocer. Comienza con el 70% y prueba algunas imágenes en diferentes niveles de calidad para encontrar el tamaño aceptable más bajo.

Este sitio web ofrece una descripción general de
[cómo estimar](http://fotoforensics.com/tutorial-estq.php) el nivel de calidad JPEG óptimo.