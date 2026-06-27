# Seguridad de datos en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/f7c0f5afa58cad4b40bd6075209daef21a83ee6b/source/is_my_data_safe.md" class="reference">9 oct 2025</a>


Nos tomamos muy en serio la protección de datos. La seguridad de datos implica proteger la información de nuestros usuarios de cualquier amenaza que pueda existir. Este artículo resume algunas de nuestras medidas administrativas, físicas, organizativas y técnicas para garantizar la seguridad de los datos en los servidores de KoboToolbox mantenidos por Kobo, Inc., la [organización sin fines de lucro detrás de KoboToolbox](https://www.kobotoolbox.org/about-us/).

Cumplimos plenamente con el Reglamento General de Protección de Datos (RGPD) de la Unión Europea. Si te encuentras en la Unión Europea, [puedes firmar un acuerdo de procesamiento de datos (DPA) aquí](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Confidencialidad

**Control de acceso físico**

-   Amazon Web Services (AWS), que se utiliza para alojar nuestros servidores de KoboToolbox, implementa, entre otras, medidas de control de acceso físico. Estas medidas incluyen, por ejemplo, videovigilancia y seguridad física de las instalaciones de servidores y redes, mantenimiento de control de acceso mediante tarjeta de identificación y restricción del acceso únicamente al personal autorizado. Para obtener una lista completa de los detalles sobre las medidas técnicas y organizativas de AWS para el control de acceso físico, [consulta este artículo](https://aws.amazon.com/compliance/data-center/controls/) sobre los controles de centros de datos proporcionados por AWS.

**Control de acceso electrónico**

-   Todas las cuentas de KoboToolbox están protegidas con contraseña. Los usuarios reciben retroalimentación visual sobre la complejidad de su contraseña, lo que los incentiva a elegir una contraseña más segura cuando corresponde. Solo se almacenan hashes de contraseñas cifradas en el servidor de KoboToolbox, utilizando el framework de código abierto predeterminado proporcionado por Django, que usa el algoritmo [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) con un hash SHA256. Las contraseñas en texto plano nunca se guardan en el servidor.
-   Todo el contenido de la base de datos está cifrado en reposo (cifrado a nivel de disco).
-   Los datos enviados al servidor están cifrados en tránsito mediante SHA-256 con cifrado RSA.
-   Los usuarios pueden [optar por habilitar también el cifrado de los datos de su proyecto (cifrado a nivel de datos)](encrypting_forms.md), lo que los hace inaccesibles en todas las etapas del procesamiento de datos y requiere una clave privada para descifrarlos localmente.

**Control de acceso interno**

-   Solo los administradores de sistemas autorizados pueden acceder al servidor de KoboToolbox. Solo pueden hacerlo con el propósito expreso de actualizar el software instalado o mantener la infraestructura del servidor.
-   Los administradores de sistemas requieren autenticación adicional, incluida la autenticación de clave pública SSH, para acceder al servidor de KoboToolbox, y autenticación de dos factores para acceder a los paneles de control proporcionados por AWS.
-   AWS proporciona un registro de las acciones realizadas en la consola de AWS. Para las conexiones SSH a las instancias individuales del servidor de KoboToolbox, Kobo recopila "eventos de acceso al sistema" por clave SSH, que luego pueden vincularse a los usuarios autorizados.
-   SSH está además protegido contra intentos de fuerza bruta y accesos no autorizados mediante la limitación de conexiones a nivel de firewall a una pequeña lista de direcciones IP explícitamente permitidas.

**Protección de datos por diseño y por defecto**

-   Solo se requiere información limitada para crear una cuenta de usuario en KoboToolbox.
-   El personal de Kobo está obligado a cumplir las normas establecidas en las políticas de privacidad de Kobo.
-   Kobo no accede a los datos procesados en nombre del usuario.
-   Los usuarios tienen la opción de aplicar cifrado avanzado. Esto garantiza que los datos se cifren con una clave pública antes de enviarse a un servidor de KoboToolbox, y que solo puedan descifrarse con una clave privada en un equipo local. KoboToolbox también ofrece la posibilidad de eliminar información de forma masiva una vez recolectada, lo que facilita la seudonimización de datos personales (mediante la eliminación de identificadores).
-   Consulta la subsección anterior "Control de acceso electrónico" para obtener más detalles sobre la retroalimentación visual sobre la complejidad de la contraseña.

## Integridad

**Control de transferencia de datos**

-   Todos los datos en tránsito están protegidos mediante SHA-256 con cifrado RSA.

**Control de entrada de datos**

-   Los usuarios controlan quién tiene permiso para ingresar datos según sus permisos en KoboToolbox. Los registros de acceso HTTP almacenados en el servidor incluyen el usuario autenticado para la mayoría de las solicitudes.

## Disponibilidad y resiliencia

-   Kobo realiza copias de seguridad diarias de todas las bases de datos en una ubicación remota independiente. En caso de una interrupción crítica, todos los datos de los usuarios se restaurarán desde la copia de seguridad más reciente lo antes posible.
-   Los firewalls bloquean todas las solicitudes externas, excepto las conexiones SSH provenientes de una pequeña lista de direcciones IP explícitamente permitidas. El tráfico HTTP y HTTPS público no puede conectarse directamente al servidor de KoboToolbox; en su lugar, es atendido por el balanceador de carga de AWS, que lo reenvía a los servidores front-end de Kobo.
-   Los servidores de KoboToolbox están configurados para utilizar múltiples instancias de servidor en ejecución simultánea y están configurados para aumentar el número de dichas instancias y evitar el impacto de cualquier falla localizada. En caso de otras fallas que amenacen el funcionamiento continuo de aspectos críticos del software de KoboToolbox, los administradores de sistemas están disponibles para intervenir con poco tiempo de aviso y restablecer el servicio.
-   Los procedimientos de reporte de Kobo incluyen alertas automatizadas, escalamiento de problemas reportados por usuarios y problemas detectados por el propio personal.
-   Los planes de contingencia incluyen la disponibilidad de múltiples personas en múltiples ubicaciones geográficas que pueden responder a emergencias y restablecer el servicio.
-   Los servidores de KoboToolbox tienen la capacidad demostrada de continuar operando en un estado degradado, recibiendo envíos mientras recuperan simultáneamente proyectos/envíos perdidos mediante recuperación puntual al minuto (PITR).
-   Los usuarios que abusen del uso de sus cuentas sobrecargando el servidor de KoboToolbox pueden ser suspendidos o ver su cuenta restringida.