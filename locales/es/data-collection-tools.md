# Recolección de datos con KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/a42f7ff93a1567cc2ac66a749d2a7d5969cfa45a/source/data-collection-tools.md" class="reference">23 Apr 2026</a>

KoboToolbox admite dos formas principales de recolectar datos: **formularios web**, que se ejecutan en un navegador, y **KoboCollect**, la aplicación Android para la recolección de datos en dispositivos móviles. Ambos métodos admiten la recolección de datos sin conexión a internet.

Este artículo explica los dos métodos de recolección de datos disponibles en KoboToolbox, cómo elegir entre ellos y cómo prepararse antes de iniciar la recolección de datos.

<p class="note">
Para obtener más información sobre cada método de recolección de datos, consulta <a href="https://support.kobotoolbox.org/es/data_through_webforms.html">Recolección de datos a través de formularios web</a> y <a href="https://support.kobotoolbox.org/es/data_collection_kobocollect.html">Recolección de datos con KoboCollect</a>.
</p>

## Métodos de recolección de datos

Puedes recolectar datos con KoboToolbox de dos maneras principales:
- Los **formularios web** son formularios basados en navegador que se utilizan para recolectar datos a través de una página web. Son ideales para encuestas autoadministradas y la entrada de datos en el navegador.
- **KoboCollect** es una aplicación Android que se utiliza para recolectar datos en dispositivos Android. Es ideal para equipos de campo con encuestadores que usan teléfonos o tabletas Android.

Ambos métodos admiten la [recolección de datos sin conexión a internet](https://support.kobotoolbox.org/es/data-collection-tools.html#offline-data-collection).

### Elegir un método de recolección de datos

El mejor método de recolección de datos depende de cómo trabajará tu equipo en la práctica, y en algunos casos los equipos pueden usar ambos métodos dentro del mismo proyecto.

La tabla a continuación resume cuándo cada método es generalmente la mejor opción:

| Formularios web | KoboCollect |
| :--- | :--- |
| **Recomendado si:** <br> <ul><li>Los encuestados enviarán datos directamente a través de un enlace</li><li>Quieres una forma sencilla de abrir y compartir un formulario</li><li>Tu equipo usa una combinación de tipos de dispositivos</li><li>Quieres usar la recolección de datos en el navegador sin instalar una aplicación</li><li>Tu formulario incluye funcionalidades que solo están disponibles en formularios web, como el [tema de cuadrícula](https://support.kobotoolbox.org/es/alternative_enketo.html) o las [matrices de preguntas](https://support.kobotoolbox.org/es/matrix_response.html)</li></ul> | **Recomendado si:**<br><ul><li>Gran parte de tu recolección de datos se realiza en campo en entornos sin conexión a internet</li><li>Los datos son recolectados por un equipo de encuestadores que usan teléfonos o tabletas Android</li><li>Los encuestadores prefieren un flujo de trabajo basado en una aplicación (por ejemplo, para guardar borradores y enviar formularios finalizados más tarde)</li><li>Tu proyecto depende de funcionalidades del dispositivo móvil, como el [escaneo de códigos de barras o la captura de imágenes y videos](https://support.kobotoolbox.org/es/photo_audio_video_file.html)</li><li>Quieres tener más control sobre el manejo de formularios y la automatización, como enviar formularios, descargar formularios o eliminar datos cargados de los dispositivos</li></ul> |

Al elegir un método, considera cómo accederán las personas al formulario, qué dispositivos usarán, con qué frecuencia necesitarán trabajar sin conexión a internet y si tu formulario incluye funcionalidades que son más compatibles con un método que con el otro.

<p class="note">
<strong>Nota:</strong>
Algunas funcionalidades funcionan de manera diferente según el método de recolección. Ten esto en cuenta antes de iniciar la recolección de datos, y siempre prueba tu formulario con el método que usará tu equipo.
</p>

### Recolección de datos sin conexión a internet

Tanto los formularios web como KoboCollect admiten la **recolección de datos sin conexión a internet.**

- Al usar **formularios web**, KoboToolbox puede almacenar el formulario y las respuestas en la caché del navegador para que los usuarios puedan continuar ingresando datos sin conexión a internet.
  - Antes de desconectarte, debes abrir el formulario mientras estás conectado a internet y esperar a que se cargue completamente y quede [almacenado en la caché del dispositivo](https://support.kobotoolbox.org/es/data_through_webforms.html#offline-data-collection).
  - Cuando el dispositivo se vuelva a conectar, los envíos guardados se cargarán automáticamente.
- Al usar **KoboCollect**, los encuestadores pueden descargar formularios en blanco mientras están en línea, completarlos sin conexión a internet, guardar borradores, finalizar envíos y enviarlos más tarde cuando tengan acceso a internet.
  - KoboCollect también puede [configurarse](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings) para enviar formularios finalizados automáticamente cuando haya conexión o solo cuando el usuario decida cargarlos.

## Preparación para la recolección de datos

Antes de poder recolectar datos, debes **implementar tu formulario** para activarlo y ponerlo a disposición para recibir envíos. Si realizas cambios en el formulario más adelante, deberás reimplementarlo.

<p class="note">
Para obtener más información sobre cómo implementar tu formulario para la recolección de datos, consulta <a href="https://support.kobotoolbox.org/es/deploy_form_new_project.html">Implementar formularios para la recolección de datos</a>.
</p>

Una vez que tu formulario esté implementado, asegúrate de que tu configuración de recolección de datos esté lista antes de iniciarla:
- Decide qué método(s) de recolección de datos usar
- Confirma quién puede acceder al formulario y si se debe requerir autenticación
- Prueba el proyecto en un escenario similar a tu recolección de datos real, usando los mismos dispositivos y el mismo método de recolección que tus encuestados o encuestadores

Según el método de recolección que elijas, también recomendamos los siguientes pasos:

| Formularios web | KoboCollect |
| :--- | :--- |
| <ul><li>Decide si el formulario debe [requerir autenticación](https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication)</li><li>Si tu formulario requiere autenticación, asegúrate de que los recolectores de datos tengan los [permisos](https://support.kobotoolbox.org/es/managing_permissions.html) correctos para acceder a tu formulario de recolección de datos</li><li>Decide qué [modo de formulario web](https://support.kobotoolbox.org/es/data_through_webforms.html#data-collection-modes) usar para la recolección de datos</li><li>Comparte el enlace correcto del formulario con los recolectores de datos o encuestados</li></ul> | <ul><li>Confirma que los recolectores de datos tengan los [permisos](https://support.kobotoolbox.org/es/managing_permissions.html) correctos para acceder a tu formulario de recolección de datos</li><li>Asegúrate de que cada recolector de datos haya [instalado y configurado](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html) la aplicación KoboCollect</li><li>Confirma que cada recolector de datos haya [descargado el/los formulario(s)](https://support.kobotoolbox.org/es/data_collection_kobocollect.html#downloading-forms) antes de iniciar el trabajo de campo</li></ul> |

<p class="note">
<strong>Nota:</strong>
Los proyectos implementados están configurados para <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requerir autenticación</a> de forma predeterminada, lo que significa que los usuarios deben iniciar sesión para acceder a un formulario web o enviar datos. Para permitir que <strong>cualquier persona con el enlace del formulario</strong> pueda enviar datos, desactiva el requisito de autenticación del formulario. Si mantienes la autenticación activada, <a href="https://support.kobotoolbox.org/es/managing_permissions.html">comparte el proyecto</a> con usuarios específicos de KoboToolbox y dales el permiso <strong>Añadir envíos</strong>.
</p>