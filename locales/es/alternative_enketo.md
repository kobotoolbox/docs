# Diseñar formularios web usando el Formbuilder
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/alternative_enketo.md" class="reference">23 abr 2026</a>

<iframe src="https://www.youtube.com/embed/wLWiw473YSQ?si=tJbKl-VzjZkDPivR&cc_lang_pref=es&hl=es" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Puedes personalizar el diseño y la apariencia visual de tus [formularios web](https://support.kobotoolbox.org/es/data_through_webforms.html) utilizando temas integrados. Estos temas te permiten controlar cómo se muestran las preguntas, ya sea en una sola página, en varias páginas o dispuestas en un diseño de cuadrícula compacto.

Los temas de formulario se aplican solo a formularios web y no son compatibles con KoboCollect. Este artículo explica cómo aplicar un tema de formulario web en el Formbuilder y cómo configurar el ancho de las preguntas al usar el tema de cuadrícula.

## Agregar un tema de formulario web en el Formbuilder

Para agregar un tema de formulario web a tu formulario en el Formbuilder:

1. Haz clic en <i class="k-icon-settings"></i> **Diseño y configuración** en la esquina superior derecha de la pantalla.
2. En la sección **Estilo del formulario**, selecciona el tema que deseas aplicar a tu formulario.

![Estilo del formulario](images/alternative_enketo/access.png)

Los siguientes temas están disponibles para personalizar tus formularios:

![Temas](images/alternative_enketo/preview.png)

<p class="note">
<strong>Nota:</strong> También puedes combinar los estilos <strong>Múltiples páginas</strong> y <strong>Tema de cuadrícula</strong>.
</p>

## Configurar el ancho de las preguntas para el tema de cuadrícula

En los formularios web, el tema de cuadrícula te permite mostrar preguntas en múltiples columnas, haciendo que tu formulario sea más compacto y visualmente organizado. La configuración de estas columnas, incluidas cuántas hay y qué tan ancha debe ser cada una, se controla asignando `valores-w` a cada pregunta en su configuración de **Aspecto (avanzado)**.

<p class="note">
 Para obtener una descripción completa del uso del tema de cuadrícula, consulta este <a href="https://ee.kobotoolbox.org/n41GqUkf">Tutorial del tema de cuadrícula</a> y <a href="https://docs.google.com/spreadsheets/d/1qKmxPTA4B0vihU6GsKgi1CJE2Db2FfE7KZpOig4nTEI/edit?gid=0#gid=0">XLSForm de ejemplo</a>.   
</p>

Para especificar el ancho relativo de cada pregunta dentro de una fila:

1. Abre la configuración de la pregunta haciendo clic en <i class="k-icon-settings"></i> **Configuración** a la derecha de la pregunta. Esto te llevará a la ventana **Opciones de pregunta**.
2. En **Aspecto (avanzado)**, asigna valores de apariencia (por ejemplo, `w1`, `w2`, `w3`) para especificar el ancho relativo de la pregunta dentro de una fila.

Las filas siempre se expandirán automáticamente al ancho completo de la página. Por ejemplo, una fila que contiene una pregunta con un valor de apariencia de `w2` y otra con `w1` dividirá la fila en dos tercios y un tercio, respectivamente.

<p class="note">
<strong>Nota:</strong> El ancho predeterminado para un grupo o grupo de repetición es de cuatro columnas (<code>w4</code>), por lo que un grupo con <code>w4</code> puede contener un máximo de cuatro preguntas <code>w1</code> en una sola fila. El <code>valor-w</code> de una pregunta es relativo al <code>valor-w</code> de su grupo. Aplica <code>valores-w</code> solo a grupos o repeticiones de nivel superior: aunque aplicarlos a grupos o repeticiones anidados es compatible, es posible que no se visualice bien.
</p>