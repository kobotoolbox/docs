# Importing an XLSForm via URL
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/050dcc9c8bfb4c528208bbe886979999037f1554/source/xls_url.md" class="reference">28 Oct 2025</a>

## Google Sheets

To get the correct link for a Google Sheets spreadsheet, follow these steps:

1. Click on **File > Publish** to the Web.

2. Under the **Web Page** dropdown, select **Microsoft Excel (.xlsx)**. Keep **Entire Document** selected in the preceding dropdown.

3. Copy the link from the resulting field.

    ![image](/images/xls_url/link.jpg)

**Note for advanced users:** in our tests, the "Automatically republish when changes are made" checkbox doesn't always work well. You may need to stop publishing and republish the spreadsheet to get an updated link.

## Dropbox

To get the correct link for a spreadsheet in Dropbox, follow these steps:

1. Make sure the XLSForm file is in a public Dropbox folder in your account.

2. Copy its link. It should end with the suffix `?dl=0`. Replace the 0 with 1, so that your link ends in `?dl=1`.
