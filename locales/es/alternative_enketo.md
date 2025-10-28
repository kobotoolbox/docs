# Uso de estilos alternativos de formularios web de Enketo
<a href="../alternative_enketo.html">Read in English</a> | <a href="../fr/alternative_enketo.html">Lire en français</a> | <a href="../ar/alternative_enketo.html">اقرأ باللغة العربية</a>
**Última actualización:** <a href="https://github.com/kobotoolbox/docs/blob/347a1280aadb22c9aebf88650fd6efa1bcadbcdf/source/alternative_enketo.md" class="reference">24 Sep 2025</a>

Los formularios web de Enketo se pueden personalizar en la forma en que se presentan tus preguntas.
Hay dos estilos alternativos que se pueden seleccionar e incluso combinar:
**Páginas múltiples** y **Tema de cuadrícula**.

El modo **Páginas múltiples** muestra una pregunta a la vez por pantalla, o un [grupo
de preguntas](group_repeat.md) configurado para mostrarse en la misma pantalla. Esta es la misma forma en que
funciona KoboCollect.

**Tema de cuadrícula** es una visualización alternativa de preguntas diseñada para ser más compacta
y más parecida a los formularios en papel donde el espacio suele ser una preocupación importante. theme-grid
permite mostrar múltiples preguntas por fila y se adapta de manera flexible en caso de lógica de salto
haciendo que una nueva pregunta aparezca o desaparezca. Para mostrar múltiples preguntas
en una fila, deben ser parte de un grupo, que por defecto muestra hasta cuatro
preguntas una al lado de la otra. Este tema se puede personalizar definiendo el
número de preguntas a incluir en cada fila a través del campo de apariencia de
la configuración de cada pregunta. Para más detalles
[consulta esta publicación](https://blog.enketo.org/gorgeous-grid).

También es posible usar tanto **Páginas múltiples** como **Tema de cuadrícula** juntos.
Puedes configurar estos estilos a través de la interfaz de usuario del editor de formularios de KoboToolbox:

![image](/images/alternative_enketo/multiple_grid.gif)

Si estás construyendo tu proyecto de encuesta a través de XLSForm, podrías hacer lo mismo
definiendo el tema bajo la columna `style` en la hoja `settings`:

**hoja settings**

| form_title  | style |
| :---------- | :---- |
| Themed form | pages |
| settings |

## Estilos disponibles en XLSForm:

| Tema XLSForm                         | Descripción                                                    |
| :----------------------------------- | :------------------------------------------------------------- |
| (dejar en blanco)                    | Predeterminado – página única                                  |
| `theme-grid no-text-transform`       | Tema de cuadrícula                                             |
| `theme-grid`                         | Tema de cuadrícula con encabezados en MAYÚSCULAS              |
| `pages`                              | Páginas múltiples                                              |
| `theme-grid pages no-text-transform` | Tema de cuadrícula + Páginas múltiples                         |
| `theme-grid pages`                   | Tema de cuadrícula + Páginas múltiples + encabezados en MAYÚSCULAS |