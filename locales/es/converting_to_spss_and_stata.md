# Convertir datos a SPSS y Stata
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/converting_to_spss_and_stata.md" class="reference">15 Feb 2022</a>


<p class="note">
  Este artículo te ayuda a convertir tus datos a <strong>SPSS</strong> y
  <strong>Stata</strong>. Ten en cuenta que necesitas
  <strong>IBM SPSS</strong> o <strong>Stata</strong>, que son aplicaciones
  de terceros.
</p>

Dado que **KoboToolbox** no exporta datos directamente en formato **SPSS** o **Stata**, este artículo te servirá de guía para realizar la conversión.

## Convertir a SPSS

1. Descarga tus datos en formato XLS siguiendo las instrucciones del
   [Exportar y descargar datos](export_download.md) o como se muestra en la imagen
   a continuación.

    ![Exportar XLS](/images/converting_to_spss_and_stata/export_xls.gif)

2. Descarga las **Etiquetas SPSS** desde la misma ventana **DATOS** como se
   muestra en la imagen a continuación. Este proceso generará una carpeta
   comprimida que contiene la sintaxis de **SPSS**.

    ![Exportar etiquetas SPSS](/images/converting_to_spss_and_stata/export_spss_labels.gif)

3. Necesitarás **IBM SPSS** para importar los datos en XLS mediante el siguiente
   método, que es compatible con todas las versiones de **SPSS**.

    - En **SPSS**, haz clic en **File -> Open -> Data** (como se muestra a continuación).
    - Una vez que hagas clic en la ventana **Data**, verás una caja de diálogo.
      En el campo **Files of type**, selecciona **Excel**.
    - Ve a la carpeta que contiene tu archivo **Excel** y busca el archivo
      **Excel** con los datos que descargaste.
    - Abre el archivo y aparecerá la caja de diálogo **Read Excel File**.

    ![Importar a SPSS](/images/converting_to_spss_and_stata/import_into_spss.gif)

4. Ahora abre la sintaxis que descargaste en el _Paso 2_ y ejecútala.

    ![Ejecutar sintaxis](/images/converting_to_spss_and_stata/run_syntax.jpg)

Ya puedes manipular tus datos en **SPSS**.

## Convertir el archivo SPSS a un archivo Stata

Lamentablemente, no existe la opción de descargar directamente un archivo **SPSS DO**. Debes seguir el proceso anterior y luego guardar los datos finales como un archivo `.dta` de **Stata**.

Asegúrate de seleccionar todas las opciones que necesites al guardar.

![Datos dta](/images/converting_to_spss_and_stata/dta_data.jpg)