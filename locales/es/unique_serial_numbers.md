# Crear números de serie únicos en formularios
<a href="../unique_serial_numbers.html">Read in English</a> | <a href="../fr/unique_serial_numbers.html">Lire en français</a> | <a href="../ar/unique_serial_numbers.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/unique_serial_numbers.md" class="reference">29 Jul 2025</a>

Hay ocasiones en las que puedes querer generar un número de serie único para cada
formulario en un proyecto. Este artículo discute varias soluciones alternativas sobre cómo
crear números de serie únicos usando el tipo de pregunta `calculate`.

## Enfoque 1: Crear números de serie únicos secuenciales basados en fecha y hora

Este método funciona mejor con [formularios web de Enketo](data_through_webforms.md). Utiliza
una función de cálculo para crear un número de serie único basado en la fecha
y hora hasta el primer milisegundo. Aunque este método puede no satisfacer todas tus
necesidades, debería darte una ilustración de cuánto puedes extender las funciones
de cálculo.

Crea un
<a class="reference" href="calculate_questions.html">tipo de pregunta <code>calculate</code></a> 
ya sea en el editor de formularios o en **XLSForm** y usa la fórmula
a continuación.

```
concat(substr(today(), 0, 4), substr(today(), 5, 7), substr(today(), 8, 10), substr(now(), 11, 13), substr(now(), 14, 16), substr(now(), 17, 19))
```

<p class="note">
  La misma fórmula puede funcionar como una pregunta de tipo <code>integer</code> cuando trabajas en
  un <strong>XLSForm</strong>.
</p>

![Ejemplo de cálculo](/images/unique_serial_numbers/calculate_example.png)

En el ejemplo, cuando previsualizas el formulario desplegado en **Enketo**, deberías poder
ver el número de serie dentro de la pregunta de nota como se muestra en la imagen
a continuación:

![Previsualizar formulario](/images/unique_serial_numbers/preview_form.png)

## Enfoque 2: Crear números de serie únicos a partir de variables seleccionadas

Este ejemplo muestra cómo crear números de serie únicos a partir de variables existentes, ya
definidas en tu formulario usando la
expresión [`concat()`](https://docs.getodk.org/form-operators-functions/#concat)
en un tipo de pregunta `calculate`. El ejemplo se muestra como un
**XLSForm**, pero puede hacerse fácilmente dentro del editor de formularios.

**hoja survey**

| type      | name    | label                                        | calculation                                                           |
| :-------- | :------ | :------------------------------------------- | :-------------------------------------------------------------------- |
| text      | Q1      | Nombre de la región                          |                                                                       |
| text      | Q2      | Nombre del distrito                          |                                                                       |
| text      | Q3      | Nombre del grupo                             |                                                                       |
| text      | Q4      | Nombre de la aldea                           |                                                                       |
| text      | Q5      | Número de serie del hogar                    |                                                                       |
| calculate | Q1_C    |                                              | substr(${Q1}, 0, 3)                                                   |
| calculate | Q2_C    |                                              | substr(${Q2}, 0, 3)                                                   |
| calculate | Q3_C    |                                              | substr(${Q3}, 0, 3)                                                   |
| calculate | Q4_C    |                                              | substr(${Q4}, 0, 3)                                                   |
| calculate | ID      |                                              | concat(${Q1_C}, '-', ${Q2_C}, '-', ${Q3_C}, '-', ${Q4_C}, '-', ${Q5}) |
| note      | note_id | Tu ID único para este formulario es: ${ID}   |                                                                       |
| survey |

Cuando previsualizas el ejemplo en los formularios web de **Enketo**, el número de serie se
presentará dentro de la pregunta de nota como se muestra en la imagen a continuación:

![Previsualizar ID único](/images/unique_serial_numbers/preview_uniqueid.png)