# Managing respondent-submitted media

Media files collected from respondents often contain important contextual information, such as photos, recordings, or documents that support and enrich survey data. After data collection begins, **these files become part of your project data** and need to be managed carefully.

This article explains how to view, download, and delete media files submitted by respondents, including images, audio recordings, videos, and other file types.

## Viewing media files

All media files submitted by respondents can be viewed from your project’s data table. To open media files in individual submissions:

1. Open your project and go to the **DATA** page.
2. In the data table, locate the cell containing the file.
3. Click the <i class="k-icon-qt-photo"></i> **image**, <i class="k-icon-qt-video"></i> **video**, or <i class="k-icon-qt-file"></i> **file** icon. For audio recordings, click **Open**. <i class="k-icon-arrow-up-right"></i>

![Gallery view for images](images/managing_media_responses/table.png)

Images can also be viewed in the **Gallery** view of your project. To view all images collected within a single project:

1. Open your project and go to the **DATA** page.
2. Open the <i class="k-icon-file-image"></i> **Gallery** tab from the left-side menu.
3. The **Gallery** view displays all images collected in the project. You can filter images by question or by date range.

## Downloading media files

You can download media files either individually from the data table, or in bulk from the **Downloads** page.

### Downloading individual media files

To download a single file:

1. Go to the **DATA** page.
2. In the data table, locate the cell containing the file.
3. Click the <i class="k-icon-qt-photo"></i> **image**, <i class="k-icon-qt-video"></i> **video**, or <i class="k-icon-qt-file"></i> **file** icon. For audio recordings, click **Open.** <i class="k-icon-arrow-up-right"></i> 
4. Click the <i class="k-icon k-icon-more"></i> three dots at the top of the preview.
5. Click <i class="k-icon-download"></i> **Download.**

![Download media](images/managing_media_responses/download.png)

### Downloading media files in bulk

To download media files in bulk:

1. Go to the **DATA** page.
2. Open the **Downloads** tab from the left-side menu.
3. Under **Select export type**, choose **Media Attachments (ZIP)**.
4. Click **New Export** and wait for the export to complete.
5. Download the generated `.zip` file from the table.

In the downloaded folder, attachments are grouped by submission. Each folder name corresponds to the submission’s `_uuid`, which also appears as a column in the dataset.

<p class="note">
<strong>Note:</strong> Media exports include only questions that are present in the most recent version of the form.
</p>

When you export your data in CSV or XLS format, the exported file also includes hyperlinks that open the associated media files in a web browser, as long as the default option to **Include media URLs** is selected.

<p class="note"> 
  To learn more about exporting your data, see <a href="https://support.kobotoolbox.org/export_download.html">Exporting and downloading your data</a>.
</p>

## Deleting media files

<iframe src="https://www.youtube.com/embed/J0-mh1R6dEs?si=9t0JFhEVdVcf21lk" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

You may need to delete media files from your KoboToolbox project for various reasons, such as maintaining confidentiality, managing storage space, or correcting submission errors. You can delete media files individually, or delete multiple files in bulk.

## Deleting individual media files

There are two ways to delete individual media files: directly from the data table or by opening the submission. Once a file is deleted, it is marked as _Deleted_ in the data table and cannot be recovered.

### Deleting individual media files from the data table

You can delete individual images, videos, and files directly from the data table, with the following steps:

1. In the data table, locate the cell with the media file you want to delete.
2. Click the <i class="k-icon k-icon-qt-photo"></i> **image**, <i class="k-icon k-icon-qt-video"></i> **video**, or <i class="k-icon k-icon-qt-file"></i> **file** icon.
3. Click the <i class="k-icon k-icon-more"></i> **three dots** at the top of the file preview.
4. Click <i class="k-icon k-icon-trash"></i> **Delete**, then **Delete** again to confirm.

![Delete media from table](/images/managing_media_responses/delete_from_table.png)

### Deleting individual media files in the submission view

You can also delete media files by opening the submission view:

1. In the data table, locate the submission with the media files you want to delete.
2. On the left side of the submission, click <i class="k-icon k-icon-view"></i> **Open**.
3. Scroll down to the media file you want to delete.
4. Click the <i class="k-icon k-icon-more"></i> **three dots** to the right of the media file.
5. Click <i class="k-icon k-icon-trash"></i> **Delete**, then **Delete** again to confirm.

![Open submission view](/images/managing_media_responses/open_submission_view.png)

### Deleting audio files in the audio question view

You can delete audio files by opening the audio question view for transcription, translation, and analysis of audio questions:

1. In the data table, click on **Open** <i class="k-icon k-icon-arrow-up-right"></i> to open the audio question view.
2. In the **TRANSCRIPT**, **TRANSLATIONS**, or **ANALYSIS** tab, locate the audio file in the top right corner.
3. Click the <i class="k-icon k-icon-more"></i> **three dots** to the right of the audio file.
4. Click <i class="k-icon k-icon-trash"></i> **Delete**, then **Delete** again to confirm.

![Delete audio](/images/managing_media_responses/delete_audio.png)

### Deleting media files in bulk

You may need to delete media files in bulk, for example, to manage storage space after they have been exported. You can delete all media files for selected submissions using the following steps:

1. Select the submissions for which you want to delete media files.
2. Click **Delete media files only** above the data table.
   * This action opens a modal showing the number and types of media files to be deleted with this selection. 
3. Check the box that says "You are about to permanently remove the following media files from the selected submissions:".
   * This step acknowledges that the files will be permanently deleted and are not recoverable.
4. Click **Delete**.

<p class="note">
  <strong>Note:</strong> With this approach, all media files from each selected submission will be deleted; it is not currently possible to choose only files for a given question.
</p>

![Bulk delete media files](/images/managing_media_responses/bulk_delete.png)

## Troubleshooting

<details>
  <summary><strong>Download as Media Attachments (ZIP) stuck as pending</strong></summary>
  If a <strong>Media Attachments (ZIP)</strong> export remains in the status <strong>Pending ... Click to refresh</strong> for an extended period, refresh the page or leave the <strong>Downloads</strong> page and return to it. Do not repeatedly click <strong>Click to refresh.</strong>
</details>

