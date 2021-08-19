# Using Alternative Enketo Web Form Styles

Enketo web forms can be customized in the way your questions are presented. There are two alternative styles that can be selected and even combined: **Multiple Pages** and **Grid Theme**.

**Multiple Pages** mode displays one question at a time per screen, or a group of questions set to display on the same screen. This is the same way [KoBoCollect works](group_repeat.md).

**Grid Theme** is an alternative display of questions meant to be more compact and more like paper forms where space is often a major concern. theme-grid allows displaying multiple questions per row and flexibly adapts in case of skip logic making a new question appear or disappear. To display multiple questions in a row they need to be part of a group, which by default shows up to four questions next to each other. This theme can be customized by defining the number of questions to be included in each row through the appearance field of each question's settings. For more details [see this post](https://blog.enketo.org/gorgeous-grid).

It is also possible to use both **Multiple Pages** and **Grid Theme** together. You can set these styles through the KoBoToolbox form-builder user interface:

![image](/images/alternative_enketo/multiple_grid.gif)

If you are building your survey project through XLSForm, you could do the same by defining the theme under the `style` column in the `settings` sheet:

__settings__

| form_title  | style |
| ---         | ---   |
| Themed form | pages |

## Available styles in XLSForm:

| XLSForm Theme                        | Description                                        |
| ---                                  | ---                                                |
| (leave blank)                        | Default – single page                              |
| `theme-grid no-text-transform`       | Grid theme                                         |
| `theme-grid`                         | Grid theme with headings in ALL CAPS               |
| `pages`                              | Multiple pages                                     |
| `theme-grid pages no-text-transform` | Grid theme + Multiple pages                        |
| `theme-grid pages`                   | Grid theme + Multiple pages + headings in ALL CAPS |

