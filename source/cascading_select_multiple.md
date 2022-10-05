# Cascading a Select Multiple Question

There could be times when you wish to cascade a question for a survey project.
Cascading a select one question is possible through the Formbuilder as outlined
in the support article
**[Adding Cascading Select Questions](cascading_select.md)**. However, if you
wish to cascade a select multiple question, it is still not possible through the
Formbuilder. This article illustrates how to cascade a select multiple question
through the XLSForm.

## Designing your survey tab:

The first sheet required in your XLSForm is the _survey_ tab. This sheet will
require six column headers (_type_, _name_, _label_, _required_,
_choice_filter_, _calculation_).

| type               | name | label                               | required | choice_filter                                                      | calculation                                                                                  |
| ------------------ | ---- | ----------------------------------- | -------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| select_multiple Q1 | Q1   | Q1. Select all that applies from Q1 | TRUE     |                                                                    |                                                                                              |
| calculate          | C1   |                                     |          |                                                                    | if(selected(${Q1}, '1'),'condition1','')                                                     |
| calculate          | C2   |                                     |          |                                                                    | if(selected(${Q1}, '2'),'condition2','')                                                     |
| calculate          | C3   |                                     |          |                                                                    | if(selected(${Q1}, '3'),'condition3','')                                                     |
| calculate          | C4   |                                     |          |                                                                    | if((selected(${Q1}, '1') and selected(${Q1}, '2') and selected(${Q1}, '3')),'condition4','') |
| select_multiple Q2 | Q2   | Q2. Select all that applies from Q2 | TRUE     | filter1=${C1} or filter2=${C2} or filter3=${C3} or   filter4=${C4} |                                                                                              |
| survey             |      |                                     |          |                                                                    |                                                                                              |

Here _row 2 and row 7_, are _select multiple_ questions where we will be
cascading the choices of Q2 (_row 7_) based on the choices selected in Q1 (_row
2_). _Row 3 to 6_ are _calculate_ questions that hold the _if function_ to
create cascading conditions for (_row 7_). The _choice_filter_ used in _row 7_
then finally cascades the choices of Q2.

## Designing your choices tab:

The second sheet your XLSForm requires is the _choices_ tab. This sheet will
require three mandatory column headers (_list_name_, _name_, _label_) and
additional column headers (_filter1_, _filter2_, _filter3_, _filter4_) that hold
the choices based on the conditions created in the _survey_ tab using the _if
function_. You could give any suitable names for these additional column headers
(_filter1_, _filter2_, _filter3_, _filter4_) if you wish to, apart from what has
already been used here.

| list_name | name | label           | filter1    | filter2    | filter3    | filter4    |
| --------- | ---- | --------------- | ---------- | ---------- | ---------- | ---------- |
| Q1        | 1    | Choice 1 for Q1 |            |            |            |            |
| Q1        | 2    | Choice 2 for Q1 |            |            |            |            |
| Q1        | 3    | Choice 3 for Q1 |            |            |            |            |
| Q2        | 1    | Choice 1 for Q2 | condition1 |            |            | condition4 |
| Q2        | 2    | Choice 2 for Q2 | condition1 |            |            | condition4 |
| Q2        | 3    | Choice 3 for Q2 |            | condition2 |            | condition4 |
| Q2        | 4    | Choice 4 for Q2 |            | condition2 |            | condition4 |
| Q2        | 5    | Choice 5 for Q2 |            |            | condition3 | condition4 |
| Q2        | 6    | Choice 6 for Q2 |            |            | condition3 | condition4 |
| choices   |      |                 |            |            |            |            |

## Designing your settings tab:

The third sheet your XLSForm requires is the _settings_ tab. This sheet will
require one optional column header (_form_title_).

| form_title                           |
| ------------------------------------ |
| Cascading a Select Multiple Question |
| settings                             |

## Data entry screen as seen in Enketo:

_This is the screen you should see when nothing is selected in Q1._

![No choices selected](/images/cascading_select_multiple/enketo_nothing.png)

_This is the screen you should see when only one choice is selected in Q1._

![One choice selected](/images/cascading_select_multiple/enketo_one.png)

_This is the screen you should see when two choices are selected in Q1._

![Two choices selected](/images/cascading_select_multiple/enketo_two.png)

_This is the screen you should see when all three choices are selected in Q1._

![Three choices selected](/images/cascading_select_multiple/enketo_three.png)

<p class="note"> You can access the XLSForm <a download href="./_static/files/cascading_select_multiple/Cascading_Select_Multiple_Question.xlsx"><b>here</b></a> that was used in this article.</p>
