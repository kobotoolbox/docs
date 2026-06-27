# Tipo de metapregunta de registro de auditoría

El registro de auditoría puede ser una herramienta útil para monitorear el comportamiento de los encuestadores y descubrir qué preguntas están tardando más en responderse, comprender mejor cómo los encuestadores navegan por un formulario determinado, y ver qué encuestadores generalmente tardan más tiempo en enviar sus respuestas.

<p class="note">Esta función requiere analizar manualmente archivos CSV.</p>

La metapregunta de registro de auditoría es un tipo de pregunta que solo está disponible usando la [aplicación Android KoboCollect](kobocollect_on_android_latest.md).

Para agregar un tipo de metapregunta `audit` a un formulario y ver los datos finalizados, sigue los pasos a continuación:

1. En un archivo XLSForm, agrega `audit` de la misma manera que agregarías cualquier otra metapregunta. Luego carga el archivo del formulario en tu proyecto e implementa el formulario.

**hoja survey**

| type  | name  | label                  |
| :---- | :---- | :--------------------- |
| start | start |                        |
| end   | end   |                        |
| audit | audit |                        |
| text  | Q1    | Q1. What is your name? |
| survey |

2. Recolecta datos usando la [aplicación Android KoboCollect](kobocollect_on_android_latest.md) y envía los formularios finalizados de vuelta al servidor. KoboCollect guarda los registros de auditoría de cada envío en un archivo CSV que se guarda y se carga en el servidor de la misma manera que lo haría una foto adjunta.

3. Una vez enviados los datos, abre tu proyecto en el navegador y ve a **DATOS**, luego a **Descargas**. Selecciona **Archivos multimedia adjuntos (ZIP)** como tipo de exportación y haz clic en **Nuevo exportable**. Una vez que la descarga haya dejado de estar pendiente, haz clic en el archivo para descargarlo a tu computadora.

![image](/images/audit_logging/zip_export.png)

4. Una vez extraído y abierto el archivo ZIP, haz clic en el archivo llamado 'audit.csv' para ver los registros de auditoría. Es importante tener en cuenta que el CSV utiliza el tiempo [Unix Epoch](https://www.unixtimestamp.com/index.php), por lo que los registros se guardan en milisegundos.

5. Dado que las marcas de tiempo se guardan para cada envío individual, probablemente necesitarás copiar los valores en una nueva hoja de cálculo para hacer un análisis más detallado de todos los envíos (por ejemplo, por encuestador o por pregunta). La consolidación de varios archivos CSV se puede realizar con [muchas herramientas gratuitas o escribiendo un script](https://www.google.com/search?q=merge+many+CSV). Para obtener información más detallada sobre la estructura del registro y los tipos de eventos, visita la documentación de ODK sobre [Logging Enumerator Behavior](https://docs.getodk.org/form-audit-log/#).

No dudes en publicar en nuestro [Foro de la comunidad](https://community.kobotoolbox.org/) para compartir tu enfoque o script favorito para usar esta función, de modo que otros puedan aprender de tu experiencia.