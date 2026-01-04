# Adding media to an XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/media.md" class="reference">25 Nov 2025</a>

<iframe src="https://www.youtube.com/embed/7TrVmKIuCa8?si=QCr1IzvDXaASEZg7" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


KoboToolbox allows you to add media, including **images**, **audio files**, and **videos**, to notes, questions, and choices in your form. Adding media can increase user engagement and make forms more accessible for users with visual impairments or literacy barriers. 

Form media works with both [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html) and [Enketo web forms](https://support.kobotoolbox.org/enketo.html). The following types of media files are currently supported:

| Media | Files |
| :--- | :--- |
| Image | jpeg, png, svg |
| Audio | aac, aacp, flac, mp3, mp4, mpeg, ogg, wav, webm, x-m4a, x-wav |
| Video | 3gpp, avi, flv, mov, mp4, ogg, quicktime (qtff), webm, wmv |

This article covers the following topics: 
- Adding media to survey questions
- Adding media to options choices
- Adding media to form translations
- Uploading media files to KoboToolbox

<p class="note">
    <strong>Note:</strong> The KoboToolbox <a href="https://support.kobotoolbox.org/formbuilder.html">Formbuilder</a> does not currently support adding media files inside your forms. To add media, you will need to use XLSForm and then upload your XLSForm to KoboToolbox. To learn more about downloading and editing your form as XLSForm, see <a href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Using XLSForm with KoboToolbox</a>.
<br><br>
For hands-on practice with adding media attachments in XLSForm, see KoboToolbox Academy’s <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Adding media to questions in XLSForm

To add media files to questions or notes in your XLSForm:
1. Add a new question in the survey worksheet, specifying the `type`, `name`, and `label` (optional).
    - Use a `note` question type if you want to display the media file without collecting any data (e.g., an organization logo or introduction video).
    - Adding a label is optional when including a media file.
2. Add a column for the media you want to include. Name it `image`, `video`, or `audio`, depending on the media type. 
3. In the media column, in the row of the question you have added, enter the exact name of the media file **including the extension**.
    - For example: `logo.png` or `intro.mp4`.

**survey worksheet**

| type | name | label | image |
| :--- | :--- | :--- | :--- |
| text | Q1 | In your own words, how would you describe the image above? | q1.png |
| survey |

<p class="note">
    <strong>Note:</strong> Previously, the format <code>media::file_type</code> was used for media column names (e.g., <code>media::image</code>, <code>media::video</code>, <code>media::audio</code>). The simplified format using only the media type without the <code>media::</code> prefix is now more commonly adopted (e.g., <code>image</code>, <code>video</code>, <code>audio</code>).
</p>

### Uploading media files to KoboToolbox

To upload the media files to KoboToolbox:
1. Go to your [KoboToolbox account](https://www.kobotoolbox.org/sign-up/).
2. In your KoboToolbox project, navigate to **SETTINGS > Media**.
3. Upload the media files that you have added to your XLSForm, ensuring the file name is exactly the same.
4. Deploy or redeploy your form to see media changes.

![Upload media files](images/media/upload_media.png)

## Adding media to choices in XLSForm

To add media files to option choices in your XLSForm:
1. Add a [select type question](https://support.kobotoolbox.org/question_types_xls.html#select-question-types) in the survey worksheet.
2. In the choices worksheet, add a `list_name`, `name`, and `label` (optional) for your choices.
    - Adding a label is optional when including a media file. If you wish to use the media files as options label, omit the label text.
3. Add a column for the media you want to include. Name it `image`, `video`, or `audio`, depending on the media type. 
4. In the media column, in the row of the choices you have added, enter the name of the media file **including the extension**.
    - For example: `goat.png` or `fish.png`

**survey worksheet**

| name | type | label |
| :--- | :--- | :--- |
| select_one animals | animals | Which of these is your favorite animal? |
| survey |

**choices worksheet**

| list_name | name | label | image |
| :--- | :--- | :--- | :--- |
| animals | goats | Goats | goat.png |
| animals | cows | Cows | cow.png |
| animals | chicken | Chickens | chicken.png |
| animals | pigs | Pigs | pig.png |
| animals | fish | Fish | fish.png |
| choices |

### Uploading media files to KoboToolbox

To upload the media files to KoboToolbox:
1. Go to your [KoboToolbox account](https://www.kobotoolbox.org/sign-up/).
2. In your KoboToolbox project, navigate to **SETTINGS > Media**.
3. Upload the media files that you have added to your XLSForm, ensuring the file name is exactly the same.
4. Deploy or redeploy your form to see media changes.

## Adding media to translations

In XLSForms that are [translated in multiple languages](https://support.kobotoolbox.org/language_xls.html), you can include different media files for each language by adding new `image`, `audio`, or `video` columns.

To add media files for different languages in your survey worksheet:

1. Rename your media columns using the format `media_type::language (code)`, where `media_type` is the type of media file and `language` is the default language.
    - For example: `image::English (en)`
2. Add a new media column for each translation language using the format `media_type::language (code)`. 
    - For example: `audio::Spanish (es)`
3. In the media column for each language, enter the name of the media file you wish to include, including the extension.
    - To use the same media file for each language, enter the same file name as the one in the default language column.

<p class="note">
    <strong>Note:</strong> If a media file is not listed in a translation column, it will not be displayed for that language. 
</p>

**survey worksheet**

| type | name | label | video::English (en) | video::Chichewa (ny) |
| :--- | :--- | :--- | :--- | :--- |
| note | intro | Before you answer the form, watch the video below: | intro.mp4 | intro_ny.mp4 |
| survey |

### Uploading media files to KoboToolbox

To upload the translated media files to KoboToolbox:
1. Go to your [KoboToolbox account](https://www.kobotoolbox.org/sign-up/).
2. In your KoboToolbox project, navigate to **SETTINGS > Media**.
3. Upload the media files that you have added to your XLSForm, ensuring the file name is exactly the same.
4. Deploy or redeploy your form to see media changes.

<p class="note">
    <strong>Note:</strong> To learn more about managing translations in XLSForm, see <a href="https://support.kobotoolbox.org/language_xls.html">Adding translations in XLSForm</a>.
</p>

## Troubleshooting

<details>
<summary><strong>Error when deploying or viewing form</strong></summary>
If you face an error when deploying or viewing your form, check the following:
    <ul>
      <li>The media file has been uploaded to KoboToolbox in the <strong>Media</strong> tab of the <strong>SETTINGS</strong> page.</li>
      <li>The file name in your XLSForm matches the media file name and extension exactly.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Media files not appearing in deployed form</strong></summary>
If media files are not appearing in your deployed form, check the following:
    <ul>
      <li>The media file has been uploaded to KoboToolbox in the <strong>Media</strong> tab of the <strong>SETTINGS</strong> page.</li>
      <li>The file name in your XLSForm matches the media file name and extension exactly.</li>
      <li>The form has been <strong>redeployed</strong> since you have uploaded the media files.</li>
      <li>You have included media files for each form translation, if relevant.</li>
    </ul>
</details>

<br>

<details>
<summary><strong>Changing the size of a media file</strong></summary>
To control the size of images displayed in your questions or choices, you must upload media files with the desired dimensions. Note that using very large files can increase loading times in Enketo forms.
</details>

<br>

<details>
<summary><strong>Form takes a long time to load</strong></summary>
Enketo forms will load slowly if your media files are large. Reduce the size of image, video, or audio files before uploading them to the server to improve loading times.
</details>

<br>

<details>
<summary><strong>Changing alignment of media files</strong></summary>
Media in KoboToolbox forms is center-aligned by default, and custom alignment (left or right) is not possible.  
</details>

<br>

<details>
<summary><strong>Animated GIF files not supported</strong></summary>
Animated GIF files are not currently supported by either Enketo web forms or the KoboCollect Android app.
</details>

<br>

<details>
<summary><strong>Unable to upload media file</strong></summary>
The maximum size for media uploads is 100 MB. Files exceeding this limit must be reduced in size before uploading.
</details>

