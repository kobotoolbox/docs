# Preguntas de tipo Nota en KoboToolbox
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/1833c42c415ddc826146609c1915525d77cf94c8/source/note_questions.md" class="reference">22 Jun 2026</a>

Las preguntas de tipo Nota se utilizan para mostrar información dentro de tu formulario sin recolectar una respuesta. Aunque aparecen como un tipo de pregunta, las preguntas de tipo Nota no almacenan ningún dato. En cambio, se utilizan para **proporcionar instrucciones, contexto o detalles adicionales** que ayuden a los encuestados o encuestadores a entender y completar el formulario correctamente.

Puedes usar preguntas de tipo Nota para introducir una nueva sección, explicar por qué se hacen ciertas preguntas, proporcionar orientación sobre cómo responder, [mostrar archivos multimedia](https://support.kobotoolbox.org/es/media.html), o mostrar los resultados de [cálculos ocultos](https://support.kobotoolbox.org/es/calculate_questions.html) o [respuestas anteriores](https://support.kobotoolbox.org/es/form_logic.html#question-referencing).

Este artículo explica cómo agregar una pregunta de tipo **Nota** en el editor de formularios de KoboToolbox **(Formbuilder)** y cómo aplicar estilos al texto de la nota.

## Agregar una pregunta de tipo Nota en el Formbuilder

Para agregar una pregunta de tipo Nota a tu formulario:

1. Haz clic en el botón <i class="k-icon-plus"></i>.
2. Ingresa la etiqueta de tu pregunta.
3. Haz clic en **+ ADD QUESTION.**
4. Elige el tipo de pregunta <i class="k-icon-qt-note"></i> **Nota**.

![Elegir el tipo de pregunta Nota](images/note_questions/note.png)

## Aspectos de las preguntas de tipo Nota

De forma predeterminada, las preguntas de tipo Nota aparecen como texto simple en tu formulario.

| Formularios web | KoboCollect |
|:----------------|:------------|
| ![Pregunta de tipo Nota en formularios web](images/note_questions/enketo_note.png) | ![Pregunta de tipo Nota en KoboCollect](images/note_questions/kobocollect_note.png) |

### Aspectos avanzados

Al agregar notas a tu formulario, puedes usar Markdown y HTML para **dar estilo al texto, agregar énfasis** con negrita o cursiva, **crear encabezados** de diferentes tamaños, **cambiar fuentes y colores**, y **agregar enlaces web con hipervínculos.**

<p class="note">
<strong>Nota:</strong> El estilo de texto también se puede aplicar a las etiquetas y sugerencias de las preguntas.
</p>

Las funciones de estilo de texto en el Formbuilder incluyen:

| Función        | Formato |
|:---------------|:--------|
| Cursiva        | `*cursiva*` o `_cursiva_` |
| Negrita        | `**negrita**` o `__negrita__` |
| Hipervínculo   | `[nombre del enlace](url)` |
| Correo electrónico | `[email@dominio.org](mailto:email@dominio.org)` |
| Encabezados    | `# Encabezado 1` (más grande) a `###### Encabezado 6` (más pequeño) |
| Emojis         | Por ejemplo, 🙂 😐 🙁 😦 😧 😩 😱 |
| Superíndice    | `100 m<sup>2</sup>` se convierte en 100 m² |
| Subíndice      | `H<sub>2</sub>O` se convierte en H₂O |
| Texto en color | `<span style="color:#f58a1f">naranja</span>` se convierte en <span style="color:#f58a1f">naranja</span> <br>`<span style="color:red">rojo</span>` se convierte en <span style="color:red">rojo</span> |
| Fuente         | `<span style="font-family:cursive">cursiva</span>` se convierte en <span style="font-family:cursive">cursiva</span> <br>`<span style="color:red; font-family:cursive">rojo y cursiva</span>` se convierte en <span style="color:red; font-family:cursive">rojo y cursiva</span> |
| Centrar texto  | `<p style="text-align:center">Etiqueta centrada</p>` centra el texto en la pantalla (solo en KoboCollect) |
| Subrayado      | `<span style="text-decoration: underline;">Este texto está subrayado</span>` subraya el texto (solo en formularios web) |

<p class="note">
<strong>Nota:</strong> Otras funciones de formato, como saltos de línea, listas con viñetas y listas numeradas, solo están disponibles cuando <a href="https://support.kobotoolbox.org/es/form_style_xls.html#styling-text">creas tu formulario en XLSForm</a>.
</p>