# Question Matrix Response Type

The Question Matrix response type allows users to create a group of questions that display in a matrix format, whereby each cell within the matrix represents a separate question. To use this response type, define the number of rows and columns you want in your matrix set and give each row and column a label or name. Each column can be a different question type. In the above screenshot, the first two columns are select-one questions, and the third column is a number question.

![image](/images/matrix_response/matrix_example.png)

<p class="note">This response type <strong>only works when using Enketo</strong>, utilizing the <strong>Grid-theme layout</strong>. Forms are set to single page layout by default -- to change it, find the "layout" button in the formbuilder toolbar, select "grid-theme", save this change, and redeploy your form to make these changes live.</p>

<p class='note'>Enketo supports only up to <code>10</code> columns in versions less than <code>2.8.0</code>, up to <code>13</code> including and after <code>2.8.0</code>.</p>

## Create a Question Matrix in the Formbuilder

1. Go to your Form Builder and click on “Add question”
2. Select ‘Question Matrix’

    ![image](/images/matrix_response/question_matrix.png)

3. Click on the gear icon in each column to set the question type.

    ![image](/images/matrix_response/question_type.png)

4. Select the question type

5. Add the Column label & response label

    ![image](/images/matrix_response/label_response.png)

6. Select the gear icon within ‘Row’ to define the row label

    ![image](/images/matrix_response/row.png)

## Create a Question Matrix in XLSForm

Alternatively, you can also build a Matrix Question in a XLSForm by following the instructions as outlined in the images below:

__survey__

| type             | name | label                                | required | kobo--matrix_list |
| ---              | ---  | ---                                  | ---      | ---               |
| begin_kobomatrix | M1   | Items                                |          | assets            |
| select_one yn    | Q1   | Q1. Which assets do you have at home | TRUE     |                   |
| integer          | Q2   | Q2. Number of assets                 | TRUE     |                   |
| end_matrix       |      |                                      |          |                   |

__choices__

| list_name | name | label |
| ---       | ---  | ---   |
| assets    | car  | Car   |
| assets    | bike | Bike  |
| assets    | tv   | TV    |
| yn        | yes  | Yes   |
| yn        | no   | No    |

__settings__

| style                        |
| ---                          |
| theme-grid no-text-transform |

<p class="note">This method uses <code>begin_kobomatrix</code>, <code>end_kobomatrix</code> and <code>kobo—matrix_list</code>.</p>

Following the steps above, you should see the question matrix shown in the screenshot below (In [Enketo](data_through_webforms.md) only):

![image](/images/matrix_response/preview.png)

It is also possible to include `relevant` and `constraint` conditions within the matrix as follows:

__survey__

| type             | name | label                                | required | kobo--matrix_list | relevant      | constraint |
| ---              | ---  | ---                                  | ---      | ---               | ---           | ---        |
| begin_kobomatrix | M1   | Items                                |          | assets            |               |            |
| select_one yn    | Q1   | Q1. Which assets do you have at home | TRUE     |                   |               |            |
| integer          | Q2   | Q2. Number of assets                 | TRUE     |                   | ${Q1} = 'yes' | . > 2      |
| end_kobomatrix   |      |                                      |          |                   |               |            |

