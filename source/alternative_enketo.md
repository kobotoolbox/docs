# Using Alternative Enketo Web Form Styles
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c8c238efa59b04f403f13c150b018e1807c66d5c/source/alternative_enketo.md" class="reference">28 Oct 2025</a>

<a href="es/alternative_enketo.html">Leer en español</a> | <a href="fr/alternative_enketo.html">Lire en français</a> | <a href="ar/alternative_enketo.html">اقرأ باللغة العربية</a>
There are two alternative styles that can be selected and even combined:
**Multiple Pages** and **Grid Theme**.

**Multiple Pages** mode displays one question at a time per screen, or a [group
of questions](group_repeat.md) set to display on the same screen. This is the same way
KoboCollect works.

**Grid Theme** is an alternative display of questions meant to be more compact
and more like paper forms where space is often a major concern. theme-grid
allows displaying multiple questions per row and flexibly adapts in case of skip
logic making a new question appear or disappear. To display multiple questions
in a row they need to be part of a group, which by default shows up to four
questions next to each other. This theme can be customized by defining the
number of questions to be included in each row through the appearance field of
each question's settings. For more details
[see this post](https://blog.enketo.org/gorgeous-grid).

It is also possible to use both **Multiple Pages** and **Grid Theme** together.
You can set these styles through the KoboToolbox formbuilder user interface:

![image](/images/alternative_enketo/multiple_grid.gif)

If you are building your survey project through XLSForm, you could do the same
by defining the theme under the `style` column in the `settings` sheet:

**settings sheet**

| form_title  | style |
| :---------- | :---- |
| Themed form | pages |
| settings |

## Available styles in XLSForm:

| XLSForm Theme                        | Description                                        |
| :----------------------------------- | :------------------------------------------------- |
| (leave blank)                        | Default – single page                              |
| `theme-grid no-text-transform`       | Grid theme                                         |
| `theme-grid`                         | Grid theme with headings in ALL CAPS               |
| `pages`                              | Multiple pages                                     |
| `theme-grid pages no-text-transform` | Grid theme + Multiple pages                        |
| `theme-grid pages`                   | Grid theme + Multiple pages + headings in ALL CAPS |
