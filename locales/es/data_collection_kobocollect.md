# Recolección de datos usando KoboCollect
<a href="../data_collection_kobocollect.html">Read in English</a> | <a href="../fr/data_collection_kobocollect.html">Lire en français</a> | <a href="../ar/data_collection_kobocollect.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/711a8034f16611e23d4ff78183c4e20825abc818/source/data_collection_kobocollect.md" class="reference">19 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/IEm61fpLoz4?si=TdlWhcVt0OxETlxl" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect es una aplicación gratuita y de código abierto de KoboToolbox diseñada para la recolección de datos en dispositivos móviles Android. Antes de comenzar, [instala y configura](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) la aplicación de Android de KoboCollect.

Una vez configurada, KoboCollect te permite completar y enviar formularios desde tu dispositivo móvil, incluso sin conexión. Este artículo explica cómo usar la aplicación para recolectar datos, incluyendo el acceso a formularios, guardar y editar respuestas, y enviar envíos finalizados.

## Descargar formularios

Para comenzar la recolección de datos con KoboCollect, necesitarás descargar el/los formulario(s) de KoboToolbox a tu dispositivo. Antes de descargar, asegúrate de tener:

- Al menos un [formulario desplegado](https://support.kobotoolbox.org/deploy_form_new_project.html) en tu cuenta de KoboToolbox (ya sea de tu propiedad o compartido contigo).
- Un proyecto (cuenta) [configurado en KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html).
- Una conexión a internet en tu dispositivo.
  
Para descargar formularios a tu dispositivo:
- Desde el menú principal, haz clic en **Descargar formulario**.
- Selecciona el/los formulario(s) que deseas descargar individualmente tocando la casilla de verificación junto a cada formulario, o toca **Seleccionar todo** para descargar todos los formularios desplegados.
- Toca **Obtener los Seleccionados**.

Los formularios descargados aparecerán cuando hagas clic en **Iniciar nuevo formulario** desde el menú principal de la aplicación.

<p class="note">
  <strong>Nota:</strong> Necesitarás repetir este proceso cada vez que se realice una actualización al formulario o a los archivos multimedia del formulario. Si anticipas actualizaciones frecuentes del formulario o estás usando <a href="https://support.kobotoolbox.org/dynamic_data_attachment.html">archivos adjuntos de datos dinámicos</a>, recomendamos habilitar las <a href="https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings">descargas automáticas de formularios</a>. 
</p>

## Recolectar datos

Una vez que los formularios estén descargados, puedes comenzar la recolección de datos. Ten en cuenta que una vez que hayas descargado el/los formulario(s) en la aplicación, no necesitas una conexión a internet para recolectar datos.

1. Desde el menú principal, toca **Iniciar nuevo formulario**.
2. Selecciona el formulario con el que deseas recolectar datos.
3. Para cambiar el idioma del formulario, toca el **ícono de tres puntos** <i class="k-icon-more"></i> en la esquina superior derecha de la pantalla y haz clic en **Cambiar idioma**.
4. Navega a través de las preguntas deslizando hacia la izquierda o haciendo clic en **SIG.** después de responder.
5. Al final de la encuesta, puedes elegir **Guardar como borrador**, **Finalizar** o **Enviar** el formulario (dependiendo de la [configuración de tu proyecto](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings)).

| **Opción** | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Guardar como borrador  &emsp;&emsp;&emsp;        | El formulario se guardará en **Borradores** y aún puede ser editado antes de finalizarlo. |
| Finalizar      | El formulario se guardará en **Listo para enviar** y ya no podrá ser editado. Esta opción aparece solo si la configuración **Envío automático** está establecida en **Desactivado**.                                  |
| Enviar           | El formulario se enviará al servidor directamente o se pondrá en cola hasta que haya una conexión a internet disponible. Ya no podrá ser editado. Esta opción aparece solo si la configuración **Envío automático** está habilitada.            |

Por defecto, los formularios y datos permanecen en el dispositivo hasta que se eliminen manualmente. Si habilitas **Eliminar después de enviar** en la [configuración del proyecto](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings), los formularios se eliminarán automáticamente una vez que hayan sido enviados al servidor.

## Editar borradores

Si guardaste una encuesta como borrador, puedes editarla antes de enviarla al servidor:

1. Desde el menú principal, selecciona **Borradores**.
2. Aparecerá una lista de formularios guardados como borradores. Selecciona el que deseas editar.
3. Realiza los cambios necesarios, luego toca **Finalizar** o **Enviar**, dependiendo de tu flujo de trabajo.

<p class="note">
  <strong>Nota:</strong> No necesitas una conexión a internet para editar un formulario guardado en KoboCollect.
</p>

## Enviar formularios finalizados al servidor

Después de finalizar tus formularios, debes subirlos al servidor de KoboToolbox. Los formularios a menudo se completan y finalizan sin conexión, y luego se suben en lote una vez que hay una conexión a internet disponible. Para enviar tus formularios al servidor de KoboToolbox:

1. Asegúrate de que el dispositivo tenga una conexión a internet segura.
2. Desde el menú principal, toca **Listo para enviar**. Aparecerá una lista de formularios finalizados.
3. Toca **Seleccionar todo**, o selecciona manualmente los formularios que deseas subir marcando la casilla de verificación.
4. Toca **Enviar seleccionado** para enviar los formularios al servidor.

Para verificar la carga exitosa, ve al menú principal y selecciona **Enviado**. Verás todos los formularios enviados al servidor, junto con su fecha de sincronización.

<p class="note">
  <strong>Nota:</strong> Si tu proyecto está <strong>configurado para enviar automáticamente los formularios finalizados</strong>, la página <strong>Listo para enviar</strong> no aparecerá en el menú principal, y puedes omitir estos pasos. Para obtener más información sobre la configuración del proyecto en KoboCollect, consulta <a href="https://support.kobotoolbox.org/kobocollect_settings.html">Personalizar la configuración de KoboCollect</a>.
</p>

## Eliminar formularios guardados y formularios en blanco

Después de finalizar la recolección de datos y subir todos los formularios completados al servidor, es posible que desees eliminar los datos de formularios restantes de la aplicación KoboCollect, a menos que la eliminación automática ya esté [habilitada](https://support.kobotoolbox.org/kobocollect_settings.html#form-management-settings) para tu dispositivo. Esto ayuda a proteger la privacidad de los datos y previene confusiones al recolectar datos para un nuevo proyecto.

Hay dos tipos de formularios que se pueden eliminar:

- **Formularios guardados**: Estos son formularios para los cuales se han completado datos, incluyendo borradores, formularios finalizados y formularios que han sido enviados al servidor.
- **Formularios en blanco**: Estos son formularios de recolección de datos vacíos que se han descargado al dispositivo desde la página **Descargar formulario**. Solo elimina estos formularios una vez que haya finalizado la recolección de datos para ellos.
  
Para eliminar formularios:
1. Desde el menú principal, toca **Borrar formulario**. Verás dos pestañas.
2. En **Formularios guardados**:
    - Toca **Seleccionar todo** para eliminar todos los formularios guardados, o selecciona formularios individuales.
    - Toca **Eliminar seleccionados**.
3. En **Formularios en blanco**:
    - Toca **Seleccionar todo** para eliminar todos los formularios en blanco, o selecciona formularios individuales.
    - Toca **Eliminar seleccionados**.

<p class="note">
  <strong>Nota:</strong> No necesitas una conexión a internet para eliminar formularios guardados en KoboCollect. Sin embargo, si los formularios en blanco se eliminan accidentalmente sin conexión, se requiere una conexión a internet para recuperarlos y continuar con la recolección de datos. Para prevenir la eliminación accidental, puedes establecer controles de acceso en la <a href="https://support.kobotoolbox.org/kobocollect_settings.html#access-control">configuración del proyecto</a>.
</p>