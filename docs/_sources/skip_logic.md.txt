# Adding Skip Logic to Your Form

Skip logic is also sometimes referred to as 'branching' or 'relevant conditions'. By default, all questions are always visible. Skip logic controls which question should be displayed only if a certain condition (or conditions) is fulfilled. Conditions are always applied to the question or group that should be sometimes hidden, sometimes visible. (This is important, as many paper surveys approach the problem from the other direction, writing things like "If yes, go to question 35".)

Conditions can be added to each question by clicking on Settings inside the question card, then Skip Logic. There are two ways to add a skip logic condition:

**1. Add a condition: Use the skip logic wizard to help you build your conditions**

   ![image](/images/skip_logic/condition.jpg)

   Example

   Q1: Are you currently in school?  
   Q2: Which grade are you in?  

   You would want to display the second question only if the respondent answers 'Yes' to the first question. The correct skip logic condition should display: 

   Q1: Are you currently in school? = Yes

   You can delete skip logic conditions by clicking on the trash can symbol.

   To add multiple conditions, add your first one, then click on the 'Add a condition' button. When using two or more conditions, be sure to choose between the two options whether the question should match any (at least one) of these criteria, or all of them.

**2. Manually enter your skip logic in XLSForm code**

   ![image](/images/skip_logic/code.jpg)
   
   Example

   Q1. Do you rear animals?  
   Q2. Which of these animals do you own?  
   Q3. Kindly type the main breed of dog you own?   

   You would want to display Q2 if Q1 is Yes, so you would need to add the following condition on the relevant column  
              ${Q1} = '1' or ${Q1} = 'Yes'

   Note: This depends on whether the response item is labelled as Yes for Yes or 1 for Yes as in our example

   Q3 will only be displayed if Q2 has Dogs as one of the response items. Since Q2 is a multiple response then you would add this condition in the relevant columns for Q3.  
            selected(${Q2}, 'Dogs')


