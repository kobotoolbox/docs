# Mapping, Sharing, and Exporting GPS Data
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/0050a936217ec4b5b9cf44a66826778898ed29d5/source/export_gps.md" class="reference">31 Oct 2025</a>


Your project may include a one or more GPS questions in its form. KoboToolbox
will include the GPS data (latitude, longitude, altitude, precision) in the
dataset that can be downloaded as XLS or CSV. It is also possible to view the
GPS coordinates on an online map and to download the points as a KML file for
use in other applications.

## Viewing your GPS points

![image](/images/export_gps/view_gps.jpg)

Both of the following options only appear if your form has any GPS questions and
has submissions with GPS coordinates.

**Option 1 - View GPS points online.**

Click on the button **View on Map**, which leads to the online map view. This
visualization also allows to see the submissions based on certain question
responses. When viewing your data on a map, you can also disaggregate by
question responses, such as displaying male and female respondents, or other
types of responses where a simple geographic distribution might be interesting.
A full list of current map features are below:

1. Settings: Upload data overlays and choose marker color schemes.
2. Toggle layers: Toggle through multiple map background options.
3. Toggle fullscreen
4. Show data as points (default)
5. Show data as heat map

**Option 2 - Download GPS points as KML.**

Click on the button **Download GPS Points**. This will start a new export
process with the latest data. Previous exports will be listed by their creation
date, allowing you do see snapshots of GPS coordinates at various points in
time. KML files can be imported in a variety of software, including Google
Earth, Google Maps, or professional GIS software, such as ArcMap.

![image](/images/export_gps/kml_exports.jpg)

Note: In case your form uses more than one GPS question, only the first one will
be used on the map.

**Option 3 - Export data as CSV and upload to GIS software.**

As an alternative to exporting your GPS data as a KML file, its possible and
easy to export and upload your data as a CSV file (which will include all
attributes) directly into GIS software as a shapefile. For a step-by-step guide,
refer to this [help article](upload_to_gis.md).

## How to share map data

You can share a map with others is to go into your Project's Settings and enable
Share Data. This means that anyone can view your data - i.e. in map, table, or
file download format. They won't be able to edit anything, which would require
giving Can Edit permissions to a particular user. After this you can send the
URL of the map (see above).
