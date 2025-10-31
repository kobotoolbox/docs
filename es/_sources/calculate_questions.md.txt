# Tipo de pregunta Calcular

**Última actualización:**
<a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/calculate_questions.md" class="reference">15
Feb 2022</a>

Algunos formularios avanzados pueden requerir que se realice un cálculo interno como parte del
formulario (en lugar de después durante el análisis). Esto se puede hacer
agregando un Cálculo y escribiendo la expresión matemática en el campo de
etiqueta de pregunta.

![image](/images/calculate_questions/calculation.gif)

Una expresión matemática podría ser tan simple como `5 + 1`, pero lo más probable es que
incluya una referencia a otra pregunta.

Hacer referencia a otras preguntas en tu pregunta de cálculo requiere dar a otras
preguntas nombres fijos a través de la configuración de la pregunta, como `girls` o
`income`. Al hacer referencia a esas preguntas, siempre debes usar el nombre único
de la pregunta (no la etiqueta) - `${girls}` o `${income}`

Por ejemplo, si quieres convertir la respuesta a una pregunta sobre los
ingresos de alguien a otra moneda (como francos ruandeses a dólares estadounidenses), debes
escribir `${income} div 688`.

También puedes usar la respuesta a esta pregunta Calcular para otros propósitos, como
construir tu lógica de salto (por ejemplo, solo hacer una pregunta de seguimiento por encima de un
cierto umbral de ingresos) o mostrándola dentro de una Nota
([consulta aquí](responses_inside_question.md) para obtener ayuda sobre cómo mostrar la
respuesta a una pregunta en la etiqueta de otra pregunta).

## Lista de funciones disponibles

Hay muchas opciones diferentes disponibles, como la función round()
(por ejemplo, `round(${int_1} div ${int_2}, 1`) redondeará el resultado de una división a un
solo decimal). Para obtener una lista de algunas de las muchas expresiones matemáticas que
se pueden usar en este campo, consulta
[Especificaciones de XForm sobre funciones de cálculo](https://docs.getodk.org/form-operators-functions/)
para conocer los antecedentes técnicos de todas las funciones disponibles en KoboToolbox y
XLSForms. Para el uso avanzado de cálculos en KoboToolbox, consulta
[este artículo](advanced_calculate.md).

## Lista de operadores matemáticos disponibles

| Operador               | Descripción                         |
| :--------------------- | :---------------------------------- |
| `+`                    | Suma                                |
| `-`                    | Resta                               |
| `*`                    | Multiplicación                      |
| `div`                  | División                            |
| `=`                    | Igual                               |
| `!=`                   | No igual                            |
| `<`                    | Menor que                           |
| `<=`                   | Menor o igual que                   |
| `>`                    | Mayor que                           |
| `>=`                   | Mayor o igual que                   |
| `or`                   | O                                   |
| `and`                  | Y                                   |
| `mod`                  | Módulo (resto de la división)       |
| `pow([base], [power])` | Potencia / exponente                |