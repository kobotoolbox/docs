# Select One or Many From External File Question Type

In some cases, it may be desirable to host a list of choice options in an external file, rather than directly in the project XLSForm. For example, a long list of choices (e.g. hundreds or thousands) could slow down the loading and navigation of the form, or adding new choice options after data collection has begun could sometimes be troublesome.

This article provides a detailed example and method for creating a `select_one` or `select_many` question type with the choice list in a separate, external file. Refer to the [XLSForm documentation](https://xlsform.org/en/#multiple-choice-from-file) for more information.

**1.** In the XLSForm, the type should be either `select_one_from_file [filename]` or `select_multiple_from_file [filename]`:

<p class="note">The file-type can be either <code>CSV</code> or <code>XML</code></p>

__survey__

| type                            | name   | label                         |
| ---                             | ---    | ---                           |
| text                            | name   | What is your name?            |
| select_one sex                  | sex    | What is your sex?             |
| select_one_from_file fruits.csv | fruits | What is your favourite fruit? |

<br/>

__choices__

| list_name | name | label  |
| ---       | ---  | ---    |
| sex       | 1    | Male   |
| sex       | 2    | Female |

<br/>

<p class="note">The <code>fruits.csv</code> is the file name containing the choices for the question "What is your favorite fruit?".</p>

**2.** Create a new `CSV` file and structure it the same as the `choices` sheet in the XLSForm:

__fruits.csv__

| list_name | name | label       |
| ---       | ---  | ---         |
| fruits    | 1    | Apple       |
| fruits    | 2    | Watermelon  |
| fruits    | 3    | Orange      |
| fruits    | 4    | Pear        |
| fruits    | 5    | Cherry      |
| fruits    | 6    | Strawberry  |
| fruits    | 7    | Nectarine   |
| fruits    | 8    | Grape       |
| fruits    | 9    | Mango       |
| fruits    | 10   | Blueberry   |
| fruits    | 11   | Pomegranate |

<br/>

**3.** Upload and deploy the XLSForm in KoBoToolbox.

**4.** Upload the `CSV` file the same way you would [add a media file to the form](media.md)

