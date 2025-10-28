# Recovering Data From Previous Form Versions
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/01270a828ec846731411368326ba58114adda98e/source/recovering_previous_formdata.md" class="reference">28 Oct 2025</a>

<a href="es/recovering_previous_formdata.html">Leer en español</a> | <a href="fr/recovering_previous_formdata.html">Lire en français</a> | <a href="ar/recovering_previous_formdata.html">اقرأ باللغة العربية</a>

**This article shows steps on how to recover data from previous versions of the form in case of question deletions**

Normally when you change a form, the data will be downloaded based on the definition of that new form. As it is if you changed the name of a question or deleted a question, all the data previously collected on that question will not be visible under the new question unless you chose to include data collected from previous versions as explained below. 

Generally, when you edit your survey forms and redeploy it you should be able to download the data that has been submitted to the server in two different ways. For this, first please see the images below for better understanding:

**Image 1:**

![image](/images/recovering_previous_formdata/no_redeployment.jpg)

**Image 1** is a scenario where there is no redeployment in the survey project while 

**Image 2:**

![image](/images/recovering_previous_formdata/redeployment.jpg)

**Image 2** is a scenario which has redeployment in the survey project (*as shown by the red marking*).

Hence the difference between the project which has no redeployment and which has a redeployment is seen as shown in **image 2** which has a check box with a message **Include fields from all 3 deployed versions**. The **3** as shown in the message is as follows: the fist one as deployed, the second and the third as redeployed version.

The thing that you should keep in mind here is that if you select the check box (*which is by default checked when a project has been redeployed*) marked with **Include fields from all 3 deployed versions** you should be able to download all the cases with the entire variables (*including the variables that has been deleted during the recent deployment*). Similarly, if you do not select the check box, you are allowed to download all the cases **but** with only the variables that are available with the latest deployment.
