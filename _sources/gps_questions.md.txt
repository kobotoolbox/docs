# GPS Question types
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/gps_questions.md" class="reference">31 Oct 2025</a>


In KoboToolbox, you can collect GPS coordinates as part of your data collection
form. There are 3 GPS question types you can use, namely "Point", "Line" and
"Area".

Use a "Point" question type when you want to record a single GPS coordinate.
This is perfect for questions where you need to show the location of a single
feature such as a house, or a borehole.

Use a "Line" question type when you want to record multiple GPS points to trace
a path. This question type can be used for collecting location data on features
such as roads, tracks and rivers.

The "Area" question type is used for collecting multiple GPS points that form
the boundaries of a feature. You can use it, for example, to trace the
boundaries of garden plots in a survey where you are enumerating land holdings.

## How to set up the "Point", "Line" and "Area" question types

### Setting up in formbuilder

Adding GPS questions on the form is simple:

- In the formbuilder, click the <i class="k-icon k-icon-plus"></i> button to add
  a new question
- Type the question text, for example "Capture the location of the housing
  unit", then click **ADD QUESTION** or press ENTER on your keyboard
- Choose the question type (e.g. Point)

![Adding GPS questions](images/gps_questions/adding_gps_questions.gif)

### Setting up in XLSForm

You can add "Point", "Line" and "Area" questions in XLSForm by using `geopoint`,
`geotrace` and `geoshape` question types respectively as in the following
example:

| type     | name   | label                                    |
| :------- | :----- | :--------------------------------------- |
| geopoint | point  | Capture the location of the housing unit |
| geotrace | road   | Trace out the road's route               |
| geoshape | garden | Trace the boundary of the garden         |
| survey   |

## Appearance of "Point", "Line" and "Area" question types in web forms and KoboCollect

### Default appearance

![Default appearances of GPS questions](images/gps_questions/gps_default_appearances.png)

## Collecting GPS points in the background

Besides including GPS questions in your form, you can also collect GPS
coordinates in the background while data is being collected. This is possible by
turning on the "Audit" option in the formbuilder (Layout & Settings -> Meta
questions) or by adding the `audit` meta question to your XLSForm. Learn more
about how to do this [here](audit_logging.md).

## Calculating distance and area with "Line" and "Area" question types

As you collect your GPS data, you might need to calculate the distance and area
from your "Line" and "Area" questions.

### Calculating distance from "Line" questions

To calculate the distance from a "Line" question type in the formbuilder, use
the "Calculate" question type and the
[`distance()`](https://docs.getodk.org/form-operators-functions/#distance)
function as shown below:

![Calculate distance](images/gps_questions/calculate_distance.png)

In the example above, the question "Trace the route of the track" has been added
as a "Line" question type. The "Data Column Name" in the question settings has
been set to "track".

The question with label `distance(${track})` is a "Calculate" question type with
a "Data Column Name" of "distance". The result will be in meters.

The "Note" question is optional and has been added with the purpose of
displaying the calculated distance within the form.

In XLSForm, you can do the same as follows:

| type      | name             | label                              | calculation        |
| :-------- | :--------------- | :--------------------------------- | :----------------- |
| geotrace  | track            | Trace the route of the track       |                    |
| calculate | distance         |                                    | distance(${track}) |
| note      | display_distance | The distance is ${distance} meters |                    |
| survey    |

### Calculating area from "Area" questions

You can calculate an area using the "Calculate" question type and the
[`area()`](https://docs.getodk.org/form-operators-functions/#area) function as
shown below:

![Calculate distance](images/gps_questions/calculate_area.png)

In the example above, the question "Trace the boundaries" has been added as an
"Area" question type. The "Data Column Name" in the question settings has been
set to "boundary".

The question with label `area(${boundary})` is a "Calculate" question type with
Data Column Name "area". The result will be in square meters.

The "Note" question is optional and has been added with the purpose of
displaying the calculated area within the form.

In XLSForm, you can do the same, as follows:

| type      | name         | label                             | calculation       |
| :-------- | :----------- | :-------------------------------- | :---------------- |
| geoshape  | boundary     | Trace the boundaries              |
| calculate | area         |                                   | area(${boundary}) |
| note      | display_area | The area is ${area} square meters |                   |
| survey    |

<p class="note">
  You can download an XLSForm with examples from this article
  <a
    download
    class="reference"
    href="./_static/files/gps_questions/gps_questions.xlsx"
    >here</a
  >.
</p>
