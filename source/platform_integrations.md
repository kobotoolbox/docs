# Integrating KoboToolbox with other platforms
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/97316be6a5af1a0e6b8f4620bfff1c7aca8e7378/source/platform_integrations.md" class="reference">19 Nov 2026</a>

You can connect KoboToolbox with external applications using the <a href="https://support.kobotoolbox.org/api.html" class="reference">Application Programming Interface (API)</a>, <a href="https://support.kobotoolbox.org/rest_services.html" class="reference">REST Services</a>, or existing third-party integrations. These connections allow you to share project data, automate workflows, and reduce manual data entry.

This article introduces several platforms with existing KoboToolbox integrations, outlining their features and how to get started.

| **Platform** | **Description** |
| :--- | :--- |
| **monday.com** | Automatically creates tasks and tracks project activities using KoboToolbox submissions. |
| **OpenFn** | Automates data processing and transfers KoboToolbox submissions to other systems, such as DHIS2. |
| **QGIS** | Imports KoboToolbox submissions as map layers for geographic visualization and analysis. |
| **TolaData** | Imports KoboToolbox data to track project indicators, monitor results, and create reports. |
| **n8n** | Connects KoboToolbox with other applications to automate data transfers, notifications, and workflows. |
| **OpenSPP** | Imports KoboToolbox submissions to manage beneficiary information and social protection program records. |
| **DevResults** | Imports KoboToolbox data into monitoring and evaluation tools to track indicators and report on results. |

## Integrating KoboToolbox with monday.com

<a href="https://monday.com/" class="reference external">monday.com</a> is a work management platform that helps teams organize tasks, manage projects, and track workflows.

The **KoboToolbox integration for monday.com** automatically sends new submissions to a monday.com board, allowing teams to track field activities and manage collected data alongside other project workflows.

With this integration, you can:

- Automatically create new items in monday.com from KoboToolbox submissions.
- Map KoboToolbox questions to corresponding board columns.
- Map questions in different form languages to monday.com columns.

<details>
<summary><strong>Connecting KoboToolbox to monday.com</strong></summary>
<br>
The integration is available through the <a href="https://monday.com/marketplace" class="reference external">monday.com Apps Marketplace</a>.
<br><br>
To set up the integration:
<ol>
  <li>Install the <a href="https://monday.com/marketplace/listing/10000284/kobotoolbox" class="reference external">KoboToolbox integration</a> in monday.com.</li>
  <li>Connect your KoboToolbox account using your <strong>server URL</strong> and <strong>API key</strong>.</li>
  <li>Select the KoboToolbox project and monday.com board you want to connect.</li>
  <li>Map the KoboToolbox questions to the corresponding monday.com columns.</li>
  <li>Configure REST Services in KoboToolbox to automatically send new submissions to monday.com:
    <ul>
      <li>Copy the integration link provided during setup or in the description on your monday.com board.</li>
      <li>Open your KoboToolbox project and go to <strong>SETTINGS &gt; REST Services &gt; Register a New Service</strong>.</li>
      <li>Paste the integration link into the <strong>Endpoint URL</strong> field.</li>
      <li>Under <strong>Custom HTTP Headers</strong>, enter <code>webhook-auth</code> in the <strong>Name</strong> field and your KoboToolbox API key in the <strong>Value</strong> field.</li>
      <li>Click <strong>SAVE</strong> to complete the configuration.</li>
    </ul>
  </li>
</ol>
Once configured, new submissions are added to your monday.com board based on the selected field mappings. Changes to existing submissions or forms in KoboToolbox are not automatically reflected in monday.com, and changes made in monday.com are not sent back to KoboToolbox.
</details>

<br/>

<p class="note">
  To learn how to find your server URL and API key, see <a href="https://support.kobotoolbox.org/api.html" class="reference">Getting started with the API</a>.
</p>

## Integrating KoboToolbox with OpenFn

<a href="https://www.openfn.org/" class="reference external">OpenFn</a> is an open source workflow automation platform that connects applications and automates data processing.

