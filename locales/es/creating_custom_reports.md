# Visualizar datos utilizando informes personalizados
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6e9f496956ced232adb4985272fbee0a6465318d/source/creating_custom_reports.md" class="reference">15 Jun 2026</a>

KoboToolbox incluye una herramienta de informes que puedes usar para monitorear los datos entrantes y ver estadísticas descriptivas simples. Puedes usar los informes para mostrar gráficos, revisar el recuento de respuestas, comparar respuestas por subgrupo, y compartir o imprimir un resumen de las preguntas seleccionadas del formulario.

<p class="note">
<strong>Nota:</strong>
    Los informes pueden ayudarte a revisar tus datos de un vistazo, pero no reemplazan la limpieza, el procesamiento, el análisis ni la visualización de datos en profundidad con herramientas externas. Para un análisis más detallado, KoboToolbox facilita <a href="https://support.kobotoolbox.org/es/export_download.html">exportar tus datos</a> o conectarlos a <a href="https://support.kobotoolbox.org/es/synchronous_exports.html">herramientas externas mediante la API</a>.
</p>

Este artículo explica cómo acceder a los informes de datos en KoboToolbox, personalizar los estilos de informe, crear informes personalizados y gestionar los permisos de los informes.

## Acceder a los informes de datos

Para acceder a los informes de tu proyecto:

1. Abre tu proyecto.
2. Ve a **DATOS.**
3. Haz clic en <i class="k-icon-reports"></i> **Informes.**

El informe predeterminado incluye todas las preguntas de tu formulario. Cada pregunta se muestra con un gráfico predeterminado y una tabla de datos. El informe también muestra el **tipo de pregunta** y el **número de envíos** con una respuesta a esa pregunta.

![Informes de datos](images/creating_custom_reports/reports.png)

Puedes imprimir el informe o guardarlo como PDF haciendo clic en el botón <i class="k-icon-print"></i> **imprimir** en la esquina superior derecha. También puedes usar <i class=" k-icon-expand"></i> **alternar pantalla completa** para ver el informe en toda la pantalla.

## Personalizar tu informe

Puedes personalizar el estilo y la configuración de tu informe haciendo clic en <i class="k-icon-settings"></i> **Configurar estilo del informe.** Los cambios realizados aquí se aplicarán a todos los gráficos y tablas después de hacer clic en **Guardar.**

![Configurar estilo del informe](images/creating_custom_reports/configure.png)

Las siguientes configuraciones están disponibles:

| Configuración | Descripción |
|:---|:---|
| Tipo de gráfico | El tipo de gráfico predeterminado es un gráfico de barras vertical. Puedes seleccionar un tipo de gráfico diferente para aplicar a todos los gráficos del informe. |
| Colores | Puedes elegir una combinación de colores diferente para todos los gráficos del informe. |
| Agrupar por | Puedes seleccionar una pregunta de tipo **Seleccionar una** de tu formulario para agrupar los gráficos y tablas por esa variable. Esto puede ser útil para comparaciones simples de subgrupos. |
| Traducción | Si tu formulario tiene varios idiomas, puedes elegir qué idioma mostrar en el informe. |


## Personalizar preguntas individuales

También puedes personalizar gráficos individuales en el informe.

Para personalizar un gráfico:

1. Encuentra el gráfico que quieres editar.
2. Haz clic en <i class="k-icon-more"></i> **Anular el estilo de gráfico** en la esquina superior derecha del gráfico.
3. Selecciona un tipo de gráfico o una combinación de colores.

![Anular el estilo de gráfico para personalizar el estilo del gráfico](images/creating_custom_reports/override.png)

Estas configuraciones se aplican únicamente al gráfico seleccionado.

## Crear un informe personalizado

Además del informe predeterminado, puedes crear informes personalizados. Los informes personalizados te permiten elegir qué preguntas incluir y guardar configuraciones de informe personalizadas.

Para crear un informe personalizado:

1. Haz clic en <i class="k-icon-plus"></i> **Crear nuevo informe** junto a **Informe predeterminado.**
2. Ingresa un título para tu informe personalizado.
3. Selecciona las preguntas que quieres incluir y haz clic en **Guardar.**
4. Haz clic en <i class="k-icon-settings"></i> **Configurar estilo del informe** para establecer el estilo y la configuración del informe.

![Crear informe personalizado](images/creating_custom_reports/new.png)

Para cambiar el título o las preguntas mostradas en un informe personalizado, haz clic en <i class="k-icon-edit"></i> **Editar preguntas del informe.**

<p class="note">
<strong>Nota:</strong> La configuración de los informes personalizados se guarda y seguirá disponible cuando salgas y vuelvas.
</p>

## Permisos y uso compartido

Los usuarios con permiso de **Ver envíos** pueden ver los informes de datos, incluidos los informes personalizados creados por otros usuarios. Sin embargo, no pueden configurar estilos de informe ni crear informes personalizados.

Los usuarios con permiso de **Gestionar el proyecto** pueden ver los informes, configurar estilos de informe y crear informes personalizados.

<p class="note">
  Para obtener más información sobre permisos y uso compartido, consulta <a class="reference external" href="https://support.kobotoolbox.org/es/managing_permissions.html">Compartir proyectos con permisos a nivel de usuario/a</a>.
</p>