# Importar un XLSForm a través de URL

Al importar un XLSForm a través de una URL, asegúrate de que la URL apunte directamente al archivo XLS y que sea de acceso público. Una forma rápida de comprobarlo es cargar la URL en un navegador: debería activar la descarga del archivo. (Si carga una página en el navegador, entonces no es la URL correcta.)

## Google Sheets

Para obtener el enlace correcto de una hoja de cálculo de Google Sheets, sigue estos pasos:

1. Haz clic en **Archivo > Publicar** en la web.

2. En el menú desplegable **Página web**, selecciona **Microsoft Excel (.xlsx)**. Mantén seleccionada la opción **Todo el documento** en el menú desplegable anterior.

3. Copia el enlace del campo resultante.

    ![image](/images/xls_url/link.jpg)

**Nota para usuarios avanzados:** en nuestras pruebas, la casilla "Volver a publicar automáticamente cuando se realicen cambios" no siempre funciona bien. Es posible que tengas que dejar de publicar y volver a publicar la hoja de cálculo para obtener un enlace actualizado.

## Dropbox

Para obtener el enlace correcto de una hoja de cálculo en Dropbox, sigue estos pasos:

1. Asegúrate de que el archivo XLSForm esté en una carpeta pública de Dropbox en tu cuenta.

2. Copia su enlace. Debe terminar con el sufijo `?dl=0`. Reemplaza el 0 por 1, de modo que el enlace termine en `?dl=1`.