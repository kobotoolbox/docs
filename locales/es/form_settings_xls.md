# Configuración de formularios en XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/form_settings_xls.md" class="reference">23 Apr 2026</a>

XLSForm te permite configurar ajustes para tus formularios usando la **hoja settings**. Por ejemplo, puedes especificar un título de formulario, establecer un idioma predeterminado o hacer seguimiento de los números de versión.

Este artículo explica cómo agregar y utilizar los ajustes de formulario disponibles en XLSForm.

## Agregar configuración de formularios en XLSForm

Para agregar configuración de formularios en XLSForm:
1. Añade una **hoja settings** a tu XLSForm.
2. Crea una nueva columna para cada ajuste, usando el nombre de columna exacto que se muestra [en la tabla a continuación](https://support.kobotoolbox.org/es/form_settings_xls.html#available-form-settings-in-xlsform).
3. Bajo cada ajuste, especifica el valor correspondiente (ver ejemplo a continuación).

**hoja settings**

| form_title            | version | default_language | style |
|:----------------------|:--------|:----------------|:------|
| Configuración de formularios en XLSForm | v3     | English (en)    | pages |
| settings |

## Configuración de formularios disponible en XLSForm

La configuración de formularios disponible en XLSForm incluye:

| Configuración del formulario | Descripción |
|:----------------------------|:------------|
| <code>form_title</code>     | Especifica el título del formulario que se muestra a los usuarios. También se puede establecer y gestionar en KoboToolbox cuando se carga el formulario. |
| <code>version</code>        | Incluye una cadena de texto que representa la versión actual del XLSForm (por ejemplo, v1 o YYYYMMDD). Útil para hacer seguimiento de las versiones del formulario en proyectos colaborativos. |
| <code>instance_name</code>  | Especifica un nombre único para cada envío del formulario usando los campos completados por el usuario durante la encuesta. Aparece en la tabla de datos para cada envío. Se puede usar para crear identificadores personalizados de participantes o envíos.<br><br>Por ejemplo, <code>concat(${lname}, '-', ${fname}, '-', today())</code> devuelve <code>apellido-nombre-fecha</code>. |
| <code>default_language</code> | Establece el idioma predeterminado en <a href="https://support.kobotoolbox.org/es/language_xls.html">formularios con traducciones</a>. Se usa el formato <code>idioma (código)</code>, según lo definido en el <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">sitio web del registro de subetiquetas de idioma de la IANA</a>. |
| <code>style</code>          | Especifica un <a href="https://support.kobotoolbox.org/es/form_style_xls.html">tema alternativo para formularios web</a>. |
| <code>allow_choice_duplicates</code> | Permite que un XLSForm reutilice nombres de opciones duplicados **dentro** de una lista de opciones (por ejemplo, al usar filtros de selección donde los nombres de opciones están duplicados). |
| <code>public_key</code>     | Especifica la clave pública para <a href="https://support.kobotoolbox.org/es/encrypting_forms.html?highlight=encryption">formularios con cifrado habilitado</a>. |