# Compartir proyectos con configuraciones a nivel de proyecto
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/bf5d17e0a4c3d4eec5dd2a353ea3afabe5da71a5/source/project_sharing_settings.md" class="reference">9 abr 2026</a>


<iframe src="https://www.youtube.com/embed/vRuAan0aSfY?si=FbKeyjF9XitYdUWC&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox te permite personalizar la configuración para compartir según las necesidades del proyecto. Este artículo explica los **controles de privacidad y uso compartido a nivel de proyecto** de KoboToolbox, incluido permitir envíos sin autenticación, hacer público un proyecto, transferir la propiedad y eliminar proyectos compartidos.

<p class="note">
  Para obtener más información sobre cómo administrar lo que <strong>usuarios específicos</strong> pueden hacer dentro de un proyecto, consulta <a href="https://support.kobotoolbox.org/es/managing_permissions.html">Compartir proyectos con permisos a nivel de usuario/a</a>.
</p>

## Permitir envíos sin autenticación

De forma predeterminada, KoboToolbox requiere un nombre de usuario y una contraseña para enviar datos, gestionar proyectos y acceder a los envíos. Cuando se implementa un nuevo proyecto, se requiere autenticación para acceder al formulario y enviar datos. Solo los usuarios con quienes hayas [compartido el formulario](https://support.kobotoolbox.org/es/managing_permissions.html) y a quienes hayas otorgado el permiso **Añadir envíos** podrán acceder al formulario y enviar datos.

En algunos casos, es posible que desees habilitar la entrada de datos para cualquier persona que tenga la URL. Esto permite que las personas con la URL del formulario envíen datos sin iniciar sesión en una cuenta de KoboToolbox.

Para permitir la entrada de datos a cualquier persona con la URL del formulario:
1. Abre el proyecto en KoboToolbox y ve a la sección **FORMULARIO**
2. En **Recolectar datos**, habilita "Permitir envíos a este formulario sin nombre de usuario ni contraseña".

![Ejemplo de requerir autenticación](images/project_sharing_settings/require_authentication.png)

También puedes cambiar esta configuración yendo a la ventana **Compartir** en la página **CONFIGURACIÓN** de tu proyecto y activando la configuración predeterminada para habilitar "Permitir envíos a este formulario sin nombre de usuario ni contraseña".

<p class="note">
  <strong>Nota:</strong> Configurar formularios para requerir autenticación ahora está disponible como una configuración por proyecto. Esta función de privacidad reemplaza la configuración anterior a nivel de cuenta para "Requerir autenticación para ver formularios y enviar datos". Con esta actualización, los nuevos proyectos requieren autenticación de forma predeterminada. Los proyectos existentes heredan tu configuración anterior a nivel de cuenta tal como estaba en el momento de esta actualización.
</p>

## Hacer público tu proyecto

Además de compartir tu proyecto con usuarios específicos de KoboToolbox, también puedes hacer público tu formulario y/o los datos del proyecto. Para hacer esto:

1. Ve a la página **CONFIGURACIÓN** de tu proyecto de recolección de datos
2. Abre la ventana **Compartir**
3. Selecciona las opciones "Cualquier persona puede ver este formulario" y/o "Cualquier persona puede ver los envíos que se realizan a través de este formulario"

<p class="note">
  <strong>Nota:</strong> Al seleccionar "Cualquier persona puede ver los envíos que se realizan a través de este formulario", la opción "Cualquier persona puede ver este formulario" también se selecciona de forma predeterminada.
</p>

Se mostrará una URL que puedes compartir para proporcionar acceso al formulario y/o a los datos del proyecto sin requerir el inicio de sesión en una cuenta de KoboToolbox. Los usuarios con el enlace podrán realizar las siguientes acciones:

| **Opción**    | **Acciones permitidas**                                |
| :----------------- | :--------------------------------------------- |
| Cualquier persona puede ver este formulario              | <ul><li>Acceder a la página <strong>FORMULARIO</strong></li> <li>Previsualizar el formulario</li> <li>Descargar el formulario como XLS o XML</li></ul> |
| Cualquier persona puede ver los envíos que se realizan a través de este formulario      | <ul><li>Acceder a la página <strong>DATOS</strong></li><li>Ver los datos en la vista de <strong>Tabla</strong></li><li>Ver e imprimir <strong>Informes</strong></li><li>Ver la <strong>Galería</strong></li><li><strong>Descargar</strong> los datos del proyecto</li><li>Ver los datos en la vista de <strong>Mapa</strong></li></ul> |

## Transferir la propiedad de un proyecto

Puedes transferir la propiedad del proyecto de tu cuenta a una cuenta de usuario diferente. Ambas cuentas deben estar en el mismo servidor de KoboToolbox.

Para transferir un proyecto:
1. Ve a la página **CONFIGURACIÓN** de tu proyecto de recolección de datos.
2. Abre la ventana **Compartir**.
3. En la sección **Transferir la propiedad del proyecto**, haz clic en **Transferir**.
4. Ingresa el nombre de usuario de la cuenta a la que deseas transferir el proyecto.
5. Haz clic en **Proyecto de transferencia**.
   
Se enviará un correo electrónico al usuario que recibe el proyecto. Para aceptar la transferencia, el destinatario debe hacer clic en el enlace del correo electrónico mientras está conectado a su cuenta de KoboToolbox. Cuando haga clic en el enlace, se mostrará un cuadro de diálogo de confirmación. El destinatario debe hacer clic en **Aceptar** para que se complete la transferencia del proyecto.

<p class="note">
  <strong>Nota:</strong> Después de aceptar la transferencia, puede tardar unos minutos en completarse. El nuevo propietario del proyecto puede ver el proyecto en su lista de proyectos de inmediato, pero la vista de la tabla de datos puede tardar más en actualizarse.
</p>

## Eliminar proyectos compartidos de tu cuenta

Para eliminar un proyecto que otro usuario compartió contigo:

1. Abre el proyecto y ve a la página **FORMULARIO**.
2. Haz clic en <i class="k-icon-more"></i> **Otras acciones** en la esquina superior derecha.
3. Selecciona **Eliminar proyecto compartido**.
4. Confirma haciendo clic en **ELIMINAR**.

<iframe src="https://www.youtube.com/embed/EZyj0tQXtzA?si=EmE0bahqxFAW2Fqm&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>