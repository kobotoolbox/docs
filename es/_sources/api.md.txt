# Primeros pasos con la API
<a href="../api.html">Read in English</a> | <a href="../fr/api.html">Lire en français</a> | <a href="../ar/api.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/24c740499cf305ed0e9bece1dde237b9b23a05c0/source/api.md" class="reference">15 Sep 2025</a>

Una **interfaz de programación de aplicaciones (API)** permite que dos componentes de software se comuniquen mediante un conjunto de definiciones y protocolos. Con una API, un script o aplicación puede trabajar con KoboToolbox sin usar la interfaz web. Por ejemplo, puedes generar automáticamente exportaciones de datos que se vinculen a fuentes externas como paneles de control o carpetas de respaldo.

Con la **API** de KoboToolbox, puedes:

- **Descargar datos** automáticamente en JSON, CSV o XLSX.
- **Generar exportaciones bajo demanda** para paneles de control, respaldos o análisis.
- **Enviar o editar registros** desde otras herramientas de recolección de datos.
- **Crear o desplegar proyectos** y clonar los existentes mediante código.
- **Manejar usuarios/as**, permisos y actividad de proyectos a escala.

Usar la API de KoboToolbox te permite automatizar tareas rutinarias, mantener actualizados los paneles de control e integrar KoboToolbox con otros sistemas, mientras reduces los pasos manuales y errores. Este artículo proporciona una introducción a la API de KoboToolbox y cubre los siguientes pasos:

- Recuperar tu **URL del servidor**
- Recuperar tu **clave API**
- Recuperar el UID del activo del proyecto
- Exportar tus datos usando la API

<p class="note">
    <strong>Nota:</strong> Los endpoints V1 ahora están obsoletos y programados para ser descontinuados en enero de 2026, en favor de la API KPI v2, más robusta y con soporte completo. Para más información sobre la migración a KPI v2, consulta <a href="migrating_api.html">Migrar de la API v1 a v2</a>.
</p>

## Recuperar tu URL del servidor
La **URL del servidor** es la dirección web base de tu servidor de KoboToolbox. Se coloca al inicio de cada solicitud de API.

Para la mayoría de los/as usuarios/as, la URL del servidor es [kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (si estás usando el Servidor Global) o [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (si estás usando el Servidor con sede en la Unión Europea). 

![Recuperar URL del servidor](images/api/server_URL.png) 

## Recuperar tu clave API
Tu **clave API** es un token personal que actúa como una contraseña, permitiendo que el software acceda a tu cuenta a través de la API. Puede ser requerida cuando un script, panel de control o aplicación externa necesita autenticación para recuperar o enviar datos del proyecto a través de la API. 

Hay diferentes formas de obtener tu **clave API**.

**Método 1:**

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **CONFIGURACIÓN DE LA CUENTA**.
3. Ve a la pestaña **Seguridad**.
4. Tu clave API está oculta por defecto. Haz clic en **Mostrar** para verla.
   
**Método 2:**

En tu navegador web, navega a `https://[server-url]/token/?format=json`. Asegúrate de reemplazar `[server-url]` con tu URL del servidor.

**Método 3:**

En la terminal, usa el siguiente comando curl:

`curl -u username:password "https:/[server-url]/token/?format=json"`

Asegúrate de reemplazar `[server-url]` con tu URL del servidor.

## Recuperar el UID del activo de tu proyecto

El **UID del activo del proyecto** es un código único que identifica un proyecto específico de KoboToolbox y debe incluirse en las llamadas de API para dirigirse a ese proyecto. 

Puedes encontrar el **UID del activo del proyecto** en la URL de la página de resumen de tu proyecto. Es la cadena de letras y números que aparece después de "forms/" en la URL, así: `https://[server-url]/#/forms/[UID del activo del proyecto]/summary`.

![Recuperar UID del activo del proyecto](images/api/project_UID.png)

## Exportar tus datos usando la API

Hay dos enfoques principales para conectar tus datos usando la API con KoboToolbox:

- **Exportaciones sincrónicas:** Devuelve un archivo CSV o XLSX listo para usar, basado en configuraciones de exportación predefinidas, que las aplicaciones externas (por ejemplo, Power BI o Excel) pueden cargar directamente.
- **Endpoint JSON:** Envía cada registro como un archivo JSON sin procesar. Esto es mejor para flujos de trabajo basados en código, no para uso directo en herramientas de hojas de cálculo o paneles de control.
  
Cada enfoque requiere conocer la URL del servidor y el UID del activo del proyecto para construir una URL de exportación personalizada. Dependiendo de la aplicación, tu clave API puede ser necesaria para la autenticación. 

<p class="note">
    Para más información sobre exportaciones sincrónicas, consulta <a href="synchronous_exports.html">Usar la API para exportaciones sincrónicas</a>. 
<br><br>
Para aprender más sobre cómo conectar tus datos a Power BI para crear paneles de control personalizados, consulta <a href="pulling_data_into_powerbi.html">Conectar KoboToolbox a Power BI</a>. 
<br><br>
Para aprender más sobre cómo conectar tus datos a Microsoft Excel, consulta <a href="pulling_data_into_excelquery.html">Conectar KoboToolbox a Microsoft Excel</a>.
</p>