# Adding Another Language to your XLSForm

There are two methods to adding multiple languages to your form. You can either add and manage them directly through the online [Project Dashboard](language_dashboard.md) or you can add them in an XLS Form and upload it to KoBo.

Here are detailed instructions on how you can add another language to your form:

1. Create your form in the default language. This should be the language that the person responsible for designing the questionnaire is most comfortable with. When you are done, or when a significant portion of the form has been created, save it. You'll be returned to the draft form's project dashboard.

2. Export the form to XLS.

3. Open the file in Excel (Google Spreadsheet, Open Office Calc, etc will all work) (If you're in Excel it's possible you have to take the file out of Protected View first. [See here](https://support.office.com/en-us/article/what-is-protected-view-d6f09ac7-e6b9-4495-8e43-2bbcdbcb6653?ocmsassetID=HA010355931&CorrelationId=04b441d5-5c7c-441a-bbac-8f34b3071869&ui=en-US&rs=en-US&ad=US).) Your spreadsheet will have three sheets (see the little tabs at the bottom): survey, choices, settings. Stay in the survey sheet for now.

4. Find the column called 'label'. This is where your original question labels are stored. Insert another column to the right of label. In the header (first row) of this new column, write `label::language`, for example `label::Français`  or  `label::English`. Note: you can change the size of your columns, add colors or change the font size, none of these will affect your form.

5. Then, if you have hints in your form, the same needs to apply to that hint column, for example `hint::Français` or `hint::English`.

    ![image](/images/language_xls/hints.png)

6. Now add your translations for every row inside the `label::yourlanguage` column. When you are done, make sure you didn't skip any questions (for every field that has text inside the label column there should be text inside the `label::yourlanguage` column).

    Tip: Copy-paste the original label column and then make changes to the translations so you don't leave anything blank by accident: It's better to have something showing in the wrong language than not having a blank question in some language. _You can repeat this step and add as many languages as you like, each in their separate columns and with a different name inside `label::yourlanguage`._

    ![image](/images/language_xls/label.png)

7. Now switch to the 'choices' sheet of your file. (If there is no such sheet in your file -you only have two sheets called survey and settings- then don't worry - your form doesn't use any multiple choice questions -- you're done! Skip the next step.)

8. In the choices sheet you have another column called label. Repeat steps 5 and 6. Make sure that you use the exact same spelling for `label::yourlanguage`. For example, `label::Francais` and `label::Français` are not identical.

    ![image](/images/language_xls/choices_label.png)

9. In the settings sheet, underneath form_title edit the text of your form's title to something like "My form (English and French)" so you can easily identify it later.

    ![image](/images/language_xls/form_title.png)

10. Save your file and close Excel.

11. Return to KoBoToolbox and click on "Replace with XLS", then upload your updated XLS Form. Choose the file you just finished editing and click OK.

12. Open the form you just uploaded and click on Preview Form. At the top next to Choose Language click on the dropdown. It will have default (your original language) as well as the new language(s) you just added.

## Translating to Tamil, Nepali, Hindi, etc. scripts

When translating to non-Latin scripts, such as Tamil, Nepali, Hindi, etc, please make sure you do not use a so-called pseudo font. When writing in these languages make sure you only use the proper Unicode characters. To write proper Unicode characters you don't have to install any particular fonts. Instead, you (or your translator) need to set your keyboard to use the respective script (Tamil, Nepali, etc.) and then write normally. The correct keyboard setting will produce the actual script letters in Unicode instead of some Latin phonetic equivalents. (This would also be the same way as writing these languages into an email, KoBoToolbox, or any other Web application.

For help with adding the correct system keyboard, [check this link](https://support.microsoft.com/en-us/help/17424/windows-change-keyboard-layout) (Windows only).

Pseudo fonts allow writing in these scripts and are commonly used in many countries, particularly in South Asia. But while they work on the computer that has a specific font installed, they will not work on any other computer that doesn't use that particular font. That is because these fonts just disguise regular Latin characters and symbols and make them appear in a different shape. For example, when writing "Hello" with the Nepali pseudo font 'Preeti', it will look like this: हेल्लो. But what is really written there remains the letters H e l l o. For some people using these fonts which often use phonetic equivalents to English, may be easier. Another reason they are being used widely is that many computers used to not have support for these scripts and thus needed pseudo fonts as a "hack". Either way, Unicode characters are the best way to go - and the only way for use in KoBoToolbox.

## Translating right-to-left scripts

When adding a language that uses right-to-left script it is important to use the correct language code, however even if the correct code is used, if the first question, hint, or note is written in a left-to-right script the form will automatically format the rest of the translation to a left-to-right format.
