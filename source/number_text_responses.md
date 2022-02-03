# Limits on Number and Text Responses
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0c5dd6987a26369bd16e779f6ee2ad77e2243b26/source/number_text_responses.md" class="reference">21 Jun 2020</a>

There are underlying technical constraints to the length of the response in a **Number** or **Text** question.
 
**Number questions** can save up to 17 digits (positive or negative number). To be exact, the largest number that can be entered is 2147483647 and the smallest -2147483648.
 
If you want a numeric response but need a number with more than 9 digits (i.e. larger than the one given above) - e.g. for long phone numbers in some countries - you can do this with a trick. Instead of a Number question, add a Text question to your form. Then in the Appearance setting of the question, set it to numbers. This will show the number keyboard instead of the standard text keyboard. 

**Text questions** (as well as Barcode questions) are almost unlimited in terms of the characters that can be entered. (The total length of text needs to be less than 1MB in size, which is more than 300 pages of text - more than can ever be expected in a response to a question.
