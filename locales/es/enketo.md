# ¿Qué son los formularios web Enketo?

Según [Enketo.org](https://enketo.org), **Enketo** es el nombre de un proyecto
de código abierto, así como el nombre de una aplicación web de código abierto
que utiliza un formato de formulario de código abierto popular.

Enketo fue desarrollado como seguimiento de una disertación de maestría de 2009
en la Universidad de Liverpool sobre la 'Aplicabilidad de las
[Tecnologías Web con capacidad sin conexión](https://blog.enketo.org/offline-capable-web-applications/)
para la gestión de información en la ayuda humanitaria'.

Después de un año de desarrollo inicial, fue adoptado por
[un laboratorio de la Universidad de Columbia](https://qsel.columbia.edu/products-tools/) y
[lanzado por primera vez](https://blog.enketo.org/enketo-is-now-open-source-and-will-be-used-in-formhub/)
en 2012. Este fue el inicio de una cascada de
[adopciones](https://enketo.org/about/adoption/) por parte de empresas y
organizaciones de todo el mundo.

## ¿Qué ecosistema utiliza Enketo?

Enketo es parte del ecosistema OpenRosa/ODK, lo que significa que:

1. Enketo puede combinarse con otras herramientas para crear de manera flexible
   un sistema de gestión de información completo. Esto ha dado lugar a la
adopción de Enketo en KoboToolbox. También significa que el proyecto Enketo
   puede enfocarse únicamente en la recolección de datos y hacerlo de la mejor
   manera posible.
2. Enketo no requiere un compromiso a largo plazo por parte del usuario.

## ¿Cuáles son las características generales?

Las encuestas implementadas con Enketo:

-   funcionan sin conexión a internet
-   tienen temas y widgets atractivos
-   son compatibles con la impresión
-   pueden usar lógica de omisión y validación muy potente
-   funcionan en cualquier dispositivo, móvil o de escritorio, siempre que
    tenga un
    [navegador moderno](https://enke.to/modern-browsers)

## ¿Cómo puedo acceder a Enketo en KoboToolbox?

Cada vez que abres un formulario en la versión de formulario web dentro de
KoboToolbox, en realidad estás usando Enketo. Para más detalles, visita nuestro
artículo de ayuda
[Recolección de datos a través de formularios web](data_through_webforms.md).

## ¿Cómo soluciono problemas con Enketo?

Los formularios web Enketo funcionan en todos los dispositivos, ya que se abren
en navegadores web normales y permiten la recolección de datos en línea o sin
conexión a internet. En general, recomendamos usar la versión más reciente de
todos los navegadores modernos;
[consulta aquí para más detalles sobre los navegadores compatibles con Enketo](https://enketo.org/faq/#browsers).

**Problemas conocidos con formularios sin conexión en iOS**

Los dispositivos iOS (que se ejecutan en iPhones y iPads) tienen varias
limitaciones conocidas al usar formularios habilitados para uso sin conexión,
debido a la plataforma del sistema operativo de Apple. Nos esforzamos por
mantener la compatibilidad total con la versión más reciente de iOS.

-   La recolección de datos sin conexión funciona en cualquier navegador
    moderno. En iOS solo recomendamos Chrome o Safari.
-   La versión 9.x muestra "NotFoundError: DOM IDBDatabase Exception 8".
    Solución: cierra todas las pestañas de Enketo en tu navegador y vuelve a
    abrir el formulario. El error debería desaparecer de forma permanente.
-   La versión 9.3.1 muestra "Attempted to assign to readonly property" al
    cargar el formulario sin conexión.
-   La versión 8.x muestra "undefined is not an object (evaluating
    'c.resources')". Solución: actualiza a la versión más reciente de iOS.

Si no necesitas recolectar datos sin conexión y ves un error en iOS, considera
usar la versión _solo en línea_ en lugar de la URL sin conexión.

Para más detalles sobre la resolución de problemas, visita nuestro artículo de
ayuda [Solución de problemas con formularios web Enketo](troubleshooting_webforms.md).