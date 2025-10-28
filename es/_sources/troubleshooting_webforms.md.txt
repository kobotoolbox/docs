# Solución de problemas de formularios web de Enketo
<a href="../troubleshooting_webforms.html">Read in English</a> | <a href="../fr/troubleshooting_webforms.html">Lire en français</a> | <a href="../ar/troubleshooting_webforms.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/troubleshooting_webforms.md" class="reference">15 Feb 2022</a>

Los [formularios web de Enketo](enketo.md) funcionan en todos los dispositivos ya que se abren en navegadores web regulares y permiten la recolección de datos en línea o sin conexión. En general, recomendamos encarecidamente la última versión de todos los
[navegadores modernos](https://enke.to/modern-browsers). También puedes visitar
las [Preguntas frecuentes de Enketo](https://enketo.org/faq/#browsers) para aprender
más sobre _qué navegadores son compatibles y recomendados_ por Enketo.

## Problemas conocidos con formularios sin conexión en iOS

Los dispositivos iOS (que se ejecutan en iPhone y iPad) tienen varias limitaciones conocidas al
usar formularios habilitados sin conexión debido a la plataforma del sistema operativo de Apple. Nos
esforzamos por tener la última versión de iOS totalmente compatible.

-   La recolección de datos sin conexión funciona en cualquier navegador moderno. En iOS solo
    recomendamos Chrome o Safari.
-   La versión 9.x muestra "NotFoundError: DOM IDBDatabase Exception 8". Solución:
    Cierra todas las pestañas de Enketo en tu navegador, luego vuelve a abrir el formulario. El error
    ahora debería desaparecer para siempre.
-   La versión 9.3.1 muestra "Attempted to assign to readonly property" al cargar
    el formulario sin conexión
-   La versión 8.x muestra "undefined is not an object (evaluating 'c.resources')".
    Solución: Actualiza a la última versión de iOS

Si no se requiere la recolección de datos sin conexión y estás viendo un error en iOS,
considera usar la _versión solo en línea_ en lugar de la URL sin conexión.

## Pérdida de datos

Al recolectar datos a través de Enketo, los/as usuarios/as nunca deben borrar la
caché del navegador (ya sea manualmente o usando alguna aplicación). Borrar la caché de tu navegador (durante
la recolección de datos) eliminará toda la información almacenada en el navegador y, por lo tanto,
tu información no llegará a tu servidor de KoboToolbox. Esta pérdida de datos es
irreversible. Por lo tanto, aconsejamos encarecidamente a los/as usuarios/as que borren la caché del navegador si y
solo si has enviado exitosamente todos tus datos a tu servidor de KoboToolbox.