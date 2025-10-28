# Configuración del formulario y metadatos
<a href="../form_meta.html">Read in English</a> | <a href="../fr/form_meta.html">Lire en français</a> | <a href="../ar/form_meta.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/86f7750dca7b9470d220501253fb365b38924706/source/form_meta.md" class="reference">24 Sep 2025</a>

En el editor de formularios, hay una serie de configuraciones opcionales que puedes establecer para tu proyecto. Puedes acceder a estas haciendo clic en el botón **Diseño y Configuración**.

![Form meta](/images/form_meta/form_meta.png)

## Estilo del formulario

Puedes cambiar la forma en que aparece el formulario en los formularios web de Enketo, como páginas múltiples, tema de cuadrícula, etc., en el menú desplegable **Estilos de Formulario**. Aprende más sobre los diferentes estilos de formulario [aquí](alternative_enketo.md).

## Metadatos del formulario

Los metadatos son preguntas ocultas que pueden ayudar en el análisis de datos y pueden utilizarse para fines de auditoría e integridad de datos. Los metadatos se capturan en segundo plano durante el proceso normal de recolección de datos:

| Metadatos              | Descripción                                                                                                                                                                      |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hora de inicio         | Fecha y hora al abrir el formulario (marca de tiempo)                                                                                                                            |
| Hora de finalización   | Fecha y hora al finalizar el formulario (se presionó el botón "Enviar")                                                                                                          |
| Hoy                    | La fecha de envío del formulario                                                                                                                                                 |
| Nombre de usuario/a    | El nombre de usuario/a del/la encuestador/a si se utiliza [autenticación](managing_permissions.md#requiring-passwords-for-accessing-enketo-web-forms) para la recolección de datos |
| Auditoría              | Registrar un registro de auditoría mientras se completa el formulario. Aprende más sobre el registro de auditoría [aquí](audit_logging.md)                                       |
| Audio de fondo         | Grabar audio en segundo plano                                                                                                                                                    |
| ID del dispositivo     | IMEI (Identidad Internacional de Equipo Móvil)                                                                                                                                   |
| Número de teléfono\*   | El número de teléfono celular del dispositivo de recolección de datos                                                                                                            |

<p class="note">
  La pregunta de metadatos de Número de teléfono solo se captura en dispositivos móviles que tienen una tarjeta SIM.
</p>

### Agregar metadatos del formulario en XLSForm

Si estás construyendo tu formulario en XLSForm, puedes agregar metadatos de la siguiente manera:

| type             | name             |
| :--------------- | :--------------- |
| start            | start            |
| end              | end              |
| today            | today            |
| username         | username         |
| audit            | audit            |
| background-audio | background_audio |
| deviceid         | deviceid         |
| phonenumber      | phonenumber      |
| survey           |                  |

<p class="note">
  No se requieren etiquetas ya que las preguntas no son visibles dentro del formulario durante la recolección de datos
</p>

## Audio de fondo

Cuando la configuración de "Audio de fondo" está activada, se grabará audio mientras el formulario esté abierto. Aprende más sobre la grabación de audio de fondo [aquí](recording-interviews.md).

## Detalles

Al crear un nuevo proyecto, tienes la opción de establecer la _descripción_, _sector_ y _país_ para tu proyecto. También puedes optar por compartir **de forma anónima** la información del país y sector con KoboToolbox con el propósito de mejorar la plataforma. Puedes agregar o cambiar estos detalles en el panel **Diseño y Configuración** dentro del editor de formularios o en la pestaña **CONFIGURACIÓN>General**.

## Configuraciones adicionales

Además de las opciones que se encuentran en la pestaña **Diseño y Configuración** del editor de formularios, también puedes cambiar otras configuraciones a nivel de proyecto, como [compartir](managing_permissions.md), [proyectos conectados](dynamic_data_attachment.md), [servicios REST](rest_services.md) y [medios](media.md) y más.

<p class="note">
  Puedes descargar un XLSForm con ejemplos de este artículo
  <a
    download
    class="reference"
    href="./_static/files/form_meta/form_meta.xlsx"
    >aquí</a
  >.
</p>