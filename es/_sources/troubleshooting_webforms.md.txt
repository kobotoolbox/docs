# Resolución de problemas con formularios web Enketo

Los [formularios web Enketo](enketo.md) funcionan en todos los dispositivos, ya que se abren en navegadores web convencionales y permiten la recolección de datos en línea o sin conexión. En general, recomendamos usar la última versión de todos los [navegadores modernos](https://enke.to/modern-browsers). También puedes visitar las [Preguntas frecuentes de Enketo](https://enketo.org/faq/#browsers) para obtener más información sobre _qué navegadores son compatibles y recomendados_ por Enketo.

## Problemas conocidos con formularios sin conexión en iOS

Los dispositivos iOS (iPhones y iPads) tienen varias limitaciones conocidas al usar formularios habilitados para uso sin conexión, debido a la plataforma del sistema operativo de Apple. Nos esforzamos por tener compatibilidad total con la última versión de iOS.

-   La recolección de datos sin conexión funciona en cualquier navegador moderno. En iOS, solo recomendamos Chrome o Safari.
-   La versión 9.x muestra "NotFoundError: DOM IDBDatabase Exception 8". Solución: cierra todas las pestañas de Enketo en tu navegador y vuelve a abrir el formulario. El error debería desaparecer de forma permanente.
-   La versión 9.3.1 muestra "Attempted to assign to readonly property" al cargar el formulario sin conexión.
-   La versión 8.x muestra "undefined is not an object (evaluating 'c.resources')". Solución: actualiza a la última versión de iOS.

Si no necesitas recolectar datos sin conexión y ves un error en iOS, considera usar la _versión solo en línea_ en lugar de la URL sin conexión.

## Pérdida de datos

Al recolectar datos a través de Enketo, los usuarios nunca deben borrar la caché del navegador (ni de forma manual ni mediante alguna aplicación). Borrar la caché del navegador durante la recolección de datos eliminará toda la información almacenada en el navegador, por lo que tus datos no llegarán a tu servidor de KoboToolbox. Esta pérdida de datos es irreversible. Por ello, recomendamos encarecidamente borrar la caché del navegador únicamente si has enviado correctamente todos tus datos a tu servidor de KoboToolbox.