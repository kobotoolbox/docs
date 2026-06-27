# Recolección de datos con KoboCollect
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/883b3a06b2cb3ea94f7a7b69c5be2b85953ad453/source/data_collection_kobocollect.md" class="reference">24 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/IEm61fpLoz4?si=TdlWhcVt0OxETlxl&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect es una aplicación gratuita y de código abierto de KoboToolbox diseñada para la recolección de datos en dispositivos móviles. Es la mejor opción para equipos de encuestadores que trabajan en terreno con teléfonos o tabletas Android, especialmente cuando es necesario recolectar datos sin conexión a internet.

Antes de comenzar, debes [instalar y configurar](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html) la aplicación KoboCollect. Una vez configurada, KoboCollect te permite completar y enviar formularios desde tu dispositivo móvil, incluso sin conexión a internet.

Este artículo explica cómo usar KoboCollect para la recolección de datos, incluyendo la descarga de formularios, cómo completar y editar envíos, enviar formularios finalizados, eliminar formularios guardados o en blanco, y resolver problemas comunes.

<p class="note">
Para obtener más información sobre la aplicación KoboCollect y los dispositivos recomendados, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html">Configuración de la aplicación KoboCollect</a>.
</p>

## Descargar formularios

Para comenzar la recolección de datos con KoboCollect, debes descargar los formularios KoboToolbox en tu dispositivo. Antes de descargar, asegúrate de tener:

