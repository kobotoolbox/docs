# Dynamic Data Attachments

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/1d7f77a9494f8bbbc0728a28c2e7af03c98f3f7b/source/dynamic_data_attachment.md" class="reference">5
Aug 2021</a>

This support article illustrates how data from one project can be linked
dynamically and referenced by other projects. It also aims to demonstrate some
practical examples that this feature supports.

Dynamically linking projects allows for the same powerful capabilities as the
[`pulldata()` function](pull_data_kobotoolbox.md) but without the need to
maintain a separate CSV file since the data stored in a linked project acts as
the data source. Users can continue collecting data in the _parent project_ and
simultaneously use that data in other linked _child projects_, therefore enable
creation and management of longitudinal survey projects (longitudinal data is
collected through a series of repeated observations of the same subjects over a
short or long period). Users can also dynamically link a _child project_ with a
**shared** _parent project_.

Users can retrieve any (non-media) responses (`text`, `integer`, `decimal`,
`select_one`, `select_multiple`, etc.) in a linked _child project_ (Round 2 in
this example) that has already been collected and stored in the _parent project_
(Round 1 in this example).

Users can also perform [various calculations](advanced_calculate.md) on linked
data in the _child project_, such as counting (`count()`) responses and
computing the sum (`sum()`), maximum (`max()`), or minimum (`min()`) value of a
particular variable.

## Dynamically linking projects in XLSForm

Dynamically linking projects requires a _parent project_ and at least one _child
project_. The
<a download class="reference" href="./_static/files/dynamic_data_attachment/Round_1.xlsx">_parent
project_</a> requires no additional modification from a normal XLSForm; however,
the
<a download class="reference" href="./_static/files/dynamic_data_attachment/Round_2.xlsx">_child
project_</a> involves adding an `xml-external` question type. All subsequent
references to the _parent project_ occur in the `calculation` column using the
node path.

Users could design their _parent project_ as shown in the image below:

![Round 1](/images/dynamic_data_attachment/Round_1.png)

In the same way, users could design their _child project_ as shown in the image
below:

![Round 2](/images/dynamic_data_attachment/Round_2.png)

> **Note:** The name used for the `xml-external` question type in the _child
> project_ is crucial for linking with the _parent project_. In the above
> example, it was named "survey", but it can be any name consisting of Latin
> characters and numbers.

## Understanding the syntax used in the `calculation` column of the _child project_

| XLSForm Syntax                                                                                  | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `count(instance('survey')/root/data[P_Enumerator])`                                             | Return the total count of `P_Enumerator` in the _parent project_.                                                                                     |
| `count(instance('survey')/root/data[P_Enumerator = current()/../C_Enumerator])`                 | Return the total count of where `C_Enumerator` in the _child project_ is equal to `P_Enumerator` in the _parent project_.                             |
| `instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Name`     | Return `P_Name` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.     |
| `instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Age`      | Return `P_Age` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.      |
| `instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Sex`      | Return `P_Sex` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.      |
| `instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Family`   | Return `P_Family` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_.   |
| `sum(instance('survey')/root/data/P_Demographic/P_Family)`                                      | Return the sum of `P_Family` (`P_Demographic` group) from the _parent project_.                                                                       |
| `max(instance('survey')/root/data/P_Demographic/P_Family)`                                      | Return the maximum value entered in `P_Family` (`P_Demographic` group) from the _parent project_.                                                     |
| `min(instance('survey')/root/data/P_Demographic/P_Family)`                                      | Return the minimum value entered in `P_Family` (`P_Demographic` group) from the _parent project_.                                                     |
| `instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Language` | Return `P_Language` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_. |
| `instance('survey')/root/data[P_Demographic/P_SN = current()/../C_SN]/P_Demographic/P_Location` | Return `P_Location` (`P_Demographic` group) from the _parent project_ where `C_SN` in the _child project_ is equal to `P_SN` in the _parent project_. |

## Setting up for dynamic linking

