# Question appearances in XLSForm
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/485fe4fed42cbb765b4838cb7f8c9665a561d091/source/appearances_xls.md" class="reference">25 Nov 2025</a>

Question appearances allow you to customize how questions are displayed in the form and the type of responses they collect. This article explains how to add question appearances in XLSForm and lists common appearances by question type. 

It is important to note that some appearances only work in [Enketo web forms](https://support.kobotoolbox.org/enketo.html), while others are supported only in [KoboCollect](https://support.kobotoolbox.org/kobocollect_on_android_latest.html). Consider your data collection method when selecting appearances.

<p class="note">
  <b>Note:</b> This article focuses on setting question appearances in <a href="https://support.kobotoolbox.org/getting_started_xlsform.html">XLSForm</a>. To learn about setting appearances in the KoboToolbox Formbuilder, see <a href="https://support.kobotoolbox.org/using-formbuilder.html">Using the Formbuilder</a> documentation.
<br><br>
For hands-on practice with question appearances in XLSForm, see KoboToolbox Academy's <a href="https://academy.kobotoolbox.org/courses/xlsform-fundamentals">XLSForm Fundamentals Course</a>.
</p>

## Adding question appearances

To add question appearances in XLSForm:
1. In the `survey` worksheet, add an **appearance** column.
2. Enter the name of the appearance in the `appearance` column. Ensure you use the exact spelling and punctuation of the appearance name.
3. Some appearances can be combined and applied to the same question. Combine appearances by entering them in the same cell and separating them with a space.

**survey worksheet**

| type | name | label | appearance |
| :--- | :--- | :--- | :--- |
| text | description | Describe the project. | multiline |
| select_one country_list | country | Which country is this project taking place in? | autocomplete minimal |
| survey |


## Available question appearances in XLSForm
The tables below list common question appearances by question type and shows which are supported in Enketo web forms and KoboCollect.

### Select question types
Select questions allow respondents to [choose from predefined options](https://support.kobotoolbox.org/question_types_xls.html#select-question-types).

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `minimal` | Displays choices in a drop-down menu. | Enketo and KoboCollect |
| `compact` | Displays choices side-by-side with minimal padding and without choice boxes. | Enketo and KoboCollect |
| `label` | Displays choice labels without the choice boxes. | Enketo and KoboCollect |
| `list-nolabel` | Displays the answer choice boxes without the labels. | Enketo and KoboCollect |
| `autocomplete` | Adds a search bar at the top of the option list. | Enketo and KoboCollect (combine with minimal appearance) |
| `horizontal` | Displays the answer choices horizontally in columns. | Enketo only |
| `horizontal-compact` | Displays the answer choices horizontally, with minimal padding and without choice boxes. | Enketo only |
| `likert` | Displays answer choices as a Likert scale (`select_one` only). | Enketo and KoboCollect  |
| `quick` | Auto-advances the form to the next question after an answer is selected (`select_one` only). | KoboCollect only |
| `quickcompact` | Displays choices side-by-side with minimal padding and without choice boxes, and auto-advances to the next question after an answer is selected (`select_one` only). | KoboCollect only |
| `columns` | Displays available choices in 2, 3, 4 or 5 columns depending on screen size. | Enketo and KoboCollect |
| `columns-pack` | Displays available choices with as many as possible on one line. | Enketo and KoboCollect |
| `columns-n` | Displays available choices in the specified number (n) of columns. | Enketo and KoboCollect |
| `map` | Displays a map to select options from. Requires <a href="https://support.kobotoolbox.org/select_from_map_xls.html">defining GPS coordinates</a> in the `choices` sheet (`select_one` only). | KoboCollect only |
| `quick map` | Displays a map to select options from, automatically recording the first selected location without displaying additional information. Requires <a href="https://support.kobotoolbox.org/select_from_map_xls.html">defining GPS coordinates</a> in the `choices` sheet (`select_one` only). | KoboCollect only |

<p class="note">
  <b>Note:</b> Appearances for <code>select_one</code> and <code>select_multiple</code> questions can also be used for <a href="https://support.kobotoolbox.org/select_from_file_xls.html">select from file</a> questions.
</p>

### Integer and decimal question types
Numeric questions are used to [collect whole numbers or decimal numbers](https://support.kobotoolbox.org/question_types_xls.html#numeric-question-types).

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `thousands-sep` | Formats large numbers using a comma separator for thousands. | Enketo and KoboCollect |
| `bearing` | Records a compass reading in degrees (`decimal` only). | KoboCollect only  |
| `counter` | Displays buttons for increasing and decreasing digits (`integer` only). | KoboCollect only |


### Range question type
Range questions are used to [select values within a specified range](https://support.kobotoolbox.org/question_types_xls.html#numeric-question-types).

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `vertical` | Changes the orientation of the number line to a vertical line. | Enketo and KoboCollect |
| `picker` | In KoboCollect, displays a pop-up spinner for selecting values. In Enketo, displays a drop-down menu. | Enketo and KoboCollect |
| `rating` | Displays stars instead of a number line. | Enketo and KoboCollect |
| `distress` | Displays a thermometer instead of a number line. | Enketo and KoboCollect  |


### Text question type
Text questions allow users to [collect open-ended responses](https://support.kobotoolbox.org/question_types_xls.html#text-and-note-question-types).

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `numbers` | Displays a numeric keyboard instead of a text keyboard (e.g., to collect phone numbers). | KoboCollect only |
| `multiline` | Displays a multiline text box for longer text responses. | Enketo and KoboCollect |
| `url` | Displays a clickable URL under the question text and makes the question read-only. Requires entering a URL in the question's `default` column, or in the `calculation` column if the URL includes dynamic values. Also works with `note` questions. | Enketo and KoboCollect |
| `masked` | Masks text entered by the respondent (e.g., a password or confidential information). | KoboCollect only |


### Date question type
Date questions are used to [capture specific calendar dates](https://support.kobotoolbox.org/question_types_xls.html#date-and-time-question-types).

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `month-year` | Captures a month and a year. | Enketo and KoboCollect |
| `year` | Captures only a year. | Enketo and KoboCollect |
| `no-calendar` | Displays a spinner to select the day, month, and year, instead of the default calendar-style picker. | KoboCollect only |
| `coptic` | Displays the Coptic calendar. | KoboCollect only |
| `ethiopian` | Displays the Ethiopian calendar. | KoboCollect only |
| `islamic` | Displays the Islamic calendar. | KoboCollect only  |
| `bikram-sambat` | Displays the Bikram Sambat calendar. | KoboCollect only |
| `myanmar` | Displays the Myanmar calendar. | KoboCollect only |
| `persian` | Displays the Persian calendar. | KoboCollect only |
| `buddhist` | Displays the Buddhist calendar. | KoboCollect only |


### GPS question types
GPS questions are used to [capture the geographic coordinates](https://support.kobotoolbox.org/question_types_xls.html#gps-question-types) of a location, path, or area directly within your forms.

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `maps` | Displays a map for users to visualize the location that is being automatically recorded (`geopoint` only). | KoboCollect only (included in default Enketo appearance)  |
| `placement-map` | Allows for manual selection of a location on a map (`geopoint` only). | KoboCollect only (included in default Enketo appearance)  |
| `hide-input` | Shows a larger map and hides other input fields (latitude, longitude, altitude, accuracy). | Enketo only |


### Image questions
Image questions allow users to [upload or record images](https://support.kobotoolbox.org/question_types_xls.html#media-question-types) directly into their forms.

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `signature` | Allows users to draw their signature. | Enketo and KoboCollect |
| `draw` | Allows users to sketch or create drawings. | Enketo and KoboCollect |
| `annotate` | Allows users to annotate an image by drawing or writing on it. | Enketo and KoboCollect |
| `new` | Prompts users to take a new picture using the device camera (no file upload). | KoboCollect only |
| `new-front` | Prompts users to take a new picture using the device's front-facing camera. | KoboCollect only |


### Barcode questions
Barcode questions allow users to [scan a QR code](https://support.kobotoolbox.org/question_types_xls.html#media-question-types) using the device's camera in KoboCollect.

| Appearance | Description | Compatibility |
| :--- | :--- | :--- |
| `hidden-answer` | Hides the scanned barcode value. | KoboCollect only |