The **KoboToolbox integration with OpenFn** allows organizations to retrieve, process, and transfer submissions to other systems for analysis and reporting.

With this integration, you can:

- Retrieve KoboToolbox submissions using the API or REST Services.
- Transform and organize data before transferring it to other platforms, such as DHIS2.
- Schedule workflows to retrieve new or updated submissions automatically.

<details>
<summary><strong>Connecting KoboToolbox to OpenFn</strong></summary>
<br>
The integration uses the KoboToolbox API or REST Services to transfer project data to OpenFn.
<br><br>
To set up the integration:
<ol>
  <li>Create an <a href="https://www.openfn.org" class="reference external">OpenFn</a> account and set up a project.</li>
  <li>Create a workflow in OpenFn and select the <a href="https://docs.openfn.org/adaptors/kobotoolbox" class="reference external">KoboToolbox adaptor</a>.</li>
  <li>Configure the connection using your KoboToolbox server URL and account credentials.</li>
  <li>Select the KoboToolbox form you want to retrieve submissions from.</li>
  <li>Configure the workflow to process the submissions and send the results to your destination platform.</li>
  <li>Test the workflow and configure how it should run automatically.</li>
</ol>
You can also use REST Services in KoboToolbox to send new submissions directly to an OpenFn workflow.
</details>

<br/>

<p class="note">
  For more information, see <a href="https://docs.openfn.org/adaptors/kobotoolbox" class="reference external">Connecting KoboToolbox to OpenFn</a> and <a href="https://docs.openfn.org/documentation/kobo-to-dhis2" class="reference external">Creating a KoboToolbox to DHIS2 workflow</a>.
</p>

## Integrating KoboToolbox with QGIS

<a href="https://www.qgis.org/" class="reference external">QGIS</a> is an open source geographic information system (GIS) used to visualize, analyze, and manage geographic data.

Several QGIS <a href="https://plugins.qgis.org/search/?q=kobotoolbox" class="reference external">plugins</a> allow you to import KoboToolbox submissions as map layers. The <a href="https://plugins.qgis.org/plugins/connect_kobo/" class="reference external">Connector for Kobo</a> plugin offers the following features:

- Import KoboToolbox submissions as GeoJSON map layers.
- Browse available projects, view submission counts, and search for forms.
- Automatically detect geographic data, including different geometry types.
- Split map layers based on attribute values.

<details>
<summary><strong>Connecting KoboToolbox to QGIS</strong></summary>
<br>
The integration is available through the <a href="https://plugins.qgis.org/plugins/" class="reference external">QGIS Plugin Repository</a>.
<br><br>
To set up the integration:
<ol>
  <li>Open QGIS and go to <strong>Plugins &gt; Manage and Install Plugins</strong>.</li>
  <li>Search for <strong>Connector for Kobo</strong> and install the plugin.</li>
  <li>Open the plugin and select <strong>Get Data</strong>.</li>
  <li>Connect to your KoboToolbox account by selecting your server and entering your credentials.</li>
  <li>Search for and select the KoboToolbox form you want to import.</li>
  <li>Download the submissions as a GeoJSON map layer.</li>
</ol>
</details>

<br/>

<p class="note">
  For more information, see <a href="https://plugins.qgis.org/plugins/connect_kobo/" class="reference external">Connector for Kobo in the QGIS Plugin Repository</a>.
</p>

## Integrating KoboToolbox with TolaData

<a href="https://www.toladata.com/" class="reference external">TolaData</a> is a monitoring and evaluation (M&E) platform that helps organizations track project indicators, analyze results, and manage reporting.

The **KoboToolbox integration with TolaData** allows you to import collected data for monitoring and reporting.

With this integration, you can:

- Import KoboToolbox submissions and link them to project indicators and results frameworks.
- Configure automatic data updates using TolaData's **Auto-Pull** feature.
- Create dashboards and reports to monitor project performance and results.

