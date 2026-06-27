# Tipo de pregunta Código de barras/Código QR

El tipo de pregunta "Código de barras/Código QR" se utiliza para escanear, decodificar y capturar códigos de barras y códigos QR con la cámara del dispositivo. Cuando se escanea un código con la cámara, se captura el valor (ya sean números o texto) almacenado en el código.

<p class="note">
  El escaneo de códigos de barras/QR solo funciona al <a href="https://support.kobotoolbox.org/es/kobocollect_on_android_latest.html">usar KoboCollect</a> en dispositivos móviles.
</p>

Se admite una amplia variedad de formatos de códigos de barras y QR, entre los que se incluyen los siguientes:

- UPC-A
- UPC-E
- EAN-8
- EAN-13
- Code 39
- Code 93
- Code 128
- Codabar
- ITF
- RSS-14
- RSS-Expanded
- QR Code
- Data Matrix
- Aztec
- PDF 417
- MaxiCode

Las preguntas de tipo "Código de barras/Código QR" pueden utilizarse en diferentes escenarios, como la gestión de activos o la distribución de artículos. Por ejemplo, puedes escanear un código QR en la tarjeta de identidad de un beneficiario para capturar su número de identificación. Luego puedes usar la función `pulldata()` para completar automáticamente campos a partir de un archivo CSV adjunto a tu proyecto o desde un [proyecto vinculado](dynamic_data_attachment.md) con información sobre el beneficiario. Puedes obtener más información sobre la función `pulldata()` [aquí](https://xlsform.org/en/#how-to-pull-data-from-csv).

## Cómo configurar el tipo de pregunta "Código de barras/Código QR"

### Configuración en el editor de formularios de KoboToolbox (Formbuilder)

Para agregar una pregunta de tipo "Código de barras/Código QR":

- Haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "Captura el código de identificación del beneficiario", luego haz clic en **AGREGAR PREGUNTA** o presiona ENTER en tu teclado
- Elige el tipo de pregunta

![Agregar preguntas de Código de barras/Código QR](images/barcode_qrcode_questions/adding_barcode_qrcode_questions.gif)

### Configuración en XLSForm

Para agregar una pregunta de tipo "Código de barras/Código QR" en XLSForm, agrega una pregunta con el tipo `barcode` de la siguiente manera:

| type    | name           | label                                          |
| :------ | :------------- | :--------------------------------------------- |
| barcode | beneficiary_id | Capture the beneficiary ID code (Captura el código de identificación del beneficiario) |
| survey  |

## Cómo se muestran las preguntas de tipo "Código de barras/Código QR" en formularios web y KoboCollect

### Aspecto predeterminado

![Aspecto predeterminado de las preguntas de Código de barras/Código QR](images/barcode_qrcode_questions/barcode_qrcode_default.png)

### Aspecto avanzado

Al agregar el tipo de pregunta "Código de barras/Código QR", puedes cambiar la configuración de aspecto para pasar de usar la cámara trasera predeterminada del dispositivo a usar la cámara frontal.

### Cambiar el aspecto avanzado en el Formbuilder

Ve a la configuración de la pregunta "Código de barras/Código QR" y escribe "front" en el campo "Aspecto (avanzado)".

![Cambiar el aspecto de las preguntas de Código de barras/Código QR](images/barcode_qrcode_questions/change_appearance_barcode_qrcode_questions.png)

### Cambiar el aspecto avanzado en XLSForm

En XLSForm, puedes configurar la cámara predeterminada para capturar el "Código de barras/Código QR" como la cámara frontal escribiendo 'front' en la columna `appearance` de la siguiente manera:

| type    | name             | label                                          | appearance |
| :------ | :--------------- | :--------------------------------------------- | :--------- |
| barcode | beneficiary_id_2 | Capture the beneficiary ID code (Captura el código de identificación del beneficiario) | front      |
| survey  |

<p class="note">
  Puedes descargar un XLSForm con ejemplos de este artículo
  <a
    download
    class="reference"
    href="./_static/files/barcode_qrcode_questions/barcode_qrcode_questions.xlsx"
    >aquí</a
  >.
</p>