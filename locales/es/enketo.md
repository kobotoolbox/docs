# ¿Qué son los formularios web de Enketo?

**Última actualización:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/enketo.md" class="reference">15
Feb 2022</a>

Según [Enketo.org](https://enketo.org), **Enketo** es el nombre de un
proyecto de código abierto, así como el nombre de una aplicación web de código abierto que
utiliza un formato de formulario de código abierto popular.

Enketo fue desarrollado como seguimiento de una tesis de maestría de 2009 en la
Universidad de Liverpool sobre la 'Aplicabilidad de
[Tecnologías Web con Capacidad Offline](https://blog.enketo.org/offline-capable-web-applications/)
para el Manejo de Información en Ayuda Humanitaria'.

Después de un año de desarrollo inicial, fue adoptado por
[un laboratorio en la Universidad de Columbia](https://qsel.columbia.edu/products-tools/) y
[lanzado por primera vez](https://blog.enketo.org/enketo-is-now-open-source-and-will-be-used-in-formhub/)
en 2012. Este fue el inicio de una cascada de
[adopción](https://enketo.org/about/adoption/) por empresas y organizaciones
en todo el mundo.

## ¿Qué ecosistema utiliza Enketo?

Enketo es parte del ecosistema OpenRosa/ODK, lo que significa:

1. Enketo puede combinarse con otras herramientas para crear de manera flexible un
   sistema de manejo de información completo. Esto ha resultado en la adopción de Enketo
   en KoboToolbox. También significa que el Proyecto Enketo puede enfocarse solo en
   la recolección de datos y hacerlo de la mejor manera posible.
2. Enketo no requiere un compromiso a largo plazo por parte del/la usuario/a.

## ¿Cuáles son las características generales?

Las encuestas desplegadas con Enketo:

-   funcionan sin conexión
-   tienen temas y widgets hermosos
-   son amigables para imprimir
-   pueden usar lógica de saltos y validación muy potente
-   se ejecutan en cualquier dispositivo, móvil o de escritorio, siempre que tenga un
    [navegador moderno](https://enke.to/modern-browsers)

## ¿Cómo puedo acceder a Enketo cuando estoy en KoboToolbox?

Cada vez que abres un formulario en la versión de formulario web dentro de KoboToolbox, estás
usando Enketo. Para más detalles, por favor visita nuestro artículo de ayuda
[Recolectar datos a través de formularios web](data_through_webforms.md).

## ¿Cómo soluciono problemas con Enketo?

Los formularios web de Enketo funcionan en todos los dispositivos ya que se abren en navegadores web regulares y
permiten la recolección de datos en línea o sin conexión. Generalmente recomendamos enfáticamente la
última versión de todos los navegadores modernos;
[consulta aquí para más detalles sobre navegadores que funcionan con Enketo](https://enketo.org/faq/#browsers).

**Problemas conocidos con formularios sin conexión en iOS**

Los dispositivos iOS (que se ejecutan en iPhone y iPad) tienen varias limitaciones conocidas con
el uso de formularios habilitados sin conexión debido a la plataforma del sistema operativo Apple. Nos
esforzamos por tener la última versión de iOS completamente compatible.

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
considera usar la versión _solo en línea_ en lugar de la URL sin conexión.

Para más detalles sobre la solución de problemas, por favor visita nuestro artículo de ayuda
[Solución de problemas de formularios web de Enketo](troubleshooting_webforms.md).