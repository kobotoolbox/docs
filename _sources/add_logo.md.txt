# Adding a Custom Logo
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c8c238efa59b04f403f13c150b018e1807c66d5c/source/add_logo.md" class="reference">28 Oct 2025</a>

<a href="es/add_logo.html">Leer en español</a> | <a href="fr/add_logo.html">Lire en français</a> | <a href="ar/add_logo.html">اقرأ باللغة العربية</a>
follows the same steps as [adding media content to your forms](media.md).

To begin:

1. Start by creating your logo image file and save it with a short file name.

2. In your XLSForm, make the first question a Note question type, leave the
   label blank, and add a column titled `media::image` with your logo file name
   in the cell. As shown below:

**survey sheet**

| type | name | label | media::image |
| :--- | :--- | :---- | :----------- |
| note | logo |       | logo.jpg     |
| survey|

3. When you're done editing the form, upload the XLSForm to either a new or
   existing project.

4. Deploy or redeploy your form, depending on whether it's a new project or it's
   replacing an existing form.

5. In your project page go to **SETTINGS>MEDIA** and [upload](media.md) your
   `logo.jpg` file.

## Tips:

-   Keep your image small.
-   Your logo image will not appear in the form preview, only when the form is
    opened.
-   Skipping the final step will mean that your form will be displayed without
    the media files. Make sure the media files are uploaded before downloading
    the form to your devices when using the Android app.

<p class="note">If you open the formbuilder after deploying your XLSForm with the logo image file, it will automatically give the question a text label and you'll need to delete it for the automated text not to appear next to your logo in your form.</p>
