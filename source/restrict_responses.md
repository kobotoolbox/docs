# Restricting Text Responses With Regular Expressions

A regular expression, or regex, is a search pattern used for matching specific characters and ranges of characters within a string. It is widely used to validate, search, extract, and restrict text in most programming languages. KoBoToolbox supports regex to control the length and character(s) during data entry to a particular question _(e.g. controlling the entry of mobile number to exactly 10 digits, controlling the entry of a valid email id etc.)_. 

#### To use a regex in KoboToolbox, follow these steps

1. Prepare a _Text_ question type.

2. Go to the question's _Settings_.

3. Go to _Validation Criteria_ and choose the _Manually enter your validation logic in XLSForm_ code option.

4. In the _Validation Code_ box, enter your regex formula between the quotation marks **(' ')** of the **regex(., ' ')** format. For reference, the period _(.)_ refers to _'this question'_, while the regular expression inside the quotation marks **(' ')** needs to conform to the established regex rules. 

5. (Optional) Add a custom _Error Message_ for the person entering data to see when they don't meet the regrex criteria. 

    ![image](/images/restrict_responses/regrex.jpg)  
    
Regex can also be coded in XLSForm by typing the regex code under the _constraint_ column. 
    
    ![image](/images/restrict_responses/xls_constraint.png)  
    
Alternatively, there is another way of using regex in KoBoToolbox i.e. by creating a calculate question type and then defining the regex code under the _calculation_ column. You could then use this variable as many times as needed in the survey form. 
    
    ![image](/images/restrict_responses/xls_calculation.png) 
    
#### How do I build the regex that I need?

In addition to the examples and tips provided below, please visit [this website](http://www.regexr.com) for more help and examples.

* Regex in KoBoToolbox should always be written in-between the apostrophes **regex(., ' ')** as shown in the examples. 
* **^**: The caret symbol _(^)_ matches the start of a string without consuming any character.
* **$**: The dollar symbol _($)_ matches the end of a string without consuming any character.
* **[abc]**: Matches either _a_, _b_ or _c_ from within the _[ ]_. 
* **[a-z]**: Matches any lowercase character from _a_ to _z_.
* **[A-Z]**: Matches any uppercase character from _A_ to _Z_.
* **[0-9]**: Matches any numbers from _0_ to _9_.
* **[a-zA-Z0-9]**: Matches any character from _a_ to _z_ or _A_ to _Z_ or _0_ to _9_. You could combine anything required.
* **[^abc]**: Matches any character except _a_, _b_ or _c_ if the caret symbol _(^)_ is used inside _[ ]_. 
* **[^A-Z]**: Matches any characters except those in the range _A_ to _Z_ if the caret symbol _(^)_ is used inside _[ ]_. 
* **(apple)**: The grouping character _( )_ matches anything that is within the parenthesis. Here, _(apple)_ matches the characters apple literally (case sensitive).
* **|**: A vertical bar also known as _Boolean_ matches any element separated by the vertical bar. 
* **\**: A back slash is used to match the literal value of any metacharacter (e.g. try using _\._ or _\@_ or _\$_ while building regex).
* **\number**: Matches the same character as most recently matched by the n<sup>th</sup> (number used) capturing group.
* **\s**: Matches any space or tab.
* **\b**: Matches, without consuming any characters immediately between a character matched by _\w_ and a character not matched by _\w_ (in either order). _\b_ is also known as the word boundary.
* **\d**: Matches any equivalent numbers _(0 to 9)_.
* **\D**: Matches anything other than numbers _(0 to 9)_.
* **\w**: Matches any word character (i.e. _a_ to _z_ or _A_ to _Z_ or _0_ to _9_ or _). 
* **\W**: Matches anything other than what _\w_ matches (i.e. it matches wild cards and spaces).
* **?**: A question mark _(?)_ used just behind a character matches or skips (if not required) a character match. 
* __*__: An asterisk symbol _*_ used just behind a character matches zero or more consecutive character. 
* **+**: The plus symbol _(+)_ used just behind a character matches one or more consecutive character.
* **{x}**: Matches exactly _'x'_ consecutive characters. 
* **{x,}**: Matches at least _'x'_ consecutive characters (or more).
* **{x,y}**: Matches between _'x'_ and _'y'_ consecutive characters.

#### Examples related to use of numbers

_For all text questions that use numbers, do not forget to type **numbers** under the appearance column._

* Restrict mobile number to ten digits : **regex(., '^[0-9]{10}$')** or **regex(., '^\d{10}$')**
* Restrict an input to _1234.56.78_ format: **regex(., '^[0-9]{4}.[0-9]{2}.[0-9]{2}$')** or **regex(., '^\d{4}\.\d{2}\.\d{2}$')**
* Restrict an input between _01_ to _99_ digits where input format of a single number (like 1 or 2) is not allowed: **regex(., '^[01-99]{2}$')** and **(. >= 01)**
* Restrict an input to only two numbers i.e. either to _12_ or _345_: **regex(., '^(12|345)$')**
* Restrict an input of nine digits where the first number can't be _0_: **regex(., '^1-9][0-9]{8}$')** or **regex(., '^[^0$]')**
* Restrict an input to one digit in between _0_ to _9_: **regex(., '^\d$')**
* Restrict an input to five digits in between _0_ to _9_: **regex(., '^\d{5}$')**
* Restrict an input to two digits and three decimals (e.g. _12.345_): **regex(., '\d{2}\.\d{3}$')**
* Restrict an input to two digits and three decimals (while the decimals are optional) (e.g. _12_ or _12.345_): **regex(., '^\d{2}(\.\d{3})?$')**

