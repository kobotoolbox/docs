# Downloading Photos and Other Media
<a href="fr/photo_download.html">Lire en français</a> | <a href="es/photo_download.html">Leer en español</a> | <a href="ar/photo_download.html">اقرأ باللغة العربية</a>
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/47cbc8887d6df73ef3bf760d5a3962b77ab26ed8/source/photo_download.md" class="reference">29 Jul 2025</a>

If your form [includes](question_types.md) a photo, video, or audio recording
question, these files will be uploaded to the server along with your other data.
When exporting your dataset to XLS or CSV these files will include references to
the filenames of the media attachments, but not the files themselves. To
download all your media files in bulk, choose the **Media Attachments (ZIP)**
option under **DATA>Downloads>Select export type**.

The following explains other options for downloading and accessing your
collected media files.

<p class='note'>The ZIP export may fail for very large projects due to a server
time-out limit of 30 minutes being reached. If that is the case, please follow
the methods below to extract your media files from the
<strong>KoboToolbox</strong> server.</p>

## Including direct hyperlinks to collected media in XLS export

1. Navigate to **DATA>Downloads** and expand the **Advanced options** section
2. Ensure that the option _Include media URLs_ is checked (enabled by default)

![Include media URLs](/images/photo_download/include_media_urls.png)

3. Click **EXPORT**

If your survey had the following question:

**survey sheet**

| type  | name    | label           |
| :---- | :------ | :-------------- |
| image | image_1 | Submit an image |
| survey |

And a submission to that question with the filename of "image.jpg", the export
will have the following result:

| image_1   | image_1_URL               |
| :-------- | :------------------------ |
| image.jpg | https://link/to/image.jpg |

## For slow connections or very large projects: Using DownThemAll

The ZIP download method will always include all of your project's media files.
This can take a long time to download in case of a large number of collected
images or videos or in case of a slow connection. Here is a workaround to
download all (or a selection of) media using the popular **DownThemAll**
download manager (only supported by the Firefox browser):

1. Save your Excel file with the added hyperlinks (see instructions above) as an
   HTML file to your Desktop, using the File > Save as... option (choose 'Web
   page')

2. Log in to your KoboToolbox account where your photos are hosted using the
   Firefox browser

3. In Firefox install the
   [DownThemAll extension](https://addons.mozilla.org/en-CA/firefox/addon/downthemall)

4. Still in Firefox, open the HTML web page saved from **Step 1**

5. Right-click somewhere on that page and choose _DownThemAll!_, or click the
   extension button in the Firefox Toolbox

6. In the extension window that opens click **Download**. By default, Firefox
   will save all files in your computer's Download folder (which can be changed)

7. Optional: In the window that opens, set a download speed limit to avoid using
   all available bandwidth. The settings also allow you to set the number of
   attempts that should be made for each file in case of connection issues.

If you have a lot of media files this will take a while to download. But the
**DownThemAll** download manager will make sure you have downloaded all the
images and let you know in case any of them were not downloaded so you can try
again.

![DownThemAll extension](/images/photo_download/downthemall_extension.jpg)

![DownThemAll links](/images/photo_download/downthemall_links.jpg)
