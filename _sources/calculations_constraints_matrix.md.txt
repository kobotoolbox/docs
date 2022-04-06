# Adding Calculations (Column Total & Row Total) and Constraints in a Matrix Question
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/9365be744903eb35c9f2abb3e518733ec1f763e5/source/calculations_constraints_matrix.md" class="reference">6 Apr 2022</a>

When working in the Formbuilder, it is simple to add calculations (see **[Calculate Question Type](calculate_questions.md)**) or constraints (see **[Limiting Responses with Validation Criteria](validation_criteria.md)**) to almost any question type. While  Formbuilder does not currently support directly adding these features to matrix question, you can use an XLSForm to do so. The steps listed below in this support article will illustrate how you can add calculations (column total & row total) and constraints to a matrix question using XLSForm.

**Step 1: Create a matrix question in the Formbuilder**

The first step is creating a matrix question in the Formbuilder (as outlined in the support article **[Question Matrix Response Type](matrix_response.md)**). Simply add rows and columns with the variables necessary for data collection.

**Step 2: Download the form as XLSForm**

Once the matrix question is ready, **SAVE** the form and download it as an XLSForm.

**Step 3: Add all appropriate column headers to your XLSForm**

Open the XLSForm and add `calculation`, `constraint` and `constraint_message` column headers. With these column headers, you will be able to add the *column total* and *row total* expressions under the `calculation` column header. You can also add appropriate *constraints* under the `constraint` column header and *constraint message* under the `constraint_message` header as needed. Additionally, you may also choose to add a `read_only` column header to your XLSForm to restrict enumerators from editing the responses while collecting data to certain questions (for example, the row total and column total that gets auto-calculated).

![Survey Tab](images/calculations_constraints_matrix/survey_tab.png)

<p class="note">In the image above, you may notice that the <b><i>name</i></b> inputs are shorter. In this example, they have been renamed from the ones auto-generated in the formbuilder to capture the entire screenshot of the survey tab. If you choose to rename yours, make sure to use your new variable names in the <b><i>calculation</i></b> and <b><i>constraint</i></b> column headers.</p>

**Step 4: Replace XLSForm**

Upload and replace your XLSForm within the existing project, or create a new project (if needed).

**Step 5: Deploy form**

Once you have replaced the XLSForm (or uploaded the XLSForm as a new project), you will need to deploy your form.

**Step 6: Collect data**

After deploying the form, you can go to **FORM>Collect Data>OPEN** to start collecting data with the web form. 

#### Data entry screen as seen in Enketo (web form): _when nothing is entered_

![Enketo Nothing Entered](images/calculations_constraints_matrix/enketo_nothing_entered.png)

#### Data entry screen as seen in Enketo (web form): _when an input error is made_

![Enketo Wrong Inputs Entered](images/calculations_constraints_matrix/enketo_wrong_inputs_entered.png)

Here you will see that there are only five total household members. If an enumerator enters 6 for the number of males (0-14 Years), the constraint will show an error message.
#### Data entry screen as seen in Enketo (web form): _when there are no input errors_

![Enketo Correct Inputs Entered](images/calculations_constraints_matrix/enketo_correct_inputs_entered.png)

Here, when you enter values in a matrix table, the rows and columns are automatically calculated.

<p class="note">You can access the XLSForm that was used for this article <b><a download href="./_static/files/calculations_constraints_matrix/calculations_constraints_matrix.xlsx">here</a></b>.</p>

## Troubleshooting:

* The matrix question only works with **Enketo**, also known as **web forms**. It is not supported with the `KoboCollect Android App`.

* The matrix table may get distorted if you fail to set the layout to **Grid-theme**. For more details, you refer to one of our other support articles, **[Using Alternative Enketo Web Form Styles](alternative_enketo.md)**.