<details>
<summary><strong>Connecting KoboToolbox to TolaData</strong></summary>
<br>
The integration uses the KoboToolbox API to retrieve project data.
<br><br>
To set up the integration:
<ol>
  <li>Open your TolaData account and configure the KoboToolbox connection using your <strong>server URL</strong> and <strong>API key</strong>.</li>
  <li>Select the KoboToolbox projects or forms you want to import.</li>
  <li>Import the submission data into TolaData.</li>
  <li>Link the imported data to relevant project indicators.</li>
  <li>Configure Auto-Pull rules if you want to update indicator results automatically as new data becomes available.</li>
</ol>
Once connected, you can use KoboToolbox data in TolaData's monitoring, analysis, and reporting tools without manually exporting and importing files each time.
</details>

<br/>

<p class="note">
  For more information, see <a href="https://www.toladata.com/docs/knowledge-base/data-collection-and-management/importing-data-from-kobo-toolbox/" class="reference external">Importing data from KoboToolbox</a>.
</p>

## Integrating KoboToolbox with n8n

<a href="https://n8n.io/" class="reference external">n8n</a> is a workflow automation platform that connects applications and automates tasks.

The <a href="https://n8n.io/integrations/kobotoolbox/" class="reference external">KoboToolbox integration</a> with n8n allows you to automate data transfers, notifications, and reporting across applications.

With this integration, you can:

- Automatically retrieve KoboToolbox forms and submissions.
- Send collected data to other applications, such as Google Sheets, Airtable, or Slack.
- Trigger workflows when new submissions are received.
- Manage files and submission validation statuses.
- Format and transform data for use in other platforms.

<details>
<summary><strong>Connecting KoboToolbox to n8n</strong></summary>
<br>
The integration is available through the <a href="https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox" class="reference external">built-in KoboToolbox node</a> in n8n.
<br><br>
To set up the integration:
<ol>
  <li>Create an n8n account and set up a new workflow.</li>
  <li>Add the <strong>KoboToolbox</strong> node to your workflow.</li>
  <li>Configure your KoboToolbox credentials using your server URL and API token.</li>
  <li>Select the KoboToolbox action you want to perform, such as retrieving forms or submissions.</li>
  <li>Add other application nodes to define how the collected data should be processed or transferred.</li>
  <li>Test the workflow and configure it to run automatically.</li>
</ol>
Once configured, n8n can automatically retrieve and process KoboToolbox data based on your workflow settings.
</details>

<br/>

<p class="note">
  For more information, see <a href="https://n8n.io/integrations/kobotoolbox/" class="reference external">KoboToolbox integrations in n8n</a> and <a href="https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/" class="reference external">KoboToolbox node documentation</a>.
</p>

## Integrating KoboToolbox with DevResults

<a href="https://www.devresults.com/" class="reference external">DevResults</a> is a monitoring and evaluation (M&E) platform that helps organizations manage project data, track indicators, and report on results.

The <a href="https://help.devresults.com/help/kobo-toolbox-integration" class="reference external">KoboToolbox integration</a> with DevResults allows you to import survey submissions into data tables for monitoring and reporting.

With this integration, you can:

- Import KoboToolbox submissions and select which form fields to include.
- Manually refresh data tables or configure automatic imports using KoboToolbox REST Services.
- Link collected data to project indicators, geographic locations, and disaggregation categories.

<details>
<summary><strong>Connecting KoboToolbox to DevResults</strong></summary>
<br>
The integration uses the KoboToolbox API to retrieve project data. A DevResults site owner must first enable the KoboToolbox integration under <strong>Administration &gt; Settings</strong>.
<br><br>
To set up the integration:
<ol>
  <li>Open DevResults and go to <strong>Program Info &gt; Data Tables</strong>.</li>
  <li>Click <strong>New Data Table</strong> and select <strong>Import from KoboToolbox</strong>.</li>
  <li>Enter your KoboToolbox server name, project Asset ID, and account credentials or API key.</li>
  <li>Select the form fields you want to import and configure the corresponding data table columns.</li>
  <li>Click <strong>Create Data Table</strong> to complete the setup and import your data.</li>
  <li>To enable automatic updates, create a DevResults API key and configure a REST Service in KoboToolbox using the data table's webhook URL and API key.</li>
