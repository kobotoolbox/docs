# Conectar KoboToolbox con Power BI
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/ae9e699afd6c0ed484945430ba6722b974b99b49/source/pulling_data_into_powerbi.md" class="reference">22 Aug 2022</a>


La API de KoboToolbox te permite conectar tu proyecto con otras herramientas de análisis de datos como Power BI, Excel y Google Sheets. Los datos que recolectas se comparten con la aplicación externa, que luego puede utilizarse para análisis, visualizaciones e informes interactivos.

Uno de los programas de análisis y visualización de datos más populares a los que puedes conectarte es [Microsoft Power BI](https://powerbi.microsoft.com).

Este artículo te guía paso a paso para conectar tu proyecto con Power BI. Si deseas conectarte con Excel, consulta el artículo [Conectar KoboToolbox con Microsoft Excel](pulling_data_into_excelquery.md).

## Paso 1: Obtener la URL de exportaciones sincrónicas

El primer paso para llevar datos a Power BI es obtener la URL de exportaciones sincrónicas a través de la API de KoboToolbox. El proceso detallado para hacerlo se describe en el artículo [Usar la API para exportaciones sincrónicas](synchronous_exports.md).

## Paso 2: Agregar la fuente de datos

Una vez que tengas tu URL, puedes seguir los pasos a continuación en Power BI:

- Haz clic en la flecha desplegable del botón "Get Data"
- Elige "Web"
- Pega la URL de exportación sincrónica que copiaste y haz clic en **OK**
- Haz clic en **Basic** para agregar tus datos de autenticación
- Escribe tu nombre de usuario y contraseña de KoboToolbox y haz clic en **CONNECT**

<p class="note">
  Si hiciste públicos los datos de tu proyecto, puedes conectarte sin necesidad de autenticación eligiendo "Anonymous" en la caja de diálogo "Access Web content". Obtén más información sobre los permisos del proyecto
  <a href="managing_permissions.html" class="reference">aquí</a>.
</p>

En el Navigator se mostrará una lista de los datos contenidos en tu proyecto.

- Elige los datos que deseas importar.
- Haz clic en **Load** para cargar los datos, o en **Transform Data** para abrir el Power Query Editor, que puedes usar para limpiar y transformar los datos antes de cargarlos.

![Get data and Authentication](images/pulling_data_into_powerbi/get_data_auth.gif)

Las tablas se mostrarán en el panel **Fields**, donde puedes desarrollar tus informes interactivos e informes.

<p class="note">
  En Power BI puedes conectar varios proyectos. Repite el proceso anterior para cada proyecto, usando su URL de exportación sincrónica. En el caso de tener varias tablas (por ejemplo, si tienes grupos de repetición), es posible que también necesites configurar relaciones entre tablas. Esto se hace en la <strong>Model View</strong>.
  Obtén más información sobre cómo crear relaciones entre tablas
  <a
    href="https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships"
    class="reference"
    >aquí</a
  >.
</p>

## Actualizar los datos en tus informes

Cuando los datos de tu proyecto se actualicen en el servidor de KoboToolbox, por ejemplo al recibir nuevos envíos, cambios en los estados de validación, ediciones o eliminaciones, deberás sincronizarlos con tus informes.

Para hacerlo, haz clic en **Refresh** en la ventana "Home".

## Resolución de problemas

### Error al conectarse a KoboToolbox

En ocasiones, incluso después de ingresar las credenciales correctas para conectarte a tu proyecto, es posible que veas un error. Esto puede ocurrir si Power BI fue configurado para conectarse a una cuenta anteriormente y ahora intentas conectarte con una cuenta diferente del mismo servidor de KoboToolbox.

Para restablecer la configuración de autenticación:

- Ve a **File -> Options and Settings -> Data Source Settings**. Selecciona los permisos existentes en la caja de diálogo y haz clic en **Clear Permissions**. Cierra la ventana e intenta agregar la nueva conexión nuevamente.

![Clear Permissions](images/pulling_data_into_powerbi/data_source_settings.gif)

### Error al actualizar los datos

Si ves un error al actualizar los datos, puede deberse a varias razones:

- Es posible que tus datos de autenticación hayan cambiado. Deberás seguir las instrucciones anteriores para cambiar tu configuración en **Data Source Settings**.
- Uno o más campos de tu formulario pueden haber sido eliminados o renombrados. Deberás
  [editar la consulta](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Puede haber una discrepancia en el tipo de datos, especialmente si cambiaste el tipo de datos de uno o más campos en Power BI. Puedes intentar restablecer el tipo de datos antes de actualizar la conexión.