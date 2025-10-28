# Conectar KoboToolbox a Power BI
<a href="../pulling_data_into_powerbi.html">Read in English</a> | <a href="../fr/pulling_data_into_powerbi.html">Lire en français</a> | <a href="../ar/pulling_data_into_powerbi.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/ae9e699afd6c0ed484945430ba6722b974b99b49/source/pulling_data_into_powerbi.md" class="reference">22 ago 2022</a>

La API de KoboToolbox te permite conectar tu proyecto con otras herramientas de análisis de datos como Power BI, Excel y Google Sheets. Los datos que recolectas se comparten con la aplicación externa, que luego puede utilizarse para análisis, visualizaciones y paneles de control.

Uno de los programas de análisis y visualización de datos más populares al que puedes conectarte es [Microsoft Power BI](https://powerbi.microsoft.com).

Este artículo te guía a través de los pasos para conectar tu proyecto con Power BI. Si deseas conectarte a Excel, consulta el artículo [aquí](pulling_data_into_excelquery.md).

## Paso 1: Obtener la URL de exportaciones sincrónicas

El primer paso para traer datos a Power BI es obtener la URL de exportaciones sincrónicas a través de la API de KoboToolbox. Un proceso detallado para hacer esto se describe en el artículo [aquí](synchronous_exports.md).

## Paso 2: Agregar la fuente de datos

Una vez que tengas tu URL, puedes continuar con los siguientes pasos en Power BI:

- Haz clic en la flecha desplegable del botón "Obtener datos"
- Elige "Web"
- Pega la URL de exportación sincrónica que copiaste y haz clic en **Aceptar**
- Haz clic en **Básico** para agregar tus detalles de autenticación
- Escribe tu nombre de usuario/a y contraseña de KoboToolbox y haz clic en **CONECTAR**

<p class="note">
  Si hiciste públicos los datos de tu proyecto, puedes conectarte sin necesidad de autenticación eligiendo "Anónimo" en el cuadro de diálogo "Acceder al contenido web". Obtén más información sobre los permisos de proyectos
  <a href="managing_permissions.html" class="reference">aquí</a>.
</p>

Se mostrará una lista de los datos contenidos en tu proyecto en el Navegador.

- Elige los datos que deseas importar.
- Haz clic en **Cargar** para traer los datos o haz clic en **Transformar datos** para abrir el Editor de Power Query, que puedes usar para limpiar y transformar los datos antes de cargarlos.

![Obtener datos y Autenticación](images/pulling_data_into_powerbi/get_data_auth.gif)

Las tablas se mostrarán en el panel **Campos** donde puedes desarrollar tus paneles de control e informes.

<p class="note">
  En Power BI puedes conectar múltiples proyectos. Repite el proceso anterior para cada proyecto, usando su URL de exportación sincrónica. En el caso de que tengas múltiples tablas (por ejemplo, si tuvieras grupos repetidos), es posible que también necesites configurar relaciones entre tablas. Esto se hace en la <strong>Vista de modelo</strong>. Obtén más información sobre cómo crear relaciones entre tablas
  <a
    href="https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships"
    class="reference"
    >aquí</a
  >.
</p>

## Actualizar los datos en tus informes

Cuando los datos de tu proyecto se actualizan en el servidor de KoboToolbox, como cuando tienes nuevos envíos, estados de validación modificados, ediciones o eliminaciones, necesitarás sincronizarlos con tus informes.

Para hacer esto, haz clic en **Actualizar** en la pestaña "Inicio".

## Solución de problemas

### Error al conectarse a KoboToolbox

A veces, incluso después de ingresar las credenciales correctas para conectarte a tu proyecto, es posible que veas un error. Esto puede suceder si Power BI se configuró para conectarse a una cuenta antes, y ahora estás intentando conectarte usando una cuenta diferente del mismo servidor de KoboToolbox.

Para restablecer la configuración de autenticación:

- Ve a **Archivo -> Opciones y configuración -> Configuración de origen de datos**. Selecciona los permisos existentes en el cuadro de diálogo y haz clic en **Borrar permisos**. Cierra e intenta agregar la nueva conexión nuevamente.

![Borrar permisos](images/pulling_data_into_powerbi/data_source_settings.gif)

### Error al actualizar datos

Si estás obteniendo un error al actualizar datos, podría haber varias razones:

- Tus detalles de autenticación podrían haber cambiado. Necesitarás seguir las instrucciones anteriores para cambiar tu **Configuración de origen de datos**.
- Uno o más campos en tu formulario podrían haber sido eliminados o renombrados. Necesitarás [editar la consulta](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Podría haber una discrepancia de tipo de datos, especialmente si cambiaste el tipo de datos de uno o más campos en Power BI. Puedes intentar restablecer el tipo de datos antes de actualizar la conexión.