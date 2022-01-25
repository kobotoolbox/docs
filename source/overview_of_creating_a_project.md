# Overview of creating a project in KoboToolbox

Once you’ve logged in to your KoboToolbox account, you can start creating your data collection project right away with our simple-to-use formbuilder. This article gives you a quick overview of how you can create a data collection project, add questions and deploy it for data entry. Use these guidelines as your basic introduction to developing and deploying forms in KoboToolbox, after which you can go through the rest of the articles in this support site to learn in depth about the steps you will learn here.

## Creating your first form

* Upon logging in to your account, click the big blue **NEW** button at the top. You will be presented with the “Create a project: choose a source” dialog box.
  
![Choose a source](images/overview_of_creating_a_project/choose_source.png)

* Click “Build from scratch” to start creating your form using the KoboToolbox formbuilder.

<p class="note"><strong>Use a template</strong>: Allows you to build a form using a template that you have in the library module. <a href="https://support.kobotoolbox.org/add_questions_library">Read more about templates on this link</a> <br /><br />
<strong>Upload XLSForm</strong>: Lets you upload an XLSForm file where you have defined your questions. <a href="https://xlsform.org">Read more about XLSForm on this link</a><br /><br /> 
<strong>Import an XLSForm via URL</strong>: Lets you upload an XLSForm file from an online source such as Google Drive. <a href="https://support.kobotoolbox.org/xls_url.html">Read more about importing XLSForms via URL on this link</a>
</p>

* On the Project Details dialog box that opens up, enter the details of your project and then click **CREATE PROJECT**

![](images/overview_of_creating_a_project/project_details.png)

<p class="note">
<strong> Project name </strong>: The title of your project <br />
<strong>Description (optional)</strong>: A descriptive paragraph to make it easy to identify your project<br />
<strong>Sector (optional)</strong>: The sector in which the data collection project is being deployed<br />
<strong>Country (optional)</strong>: The country where the data collection project will be deployed <br /><br />
You can check the last option to anonymously share the sector and country information with KoboToolbox. The data is used to help improve the KoboToolbox platform.
</p>

## Adding questions

Once the formbuilder opens up, you can start adding your questions.

1. Click the <i class="k-icon k-icon-plus"></i> button below the message that says “This form is empty”.
![](images/overview_of_creating_a_project/add_new_question.png)
2. Type in your question text.
3. Press ENTER or click the **ADD QUESTION** button.
![](images/overview_of_creating_a_project/add_question_button.png)
4. Finally, select the question type from the list (see the practice example below)

<div class="box">
<p><strong> Practice: Adding questions </strong></p>
Let’s add the following questions: <br>
What is your name?<br> How old are you?<br>
Gender: Male; Female; Nonbinary; Prefer not to say
<p><strong>Steps:</strong></p>
<ol>
<li>Click the <i class="k-icon k-icon-plus"></i> button to add a new question</li>
<li>Type: What is your name</li>
<li>Press ENTER or click **ADD QUESTION**</li>
<li>Choose the **Text** question type</li>
<li>To add the second question, click the **+** button just below the question you just added</li>
<image src="_images/add_next_question.png" />
<li>Type: How old are you?</li>
<li>Press ENTER or click **ADD QUESTION**</li>
<li>Choose the **Number** question type</li>
<li>Finally, click the **+** button just below the second question you added</li>
<li>Type: Gender</li>
<li>Press ENTER or click **ADD QUESTION**</li>
<li>Choose the **Select one** question type</li>
<li>On Option 1, type: Male. </li>
<li>On Option 2, type: Female</li>
<li>Click **Click to add another response** and type Nonbinary</li>
<li>Click **Click to add another response** and type Prefer not to say</li>
<li>Click the **SAVE** button at the top right of the formbuilder</li>
</ol>
<p>The form will look as follows:</p>
<image src="_images/questions.png" />
</div>


## Previewing the form

It helps to preview the form to see how it is going to display on data entry. Only the web form preview is available from the formbuilder.

Click the <i class="k-icon k-icon-view"></i> Preview icon on the grey toolbar to go to preview mode

![](images/overview_of_creating_a_project/preview.png)

The form we created in the Adding Questions practice above will display as follows:

![](images/overview_of_creating_a_project/form_preview.png)

You can press the Escape key (Esc) on the keyboard to return to the formbuilder (or click the close button on the Form Preview window)

<p class="note">
KoBoToolbox has functionality that allows you to define <a href="skip_logic.html">Skip logic</a>, <a href="validation_criteria.html">validation criteria</a>, <a href="calculate_questions.html">perform calculations</a> and <a href="language_dashboard.html">add translations</a>. Click the linked articles to learn more about how to add these in your form.
</p>

## Deploying the form

Once you have finished developing the form, you need to deploy it to start data entry. 
1. Make sure you have saved all the changes you have made to the form (If there is a * on the **SAVE** button, you might have changes that need to be saved.)
2. Click the <i class="k-icon k-icon-close"></i> close button next to the **SAVE** button at the top

![](images/overview_of_creating_a_project/close_form.png)

1. Click the **DEPLOY** button.

If you don’t have any errors, a “deployed form” message will appear at the bottom left corner.

Please note that the screen will refresh to show you the current version of the form and options for collecting data using the form.

## Entering data using the web webform

To enter data using the web form:

1. Choose the data entry method from the drop down list below the heading **Collect data**. For the sake of this article, we will leave the default “Online-Offline multiple submission”. This option opens up Enketo Web Form, and allows you to enter multiple submissions to the form even while you are offline. 

![](images/overview_of_creating_a_project/collect_data.png)

For other Web form data entry modes, [read this article](https://support.kobotoolbox.org/data_through_webforms.html)

To learn how to configure and enter data using KoboCollect, [read this article](https://support.kobotoolbox.org/kobocollect_on_android_latest.html)

2. Click **OPEN**
A new window will open with your form.

3. Enter data on the form and click **SUBMIT** when you finish

<div class="box">
<strong>Practice: Adding questions</strong>
Practice entering several dummy records using the form we developed in Adding Questions practice.
</div>

## Viewing the data

After entering some records using the web form: 
1. Switch back to the browser tab where you were developing the form.
2. Refresh the browser window.

You will see the number of records that has been submitted on the top right of the screen:

![](images/overview_of_creating_a_project/submissions.png)

3. View the data submitted, click the “DATA” tab at the top.
  
![](images/overview_of_creating_a_project/data_tab.png)

## Downloading the data

While you are on the data tab:
1. Click on Downloads on the menu on the left.

![](images/overview_of_creating_a_project/downloads_tab.png)

2. Click **EXPORT** to generate an XLS (Excel) file using the default settings.
3. Once the file is generated and shown under the “Exports” table, click the download button next to it.

![](images/overview_of_creating_a_project/exports.png)
  
You can now open your downloaded file.

<p class="note">
<a href="https://support.kobotoolbox.org/export_download.html">Read this article</a> to learn more about exporting and downloading the data
</p>