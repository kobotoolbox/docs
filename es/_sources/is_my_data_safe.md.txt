# Medidas de seguridad de datos de KoboToolbox: Mantener tus datos seguros
<a href="../is_my_data_safe.html">Read in English</a> | <a href="../fr/is_my_data_safe.html">Lire en français</a> | <a href="../ar/is_my_data_safe.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/f7c0f5afa58cad4b40bd6075209daef21a83ee6b/source/is_my_data_safe.md" class="reference">9 Oct 2025</a>

Nos tomamos muy en serio la protección de datos. La seguridad de datos significa proteger los datos de nuestros/as usuarios/as de cualquier amenaza que pueda existir. Este artículo resume algunas de nuestras medidas administrativas, físicas, organizacionales y técnicas para hacer cumplir la seguridad de datos en los servidores de KoboToolbox mantenidos por Kobo, Inc., la [organización sin fines de lucro detrás de KoboToolbox](https://www.kobotoolbox.org/about-us/).

Cumplimos plenamente con el Reglamento General de Protección de Datos (RGPD) de la Unión Europea. Si te encuentras en la Unión Europea, [puedes firmar un acuerdo de procesamiento de datos (DPA) aquí](https://www.digisigner.com/online/showTemplate?linkId=495db186-9c9e-4627-99f7-a943282eeab5).

## Confidencialidad

**Control de Acceso Físico**

-   Las medidas de control de acceso físico, entre otras, son implementadas por Amazon Web Services (AWS), que se utiliza para alojar nuestros servidores de KoboToolbox. Estas medidas incluyen, por ejemplo, videovigilancia y seguridad física de las instalaciones de servidores y redes, mantenimiento de control de acceso con tarjetas de identificación, limitación de acceso solo a personal autorizado. Para obtener una lista completa de detalles sobre las medidas técnicas y organizacionales de AWS para el control de acceso físico, [consulta este artículo](https://aws.amazon.com/compliance/data-center/controls/) sobre controles de centros de datos proporcionados por AWS.

**Control de Acceso Electrónico**

-   Todas las cuentas de KoboToolbox están protegidas con contraseña. Los/as usuarios/as reciben retroalimentación visual sobre la complejidad de su contraseña, lo que los/as alienta a seleccionar una contraseña más segura cuando sea aplicable. Solo se almacenan hashes de contraseñas cifradas en el servidor de KoboToolbox, utilizando el marco de código abierto predeterminado proporcionado por Django, que usa el algoritmo [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) con un hash SHA256. Las contraseñas en texto plano nunca se guardan en el servidor.
-   Todo el contenido de la base de datos está cifrado en reposo (cifrado a nivel de disco).
-   Los datos enviados al servidor están cifrados en tránsito utilizando SHA-256 con cifrado RSA.
-   Los/as usuarios/as pueden [optar por habilitar también el cifrado de los datos de su proyecto (cifrado a nivel de datos)](encrypting_forms.md), lo que los hace inaccesibles en todas las etapas del procesamiento de datos y requiere una clave privada para descifrarlos localmente.

**Control de Acceso Interno**

-   Solo los/as administradores/as de sistemas autorizados/as pueden acceder al servidor de KoboToolbox. Solo pueden hacerlo con el propósito expreso de actualizar el software instalado o mantener la infraestructura del servidor.
-   Los/as administradores/as de sistemas requieren autenticación adicional, incluida la autenticación de clave pública SSH, para acceder al servidor de KoboToolbox y autenticación de dos factores para acceder a los paneles de control proporcionados por AWS.
-   AWS proporciona un registro de las acciones realizadas en la consola de AWS. Para las conexiones SSH a las instancias individuales del servidor de KoboToolbox, Kobo recolecta "eventos de acceso al sistema" por clave SSH, que luego se pueden relacionar con los/as usuarios/as autorizados/as.
-   SSH está además protegido contra intentos de fuerza bruta y acceso no autorizado al limitar las conexiones a nivel de firewall solo a una pequeña lista de direcciones IP explícitamente permitidas.

**Protección de Datos por Diseño y por Defecto**

-   Solo se requiere información limitada para crear una cuenta de usuario/a de KoboToolbox.
-   El personal de Kobo está obligado a cumplir con las reglas establecidas en las políticas de privacidad de Kobo.
-   Los datos procesados en nombre del/de la usuario/a no son accedidos por Kobo.
-   Los/as usuarios/as tienen la opción de aplicar cifrado avanzado. Esto garantiza que los datos se cifren utilizando una clave pública antes de enviarse a un servidor de KoboToolbox, y que solo se puedan descifrar con una clave privada en una computadora local. KoboToolbox también ofrece la posibilidad de eliminar información de forma masiva una vez que se ha recolectado, facilitando la seudonimización de datos personales (mediante la eliminación de identificadores).
-   Consulta la subsección anterior "Control de Acceso Electrónico" para obtener detalles sobre la retroalimentación visual sobre la complejidad de la contraseña.

## Integridad

**Control de Transferencia de Datos**

-   Todos los datos en tránsito están protegidos mediante SHA-256 con cifrado RSA.

**Control de Entrada de Datos**

-   Los/as usuarios/as controlan quién tiene permiso para ingresar datos según sus permisos de KoboToolbox. Los registros de acceso HTTP almacenados en el servidor incluyen el/la usuario/a autenticado/a para la mayoría de las solicitudes.

## Disponibilidad y Resiliencia

-   Kobo realiza copias de seguridad diarias de todas las bases de datos en una ubicación remota separada. En caso de una interrupción crítica, todos los datos de los/as usuarios/as se restaurarán desde la copia de seguridad más reciente lo más rápido posible.
-   Los firewalls bloquean todas las solicitudes externas excepto las conexiones SSH desde una pequeña lista de direcciones IP explícitamente permitidas. El tráfico HTTP y HTTPS público no puede conectarse directamente al servidor de KoboToolbox, sino que es atendido por el balanceador de carga de AWS, que luego lo reenvía a los servidores front-end de Kobo.
-   Los servidores de KoboToolbox están configurados para usar múltiples instancias de servidor que se ejecutan simultáneamente y están configurados para aumentar el número de dichas instancias para evitar el impacto de cualquier falla localizada. En caso de cualquier otra falla que amenace la operación continua de aspectos críticos del software de KoboToolbox, los/as administradores/as de sistemas están disponibles para intervenir con poca antelación y restaurar el servicio.
-   Los procedimientos de informes de Kobo incluyen alertas automatizadas, escalamiento de problemas reportados por usuarios/as y problemas autodetectados por el personal.
-   Los planes de contingencia incluyen la disponibilidad de múltiples personas en múltiples ubicaciones geográficas que pueden responder a emergencias y restaurar el servicio.
-   Los servidores de KoboToolbox tienen la capacidad demostrada de continuar operando en un estado degradado, recibiendo envíos mientras simultáneamente recuperan proyectos/envíos perdidos mediante recuperación puntual al minuto (PITR).
-   Los/as usuarios/as que abusen del uso de sus cuentas al sobrecargar el servidor de KoboToolbox pueden ser suspendidos/as o su cuenta puede ser restringida.