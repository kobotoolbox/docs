# Personalizar la configuración de KoboCollect
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/b2f0bf10348744a1576080786c7c44eff0dafa1c/source/kobocollect_settings.md" class="reference">24 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/Qeky3aomiWI?si=M1l_jorFQEDacX2A&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect es una aplicación gratuita y de código abierto de KoboToolbox diseñada para la recolección de datos en dispositivos móviles Android. Antes de comenzar, [instala y configura](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html) la aplicación KoboCollect. Una vez instalada y configurada, puedes personalizar la aplicación según las necesidades de tu proyecto o usuario. La configuración del proyecto te permite:

- Ajustar la **interfaz de usuario** (p. ej., idioma, tamaño de fuente, tema)
- Configurar los **ajustes del mapa** para preguntas basadas en ubicación
- Gestionar cómo se manejan los formularios (p. ej., envío automático, finalización, reglas de edición)
- Establecer la identidad del **usuario y del dispositivo** para el seguimiento de envíos
- Proteger el acceso a la aplicación y su configuración con **contraseñas o controles de administrador**

Para acceder al menú de configuración:

1. Toca el **ícono del proyecto** en la esquina superior derecha de la pantalla.
2. Toca **Ajustes**.

<p class="note">
  <strong>Nota:</strong> Los usuarios no necesitan conexión a internet para acceder o cambiar la configuración del proyecto en KoboCollect.
</p>

