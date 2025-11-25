# Configurar la autenticación de dos factores en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/3c86f234242bee25d3d6f91bffee5cb93d808344/source/two_factor_authentication.md" class="reference">5 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/4BhF0eva_d4?si=Ha6XbjiSjfPEL-CX" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br>

KoboToolbox admite la **Autenticación de Dos Factores (2FA)** para mejorar la seguridad de la cuenta. Con 2FA, necesitarás ingresar la contraseña de tu cuenta y un código de una aplicación de smartphone para acceder a tu cuenta de KoboToolbox.

2FA minimiza los riesgos de una contraseña comprometida. Incluso si tu contraseña es hackeada, obtenida mediante phishing o adivinada, 2FA previene el acceso no autorizado a tu cuenta al agregar una capa adicional de seguridad más allá de la **Autenticación de Un Solo Factor (SFA)**.

<p class="note">
    <strong>Nota:</strong> Se requiere una aplicación de autenticación compatible en tu dispositivo móvil para configurar 2FA para tu cuenta de KoboToolbox. Este artículo utiliza Google Authenticator, disponible en <a href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2">Google Play Store</a> y <a href="https://apps.apple.com/fr/app/google-authenticator/id388497605?l=en-GB">Apple App Store</a>, pero otras aplicaciones de autenticación también pueden funcionar.
</p>

Este artículo cubre los siguientes temas:

- Configurar 2FA con un código QR o clave manual
- Desactivar y reconfigurar 2FA
- Usar KoboCollect cuando 2FA está habilitado

## Configurar 2FA en KoboToolbox

2FA en KoboToolbox se puede configurar utilizando dos enfoques diferentes: el enfoque de **código QR** y el enfoque de **clave manual**. Para comenzar con cualquiera de los dos enfoques:

1. Inicia sesión en tu cuenta de KoboToolbox.
2. Haz clic en el ícono de tu perfil en la esquina superior derecha.
3. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
4. Ve a la pestaña **Seguridad**.
5. En la **sección de Autenticación de dos factores**, habilita 2FA alternando el botón **Deshabilitado**.
6. Abre tu aplicación de autenticación y sigue los pasos para uno de los dos enfoques a continuación.

### Configurar 2FA con un código QR

El primer método es el enfoque de **código QR**, que utiliza la cámara de tu dispositivo para escanear un código QR y configurar 2FA para tu cuenta.

<p class="note">
  <b>Nota:</b> Los pasos a continuación describen el proceso utilizando la aplicación Google Authenticator. El proceso debería ser similar con otras aplicaciones de autenticación, pero puede haber algunas diferencias.
</p>

Para configurar 2FA con un código QR:

1. Abre tu aplicación de autenticación y presiona **Comenzar**.
2. Selecciona **Escanear un código QR**. La cámara de tu dispositivo ahora debería estar activa.
3. Escanea el código QR visible en tu monitor.
4. Ingresa el PIN de 6 dígitos de la aplicación de autenticación en tu cuenta de KoboToolbox para configurar 2FA, luego presiona **Siguiente**.
5. Se mostrarán códigos de recuperación para ayudarte a acceder a tu cuenta si tu aplicación de autenticación falla. Descarga los códigos seleccionando **Descargar códigos** y guárdalos en un lugar seguro.
6. Continúa seleccionando **Guardé mis códigos**.

Ahora has configurado exitosamente 2FA en tu cuenta de KoboToolbox a través del **enfoque de código QR**.

### Configurar 2FA con una clave manual

El segundo enfoque es el **enfoque de clave manual**, que no requiere la cámara de tu dispositivo para configurar 2FA para tu cuenta de KoboToolbox.

Para configurar 2FA con una clave manual:

1. En la parte inferior de la ventana de 2FA en KoboToolbox, haz clic en **¿No tienes código QR? Ingresa la clave manualmente**. Se mostrará una clave de 32 caracteres.
2. Abre tu aplicación de autenticación y presiona **Comenzar**.
3. Selecciona **Ingresar una clave de configuración**.
4. Ingresa el nombre de la cuenta (por ejemplo, "KoboToolbox") y la clave de 32 caracteres en la aplicación, luego presiona **Agregar**.
5. Ingresa el PIN de 6 dígitos de tu aplicación de autenticación en tu cuenta de KoboToolbox para configurar 2FA, luego presiona **Siguiente**.
6. Se mostrarán códigos de recuperación para ayudarte a acceder a tu cuenta si tu aplicación de autenticación falla. **Descarga los códigos** seleccionando Descargar códigos y guárdalos en un lugar seguro.
7. Continúa seleccionando **Guardé mis códigos**.

