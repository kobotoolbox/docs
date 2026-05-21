# Qualitative analysis of audio responses in KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/3d800e00d14000ecaa30ed97fcbf03a9feee65eb/source/qualitative_analysis.md" class="reference">3 May 2024</a>

<iframe src="https://www.youtube.com/embed/Ud65hNS_cuo?si=aFfCfExpyn3MZVAs" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Qualitative analysis helps you turn open-ended audio responses into clear, usable insights. This is especially valuable in research and emergency response, where important context can be missed in quantitative data alone.

KoboToolbox offers two ways to analyze qualitative audio responses. You can either **analyze data manually** or use **artificial intelligence (AI)** to generate the analysis. Using analysis questions, you can summarize, categorize, and describe each response, then save those results as new columns in your dataset.

This article explains how to create analysis questions, analyze responses manually or with AI, review and verify results, customize display settings, and move between responses during analysis.

## Creating analysis questions

To use qualitative analysis, your form must include at least one **Audio** question or have [background audio recording](https://support.kobotoolbox.org/recording-interviews.html#recording-interviews-with-background-audio-recordings) enabled. It may be helpful to transcribe or translate your audio files before you begin, but this is not required.

<p class="note">
<strong>Note:</strong>
   Qualitative analysis is currently available only for audio responses, including background audio recordings. It is not supported for text or other response types. 
</p>

To start analyzing your qualitative data:

1. Open your project and go to **DATA > Table.**
2. Click **Open** in the cell of the audio response you want to analyze.
3. Open the **ANALYSIS** tab.
4. Click **Add question.**
5. Enter a title for the analysis question. 
    - This title becomes the column name in your dataset.
6. Select the question type you want to use, and add answer choices if needed.

![Add question](images/qualitative_analysis/add_question.png)

Each analysis question you create will appear in the **ANALYSIS** tab for other responses to the same audio question.

<p class="note">
<strong>Note:</strong>
You can also <a href="https://support.kobotoolbox.org/qualitative_analysis.html#adding-hints">add hints</a> to analysis questions or answer choices. This is a good place to add information from a codebook or instructions for coders. 
</p>

### Analysis question types

The following question types are available for analysis questions:

| Question type | Description | 
|:----|:----|
| <i class="k-icon k-icon-tag"></i> Tags | Add keywords or themes to describe the audio response. |
| <i class="k-icon-qt-text"></i> Text | Add an open text response, such as a summary, notes, or overall impression. |
| <i class="k-icon-qt-number "></i> Number | Record a number, such as the respondent's age or the number of times a theme is mentioned. |
| <i class="k-icon-qt-select-one"></i> Single choice | Select one option from a list, such as the main theme or perceived level of satisfaction. |
| <i class="k-icon-qt-select-many"></i> Multiple choice | Select one or more options from a list, such as themes or barriers mentioned in the response. |
| <i class="k-icon-qt-note"></i> Note | Add instructions or section labels to organize the analysis workspace. |

Each field you add becomes a new column in your dataset when you download your data.

### Adding hints to analysis questions

Hints can help make your analysis more consistent, whether responses are reviewed by human coders or generated with AI. Use hints to explain how each analysis question should be answered.

For example, you can add:

- A full codebook or coding framework
- Definitions for tags, categories, or themes
- Examples of how to apply each answer choice
- Instructions for handling unclear or incomplete responses
- Any guidance you would normally give to a human coder
- Prompt-style instructions for AI-generated analysis

![Add hints](images/qualitative_analysis/hints.png)

Hints can be **especially useful when using AI**, because they give the AI more context about how to interpret the audio response and how the analysis should be structured. 

Hints do not have a word limit, so you can include detailed instructions when needed. We recommend keeping hints clear and specific so they are easy for both team members and AI tools to follow.

<p class="note">
<strong>Note:</strong>
    If your hints are very long, such as detailed instructions for AI-generated responses, you can disable the <strong>Show hints</strong> button at the top of the <strong>Analysis</strong> window to hide them.
</p>

## Analyzing your data

You can analyze responses manually or use AI to generate a response.

- **For manual analysis:** Manually enter a response for each analysis question.
- **For automated analysis:** Click Generate with AI under the question. After a few seconds, a response will be generated. You can then review the response and edit it if needed.

![Generate analysis with AI](images/qualitative_analysis/generate.png)

<p class="note">
<strong>Note:</strong>
A response that has been generated with AI will include the mention <strong>AI-generated</strong> underneath the question.    
</p>

### Reviewing and verifying responses

For both manual and AI-generated analysis, you can review each response and mark it as verified. This can help with quality control, whether you are checking coding across a team or confirming that an AI-generated response is accurate.

To verify a response, check the **Verified** box below it. If you leave the box unchecked, the analysis result will still be saved, but your team will be able to see that it has not yet been reviewed. 

![Verify analysis](images/qualitative_analysis/verify.png)

### Viewing and exporting analysis data

When you finish analyzing your audio files, each analysis field is saved as a new column in your dataset. Your dataset will also include a **Verified** column with **Yes** or **No** values. 

![Data table](images/qualitative_analysis/data_table.png)

You can [download](https://support.kobotoolbox.org/export_download.html) your data with these analysis fields included for further review, synthesis, or reporting. For example, you can use them to track how often specific themes appear across your transcripts.

### Customizing the display settings

By default, the display panel on the right side of the **ANALYSIS** screen shows the audio recording, the original transcript, and responses to other questions.

You can change the display to include the information that best supports your analysis. For example, if you are working in multiple languages, you may want to show a translation or hide the original transcript.

To change the display:

1. Click **Display settings** in the top right corner.
2. Select the information you want to show.

![Display settings](images/qualitative_analysis/display.png)

You can choose to show or hide:

- The audio recording
- Responses to other questions in the form (all or specific questions)
- The original transcript
- Transcript translations

If the recording has not been transcribed, only the audio recording and submission data will be available.

<p class="note">
<strong>Note:</strong>
To learn more about transcription and translation of audio responses in KoboToolbox, see <a href="https://support.kobotoolbox.org/transcription-translation.html#">Transcription and translation of audio responses</a>.
</p>

### Switching to a different question or transcript

You can analyze only one audio response at a time, but you can move easily between responses and questions.

To switch to the next or previous submission, use the arrows to the left of the **DONE** button.

![Switch submission](images/qualitative_analysis/switch_submission.png)

To switch to a different audio question within the same submission, use the drop-down menu at the top of the screen and select the question you want to analyze. You will be able to add **new analysis questions** for this audio question.

![Switch question](images/qualitative_analysis/switch_question.png)

## Usage limits for AI-generated analysis

Community Plan users can make up to 25 AI-generated analysis requests for free. Each time you click **Generate with AI**, it counts as one request.

If you need more AI-generated analysis requests, you can [upgrade](https://www.kobotoolbox.org/pricing/) to a plan with a higher quota or purchase a **Natural Language Processing (NLP)** add-on. ​​You can always continue using the manual analysis features with no usage limit.

