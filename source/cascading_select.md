# Adding Cascading Select Questions

Cascading select questions are sets of questions whose options depend on the response to a previous question. For example, your form may first ask the region where a respondent is from, and then in the next question list only the towns and villages of that region.
 
Adding sets of cascading select questions to your form can be done by importing them to a draft form in the formbuilder or adding them manually to an XLS Form and then uploading that file.

#### Importing cascading question sets in the formbuilder

_(Note: This is only available in the new version of KoBoToolbox)_

![image](/images/cascading_select/cascade_import.gif)  

1. Open Excel or another spreadsheet program and create your template of questions and responses to be added.  

2. [Follow this template as an example](https://docs.google.com/spreadsheets/d/1C_uDOkjjbv5Kx3lyOY7ORwM-muW6BKVzdaPMB1X8-2A/edit#gid=0) and follow the instructions in the template.  

3. Select and copy the whole cascading table template, then paste it into the Import Cascade, then click Done to import it. (If there were any mistakes in the formatting you will not be able to import the set - correct any formatting mistakes and make sure you followed the template instructions.)  

4. You can move the imported questions anywhere in your form and change the labels of both the question and responses and delete responses.  

5. If you want to add additional responses to the cascading list just delete the imported questions and import a new list from your spreadsheet.  

#### Adding cascading question sets in XLS Form (Option 1)

1. (If you have an existing form, download it as XLS to your computer and open it in Excel or another spreadsheet program).

2. In the survey sheet, add new lines for the questions you'd like to add, following [this template](https://docs.google.com/spreadsheets/d/10gpBV6YaYGx1i367hyW-w1Ms9tkUQnCx0V8YsdwYxmk/edit#gid=0).  

    ![image](/images/cascading_select/survey.png)  
    
3. In the same sheet, add a column called choice_filter and add the XLSForm reference to each of the parent items.

4. In the choices sheet of the file add all the options you would like to appear in the different questions, e.g. the lists of states, counties, and cities (follow the above template).  

    ![image](/images/cascading_select/choices.png)  

5. Note that for each of the child elements you need to add a column to specify its parent. For example, King and Pierce counties are in Washington state, so you would write 'washington' into the 'state' column for these two counties.

6. Save your form. In KoBoToolbox open the main menu and click on Projects. From here you can upload and deploy your form directly, including the newly added cascading select questions.

    ![image](/images/cascading_select/upload.png)  
    
#### Adding cascading question sets in XLS Form (Option 2)

Sometimes it is so required that a researcher wishes to limit the responses (choices) from the previous question to the subsequent question. For this one could do as follows:

**In the survey tab of the xlsform:**

![image](/images/cascading_select/survey_1.png)

**In the choices tab of the xlsform:**

![image](/images/cascading_select/choices_1.png)  

**Screenshot (while collecting data) in Enketo:**

![image](/images/cascading_select/preview.png)  

As seen in the screenshot (above), you will be able to restrict the choices in **Q2** based on the choices that you entered in **Q1**.
