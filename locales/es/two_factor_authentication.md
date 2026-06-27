# Configurar la autenticación de dos factores en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/two_factor_authentication.md" class="reference">23 Apr 2026</a>


<iframe src="https://www.youtube.com/embed/4BhF0eva_d4?si=Ha6XbjiSjfPEL-CX&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br>

KoboToolbox admite la **autenticación de dos factores (2FA)** para mejorar la seguridad de tu cuenta. Con la 2FA, necesitarás ingresar la contraseña de tu cuenta y un código generado por una aplicación en tu smartphone para acceder a tu cuenta de KoboToolbox.

La 2FA minimiza los riesgos asociados a una contraseña comprometida. Incluso si tu contraseña es hackeada, obtenida mediante phishing o adivinada, la 2FA impide el acceso no autorizado a tu cuenta al agregar una capa adicional de seguridad más allá de la **autenticación de un solo factor (SFA)**.

<p class="note">
    <strong>Nota:</strong> Para configurar la 2FA en tu cuenta de KoboToolbox, necesitas una aplicación de autenticación compatible en tu dispositivo móvil. Este artículo utiliza Google Authenticator, disponible en <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2">Google Play Store</a> y <a href="https://apps.apple.com/fr/app/google-authenticator/id388497605?l=en-GB">Apple App Store</a>, aunque también funcionan otras aplicaciones de autenticación.
</p>

Este artículo cubre los siguientes temas:

- Configurar la 2FA con un código QR o una clave manual
- Deshabilitar y reconfigurar la 2FA
- Usar KoboCollect cuando la 2FA está habilitada

## Configurar la 2FA en KoboToolbox

La 2FA en KoboToolbox se puede configurar mediante dos enfoques: el enfoque de **código QR** y el enfoque de **clave manual**. Para comenzar con cualquiera de los dos:

1. Inicia sesión en tu cuenta de KoboToolbox.
2. Haz clic en el ícono de tu perfil en la esquina superior derecha.
3. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
4. Ve a la ventana **Seguridad**.
5. En la sección **Autenticación de dos factores**, habilita la 2FA activando el botón **Desactivado**.
6. Abre tu aplicación de autenticación y sigue los pasos para uno de los dos enfoques que se describen a continuación.

### Configurar la 2FA con un código QR

El primer método es el enfoque de **código QR**, que utiliza la cámara de tu dispositivo para escanear un código QR y configurar la 2FA en tu cuenta.

<p class="note">
  <b>Nota:</b> Los pasos a continuación describen el proceso usando la aplicación Google Authenticator. El proceso debería ser similar con otras aplicaciones de autenticación, aunque puede haber algunas diferencias.
</p>

Para configurar la 2FA con un código QR:

1. Abre tu aplicación de autenticación y haz clic en **Comenzar**.
2. Selecciona **Escanear un código QR**. La cámara de tu dispositivo debería activarse.
3. Escanea el código QR visible en tu monitor.
4. Ingresa el PIN de 6 dígitos de la aplicación de autenticación en tu cuenta de KoboToolbox para configurar la 2FA y, a continuación, haz clic en **Siguiente**.
5. Se mostrarán códigos de recuperación para ayudarte a acceder a tu cuenta si tu aplicación de autenticación falla. Descarga los códigos seleccionando **Descarga los códigos** y guárdalos en un lugar seguro.
6. Continúa seleccionando **Guardar mis códigos**.

Has configurado correctamente la 2FA en tu cuenta de KoboToolbox mediante el **enfoque de código QR**.

### Configurar la 2FA con una clave manual

El segundo enfoque es el **enfoque de clave manual**, que no requiere la cámara de tu dispositivo para configurar la 2FA en tu cuenta de KoboToolbox.

Para configurar la 2FA con una clave manual:

1. En la parte inferior de la ventana de 2FA en KoboToolbox, haz clic en **¿No tienes un código QR? Ingresa la clave manualmente**. Se mostrará una clave de 32 caracteres.
2. Abre tu aplicación de autenticación y haz clic en **Comenzar**.
3. Selecciona **Ingresar una clave de configuración**.
4. Ingresa el nombre de la cuenta (por ejemplo, "KoboToolbox") y la clave de 32 caracteres en la aplicación y, a continuación, haz clic en **Agregar**.
5. Ingresa el PIN de 6 dígitos de tu aplicación de autenticación en tu cuenta de KoboToolbox para configurar la 2FA y, a continuación, haz clic en **Siguiente**.
6. Se mostrarán códigos de recuperación para ayudarte a acceder a tu cuenta si tu aplicación de autenticación falla. **Descarga los códigos** seleccionando Descarga los códigos y guárdalos en un lugar seguro.
7. Continúa seleccionando **Guardar mis códigos**.

