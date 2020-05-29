# Downloading photos and other media

If your form includes a photo, video, or sound recording question, these files will be uploaded to the server along with your other data. When exporting your dataset to XLS or CSV these files will include references to the filenames of the media attachments, but not the files themselves. To download your media files choose the ZIP option under 'Download data'. 
 
The following explains other options for downloading and accessing your collected media files.

#### Adding direct hyperlinks to collected media in Excel
1. Download your data to XLS and open the file
2. In a new column next to the one that contains the filenames of your images, enter the following formula: 

    **If using the KoBoToolbox server**: 
    =HYPERLINK("https://kc.kobotoolbox.org/attachment/original?media_file=username/attachments/"&A2")   
    **If using OCHA's server**: 
    =HYPERLINK("https://kc.humanitarianresponse.info/attachment/original?media_file=username/attachments/"&A2")

3. In the formula replace 'username' with your own username and 'A2' with the first cell reference that contains the file name of your photo. Then copy the formula down for all your records. 
4. You can then click on each of the links to open the media file. Note: This will only work if you are signed in to your user account in your default browser. 

    The result will look like this:

    ![image](/images/photo_download/excel_hyperlinks.jpg)

**For slow connections or very large projects: Using DownThemAll to download media files**

The ZIP download method will always include all of your project's media files. This can take a long time to download in case of a large number of collected images or videos or in case of a slow connection. Here is a workaround to download all (or a selection of) media using the popular DownThemAll download manager (only supported by the Firefox browser):

1. Save your Excel file with the added hyperlinks (see instructions above) as an HTML file to your Desktop, using the File > Save as... option (choose 'Web page')
2. Log in to your KoBoToolbox account where your photos are hosted using the Firefox browser
3. In Firefox install the DownThemAll extension
4. Still in Firefox, open the HTM web page saved on your Desktop in step 1
5. Right-click somewhere on that page and choose 'DownThemAll!...', or click the extension button in the Firefox Toolbox
6. In the extension window that opens click 'Download'. By default, Firefox will save all files in your computer's Download folder (which can be changed).
7. Optional: In the window that opens set a download speed limit to avoid using all available bandwidth. The settings also allow you to set the number of attempts that should be made for each file in case of connection issues.

If you have a lot of media files this will take a while to download. But the DownThemAll download manager will make sure you have downloaded all the images and let you know in case any of them were not downloaded so you can try again.

![image](/images/photo_download/downthemall_extension.jpg)

![image](/images/photo_download/downthemall_links.jpg)
