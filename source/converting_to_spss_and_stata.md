# Converting Data into SPSS and/or Stata

**This article helps you convert your data into SPSS and Stata. Please note you need IBM SPSS and Stata which are third party apps**

Normally the data from our system can be exported as either XLS or CSV. This article helps you convert your data into SPSS and Stata. Kindly note that you need the third-party applications IBM SPSS and Stata to do this.

Since KoboToolbox does not export data directly in SPSS or Stata format, this workaround will help you make the conversion.

## Converting to SPSS

1. Download your data as XLS using the instructions provided in [this support article](https://support.kobotoolbox.org/export_download.html).  In summary, you can export data from the download tab as illustrated in the image below.

    ![image](/images/converting_to_spss_and_stata/Image1_ExportXLS.gif)

2. Download the SPSS labels from the same DATA tab as shown in the image below. This process will generate a zipped folder that contains an SPSS syntax for SPSS.

    ![image](/images/converting_to_spss_and_stata/Image2_ExportSPSSlabels.gif)

3. You will now need IBM SPSS to import the data in XLS using the following method which is compatible with all versions of SPSS. 

   a. Within SPSS, click File -> Open -> Data (as below).
   b. Once you click the Data tab, you will see a data box that will appear. In the Files of type box, select Excel.
   c. Navigate to the folder that contains your Excel file, and find the Excel file that contains the data you downloaded.
   d. Open the file, and you’ll get the Read Excel File dialog box.

    ![image](/images/converting_to_spss_and_stata/Image3_ImportintoSPSS.gif)

4. Now open the syntax you downloaded on step 2 and run the syntax

    ![image](/images/converting_to_spss_and_stata/run_syntax.jpg)

You are now ready to manipulate your data in SPSS

## Converting the SPSS file into a STATA file

Unfortunately we do not have an option to directly download an SPSS DO file. You need to go through the above process then save the final data as a .dta stata data. 

Ensure you choose to save all the options you need when saving.

![image](/images/converting_to_spss_and_stata/dta_data.jpg)

Wishing you the best with your data management.