#### Examples related to use of alphabets letters

* Restrict an input of any characters (_up to 6 characters long_) consisting lowercase letters: **regex(., '^[a-z]{1,6}$')**
* Restrict an input of any characters (_up to 10 characters long_) consisting uppercase letters: **regex(., '^[A-Z]{1,10}$')**
* Restrict an input to only one of the three fruits outlined i.e. either to _Apple_ or _Orange_ or _Banana_: **regex(., '^(Apple|Orange|Banana)$')**
* Restrict an input to only two words i.e. _pear_ or _pair_: **regex(., '^p(ea|ai)r$')**
* Restrict an input to only two words i.e. _sun_ or _son_: **regex(., '^s[ou]n$')**
* Restrict an input with a valid email address: **regex(., '^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+[.][A-Za-z]{2,}$')**
* Restrict an input of the beneficiaries name where the initials of the first name and last name are uppercase e.g. _Kobe Bryant_: **regex(., '^[A-Z]{1}[a-z]{1,}[ ]{1}[A-Z]{1}[a-z]{1,}$')**
* Restrict an input of the beneficiaries name with first name, middle name (if any) and last name e.g. _Kobe Bean Bryant_: **regex(., '^\w{1,}\s(\w{1,})?(\s)?\w{1,}$')**
* Restrict an input of the beneficiaries' full name where the initials of the names are in uppercase and the name are quite long (often greater than 3 words) e.g. _Samayamantri Venkata Rama Naga Butchi Anjaneya Satya Krishna Vijay_ (this is an example of south Indian names): **regex(., '^([A-Z]{1}[a-z]{1,}\s)([A-Z]{1}[a-z]{1,}\s?)+$')**
* Restrict an input of the beneficiaries' first name (so that you are able to capture the exact spelling) where the enumerators are forced to enter the beneficiaries first name twice e.g. _Kobe Bryant Kobe_. (This could be helpful when you are trying to document beneficiaries details where a typo error could cost you heavy): **regex(., '^(\D+)\s(\D+)\s?\1$')**
* Restrict an input of the beneficiaries' last name (so that you are able to capture the exact spelling) where the enumerators are forced to enter the beneficiaries last name twice e.g. _Kobe Bryant Bryant_. _(This could be helpful when you are trying to document beneficiaries details where a typo error could cost you heavy)_: **regex(., '^(\D+)\s(\D+)\s?\2$')**
* Restrict a character within a word by using the _?_ (quantifier) e.g. allow either _color_ or _colour_ as an input: **regex(., '^colou?r$')**
* Restrict a character within a word by using the _*_ (quantifier) e.g. allow either _a!_ or _ah!_ or _ahh!_ or _ahhh!_ and so on as an input: __regex(., '^ah*!$')__
* Restrict a character within a word by using the _+_ (quantifier) e.g. allow either _ah!_ or _ahh!_ or _ahhh!_ and so on as an input: **regex(., '^ah+!$')**
* Restrict an input to a non-digit character (e.g. _a_ or _c_ or _!_ or _#_ or _%_ etc.): **regex(., '^\D$')**
* Restrict an input to five non-digit character (e.g. _aZcB!#%_ etc.): **regex(., '^\D{5 }$')**

#### Examples related to use of a combination of alphabets letters and numbers

* Restrict one character which matches between _a_ to _z_ or _A_ to _Z_ or _0_ to _9_ or _ (i.e. match one character from _[a-zA-Z0-9_]_): **regex(., '^\w$')**
* Restrict three character which matches between a to z or A to Z or 0 to 9 or _ (i.e. match one character from _[a-zA-Z0-9_]_): **regex(., '^\w{3}$')**
* Restrict your beneficiary ID to a specific format e.g. _CAR_PRC_2020_0048_: **regex(., '^[A-Z]{3}[_][A-Z]{3}[_][0-9]{4}[_][0-9]{4}$')**
* Restrict your beneficiary ID to a specific format e.g. _CAR-PRC-2020-0048_ (_where the enumerators should enter an exact match from _CAR_ to - i.e. _CAR-PRC-2020-_ and can enter any 4 digit serial number): **regex(., '^CAR-PRC-2020-[0-9]{4}$')**
* Restrict a currency input of three digits with a currency sign (either dollar or pound) in front (e.g. _$999_ or _£500_): **regex(., '^[\$|\£]\d{3}$')**
* Restrict an exact input of number of words (e.g. to restrict exactly 3 words "_I love you._"): __regex(., '^\W*(\w+\b\W*){3}$')__
* Restrict an input of number of words (e.g. to restrict a range of words say 3 to 5): __regex(., '^\W*(\w+\b\W*){3,5}$')__

#### Considerations when using regex

* If you wish to use a regex constraint on a number, make sure you **ALWAYS** type **numbers** under the **appearance**. This restricts the display of alphabets, making only numbers visible for inputs.

* Be careful, with the mode of data collection (i.e. KoBoCollect android app or Enketo web forms) you wish, once you have completed designing and deploying your survey forms (using regex). This is because, KoBoCollect android app and Enketo web forms behaves a bit differently with regex. KoBoCollect android app behaves as if you have used the anchors (^ $) around the regex (even if you have not used them), while Enketo requires the anchors as mandatory for an exact match.
