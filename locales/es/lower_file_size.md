# Reducir el tamaño de archivo de los medios recolectados
<a href="../lower_file_size.html">Read in English</a> | <a href="../fr/lower_file_size.html">Lire en français</a> | <a href="../ar/lower_file_size.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/lower_file_size.md" class="reference">15 Feb 2022</a>

Cuando tu formulario recolecta más de una imagen o estás recolectando decenas de
miles de registros, podrías enfrentar dificultades al generar el ZIP de Archivos
Adjuntos Multimedia si no ajustas la configuración de calidad de imagen antes de comenzar
la recolección de datos.

Open Camera es una aplicación de código abierto de terceros que puede ayudarte a hacer esto.

## Instrucciones

[Instala Open Camera](https://play.google.com/store/apps/details?id=net.sourceforge.opencamera&hl=en_US)
desde Android Play Store.

![image](/images/lower_file_size/open_cam.png)

## KoboCollect

En KoboCollect, cuando tomes una foto, ahora se te preguntará qué aplicación debe usarse
de forma predeterminada: Elige Open Camera y selecciona 'Siempre' para que no se te pregunte
de nuevo.

## Open Camera

En la configuración de Open Camera, ve a Configuración de Fotos, luego:

1. Abre Resolución de Cámara y elige la resolución aceptable más pequeña.
2. Abre calidad de imagen y elige un porcentaje: 90% se verá casi perfecto,
   por debajo del 50% la imagen se volverá más difícil de reconocer. Comienza con 70% y prueba
   algunas imágenes en diferentes niveles de calidad para encontrar el tamaño aceptable más bajo.

Este sitio web proporciona una descripción general de
[cómo estimar](http://fotoforensics.com/tutorial-estq.php) el nivel óptimo de
calidad JPEG.