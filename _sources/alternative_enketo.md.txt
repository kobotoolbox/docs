# Using Alternative Enketo Web Form Styles

Enketo web forms can be customized in the way your questions are presented. There are two alternative styles that can be selected and even combined: **Multiple Pages** and **Grid Theme**.
 
**Multiple Pages** mode displays one question at a time per screen, or a group of questions set to display on the same screen. This is the same way [KoBoCollect works](group_repeat.md).
 
**Grid Theme** is an alternative display of questions meant to be more compact and more like paper forms where space is often a major concern. theme-grid allows displaying multiple questions per row and flexibly adapts in case of skip logic making a new question appear or disappear. To display multiple questions in a row they need to be part of a group, which by default shows up to four questions next to each other. This theme can be customized by defining the number of questions to be included in each row through the appearance field of each question's settings. For more details [see this post](https://blog.enketo.org/gorgeous-grid).
 
It is also possible to use both Multiple Pages and Grid Theme together. To use these styles through the KoBoToolbox form builder user interface, simply refer to the image below:

![image](/images/alternative_enketo/multiple_grid.jpg)

_Go to your Form Settings and choose one of the options under the Form Style. This preference is saved along with the form._

If you are building your survey project through an XLSForm, you could do the same by mentioning the style under the style at the settings tab as shown in the image below:

![image](/images/alternative_enketo/xls.png)

## List of available styles in XLSForm:

Default – single page : _(leave blank)_  
Grid theme : _theme-grid no-text-transform_  
Grid theme with headings in ALL CAPS: _theme-grid_  
Multiple pages: _pages_  
Grid theme + Multiple pages: _theme-grid pages no-text-transform_  
Grid theme + Multiple pages + headings in ALL CAPS: _theme-grid pages_
