# Encriptar formularios
<a href="../encrypting_forms.html">Read in English</a> | <a href="../fr/encrypting_forms.html">Lire en français</a> | <a href="../ar/encrypting_forms.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/179faeb3c5a17b69406b0243ab9c22f7ca86aa44/source/encrypting_forms.md" class="reference">4 Nov 2024</a>

_Este procedimiento es bastante técnico y está destinado a usuarios/as que se sienten cómodos/as
con instrucciones técnicas avanzadas y requiere una atención estricta a los detalles._

Los formularios encriptados funcionan encriptando los datos en el teléfono en el momento en que se guardan.
Los datos enviados a KoboToolbox están encriptados y son completamente inaccesibles para cualquier persona que no
posea la clave privada. En este caso, KoboToolbox sirve simplemente como un casillero de almacenamiento
para tus archivos encriptados - un lugar para cargar y luego descargar más tarde
para la desencriptación local
([usando ODK Briefcase](http://blog.formhub.org/2013/06/27/formhub-supports-odk-briefcase/)).
Dado que los envíos de formularios están encriptados, significa, sin embargo, que cualquier cosa que
requiera acceso a los datos como la vista de mapa o la exportación de datos no funcionará dentro de
KoboToolbox. El nivel adicional de seguridad hace posible usar KoboToolbox de una manera para
recolectar datos sensibles mientras se cumplen ciertos protocolos de protección de datos.

## Cómo funciona

KoboCollect admite la capacidad de encriptar el contenido de un formulario en el momento en que
se marca como completado y listo para el envío en el teléfono. Para aprovechar
esto se requiere el uso de una clave de encriptación pública que incluyes en el
XLSForm y una clave privada (que nunca compartes) que es utilizada por ODK Briefcase
para desencriptar los datos localmente después de que los hayas descargado de KoboToolbox. La
clave pública se usa para encriptar datos mientras que la clave privada los desencripta. Solo una
persona que tiene la clave privada puede desencriptar los datos encriptados con la clave
pública. Para entender más sobre la infraestructura de clave pública y privada
[consulta aquí](https://en.wikipedia.org/wiki/Public-key_cryptography).

## Cómo encriptar formularios XLS

1. Crea tu formulario en KoboToolbox como siempre. Descarga el formulario de la lista de borradores
   como un archivo XLS.

2. En el archivo descargado ve a la hoja 'settings'.

3. Agrega una columna _submission_url_ y escribe
   `https://kc.kobotoolbox.org/submission` o
   `https://kc-eu.kobotoolbox.org/submission` (dependiendo
   del servidor que estés usando).

5. Agrega otra columna _public_key_ (es decir, base64RsaPublicKey). Pega tu
   clave pública compatible.

    (Por favor consulta la imagen a continuación como referencia)

    ![image](/images/encrypting_forms/column.png)

6. Carga el archivo XLS de nuevo a KoboToolbox. Puedes importarlo de nuevo a la
   lista de Borradores de Formularios y luego desplegarlo como un nuevo proyecto de encuesta, o importarlo
   directamente a tu lista de Proyectos desplegados. Una vez desplegado deberías ver una etiqueta
   con el texto "encrypted" junto al nombre de tu formulario.

<p class="note">
  Ten en cuenta que la URL para un/a usuario/a autenticado/a ya no incluye **tunombredeusuario** según actualizaciones recientes. 
</p>

## Cómo desencriptar formularios

ODK Briefcase se usa para descargar los archivos encriptados de KoboToolbox y
desencriptarlos localmente en tu computadora usando una clave privada asegurando acceso único
a los datos. Para que la desencriptación sea exitosa con ODK Briefcase asegúrate de
descargar e instalar _Java Cryptography Extension (JCE) Unlimited Strength
Jurisdiction Policy Files 6_ desde el
[sitio de descarga de Java](https://www.oracle.com/java/technologies/javase-jce-all-downloads.html).
Esto es necesario para que la desencriptación sea exitosa.

### Para instalar el JCE:

1. Descomprime el archivo zip descargado

2. Navega al árbol de directorios extraído y copia los archivos local_policy.jar y
   US_export_policy.jar al directorio lib\security

3. Pega estos archivos dentro del directorio de instalación del Java Runtime
   Environment (JRE) de tu computadora, reemplazando versiones anteriores de estos
   archivos.
    - En **Windows**, el JRE generalmente se instala aquí: C:\Program
      Files\Java\jre7\lib\security
    - En **OSX** la ubicación es /Library/Internet
      Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/security

### Para desencriptar tus formularios:

1. Descarga y abre [ODK Briefcase](https://docs.getodk.org/briefcase-intro/).

2. Especifica una **Storage Location** bajo la pestaña **Settings**.

3. Abre la pestaña **Pull** y haz clic en **Configure**.  
   ![image](/images/encrypting_forms/configure.png)

4. Luego ingresa lo siguiente:

    - `https://kc.kobotoolbox.org` O
      `https://kc-eu.kobotoolbox.org`(dependiendo de qué
      servidor uses)
    - Tu nombre de usuario/a
    - Tu contraseña
    - Presiona **Connect** cuando termines  
      ![image](/images/encrypting_forms/connect.png)

<p class="note">
  Ten en cuenta que las URLs del servidor anteriores ya no necesitan incluir **tunombredeusuario** según actualizaciones recientes. 
</p>

5. Se muestra una lista de proyectos. Selecciona un proyecto que desees extraer y
   presiona **Pull**. Recibirás un mensaje **Success** bajo el **Pull
   Status**.

6. Ahora ve a la pestaña **Export**.

7. Presiona **Edit Default Configuration** para asegurarte de que tienes la **PEM
   private key** en la **PEM file location**.  
   ![image](/images/encrypting_forms/private_key.png)  
   Si no está ahí, selecciona la **PEM private key** de la carpeta que habías
   asegurado de forma segura. (_Nota: También verás aquí todos los proyectos que se han
   extraído exitosamente._)

8. Ahora marca el proyecto que deseas exportar y presiona **Export**.

9. Los datos se exportan como un archivo CSV, ahora puedes ver los datos desencriptados.

## Generar claves de encriptación RSA

Para generar los pares de claves pública-privada RSA puedes usar el paquete de software
OpenSSL, que está preinstalado en OSX y Linux. En Windows tienes que
descargar e instalar el paquete de software OpenSSL desde
[este sitio](http://slproweb.com/products/Win32OpenSSL.md). (_Nota: instala el
Win64 OpenSSL v1.1.1c en **C**: en lugar de la ubicación predeterminada **C:\Program
Files**_)

### Cómo generar una clave RSA para usar con formularios encriptados en KoboToolbox

_Nota: Recomendamos encarecidamente usar OpenSSL como se documenta a continuación para crear tu
par de claves pública/privada ya que otros métodos pueden no ser compatibles con el software._

1. Abre una ventana 'cmd' de Windows.

2. Escribe el siguiente comando: `cd C:\OpenSSL-Win32\bin` para cambiar al directorio /bin
   en el directorio OpenSSL.

    ![image](/images/encrypting_forms/openssl_1.png)

3. Crea una clave privada de 2048 bits y escríbela en el archivo **MyPrivateKey.pem**
   escribiendo el siguiente comando, luego presiona **Enter**:
   `openssl genpkey -out MyPrivateKey.pem -outform PEM -algorithm RSA -pkeyopt rsa_keygen_bits:2048`

    ![image](/images/encrypting_forms/openssl_2.png)

4. Luego, extrae la clave pública para la clave privada anterior. Escribe el siguiente
   comando luego presiona **Enter**:
   `openssl rsa -in MyPrivateKey.pem -inform PEM -out MyPublicKey.pem -outform PEM -pubout`

    ![image](/images/encrypting_forms/openssl_3.png)

5. Ahora has generado dos archivos que son:

    - **MyPrivateKey.pem** - tu clave privada que necesitas mover a una ubicación
      segura.
    - **MyPublicKey.pem** - tu clave pública, que puedes compartir con cualquier persona con la que
      quieras compartir información de forma segura

6. Abre el **MyPublicKey.pem** con el Bloc de notas u otro editor de texto, tu clave
   pública es la cadena muy larga e ininterrumpida de caracteres,

`ej.:Tjhfur1K9+BRQ2USezIPbtyahbfuNqviI5Suhm8maA3JoELRHj9psjf/oNWoG87aFtKNbLrRaCEDP oFMDC9NEzWlv5L49BygeieMu/wg/rtMT0M0kgDbKxw5weJJgyb9P41aMsrqAAAAB3NzaC1yc2EAAAADAQAB AAABAQDfNoFX7bh3bfdW6lGfDht1Ea8PUBLKYjugbHN5jS7j5fHV6dexM+kzvITVgoyjhhKPXeCbaT62vD/ saTqJFXJzlysnZ24fqxNkjreO5K5EQ9c3ggwqML06+AKrFUSP5jpnyJJH8btNwKl6D5pG4ZseHwDUKzZtae xtPTNQz67kdYIKdtCkCsQHVsy4xvy/A0jzfK3xyOkG6j+L`

Esta cadena es lo que necesitarás pegar bajo el campo public_key en tu
hoja de configuración en tu archivo XLS.

**IMPORTANTE**: ¡asegúrate de pegar solo la cadena de clave pública y sin espacios
en blanco o saltos de línea!

**MyPrivateKey.pem** es el archivo que usarás al exportar los envíos
usando ODK Briefcase.

Nota: Al intentar editar un formulario que ha sido encriptado, recibes un mensaje
"This form cannot be edited once it has been marked as finalized. It may by
encrypted".