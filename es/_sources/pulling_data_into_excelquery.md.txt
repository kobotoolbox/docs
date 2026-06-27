# Conectar KoboToolbox con Microsoft Excel
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/df082614a0ae0bce8543b0c1474a9567fea7293e/source/pulling_data_into_excelquery.md" class="reference">23 ago 2022</a>


KoboToolbox te permite conectar tu proyecto de recolección de datos con programas
externos como Microsoft Excel, Power BI o Google Sheets, lo cual es posible
gracias a la interfaz de programación de aplicaciones (API).

Este artículo te guía a través del proceso de conectar tu proyecto con Excel.
Si deseas conectarte con Power BI, consulta el artículo
[aquí](pulling_data_into_powerbi.md).

## Paso 1: Obtén la URL de exportaciones sincrónicas

Para importar datos a Excel, primero debes obtener la URL de exportaciones sincrónicas
a través de la API de KoboToolbox. El proceso paso a paso para hacerlo se describe
en el artículo [aquí](synchronous_exports.md).

## Paso 2: Agrega la fuente de datos

<p class="note">Estos pasos solo funcionan en Excel 2016 y versiones posteriores.</p>

- Abre Excel y crea un libro en blanco. También puedes trabajar dentro de un libro
  existente, incluso si ya tiene datos.
- Haz clic en la ventana **Datos**, elige **Obtener datos -> Desde otras fuentes -> Desde la web**.
- Pega la URL de exportaciones sincrónicas que copiaste y haz clic en **Aceptar**.

![Get data](images/pulling_data_excelquery/get_data.gif)

- Dentro de la caja de diálogo "Acceder a contenido web", haz clic en **Básica** para agregar
  tus datos de autenticación.
- Ingresa tu nombre de usuario y contraseña de KoboToolbox y haz clic en **CONECTAR**.

![Authentication](images/pulling_data_excelquery/authentication.gif)

<p class="note">
  Si hiciste públicos los datos de tu proyecto, puedes conectarte sin autenticación
  eligiendo "Anónimo" en la caja de diálogo "Acceder a contenido web". Obtén más información
  sobre los permisos del proyecto
  <a href="managing_permissions.html" class="reference">aquí</a>.
</p>

En el Navegador se mostrará una lista de los datos contenidos en tu proyecto.

<p class="note">
  Si tu formulario tiene grupos de repetición, cada grupo aparecerá como una hoja
  de trabajo separada en el Navegador. Asegúrate de usar el enlace "data_url_xlsx" ya que
  la exportación CSV <em>no</em> incluye grupos de repetición.
</p>

- Elige los datos que deseas importar. Para importar varias tablas a la vez,
  haz clic en "Seleccionar varios elementos" y luego elige los elementos de la lista.
- Haz clic en **Cargar** para importar los datos, o haz clic en **Transformar datos** para abrir el
  Editor de Power Query, que puedes usar para limpiar y transformar los datos antes
  de cargarlos.

![Choosing tables](images/pulling_data_excelquery/navigator.gif)

<p class="note">
  Puedes conectar varios proyectos en un mismo libro de Excel. Repite el proceso
  anterior para cada proyecto, usando su URL de exportación sincrónica. En la mayoría de los casos
  en que tengas varias tablas, puede ser necesario configurar relaciones entre tablas
  antes de poder usar los campos para crear informes y paneles.
  Configura las relaciones yendo a
  <strong>Datos -> Herramientas de datos -> Relaciones</strong>. Obtén más información sobre
  cómo crear relaciones entre tablas
  <a
    href="https://support.microsoft.com/en-us/office/create-a-relationship-between-tables-in-excel-fe1b6be7-1d85-4add-a629-8a3848820be3"
    class="reference"
    >aquí</a
>.
</p>

### Usar los datos importados

Excel te ofrece varias formas de trabajar con los datos que acabas de importar.

#### 1. Crear tablas dinámicas y gráficos dinámicos desde el modelo de datos

Una tabla dinámica es una herramienta eficaz que se usa para calcular, resumir y analizar datos,
lo que te permite ver comparaciones, patrones y tendencias en los datos. Los datos
resumidos en tablas dinámicas se pueden visualizar de forma sencilla mediante
gráficos dinámicos.

- Haz clic en la **ventana Insertar** y luego en la flecha desplegable de Tabla dinámica.
- Elige **Desde el modelo de datos**.
- Elige **Nueva hoja de cálculo**.
- Haz clic en **Aceptar**.

![Creating a pivot table](images/pulling_data_excelquery/pivot.gif)

Las tablas importadas se mostrarán en la sección **Campos de tabla dinámica**, donde
puedes elegir los campos que necesitas.

#### 2. Cargar datos en la hoja de cálculo

Cuando importas una sola tabla, como cuando tu proyecto no tiene grupos de
repetición, los datos se cargan automáticamente como una tabla en la hoja de cálculo.
Sin embargo, cuando los datos provienen de varias tablas, estas aparecen en el
panel **Consultas y conexiones**.

Para cargar estos datos en tu hoja de cálculo:

- Haz clic derecho en una tabla del panel **Consultas y conexiones** y elige
  **Cargar en**. (Si no ves el panel, ve a **Datos -> Consultas y
  conexiones**).
- En la siguiente caja de diálogo, elige **Tabla** y haz clic en **Aceptar**. También puedes
  elegir las otras opciones disponibles según tus necesidades.

![Loading a table in Excel](images/pulling_data_excelquery/load_table.gif)

Puedes hacer esto con todas las tablas que aparecen en el panel **Consultas y conexiones**.

## Actualizar los datos en tus informes

Cuando los datos de tu proyecto se actualizan en el servidor de KoboToolbox, por ejemplo cuando
tienes nuevos envíos, cambios en los estados de validación, ediciones o eliminaciones, deberás
sincronizarlos con tus informes. En Excel:

- Ve a la ventana **Datos**.
- En "Consultas y conexiones", haz clic en **Actualizar**.

## Resolución de problemas

### Error al conectarse a KoboToolbox

En ocasiones, incluso después de ingresar las credenciales correctas para conectarte a tu
proyecto, es posible que aparezca un error. Esto puede ocurrir si Excel estaba configurado
para conectarse a una cuenta anteriormente y ahora intentas conectarte usando una
cuenta diferente del mismo servidor de KoboToolbox, es decir, ambas del
servidor Humanitario.

Para restablecer la configuración de autenticación:

- Ve a **Ventana Datos -> Obtener datos -> Configuración de origen de datos**. Selecciona los
  permisos existentes en la caja de diálogo y haz clic en **Borrar permisos**. Cierra e intenta
  agregar la nueva conexión nuevamente.

![Clearing data source settings](images/pulling_data_excelquery/data_source_settings.gif)

### Error al actualizar datos

Si aparece un error al actualizar los datos, puede deberse a varias razones:

- Es posible que tus datos de autenticación hayan cambiado. Deberás seguir las
  instrucciones anteriores para cambiar la **Configuración del origen de datos**.
- Uno o más campos de tu formulario pueden haber sido eliminados o renombrados.
  [Deberás editar la consulta en Power Query](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-query-overview).
- Puede haber una discrepancia en el tipo de datos, especialmente si cambiaste el tipo de datos
  de uno o más campos en Excel. Puedes intentar restablecer el tipo de datos antes
  de actualizar la conexión.