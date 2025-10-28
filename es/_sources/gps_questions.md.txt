# Tipos de preguntas GPS
<a href="../gps_questions.html">Read in English</a> | <a href="../fr/gps_questions.html">Lire en français</a> | <a href="../ar/gps_questions.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/27e85949b3f42b42dcb60701fbfc80aadddbb616/source/gps_questions.md" class="reference">30 Jul 2022</a>

En KoboToolbox, puedes recolectar coordenadas GPS como parte de tu formulario de recolección de datos. Hay 3 tipos de preguntas GPS que puedes usar, a saber "Punto", "Línea" y "Área".

Usa un tipo de pregunta "Punto" cuando quieras registrar una sola coordenada GPS. Esto es perfecto para preguntas donde necesitas mostrar la ubicación de una característica única como una casa o un pozo de agua.

Usa un tipo de pregunta "Línea" cuando quieras registrar múltiples puntos GPS para trazar una ruta. Este tipo de pregunta puede usarse para recolectar datos de ubicación sobre características como carreteras, caminos y ríos.

El tipo de pregunta "Área" se usa para recolectar múltiples puntos GPS que forman los límites de una característica. Puedes usarlo, por ejemplo, para trazar los límites de parcelas de jardín en una encuesta donde estás enumerando tenencias de tierra.

## Cómo configurar los tipos de preguntas "Punto", "Línea" y "Área"

### Configuración en el editor de formularios

Agregar preguntas GPS en el formulario es simple:

- En el editor de formularios, haz clic en el botón <i class="k-icon k-icon-plus"></i> para agregar una nueva pregunta
- Escribe el texto de la pregunta, por ejemplo "Captura la ubicación de la unidad de vivienda", luego haz clic en **AGREGAR PREGUNTA** o presiona ENTER en tu teclado
- Elige el tipo de pregunta (por ejemplo, Punto)

![Agregar preguntas GPS](images/gps_questions/adding_gps_questions.gif)

### Configuración en XLSForm

Puedes agregar preguntas "Punto", "Línea" y "Área" en XLSForm usando los tipos de pregunta `geopoint`, `geotrace` y `geoshape` respectivamente como en el siguiente ejemplo:

| type     | name   | label                                       |
| :------- | :----- | :------------------------------------------ |
| geopoint | point  | Captura la ubicación de la unidad de vivienda |
| geotrace | road   | Traza la ruta del camino                    |
| geoshape | garden | Traza el límite del jardín                  |
| survey   |

## Apariencia de los tipos de preguntas "Punto", "Línea" y "Área" en formularios web y KoboCollect

### Apariencia predeterminada

![Apariencias predeterminadas de preguntas GPS](images/gps_questions/gps_default_appearances.png)

## Recolectar puntos GPS en segundo plano

Además de incluir preguntas GPS en tu formulario, también puedes recolectar coordenadas GPS en segundo plano mientras se recolectan los datos. Esto es posible activando la opción "Auditoría" en el editor de formularios (Diseño y Configuración -> Preguntas Meta) o agregando la pregunta meta `audit` a tu XLSForm. Aprende más sobre cómo hacer esto [aquí](audit_logging.md).

## Calcular distancia y área con los tipos de preguntas "Línea" y "Área"

A medida que recolectas tus datos GPS, podrías necesitar calcular la distancia y el área de tus preguntas "Línea" y "Área".

### Calcular distancia de preguntas "Línea"

Para calcular la distancia de un tipo de pregunta "Línea" en el editor de formularios, usa el tipo de pregunta "Calcular" y la función [`distance()`](https://docs.getodk.org/form-operators-functions/#distance) como se muestra a continuación:

![Calcular distancia](images/gps_questions/calculate_distance.png)

En el ejemplo anterior, la pregunta "Traza la ruta del camino" se ha agregado como un tipo de pregunta "Línea". El "Nombre de la Columna de Datos" en la configuración de la pregunta se ha establecido como "track".

La pregunta con la etiqueta `distance(${track})` es un tipo de pregunta "Calcular" con un "Nombre de la Columna de Datos" de "distance". El resultado estará en metros.

La pregunta "Nota" es opcional y se ha agregado con el propósito de mostrar la distancia calculada dentro del formulario.

En XLSForm, puedes hacer lo mismo de la siguiente manera:

| type      | name             | label                                 | calculation        |
| :-------- | :--------------- | :------------------------------------ | :----------------- |
| geotrace  | track            | Traza la ruta del camino              |                    |
| calculate | distance         |                                       | distance(${track}) |
| note      | display_distance | La distancia es ${distance} metros    |                    |
| survey    |

### Calcular área de preguntas "Área"

Puedes calcular un área usando el tipo de pregunta "Calcular" y la función [`area()`](https://docs.getodk.org/form-operators-functions/#area) como se muestra a continuación:

![Calcular distancia](images/gps_questions/calculate_area.png)

En el ejemplo anterior, la pregunta "Traza los límites" se ha agregado como un tipo de pregunta "Área". El "Nombre de la Columna de Datos" en la configuración de la pregunta se ha establecido como "boundary".

La pregunta con la etiqueta `area(${boundary})` es un tipo de pregunta "Calcular" con el Nombre de la Columna de Datos "area". El resultado estará en metros cuadrados.

La pregunta "Nota" es opcional y se ha agregado con el propósito de mostrar el área calculada dentro del formulario.

En XLSForm, puedes hacer lo mismo de la siguiente manera:

| type      | name         | label                                  | calculation       |
| :-------- | :----------- | :------------------------------------- | :---------------- |
| geoshape  | boundary     | Traza los límites                      |
| calculate | area         |                                        | area(${boundary}) |
| note      | display_area | El área es ${area} metros cuadrados    |                   |
| survey    |

<p class="note">
  Puedes descargar un XLSForm con ejemplos de este artículo
  <a
    download
    class="reference"
    href="./_static/files/gps_questions/gps_questions.xlsx"
    >aquí</a
  >.
</p>