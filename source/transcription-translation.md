# Transcription and translation of audio responses
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/transcription-translation.md" class="reference">31 Oct 2025</a>


<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

KoboToolbox’s natural language processing tools help you collect, manage, and analyze qualitative data more effectively. These tools include automatic speech-to-text transcription and machine translation, with automated qualitative analysis coming soon. The original transcript for your audio files and all translated text are added as new data columns in the data table and can be [downloaded](https://support.kobotoolbox.org/export_download.html) alongside your survey data.

To use these features, first collect audio responses in your form using the [Audio question type](https://support.kobotoolbox.org/photo_audio_video_file.html) or [background audio recordings](https://support.kobotoolbox.org/recording-interviews.html).


<p class="note">
    <strong>Note</strong>: Automatic transcription and translation may not be available for <a href="#language-list">all languages</a>. For these languages, only manual transcription and translation are possible.
</p>

## Adding automatic transcriptions

![Adding automatic transcriptions example](images/transcription_translation/transcription.png)

To start transcribing your audio responses:

1. Open your project and navigate to **DATA > Table**.
2. Click the **Open** button next to the audio response you would like to transcribe.
3. In the **TRANSCRIPT** tab, click **begin**.
    - Select the original language of the audio file and the **automatic** option (the **manual** option will allow you to manually transcribe the audio recording).
    - Click **create transcript** to begin the automatic transcription.
4. Once the transcript is complete, you can edit it manually. You can play the audio recording in the top right corner to help check the accuracy of the transcript.
    - After editing the transcript, click the **Save** button to ensure your work is safely stored.
5. When complete, either click **DONE** to exit, navigate to the next submission by clicking the arrows next to the **DONE** button, or proceed to the **TRANSLATIONS** tab.
    - If you click **DONE**, you will be taken back to the data table view, where a new column containing the transcript will have been added.

<p class="note">
    <strong>Note</strong>: Automatically generated transcripts and translations must be saved to prevent data loss. Navigating away from the page without saving will result in losing the data.
</p>

## Adding automatic translations

![Adding automatic translations example](images/transcription_translation/translation.png)

Once you have a completed transcript for your audio response, you can add translations into multiple languages:

1. Proceed to the **TRANSLATIONS** tab.
    - The translation option is only available once a transcript has been completed.
2. Click **begin** and choose the language of the translation.
    - Click **automatic** for machine translation (the **manual** option will allow you to manually translate the transcript)
    - Click **create translation** to begin the automatic translation
3. Once the translation is complete, you can edit it manually. The original transcript appears on the right of the screen, and the original audio appears underneath. 
    - After editing the translation, click the **Save** button to ensure your work is safely stored.
4. When the translation is complete, you can add another translation by clicking <i class="k-icon-plus"></i> **new translation**, move to the next submission by clicking the arrows next to the item number in the top right corner, or click **DONE** to navigate back to the data table.

<p class="note">
    <strong>Note</strong>: Audio files can only contain a single transcript, but each transcript may have multiple translations.
</p>

## Language list

These natural language processing features integrate automated speech recognition (ASR) and machine translation (MT) capabilities provided by Google Cloud Compute, which currently offers automatic transcription in 72 languages (with 138 regional variants) and automatic translation in 106 languages. For manual transcription or translation, you can select from approximately 7,000 languages based on the ISO 639-3 comprehensive list, maintained by SIL International (filtered for "living languages"). If a language supports ASR or MT, you can choose between **manual** and **automatic** methods. For other languages, only the **manual** method is available.

If you cannot find a language in the list, consider alternative spellings or names. All language names are currently listed using their English names and spelling (e.g., Spanish instead of Español). For languages with fewer speakers, there might be alternative names. For example, the Bura language in Northern Nigeria is listed as Bura-Pabir but is also known as Bourrah or Babir.

<p class="note">
    <strong>Note</strong>: When manually transcribing audio responses, it is important to select the correct language. If the manually generated transcript does not accurately match the chosen language or region, subsequent automatic translations using that transcript may be incorrect and produce inaccuracies.
</p>

## Troubleshooting

<details>
    <summary><strong>Translation not loading</strong></summary>
    Sometimes, the second translation may get stuck with a loading icon. If this happens, refresh the page, and the translation should appear. This is an issue we are working to fix.
</details>


