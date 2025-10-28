# Respuestas "Otro" especificadas por el/la usuario/a para preguntas de opción múltiple
<a href="../user_specified_other.html">Read in English</a> | <a href="../fr/user_specified_other.html">Lire en français</a> | <a href="../ar/user_specified_other.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/user_specified_other.md" class="reference">15 Feb 2022</a>

Crear respuestas "Otro" especificadas por el/la usuario/a para preguntas de opción múltiple en un solo paso es una funcionalidad que actualmente se encuentra en la hoja de ruta de desarrollo de KoboToolbox. Mientras tanto, aquí te mostramos cómo crearlas manualmente en tu formulario usando lógica de salto.

1. Agrega la pregunta deseada a tu formulario como una pregunta de opción múltiple ordinaria. Puede ser del tipo "seleccionar uno" (como se muestra aquí) o "seleccionar varios".

    ![image](/images/user_specified_other/type.png)

2. Agrega una pregunta de seguimiento del tipo "Texto" en la cual el/la encuestado/a pueda especificar manualmente su respuesta cuando sea necesario.

    ![image](/images/user_specified_other/text.png)

    NOTA: Si estás usando La aplicación de Android de KoboCollect para la recolección de datos, es importante no mostrar la segunda pregunta de texto en un grupo en la misma pantalla, ya que de lo contrario no sería visible. Esto se debe a que KoboCollect solo muestra preguntas en la misma pantalla que son relevantes en el momento en que la pantalla se muestra por primera vez. Solo asegúrate de colocarla fuera del grupo cuando elijas mostrar múltiples preguntas en la misma pantalla. (Al usar Formularios Web de Enketo esto no es un problema, ya que muestra dinámicamente las preguntas una vez que se vuelven relevantes.)

3. Agrega una [lógica de salto](skip_logic.md) a la pregunta de seguimiento anterior para que solo se muestre cuando sea necesario.

    ![image](/images/user_specified_other/skip_logic.png)

4. Por último, previsualiza tu formulario para asegurarte de que se comporte como se espera.

    ![image](/images/user_specified_other/preview.png)