Has configurado correctamente la 2FA en tu cuenta de KoboToolbox mediante el **enfoque de clave manual**.

## Deshabilitar la 2FA

Para deshabilitar la 2FA en tu cuenta de KoboToolbox:

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
3. Ve a la ventana **Seguridad**.
4. En la sección **Autenticación de dos factores**, deshabilita la 2FA desactivando el botón **Activado**.
5. Abre la aplicación de autenticación en tu smartphone, obtén el código de 6 dígitos e ingrésalo. Haz clic en **Siguiente**.
6. Después de ingresar el código de 6 dígitos, el sistema deshabilitará la 2FA en tu cuenta.

![image](/images/two_factor_authentication/Deactivate_2FA.png)

## Reconfigurar la 2FA

Para reconfigurar la 2FA en tu cuenta de KoboToolbox (por ejemplo, para configurar un nuevo smartphone):

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
3. Ve a la ventana **Seguridad**.
4. En la sección **Autenticación de dos factores**, junto a **Aplicación de autenticación**, haz clic en el botón **Volver a configurar** para comenzar a reconfigurar la 2FA. Este proceso sigue los mismos pasos que la configuración inicial de la 2FA.

Cuando reconfiguras la 2FA en tu cuenta, la configuración anterior se elimina automáticamente. Los tokens o códigos de recuperación de la configuración anterior dejarán de ser válidos. Una vez desactivada tu 2FA actual, se te pedirá que la configures nuevamente. Si no puedes completar el proceso, la 2FA quedará deshabilitada en tu cuenta. En ese caso, puedes habilitarla nuevamente en cualquier momento siguiendo el proceso habitual descrito anteriormente.

## Usar KoboCollect con la 2FA

La autenticación de dos factores agrega una capa de protección a las cuentas con datos sensibles. El uso de estas cuentas para la recolección de datos puede representar riesgos significativos. Por ello, al activar la 2FA en tu cuenta, ya no podrás descargar formularios ni enviar datos a [KoboCollect](../es/data_collection_kobocollect.md) desde esta cuenta. Recibirás un mensaje de error al intentar descargar nuevos formularios dentro de la aplicación, como "Server Requires Authentication: Invalid username or password for server."

Para recolectar datos con KoboCollect cuando la 2FA está activa, recomendamos cualquiera de los siguientes enfoques:

1. Crea una cuenta de KoboToolbox separada para la recolección de datos y las pruebas de formularios, y úsala con KoboCollect. Comparte tus formularios con esta nueva cuenta y restringe sus [permisos](../es/managing_permissions.md) a **Añadir envíos** para mayor seguridad.
2. [Habilita](../es/project_sharing_settings.md#allowing-submissions-without-authentication) "Permitir envíos a este formulario sin nombre de usuario ni contraseña" para tus formularios y [conéctate a KoboCollect](../es/kobocollect_on_android_latest.md) usando las siguientes credenciales:
    - **URL**: `https://[kobocollect_url]/[username]`
    - **Nombre de usuario**: (en blanco)
    - **Contraseña**: (en blanco)

El segundo enfoque permite a los usuarios descargar y enviar datos a cualquier formulario compartido con `username` que no [requiera autenticación](../es/project_sharing_settings.md#allowing-submissions-without-authentication).

## Resolución de problemas
<details>
<summary><b>Generar nuevos códigos de recuperación</b></summary>
Si has extraviado tus códigos de recuperación o crees que han sido comprometidos, puedes generar nuevos códigos de recuperación para la 2FA haciendo clic en el botón <b>Generar nuevos</b> junto a <b>Códigos de recuperación</b>.
</details>

<br>

<details>
<summary><b>No puedo acceder a mi cuenta de KoboToolbox</b></summary>
Si no puedes acceder a tu cuenta de KoboToolbox con la 2FA habilitada (por ejemplo, si restableciste tu smartphone y desinstalaste la aplicación de autenticación, o extraviaste tus códigos de recuperación), puedes contactar a <a class="reference external" href="support@kobotoolbox.org">support@kobotoolbox.org</a>. Usa la dirección de correo electrónico registrada en tu cuenta para solicitar que se deshabilite la 2FA.
</details>