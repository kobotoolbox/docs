# Introducción a la API
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/afd562326337a448c613f919951aaed8005b62ef/source/api.md" class="reference">22 Jun 2026</a>


Una **interfaz de programación de aplicaciones (API)** permite que dos componentes de software se comuniquen mediante un conjunto de definiciones y protocolos. Con una API, un script o una aplicación pueden trabajar con KoboToolbox sin usar la interfaz web. Por ejemplo, puedes generar automáticamente exportaciones de datos que se vinculen a fuentes externas como informes interactivos o carpetas de respaldo.

Con la **API** de KoboToolbox, puedes:

- **Descargar datos** automáticamente en JSON, CSV o XLSX.
- **Generar exportaciones bajo demanda** para informes interactivos, respaldos o análisis.
- **Enviar o editar registros** desde otras herramientas de recolección de datos.
- **Crear o implementar proyectos** y clonar los existentes mediante código.
- **Gestionar usuarios**, permisos y la actividad de los proyectos a escala.

Usar la API de KoboToolbox te permite automatizar tareas rutinarias, mantener los informes actualizados e integrar KoboToolbox con otros sistemas, reduciendo los pasos manuales y los errores. Este artículo es una introducción a la API de KoboToolbox y cubre los siguientes pasos:

- Obtener la **URL del servidor**
- Obtener tu **Clave API**
- Obtener el UID del proyecto
- Exportar datos usando la API
- Documentación avanzada de la API

## Obtener la URL del servidor
La **URL del servidor** es la dirección web base de tu servidor de KoboToolbox. Se coloca al inicio de cada solicitud a la API.

Para la mayoría de los usuarios, la URL del servidor es [kf.kobotoolbox.org](https://kf.kobotoolbox.org/) (si usas el Servidor Global) o [eu.kobotoolbox.org](https://eu.kobotoolbox.org/) (si usas el Servidor con sede en la Unión Europea).

![Retrieve server URL](images/api/server_URL.png)

## Obtener tu Clave API
Tu **Clave API** es un token personal que funciona como una contraseña y permite que el software acceda a tu cuenta a través de la API. Puede ser necesaria cuando un script, un informe interactivo o una aplicación externa requieren autenticación para recuperar o enviar datos del proyecto a través de la API.

Hay diferentes formas de obtener tu **Clave API**.

**Método 1:**

1. Haz clic en el ícono de tu perfil en la esquina superior derecha.
2. Selecciona **Configuración de la cuenta**.
3. Ve a la ventana **Seguridad**.
4. Tu Clave API está oculta de forma predeterminada. Haz clic en **Mostrar** para verla.

![Display API Key](images/api/key.png)

**Método 2:**

En tu navegador web, ve a `https://[server-url]/token/?format=json`. Asegúrate de reemplazar `[server-url]` con la URL de tu servidor.

**Método 3:**

En la terminal, usa el siguiente comando curl:

`curl -u username:password "https:/[server-url]/token/?format=json"`

Asegúrate de reemplazar `[server-url]` con la URL de tu servidor.

<p class="note">
    <strong>Nota:</strong> Si tu Clave API se comparte, se hace pública o se ve comprometida de alguna otra forma, regénérala de inmediato. Tu Clave API proporciona acceso a todos los datos de tu cuenta. Para regenerarla, ve a <strong>Configuración de la cuenta > Seguridad</strong> y haz clic en <strong>Regenerar clave</strong>. Esto revocará todo el acceso a través de tu Clave API existente y generará una nueva clave aleatoria.
</p>

## Obtener el UID del proyecto

El **UID del proyecto** es un código único que identifica un proyecto específico de KoboToolbox y debe incluirse en las llamadas a la API para apuntar a ese proyecto.

Puedes encontrar el **UID del proyecto** en la URL de la página de resumen de tu proyecto. Es la cadena de letras y números que aparece después de "forms/" en la URL, de la siguiente forma: `https://[server-url]/#/forms/[project asset UID]/summary`.

![Retrieving project asset UID](images/api/project_UID.png)

## Exportar datos usando la API

Hay dos enfoques principales para conectar tus datos usando la API con KoboToolbox:

- **Exportaciones sincrónicas:** Devuelven un archivo CSV o XLSX listo para usar, basado en configuraciones de exportación predefinidas, que las aplicaciones externas (por ejemplo, Power BI o Excel) pueden cargar directamente.
- **Endpoint JSON:** Envía cada registro como un archivo JSON sin procesar. Es la mejor opción para flujos de trabajo basados en código, no para uso directo en hojas de cálculo o herramientas de informes interactivos.

Cada enfoque requiere conocer la URL del servidor y el UID del proyecto para construir una URL de exportación personalizada. Según la aplicación, puede ser necesaria tu Clave API para la autenticación.

<p class="note">
    Para más información sobre las exportaciones sincrónicas, consulta <a href="https://support.kobotoolbox.org/es/synchronous_exports.html">Usar la API para exportaciones sincrónicas</a>.
<br><br>
Para aprender más sobre cómo conectar tus datos a Power BI para crear informes interactivos personalizados, consulta <a href="https://support.kobotoolbox.org/es/pulling_data_into_powerbi.html">Conectar KoboToolbox con Power BI</a>.
<br><br>
Para aprender más sobre cómo conectar tus datos a Microsoft Excel, consulta <a href="https://support.kobotoolbox.org/es/pulling_data_into_excelquery.html">Conectar KoboToolbox con Microsoft Excel</a>.
</p>

## Documentación avanzada

La documentación de la API en `https://[server-url]/api/v2/docs/` ofrece una interfaz interactiva para los endpoints de la API. Reemplaza la información que antes se presentaba en cada endpoint.

| **Servidor de KoboToolbox**    | **Documentación de la API**                     |
| :----------------- | :--------------------------------------------- |
| Servidor Global               | [https://kf.kobotoolbox.org/api/v2/docs/](https://kf.kobotoolbox.org/api/v2/docs/)  |
| Servidor con sede en la Unión Europea       | [https://eu.kobotoolbox.org/api/v2/docs/](https://eu.kobotoolbox.org/api/v2/docs/)  |

Estas páginas de documentación avanzada listan todos los endpoints, muestran los parámetros de consulta permitidos, incluyen una barra de búsqueda, muestran ejemplos de respuestas y de respuestas de error, y permiten probar solicitudes directamente en el navegador. Usa esta documentación para verificar la autenticación, descubrir funciones y copiar las URL exactas en scripts personalizados.

También puedes descargar el esquema de la documentación de la API en formato YAML en `https://[server-url]/api/v2/schema/` o en formato JSON en `https://[server-url]/api/v2/schema/?format=json`.

<p class="note">
    <strong>Nota:</strong> Los endpoints de la V1 están ahora obsoletos, en favor de la API KPI v2, más robusta y con soporte completo. Para más información sobre la migración a KPI v2, consulta <a href="https://support.kobotoolbox.org/es/migrating_api.html">Migración de API v1 a API v2</a>.
</p>

Para ver más ejemplos del uso de la API, consulta esta [publicación del Foro de la comunidad](https://community.kobotoolbox.org/t/kobo-api-examples-using-new-kpi-endpoints/2742).