</ol>
</details>

<br/>

<p class="note">
  For more information, see <a href="https://help.devresults.com/help/kobo-toolbox-integration" class="reference external">Import Data From KoboToolbox</a>.
</p>

## Integrating KoboToolbox with OpenSPP

<a href="https://openspp.org/en/" class="reference external">OpenSPP</a> is an open source social protection platform that helps organizations manage beneficiary registries and social assistance programs.

The <a href="https://docs.openspp.org/config_guide/event_data/odk_kobo" class="reference external">KoboToolbox integration with OpenSPP</a> allows you to import survey submissions and link them to beneficiary records for verification and program monitoring.

With this integration, you can:

- Automatically import KoboToolbox submissions through scheduled updates or direct transfers.
- Map form questions to OpenSPP event fields and link submissions to existing registrants using unique identifiers.
- Import geographic coordinates and media attachments, such as photos.
- Configure approval workflows to review imported records before activation.

<details>
<summary><strong>Connecting KoboToolbox to OpenSPP</strong></summary>
<br>
The integration uses the KoboToolbox API to retrieve project data. OpenSPP supports scheduled imports (Pull Sync) and direct submission transfers (Push Sync).
<br><br>
To set up scheduled imports from KoboToolbox:
<ol>
  <li>Create a form in KoboToolbox and an event type with corresponding fields in OpenSPP.</li>
  <li>Open OpenSPP and go to <strong>Studio &gt; External Data Sources &gt; Create</strong>.</li>
  <li>Select <strong>KoboToolbox</strong> as the source type and enter your KoboToolbox server URL, username, and API token.</li>
  <li>Enter your KoboToolbox form ID, select the corresponding OpenSPP event type, and configure the synchronization schedule.</li>
  <li>Map KoboToolbox questions to the corresponding OpenSPP event fields.</li>
  <li>Configure a registrant identifier to link submissions to existing records or create new registrants when no match is found.</li>
  <li>Click <strong>Test Connection</strong> to verify the configuration, then <strong>Activate</strong> to enable automatic synchronization.</li>
</ol>
Once configured, OpenSPP automatically retrieves new KoboToolbox submissions based on your synchronization schedule and creates event records linked to the corresponding registrants.
</details>

<br/>

<p class="note">
  For more information, see <a href="https://docs.openspp.org/config_guide/event_data/odk_kobo" class="reference external">ODK/KoboToolbox Integration in OpenSPP</a>.
</p>

## Connecting KoboToolbox to other applications

In addition to these integrations, you can use the KoboToolbox API to connect project data to other applications for analysis, reporting, and automation.

For example, you can:

- Connect KoboToolbox to <a href="https://support.kobotoolbox.org/connect_excel_powerbi.html" class="reference">Microsoft Excel and Power BI</a> to create reports and dashboards.
- Connect KoboToolbox to <a href="https://support.kobotoolbox.org/connect_google.html" class="reference">Google Sheets and Data Studio</a> to analyze data and create interactive dashboards.
- Retrieve project data <a href="https://support.kobotoolbox.org/connect_r.html" class="reference">directly into R</a> or Python for statistical analysis.
- Connect KoboToolbox to other applications using <a href="https://pipedream.com/apps/kobotoolbox" class="reference external">Pipedream</a> to automate data transfers and workflows.
- Use <a href="https://support.kobotoolbox.org/synchronous_exports.html" class="reference">synchronous exports</a> to connect external applications to CSV or XLSX data.
- Configure <a href="https://support.kobotoolbox.org/rest_services.html" class="reference">REST Services</a> to automatically send new submissions to external systems.

<p class="note">
  <strong>Note:</strong> Third-party integrations may have their own subscription requirements, permissions, and data security policies. Review each platform's requirements before connecting your KoboToolbox account, and ensure that project data is only shared with authorized applications.
</p>
