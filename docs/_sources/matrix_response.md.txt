# Question Matrix response type

The Question Matrix response type allows users to create a group of questions that display in a matrix format, whereby each cell within the matrix represents a separate question. To use this response type, define the number of rows and columns you want in your matrix set and give each row and column a label or name. Each column can be a different question type. In the above screenshot, the first two columns are select-one questions, and the third column is a number question. 

![image](/images/matrix_response/matrix_example.png)

**NOTE**: This response type **only works when using Enketo**, utilizing the **Grid-theme layout**. Forms are set to single page layout by default -- to change it, find the "layout" button in the formbuilder toolbar, select "grid-theme", save this change, and redeploy your form to make these changes live.

**Create a Question Matrix in the Formbuilder**

1. Go to your Form Builder and click on “Add question”
2. Select  ‘Question Matrix’

    ![image](/images/matrix_response/question_matrix.png)
    
3. Click on the gear icon in each column to set the question type.

    ![image](/images/matrix_response/question_type.png)

4. Select the question type

5. Add the Column label & response label

    ![image](/images/matrix_response/label_response.png)

6. Select the gear icon within ‘Row’ to define the row label

    ![image](/images/matrix_response/row.png)

**Create a Question Matrix in XLSForm**

Alternatively, you can also build a Matrix Question in a XLSForm by following the instructions as outlined in the images below:

**In the survey tab:**

![image](/images/matrix_response/survey_xls.png)

**In the choices tab:**

![image](/images/matrix_response/choices_xls.png)

**In the settings tab:**

![image](/images/matrix_response/settings_xls.png)

_Please note: this method uses **begin_kobomatrix**, **end_kobomatrix** and **kobo—matrix_list**._

Following the steps above, you should see the question matrix shown in the screenshot below (In Enketo only):

![image](/images/matrix_response/preview.png)
