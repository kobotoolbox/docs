# Personalizar los ajustes de KoboCollect
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/5599bf9bc43c6872244104e236df84c6a6ed5f15/source/kobocollect_settings.md" class="reference">19 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/Qeky3aomiWI?si=M1l_jorFQEDacX2A" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboCollect es una aplicación gratuita y de código abierto de KoboToolbox diseñada para la recolección de datos en dispositivos móviles Android. Antes de comenzar, [instala y configura](kobocollect_on_android_latest.md) la aplicación de KoboCollect. Una vez instalada y configurada, puedes personalizar la aplicación según las necesidades de tu proyecto o usuario/a. Los ajustes del proyecto te permiten:

- Ajustar la **interfaz de usuario/a** (por ejemplo, idioma, tamaño de fuente, tema)
- Configurar los **ajustes del mapa** para preguntas basadas en ubicación
- Gestionar cómo se manejan los formularios (por ejemplo, envío automático, finalizar, reglas de edición)
- Establecer la **identidad del usuario/a y del dispositivo** para rastrear los envíos
- Proteger el acceso a la aplicación y sus ajustes con **contraseñas o controles de administrador/a**
  
Para acceder al menú de ajustes:

1. Toca el **ícono de Proyecto** en la esquina superior derecha de tu pantalla.
2. Toca **Ajustes**.

<p class="note">
  <strong>Nota:</strong> Los/as usuarios/as no necesitan una conexión a Internet para acceder o cambiar los ajustes del proyecto en KoboCollect.
</p>

