# Using HXL Tags
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/hxl.md" class="reference">31 Oct 2025</a>


## What exactly is HXL?

HXL stands for **Humanitarian Exchange Language**. The goal of HXL is to improve
information sharing during a humanitarian crisis by creating a simple way to
promote interoperability of data. It does this by coding the data through
hashtags (#) similar to Twitter. For more information on HXL, please
[visit here](https://hxlstandard.org).

## How to use the HXL feature in the formbuilder

_Credits: [David Megginson](http://www.megginson.com)_ _Link to step-by-step
[slide show guide](https://docs.google.com/presentation/d/123bHSkNh4T30CNq0i37IxOLfrqSC-3V_Khtkf6bIdg0/edit#slide=id.p)_

1. After starting a form and creating a question, go into Question Settings and
   in the Question Options tab, choose your HXL tag and add attributes.

    ![image](/images/hxl/hxl.gif)

2. After the form has been created, the project deployed, and data has been
   collected, go to the Downloads tab in the Data page. Select the export type
   as XLS and be sure to select **XML values and headers** for the value and
   header format. Then Export.

    ![image](/images/hxl/xml_values.gif)

3. Once you have exported and downloaded the data to your computer, open up the
   XLS file to see your HXL tags. It's okay to have Kobo metadata that doesn't
   have HXL hashtags.

    ![image](/images/hxl/xls_affected.jpg)

<p class="note">The hashtag before name is mandatory and spaces are not allowed.</p>

## How to use HXL in an XLSForm

When authoring an XLSForm, simply insert one extra column in any existing
spreadsheet and fill it with HXL hashtags identifying the type of information in
each column.

**survey sheet**

| type                 | name     | label                            | hxl        |
| :------------------- | :------- | :------------------------------- | :--------- |
| select_one countries | country  | Select affected country          | #country   |
| select_one admin1    | province | Please select the province       | #adm1+code |
| select_one admin2    | county   | Select the county                | #adm2+name |
| select_one sector    | cluster  | Cluster                          | #sector    |
| integer              | affected | Number of people affected        | #affected  |
| integer              | reached  | Number of people reached to date | #reached   |
| survey |
