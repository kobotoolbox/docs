# Usar la API para exportaciones sincrónicas
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/b0d195136b7fb3fe51b687cc03a5e8dcde946309/source/synchronous_exports.md" class="reference">22 Jun 2026</a>


<iframe src="https://www.youtube.com/embed/qrkLi3VixVs?si=UXE40HQX2jEQrjBs&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox ofrece dos métodos principales para acceder a tus datos: exportaciones asincrónicas y sincrónicas. El método asincrónico estándar consiste en [descargar manualmente archivos de datos](../es/export_download.md) que contienen todos los envíos hasta el momento de la descarga. En cambio, las exportaciones sincrónicas permiten la integración automática de tus datos de KoboToolbox con aplicaciones externas como Microsoft Power BI, Excel o Google Sheets.

Con las exportaciones sincrónicas, tus datos se actualizan automáticamente a medida que se reciben nuevos envíos, lo que elimina la necesidad de actualizar manualmente. Este método proporciona un archivo CSV o XLSX configurado con tus ajustes de exportación predefinidos, que pueden incluir etiquetas de preguntas, idiomas, filtros y datos de grupos de repetición.

<p class="note">
    <strong>Nota:</strong> Este artículo se centra en las exportaciones sincrónicas, que es una de las dos formas principales de usar la API de KoboToolbox. La otra es la API JSON, diseñada para scripts personalizados y automatizaciones en tiempo real, que entrega datos JSON sin procesar, registro por registro. A diferencia de las exportaciones sincrónicas, la API JSON no incluye funciones avanzadas de exportación como etiquetas de preguntas ni compatibilidad con varios idiomas.
</p>

Este artículo cubre los siguientes pasos:

- Generar una exportación con nombre
- Recuperar el enlace de exportación sincrónica
- Conectar tus datos a una aplicación externa y autenticación

<p class="note">
    Para una introducción a la API de KoboToolbox, consulta <a href="../es/api.md">Introducción a la API</a>.
</p>

## Generar una exportación con nombre

Para generar exportaciones sincrónicas, primero debes crear una exportación con nombre para tu proyecto siguiendo estos pasos:

1. En tu proyecto de KoboToolbox, ve a la ventana **DATOS > Descargas**.
2. Ajusta la [configuración de exportación](../es/export_download.md) según sea necesario.
3. Haz clic en **Opciones avanzadas** para [personalizar los datos](../es/advanced_export.md) que se exportarán.
4. Elige **Guardar selección como…** e ingresa un nombre para tu exportación.
5. Haz clic en **Exportar** para guardar esta configuración.

## Recuperar el enlace de exportación sincrónica

Para recuperar el enlace de exportación sincrónica, necesitarás lo siguiente:

- **UID del proyecto:** Un ID único para cada proyecto de KoboToolbox, que se encuentra en la URL del proyecto.
- **URL del servidor:** La URL del servidor que estás usando (`kf.kobotoolbox.org` para el Servidor Global, `eu.kobotoolbox.org` para el Servidor con sede en la Unión Europea, o la URL del servidor privado de tu organización).

<p class="note">
    Para obtener más información sobre cómo recuperar la URL del servidor y el UID del proyecto, consulta <a href="../es/api.md">Introducción a la API</a>.
</p>

Para recuperar el enlace de exportación, sigue estos pasos:

1. Abre una nueva pestaña del navegador.
2. Reemplaza la **URL del servidor** y el **UID del proyecto** en la siguiente URL: `https://[server_url]/api/v2/assets/[project_asset_uid]/export-settings/`.
3. Abre la página web correspondiente a la URL modificada.
4. Desplázate hasta la sección **CURRENT ENDPOINT**.
5. Encuentra la configuración de exportación que coincida con la exportación con nombre que creaste en el primer paso.
6. Localiza los enlaces `data_url_csv` y `data_url_xlsx`, que son los enlaces de exportación sincrónica de tu proyecto.
7. Copia el enlace que mejor se adapte a tus necesidades (archivo CSV o XLSX).

![Recuperar el enlace de exportación sincrónica](images/synchronous_exports/export_link.png)

