Collecting GPS Locations
========================

Location coordinates can be collected easily in all forms with the 'GPS' response types. 

**Creating the Different Types of GPS Questions**

To collect a GPS coordinate during the data collection process simply add a GPS question to your form. There are three types of GPS questions: **Point**, **Line** and **Area** 

- When using the **form builder** these question types can be found when one taps the add question button as illustrated below.

.. image:: /images/collect_gps/form_builder.jpg

- When using **XLSForm** design, you have to define the question types as below to get the question you desire.

.. image:: /images/collect_gps/xls.png

**Collecting Data Using the GPS Questions**

During data entry the enumerator will see different options for collecting the coordinates, which are dependent on the type of data collection device and approach.

**Collecting Data Using Enketo Webforms**

The form will have various collection options including 

**1. Manual Collection:** Simply tap any point(s) on the map to collect the location coordinates or you may type in the latitude and longitude coordinates if they're known. 

.. image:: /images/collect_gps/point_manual.png

**2. Pasting KML points:** Paste KML coordinates on the text box prompt that comes up. 

.. image:: /images/collect_gps/kml.png

**3. Detect Current Location:** Simply click the button shown below to collect the current GPS coordinates for the location of the device.

.. image:: /images/collect_gps/current_location.jpg

**Collecting Data Using KoBoCollect**

The interviewer will see various options depending on the GPS question type

**1. Single GPS point coordinate** 

- *The enumerator will see this screen which they can tap on the Start GeoPoint.*

.. image:: /images/collect_gps/geopoint.jpg

- *If enumerators taps the Start Geopoint they will see the location loading and the accuracy achieved. If the question had not been set to pick a specific accuracy level, it will wait for the enumerator to save the GeoPoint as illustrated below.*

.. image:: /images/collect_gps/autopoint.jpg

**2. GPS Line**

- *The enumerators will see the following option for the line question*

.. image:: /images/collect_gps/line.jpg

- *If they tap the Start GeoTrace button they will see an option to either collect the trace manually or automatically as shown below*

.. image:: /images/collect_gps/trace_mode.jpg

- *If the enumerators select manual mode for collecting data then they will be able to select the points manually by pressing the points on the map. The enumerator will have to select at least two coordinates to make a line trace.*

- *If the enumerators select the automatic mode, then they will see an option for how long the system should take before collecting different points as shown in the figure below.*

.. image:: /images/collect_gps/automodes.jpg

**3. GPS Area**

*The GPS area allows you to manually collect GPS area based on manual mode by pressing the map to select the points that create the polygon; the enumerators would need to collect at least three points to create a polygon.*

**Accuracy of the Collected GPS Coordinates**

The accuracy of the collected GPS is dependent on various factors

**Absence of GPS sensor or GPS disabled**

When collecting GPS coordinate and their device doesn't have a GPS sensor or GPS is disabled, a location might be determined using other means, which might not be as accurate. Location services are controlled by the device, and not all devices are equipped with a GPS sensor. GPS may also be turned off, or the device may be set to use WiFi and cellular networks to establish a location rather than using satellite navigation systems.

**The time it takes for a device to determine its GPS coordinates varies strongly and may depend on:**

- The quality of the GPS sensor
- The last time since the device had last determined its GPS location
- Cloud cover
- Buildings or other structures obstructing view of the sky

**To obtain a GPS signal you should be outdoors with good visibility of the sky. To get a strong GPS signal:**

- Stand as far from buildings, trees, or other structures as possible
- Make sure your body isn't obstructing view of the sky
- Get an initial GPS location at the beginning of the day before starting to collect points in the field
- Enable A-GPS (data-network assisted) on your device

*Note: GPS in this context does not exclusively refer to the Global Positioning System but also to other satellite navigation systems used by mobile devices, such as GLONASS.*

**Troubleshooting**

If you are unable to get a GPS location with the GPS response type, please check these options:

- Check the location settings on your device to ensure GPS is enabled
- Install a free app that uses GPS to see if you can get a GPS location that way (e.g. `GPS Status for Android <https://play.google.com/store/apps/details?id=com.eclipsim.gpsstatus2>`_ or `GPS Status for iPhones <https://apps.apple.com/ca/app/gps-status/id378085995>`_)
- Check your phone settings/manufacturer manual to see if the device has GPS available
- If your collected GPS points are pointing to the wrong location, it's possible your device is set to collecting its location from a network tower that was bought second hand and has not properly been reset with the new hard-coded location. You can avoid this issue by turning off network location as an option within the Android system settings, forcing Collect to wait for the actual GPS location.

