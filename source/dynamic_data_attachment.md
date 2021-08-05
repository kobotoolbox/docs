# Dynamic Data Attachments

This support article illustrates how data from one project can be linked dynamically and referenced by other projects. It also aims to demonstrate some practical examples that this feature supports.

Dynamically linking projects allows for the same powerful capabilities as the [`pulldata()` function](pull_data_kobotoolbox.md) but without the need to maintain a separate CSV file since the data stored in a linked project acts as the data source. Users can continue collecting data in the _parent project_ and simultaneously use that data in other linked _child projects_, therefore enable creation and management of longitudinal survey projects (longitudinal data is collected through a series of repeated observations of the same subjects over a short or long period). Users can also dynamically link a _child project_ with a __shared__ _parent project_.

Users can retrieve any (non-media) responses (`text`, `integer`, `decimal`, `select_one`, `select_multiple`, etc.) in a linked _child project_ (Round 2 in this example) that has already been collected and stored in the _parent project_ (Round 1 in this example).

Users can also perform [various calculations](advanced_calculate.md) on linked data in the _child project_, such as counting (`count()`) responses and computing the sum (`sum()`), maximum (`max()`), or minimum (`min()`) value of a particular variable.

## Dynamically linking projects in XLSForm

Dynamically linking projects requires a _parent project_ and at least one _child project_. The <a download class="reference" href="./_static/files/dynamic_data_attachment/Round_1.xlsx">_parent project_</a> requires no additional modification from a normal XLSForm; however, the <a download class="reference" href="./_static/files/dynamic_data_attachment/Round_1.xlsx">_child project_</a> involves adding an `xml-external` question type. All subsequent references to the _parent project_ occur in the `calculation` column using the node path.

Users could design their _parent project_ as shown in the image below:

![Round 1](/images/dynamic_data_attachment/Round_1.png)

In the same way, users could design their _child project_ as shown in the image below:

![Round 2](/images/dynamic_data_attachment/Round_2.png)

> __Note:__ The name used for the `xml-external` question type in the _child project_ is crucial for linking with the _parent project_. In the above example, it was named "survey", but it can be any name consisting of Latin characters and numbers.

## Understanding the syntax used in the `calculation` column of the _child project_

XLSForm Syntax | Description
--- | ---
`count(instance('survey')/root/data[P_Enumerator])` | Return the total count of `P_Enumerator` in the _parent project_.
`count(instance('survey')/root/data[P_Enumerator = current()/../C_Enumerator])` | Return the total count of where `C_Enumerator` in the _child project_ is equal to `P_Enumerator` in the _parent project_.
`instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Name` | Return `P_Name` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.
`instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Age` | Return `P_Age` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.
`instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Sex` | Return `P_Sex` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.
`instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Family` | Return `P_Family` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.
`sum(instance('survey')/root/data/P_Demographic/P_Family)` | Return the sum of `P_Family` (`P_Demographic` group) from the _parent project_.
`max(instance('survey')/root/data/P_Demographic/P_Family)` | Return the maximum value entered in `P_Family` (`P_Demographic` group) from the _parent project_.
`min(instance('survey')/root/data/P_Demographic/P_Family)` | Return the minimum value entered in `P_Family` (`P_Demographic` group) from the _parent project_.
`instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Language` | Return `P_Language` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.
`instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Location` | Return `P_Location` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.

## Setting up for dynamic linking

Users can link projects dynamically in two scenarios:
1. The same user owns both the _parent project_ and _child project_, and
2. Different users own each of the projects and the _parent project_ is shared

### 1. Both projects owned by the same user

Follow the steps below to dynamically link projects:

__Step 1:__ Upload and deploy the _parent project_.

<video controls style="width:100%"><source src="./_static/files/dynamic_data_attachment/Uploading_and_Deploying_xlsform_(round_1_survey).mp4" type="video/mp4"></video>

__Step 2:__ Enable data sharing with _child projects_ by toggling the __Data Sharing__ switch in the _parent project_’s __SETTINGS>Connect Projects__ section (disabled by default), and click __ACKNOWLEDGE AND CONTINUE__ in the confirmation modal. Users can then restrict specific variables to share with _child projects_ or share __all__ variables from the table by toggling the __Select specific questions__ switch.

<video controls style="width:100%"><source src="./_static/files/dynamic_data_attachment/Connect_Projects_(round_1_survey).mp4" type="video/mp4"></video>

__Step 3:__ Upload and deploy the _child project_.

<video controls style="width:100%"><source src="./_static/files/dynamic_data_attachment/Uploading_and_Deploying_xlsform_(round_2_survey).mp4" type="video/mp4"></video>

__Step 4:__ In the _child project_'s __SETTINGS>Connect Projects__, click the __Select a different project to import data from__ dropdown menu and select a _parent project_ to link. Rename the linked _parent project_ to the same `xml-external` question name defined in the XLSForm ("survey" in this example) and click __IMPORT__. You can then select specific variables from the _parent project_ to share with the _child project_.

<video controls style="width:100%"><source src="./_static/files/dynamic_data_attachment/Connect_Projects_(round_2_survey).mp4" type="video/mp4"></video>

The _child project_ now has access to data from the _parent project_. In this example, data from the _Round 1 Survey_ is linked to the _Round 2 Survey_.

### 2. Projects owned by different users

Assume a scenario where __userA__ has a _parent project_ shared with __userB__. __userB__ can create a _child project_ and link it dynamically with that project. For example:

__Step 1:__ __userA__ should follow __Step 1__ and __Step 2__ of __Both Projects Owned by Same User__ to _upload_, _deploy_ and _configure_ the _parent project_.

__Step 2:__ __userA__ should then <a class="reference" href="managing_permissions.html" >share the _parent project_ with __userB__</a> and grant the minimum permissions of: _View form_, _Edit form_, _View submissions_, and _Add submissions_. __userB__ can now dynamically link their _child project_ to the _parent project_ of __userA__.

__Step 3:__ __userB__ should now _upload_, _deploy_ and _configure_ their _child project_ as outlined in __Step 3__ and __Step 4__ of __Both Projects Owned by Same User__.

## Collecting and managing data with dynamic linking

Users can collect data for dynamically linked projects on both the <a class="reference" href="kobocollect-android.html">__Collect__ Android app</a> and <a class="reference" href="data_through_webforms.html">__Enketo__ web form</a>.

Please note the following when collecting data:
- At least one submission must be present in the _parent project_ for the _child project_ to function as expected.
- There is a five-minute delay syncing the _parent project_'s updated data with the _child project_.
- Frequently download the _child project_ in __Collect__ or __Enketo__ (when in offline mode) to ensure the data is in sync with the _parent project_*

\*One can configure the __Collect__ Android app, with an internet connection, to update the _parent project_'s data automatically in __General Settings>Form management>Blank form update mode>Previously downloaded forms only or Exactly match server__. Note that enabling this setting could drain your device's battery faster than usual.

In this example, some "dummy" entries have been made in the _parent project_.

![Data](/images/dynamic_data_attachment/Server_data.png)

With some dummy entries in the _parent project_, the _child project_ can now see that data during data collection. In this example _child project_ (_Round 2 Survey_), only the two fields of __Enumerators name__ and __Identification Number__ are entered manually while the rest is linked automatically with the _parent project_.

![Enketo web form](/images/dynamic_data_attachment/Enketo.png)
