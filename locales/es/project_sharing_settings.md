# Compartir proyectos con configuraciones a nivel de proyecto
<a href="../project_sharing_settings.html">Read in English</a> | <a href="../fr/project_sharing_settings.html">Lire en français</a> | <a href="../ar/project_sharing_settings.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/03c0981e6da0be6aec3385dfe68b2ebb0f71b2f8/source/project_sharing_settings.md" class="reference">5 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/vRuAan0aSfY?si=FbKeyjF9XitYdUWC" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox te permite personalizar la configuración de uso compartido según las necesidades del proyecto. Este artículo explica los **controles de privacidad y uso compartido a nivel de proyecto** de KoboToolbox, incluyendo permitir envíos sin autenticación, hacer público un proyecto, transferir la propiedad y eliminar proyectos compartidos.

<p class="note">
  Para obtener más información sobre cómo gestionar lo que <strong>usuarios/as específicos/as</strong> pueden hacer dentro de un proyecto, consulta <a href="https://support.kobotoolbox.org/managing_permissions.html">Compartir tu proyecto con permisos específicos de usuario/a</a>.
</p>

## Permitir envíos sin autenticación

De forma predeterminada, KoboToolbox requiere un nombre de usuario/a y contraseña para enviar datos, gestionar proyectos y acceder a los envíos. Cuando se despliega un nuevo proyecto, se requiere autenticación para acceder al formulario y enviar envíos. Solo los/as usuarios/as con quienes hayas [compartido el formulario](https://support.kobotoolbox.org/managing_permissions.html) y otorgado el permiso **Agregar envíos** podrán acceder al formulario y enviar datos.

En algunos casos, es posible que desees habilitar la entrada de datos para cualquier persona que tenga la URL. Esto permite que las personas con la URL del formulario envíen envíos sin iniciar sesión en una cuenta de KoboToolbox.

Para permitir la entrada de datos a cualquier persona con la URL del formulario:
1. Abre el proyecto en KoboToolbox y ve a la sección **FORMULARIO**
2. En **Recolectar datos**, habilita "Permitir envíos a este formulario sin un nombre de usuario/a y contraseña".

![Ejemplo de requerir autenticación](images/project_sharing_settings/require_authentication.png)

También puedes cambiar esta configuración yendo a la pestaña **Compartir** en la página **CONFIGURACIÓN** de tu proyecto y alternando la configuración predeterminada para habilitar "Permitir envíos a este formulario sin un nombre de usuario/a y contraseña".

<p class="note">
  <strong>Nota:</strong> Configurar formularios para requerir autenticación ahora está disponible como una configuración por proyecto. Esta función de privacidad reemplaza la configuración anterior a nivel de cuenta para "Requerir autenticación para ver formularios y enviar datos". Con esta actualización, los nuevos proyectos requieren autenticación de forma predeterminada. Los proyectos existentes heredan tu configuración anterior a nivel de cuenta tal como estaba en el momento de esta actualización.
</p>

## Hacer público tu proyecto

Además de compartir tu proyecto con usuarios/as específicos/as de KoboToolbox, también puedes hacer público tu formulario y/o los datos del proyecto. Para hacer esto:

1. Ve a la página **CONFIGURACIÓN** de tu proyecto de recolección de datos
2. Abre la pestaña **Compartir**
3. Selecciona las opciones "Cualquiera puede ver este formulario" y/o "Cualquiera puede ver los envíos realizados a este formulario"

<p class="note">
  <strong>Nota:</strong> Al seleccionar "Cualquiera puede ver los envíos realizados a este formulario", la opción "Cualquiera puede ver este formulario" también se selecciona de forma predeterminada.
</p>

Se mostrará una URL que puedes compartir para proporcionar acceso al formulario y/o a los datos del proyecto sin requerir el inicio de sesión en una cuenta de KoboToolbox. Los/as usuarios/as con el enlace podrán realizar las siguientes acciones:

| **Opción**    | **Acciones permitidas**                                |
| :----------------- | :--------------------------------------------- |
| Cualquiera puede ver este formulario              | <ul><li>Acceder a la página **FORMULARIO**</li> <li>Previsualizar el formulario</li> <li>Descargar el formulario como XLS o XML</li></ul> |
| Cualquiera puede ver los envíos realizados a este formulario      | <ul><li>Acceder a la página **DATOS**</li><li>Ver los datos en la vista de **Tabla**</li><li>Ver e imprimir **Informes**</li><li>Ver la **Galería**</li><li>**Descargar** los datos del proyecto</li><li>Ver los datos en la vista de **Mapa**</li></ul> |

## Transferir la propiedad de un proyecto

Puedes transferir la propiedad del proyecto de tu cuenta a una cuenta de usuario/a diferente. Ambas cuentas deben estar en el mismo servidor de KoboToolbox.

Para transferir un proyecto:
1. Ve a la página **CONFIGURACIÓN** de tu proyecto de recolección de datos.
2. Abre la pestaña **Compartir**.
3. En la sección **Transferir propiedad del proyecto**, haz clic en **Transferir**.
4. Ingresa el nombre de usuario/a de la cuenta a la que deseas transferir el proyecto.
5. Haz clic en **Transferir proyecto**.
   
Se enviará un correo electrónico al/a la usuario/a que recibe el proyecto. Para aceptar la transferencia, el/la destinatario/a debe hacer clic en el enlace del correo electrónico mientras tiene la sesión iniciada en su cuenta de KoboToolbox. Cuando haga clic en el enlace, se mostrará un cuadro de diálogo de confirmación. El/la destinatario/a debe hacer clic en **Aceptar** para que se complete la transferencia del proyecto.

<p class="note">
  <strong>Nota:</strong> Después de aceptar la transferencia, puede tomar algunos minutos completarse. El/la nuevo/a propietario/a del proyecto puede ver el proyecto en su lista de proyectos de inmediato, pero la vista de tabla de datos puede tardar más en actualizarse.
</p>

## Eliminar proyectos compartidos de tu cuenta

Para eliminar un proyecto que otro/a usuario/a compartió contigo:

1. Abre el proyecto y ve a la página **FORMULARIO**.
2. Haz clic en <i class="k-icon-more"></i> **Más acciones** en la esquina superior derecha.
3. Selecciona **Eliminar proyecto compartido**.
4. Confirma haciendo clic en **ELIMINAR**.

<iframe src="https://www.youtube.com/embed/EZyj0tQXtzA?si=EmE0bahqxFAW2Fqm" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>