<p class="note">
    <strong>Nota:</strong> Los grupos de repetición se exportan como hojas separadas en archivos de Excel y no se incluyen en las exportaciones CSV. Si tu proyecto contiene grupos de repetición, usa el enlace <code>data_url_xlsx</code>.
</p>

## Conectar tus datos a una aplicación externa

Después de recuperar el enlace de exportación sincrónica, puedes conectar tus datos a la aplicación externa que prefieras. El método para integrar el enlace de exportación sincrónica varía según la aplicación.

<p class="note">
    Para aprender a conectar tus datos a Power BI y crear informes interactivos personalizados, consulta <a href="../es/pulling_data_into_powerbi.md">Conectar KoboToolbox con Power BI</a>.
    <br><br>
    Para aprender a conectar tus datos a Microsoft Excel, consulta <a href="../es/pulling_data_into_excelquery.md">Conectar KoboToolbox con Microsoft Excel</a>.
</p>

### Autenticación

Muchas aplicaciones externas pueden conectarse a tus datos de KoboToolbox. Sin embargo, no todas admiten **solicitudes autenticadas**, es decir, solicitudes que incluyen credenciales (por ejemplo, la clave API o el nombre de usuario y contraseña) para que el servidor pueda verificar la identidad del solicitante. Si la aplicación externa no admite solicitudes autenticadas, solo podrá acceder a los recursos que se hayan hecho **accesibles públicamente** mediante un enlace de exportación anónimo.

Para conectar tu proyecto sin autenticación (por ejemplo, a Google Sheets), debes asegurarte de que la opción "Cualquier persona puede ver los envíos que se realizan a través de este formulario" esté marcada en **CONFIGURACIÓN > Compartir**.

<p class="note">
    Para obtener más información sobre cómo compartir proyectos, consulta <a href="../es/project_sharing_settings.md">Compartir proyectos con configuraciones a nivel de proyecto</a>.
</p>

En el caso de proyectos con datos sensibles o privados, la opción "Cualquier persona puede ver los envíos que se realizan a través de este formulario" debe permanecer desmarcada. En estos casos, considera usar únicamente aplicaciones que admitan solicitudes autenticadas.

Al usar aplicaciones que admiten solicitudes autenticadas, como Power BI, se te pedirá autenticación básica con tu nombre de usuario y contraseña, o un token (también llamado clave API) para acceder a los datos. Tu clave API se encuentra en **CONFIGURACIÓN DE LA CUENTA**, en la ventana **Seguridad**.

<p class="note">
    Para obtener más información sobre la clave API, consulta <a href="../es/api.md">Introducción a la API</a>.
</p>

## Limitaciones

Para mantener la fiabilidad del servidor, las exportaciones sincrónicas tienen las siguientes limitaciones:

- **Intervalo de actualización de datos:** Los datos en las exportaciones sincrónicas se actualizan cada 5 minutos. Las solicitudes de exportación realizadas dentro de este intervalo de 5 minutos no incluirán los nuevos datos de envío recibidos durante ese período.
- **Tiempo de finalización de la exportación:** Las exportaciones deben completarse en 120 segundos. Los proyectos con un gran número de envíos o preguntas pueden fallar. Para evitarlo, añade una restricción de consulta en la configuración de exportación para limitar los envíos o filtrar las preguntas innecesarias. Consulta esta [publicación del Foro de la comunidad](https://community.kobotoolbox.org/t/how-to-download-data-between-two-dates-from-date-to-date/25569/4) para obtener orientación.

## Resolución de problemas

<details>
  <summary><strong>Las URL de archivos multimedia de exportaciones anteriores ya no funcionan</strong></summary>
Los usuarios que dependen de URL de archivos multimedia de exportaciones sincrónicas anteriores pueden notar que estos enlaces ya no funcionan desde que <a href="../es/migrating_api.md">se deprecó la API v1</a>.
<br><br>
Las URL afectadas usan el formato antiguo:
<code>https://kc.kobotoolbox.org/media/original?media_file=...</code>
<br><br>
Para solucionar este problema, vuelve a crear tus exportaciones sincrónicas con la opción <strong>Incluir URL de archivos multimedia</strong> seleccionada. La nueva exportación incluirá URL de archivos multimedia actualizadas.
</details>