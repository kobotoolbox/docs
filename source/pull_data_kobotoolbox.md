# Pull Data Functionality in KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/050dcc9c8bfb4c528208bbe886979999037f1554/source/pull_data_kobotoolbox.md" class="reference">28 Oct 2025</a>

<a href="es/pull_data_kobotoolbox.html">Leer en español</a> | <a href="fr/pull_data_kobotoolbox.html">Lire en français</a> | <a href="ar/pull_data_kobotoolbox.html">اقرأ باللغة العربية</a>

-   In the survey side of the form add a calculate field to your survey.
-   Give that field a name that you want
-   Then in its calculation column, call the pulldata() function, indicating
    which field to pull from which row of which .csv file. This can be achieved
    by writing as follows
    `pulldata(‘nameofcsv’, ‘columnheadingtopulldatafrom’, ‘columncheckformatchingTEXT’, ‘TEXTtoCheckfor’`

    ![image](/images/pull_data_kobotoolbox/xls.png)

-   Note your CSV needs to have at-least two columns and ensure that the
    columntocheckformatchingTEXT is always the first column from the left
-   TexttoCheckfor can also be referenced from an earlier field question by
    using `${Question}` as an example above
-   Once you have finished updating the xls you will need to upload your form
    from xls (do not edit it on the formbuilder), you will then upload your CSV
    the same way you would upload your images.
-   When you deploy your file the csv will be downloaded to the media files

**Things to note**

-   This will work both on KoboCollect app and Enketo (web form).
-   Compress a large .csv file into a .zip archive before uploading it.
-   Save .csv file in UTF-8 format if pre-loaded data contains non-English fonts
    or special characters this enables your Android device to render the text
    correctly.
-   Data fields pulled from a .csv file are considered to be text strings
    therefore use the int() or number() functions to convert a pre-loaded field
    into numeric form.
-   If the .csv file contains sensitive data that you may not want to upload to
    the server, upload a blank .csv file as part of your form, then replace it
    with the real .csv file by hand-copying the file onto each of your devices.
-   If you are facing error messages when using this feature, try changing the file name to remove any underscores or symbols.
