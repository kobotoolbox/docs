# List of Question Types

The below table provides a high-level summary of each of the response types available to use in your XLSForm and formbuilder:

| Question type                    | Answer input                                                                                 |
| ---                              | ---                                                                                          |
| integer                          | Integer (i.e., whole number) input.                                                          |
| decimal                          | Decimal input.                                                                               |
| range                            | Range input (including rating)                                                               |
| text                             | Free text response.                                                                          |
| select_one [options]             | Multiple choice question; only one answer can be selected.                                   |
| select_multiple [options]        | Multiple choice question; multiple answers can be selected.                                  |
| select_one_from_file [file]      | Multiple choice from file; only one answer can be selected.                                  |
| select_multiple_from_file [file] | Multiple choice from file; multiple answers can be selected.                                 |
| rank [options]                   | Rank question; order a list.                                                                 |
| note                             | Display a note on the screen, takes no input. Shorthand for type=text with readonly=true.    |
| geopoint                         | Collect a single GPS coordinate.                                                             |
| geotrace                         | Record a line of two or more GPS coordinates.                                                |
| geoshape                         | Record a polygon of multiple GPS coordinates; the last point is the same as the first point. |
| date                             | Date input.                                                                                  |
| time                             | Time input.                                                                                  |
| dateTime                         | Accepts a date and a time input.                                                             |
| image                            | Take a picture or upload an image file.                                                      |
| audio                            | Take an audio recording or upload an audio file.                                             |
| background-audio                 | Audio is recorded in the background while filling the form.                                  |
| video                            | Take a video recording or upload a video file.                                               |
| file                             | Generic file input (txt, pdf, xls, xlsx, doc, docx, rtf, zip)                                |
| barcode                          | Scan a barcode, requires the barcode scanner app to be installed.                            |
| calculate                        | Perform a calculation; see the Calculation section below.                                    |
| acknowledge                      | Acknowledge prompt that sets value to "OK" if selected.                                      |
| hidden                           | A field with no associated UI element which can be used to store a constant                  |
| xml-external                     | Adds a reference to an external XML data file                                                |

For more information on the response types, please visit [xlsform.org](http://xlsform.org/).

Addtional, KoBoToolBox-specific types can also be used from within the formbuilder:

| Formbuilder Question type | Answer input                                                |
| ---                        | ---                                                         |
| Rating                     | Compare different items using a common scale                |
| Ranking                    | Compare a list of different objects to one another          |
| Question Matrix            | Create a group of questions that display in a matrix format |

<p class="note"><a class="reference" href="/calculate_questions.html">Calculate Questions</a> are not displayed in your form, but are executed automatically as your form is being answered.</p>

<p class="note">The <a class="reference" href="matrix_response.html">Question Matrix Type</a> is only supported in Enketo and with the Grid Theme set. </p>
