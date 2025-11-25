# Question types in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/2afa3a0c670fe98b296a79b798f33abf248d0273/source/question_types_xls.md" class="reference">Oct 10, 2025</a>

When adding questions to an XLSForm, you'll need to choose the appropriate **question type**. The question type will depend on the kind of information you want to collect: some question types are more suited for text, others for numbers, dates, or multiple choice inputs.

The question type in XLSForm is entered in the **type** column of the **survey** worksheet. Always use the exact spelling and letter case. You can add additional [appearances](https://support.kobotoolbox.org/appearances_xls.html) to most question types to modify their display or functionality.

<p class="note">
<strong>Note:</strong> While XLSForm is fully integrated within KoboToolbox, some question types have different names and functionalities in the <a href="https://support.kobotoolbox.org/formbuilder.html">Formbuilder</a> than they do in XLSForm. 
</p>

This article covers available question types in XLSForm, including their descriptions and Formbuilder equivalents. Links are provided at the end of each section for more information on question type functionalities and appearances during data collection.

<p class="note">
To learn more about building forms in XLSForm, see <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">Getting started with XLSForm</a>.
</p>

### Select question types

Select questions allow respondents to choose from predefined options. For `select_one`, `select_multiple`, and `rank` questions, [option choices](https://support.kobotoolbox.org/option_choices_xls.html) are defined in the **choices** worksheet of the XLSForm.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `select_one` | Allows respondents to select one option from a predefined list. | Select One |
| `select_multiple` | Allows respondents to select multiple options from a predefined list. | Select Many |
| `rank` | Allows respondents to rank items or options in a choice list. | Ranking |
| `acknowledge` | A single checkbox that respondents can select to acknowledge their agreement with a statement. | Acknowledge |
| `select_one_from_file` | Allows respondents to select one option from a predefined list, stored in an external CSV file. | Select One From External File |
| `select_multiple_from_file` | Allows respondents to select multiple options from a predefined list, stored in an external CSV file. | Select Many From External File |


<p class="note">
To learn more about select question types in KoboToolbox, see <a href="https://support.kobotoolbox.org/select_one_and_select_many.html">Select One and Select Many question types</a>, <a href="https://support.kobotoolbox.org/rating_ranking.html">Rating vs Ranking question types</a>, <a href="https://support.kobotoolbox.org/acknowledge.html">Acknowledge question type</a>, and <a href="https://support.kobotoolbox.org/external_file.html">Select One or Many From External File question types</a>.
</p>


### Numeric question types

Numeric questions are used to collect whole numbers, decimal numbers, or values within a specified range.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `integer` | Allows respondents to input whole numbers. | Number |
| `decimal` | Allows respondents to input numbers that may contain decimal points. | Decimal |
| `range` | Allows respondents to select a numeric value within a specified range constrained by minimum and maximum values, <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">configured</a> in the **parameters column**. | Range |


<p class="note">
To learn more about numeric question types in KoboToolbox, see <a href="https://support.kobotoolbox.org/number_decimal_range.html">Number, Decimal, and Range question types</a>.
</p>


### Text and note question types

Text questions are used to collect open-ended responses, while note questions provide information or give instructions to respondents.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `text` | Provides a text box to collect open-ended responses when choices cannot be easily predefined, such as names, opinions, or detailed descriptions. | Text |
| `note` | Provides information to the respondent without requiring any input, such as instructions or explanations. | Note |


<p class="note">
To learn more about text and note question types in KoboToolbox, see <a href="https://support.kobotoolbox.org/text_and_note.html">Text and Note question types</a>.
</p>

### Media question types

Media questions allow respondents to upload or record images, audio, and video files, or to scan barcodes directly into their forms.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `image` | Allows respondents to upload images or take photos when using the KoboCollect app. The quality of image files can be <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">adjusted</a> in the **parameters** column. | Photo |
| `audio` | Allows respondents to upload an audio file or record audio as a response to a specific question. The quality of audio files can be <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">adjusted</a> in the **parameters** column. | Audio |
| `video` | Allows respondents to upload videos or record videos when using the KoboCollect app. | Video |
| `file` | Allows respondents to upload files, such as text files, spreadsheets, and PDF files. Accepted file types can be <a href="https://support.kobotoolbox.org/question_options_xls.html#additional-question-options">restricted</a> by specifying file extensions in the **body::accept** column (e.g., `.pdf, .docx`). | File |
| `barcode` | Scans a QR code to collect embedded information using the device's camera in KoboCollect. | Barcode |
| `background-audio` | Collects audio continuously while the form is open. Audio recording begins when the form is opened and continues until the form is closed. | Background Audio Recording |


<p class="note">
To learn more about media question types in KoboToolbox, see <a href="https://support.kobotoolbox.org/photo_audio_video_file.html">Media question types</a>, <a href="https://support.kobotoolbox.org/barcode_qrcode_questions.html">Barcode/QR code question type</a>, and <a href="https://support.kobotoolbox.org/recording-interviews.html">Recording interviews using background audio recording</a>.
</p>

### GPS question types

GPS questions are used to capture the geographic coordinates of a location, path, or area directly within your forms.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `geopoint` | Collects a single geographic location, such as the coordinates of a specific school, clinic, or house. Default accuracy and warning accuracy can be <a href="https://support.kobotoolbox.org/question_options_xls.html#question-parameters">configured</a> in the **parameters** column. | Point |
| `geotrace` | Records multiple GPS points that form a line, for example to track a path, trace a route, or map a drain. | Line |
| `geoshape` | Collects points that form an enclosed area, such as a plot of land or a field. | Area |


<p class="note">
To learn more about GPS question types in KoboToolbox, see <a href="https://support.kobotoolbox.org/gps_questions.html">GPS question types</a>.
</p>

### Date and time question types

Date and time questions are used to capture specific calendar dates, times, or both in a single response.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `date` | Captures a specific calendar date, typically in the format of day, month, and year. | Date |
| `time` | Captures a specific time in hours and minutes. | Time |
| `datetime` | Captures both a date and a time in a single combined response. | Date and Time |


<p class="note">
To learn more about date and time questions in KoboToolbox, see <a href="https://support.kobotoolbox.org/date_time.html">Date and Time question types</a>.
</p>

### Calculate and hidden question types

Calculate and hidden questions are used to perform automatic calculations within a form based on previous responses or to store predefined values.

| XLSForm type | Description | Formbuilder equivalent |
| :--- | :--- | :--- |
| `calculate` | Automatically performs calculations within a form based on responses to previous questions. | Calculate |
| `hidden` | Stores predefined values that are not visible to the respondent. The value is <a href="https://support.kobotoolbox.org/question_options_xls.html#default-responses">stored</a> in the **default** column. | Hidden |

To learn more about calculations in the Formbuilder, see <a href="https://support.kobotoolbox.org/calculate_questions.html">Calculate question type</a>. To learn more about calculations in XLSForm, see <a href="https://support.kobotoolbox.org/calculations_xls.html">Adding calculations in XLSForm</a>.

<p class="note">
For hands-on practice with different question types XLSForm, see <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">KoboToolbox Academy's XLSForm Fundamentals Course</a>.
</p>