Users can link projects dynamically in two scenarios:

1. The same user owns both the _parent project_ and _child project_, and
2. Different users own each of the projects and the _parent project_ is shared

### 1. Both projects owned by the same user

Follow the steps below to dynamically link projects:

**Step 1:** Upload and deploy the _parent project_.

<video controls><source src="./_static/files/dynamic_data_attachment/Uploading_and_Deploying_xlsform_(round_1_survey).mp4" type="video/mp4"></video>

**Step 2:** Enable data sharing with _child projects_ by toggling the **Data
Sharing** switch in the _parent project_’s **SETTINGS>Connect Projects** section
(disabled by default), and click **ACKNOWLEDGE AND CONTINUE** in the
confirmation modal. Users can then restrict specific variables to share with
_child projects_ or share **all** variables from the table by toggling the
**Select specific questions** switch.

<video controls><source src="./_static/files/dynamic_data_attachment/Connect_Projects_(round_1_survey).mp4" type="video/mp4"></video>

**Step 3:** Upload and deploy the _child project_.

<video controls><source src="./_static/files/dynamic_data_attachment/Uploading_and_Deploying_xlsform_(round_2_survey).mp4" type="video/mp4"></video>

**Step 4:** In the _child project_'s **SETTINGS>Connect Projects**, click the
**Select a different project to import data from** dropdown menu and select a
_parent project_ to link. Rename the linked _parent project_ to the same
`xml-external` question name defined in the XLSForm ("survey" in this example)
and click **IMPORT**. You can then select specific variables from the _parent
project_ to share with the _child project_.

<video controls><source src="./_static/files/dynamic_data_attachment/Connect_Projects_(round_2_survey).mp4" type="video/mp4"></video>

The _child project_ now has access to data from the _parent project_. In this
example, data from the _Round 1 Survey_ is linked to the _Round 2 Survey_.

### 2. Projects owned by different users

Assume a scenario where **userA** has a _parent project_ shared with **userB**.
**userB** can create a _child project_ and link it dynamically with that
project. For example:

**Step 1:** **userA** should follow **Step 1** and **Step 2** of **Both Projects
Owned by Same User** to _upload_, _deploy_ and _configure_ the _parent project_.

**Step 2:** **userA** should then
<a class="reference" href="managing_permissions.html" >share the _parent
project_ with **userB**</a> and grant the minimum permissions of: _View form_
and _View submissions_. **userB** can now dynamically link their _child project_
to the _parent project_ of **userA**.

**Step 3:** **userB** should now _upload_, _deploy_ and _configure_ their _child
project_ as outlined in **Step 3** and **Step 4** of **Both Projects Owned by
Same User**.

## Collecting and managing data with dynamic linking

Users can collect data for dynamically linked projects on both the
<a class="reference" href="kobocollect-android.html">**Collect** Android app</a>
and <a class="reference" href="data_through_webforms.html">**Enketo** web
form</a>.

Please note the following when collecting data:

-   At least one submission must be present in the _parent project_ for the
    _child project_ to function as expected.
-   There is a five-minute delay syncing the _parent project_'s updated data
    with the _child project_.
-   Frequently download the _child project_ in **Collect** or **Enketo** (when
    in offline mode) to ensure the data is in sync with the _parent project_\*

\*One can configure the **Collect** Android app, with an internet connection, to
update the _parent project_'s data automatically in **General Settings>Form
management>Blank form update mode>Previously downloaded forms only or Exactly
match server**. Note that enabling this setting could drain your device's
battery faster than usual.

In this example, some "dummy" entries have been made in the _parent project_.

![Data](/images/dynamic_data_attachment/Server_data.png)

With some dummy entries in the _parent project_, the _child project_ can now see
that data during data collection. In this example _child project_ (_Round 2
Survey_), only the two fields of **Enumerators name** and **Identification
Number** are entered manually while the rest is linked automatically with the
_parent project_.

![Enketo web form](/images/dynamic_data_attachment/Enketo.png)
