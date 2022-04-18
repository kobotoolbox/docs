# Limiting Responses with Validation Criteria

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/f9bb069f3517cb6d0b581aa7cec180b5ff707d2b/source/validation_criteria.md" class="reference">12
Aug 2021</a>

This feature allows you to avoid accidental or invalid answers, especially in
numeric questions (`integer` or `decimal` response types). However, validation
can be used on any question. Validation criteria are also sometimes referred to
as constraints.

For example, if you want to restrict a question about age to numbers between 0
and 130.

## Add validation criteria in Formbuilder

To add validation criteria for a specific question, go to **Settings**, then
**Validation Criteria**.

![image](/images/validation_criteria/formbuilder.gif)

You can directly add a condition or manually enter validation logic in XLSFrom
code. The type of restrictions under "**Add a condition**" corresponds to the
type of the questions (123 - numbers, text, date) selected. As seen from the
example above, the question type is number and the validation criteria restricts
the response to be greater than 3 and less than or equal to 30. The **Error
Message** (optional) is the message your interviewer sees when they enter an
invalid response.

## Add validation criteria in XLSForm

Validation criteria in XLSForm needs to be entered in specific syntax.

## Example Validation Criteria

| Criteria             | Description                                  |
| :------------------- | :------------------------------------------- |
| `. > 17`             | Response must be greater than 17             |
| `. >= 18`            | Response must be greater than or equal to 18 |
| `. > 17 and . < 130` | Response must be between 17 and 130          |

In the validation criteria syntax,`.` refers to the current question.
`${some_question}` refers to the fixed `name` of a question, which needs to be
set in the **Question Options** and then surrounded by `${}`. See below example:

**survey**

| type    | name | label                          | constraint        | constraint_message                                                            |
| :------ | :--- | :----------------------------- | :---------------- | :---------------------------------------------------------------------------- |
| integer | Q1   | Please enter your work ID      | . > 0 and . < 100 | ID cannot be 0 and must be less than 100                                      |
| integer | Q2   | Total number of workers        |                   |                                                                               |
| integer | Q3   | Total number of male workers   | . <= ${Q2}        | Total number of male workers should not exceed the total number of workers!   |
| integer | Q4   | Total number of female workers | . <= ${Q2}        | Total number of female workers should not exceed the total number of workers! |

**Examples of More Advanced Validation Criteria**

| Criteria                                                                      | Description                                                                                             |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| `(. >= 18 and . < 130) or (. = 999)`                                          | Response must be between 17 and 130 or be equal to 999. (The code 999 is often used for non-responses.) |
| `not(${in_university} = 'yes' and . < 16)`                                    | When answering 'yes' to the question `in_university`, the current response must be greater than 16.     |
| `not(selected(., 'none') and (selected(., 'chair') or selected(., 'table')))` | Response 'none' can't be combined with the two other options of this `select_multiple` question         |

There are many other combinations possible, including
[advanced mathematical calculations](advanced_calculate.md).
[See here](https://docs.getodk.org/form-logic/) for more details.
