# Uso de la API para exportaciones sincrónicas
<a href="../synchronous_exports.html">Read in English</a> | <a href="../fr/synchronous_exports.html">Lire en français</a> | <a href="../ar/synchronous_exports.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/a4e0388d846fe94926c32f6dacb82b6e34c7f102/source/synchronous_exports.md" class="reference">13 Sep 2025</a>

<iframe src="https://www.youtube.com/embed/qrkLi3VixVs?si=UXE40HQX2jEQrjBs" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox ofrece dos métodos principales para acceder a tus datos: exportaciones asincrónicas y sincrónicas. El método asincrónico estándar implica [descargar manualmente archivos de datos](https://support.kobotoolbox.org/export_download.html) que contienen todos los envíos hasta el momento de la descarga. En contraste, las exportaciones sincrónicas permiten la integración automática de tus datos de KoboToolbox con aplicaciones externas como Microsoft Power BI, Excel o Google Sheets.

Con las exportaciones sincrónicas, tus datos se actualizan automáticamente a medida que se reciben nuevos envíos, eliminando la necesidad de actualizar manualmente. Este método proporciona un archivo CSV o XLSX, configurado con tus ajustes de exportación predefinidos, que pueden incluir etiquetas de preguntas, idiomas, filtros y datos de grupos de repetición.

<p class="note">
    <strong>Nota:</strong> Este artículo se centra en las exportaciones sincrónicas, que es una de las dos formas principales de usar la API de KoboToolbox. La otra es la API JSON, diseñada para scripts personalizados y automatizaciones en tiempo real, que entrega datos JSON sin procesar, registro por registro. A diferencia de las exportaciones sincrónicas, la API JSON no incluye funcionalidades avanzadas de exportación como etiquetas de preguntas o soporte para múltiples idiomas.
</p>

Este artículo cubre los siguientes pasos:

- Generar una exportación con nombre
- Recuperar el enlace de exportación sincrónica
- Conectar tus datos a una aplicación externa y autenticación
  
## Generar una exportación con nombre

Para generar exportaciones sincrónicas, primero debes crear una exportación con nombre para tu proyecto siguiendo estos pasos:

1. En tu proyecto de KoboToolbox, navega a la ventana **DATOS > Descargas**.
2. Ajusta la [configuración de exportación](https://support.kobotoolbox.org/export_download.html) según sea necesario.
3. Haz clic en **Opciones avanzadas** para [personalizar los datos](https://support.kobotoolbox.org/advanced_export.html) para la exportación.
4. Elige **Guardar selección como…** y proporciona un nombre para tu exportación.
5. Haz clic en **Exportar** para guardar esta configuración.

## Recuperar el enlace de exportación sincrónica

Para recuperar el enlace de exportación sincrónica, necesitarás lo siguiente:

- **UID del activo del proyecto:** Un ID único para cada proyecto de KoboToolbox, que se encuentra en la URL del proyecto.
- **URL del servidor:** La URL del servidor que estás usando (`kf.kobotoolbox.org` para el Servidor Global, `eu.kobotoolbox.org` para el Servidor con sede en la Unión Europea, o `[tu organización].kobotoolbox.org` para servidores privados).

<p class="note">
    Para obtener más información sobre cómo recuperar la URL del servidor y el UID del activo del proyecto, consulta <a href="https://support.kobotoolbox.org/api.html">Primeros pasos con la API</a>.
</p>

Para recuperar el enlace de exportación, sigue estos pasos:

1. Abre una nueva pestaña del navegador.
2. Reemplaza tu **URL del servidor** y **UID del activo del proyecto** en la siguiente URL: `https://[server_url]/api/v2/assets/[project_asset_uid]/export-settings/`.
3. Abre la página web correspondiente a la URL modificada.
4. Desplázate hasta la sección **CURRENT ENDPOINT**.
5. Encuentra la configuración de exportación que coincida con la exportación con nombre que creaste en el primer paso.
6. Localiza los enlaces `data_url_csv` y `data_url_xlsx`, que son los enlaces de exportación sincrónica de tu proyecto.
7. Copia el enlace que mejor se adapte a tus necesidades (archivo CSV o XLSX).

![Recuperar enlace de exportación sincrónica](images/synchronous_exports/export_link.png)

<p class="note">
    <strong>Nota:</strong> Los grupos de repetición se exportan como hojas separadas en archivos de Excel y no se incluyen en las exportaciones CSV. Si tu proyecto contiene grupos de repetición, usa el enlace <code>data_url_xlsx</code>.
</p>

## Conectar tus datos a una aplicación externa

Después de recuperar el enlace de exportación sincrónica, puedes conectar tus datos a tu aplicación externa preferida. El método para integrar el enlace de exportación sincrónica variará según la aplicación.

<p class="note">
    Para aprender cómo conectar tus datos a Power BI para crear paneles personalizados, consulta <a href="https://support.kobotoolbox.org/pulling_data_into_powerbi.html">Conectar KoboToolbox a Power BI</a>. 
    <br><br>
    Para aprender cómo conectar tus datos a Microsoft Excel, consulta <a href="https://support.kobotoolbox.org/pulling_data_into_excelquery.html">Conectar KoboToolbox a Microsoft Excel</a>.
</p>

### Autenticación

Muchas aplicaciones externas pueden conectarse a tus datos de KoboToolbox. Sin embargo, no todas admiten **solicitudes autenticadas**, que son solicitudes que llevan credenciales (por ejemplo, la clave API o nombre de usuario/a y contraseña) para que el servidor pueda verificar la identidad del/de la solicitante. Si la aplicación externa no admite solicitudes autenticadas, solo podrá acceder a recursos que se hayan hecho **públicamente accesibles** a través de un enlace de exportación anónimo.

Para conectar tu proyecto sin autenticación (por ejemplo, a Google Sheets), deberás asegurarte de que la opción "Cualquiera puede ver los envíos realizados a este formulario" esté marcada en **CONFIGURACIÓN > Compartir**.

<p class="note">
    Para obtener más información sobre cómo compartir proyectos, consulta <a href="https://support.kobotoolbox.org/project_sharing_settings.html">Compartir proyectos con configuraciones a nivel de proyecto</a>.
</p>

Para proyectos con datos sensibles o privados, la opción "Cualquiera puede ver los envíos realizados a este formulario" debe permanecer sin marcar. En estos casos, considera usar solo aplicaciones que admitan solicitudes autenticadas.

Cuando uses aplicaciones que admiten solicitudes autenticadas, como Power BI, se te pedirá autenticación básica con tu nombre de usuario/a y contraseña o un token (también llamado clave API) para acceder a los datos. Tu clave API se encuentra en tu **CONFIGURACIÓN DE CUENTA** en la pestaña **Seguridad**.

<p class="note">
    Para obtener más información sobre la clave API, consulta <a href="https://support.kobotoolbox.org/api.html">Primeros pasos con la API</a>.
</p>

## Limitaciones

Para mantener la confiabilidad del servidor, las exportaciones sincrónicas tienen las siguientes limitaciones:

- **Intervalo de actualización de datos:** Los datos en las exportaciones sincrónicas se actualizan cada 5 minutos. Las solicitudes de exportación realizadas dentro de esta ventana de 5 minutos no incluirán los datos de nuevos envíos recibidos dentro del intervalo de 5 minutos.
- **Tiempo de finalización de exportación:** Las exportaciones deben completarse en 120 segundos. Los proyectos con un gran número de envíos o preguntas pueden fallar. Para evitar esto, agrega una restricción de consulta en la configuración de exportación para limitar los envíos o filtrar preguntas innecesarias. Consulta esta [publicación del Foro de la comunidad](https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4) para obtener orientación.