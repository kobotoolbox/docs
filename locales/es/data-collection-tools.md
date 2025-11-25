# Descripción general de las herramientas de recolección de datos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/53c2e7dae53b8450c51194fb49c7d915fe735012/source/data-collection-tools.md" class="reference">11 Sep 2025</a>

KoboToolbox permite la recolección de datos de múltiples maneras. Debido a que KoboToolbox está
construido sobre los [estándares Xform/ODK](https://xlsform.org), nuestros formularios son
compatibles con
[una serie de herramientas diferentes](https://xlsform.org/en/#tools-that-support-xlsforms)
que se pueden utilizar para la recolección de datos.

Para dispositivos Android, recomendamos usar
la [aplicación de Android de KoboCollect](https://play.google.com/store/apps/details?id=org.koboc.collect.android&hl=en_US),
que se puede descargar desde Google Play Store e instalar en cualquier
teléfono o tableta Android estándar.

Para cualquier otro dispositivo (incluyendo iPhone, iPad o cualquier computadora portátil o de escritorio), 
recomendamos usar el formulario web [para recolectar datos](data_through_webforms.md).

## Un resumen rápido sobre las diferencias entre las dos opciones

| &nbsp;                                                                         | Formularios web                                    | KoboCollect                                            |
| :----------------------------------------------------------------------------- | :------------------------------------------------- | :----------------------------------------------------- |
| Dispositivos                                                                   | Cualquier dispositivo móvil o computadora          | Solo Android                                           |
| Se ejecuta en...                                                               | Navegador                                          | Aplicación nativa de Android                           |
| Configurable                                                                   | A nivel del servidor                               | En cada dispositivo                                    |
| Visualización predeterminada del formulario                                    | Todas las preguntas en la misma pantalla           | Una pregunta por pantalla                              |
| Carga de datos                                                                 | Automáticamente cuando hay conexión disponible     | A petición del/a usuario/a o inmediatamente si hay conexión disponible |
| Metapreguntas específicas del teléfono (`subscriberid`, `simserial`, `phonenumber`) | No                                          | Sí                                                     |
| Tipo de pregunta `barcode`                                                     | No (excepto entrada manual)                        | Sí                                                     |
| Diferentes estilos de formulario                                               | Sí                                                 | No                                                     |
| Encriptación                                                                   | No para almacenamiento, pero siempre durante la transferencia | Se puede habilitar en el dispositivo, siempre durante la transferencia |
| Apariencia `hide-input` para mapas para ocultar entradas GPS manuales          | Sí                                                 | No                                                     |
| Opciones avanzadas de apariencia de mapas (`streets`, `terrain`, `satellite`, `[other]`) | Sí                                      | No                                                     |
| Formato de texto en notas y etiquetas (negrita, cursiva, enlaces)              | Sí                                                 | No                                                     |
| Combinar notas subsecuentes en una sola nota en la pantalla                    | Sí                                                 | No                                                     |
| Apariencia `multiline` para preguntas de tipo `text`                           | Sí                                                 | Sí                                                     |
| Apariencia `horizontal-compact` para preguntas de tipo selección               | Sí                                                 | No                                                     |
| Apariencia de escala `likert` para preguntas de tipo selección                 | Sí                                                 | Sí                                                     |
| Apariencia `compact-2` para preguntas de tipo selección                        | No                                                 | Sí                                                     |
| Apariencia `no-calendar`                                                       | No                                                 | Sí                                                     |
| Apariencias avanzadas de imagen (`annotate`, `draw`, `signature`)              | Sí                                                 | Sí                                                     |
| Comando de cálculo `repeat_count()`                                            | Establece un número mínimo de grupos repetidos     | Establece un número exacto de grupos repetidos         |

### Recolectar datos usando KoboCollect

Después de desplegar un proyecto, puedes ir a **Formulario - Recolectar datos**, y luego
seleccionar la aplicación de Android.

![image](/images/data_collection_tool/KoboCollect.gif)

Para obtener detalles sobre cómo configurar KoboCollect en cualquier dispositivo Android,
[lee este artículo](kobocollect_on_android_latest.md).

### Recolectar datos usando el formulario web Enketo

Para [usar el formulario web](data_through_webforms.md), después de desplegar un proyecto, puedes
ir a **Formulario - Recolectar datos**, donde hay múltiples opciones disponibles (en línea o sin conexión, envío
único o múltiple). La opción predeterminada es **En línea-Sin conexión
(envío múltiple)**.

![image](/images/data_collection_tool/Webform.gif)