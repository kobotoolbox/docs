# Brindar más detalles sobre una opción de selección múltiple
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/user_specified_other.md" class="reference">23 Apr 2026</a>


Crear respuestas "Otro" especificadas por el usuario para preguntas de selección múltiple en un solo paso es una funcionalidad que actualmente está en el plan de desarrollo de KoboToolbox. Mientras tanto, aquí te explicamos cómo crearlas manualmente en tu formulario usando lógica de omisión.

1. Agrega la pregunta deseada a tu formulario como una pregunta de selección múltiple ordinaria. Puede ser del tipo "seleccionar una" (como se muestra aquí) o "seleccionar varias".

![image](/images/user_specified_other/type.png)

2. Agrega una pregunta de seguimiento del tipo "Texto" en la que el encuestado pueda especificar manualmente su respuesta cuando sea necesario.

    ![image](/images/user_specified_other/text.png)

    NOTA: Si usas la aplicación KoboCollect para la recolección de datos, es importante no mostrar la segunda pregunta de texto en un grupo en la misma pantalla, ya que de lo contrario no sería visible. Esto se debe a que KoboCollect solo muestra las preguntas en la misma pantalla que son relevantes en el momento en que esta se muestra por primera vez. Asegúrate de colocarla fuera del grupo cuando elijas mostrar varias preguntas en la misma pantalla. (Al usar formularios web esto no es un problema, ya que muestra las preguntas de forma dinámica una vez que se vuelven relevantes.)

3. Agrega una [lógica de omisión](skip_logic.md) a la pregunta de seguimiento anterior para que solo se muestre cuando sea necesario.

    ![image](/images/user_specified_other/skip_logic.png)

4. Por último, previsualiza tu formulario para asegurarte de que funciona como se espera.

    ![image](/images/user_specified_other/preview.png)