- Al menos un [formulario implementado](https://support.kobotoolbox.org/es/deploy_form_new_project.html) en tu cuenta de KoboToolbox (ya sea de tu propiedad o compartido contigo).
- Un proyecto (cuenta) [configurado en KoboCollect](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html).
- Una conexión a internet en tu dispositivo.

Para descargar formularios en tu dispositivo:
- Desde el menú principal, haz clic en **Download form** (Descargar formulario).
- Selecciona los formularios que deseas descargar individualmente tocando la casilla junto a cada formulario, o toca **Select All** (Seleccionar todo) para descargar todos los formularios implementados.
- Toca **Get Selected** (Obtener los Seleccionados).

Los formularios descargados aparecerán cuando hagas clic en **Start new form** (Iniciar nuevo formulario) desde el menú principal de la aplicación.

<p class="note">
  <strong>Nota:</strong> 
Si tu proyecto está configurado para <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">descargas automáticas de formularios</a> con la opción <strong>Exactly match server</strong> (Coincidencia exacta de servidor), todos los formularios compartidos con la cuenta se descargan automáticamente en el dispositivo, por lo que no es necesario realizar el paso anterior.
</p>

## Obtener actualizaciones de formularios

Cuando se realizan cambios en un formulario de recolección de datos, debes obtener las actualizaciones en KoboCollect **mientras estás conectado a internet.** El método para obtener las actualizaciones depende de la [configuración del proyecto](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings).

| Configuración | Obtener actualizaciones de formularios |
|:---|:---|
| Configuración predeterminada | Descarga las nuevas versiones de un formulario haciendo clic en **Download form** (Descargar formulario), seleccionando los formularios a actualizar y haciendo clic en **Get Selected** (Obtener los Seleccionados). |
| Solo formularios descargados previamente | Las actualizaciones se descargarán automáticamente con la frecuencia configurada en los ajustes del proyecto.<br><br>Para forzar una actualización y asegurarte de usar la versión más reciente, haz clic en **Download form** (Descargar formulario), selecciona los formularios a actualizar y haz clic en **Get Selected** (Obtener los Seleccionados). |
| Coincidencia exacta de servidor | Las actualizaciones se descargarán automáticamente con la frecuencia configurada en los ajustes del proyecto.<br><br>Para forzar una actualización y asegurarte de usar la versión más reciente, haz clic en **Start new form** (Iniciar nuevo formulario) y luego haz clic en el botón de actualizar en la esquina superior derecha. |

<p class="note">
  <strong>Nota:</strong> 
Si anticipas actualizaciones frecuentes de formularios o usas <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">conexión dinámica de proyectos</a>, que requiere actualizaciones periódicas del formulario para obtener datos del formulario primario, te recomendamos activar las <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">descargas automáticas de formularios</a>.
</p>

## Recolectar datos

Una vez descargados los formularios, puedes comenzar la recolección de datos. Ten en cuenta que, una vez descargados los formularios en la aplicación, no necesitas conexión a internet para recolectar datos.

1. Desde el menú principal, toca **Start new form** (Iniciar nuevo formulario).
2. Selecciona el formulario con el que deseas recolectar datos.
3. Para cambiar el idioma del formulario, toca el <i class="k-icon-more"></i> **ícono de tres puntos** en la esquina superior derecha de la pantalla y haz clic en **Change Language** (Cambiar idioma).
4. Navega por las preguntas deslizando hacia la izquierda o haciendo clic en **NEXT** (SIG.) después de responder.
5. Al final de la encuesta, puedes elegir **Save as draft** (Guardar como borrador), **Finalize** (Finalizar) o **Send** (Enviar) el formulario (según la [configuración de tu proyecto](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings)).

| **Opción** | **Descripción** |
| :----------------- | :--------------------------------------------- |
| Save as draft (Guardar como borrador) &emsp;&emsp;&emsp; | El formulario se guardará en **Drafts** (Borradores) y aún podrá editarse antes de finalizarlo. |
| Finalize (Finalizar) | El formulario se guardará en **Ready to send** (Listo para enviar) y ya no podrá editarse. Esta opción aparece solo si el ajuste **Auto send** (Envío automático) está configurado como **Off** (Desactivado). |
| Send (Enviar) | El formulario se enviará directamente al servidor o se pondrá en cola hasta que haya conexión a internet disponible. Ya no podrá editarse. Esta opción aparece solo si el ajuste **Auto send** (Envío automático) está activado. |

De forma predeterminada, los formularios y los datos permanecen en el dispositivo hasta que se eliminan manualmente. Si activas **Delete after send** (Eliminar después de enviar) en la [configuración del proyecto](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings), los formularios se eliminarán automáticamente una vez enviados al servidor.

## Editar borradores

Si guardaste una encuesta como borrador, puedes editarla antes de enviarla al servidor:

1. Desde el menú principal, selecciona **Drafts** (Borradores).
2. Aparecerá una lista de los formularios guardados como borrador. Selecciona el que deseas editar.
3. Realiza los cambios necesarios y luego toca **Finalize** (Finalizar) o **Send** (Enviar), según tu flujo de trabajo.

<p class="note">
  <strong>Nota:</strong> No necesitas conexión a internet para editar un formulario guardado en KoboCollect.
</p>

## Enviar formularios finalizados al servidor

Después de finalizar tus formularios, debes cargarlos al servidor de KoboToolbox. Los formularios suelen completarse y finalizarse sin conexión a internet, y luego cargarse en bloque cuando hay conexión disponible. Para enviar tus formularios al servidor de KoboToolbox:

1. Asegúrate de que el dispositivo tenga una conexión a internet segura.
2. Desde el menú principal, toca **Ready to send** (Listo para enviar). Aparecerá una lista de los formularios finalizados.
3. Toca **Select All** (Seleccionar todo) o selecciona manualmente los formularios que deseas cargar marcando la casilla correspondiente.
4. Toca **Send Selected** (Enviar seleccionado) para enviar los formularios al servidor.

Para verificar que la carga fue exitosa, ve al menú principal y selecciona **Sent** (Enviado). Verás todos los formularios enviados al servidor, junto con su fecha de sincronización.

<p class="note">
  <strong>Nota:</strong> Si tu proyecto está <strong>configurado para enviar automáticamente los formularios finalizados</strong>, la página <strong>Ready to send</strong> (Listo para enviar) no aparecerá en el menú principal y puedes omitir estos pasos. Para obtener más información sobre la configuración del proyecto en KoboCollect, consulta <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html">Personalizar la configuración de KoboCollect</a>.
</p>

## Eliminar formularios guardados y formularios en blanco

Después de finalizar la recolección de datos y cargar todos los formularios completados al servidor, es posible que quieras eliminar los datos de formularios restantes de la aplicación KoboCollect, a menos que la eliminación automática ya esté [activada](https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings) en tu dispositivo. Esto ayuda a proteger la privacidad de los datos y evita confusiones al recolectar datos para un nuevo proyecto.

Hay dos tipos de formularios que se pueden eliminar:

- **Saved Forms (Formularios guardados)**: Son [formularios en los que se han ingresado datos](https://support.kobotoolbox.org/es/glossary.html#saved-forms-kobocollect), incluyendo borradores, formularios finalizados y formularios que ya han sido enviados al servidor.
- **Blank Forms (Formularios en blanco)**: Son [formularios de recolección de datos vacíos](https://support.kobotoolbox.org/es/glossary.html#blank-forms-kobocollect) que se han descargado en el dispositivo desde la página **Download form** (Descargar formulario). Elimina estos formularios solo cuando haya terminado la recolección de datos correspondiente.

Para eliminar formularios:
1. Desde el menú principal, toca **Delete form** (Borrar formulario). Verás dos pestañas.
2. En **Saved Forms** (Formularios guardados):
    - Toca **Select All** (Seleccionar todo) para eliminar todos los formularios guardados, o selecciona formularios individuales.
    - Toca **Delete Selected** (Eliminar lo seleccionado).
3. En **Blank Forms** (Formularios en blanco):
    - Toca **Select All** (Seleccionar todo) para eliminar todos los formularios en blanco, o selecciona formularios individuales.
    - Toca **Delete Selected** (Eliminar lo seleccionado).

<p class="note">
  <strong>Nota:</strong> No necesitas conexión a internet para eliminar formularios en KoboCollect. Sin embargo, si los formularios en blanco se eliminan accidentalmente sin conexión, se necesita una conexión a internet para recuperarlos y continuar con la recolección de datos. Para evitar eliminaciones accidentales, puedes establecer controles de acceso en la <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#access-control">configuración del proyecto</a>.
</p>

## Resolución de problemas

<details>
<summary><strong>La descarga del formulario tarda demasiado en cargar</strong></summary>
Si la página <strong>Download form</strong> (Descargar formulario) tarda mucho en conectarse al servidor o en cargar los formularios disponibles para descargar, es posible que tu cuenta de KoboToolbox tenga demasiados formularios activos o que tu conexión a internet sea débil.
<br><br>
Prueba lo siguiente:
<br>
<ul>
<li>Archiva los formularios que ya no estén en uso para reducir la cantidad de formularios que KoboCollect necesita cargar.</li>
<li>Verifica que tu conexión a internet sea estable y vuelve a intentarlo.</li>
</ul>
</details>

<br>

<details>
<summary><strong>KoboCollect muestra una versión antigua del formulario</strong></summary>
Si KoboCollect muestra una versión anterior de tu formulario, descarga el formulario nuevamente para obtener la última versión implementada. También puedes activar las <a href="https://support.kobotoolbox.org/es/kobocollect_settings.html#form-management-settings">actualizaciones automáticas de formularios</a> en KoboCollect para que la aplicación busque versiones más recientes al conectarse al servidor.
</details>

<br>

<details>
<summary><strong>Error evaluating field […] XPath evaluation: type mismatch. This field is repeated</strong></summary>
Este error significa que tu formulario usa <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment.html">conexión dinámica de proyectos</a> y que el campo utilizado para vincular los datos del formulario primario y el secundario contiene valores duplicados en los datos del formulario primario. El campo de vinculación debe contener únicamente valores únicos.
<br><br>
Para solucionar esto, elimina o corrige los valores duplicados en el campo de vinculación de los datos del formulario primario, o usa el argumento <code>[position() = 1]</code> en tu cálculo.
</details>

<br>

<details>
<summary><strong>Repeats in 'field-list' groups are not supported</strong></summary>
Este error ocurre en KoboCollect cuando un grupo de repetición está anidado dentro de un grupo más amplio que usa la apariencia <code>field-list</code>. KoboCollect no admite grupos de repetición dentro de grupos con apariencia <code>field-list</code>. Los grupos de repetición deben aparecer en su propia página.
<br><br>
Para resolver este problema, mueve el grupo de repetición fuera del grupo principal o elimina la apariencia <code>field-list</code> del grupo principal.
</details>

<br>

<details>
<summary><strong>Error getting form list</strong></summary>
Si ves "Error getting form list" después de abrir <strong>Download form</strong> (Descargar formulario), primero verifica que la URL del servidor de KoboToolbox en KoboCollect sea correcta. Un pequeño error tipográfico en la URL es una causa común de este error.
<br><br>
Asegúrate también de que el dispositivo esté conectado a internet. En algunos casos, el dispositivo puede parecer conectado a una red Wi-Fi pero aún requerir que inicies sesión a través de un navegador antes de que el acceso a internet esté disponible.
</details>

<br>

<details>
<summary><strong>Errores de conexión segura</strong></summary>
Es posible que veas un error como "Generic Exception: No peer certificate", "Form listing failed" o <code>SSLPeerUnverifiedException</code> cuando KoboCollect no puede establecer una conexión segura con el servidor.
<br><br>
La causa más común es que la fecha del dispositivo sea incorrecta. Verifica la configuración de fecha y hora del teléfono o tableta y vuelve a intentarlo. Esto puede ocurrir si la batería del dispositivo se agotó por completo y la fecha se restableció.
<br><br>
Este error también puede aparecer cuando se usa una red Wi-Fi o punto de acceso que requiere iniciar sesión a través de un navegador antes de permitir el acceso a internet.
</details>

<br>

<details>
<summary><strong>Unable to edit this blank form because the corresponding blank form is not present or was deleted</strong></summary>
Este error aparece cuando intentas editar un <a href="https://support.kobotoolbox.org/es/glossary.html#saved-forms-kobocollect">formulario guardado</a>, pero el <a href="https://support.kobotoolbox.org/es/glossary.html#blank-forms-kobocollect">formulario en blanco</a> original ya no está disponible en el dispositivo.
<br><br>
Para solucionar esto, descarga nuevamente el formulario en blanco. Después de eso, deberías poder volver a abrir y continuar editando el formulario guardado.
</details>

<br>

<details>
<summary><strong>Sin acceso a internet en ningún momento</strong></summary>
Si los dispositivos de campo no pueden acceder a internet en ningún momento, los envíos de KoboCollect aún pueden transferirse manualmente desde el dispositivo a un computador usando <a href="https://docs.getodk.org/briefcase-intro">herramientas externas</a> y una conexión USB. En configuraciones más avanzadas, también es posible <a href="https://github.com/kobotoolbox/kobo-install">ejecutar KoboToolbox localmente</a> en un computador y conectar dispositivos a él a través de una red local sin acceso a internet.
<br><br>
Estos enfoques son menos comunes y requieren una configuración adicional, por lo que generalmente son más adecuados para flujos de trabajo especializados.
</details>