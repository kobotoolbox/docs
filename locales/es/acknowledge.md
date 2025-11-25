# Tipo de pregunta Reconocimiento
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/cbfd264f05913df75ec184d5d9eb002f6e66f905/source/acknowledge.md" class="reference">17 jul 2025</a>

El tipo de pregunta "Reconocimiento" muestra una sola opción, para seleccionar "OK" en el
formulario.

Puedes usar el tipo "Reconocimiento" para preguntas que requieren solo 2 estados de
respuesta: respondida y no respondida, o aceptada y no aceptada. Podrías usar
este tipo de pregunta con un consentimiento informado en tu formulario de encuesta, o como una forma de
asegurar que el/la entrevistado/a ha leído y acepta los términos, generalmente
descritos usando un [tipo de pregunta "Nota"](question_types.md).

## Cómo configurar la pregunta

1. En el editor de formularios de KoboToolbox (Formbuilder), haz clic en el botón <i class="k-icon k-icon-plus"></i> para
   agregar una nueva pregunta.
2. Escribe el texto de la pregunta. Por ejemplo, "Si estás de acuerdo en continuar con la
   encuesta, haz clic en OK."
3. Haz clic en "<i class="k-icon k-icon-plus"></i> AGREGAR PREGUNTA" (o presiona la tecla Enter
   en el teclado).
4. Elige el tipo de pregunta "<i class="k-icon k-icon-qt-acknowledge"></i> Reconocimiento".

![Agregar la pregunta de reconocimiento](images/acknowledge/acknowledge_adding.gif)

## Cómo se muestra en formularios web y KoboCollect

La pregunta "Reconocimiento" muestra un solo botón de opción con la etiqueta "OK" como
se muestra a continuación:

![Preguntas de reconocimiento en KoboCollect y Enketo](images/acknowledge/acknowledge.png)

## Uso de lógica de salto y criterios de validación

Una pregunta "Reconocimiento" tiene solo 2 estados de respuesta: uno donde la pregunta
está respondida, y uno donde no lo está, es decir, el valor de respuesta es "OK" o
_en blanco_.

![Preguntas de reconocimiento en lógica de salto](images/acknowledge/acknowledge_skip.gif)

En el ejemplo anterior, el grupo "Encuesta" solo se mostrará si la
pregunta "Reconocimiento" fue respondida (el/la usuario/a hizo clic en OK).

A continuación se muestra la lógica de formulario equivalente en sintaxis XLSForm:

**hoja survey**

| type        | name    | label                                              | relevant          |
| :---------- | :------ | :------------------------------------------------- | :---------------- |
| acknowledge | consent | Si estás de acuerdo en continuar con la encuesta, haz clic en OK |                   |
| begin_group | survey  | Encuesta                                             | ${consent} = "OK" |
| text        | name    | ¿Cuál es tu nombre?                                 |                   |
| integer     | age     | ¿Cuántos años tienes?                                   |                   |
| end_group   |         |                                                    |                   |
| survey |

<p class="note">
  Puedes descargar el XLSForm de ejemplo
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >aquí <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>