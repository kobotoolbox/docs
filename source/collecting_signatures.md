# Signature Question Type

Some forms may require signatures to be included with them. You can use appearance `signature` on both Collect Android app and Enketo. The draw widget is only available when using Enketo for data collection.

## Collect Android app

Collect allows for a digital signature to be collected directly on the screen of the phone/tablet.

To add this to your form:
1. Open or download the XLS version of your form.
2. Create the question and set the type as `image`
3. Set the appearance to `signature`

## Enketo

Digital signatures also work on Enketo web forms, where you have the additional option to use a draw widget to collect signatures. In your XLSForm just add `signature` or `draw` under the `appearance` column for an `image`-type question.

__survey__

| type  | name      | label            | appearance | hint                             |
| ---   | ---       | ---              | ---        | ---                              |
| image | draw      | Draw widget      | draw       | Image type with draw appearance  |
| image | sign      | Signature widget | signature  | Image type with signature widget |

<br/>

[Follow this link](https://enke.to/draw) to test the difference between the draw and signature widgets.

## Create a Signature question type in the form-builder

1. Create a new question and select Photo as the question type.

![image](/images/collecting_signatures/new_question.jpg)

2. In the Settings under Question Options, click on the Appearance drop down and select Signature.

![image](/images/collecting_signatures/signature.jpg)
