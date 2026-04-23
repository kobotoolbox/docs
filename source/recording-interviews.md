# Collecting qualitative data with KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/6f05aaa00b0eaf39e8ec1db4a6529a491fb1c551/source/recording-interviews.md" class="reference">23 Apr 2026</a>

Qualitative data helps you **understand experiences, priorities, and context** that closed-ended questions can miss. It can reveal why people respond in certain ways, how they describe their needs, and what details matter most in a local context.

In practice, qualitative data is often harder to collect and analyze at scale. Writing down open-ended responses, reviewing images, and transcribing audio interviews can take significant time. Because of this, teams often collect less qualitative data than they would like, or struggle to use everything they collect.

KoboToolbox includes features that **make qualitative data collection more practical.** You can collect text, images, audio, video, and background audio recordings in your forms, then review and manage them directly in KoboToolbox. For audio responses, KoboToolbox also includes built-in tools for [transcription, translation](https://support.kobotoolbox.org/transcription-translation.html), and [analysis](https://support.kobotoolbox.org/qualitative_analysis.html).

This article covers the main ways to collect qualitative data with KoboToolbox, including relevant question types, background audio recordings, and options for managing and analyzing qualitative data after collection.

## Question types for qualitative data collection

KoboToolbox supports several question types that are useful for qualitative research and open-ended data collection.

- **Text:** Text questions can be used for short or long written responses. For longer answers, you can use the `multiline` [appearance](https://support.kobotoolbox.org/text_questions.html#advanced-appearances) to give respondents a larger text box.
- **Image:** Image questions can be used to collect photos, sketches, or annotated images. This can be useful for visual documentation, participatory mapping, site observations, or collecting photo evidence. Use the `draw` [appearance](https://support.kobotoolbox.org/photo_audio_video_file.html#advanced-appearances) with image questions to create a drawing, and use the `annotate` appearance to mark up an image.
- **Video:** Video questions can be used to collect video files. This may be useful when visual context, movement, or demonstrations are important.
- **Audio:** Audio questions allow respondents or enumerators to record spoken responses or upload audio files. They are useful for open-ended interviews and other cases where tone and exact wording matter, and they reduce the need for enumerators to summarize responses on the spot.
- **Background audio recording:** Background audio recording captures audio continuously while the form is open. This can be useful for recording a full interview instead of recording separate answers question by question.

<p class="note">
To learn more about qualitative question types, see <a href="https://support.kobotoolbox.org/text_questions.html">Text questions in KoboToolbox</a>, <a href="https://support.kobotoolbox.org/photo_audio_video_file.html#">Media questions in KoboToolbox</a> and <a href="https://support.kobotoolbox.org/form_meta.html#enabling-background-audio-recording">Enabling background audio recording</a>.
</p>

## Collecting qualitative data with KoboCollect vs web forms

Qualitative question types can behave differently depending on whether data is collected in [KoboCollect](https://support.kobotoolbox.org/data_collection_kobocollect.html) or [web forms](https://support.kobotoolbox.org/data_through_webforms.html), and on whether respondents are using a computer or mobile device.

The following table describes how each qualitative question type behaves in KoboCollect and web forms.

| Question type | KoboCollect behavior | Web forms behavior |
|:---|:---|:---|
| Text | Respondents can type their response in a text box. | Respondents can type their response in a text box. |
| Image | Respondents can take photos from the device or upload an image file. | On a computer, respondents can **only upload** an image file.<br><br>When using mobile devices, respondents may also have the option to take a photo from the device. |
| Video | Respondents can record a video from the device or upload a video file. | On a computer, respondents can **only upload** a video file.<br><br>When using mobile devices, respondents may also have the option to record a video from the device. |
| Audio | Respondents can record an audio response or upload an audio file. | Respondents can record an audio response (even from a computer) or upload an audio file. |
| Background audio recording | Records continuously while the form is open, as long as permission to record has been granted. | Records continuously while the form is open (even from a computer), as long as permission to record has been granted. |

<p class="note">
<strong>Note:</strong>
When background audio recording is active on a form, <strong>Audio</strong> question types in <strong>KoboCollect</strong> are deactivated, as it is not possible to record audio using both features simultaneously. 
</p>

## Recording interviews with background audio recordings

Background audio recording is useful when you want to **capture a full interview** rather than separate audio clips for individual questions. It starts when the form opens and continues until the form is closed.

Background audio can be recorded in the KoboCollect app and in web forms. 

- In web forms, a disclaimer appears at the beginning of the form to inform respondents that background audio is being recorded.
- In both web forms and KoboCollect, a microphone icon appears at the top of the form while recording is active and shows the recording duration.

<p class="note">
<strong>Note:</strong>
Background audio recording is collected as form metadata. For more information about setting up background audio recordings in your form, see <a href="https://support.kobotoolbox.org/form_meta.html#enabling-background-audio-recording">Adding form metadata in the Formbuilder</a> or <a href="https://support.kobotoolbox.org/metadata_xls.html">Form metadata in XLSForm</a>.
</p>

### Ethical considerations for audio recording

Before recording audio, **make sure respondents give informed consent.** They should understand that audio is being recorded, why it is being collected, how it will be used, who will have access to it, and how long it will be stored.

Audio data can be especially sensitive. Before using background audio recording, consider whether full interview recordings are necessary for your project and whether they create additional **privacy or protection risks.** Kobo strongly encourages compliance with all applicable data protection and privacy requirements in the place where data collection takes place.

## Managing and analyzing qualitative data

KoboToolbox includes built-in features to help you review qualitative data after collection.

- **Text:** You can review all responses to a text question in **DATA > Report.** This is useful for quickly reading open-ended answers together and spotting common themes.
- **Images:** You can review collected images in **DATA > Gallery.** This makes it easier to browse visual responses across submissions.
- **Video:** Video files can be viewed within individual submissions. This is useful when you need to review visual context alongside other responses from the same record.
- **Audio:** Audio responses, including background audio recordings, can be opened in their own view for review, transcription, translation, and analysis. 

<p class="note">
To learn more about transcribing, translating, and analyzing audio responses, see <a href="https://support.kobotoolbox.org/transcription-translation.html">Transcription and translation of audio responses</a> and <a href="https://support.kobotoolbox.org/qualitative_analysis.html">Qualitative analysis of audio responses</a>.
</p>

Qualitative data is included in your dataset when you [export](https://support.kobotoolbox.org/export_download.html) it, including links to media files for each submission, any transcription, translation, and analysis data, and any text responses. Media files can also be [downloaded separately](https://support.kobotoolbox.org/managing_media_responses.html#downloading-media-files), either individually or in bulk.

## Troubleshooting

<details>
  <summary><strong>Not enough storage on device</strong></summary>
Before collecting qualitative data (e.g., images or background audio recordings), make sure your device has enough storage space to save the files.
</details>

<br>

<details>
  <summary><strong>Not enough storage on KoboToolbox server</strong></summary>
Media files can be large and may cause your account to exceed its storage limit (1 GB for free accounts). If you need more space, you can <a href="https://support.kobotoolbox.org/managing_media_responses.html#deleting-media-files">delete media files</a> from submissions, <a href="https://www.kobotoolbox.org/pricing/">upgrade your plan</a>, or purchase a <strong>storage add-on</strong> in <strong>Account Settings > Add-ons.</strong>
</details>

<br>

<details>
  <summary><strong>Background audio recording not working</strong></summary>
  Your device must have a built-in audio recorder for this feature to work. If your device does not include one, you can download <a href="https://play.google.com/store/apps/details?id=com.media.bestrecorder.audiorecorder&pcampaignid=web_share">Voice Recorder</a> or any other audio recording app on your device.
</details>

<br>

<details>
  <summary><strong>Editing submissions with background audio recording</strong></summary>
If you edit a form that includes background audio from the KoboToolbox platform, the initial recording will not be replaced. A message at the top of the form will say “This submission has a background audio recording.” 
</details>

<br>

<details>
  <summary><strong>Forms with background audio recording saved as drafts</strong></summary>
If a form with background audio recording is saved as a draft in <strong>web forms</strong>, only the initial recording will be retained. The recording will not resume or be replaced when the draft form is reopened. <br><br>
If a form with background audio recording is saved as a draft in <strong>KoboCollect</strong>, recording will resume when the draft form is reopened. Both recordings will be stored together in a single file.
</details>

<br>
