# Tipo de pregunta Consentimiento

El tipo de pregunta "Consentimiento" muestra una sola opción para seleccionar "OK" en el formulario.

Puedes usar el tipo "Consentimiento" para preguntas que requieren solo 2 estados de respuesta: respondida y no respondida, o aceptada y no aceptada. Puedes usar este tipo de pregunta con un consentimiento informado en tu formulario de encuesta, o como una forma de asegurarte de que el entrevistado haya leído y aceptado los términos, generalmente descritos mediante un [Agregar preguntas con el Formbuilder](question_types.md).

## Cómo configurar la pregunta

1. En el editor de formularios de KoboToolbox (Formbuilder), haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta.
2. Escribe el texto de la pregunta. Por ejemplo, "Si aceptas continuar con la encuesta, haz clic en OK."
3. Haz clic en "<i class="k-icon k-icon-plus"></i> AGREGAR PREGUNTA" (o presiona la tecla Enter en el teclado).
4. Elige el tipo de pregunta "<i class="k-icon k-icon-qt-acknowledge"></i> Consentimiento".

![Agregar la pregunta de consentimiento](images/acknowledge/acknowledge_adding.gif)

## Cómo se muestra en formularios web y KoboCollect

La pregunta "Consentimiento" muestra un único botón de opción con la etiqueta "OK", como se muestra a continuación:

![Preguntas de consentimiento en KoboCollect y Enketo](images/acknowledge/acknowledge.png)

## Usar lógica de omisión y criterios de validación

Una pregunta "Consentimiento" tiene solo 2 estados de respuesta: uno en el que la pregunta fue respondida y otro en el que no lo fue, es decir, el valor de la respuesta es "OK" o está _en blanco_.

![Preguntas de consentimiento en lógica de omisión](images/acknowledge/acknowledge_skip.gif)

En el ejemplo anterior, el grupo "Survey" solo se mostrará si la pregunta "Consentimiento" fue respondida (el usuario hizo clic en OK).

A continuación se muestra la lógica de formulario equivalente en sintaxis XLSForm:

**hoja survey**

| type        | name    | label                                                              | relevant          |
| :---------- | :------ | :----------------------------------------------------------------- | :---------------- |
| acknowledge | consent | Si aceptas continuar con la encuesta, haz clic en OK |                   |
| begin_group | survey  | Survey                                                             | ${consent} = "OK" |
| text        | name    | ¿Cuál es tu nombre?                                                |                   |
| integer     | age     | ¿Cuántos años tienes?                                              |                   |
| end_group   |         |                                                                    |                   |

<p class="note">
  Puedes descargar el XLSForm de ejemplo
  <a
    download
    class="reference"
    href="./_static/files/acknowledge/acknowledge.xlsx"
    >aquí <i class="k-icon k-icon-file-xls"></i></a
  >.
</p>