## Configuración de visualización del proyecto
En la aplicación KoboCollect, puedes [conectarte a múltiples cuentas de KoboToolbox](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html#setting-up-multiple-projects-in-kobocollect). Las cuentas de usuario se denominan **Proyectos** en KoboCollect.

Para personalizar cómo se muestra cada proyecto y facilitar su reconocimiento y cambio, puedes editar la configuración de **visualización del proyecto**. Estos cambios solo afectan cómo aparece el proyecto en la interfaz del dispositivo y no afectan los datos ni otros dispositivos.

| **Configuración**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Nombre del proyecto              | Asigna un nombre distintivo a tu proyecto de KoboCollect.                                  |
| Ícono del proyecto      | Cambia la letra que aparece en el círculo de la esquina superior derecha.                                  |
| Color del proyecto           | Cambia el color del círculo de la esquina superior derecha.            |

## Configuración de la interfaz de usuario

La configuración de la interfaz de usuario te permite ajustar la apariencia, el idioma y el tamaño del texto de la aplicación para mejorar la legibilidad.

| **Configuración**    | **Descripción** |
| :----------------- | :--------------------------------------------- |
| Tema  | Elige entre la apariencia clara, oscura o la predeterminada del sistema para la aplicación. |
| Idioma      | Establece el idioma para la visualización de la interfaz de la aplicación. De forma predeterminada, KoboCollect utiliza el idioma del dispositivo.|
| Tamaño de fuente del texto           | Ajusta el tamaño del texto para mejorar la legibilidad.            |
| Navegación           | Personaliza cómo te desplazas por los formularios. Elige entre deslizamientos horizontales, botones de avance/retroceso o un diseño combinado. |


<p class="note">
    <strong>Nota:</strong> Cambiar el idioma solo establece el idioma para la interfaz de usuario de la aplicación, no para el formulario. En formularios con <a href="https://support.kobotoolbox.org/es/language_dashboard.html">múltiples idiomas</a>, el idioma del formulario se establece durante la entrada de datos.
</p>

## Configuración del mapa

La configuración del mapa define la visualización y el comportamiento de los mapas dentro de la aplicación para preguntas basadas en ubicación.

| **Configuración**        | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Fuente   &emsp;&emsp;&emsp;&emsp;            | Define la fuente del mapa. Elige entre Google, OpenStreetMap, USGS o Carto. |
| Estilo del mapa      | Define el estilo del mapa si usas Google Maps, USGS o Carto. |
| Capa           | Selecciona una [capa sin conexión](https://docs.getodk.org/collect-offline-maps/) para los mapas. Puedes agregar opciones seleccionando un archivo MBTiles desde tu dispositivo. |

## Configuración del manejo de formularios

La configuración del manejo de formularios controla cómo se gestionan los formularios dentro de la aplicación, incluyendo las actualizaciones de versiones, los envíos y los comportamientos de entrada de datos.

| **Configuración** | **Descripción**                  |
| :----------------- | :--------------------------------------------- |
| Modo de actualización de formulario en blanco &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Define si deseas que las nuevas versiones de los formularios se actualicen automáticamente o de forma manual. Las opciones incluyen: <ul><li><strong>Manual</strong>: El modo predeterminado, en el que los encuestadores gestionan manualmente la actualización de los formularios.</li><li><strong>Solo formularios descargados previamente</strong>: Cuando uno o más formularios descargados anteriormente en el dispositivo tienen una actualización disponible, se actualizan automáticamente (si la opción <strong>Descarga automática</strong> está activada) o se notifica a los usuarios de las actualizaciones disponibles.</li><li><strong>Coincidencia exacta de servidor</strong>: Todos los formularios compartidos con la cuenta se descargan y actualizan automáticamente según los cambios en el servidor.</li></ul> |
| Frecuencia de actualización automática      | Especifica con qué frecuencia KoboCollect debe buscar actualizaciones de los formularios en el servidor cuando se usa **Solo formularios descargados previamente** o **Coincidencia exacta de servidor**. |
| Descarga automática | Cuando se selecciona **Solo formularios descargados previamente**, puedes elegir si los formularios se actualizan automáticamente. De lo contrario, los usuarios solo recibirán notificaciones de las actualizaciones disponibles.<br><br>Esta configuración se activa automáticamente cuando se selecciona **Coincidencia exacta de servidor**.  |
| Ocultar versiones antiguas del formulario           | Si hay varias versiones del mismo formulario, solo se mostrará la descargada más recientemente al iniciar un nuevo formulario. |
| Envío automático           | Cuando está activado, los formularios se envían al servidor inmediatamente al finalizarlos, si el dispositivo puede conectarse a internet. Si no hay conexión a internet en el momento de la finalización, los formularios finalizados se pondrán en cola para enviarse en cuanto se establezca la conectividad. Puedes especificar si enviar por WiFi, datos móviles o ambos. |
| Eliminar después de enviar         | Elimina los formularios finalizados y los archivos multimedia del dispositivo después de enviarlos correctamente al servidor. |
| Procesamiento de restricciones | Cuando tus formularios incluyen restricciones (criterios de validación), elige entre validar las respuestas al pasar a la siguiente página o al final del formulario. |
| Video de alta resolución        | Activa o desactiva las grabaciones de video de alta resolución al tomar videos a través de la aplicación. |
| Tamaño de imagen      | Define el tamaño de imagen preferido, desde muy pequeño hasta grande. Esto puede ayudar a conservar espacio de almacenamiento en el servidor. |
| Mostrar orientación para las preguntas         | Define cómo se deben mostrar las [sugerencias adicionales](https://support.kobotoolbox.org/es/question_options.html#guidance-hint) dentro del formulario. |
| Usar aplicación externa para grabación de audio        | De forma predeterminada, se usa una grabadora interna para la grabación de audio. Activa esta configuración para usar una aplicación de audio externa en su lugar. |
| Finalizar formularios al importar            | Cuando está activado, los formularios que se incorporan a KoboCollect desde fuera de la aplicación (p. ej., copiados desde el almacenamiento del dispositivo o una tarjeta SD) se marcan automáticamente como <strong>Finalizados</strong>, por lo que están listos para enviar sin necesidad de finalizarlos manualmente. |


<p class="note">
    <strong>Nota:</strong> Se recomienda configurar los proyectos con <strong>actualizaciones automáticas de formularios</strong> en proyectos con ediciones frecuentes de formularios o con <a href="https://support.kobotoolbox.org/es/dynamic_data_attachment_formbuilder.html">conexión dinámica de proyectos</a>. Esto elimina la necesidad de descargar manualmente las actualizaciones de formularios. Sin embargo, las actualizaciones automáticas más frecuentes agotarán la batería del dispositivo más rápidamente.
</p>

## Configuración de identidad del usuario y del dispositivo

La configuración de identidad del usuario y del dispositivo te permite establecer metadatos del dispositivo para el seguimiento de envíos.

| **Configuración**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Metadatos del formulario  &emsp;&emsp;             | Ingresa un <strong>nombre de usuario</strong>, <strong>número de teléfono</strong> y <strong>correo electrónico</strong>, y consulta el <strong>ID del dispositivo</strong> (definido automáticamente) para proporcionar detalles adicionales sobre quién envió los registros al servidor. Estos detalles pueden ayudar a validar la calidad de los datos recolectados por el equipo. |
| Recolectar datos de uso anónimos      | Permite al equipo de KoboToolbox recolectar datos de uso anónimos para ayudarnos a priorizar correcciones y funcionalidades. |

## Establecer contraseña de administrador

Establece una contraseña de administrador en la aplicación KoboCollect para limitar el acceso al menú de configuración **Protegida** solo a los miembros del equipo que tengan la contraseña de administrador. Esto puede ayudar a evitar que los recolectores de datos modifiquen la configuración en el campo.

Para eliminar la contraseña de administrador, haz clic en **Establecer contraseña de administrador**, deja el campo en blanco y haz clic en **OK**.

## Gestión del proyecto

La configuración de gestión del proyecto proporciona herramientas para gestionar y restablecer la configuración relacionada con el proyecto en tu dispositivo, incluyendo la reconfiguración de ajustes, el restablecimiento de datos específicos o la eliminación de todos los datos del proyecto.

| **Configuración**&emsp;&emsp;&emsp;    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Volver a configurar con código QR &emsp;&emsp; | Reconfigura la configuración de KoboCollect escaneando un código QR de otro proyecto. Ten en cuenta que este método reemplazará el proyecto actual por el nuevo. Aquí también puedes encontrar el código QR para [configurar otro dispositivo](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) con la misma configuración. |
| Restablecer | Restablece configuraciones específicas, como borrar [formularios guardados](https://support.kobotoolbox.org/es/glossary.html#saved-forms-kobocollect), datos en caché o capas de mapa, sin afectar otras partes de la aplicación. |
| Eliminar | Elimina el proyecto y todos los datos relacionados con él del dispositivo, incluyendo [formularios en blanco](https://support.kobotoolbox.org/es/glossary.html#blank-forms-kobocollect), formularios enviados, formularios finalizados y borradores, lo que puede ser útil al retirar un dispositivo o prepararlo para un nuevo usuario. |

<p class="note"> 
    <strong>Nota:</strong> Usa estas opciones con precaución, especialmente al eliminar datos, ya que algunas acciones no se pueden deshacer. Eliminar datos del dispositivo no afecta el proyecto general de KoboToolbox y <strong>no elimina los datos que ya se han enviado al servidor</strong>, pero sí elimina los envíos no enviados o en borrador.
</p>

## Control de acceso

Este menú te permite ocultar o restringir partes de la interfaz de la aplicación, lo que te ayuda a personalizar la aplicación según el rol del usuario (p. ej., encuestador vs. supervisor). Esto simplifica la aplicación y evita cambios no autorizados.

| **Configuración**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Configuración del menú principal | Oculta o muestra las opciones del menú principal (p. ej., **Descargar formulario** o **Borrar formulario**). |
| Configuración del usuario | Oculta o muestra la configuración general (p. ej., cambiar el servidor o la identidad del usuario). |
| Configuración de entrada de formularios | Oculta o muestra la configuración de entrada de formularios (p. ej., permitir la navegación hacia atrás, editar formularios guardados). |

Usa las casillas de verificación para activar o desactivar botones y configuraciones específicos. Una vez configurado, agregar una [contraseña de administrador](#set-admin-password) puede evitar cambios no autorizados.