# Converting Data into SPSS and/or Stata
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c8c238efa59b04f403f13c150b018e1807c66d5c/source/converting_to_spss_and_stata.md" class="reference">28 Oct 2025</a>

<a href="es/converting_to_spss_and_stata.html">Leer en español</a> | <a href="fr/converting_to_spss_and_stata.html">Lire en français</a> | <a href="ar/converting_to_spss_and_stata.html">اقرأ باللغة العربية</a>

<p class="note">
  This article helps you convert your data into <strong>SPSS</strong> and
  <strong>Stata</strong>. Please note you that need
  <strong>IBM SPSS</strong> or <strong>Stata</strong> which are third party
  applications.
</p>

Since **KoboToolbox** does not export data directly in **SPSS** or **Stata**
format, this article will be a guide for you to make the conversion.

## Converting to SPSS

1. Download your data as XLS using the instructions provided in
   [this support article](export_download.md) or as illustrated in the image
   below.

    ![Export XLS](/images/converting_to_spss_and_stata/export_xls.gif)

2. Download the **SPSS Labels** from the same **DATA** tab as shown in the image
   below. This process will generate a zipped folder that contains the **SPSS**
   syntax.

    ![Export SPSS Labels](/images/converting_to_spss_and_stata/export_spss_labels.gif)

3. You will now need **IBM SPSS** to import the data in XLS using the following
   method which is compatible with all versions of **SPSS**.

    - Within **SPSS**, click **File -> Open -> Data** (as below).
    - Once you click the **Data** tab, you will see a data box that will appear.
      In the **Files** of type box, select **Excel**.
    - Navigate to the folder that contains your **Excel** file, and find the
      **Excel** file that contains the data you downloaded.
    - Open the file, and you’ll get the **Read Excel File** dialogue box.

    ![Import into SPSS](/images/converting_to_spss_and_stata/import_into_spss.gif)

4. Now open the syntax you downloaded in _Step 2_ and run the syntax.

    ![Run Syntax](/images/converting_to_spss_and_stata/run_syntax.jpg)

You are now ready to manipulate your data in **SPSS**.

## Converting the SPSS file into a STATA file

Unfortunately we do not have an option to directly download an **SPSS DO** file.
You need to go through the above process then save the final data as a `.dta`
**Stata** data.

Ensure you choose to save all the options you need when saving.

![dta data](/images/converting_to_spss_and_stata/dta_data.jpg)
