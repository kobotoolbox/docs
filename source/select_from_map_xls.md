# Selecting options from a map

With **select_one** and **select_one_from_file** question types, you can configure your XLSForm to let users select a choice directly from a map instead of a list. When the map opens, it displays all available points, lines, or polygons based on the choices provided. Users can then tap a feature on the map to record their selection. This functionality is **available only in KoboCollect.**

This article explains how to configure your XLSForm to allow selecting options from a map, how to customize styling options such as colors, symbols, and line widths, and how choices are displayed and selected on the map.

<p class="note">
<strong>Note:</strong> The KoboToolbox Formbuilder does not support map-based selection for the <code>select_one</code> question type. To use this feature, configure it in an XLSForm and upload the form to KoboToolbox. 
  <br><br>
  To learn more about downloading and editing your form as XLSForm, see <a href="https://support.kobotoolbox.org/xlsform_with_kobotoolbox.html">Using XLSForm with KoboToolbox</a>.
</p>

## Setting up your XLSForm

To set up a **select from map** question in XLSForm:
1. In the `survey` worksheet, add a `select_one` or `select_one_from_file` question.
2. Add an `appearance` column. 
3. In the `appearance` column of the select question, enter **map** or **quick map.**
    - The **map** appearance allows respondents to click on different locations and view information about each before confirming their selection.
    - The **quick map** appearance automatically records the first selected location without displaying additional information.

**survey worksheet**

| type        | name     | label                       | appearance |
|:------------|:---------|:----------------------------|:-----------|
| select_one  | location | Where are you currently based? | map       |
| survey | 

4. In the `choices` worksheet or in your [external list of choices](https://support.kobotoolbox.org/select_from_file_xls.html), enter the choices as you normally would.
5. Next to your choice list, add a **geometry** column.
6. For each choice, enter the corresponding GPS coordinates in the **geometry** column.
    - This field can include unique or multiple GPS coordinates, to define a point, a line, or a polygon.

**choices worksheet**

| list_name | name | label  | geometry           |
|:----------|:-----|:-------|:------------------|
| cities    | 1    | Warsaw | 52.2297 21.0122 0 0 |
| cities    | 2    | Berlin | 52.5200 13.4050 0 0 |
| cities    | 3    | Paris  | 48.8566 2.3522 0 0  |
| cities    | 4    | Kyiv   | 50.4501 30.5234 0 0 |
| cities    | 5    | Prague | 50.0755 14.4378 0 0 |
| choices | 

### Format of GPS coordinates

When entering GPS coordinates in the `choices` worksheet or an external CSV or XML file, the following format must be used: `longitude latitude altitude accuracy`. 

- For example, the GPS coordinates for Paris would be `48.8566 2.3522 0 0`.

When providing multiple GPS coordinates (e.g., for a line or polygon), coordinates are separated by a semicolon. 
- For example, the GPS coordinates for a line going from Paris to Madrid would be `48.8566 2.3522 0 0;40.4637 -3.6556 0 0`.
- For a polygon, the GPS coordinates must start and end with the same coordinates.

<p class="note">
<strong>Note:</strong> To obtain your GPS coordinates in the correct format, you can use this <a href="https://ee.kobotoolbox.org/preview/7OmWg7pD">KoboToolbox form</a>. It lets you select points on a map and automatically generates the corresponding GPS coordinates in ODK format.
</p>

If you are using a GeoJSON file to provide GPS coordinates, follow the [GeoJSON format](https://docs.getodk.org/form-datasets/#selects-from-geojson) to specify the feature `geometry` .

<p class="note">
  For an example of map-based select questions, see this <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/SelectFromMap.xlsx">sample XLSForm</a>. External choice files for upload to KoboToolbox are available <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities1.csv">here</a> (CSV), <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities2.geojson">here</a> (GeoJSON), and <a href="https://support.kobotoolbox.org/_static/files/select_from_map_xls/cities3.xml">here</a> (XML). To learn more about using external choice files, see <a href="https://support.kobotoolbox.org/select_from_file_xls.html">Selecting options from an external file</a>.
</p>

## Adding choice properties

You can further customize your map by adding choice properties in the `choices` worksheet or external choice file.

Available choice properties include:

| Choice property | Description |
|:----------------|:------------|
| info            | Text description of the choice. |
| marker-color    | HEX color for the geopoint marker. |
| marker-symbol   | Single character, symbol, or emoji displayed on the geopoint marker. |
| stroke          | HEX color for the geotrace line or the geoshape polygon outline. |
| stroke-width    | Width of the geotrace line or the geoshape polygon outline (e.g., 5 or 6.5). |
| fill            | HEX color for the polygon interior. The fill color is displayed with fixed transparency. |

To add properties in the `choices` worksheet of your XLSForm:

1. Add a column with the appropriate property name (e.g., `info`, `stroke`, or `fill`).
2. For each choice, enter the corresponding value (e.g., a text description or a HEX code)

**choices worksheet**

| list_name | name | label  | geometry           | info                       |
|:----------|:-----|:-------|:------------------|:---------------------------|
| cities    | 1    | Warsaw | 52.2297 21.0122 0 0 | Capital of Poland          |
| cities    | 2    | Berlin | 52.5200 13.4050 0 0 | Capital of Germany         |
| cities    | 3    | Paris  | 48.8566 2.3522 0 0  | Capital of France          |
| cities    | 4    | Kyiv   | 50.4501 30.5234 0 0 | Capital of Ukraine         |
| cities    | 5    | Prague | 50.0755 14.4378 0 0 | Capital of Czech Republic  |
| choices | 

If you are using a GeoJSON file to provide GPS coordinates, follow the [GeoJSON format](https://docs.getodk.org/form-datasets/#selects-from-geojson) to specify feature `properties`.

## Map selection in KoboCollect

<iframe src="https://www.youtube.com/embed/C7o9rCKmCeo?si=h9y-meFvNwury_mI" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<p class="note">
<strong>Note:</strong> Selecting options from a map is <strong>only available in KoboCollect.</strong> In Enketo web forms, the option choices will appear as a normal list of options.
</p>

In KoboCollect, adding a **select type question** with a **map** or **quick map** appearance allows users to choose an option directly from a map rather than from a list. When the map opens, it centers on the device’s current location. Buttons on the right let users recenter on their location or show all available map points.

Point choices are shown as map markers. Tapping a marker increases its size.
Line and polygon choices are displayed as red outlines, with polygons shaded in red. Users can tap a line or polygon to select it. When a location is selected, its [properties](https://support.kobotoolbox.org/select_from_map_xls.html#adding-choice-properties) appear at the bottom of the screen, unless the **quick map** appearance is used. 

Under the choice label, a **Select** button appears to confirm and save the selected location to the form, unless the **quick map** appearance is used.

<p class="note">
<strong>Note:</strong> The <strong>map</strong> and <strong>quick map</strong> appearances can be combined with <a href="https://support.kobotoolbox.org/choice_filters_xls.html">choice filters</a> to display options on the map based on a previous selection.
</p>

