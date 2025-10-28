# Uso de etiquetas HXL
<a href="../hxl.html">Read in English</a> | <a href="../fr/hxl.html">Lire en français</a> | <a href="../ar/hxl.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/hxl.md" class="reference">29 Jul 2025</a>

## ¿Qué es exactamente HXL?

HXL significa **Humanitarian Exchange Language** (Lenguaje de Intercambio Humanitario). El objetivo de HXL es mejorar
el intercambio de información durante una crisis humanitaria mediante la creación de una forma sencilla de
promover la interoperabilidad de los datos. Esto lo hace codificando los datos a través de
hashtags (#) similar a Twitter. Para obtener más información sobre HXL, por favor
[visita aquí](https://hxlstandard.org).

## Cómo usar la función HXL en el editor de formularios

_Créditos: [David Megginson](http://www.megginson.com)_ _Enlace a la
[guía de presentación paso a paso](https://docs.google.com/presentation/d/123bHSkNh4T30CNq0i37IxOLfrqSC-3V_Khtkf6bIdg0/edit#slide=id.p)_

1. Después de iniciar un formulario y crear una pregunta, ve a Configuración de la pregunta y
   en la pestaña Opciones de la pregunta, elige tu etiqueta HXL y añade atributos.

    ![image](/images/hxl/hxl.gif)

2. Después de que el formulario haya sido creado, el proyecto desplegado y los datos hayan sido
   recolectados, ve a la pestaña Descargas en la página DATOS. Selecciona el tipo de exportación
   como XLS y asegúrate de seleccionar **Valores y encabezados XML** para el formato de valores y
   encabezados. Luego Exportar.

    ![image](/images/hxl/xml_values.gif)

3. Una vez que hayas exportado y descargado los datos a tu computadora, abre el
   archivo XLS para ver tus etiquetas HXL. No hay problema en tener metadatos de Kobo que no
   tengan hashtags HXL.

    ![image](/images/hxl/xls_affected.jpg)

<p class="note">El hashtag antes del nombre es obligatorio y no se permiten espacios.</p>

## Cómo usar HXL en un XLSForm

Al crear un XLSForm, simplemente inserta una columna adicional en cualquier hoja de cálculo
existente y llénala con hashtags HXL que identifiquen el tipo de información en
cada columna.

**hoja survey**

| type                 | name     | label                                      | hxl        |
| :------------------- | :------- | :----------------------------------------- | :--------- |
| select_one countries | country  | Selecciona el país afectado                | #country   |
| select_one admin1    | province | Por favor selecciona la provincia          | #adm1+code |
| select_one admin2    | county   | Selecciona el condado                      | #adm2+name |
| select_one sector    | cluster  | Clúster                                    | #sector    |
| integer              | affected | Número de personas afectadas               | #affected  |
| integer              | reached  | Número de personas alcanzadas hasta la fecha | #reached   |
| survey |