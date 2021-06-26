# Dynamic Data Attachment

This is <a download href="./_static/files/test.xlsx">a downloadable file</a>.

Here you can watch a video:

<video controls><source src="./_static/files/test.mp4" type="video/mp4"></video>

To create a downloadable file, you need to add the file to `source/_static/files/` directory and then create a link:

`<a download href="./_static/files/FILENAME WITH EXTENSION">LINK TEXT</a>`

To create a video, put the file in the same directory as downloads (`source/_static/files/`) and use this code:

`<video controls><source src="./_static/files/FILENAME WITH EXTENSION" type="video/mp4"></video>`