## Ajustes de visualización del proyecto
En la aplicación de KoboCollect, puedes [conectarte a múltiples cuentas de KoboToolbox](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html#setting-up-multiple-projects-in-kobocollect). Las cuentas de usuario/a se llaman **Proyectos** en KoboCollect. 

Para personalizar cómo se muestra cada proyecto para facilitar el reconocimiento y el cambio entre ellos, puedes editar los ajustes de **visualización del proyecto**. Estos cambios solo afectan cómo aparece el proyecto en la interfaz del dispositivo y no afectan los datos ni otros dispositivos.

| **Ajuste**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Nombre del proyecto              | Dale un nombre distintivo a tu proyecto de KoboCollect.                                  |
| Ícono del proyecto      | Cambia la letra que aparece en el círculo superior derecho.                                  |
| Color del proyecto           | Cambia el color del círculo superior derecho.            |

## Ajustes de interfaz de usuario/a

Los ajustes de interfaz de usuario/a te permiten ajustar la apariencia de la aplicación, el idioma y el tamaño del texto para una mejor legibilidad.

| **Ajuste**    | **Descripción** |
| :----------------- | :--------------------------------------------- |
| Tema  | Elige entre apariencia clara, oscura o predeterminada del sistema para la aplicación. |
| Idioma      | Establece el idioma para la visualización de la interfaz de la aplicación. Por defecto, KoboCollect coincide con el idioma del dispositivo.|
| Tamaño de fuente del texto           | Ajusta el tamaño del texto para una mejor legibilidad.            |
| Navegación           | Personaliza cómo te mueves a través de los formularios. Elige entre deslizamientos horizontales, botones adelante/atrás o un diseño combinado. |


<p class="note">
    <strong>Nota:</strong> Cambiar el idioma solo establece el idioma para la interfaz de usuario/a de la aplicación y no para el formulario. Para formularios con <a href="language_dashboard.html">múltiples idiomas</a>, el idioma del formulario se establece durante la entrada de datos.
</p>

## Ajustes de mapas

Los ajustes de mapas configuran la visualización y el comportamiento de los mapas dentro de la aplicación para preguntas basadas en ubicación.

| **Ajuste**        | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Fuente   &emsp;&emsp;&emsp;&emsp;            | Define tu fuente de mapa. Elige entre Google, OpenStreetMap, USGS o Carto. |
| Estilo de mapa      | Define tu estilo de mapa si usas Google Maps, USGS o Carto. |
| Capa           | Selecciona una capa sin conexión para los mapas. Puedes agregar opciones seleccionando un archivo MBTiles de tu dispositivo. |

## Ajustes de manejo de formularios

Los ajustes de manejo de formularios controlan cómo se manejan los formularios dentro de la aplicación, incluyendo actualizaciones de versión de formularios, envíos y comportamientos de entrada de datos. 

| **Ajuste** | **Descripción**                  |
| :----------------- | :--------------------------------------------- |
| Modo de actualización de formulario en blanco &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;              | Define si deseas que las nuevas versiones de los formularios se actualicen automática o manualmente. Las opciones incluyen: <ul><li><strong>Manual</strong>: El modo predeterminado, en el cual los/as encuestadores/as gestionan manualmente la actualización de formularios.</li><li><strong>Solo formularios descargados previamente</strong>: Los/as encuestadores/as reciben una notificación cuando uno o más formularios descargados previamente en el dispositivo tienen una actualización disponible.</li><li><strong>Coincidir exactamente con el servidor</strong>: Todos los formularios compartidos con la cuenta se descargan y actualizan automáticamente según los cambios en el servidor.</li></ul> |
| Frecuencia de actualización automática      | Especifica con qué frecuencia KoboCollect debe verificar actualizaciones de formularios en el servidor cuando se usa **Solo formularios descargados previamente** o **Coincidir exactamente con el servidor**. |
| Descarga automática | Cuando se selecciona **Solo formularios descargados previamente**, puedes elegir si los formularios se actualizan automáticamente. De lo contrario, los/as usuarios/as solo serán notificados/as de las actualizaciones disponibles.<br><br>Este ajuste se habilita automáticamente cuando se selecciona **Coincidir exactamente con el servidor**.  |
| Ocultar versiones antiguas de formularios           | Si hay múltiples versiones del mismo formulario, solo se mostrará la descargada más recientemente al iniciar un nuevo formulario. |
| Envío automático           | Cuando está habilitado, los formularios se envían al servidor inmediatamente cuando se finalizan, si el dispositivo puede conectarse a Internet. Si no hay conexión a Internet disponible en el momento de la finalización, tus formularios finalizados se pondrán en cola para enviarse tan pronto como se establezca la conectividad. Puedes especificar si enviar por WiFi, datos móviles o ambos. |
| Eliminar después de enviar         | Elimina los formularios finalizados y los medios del dispositivo después de enviarlos exitosamente al servidor. |
| Procesamiento de restricciones | Cuando tus formularios incluyen restricciones (criterios de validación), elige entre validar respuestas al pasar a la siguiente página o al final del formulario. |
| Video de alta resolución        | Habilita o deshabilita las grabaciones de video de alta resolución al tomar videos a través de la aplicación. |
| Tamaño de imagen      | Define el tamaño de imagen preferido, desde muy pequeño hasta grande. Esto puede ayudar a conservar espacio de almacenamiento en el servidor. |
| Mostrar orientación para preguntas         | Define cómo deben mostrarse las [sugerencias de orientación](https://support.kobotoolbox.org/es/question_options.html?highlight=guidance+hint#guidance-hint-optional) dentro de tu formulario. |
| Usar aplicación externa para grabación de audio        | Por defecto, se usa una grabadora interna para la grabación de audio. Habilita este ajuste para usar una aplicación de audio externa en su lugar. |
| Finalizar formularios al importar            | Cuando está habilitado, los formularios que se traen a KoboCollect desde fuera de la aplicación (por ejemplo, copiados desde el almacenamiento del dispositivo o tarjeta SD) se marcan automáticamente como <strong>Finalizados</strong>, por lo que están listos para enviar sin requerir finalización manual. |


<p class="note">
    <strong>Nota:</strong> Se recomienda configurar proyectos para <strong>actualizaciones automáticas de formularios</strong> en proyectos con ediciones frecuentes de formularios o <a href="dynamic_data_attachment.html">archivos adjuntos de datos dinámicos</a>. Esto elimina la necesidad de descargar manualmente las actualizaciones de formularios. Sin embargo, las actualizaciones automáticas más frecuentes agotarán la batería de tu dispositivo más rápidamente.
</p>

## Ajustes de identidad de usuario/a y dispositivo

Los ajustes de identidad de usuario/a y dispositivo te permiten establecer metadatos del dispositivo para rastrear los envíos.

| **Ajuste**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Metadatos del formulario  &emsp;&emsp;             | Ingresa un <strong>nombre de usuario/a</strong>, <strong>número de teléfono</strong> y <strong>dirección de correo electrónico</strong>, y visualiza el <strong>id del dispositivo</strong> (definido automáticamente) para proporcionar detalles adicionales sobre quién envió los registros al servidor. Estos detalles pueden ayudar a validar la calidad de los datos recolectados por el equipo. |
| Recolectar datos de uso anónimos      | Permite al equipo de KoboToolbox recolectar datos de uso anónimos para ayudarnos a priorizar correcciones y funcionalidades. |

## Establecer contraseña de administrador/a

Establece una contraseña de administrador/a en la aplicación de KoboCollect, limitando el acceso al menú de ajustes **Protegidos** solo a los/as miembros/as del equipo con la contraseña de administrador/a. Esto puede ayudar a prevenir que los/as recolectores/as de datos modifiquen los ajustes en el campo.

Para eliminar la contraseña de administrador/a, haz clic en **Establecer contraseña de administrador/a**, deja el campo en blanco y haz clic en **OK**. 

## Manejo del proyecto

Los ajustes de manejo del proyecto proporcionan herramientas para gestionar y restablecer los ajustes relacionados con el proyecto en tu dispositivo, incluyendo reconfigurar ajustes, restablecer datos específicos o eliminar todos los datos del proyecto.

| **Ajuste**&emsp;&emsp;&emsp;    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
|Reconfigurar con código QR &emsp;&emsp; | Reconfigura tus ajustes de KoboCollect escaneando un código QR de otro proyecto. Ten en cuenta que este enfoque reemplazará el proyecto actual con el nuevo. Aquí también puedes encontrar el código QR para [configurar otro dispositivo](https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html#setting-up-kobocollect-with-a-qr-code) con los mismos ajustes. |
| Restablecer | Restablece ajustes específicos, como borrar formularios guardados, datos en caché o capas de mapas, sin afectar otras partes de la aplicación. |
| Eliminar | Elimina todos los datos relacionados con el proyecto del dispositivo, incluyendo formularios en blanco, datos enviados y ajustes, lo cual puede ser útil al retirar un dispositivo o prepararlo para un/a nuevo/a usuario/a. |

<p class="note"> 
    <strong>Nota:</strong> Usa estas opciones con precaución, especialmente al eliminar datos, ya que algunas acciones no se pueden deshacer. Eliminar datos del dispositivo no afecta el proyecto general de KoboToolbox y no elimina datos del servidor.
</p>

## Control de acceso

Este menú te permite ocultar o restringir partes de la interfaz de la aplicación, ayudándote a personalizar la aplicación según el rol del usuario/a (por ejemplo, encuestador/a vs. supervisor/a). Esto ayuda a simplificar la aplicación y previene cambios no autorizados.

| **Ajuste**    | **Descripción**                                |
| :----------------- | :--------------------------------------------- |
| Ajustes del Menú Principal | Oculta o muestra las opciones del menú principal (por ejemplo, **Descargar formulario** o **Borrar formulario**). |
| Ajustes de Usuario/a | Oculta o muestra los ajustes generales (por ejemplo, cambiar servidor o identidad de usuario/a). |
| Ajustes de Entrada de Formulario | Oculta o muestra los ajustes de entrada de formulario (por ejemplo, permitir navegación hacia atrás, editar formularios guardados). |

Usa las casillas de verificación para habilitar o deshabilitar botones y ajustes específicos. Una vez configurado, agregar una [contraseña de administrador/a](#establecer-contraseña-de-administradora) puede prevenir cambios no autorizados.