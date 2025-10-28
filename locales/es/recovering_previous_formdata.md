# Recuperar datos de versiones anteriores del formulario
<a href="../recovering_previous_formdata.html">Read in English</a> | <a href="../fr/recovering_previous_formdata.html">Lire en français</a> | <a href="../ar/recovering_previous_formdata.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6c4fc8e55497e4a00b39095f090a6f43eb01c37b/source/recovering_previous_formdata.md" class="reference">26 Jul 2020</a>

**Este artículo muestra los pasos sobre cómo recuperar datos de versiones anteriores del formulario en caso de eliminación de preguntas**

Normalmente, cuando cambias un formulario, los datos se descargarán según la definición de ese nuevo formulario. Tal como está, si cambiaste el nombre de una pregunta o eliminaste una pregunta, todos los datos recolectados previamente en esa pregunta no serán visibles bajo la nueva pregunta a menos que elijas incluir datos recolectados de versiones anteriores como se explica a continuación.

Generalmente, cuando editas tus formularios de encuesta y los vuelves a desplegar, deberías poder descargar los datos que han sido enviados al servidor de dos maneras diferentes. Para esto, primero consulta las imágenes a continuación para una mejor comprensión:

**Imagen 1:**

![image](/images/recovering_previous_formdata/no_redeployment.jpg)

La **Imagen 1** es un escenario donde no hay redespliegue en el proyecto de encuesta mientras que

**Imagen 2:**

![image](/images/recovering_previous_formdata/redeployment.jpg)

La **Imagen 2** es un escenario que tiene redespliegue en el proyecto de encuesta (*como se muestra con la marca roja*).

Por lo tanto, la diferencia entre el proyecto que no tiene redespliegue y el que tiene un redespliegue se ve como se muestra en la **imagen 2**, que tiene una casilla de verificación con un mensaje **Incluir campos de las 3 versiones desplegadas**. El **3** como se muestra en el mensaje es el siguiente: la primera como desplegada, la segunda y la tercera como versión redesplegada.

Lo que debes tener en cuenta aquí es que si seleccionas la casilla de verificación (*que está marcada por defecto cuando un proyecto ha sido redesplegado*) marcada con **Incluir campos de las 3 versiones desplegadas**, deberías poder descargar todos los casos con todas las variables (*incluyendo las variables que han sido eliminadas durante el despliegue reciente*). De manera similar, si no seleccionas la casilla de verificación, se te permite descargar todos los casos **pero** solo con las variables que están disponibles con el último despliegue.