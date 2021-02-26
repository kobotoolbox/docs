# Restricting Text Responses With Regular Expressions

A regular expression, or regex, is a search pattern used for matching specific characters and ranges of characters within a string. It is widely used to validate, search, extract, and restrict text in most programming languages. KoBoToolbox supports regex to control the length and character(s) during data entry to a particular question _(e.g. controlling the entry of mobile number to exactly 10 digits, controlling the entry of a valid email id etc.)_. 

#### To use a regex in KoboToolbox, follow these steps

1. Prepare a _Text_ question type.

2. Go to the question's _Settings_.

3. Go to _Validation Criteria_ and choose the _Manually enter your validation logic in XLSForm_ code option.

4. In the _Validation Code_ box, enter your regex formula between the quotation marks `(' ')` of the `regex(., ' ')` format. For reference, the period `(.)` refers to _'this question'_, while the regular expression inside the quotation marks `(' ')` needs to conform to the established regex rules. 

5. (Optional) Add a custom _Error Message_ for the person entering data to see when they don't meet the regrex criteria. 

    ![image](/images/restrict_responses/regrex.jpg)  
    
Regex can also be coded in XLSForm by typing the regex code under the _constraint_ column. 
    
    ![image](/images/restrict_responses/xls_constraint.png)  
    
Alternatively, there is another way of using regex in KoBoToolbox i.e. by creating a calculate question type and then defining the regex code under the _calculation_ column. You could then use this variable as many times as needed in the survey form. 
    
    ![image](/images/restrict_responses/xls_calculation.png) 
    
#### How do I build the regex that I need?

In addition to the examples and tips provided below, please visit [this website](http://www.regexr.com) for more help and examples.

* Regex in KoBoToolbox should always be written in-between the apostrophes `regex(., ' ')` as shown in the examples. 
* **^**: The caret symbol `(^)` matches the start of a string without consuming any character.
* **$**: The dollar symbol `($)` matches the end of a string without consuming any character.
* **[abc]**: Matches either `a`, `b` or `c` from within the `[ ]`. 
* **[a-z]**: Matches any lowercase character from `a` to `z`.
* **[A-Z]**: Matches any uppercase character from `A` to `Z`.
* **[0-9]**: Matches any numbers from `0` to `9`.
* **[a-zA-Z0-9]**: Matches any character from `a` to `z` or `A` to `Z` or `0` to `9`. You could combine anything required.
* **[^abc]**: Matches any character except `a`, `b` or `c` if the caret symbol `(^)` is used inside `[ ]`. 
* **[^A-Z]**: Matches any characters except those in the range `A` to `Z` if the caret symbol `(^)` is used inside `[ ]`. 
* **(apple)**: The grouping character `( )` matches anything that is within the parenthesis. Here, `(apple)` matches the characters apple literally (case sensitive).
* **|**: A vertical bar also known as _Boolean_ matches any element separated by the vertical bar. 
* **\\**: A back slash is used to match the literal value of any metacharacter (e.g. try using `\.` or `\@` or `\$` while building regex).
* **\number**: Matches the same character as most recently matched by the n<sup>th</sup> (number used) capturing group.
* **\s**: Matches any _space_ or _tab_.
* **\b**: Matches, without consuming any characters immediately between a character matched by `\w` and a character not matched by `\w` (in either order). `\b` is also known as the _word boundary_.
* **\d**: Matches any equivalent numbers `(0 to 9)`.
* **\D**: Matches anything other than numbers `(0 to 9)`.
* **\w**: Matches any word character (i.e. `a` to `z` or `A` to `Z` or `0` to `9` or `_`). 
* **\W**: Matches anything other than what `\w` matches (i.e. it matches wild cards and spaces).
* **?**: A question mark `(?)` used just behind a character matches or skips (if not required) a character match. 
* __*__: An asterisk symbol `*` used just behind a character matches zero or more consecutive character. 
* **+**: The plus symbol `(+)` used just behind a character matches one or more consecutive character.
* **{x}**: Matches exactly `x` consecutive characters. 
* **{x,}**: Matches at least `x` consecutive characters (or more).
* **{x,y}**: Matches between `x` and `y` consecutive characters.

#### Examples related to use of numbers

_For all text questions that use numbers, do not forget to type **numbers** under the appearance column._

* Restrict mobile number to _ten digits_: `regex(., '^[0-9]{10}$')` or `regex(., '^\d{10}$')`
* Restrict an input to `1234.56.78` format: `regex(., '^[0-9]{4}.[0-9]{2}.[0-9]{2}$')` or `regex(., '^\d{4}\.\d{2}\.\d{2}$')`
* Restrict an input between `01` to `99` digits where input format of a _single number_ (like 1 or 2) is not allowed: `regex(., '^[01-99]{2}$') and (. >= 01)`
* Restrict an input to only _two numbers_ i.e. either to `12` or `345`: `regex(., '^(12|345)$')`
* Restrict an input of _nine digits_ where the first number can't be `0`: `regex(., '^1-9][0-9]{8}$')` or `regex(., '^[^0$]')`
* Restrict an input to _one digit_ in between `0` to `9`: `regex(., '^\d$')`
* Restrict an input to _five digits_ in between `0` to `9`: `regex(., '^\d{5}$')`
* Restrict an input to _two digits and three decimals_ (e.g. `12.345`): `regex(., '\d{2}\.\d{3}$')`
* Restrict an input to _two digits and three decimals_ (while the decimals are optional) (e.g. `12` or `12.345`): `regex(., '^\d{2}(\.\d{3})?$')`

