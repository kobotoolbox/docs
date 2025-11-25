# Importar un XLSForm a través de URL
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/d14c3f76675d9085da27e1c5dd4fcf981a6b3a7d/source/xls_url.md" class="reference">7 ene 2025</a>

Al importar un XLSForm a través de URL, asegúrate de que la URL apunte directamente al archivo XLS y que sea de acceso público. Una forma rápida de probar esto es cargar la URL en un navegador: debería activar la descarga del archivo. (Si carga una página en el navegador, entonces no es la URL correcta.)

## Google Sheets

Para obtener el enlace correcto de una hoja de cálculo de Google Sheets, sigue estos pasos:

1. Haz clic en **Archivo > Publicar** en la Web.

2. En el menú desplegable **Página web**, selecciona **Microsoft Excel (.xlsx)**. Mantén seleccionado **Documento completo** en el menú desplegable anterior.

3. Copia el enlace del campo resultante.

    ![image](/images/xls_url/link.jpg)

**Nota para usuarios/as avanzados/as:** en nuestras pruebas, la casilla de verificación "Volver a publicar automáticamente cuando se realicen cambios" no siempre funciona bien. Es posible que necesites detener la publicación y volver a publicar la hoja de cálculo para obtener un enlace actualizado.

## Dropbox

Para obtener el enlace correcto de una hoja de cálculo en Dropbox, sigue estos pasos:

1. Asegúrate de que el archivo XLSForm esté en una carpeta pública de Dropbox en tu cuenta.

2. Copia su enlace. Debería terminar con el sufijo `?dl=0`. Reemplaza el 0 con 1, de modo que tu enlace termine en `?dl=1`.