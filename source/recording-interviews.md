# Recording an Entire Interview with Background Audio Recording
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/511ea4cb3c698a4b45e7c2b4efd1af4e356e811f/source/recording-interviews.md" class="reference">15 Feb 2022</a>

**Background audio recording** is a powerful feature that allows users to record
an interview in the background (when the form is open) and store the recording
as audio data. This feature enhances qualitative data collection by allowing for
nuanced information to be collected in its entirety.

Background audio recording also allows for supervisors and project managers to
know how their enumerators conducted the interview in terms of data quality
assurance or if they wish to have a backup recording of the transcribed
interview.

Currently, users can record the full interview with the **Collect Android app**
`v1.30` and above. **Enketo** does not yet support this feature.

<p class="note">
  If you require an audio recording instead of the full
  <strong>background-audio recording</strong>, see our support article,
  <a class="reference" href="media.html"
    >Adding Various Types of Media (image, audio, video) to a Form</a
  >.
</p>

## Activating background audio recording in the formbuilder

If you are designing your survey form through the formbuilder and wish to enable
the **background audio recording**, follow the steps shown in the video below:

<video controls>
  <source
    src="./_static/files/recording_interviews/activating_background_audio_recording_UI.mp4"
    type="video/mp4"
  />
</video>

-   Under the **FORM**, select the **Edit** button. _(This step may not be
    required if you are already in the formbuilder)_
-   At the top right corner, select **Layout & Settings** and then **Background
    audio** should be visible.
-   Toggle the **Enable audio recording in the background** button. A
    notification should pop up at the top of the formbuilder.
-   **Voice only** is the default audio quality for the **background audio**.
    You can change the audio quality to **Low** or **Normal** as required (see
    chart below for differences in file size).
-   After making all the necessary configurations, select **SAVE** and **Exit**
    in the formbuilder.
-   **DEPLOY** the form to make it live.

## Including background audio question type in XLSForm

If you are designing your survey form through the XLSForm and want to include a
`background-audio` question type, follow the steps shown in the video below:

<video controls>
  <source
    src="./_static/files/recording_interviews/including_background_audio_question_type_xlsform.mp4"
    type="video/mp4"
  />
</video>

In your XLSForm, add `background-audio` under the `type` column of the
**survey** sheet. This is the question type that will record the audio in the
background.

## Setting an appropriate audio quality

The `parameters` column is optional but it is important to choose the
appropriate parameter. Audio quality is directly related to the file size that
will be stored on the server. Keep in mind how much of your total storage space
you want to use towards your audio files. Refer to the table below when choosing
the appropriate parameter:

| Quality    | Parameters         | Extension | Encoding | Bit rate  | Sample rate | File size    |
| ---------- | ------------------ | --------- | -------- | --------- | ----------- | ------------ |
| normal     | quality=normal     | .m4a      | AAC      | 64 kbps   | 32 kHz      | ~ 30 MB/hour |
| low        | quality=low        | .m4a      | AAC      | 24 kbps   | 32 kHz      | ~ 11 MB/hour |
| voice-only | quality=voice-only | .amr      | AMR      | 12.2 kbps | 8 kHz       | ~ 5 MB/hour  |

You can leave the column blank to have the parameter set to `voice-only`, which
will capture audio well in a quiet interview setting. If you are recording audio
where there could be multiple people talking simultaneously, `low` would be more
suitable. `normal` is the highest quality option and it will use the most
storage space.

## Collecting background audio with Collect Android app

Review our support article,
[Data Collection on KoboCollect App](kobocollect_on_android_latest.md), to learn
in detail about collecting data on the **Collect Android app**.

<video controls>
  <source
    src="./_static/files/recording_interviews/collecting_data_with_background_audio_in_collect_app.mp4"
    type="video/mp4"
  />
</video>

While actively recording background audio with the **Collect Android app**, you
should be able to see a microphone at the top of your form.

![Background audio screen](/images/recording_interviews/background_audio_screen.jpg)

## Viewing audio files that were recorded as background audio

When you have `background-audio` configured for your project, you can view the
recorded audio file under the **DATA>Table** as shown in the image below.

![Data table view](/images/recording_interviews/data_table_view.png)

## Downloading audio files

You can download all background audio files as a ZIP file from
**DATA>Downloads>Media Attachments (ZIP)** as shown in the video below.

<video controls>
  <source
    src="./_static/files/recording_interviews/downloading_audio_files_that_were_recorded_as_background_audio.mp4"
    type="video/mp4"
  />
</video>

## Ethical considerations

When collecting data, it is ethical to have informed consent from survey
respondents prior to data collection, in this case by recording background
audio.

<p class="note">
  We encourage all users to consider ethical implications of their data
  collection and to comply with applicable data protection legislation within
  the jurisdiction of their work.
</p>

## Troubleshooting

-   This feature is supported with the **Collect Android app** `v1.30` and
    above.
-   This feature is currently not supported in the **Enketo web forms**.
-   Your device should have a built-in audio recorder to have this feature work
    smoothly. You can download
    [Audio Recorder](https://play.google.com/store/apps/details?id=com.github.axet.audiorecorder)
    from Google play store if needed.
-   Before starting data collection, ensure that your device has sufficient
    space to store the background audio recordings.
-   If you edit your audio file under **Edit Saved Form**, you will have both
    versions (the original audio file and the edited file) in one single file.
    For example, if you have a background audio of _'Sample testing'_ and you
    edited the recording, changing it to _'Sample for re-testing'_, when you
    download your background audio file, it will consist of the combined
    background audio of _'Sample testing'_ and _'Sample for re-testing'_.
-   If your background audio files take up enough storage space to push your
    total storage over your allotted amount (5GB for all free accounts), you can
    request additional space (for a cost) by reaching out to
    [info@kobotoolbox.org](mailto:info@kobotoolbox.org). The payment is used to
    cover the additional costs associated with large data collection projects
    and ensures that the server remains running well for our users.
-   When you have large and/or long background audio files in your account, you
    may have issues downloading them as **Media Attachments (ZIP)**. In such a
    case, follow our support article
    [Downloading Photos and Other Media](photo_download.md), which should help
    you download large media files from the system.
