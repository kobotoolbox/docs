# Descargar envíos manualmente
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/manual_upload.md" class="reference">23 Apr 2026</a>


<p class="note">Ten en cuenta que esta es todavía una función experimental y no impide la creación de envíos duplicados.</p>

En ciertas situaciones, es posible que no puedas utilizar la opción de carga estándar después de recolectar datos con **KoboCollect** o **formularios web**. Esto puede deberse a problemas con tu dispositivo móvil (por ejemplo, la pantalla rota), o a encontrarte en una ubicación remota sin acceso a internet. Es posible que quieras descargar tus envíos del dispositivo de recolección de datos a tu computadora local y luego cargarlos al servidor cuando recuperes la conectividad a internet.

## Exportar datos desde formularios web

1. En tu **formulario web** habilitado para uso sin conexión, abre el "Panel lateral" haciendo clic en el corchete de la izquierda.

![Side Panel](/images/manual_upload/Side_Panel.png)

2. Haz clic en el botón **Exportar** y se guardará un archivo ZIP en tu computadora. Si no es así, haz clic en el botón **Exportar** nuevamente. En algunos navegadores esto puede no funcionar y tendrás que hacer clic en el enlace "alternative download - online", que requiere conexión a internet.

![Export](/images/manual_upload/Export.png)

3. Ahora sigue las [instrucciones que se detallan a continuación](#importing-a-data-zip-file) para importar tus envíos.

## Exportar datos desde KoboCollect

1. Conecta el dispositivo a tu computadora mediante un cable USB.

2. Abre el almacenamiento interno del dispositivo en tu computadora. (En **Windows**, los controladores se instalarán automáticamente y podrás acceder al dispositivo desde **Mi PC**. En **MacOS** necesitarás [Android File Transfer](https://www.android.com/intl/en_us/filetransfer/) de Google para acceder a los archivos del dispositivo.)

3. En tu dispositivo, navega hasta la carpeta **KoboCollect** (que se encuentra en la siguiente ruta):

`Phone\Android\data\org.koboc.collect.android\files\projects`

    Puedes obtener más información sobre la ruta de almacenamiento del dispositivo [Importar formularios en KoboCollect](transferring_forms.md).

4. Copia la carpeta "instances" y pégala en algún lugar de tu computadora.

5. Si tienes más de un dispositivo, repite los pasos anteriores y cambia el nombre de cada carpeta "instances" con un nombre o número único.

6. Crea un archivo ZIP de la carpeta.

7. Ahora sigue las [instrucciones que se detallan a continuación](#importing-a-data-zip-file) para importar tus envíos.

## Importar un archivo ZIP de datos

1. Inicia sesión en tu cuenta de KoboToolbox y visita:
   `https://kc-eu.kobotoolbox.org/your_username/bulk-submission-form` O
   `https://kc.kobotoolbox.org/your_username/bulk-submission-form` (según el servidor donde te registraste), y reemplaza `your_username` con **tu propio nombre de usuario**.

2. Selecciona y carga el archivo ZIP. Todos los registros se cargarán al servidor, siempre que correspondan a un formulario existente.

Una vez que se hayan cargado todas las instancias, verás un mensaje de confirmación para cada registro. Si aparece un mensaje de tiempo de espera agotado, puedes intentar cargar varios archivos ZIP más pequeños con menos registros. Cargar los mismos registros dos veces no es un problema, ya que los registros duplicados serán rechazados.