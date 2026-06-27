# Introducción a XLSForm
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/edit_forms_excel.md" class="reference">25 Nov 2025</a>

KoboToolbox utiliza [XLSForm](http://xlsform.org/en/), un estándar para diseñar formularios electrónicos en Excel u otros programas de hojas de cálculo. XLSForm facilita el manejo de formularios complejos, como aquellos con listas de opciones extensas o múltiples traducciones. Si bien el editor de formularios de KoboToolbox **(Formbuilder)** ofrece una interfaz intuitiva y de uso amigable, se recomienda XLSForm cuando se trabaja con funcionalidades avanzadas o formularios complejos.

Todos los formularios en KoboToolbox son totalmente compatibles con XLSForm. Esto significa que puedes importar y exportar fácilmente tus formularios entre KoboToolbox y otras plataformas de recolección de datos. XLSForm proporciona un formato estandarizado para el desarrollo de formularios utilizando programas de hojas de cálculo comunes, lo que lo convierte en una opción práctica para la colaboración y el intercambio.

Este artículo cubre los siguientes temas:

- Beneficios de usar XLSForm para el desarrollo de formularios
- Descripción general del uso de XLSForm con KoboToolbox
- Recursos adicionales para aprender XLSForm

![image](/images/edit_forms_excel/sample_xlsform.png)

<p class="note">
  Este artículo ofrece una introducción a XLSForm. Para comenzar a crear XLSForms, consulta <a class="reference" href="https://support.kobotoolbox.org/es/getting_started_xlsform.html">Crear un XLSForm</a>.
  <br><br>
  Para practicar el desarrollo de formularios con XLSForm, consulta el <a class="reference" href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">curso XLSForm Fundamentals de la KoboToolbox Academy</a>.
</p>

## Beneficios de usar XLSForm

XLSForm ofrece numerosos beneficios para crear formularios de recolección de datos, tanto simples como complejos.

### Elaboración y edición eficiente de formularios

XLSForm aprovecha las funciones familiares de las hojas de cálculo para crear y modificar formularios de manera eficiente. Puedes usar fórmulas y funcionalidades de Excel como copiar y pegar, arrastrar, Buscar y Reemplazar, ordenar y filtrar para crear y gestionar formularios extensos con rapidez.

### Manejo de listas de opciones para preguntas de selección múltiple

XLSForm facilita la creación y el manejo de [listas de opciones de respuesta](https://support.kobotoolbox.org/es/option_choices_xls.html). Puedes copiar listas extensas directamente desde fuentes externas, reutilizar las mismas opciones en varias preguntas o duplicarlas en distintos formularios, lo que ahorra tiempo, garantiza consistencia y reduce errores manuales.

### Control de versiones y colaboración

XLSForm simplifica el intercambio y la gestión de versiones de formularios. Como los formularios son archivos de Excel o Google Sheets, los equipos pueden colaborar en ellos en tiempo real, compartirlos para revisión y mantener registros de versiones.

### Personalización de formularios

XLSForm te permite adaptar completamente tus formularios a diferentes necesidades. Puedes agregar y gestionar [múltiples traducciones](https://support.kobotoolbox.org/es/language_xls.html) directamente en tu XLSForm para facilitar la recolección de datos en varios idiomas. Puedes configurar fácilmente estructuras de formularios complejas, como [grupos de preguntas](https://support.kobotoolbox.org/es/grouping_questions_xls.html) o [secciones de repetición](https://support.kobotoolbox.org/es/repeat_groups_xls.html). Además, puedes conectar tu formulario a [fuentes de datos externas](https://support.kobotoolbox.org/es/pull_data_kobotoolbox.html) y a [otros proyectos de KoboToolbox](https://support.kobotoolbox.org/es/dynamic_data_attachment.html).

### Funcionalidades avanzadas

XLSForm facilita el uso de funcionalidades avanzadas para la elaboración de formularios, como [lógica de omisión](https://support.kobotoolbox.org/es/skip_logic_xls.html), [cálculos](https://support.kobotoolbox.org/es/calculations_xls.html) y [restricciones](https://support.kobotoolbox.org/es/constraints_xls.html). Al ser un estándar abierto, XLSForm también ofrece acceso a funcionalidades que aún podrían no estar disponibles en el Formbuilder.

## Usar XLSForm con KoboToolbox

XLSForm se integra de manera fluida con KoboToolbox para la elaboración, previsualización, edición e implementación de formularios para la recolección de datos.

Los usuarios pueden comenzar en el Formbuilder creando un nuevo formulario y agregando preguntas, y luego [descargar su formulario](https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html#downloading-an-xlsform-from-kobotoolbox) como XLSForm para personalizarlo. Esto proporciona una base estructurada, lo que puede ser útil para nuevos proyectos o usuarios con menos experiencia en la elaboración de formularios.

Los formularios creados en XLSForm pueden cargarse en KoboToolbox para su previsualización, prueba, edición e implementación. Los formularios pueden revisarse para detectar errores y modificarse fácilmente en KoboToolbox, por ejemplo, cambiando el título o la configuración.

<p class="note">
  Para más información, consulta <a class="reference" href="https://support.kobotoolbox.org/es/xlsform_with_kobotoolbox.html">Usar XLSForm con KoboToolbox</a>.
</p>

## Recursos adicionales de XLSForm

Hay numerosos recursos disponibles para aprender XLSForm y resolver problemas.

KoboToolbox ofrece los siguientes recursos:

- [Centro de Ayuda de KoboToolbox](https://support.kobotoolbox.org): Una extensa biblioteca de documentación con artículos de ayuda sobre KoboToolbox y XLSForm.
- [Curso XLSForm Fundamentals de KoboToolbox](https://academy.kobotoolbox.org/courses/xlsform-fundamentals): Un curso en línea desarrollado por nuestro equipo de expertos, que cubre una variedad de habilidades, como crear un XLSForm desde cero, usar lógica de formularios y cálculos, y probar e implementar formularios para la recolección de datos con KoboToolbox.
- [Foro de la comunidad de KoboToolbox](https://community.kobotoolbox.org): Un espacio para conectarte con nuestra comunidad global de usuarios, obtener ayuda con la elaboración personalizada de formularios o la resolución de problemas, y compartir recursos de KoboToolbox.

Los recursos externos incluyen:

- [Documentación de XLSForm](https://xlsform.org/en/): Un extenso sitio web de documentación dedicado a XLSForm.
- [Referencia y plantilla de XLSForm](https://xlsform.org/en/ref-table/): Un recurso detallado para crear y personalizar formularios, que incluye tipos de preguntas, apariencias y columnas opcionales.
- [Documentación de ODK](https://docs.getodk.org/form-reference/): Otro extenso sitio web de documentación dedicado a XLSForm.