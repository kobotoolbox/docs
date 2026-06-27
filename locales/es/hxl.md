# Uso de etiquetas HXL

## ¿Qué es exactamente HXL?

HXL son las siglas de **Humanitarian Exchange Language** (Lenguaje de Intercambio Humanitario). El objetivo de HXL es mejorar el intercambio de información durante una crisis humanitaria mediante la creación de una forma sencilla de promover la interoperabilidad de los datos. Para ello, codifica los datos mediante hashtags (#) similares a los de Twitter. Para obtener más información sobre HXL, [visita este enlace](https://hxlstandard.org).

## Cómo usar la función HXL en el editor de formularios de KoboToolbox **(Formbuilder)**

_Créditos: [David Megginson](http://www.megginson.com)_ _Enlace a la [guía paso a paso en diapositivas](https://docs.google.com/presentation/d/123bHSkNh4T30CNq0i37IxOLfrqSC-3V_Khtkf6bIdg0/edit#slide=id.p)_

1. Después de iniciar un formulario y crear una pregunta, ve a Configuración de la pregunta y, en la ventana Opciones de pregunta, elige tu etiqueta HXL y agrega atributos.

    ![image](/images/hxl/hxl.gif)

2. Una vez creado el formulario, implementado el proyecto y recolectados los datos, ve a la ventana Descargas en la página de Datos. Selecciona el tipo de exportación XLS y asegúrate de seleccionar **Valores y encabezados XML** como formato de valores y encabezados. Luego haz clic en Exportar.

    ![image](/images/hxl/xml_values.gif)

3. Una vez que hayas exportado y descargado los datos en tu computadora, abre el archivo XLS para ver tus etiquetas HXL. No hay problema si hay metadatos de Kobo que no tengan hashtags HXL.

    ![image](/images/hxl/xls_affected.jpg)

<p class="note">El hashtag antes del nombre es obligatorio y no se permiten espacios.</p>

## Cómo usar HXL en un XLSForm

Al crear un XLSForm, simplemente inserta una columna adicional en cualquier hoja de cálculo existente y rellénala con hashtags HXL que identifiquen el tipo de información en cada columna.

**hoja survey**

| type                 | name     | label                                        | hxl        |
| :------------------- | :------- | :------------------------------------------- | :--------- |
| select_one countries | country  | Select affected country                      | #country   |
| select_one admin1    | province | Please select the province                   | #adm1+code |
| select_one admin2    | county   | Select the county                            | #adm2+name |
| select_one sector    | cluster  | Cluster                                      | #sector    |
| integer              | affected | Number of people affected                    | #affected  |
| integer              | reached  | Number of people reached to date             | #reached   |
| survey |