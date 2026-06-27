# Recolección de datos a través de formularios web
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/7422ce15732061510b56a7bf2bfb464ddee641a0/source/data_through_webforms.md" class="reference">6 de mayo de 2026</a>

Los formularios web de KoboToolbox te permiten **recolectar datos directamente en un navegador web**, sin necesidad de instalar una aplicación. Son versiones de tu formulario que funcionan en el navegador y que puedes usar para previsualizar y probar tu cuestionario, o para recolectar datos reales en teléfonos, tabletas y computadoras.

Los formularios web funcionan en la mayoría de los dispositivos modernos, incluidos dispositivos Android, iPhones, iPads, laptops y computadoras de escritorio. Son especialmente útiles en proyectos donde los encuestados completan un formulario a través de un enlace compartido, donde el equipo de recolección de datos usa diferentes tipos de dispositivos, o donde se desea ingresar datos en una computadora en lugar de hacerlo a través de una aplicación.

Los formularios web también admiten **recolección de datos sin conexión** una vez que el formulario se ha abierto y almacenado en caché en el navegador. Son compatibles con toda la lógica de formulario configurada en KoboToolbox, incluidas la lógica de omisión y las reglas de validación, y su apariencia puede personalizarse mediante diferentes [temas de formulario web](https://support.kobotoolbox.org/es/alternative_enketo.html).

<p class="note">
<strong>Nota:</strong>
 Los formularios web de KoboToolbox funcionaban anteriormente con <a href="https://enketo.org">Enketo</a>, razón por la cual en documentación anterior se los denominaba formularios web Enketo.
</p>

Este artículo cubre los siguientes temas:
- Compartir formularios web de KoboToolbox para la recolección de datos
- Elegir el modo de formulario web adecuado
- Recolectar datos y guardar borradores en el navegador
- Usar formularios web sin conexión
- Personalizar los enlaces de formularios web para casos de uso específicos
- Solución de problemas comunes

## Compartir formularios web para la recolección de datos

Una vez que tu proyecto esté listo para la recolección de datos, puedes compartir fácilmente un enlace con los encuestados o los recolectores de datos para que ingresen información.

Para compartir un enlace con los encuestados:

1. Abre la página **FORMULARIO** y asegúrate de que tu formulario haya sido [implementado](https://support.kobotoolbox.org/es/deploy_form_new_project.html).
2. En la sección **Recolectar datos**, haz clic en **COPIAR** para copiar el enlace y compartirlo con los recolectores de datos o los encuestados.
3. También puedes hacer clic en **ABRIR** para abrir el formulario en una nueva pestaña del navegador.

![Abrir o copiar un formulario](images/data_through_webforms/copy_open.png)

### Requisito de autenticación

De forma predeterminada, los proyectos implementados [requieren que los usuarios inicien sesión](https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication) antes de poder abrir un formulario web o enviar datos.

- Para mantener la autenticación requerida, comparte el proyecto con usuarios específicos de KoboToolbox y otórgales el permiso **Añadir envíos**.
- Para permitir que cualquier persona con el enlace envíe datos sin nombre de usuario ni contraseña, puedes desactivar el requisito de autenticación en la sección **Recolectar datos** activando la opción "Permitir envíos a este formulario sin nombre de usuario ni contraseña".

<p class="note">
Para obtener más información sobre los permisos para compartir formularios, consulta <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html">Compartir proyectos con configuraciones a nivel de proyecto</a> y <a href="https://support.kobotoolbox.org/es/managing_permissions.html">Compartir proyectos con permisos a nivel de usuario/a</a>.
</p>

### Modos de recolección de datos

KoboToolbox ofrece varias opciones de enlace de formulario web en la sección **Recolectar datos**. Estas opciones afectan el enlace que abres o compartes, pero no modifican el formulario en sí.

![Seleccionar modo de recolección de datos](images/data_through_webforms/modes.png)

Los modos de formulario web disponibles son:

| Modo de recolección de datos | Descripción |
|:---|:---|
| En línea-Sin conexión (múltiples envíos) | Permite la recolección de datos en línea o sin conexión y admite múltiples envíos desde el mismo dispositivo. |
| Solo en línea (múltiples envíos) | Admite múltiples envíos desde el mismo dispositivo, pero requiere conexión a internet para funcionar. |
| Solo en línea (único envío) | Permite un envío a la vez desde el mismo dispositivo y puede usarse con un <a href="https://support.kobotoolbox.org/es/data_through_webforms.html#redirecting-users-to-another-webpage-after-submission">enlace de redirección</a> después del envío. No se impide que los usuarios vuelvan a abrir el enlace para enviar datos nuevamente. |
| Solo en línea (uno por encuestado) | Impide que el mismo usuario en el mismo navegador y dispositivo envíe más de una vez. |
| Código de formulario web integrable | Proporciona código HTML para insertar el formulario en tu propio sitio web. |
| Solo lectura | Abre el formulario para previsualización y pruebas sin permitir envíos. |

### Imprimir un formulario web

También puedes **imprimir un formulario web** para compartirlo durante el desarrollo del formulario o usarlo para la recolección de datos en papel. Para hacerlo:

1. Abre tu formulario web.
2. Haz clic en el botón de impresora en la esquina superior derecha.

La versión impresa incluye todas las preguntas y sugerencias adicionales, independientemente de la lógica del formulario.

![Hacer clic en el ícono de impresión para imprimir el formulario](images/data_through_webforms/print.png)

## Recolectar datos con formularios web

Después de abrir el formulario, los usuarios pueden completarlo directamente en su navegador. Si el formulario incluye [varios idiomas](https://support.kobotoolbox.org/es/collecting_data_multiple_languages.html), los usuarios pueden cambiar el idioma en la parte superior del formulario.

![Cambiar el idioma del formulario](images/data_through_webforms/change_language.png)

Al final del formulario, los usuarios pueden guardar su trabajo como borrador o enviarlo:

- **Enviar** finaliza el envío y lo envía al servidor cuando hay conexión disponible. Una vez enviado, el registro ya no puede editarse en el navegador.
- **Guardar borrador** almacena el envío en el dispositivo para que pueda reabrirse y completarse más tarde.

![Guardar o enviar un formulario](images/data_through_webforms/save_submit.png)

### Gestión de borradores

Guardar un borrador almacena el envío en el navegador para que pueda reabrirse y completarse más tarde. Los borradores no se envían al servidor de KoboToolbox hasta que se reabren, finalizan y envían.

Cuando guardas un formulario como borrador, se te pedirá que le **asignes un nombre** para que sea más fácil encontrarlo después.

El **contador de cola** en la esquina superior izquierda muestra cuántos borradores están guardados en el navegador. Para reabrir un borrador:

1. Haz clic en el **contador de cola** para abrir la lista de borradores guardados.
2. Selecciona el borrador que deseas abrir.
3. Revisa o edita el borrador y luego envíalo.

![Ícono del contador de cola](images/data_through_webforms/queue.png)

<p class="note">
<strong>Nota:</strong>
Los borradores se almacenan en el navegador hasta que se envían, incluso si cierras el navegador, apagas el dispositivo o te quedas sin conexión. No borres la caché del navegador ni los datos del sitio durante la recolección de datos, y asegúrate de que el dispositivo no esté configurado para borrarlos automáticamente, ya que esto podría eliminar permanentemente los borradores guardados.
</p>

### Recolección de datos sin conexión

Los formularios web **admiten la recolección de datos sin conexión** en todos los navegadores y dispositivos de uso generalizado. Al usar formularios web, KoboToolbox puede almacenar el formulario y las respuestas en el navegador para que los usuarios puedan continuar ingresando datos sin conexión a internet.

<p class="note">
<strong>Nota:</strong>
Al ingresar datos sin conexión, no borres la caché del navegador ni los datos del sitio durante la recolección de datos, y asegúrate de que el dispositivo no esté configurado para borrarlos automáticamente, ya que esto podría eliminar permanentemente los formularios sin conexión y los envíos en cola.
</p>

Para recolectar datos sin conexión con formularios web:

1. Antes de desconectarte, abre el formulario con conexión y espera a que se cargue completamente y se almacene en caché en el dispositivo. Esto puede tardar hasta 30 segundos.
2. Una vez que el formulario se haya almacenado en caché, aparece un **ícono de confirmación** en la esquina superior izquierda para indicar que ya puede usarse sin conexión.
    - Si te desconectas antes de que el formulario se haya almacenado en caché, es posible que pierdas acceso a la página cuando se actualice.

    ![Ícono de barras de señal](images/data_through_webforms/signal_bars.png)
3. Al enviar datos sin conexión, los envíos se agregan a la cola. El **contador de cola** muestra cuántos registros están esperando para cargarse.

![Ícono del contador de cola](images/data_through_webforms/queue.png)

4. Haz clic en el **contador de cola** para ver los envíos finalizados que esperan cargarse cuando haya conexión a internet disponible. También puedes exportar los envíos en cola como un archivo ZIP.
5. Una vez que el dispositivo se vuelva a conectar, los envíos guardados se cargan automáticamente en segundo plano mientras el formulario permanece abierto.

<p class="note">
<strong>Nota:</strong>
Para facilitar el acceso durante la recolección de datos sin conexión, puede ser útil marcar el formulario como favorito o agregar un acceso directo a la pantalla de inicio de tu teléfono usando la opción <strong>Agregar a la pantalla de inicio</strong> del menú del navegador.
</p>

## Personalizar los enlaces de formularios web

Puedes modificar un enlace de formulario web para controlar cómo se abre o se comporta el formulario para diferentes usuarios y casos de uso. Por ejemplo, puedes abrir el formulario en un idioma específico, rellenar previamente ciertos valores o redirigir a los usuarios a otra página después de que envíen el formulario.

### Abrir el formulario en un idioma específico

Si tu formulario tiene varios idiomas, puedes agregar un parámetro de idioma a la URL del formulario web para que se abra en un idioma específico. Esto puede ser útil cuando se comparten diferentes enlaces con diferentes grupos de usuarios.

Para compartir un enlace que abra el formulario en un idioma diferente al idioma predeterminado del formulario:

1. Copia el enlace de tu formulario en **FORMULARIO > Recolectar datos**.
2. Agrega `?lang=código_de_idioma` al final de la URL, donde `código_de_idioma` es el código del idioma seleccionado.
- Por ejemplo: `https://ee.kobotoolbox.org/x/[form_id]?lang=fr`.

<p class="note">
Para obtener más información, consulta <a href="https://support.kobotoolbox.org/es/collecting_data_multiple_languages.html#language-specific-form-url">Recolectar datos en diferentes idiomas</a>.
</p>

### Rellenar previamente un campo desde el enlace web

También puedes rellenar previamente un campo de tu formulario a través del enlace web. Esto es útil cuando deseas pasar un valor conocido al formulario de forma automática.

Por ejemplo, podrías compartir diferentes enlaces en diferentes lugares, y cada enlace podría abrir el mismo formulario con un campo oculto que indique de dónde proviene el enlace. También podrías compartir un enlace diferente con cada encuestado, con el ID único de esa persona ya incluido en el enlace.

Para compartir un enlace que rellene previamente un campo de tu formulario:

1. Agrega la pregunta que deseas rellenar previamente a tu formulario y luego configura su [nombre de columna de datos](https://support.kobotoolbox.org/es/glossary.html#data-column-name).
    - Puede ser una pregunta de tipo [Oculto](https://support.kobotoolbox.org/es/form_logic.html#storing-constants-in-your-form) si deseas almacenar el valor en segundo plano, o cualquier tipo de pregunta estándar si deseas que los encuestados lo vean en el formulario.
2. Copia el enlace de tu formulario en **FORMULARIO > Recolectar datos**.
3. Agrega `?d[nombre_de_columna_de_datos]=valor` al final de la URL, donde `nombre_de_columna_de_datos` es el nombre de columna de datos de la pregunta Oculta y `valor` es el valor rellenado previamente.
    - Por ejemplo: `https://ee.kobotoolbox.org/x/[form_id]?d[prefilled_field]=12345`.

<p class="note">
<strong>Nota:</strong>
Usa el nombre completo de la columna de datos en el parámetro de la URL. Si la pregunta está dentro de uno o más grupos, el nombre debe incluir también el <strong>nombre del grupo o los nombres de los grupos</strong> (por ejemplo, <code>group1/question1</code>). Puedes encontrar el nombre exacto en el campo <a href="https://support.kobotoolbox.org/es/question_options.html#data-column-name">Nombre de columna de datos</a> de la pregunta en el Formbuilder, o en la columna <code>name</code> de un XLSForm.
</p>

### Redirigir a los usuarios a otra página web después del envío

Al usar el modo de recolección de datos **Solo en línea (único envío)**, puedes redirigir a los usuarios a otra página web después de que envíen su formulario.

Para redirigir a los usuarios a otra página web:

1. En **FORMULARIO > Recolectar datos**, selecciona el modo de recolección de datos **Solo en línea (único envío)**.
2. Copia el enlace de tu formulario.
3. Agrega `?return_url=página_web` al final de la URL, donde `página_web` es la URL de la página web.
    - Por ejemplo: `https://ee.kobotoolbox.org/x/[form_id]?return_url=https://website.com`.

<p class="note">
<strong>Nota:</strong>
Puedes combinar varios parámetros en el mismo enlace separándolos con <code>&</code>.
</p>

## Solución de problemas

<details>
<summary><strong>El formulario no funciona sin conexión</strong></summary>
Antes de desconectarte, asegúrate de que el formulario se haya abierto completamente y almacenado en caché en el navegador. Verifica el indicador de disponibilidad sin conexión en el formulario antes de comenzar la recolección de datos sin acceso a internet.

![Ícono de barras de señal](images/data_through_webforms/signal_bars.png)
</details>

<br>

<details>
<summary><strong>El navegador se cierra inesperadamente durante la recolección de datos</strong></summary>
Si el dispositivo se reinicia, el navegador se actualiza o el formulario se cierra mientras estás ingresando datos, tus respuestas generalmente se guardan en el navegador. Cuando vuelvas a abrir el formulario, KoboToolbox te preguntará si deseas descartar los datos ingresados anteriormente o cargarlos nuevamente en el formulario para continuar.
</details>

<br>

<details>
<summary><strong>Los envíos no llegan al servidor</strong></summary>
Si el formulario se usó sin conexión, es posible que los envíos aún estén esperando en la cola. Verifica el contador de cola y asegúrate de que el dispositivo se haya vuelto a conectar a internet. Los formularios web cargan automáticamente los envíos en cola cuando hay conexión disponible.

![Ícono del contador de cola](images/data_through_webforms/queue.png)
</details>

<br>

<details>
<summary><strong>Se pide a los encuestados que inicien sesión</strong></summary>
Verifica si el proyecto está configurado para <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requerir autenticación</a> para los envíos. Si es así, los usuarios deben iniciar sesión con una cuenta que tenga permiso para añadir envíos, o puedes desactivar el requisito en <strong>FORMULARIO > Recolectar datos</strong>.
</details>

<br>

<details>
<summary><strong>Cambiar de cuenta en los formularios web</strong></summary>
Si se <a href="https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication">requiere autenticación</a> para los envíos, es posible que los formularios web mantengan la sesión iniciada con la cuenta usada anteriormente para formularios web en ese navegador. Esto puede generar confusión si el formulario se comparte con una cuenta diferente o si necesitas enviar datos como otro usuario.<br><br>Para cambiar de cuenta, haz clic en <strong>cerrar sesión</strong> debajo del botón <strong>Enviar</strong> en el formulario web. Luego, cierra el formulario web y vuelve a abrirlo. A continuación, se te pedirá que inicies sesión con la otra cuenta.<br><br>Ten en cuenta que el inicio de sesión en el formulario web es independiente de la cuenta con la que has iniciado sesión en KoboToolbox en el mismo navegador. Si no estás seguro de qué cuenta tienes actualmente iniciada desde la interfaz del formulario web, te recomendamos cerrar sesión y volver a iniciarla.
</details>

<br>

<details>
<summary><strong>Parece que faltan datos</strong></summary>
No borres la caché del navegador ni elimines los datos del navegador mientras recolectas datos con formularios web. Borrar la caché <strong>elimina del dispositivo los formularios almacenados, los borradores y los envíos en cola</strong>, y estos datos no pueden recuperarse si aún no se han cargado al servidor de KoboToolbox.
</details>

<br>

<details>
<summary><strong>El navegador no es compatible</strong></summary>
Usa la versión más reciente de un navegador moderno. En general, se recomienda Chrome para trabajar con formularios web, aunque Safari, Firefox, Edge, Opera, Samsung Internet y otros navegadores también son compatibles. Internet Explorer no es compatible.
</details>

<br>

<details>
<summary><strong>El envío del formulario web falla</strong></summary>
Si el envío de un formulario web falla, verifica si tu formulario usa un <strong>término reservado de XLSForm</strong> como <a href="https://support.kobotoolbox.org/es/glossary.html#data-column-name">nombre de columna de datos</a>. Las palabras reservadas son términos que no pueden usarse como nombres de variables porque el motor XForms subyacente los utiliza para estructura, lógica o análisis de datos (por ejemplo, type, label, start, today). El uso de estas palabras puede causar errores de validación del formulario, fallos en la publicación o problemas en la exportación de datos.<br><br>

Para solucionar el problema, cambia el nombre de la pregunta afectada por un valor diferente y luego vuelve a implementar el formulario. Este problema suele afectar a los formularios web incluso cuando el formulario se abre con normalidad, mientras que KoboCollect puede seguir funcionando correctamente. Ten en cuenta que los envíos ya guardados con la versión anterior del formulario pueden quedar sin posibilidad de enviarse, por lo que es importante actualizar el formulario lo antes posible si estás recolectando datos a través de formularios web. Siempre <strong>prueba el envío del formulario antes de iniciar la recolección de datos</strong> para detectar problemas de nomenclatura a tiempo.
</details>

<br>