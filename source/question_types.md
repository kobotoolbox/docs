# List of Question Types
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/531e3363e769126679697d4a7219e3de3d94f1fa/source/question_types.md" class="reference">6 Jan 2022</a>

The below table provides a high-level summary of each of the response types available to use in your XLSForm and formbuilder:

| Question type | Icon | Answer input |
| --- | --- | --- |
| integer | <i class="k-icon k-icon-qt-number"></i> | Integer (i.e., whole number) input. |
| decimal | <i class="k-icon k-icon-qt-decimal"></i> | Decimal input. |
| range | <i class="k-icon k-icon-qt-range"></i> | Range input (including rating). |
| text | <i class="k-icon k-icon-qt-text"></i> | Free text response. |
| select_one [options] | <i class="k-icon k-icon-qt-select-one"></i> | Multiple choice question; only one answer can be selected. |
| select_multiple [options] | <i class="k-icon k-icon-qt-select-many"></i> | Multiple choice question; multiple answers can be selected. |
| select_one_from_file [file] | <i class="k-icon k-icon-qt-select-one"></i> | Multiple choice from file; only one answer can be selected. |
| select_multiple_from_file [file] | <i class="k-icon k-icon-qt-select-many"></i> | Multiple choice from file; multiple answers can be selected. |
| rank [options] | n/a | Rank question; order a list. |
| note | <i class="k-icon k-icon-qt-note"></i> | Display a note on the screen, takes no input. Shorthand for type=text with readonly=true. |
| geopoint | <i class="k-icon k-icon-qt-point"></i> | Collect a single GPS coordinate. |
| geotrace | <i class="k-icon k-icon-qt-line"></i> | Record a line of two or more GPS coordinates. |
| geoshape | <i class="k-icon k-icon-qt-area"></i> | Record a polygon of multiple GPS coordinates; the last point is the same as the first point. |
| date | <i class="k-icon k-icon-qt-date"></i> | Date input. |
| time | <i class="k-icon k-icon-qt-time"></i> | Time input. |
| dateTime | <i class="k-icon k-icon-qt-date-time"></i> | Accepts a date and a time input. |
| image | <i class="k-icon k-icon-qt-photo"></i> | Take a picture or upload an image file. |
| audio | <i class="k-icon k-icon-qt-audio"></i> | Take an audio recording or upload an audio file. |
| background-audio | <i class="k-icon k-icon-background-rec"></i> | Audio is recorded in the background while filling the form. |
| video | <i class="k-icon k-icon-qt-video"></i> | Take a video recording or upload a video file. |
| file | <i class="k-icon k-icon-qt-file"></i> | Generic file input (txt, pdf, xls, xlsx, doc, docx, rtf, zip) |
| barcode | <i class="k-icon k-icon-qt-barcode"></i> | Scan a barcode, requires the barcode scanner app to be installed. |
| calculate | <i class="k-icon k-icon-qt-calculate"></i> | Perform a calculation; see the Calculation section below. |
| acknowledge | <i class="k-icon k-icon-qt-acknowledge"></i> | Acknowledge prompt that sets value to "OK" if selected. |
| hidden | <i class="k-icon k-icon-qt-hidden"></i> | A field with no associated UI element which can be used to store a constant. |
| xml-external | <i class="k-icon k-icon-qt-external-xml"></i> | Adds a reference to an external XML data file. |

For more information on the response types, please visit [xlsform.org](http://xlsform.org/).

Additionally, KoboToolbox-specific types can also be used from within the formbuilder:

| Formbuilder Question type | Icon | Answer input |
| --- | --- | --- |
| Rating | <i class="k-icon k-icon-qt-rating"></i> | Compare different items using a common scale. |
| Ranking | <i class="k-icon k-icon-qt-ranking"></i> | Compare a list of different objects to one another. |
| Question Matrix | <i class="k-icon k-icon-qt-question-matrix"></i> | Create a group of questions that display in a matrix format. |

<p class="note"><a class="reference" href="/calculate_questions.html">Calculate Questions</a> are not displayed in your form, but are executed automatically as your form is being answered.</p>

<p class="note">The <a class="reference" href="matrix_response.html">Question Matrix Type</a> is only supported in Enketo and with the Grid Theme set. </p>
