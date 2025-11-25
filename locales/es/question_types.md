# Lista de Tipos de Preguntas
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/3993133bcf0aafda0b0978709534175cb583e049/source/question_types.md" class="reference">28 Oct 2024</a>

La siguiente tabla proporciona un resumen de alto nivel de cada uno de los tipos de respuesta
disponibles para usar en tu XLSForm y editor de formularios:

| Tipo de pregunta                 | Ícono                                         | Entrada de respuesta                                                                                    |
| :------------------------------- | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| integer                          | <i class="k-icon k-icon-qt-number"></i>       | Entrada de número entero (es decir, número completo).                                                   |
| decimal                          | <i class="k-icon k-icon-qt-decimal"></i>      | Entrada decimal.                                                                                        |
| range                            | <i class="k-icon k-icon-qt-range"></i>        | Entrada de rango (incluyendo calificación).                                                             |
| text                             | <i class="k-icon k-icon-qt-text"></i>         | Respuesta de texto libre.                                                                               |
| select_one [options]             | <i class="k-icon k-icon-qt-select-one"></i>   | Pregunta de opción múltiple; solo se puede seleccionar una respuesta.                                   |
| select_multiple [options]        | <i class="k-icon k-icon-qt-select-many"></i>  | Pregunta de opción múltiple; se pueden seleccionar múltiples respuestas.                                |
| select_one_from_file [file]      | <i class="k-icon k-icon-qt-select-one"></i>   | Opción múltiple desde archivo; solo se puede seleccionar una respuesta.                                 |
| select_multiple_from_file [file] | <i class="k-icon k-icon-qt-select-many"></i>  | Opción múltiple desde archivo; se pueden seleccionar múltiples respuestas.                              |
| rank [options]                   | n/a                                           | Pregunta de clasificación; ordenar una lista.                                                           |
| note                             | <i class="k-icon k-icon-qt-note"></i>         | Muestra una nota en la pantalla, no recibe entrada. Abreviatura de type=text con readonly=true.         |
| geopoint                         | <i class="k-icon k-icon-qt-point"></i>        | Recolectar una sola coordenada GPS.                                                                     |
| geotrace                         | <i class="k-icon k-icon-qt-line"></i>         | Registrar una línea de dos o más coordenadas GPS.                                                       |
| geoshape                         | <i class="k-icon k-icon-qt-area"></i>         | Registrar un polígono de múltiples coordenadas GPS; el último punto es el mismo que el primer punto.    |
| date                             | <i class="k-icon k-icon-qt-date"></i>         | Entrada de fecha.                                                                                       |
| time                             | <i class="k-icon k-icon-qt-time"></i>         | Entrada de hora.                                                                                        |
| datetime                         | <i class="k-icon k-icon-qt-date-time"></i>    | Acepta una entrada de fecha y hora.                                                                     |
| image                            | <i class="k-icon k-icon-qt-photo"></i>        | Tomar una foto o cargar un archivo de imagen.                                                           |
| audio                            | <i class="k-icon k-icon-qt-audio"></i>        | Hacer una grabación de audio o cargar un archivo de audio.                                              |
| background-audio                 | <i class="k-icon k-icon-background-rec"></i>  | El audio se graba en segundo plano mientras se completa el formulario.                                  |
| video                            | <i class="k-icon k-icon-qt-video"></i>        | Hacer una grabación de video o cargar un archivo de video.                                              |
| file                             | <i class="k-icon k-icon-qt-file"></i>         | Entrada de archivo genérico (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                 |
| barcode                          | <i class="k-icon k-icon-qt-barcode"></i>      | Escanear un código de barras o código QR                                                                |
| calculate                        | <i class="k-icon k-icon-qt-calculate"></i>    | Realizar un cálculo; consulta la sección de Cálculo a continuación.                                     |
| acknowledge                      | <i class="k-icon k-icon-qt-acknowledge"></i>  | Mensaje de confirmación que establece el valor en "OK" si se selecciona.                                |
| hidden                           | <i class="k-icon k-icon-qt-hidden"></i>       | Un campo sin elemento de interfaz de usuario asociado que se puede usar para almacenar una constante.   |
| xml-external                     | <i class="k-icon k-icon-qt-external-xml"></i> | Agrega una referencia a un archivo de datos XML externo.                                                |

Para obtener más información sobre los tipos de respuesta, visita
[xlsform.org](http://xlsform.org/).

Además, los tipos específicos de KoboToolbox también se pueden usar desde el
editor de formularios:

| Tipo de pregunta del editor de formularios | Ícono                                            | Entrada de respuesta                                                       |
| :------------------------------------------ | :----------------------------------------------- | :------------------------------------------------------------------------- |
| Rating                                      | <i class="k-icon k-icon-qt-rating"></i>          | Comparar diferentes elementos usando una escala común.                     |
| Ranking                                     | <i class="k-icon k-icon-qt-ranking"></i>         | Comparar una lista de diferentes objetos entre sí.                         |
| Question Matrix                             | <i class="k-icon k-icon-qt-question-matrix"></i> | Crear un grupo de preguntas que se muestran en formato de matriz.         |

<p class="note"><a class="reference" href="/calculate_questions.html">Las Preguntas de Cálculo</a> no se muestran en tu formulario, pero se ejecutan automáticamente mientras se responde tu formulario.</p>

<p class="note">El <a class="reference" href="matrix_response.html">Tipo de Matriz de Preguntas</a> solo es compatible con Enketo y con el Tema de Cuadrícula configurado. </p>