#### Examples related to use of alphabets letters

* Restrict an input of any characters (_up to 6 characters long_) consisting _lowercase letters_: `regex(., '^[a-z]{1,6}$')`
* Restrict an input of any characters (_up to 10 characters long_) consisting _uppercase letters_: `regex(., '^[A-Z]{1,10}$')`
* Restrict an input to only _one of the three fruits_ outlined i.e. either to `Apple` or `Orange` or `Banana`: `regex(., '^(Apple|Orange|Banana)$')`
* Restrict an input to only _two words_ i.e. `pear` or `pair`: `regex(., '^p(ea|ai)r$')`
* Restrict an input to only _two words_ i.e. `sun` or `son`: `regex(., '^s[ou]n$')`
* Restrict an input with a _valid email address_: `regex(., '^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+[.][A-Za-z]{2,}$')`
* Restrict an input of the beneficiaries name where the _initials of the first name and last name are uppercase_ e.g. `Kobe Bryant`: `regex(., '^[A-Z]{1}[a-z]{1,}[ ]{1}[A-Z]{1}[a-z]{1,}$')`
* Restrict an input of the beneficiaries name with _first name, middle name (if any) and last name_ e.g. `Kobe Bean Bryant`: `regex(., '^\w{1,}\s(\w{1,})?(\s)?\w{1,}$')`
* Restrict an input of the beneficiaries' full name where the _initials of the names are in uppercase_ and the name are quite long (often greater than 3 words) e.g. `Samayamantri Venkata Rama Naga Butchi Anjaneya Satya Krishna Vijay` (this is an example of south Indian names): `regex(., '^([A-Z]{1}[a-z]{1,}\s)([A-Z]{1}[a-z]{1,}\s?)+$')`
* Restrict an input of the beneficiaries' first name (so that you are able to capture the exact spelling) where the _enumerators are forced to enter the beneficiaries first name twice_ e.g. `Kobe Bryant Kobe`. (This could be helpful when you are trying to document beneficiaries details where a typo error could cost you heavy): `regex(., '^(\D+)\s(\D+)\s?\1$')`
* Restrict an input of the beneficiaries' last name (so that you are able to capture the exact spelling) where the _enumerators are forced to enter the beneficiaries last name twice_ e.g. `Kobe Bryant Bryant`. _(This could be helpful when you are trying to document beneficiaries details where a typo error could cost you heavy)_: `regex(., '^(\D+)\s(\D+)\s?\2$')`
* Restrict a character within a word by using the `?` (quantifier) e.g. allow either `color` or `colour` as an input: `regex(., '^colou?r$')`
* Restrict a character within a word by using the `*` (quantifier) e.g. allow either `a!` or `ah!` or `ahh!` or `ahhh!` and so on as an input: `regex(., '^ah*!$')`
* Restrict a character within a word by using the `+` (quantifier) e.g. allow either `ah!` or `ahh!` or `ahhh!` and so on as an input: `regex(., '^ah+!$')`
* Restrict an input to a _non-digit character_ (e.g. `a` or `c` or `!` or `#` or `%` etc.): `regex(., '^\D$')`
* Restrict an input to _five non-digit character_ (e.g. `aZcB!#%` etc.): `regex(., '^\D{5 }$')`

#### Examples related to use of a combination of alphabets letters and numbers

* Restrict one character which matches between `a` to `z` or `A` to `Z` or `0` to `9` or `_` (i.e. match one character from `[a-zA-Z0-9_]`): `regex(., '^\w$')`
* Restrict three character which matches between `a` to `z` or `A` to `Z` or `0` to `9` or `_` (i.e. match one character from `[a-zA-Z0-9_]`): `regex(., '^\w{3}$')`
* Restrict your beneficiary ID to a specific format e.g. `CAR_PRC_2020_0048`: `regex(., '^[A-Z]{3}[_][A-Z]{3}[_][0-9]{4}[_][0-9]{4}$')`
* Restrict your beneficiary ID to a specific format e.g. `CAR-PRC-2020-0048` (_where the enumerators should enter an exact match from `CAR` to `-` i.e. `CAR-PRC-2020-` and can enter any 4 digit serial number_): `regex(., '^CAR-PRC-2020-[0-9]{4}$')`
* Restrict a currency input of _three digits_ with a currency sign (either `dollar` or `pound`) in front (e.g. `$999` or `£500`): `regex(., '^[\$|\£]\d{3}$')`
* Restrict an exact input of number of words (e.g. to restrict exactly 3 words `I love you.`): `regex(., '^\W*(\w+\b\W*){3}$')`
* Restrict an input of number of words (e.g. to restrict a range of words say `3` to `5`): `regex(., '^\W*(\w+\b\W*){3,5}$')`

#### Considerations when using regex

* If you wish to use a regex constraint on a number, make sure you **ALWAYS** type **numbers** under the **appearance**. This restricts the display of alphabets, making only numbers visible for inputs.

* Be careful, with the mode of data collection (i.e. KoBoCollect android app or Enketo web forms) you wish, once you have completed designing and deploying your survey forms (using regex). This is because, KoBoCollect android app and Enketo web forms behaves a bit differently with regex. KoBoCollect android app behaves as if you have used the anchors `(^ $)` around the regex (even if you have not used them), while Enketo requires the anchors as mandatory for an exact match.
