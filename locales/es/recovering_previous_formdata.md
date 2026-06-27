# Recuperar datos de versiones anteriores del formulario

**Este artículo muestra los pasos para recuperar datos de versiones anteriores del formulario en caso de que se hayan eliminado preguntas**

Normalmente, cuando cambias un formulario, los datos se descargan según la definición del nuevo formulario. Es decir, si cambiaste el nombre de una pregunta o eliminaste una pregunta, todos los datos recolectados anteriormente en esa pregunta no serán visibles en la nueva pregunta, a menos que elijas incluir los datos recolectados de versiones anteriores, como se explica a continuación.

En general, cuando editas tus formularios de encuesta y los vuelves a implementar, deberías poder descargar los datos enviados al servidor de dos maneras diferentes. Para esto, primero revisa las imágenes a continuación para una mejor comprensión:

**Imagen 1:**

![image](/images/recovering_previous_formdata/no_redeployment.jpg)

La **Imagen 1** muestra un escenario en el que no hay reimplementación en el proyecto de encuesta, mientras que

**Imagen 2:**

![image](/images/recovering_previous_formdata/redeployment.jpg)

La **Imagen 2** muestra un escenario con reimplementación en el proyecto de encuesta (*indicado por la marca roja*).

La diferencia entre el proyecto sin reimplementación y el que tiene reimplementación se observa en la **Imagen 2**, que muestra una casilla de verificación con el mensaje **Include fields from all 3 deployed versions** (Incluir campos de todas las 3 versiones implementadas). El número **3** que aparece en el mensaje corresponde a: la primera versión implementada, la segunda y la tercera como versiones reimplementadas.

Ten en cuenta que si seleccionas la casilla de verificación (*que está marcada de forma predeterminada cuando un proyecto ha sido reimplementado*) con el mensaje **Include fields from all 3 deployed versions** (Incluir campos de todas las 3 versiones implementadas), podrás descargar todos los registros con todas las variables (*incluidas las variables que fueron eliminadas durante la implementación más reciente*). Del mismo modo, si no seleccionas la casilla de verificación, podrás descargar todos los registros **pero** solo con las variables disponibles en la última implementación.