Ahora has configurado exitosamente 2FA en tu cuenta de KoboToolbox a través del **enfoque de clave manual**.

## Desactivar 2FA

Para desactivar 2FA de tu cuenta de KoboToolbox:

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
3. Ve a la pestaña **Seguridad**.
4. En la **sección de Autenticación de dos factores**, desactiva 2FA alternando el botón **Habilitado**.
5. Abre la aplicación de autenticación en tu smartphone, obtén el código de 6 dígitos e ingrésalo. Presiona **Siguiente**.
6. Después de ingresar el código de 6 dígitos, el sistema desactivará 2FA de tu cuenta.

![image](/images/two_factor_authentication/Deactivate_2FA.png)

## Reconfigurar 2FA

Para reconfigurar 2FA para tu cuenta de KoboToolbox (por ejemplo, para configurar un nuevo smartphone):

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
3. Ve a la pestaña **Seguridad**.
4. En la **sección de Autenticación de dos factores**, junto a **Aplicación de autenticación**, presiona el botón **Reconfigurar** para comenzar a reconfigurar 2FA. Este proceso sigue los mismos pasos que configurar 2FA.

Cuando reconfigures 2FA para tu cuenta, la configuración anterior se eliminará automáticamente. Cualquier token o código de recuperación de la configuración anterior ya no será válido. Después de que tu 2FA actual haya sido desactivado, se te pedirá que lo configures nuevamente. Si no puedes completar el proceso, 2FA permanecerá deshabilitado para tu cuenta. En este caso, puedes habilitarlo nuevamente en cualquier momento a través del proceso habitual, como se compartió anteriormente.

## Usar KoboCollect con 2FA

La autenticación de dos factores agrega una capa de protección a las cuentas con datos sensibles. Usar estas cuentas para la recolección de datos podría representar riesgos significativos. Por lo tanto, al activar 2FA para tu cuenta, ya no puedes descargar formularios ni enviar datos a [KoboCollect](kobocollect_on_android_latest.md) desde esta cuenta. Recibirás un mensaje de error al intentar descargar nuevos formularios dentro de la aplicación, como "El servidor requiere autenticación: Nombre de usuario o contraseña no válidos para el servidor".

Para recolectar datos con KoboCollect cuando 2FA está activo, recomendamos cualquiera de los siguientes enfoques:

1. Crea una cuenta de KoboToolbox separada para la recolección de datos y pruebas de formularios para usar con KoboCollect. Comparte tu(s) formulario(s) con esta nueva cuenta y restringe sus [permisos](managing_permissions.md) a **Agregar envíos** para máxima seguridad.
2. [Habilita](https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication) "Permitir envíos a este formulario sin nombre de usuario y contraseña" para tus formularios, y [conéctate a KoboCollect](kobocollect_on_android_latest.md) usando las siguientes credenciales:
    - **URL**: `https://[kobocollect_url]/[username]`
    - **Nombre de usuario**: (en blanco)
    - **Contraseña**: (en blanco)

El segundo enfoque permite a los/as usuarios/as descargar y enviar datos a cualquier formulario compartido con `username` que no [requiera autenticación](https://support.kobotoolbox.org/es/project_sharing_settings.html#allowing-submissions-without-authentication).

## Solución de problemas
<details>
<summary><b>Generar nuevos códigos de recuperación</b></summary>
Si has extraviado tus códigos de recuperación o crees que han sido comprometidos, puedes generar nuevos códigos de recuperación para 2FA presionando el botón <b>Generar nuevos</b> junto a <b>Códigos de recuperación</b>.
</details>

<br>

<details>
<summary><b>No se puede acceder a la cuenta de KoboToolbox</b></summary>
Si no puedes acceder a tu cuenta de KoboToolbox con 2FA habilitado (por ejemplo, si restableciste tu smartphone y desinstalaste la aplicación de autenticación, o extraviaste tus códigos de recuperación), puedes contactar a <a class="reference external" href="support@kobotoolbox.org">support@kobotoolbox.org</a>. Por favor, utiliza la dirección de correo electrónico registrada en tu cuenta para solicitar que se desactive 2FA.
</details>

<br>

<details>
<summary><b>Funcionalidad no disponible</b></summary>
Esta funcionalidad actualmente no está disponible para los/as usuarios/as en el Community Plan (Plan Comunitario). Sin embargo, 2FA se extenderá a todos/as los/as usuarios/as en los próximos meses, independientemente de su plan.
</details>