# Advanced Calculate Question Type
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/050dcc9c8bfb4c528208bbe886979999037f1554/source/advanced_calculate.md" class="reference">28 Oct 2025</a>

<a href="es/advanced_calculate.html">Leer en español</a> | <a href="fr/advanced_calculate.html">Lire en français</a> | <a href="ar/advanced_calculate.html">اقرأ باللغة العربية</a>

This article provides step-by-step instructions on how to add calculations while using the formbuilder or by downloading and adding it directly to the XLSform. 

To view a complete and detailed list of all functions please visit ODK's excellent [XPath Functions documentation](https://getodk.github.io/xforms-spec).  

## Approaches towards adding calculate questions:

### Using the formbuilder

Step 1: Add a calculate question

![image](/images/advanced_calculate/calculate_question.jpg)

Step 2: Type your calculation formulae where you would typically write your question.

![image](/images/advanced_calculate/formulas.jpg)

Note:

* Your calculate question will not be displayed when conducting data entry/collection either on Kobo Collect or Enketo. It will, however, be displayed when looking at the data in the table view or in the downloaded version.  
* You must follow similar rules as for XLS forms (see our section rules below).  

### Using the XLS forms

We recommend this approach when working with more advanced calculate functions. 

XLS forms allow for use of calculate function on different types of question types. 

* You can mimic the approach used in the formbuilder where the question will not be displayed on data collection by simply defining the question type as 'calculate' and then typing your calculation within the calculate column. 
* You can use 'calculate' for different question types, and in this case the question will be displayed during data collection. You can choose to make that question a read-only so that no one can change the entry. The question types we have tested with this approach include:

    a. integer (will only take numeric calculate functions)  
    b. text (will only take string calculate functions)  
    c. note (will take only question referencing and not calculate functions)  
    d. date (will only take date calculate functions)  
    e. time (will only take time calculate functions)  
    
    ![image](/images/advanced_calculate/xls.png)

## Rules when working with calculate questions:

### These rules apply to both the formbuilder and XLSform

1. You cannot use both numeric and string calculations within the same question  
2. Your numeric calculations will follow the BODMAS rule in applying calculations i.e. the order of executing the calculations will be Brackets, Divisions, Multiplications, Additions then Subtractions (Always remember this when ordering a question)  
3. Calculate questions that reference other questions should not be placed on the same group as the reference questions since the calculate will not appear unless you move from the group  
4. When referencing a question in a calculation you need to indicate it as `${Question}` where question is the name of the question  
5. You can "force" a calculation to evaluate by setting 'required' to TRUE  

### List of tested calculate functions

_(Please feel free to recommend additional ones and we will update)_

![image](/images/advanced_calculate/list.png)

### Working with IF command on calculations

![image](/images/advanced_calculate/if_command.png)

### Work-arounds for calculations

_Recommended for advanced users_

#### Workaround 1: Creating Dummy Questions for Calculation of Final Score in a Series of Questions**

Let's say you have a question like  `QN1 Do you have a question?` Answers `Yes=1 No=2 Don’t Know=999`

In this case you may want to create a dummy QN1 right after QN1 to account for the differences in coding and define the mathematical equivalent. So you will create a calculate question QN1d (_note this is my own naming convention d stands for dummy) and define the default value as 0 but write the formula as **If (${QN1}=1,1,0**_) 

Notice in my test form I managed to create the situation and the data appears as coded for Q1N and as calculated for mathematical meaning for Q1Nd. This should be meaning that is meant by your score. _You can do this for calculations such as wealth where Yes and No could mean a different value in different countries._

Once you do this for all your questions you can add a calculate question that sums up all the dummies as:  

`${QN1d}+${QN2d}+ etc`
