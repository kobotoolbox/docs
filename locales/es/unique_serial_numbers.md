# Crear seriales únicos
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/unique_serial_numbers.md" class="reference">23 Apr 2026</a>


En ocasiones, es posible que quieras generar un serial único para cada formulario de un proyecto. Este artículo describe distintas alternativas para crear seriales únicos usando el tipo de pregunta `calculate`.

## Enfoque 1: Crear seriales únicos secuenciales basados en fecha y hora

Este método funciona mejor con [Recolección de datos a través de formularios web](data_through_webforms.md). Utiliza una función de cálculo para crear un serial único basado en la fecha y la hora hasta el primer milisegundo. Aunque este método puede no satisfacer todas tus necesidades, te dará una idea de hasta dónde puedes llevar las funciones de cálculo.

Crea un <a class="reference" href="calculate_questions.html"><code>tipo de pregunta calculate</code></a> en el editor de formularios de KoboToolbox **(Formbuilder)** o en un **XLSForm** y usa la siguiente fórmula.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  La misma fórmula puede funcionar como una pregunta de tipo <code>integer</code> cuando se trabaja en un <strong>XLSForm</strong>.
</p>

![Calculate example](/images/unique_serial_numbers/calculate_example.png)

En el ejemplo, al previsualizar el formulario implementado en **formularios web**, deberías poder ver el serial dentro de la pregunta de tipo nota, como se muestra en la imagen a continuación:

![Preview form](/images/unique_serial_numbers/preview_form.png)

## Enfoque 2: Crear seriales únicos a partir de variables seleccionadas

Este ejemplo muestra cómo crear seriales únicos a partir de variables ya definidas en tu formulario usando la expresión [`concat()`](https://docs.getodk.org/form-operators-functions/#concat) en un tipo de pregunta `calculate`. El ejemplo se presenta como un **XLSForm**, pero puede realizarse igualmente en el Formbuilder.

**hoja survey**

| type      | name    | label                                  | calculation                                                           |
| :-------- | :------ | :------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Region Name                            |                                                                       |
| text      | Q2      | District Name                          |                                                                       |
| text      | Q3      | Cluster Name                           |                                                                       |
| text      | Q4      | Village Name                           |                                                                       |
| text      | Q5      | Household Serial Number                |                                                                       |
| calculate | Q1_C    |                                        | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                        | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                        | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                        | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                        | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Your Unique ID for this form is: ${ID} |                                                                       |
| survey |

Al previsualizar el ejemplo en formularios web, el serial se mostrará dentro de la pregunta de tipo nota, como se muestra en la imagen a continuación:

![Preview unique id](/images/unique_serial_numbers/preview_uniqueid.png)