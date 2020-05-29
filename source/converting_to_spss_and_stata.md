# Converting your Data into SPSS and/or Stata

#### This article helps you convert your data into SPSS and/or Stata. Please note you need IBM SPSS and Stata which are third party apps

KoboToolBox does not provide direct conversion on the system for the two systems so this is a workaround on how to get this done.

The first thing to note is that exports best work with CSV output, however it can work with excel outputs but we recommend working with a saved CSV version from the excel.

Converting to SPSS

1. The first step involves downloading your data as CSV. You can do this from the DATA tab under downloads

    ![image](/images/converting_to_spss_and_stata/data_csv.jpg)

2. You will then need to download the value labels for SPSS from the same DATA tab. This will generate a syntax for SPSS (An SPSS equivalent of STATA do files). It will give you a zipped folder which you can unzip to get the syntax.

    ![image](/images/converting_to_spss_and_stata/zipped_folder.jpg)

3. You will now need IBM SPSS to import the CSV

    *You should open the location of the CSV you downloaded*

    ![image](/images/converting_to_spss_and_stata/location_csv.jpg)

    ![image](/images/converting_to_spss_and_stata/delimited_csv.jpg)

    ![image](/images/converting_to_spss_and_stata/all_cases.jpg)

    *Ensure you check the boxes Comma and Semicolon*

    ![image](/images/converting_to_spss_and_stata/comma_semicolon.jpg)

    *When you finish you should have your data without label*

    ![image](/images/converting_to_spss_and_stata/without_label.jpg)

4. Now open the syntax you downloaded on step 2 and run the syntax

    ![image](/images/converting_to_spss_and_stata/run_syntax.jpg)

You are now ready to manipulate your data in SPSS

#### Getting STATA file 

Unfortunately we do not a direct download on the system for an SPSS DO file. So you need to go through the above process then save the final data as a .dta stata data. 

Ensure you choose to save all the options you need when saving.

![image](/images/converting_to_spss_and_stata/dta_data.jpg)

Wishing you the best with your data management
