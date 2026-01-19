# Mapping your GPS data

GPS questions in KoboToolbox allow you to collect precise geographic information as single points, or a collection of points representing a path or area during data collection. Each GPS record includes latitude, longitude, altitude, and accuracy, which you can view directly in the data table. KoboToolbox also provides a built-in <strong>Map view</strong> that helps users visualize single GPS points, explore patterns, and better understand where submissions were collected.

This article explains how to view and map GPS data in KoboToolbox and describes the available export formats for using geospatial data in other tools and workflows.

## Collecting GPS data in KoboToolbox

KoboToolbox allows you to collect three types of GPS data in your forms:

| Formbuilder question type | XLSForm question type | GPS data type                         |
|:--------------------------|:----------------------|:--------------------------------------|
| Point                     | `geopoint`            | A single point                        |
| Line                      | `geotrace`            | A path made up of multiple points     |
| Area                      | `geoshape`            | An area made up of multiple points    |

GPS data can be collected using both Enketo web forms and KoboCollect. All GPS responses appear in the data table and are included in data exports. Only single points, referred to as <strong>geopoints</strong> in the user interface, can be displayed in the KoboToolbox <strong>Map</strong> view.

<p class="note">
To learn more about collecting GPS data in your KoboToolbox forms, see <a href="https://support.kobotoolbox.org/collect_gps.html">Collecting GPS data</a>.
</p>

## Mapping GPS data in KoboToolbox

KoboToolbox includes a built-in <strong>Map</strong> view that displays GPS points collected through your form. Any user with <strong>View submissions</strong> [permission](https://support.kobotoolbox.org/managing_permissions.html) can access the map.

To open the map:

1. Open your project and go to the <strong>DATA</strong> page.
2. In the left menu, select <i class=""></i> <strong>Map</strong>
3. If your form includes at least one geopoint question, the collected locations appear on the map.

[A world map with orange geopoints in the United States, Canada, Columbia, Brasil, France, UK, Italy, Russia, Morocco, Nigera, Kenya, Pakistan](source/images/mapping_gps/map.png)

You can zoom in or out using the <i class=""></i>+ and <i class=""></i>− buttons in the top left corner of the map. To view the map in full screen, click <i class=""></i> <strong>Toggle fullscreen</strong> in the top right corner.

When multiple GPS points are close together, they appear as a single clustered point with a number indicating how many submissions are grouped there. Zoom in to view individual points.

<p class="note">
<strong>Note:</strong> Only geopoint questions are displayed on the map. Geotrace and geoshape data are not displayed.
</p>

### Selecting which question to view on the map

By default, the map displays data from the first geopoint question in your form. If your form includes multiple geopoint questions, you can choose which one to display.

To select a different question:

1. Click <i class=""></i> <strong>Map display settings</strong>.
2. Select a different geopoint question from the list.

[Map settings window for choosing geopoint question](source/images/mapping_gps/select.png) 

### Customizing the map

You can change how GPS data is displayed on the map using the available map controls.

To switch display types:

- Click <i class=""></i> <strong>Show as a heatmap</strong> in the top right corner to view data as a heatmap.
- Click <i class=""></i> <strong>Show as points</strong> to return to individual point markers.

<p class="note">
<strong>Note:</strong> A <strong>heatmap</strong> is a visualization that shows the concentration of submissions based on their geographic coordinates. Areas with more closely clustered data points appear more intense, while areas with fewer submissions appear lighter. Heatmaps help identify geographic patterns and hotspots without displaying individual points.
</p>

To change the base map layer:

- Click <i class=""></i> <strong>Toggle layers</strong> in the top right corner.
- Select a base layer, such as OpenStreetMap, OpenTopoMap, ESRI World Imagery, or Humanitarian. The default base layer is OpenStreetMap.

[The base layer of the world map](source/images/mapping_gps/base_layer.png)

You can also add additional custom layers on top of your map:
1. Open <i class=""></i> <strong>Map display settings</strong>.
2. Go to <strong>OVERLAYS</strong>.
3. Enter a label for the layer and upload a file in CSV, KML, KMZ, WKT, or GeoJSON format.

Uploaded files appear as optional layers that you can turn on or off from the map.

### Disaggregating points by survey responses

You can group GPS points on the map based on responses to other questions in your form. This helps you understand how different respondent groups are distributed geographically.

To disaggregate points:

1. Click <strong>Disaggregate by survey responses</strong> in the bottom left corner of the map.
2. Select the question you want to use to categorize the points. You can also change the display language.

[World map displaying disaggregated geopoint markers in shades of blue](source/images/mapping_gps/disaggregate.png)

To change the color set used for disaggregated points:

1. Open <i class=""></i> <strong>Map display settings</strong>.
2. Select <strong>MARKER COLORS</strong>.
3. Choose a different color set.

To remove disaggregation:

1. Click <strong>Disaggregated using: [question label]</strong>.
2. Select <strong>-- See all data --</strong> from the list.

## Exporting GPS data 

KoboToolbox provides several options for exporting GPS data. Each format supports different workflows, including data review, mapping, and geospatial analysis.

