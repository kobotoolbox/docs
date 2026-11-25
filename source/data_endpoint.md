# Using the API data endpoint
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/ad57360b1651a3aa0ef4f4002a4f29787631a47e/source/data_endpoint.md" class="reference">19 Nov 2026</a>

The **KoboToolbox API data endpoint** allows you to retrieve project submissions directly into external applications, such as R or Python, without manually downloading data files. You can use it to filter submissions, automate data retrieval, and connect KoboToolbox data to other tools for analysis and reporting.

This article covers understanding the data endpoint, accessing project submissions, authenticating API requests, using pagination and filters, connecting KoboToolbox data to R, and automating data retrieval.

<p class="note">
  If you prefer to connect external applications to ready-to-use CSV or XLSX files without writing custom scripts, see <a href="https://support.kobotoolbox.org/synchronous_exports.html" class="reference">Using the API for synchronous exports</a>.
</p>

## Understanding the data endpoint

The data endpoint is part of the KoboToolbox **Application Programming Interface (API)**. It provides direct access to project submissions in **JSON format**, a structured data format commonly used by software applications.

Unlike <a href="https://support.kobotoolbox.org/synchronous_exports.html" class="reference">synchronous exports</a>, which use saved export settings to generate CSV or XLSX files, the data endpoint provides more flexible access to individual submission records. It allows you to customize requests and control which data is retrieved.

The data endpoint returns <a href="https://support.kobotoolbox.org/glossary.html#question-name" class="reference">question names</a> and <a href="https://support.kobotoolbox.org/glossary.html#choice-name" class="reference">choice names</a> rather than their labels. If you need question and choice labels in your exported data, use synchronous exports instead.

The data endpoint is particularly useful for:

- Retrieving submissions directly into statistical software, such as R or Python.
- Filtering submissions based on specific conditions.
- Automating data retrieval for recurring analysis and reports.
- Integrating KoboToolbox data with other datasets or applications.

Accessing the data endpoint typically requires some programming knowledge or software that supports API connections. Some packages and applications can simplify this process by handling API requests automatically.

<p class="note">
  To learn more about using R packages to connect to the data endpoints, see <a href="https://support.kobotoolbox.org/connect_r.html" class="reference">Connecting KoboToolbox data to R</a>.
</p>

## Accessing the data endpoint

To access the data endpoint, you need your **server URL**, **project asset UID**, and **API key**.

- **Server URL:** The web address of the KoboToolbox server where your account is hosted.
- **Project asset UID:** A unique identifier for the KoboToolbox project you want to access.
- **API key:** A personal authentication token that allows external applications to access your KoboToolbox account and project data.

<p class="note">
  For instructions on retrieving these details, see <a href="https://support.kobotoolbox.org/api.html" class="reference">Getting started with the API</a>.
</p>

### Finding your project's data endpoint

Each KoboToolbox project has a data endpoint with the following URL structure:

`https://[server-url]/api/v2/assets/[project-asset-UID]/data/?format=json`

Replace `[server-url]` and `[project-asset-UID]` with your KoboToolbox server URL and project asset UID.

When an application sends a request to this endpoint, KoboToolbox returns the project's submission data in JSON format.

### Authenticating API requests

KoboToolbox uses **authentication** to verify that an application has permission to access project data.

For API requests, authentication is typically provided through an API key included in the request header:

`Authorization: Token [your-api-key]`

Replace `[your-api-key]` with your actual KoboToolbox API key.

For example, you can retrieve submissions using the following `curl` command in a terminal:

```bash
curl -H "Authorization: Token YOUR_API_KEY" \
"https://kf.kobotoolbox.org/api/v2/assets/YOUR_PROJECT_UID/data/?format=json"
```

<p class="note">
  <strong>Note:</strong> Keep your API key confidential. Avoid including it directly in scripts that are shared publicly. For automated workflows, use environment variables or other secure methods to store credentials.
</p>

### Understanding the API response

When you retrieve submissions through the data endpoint, KoboToolbox returns a **JSON response** containing the submission records your account has permission to access and information about the results.

For example, a simplified response for a project with 250 submissions might look like this:

```json
{
  "count": 250,
  "next": "https://[server-url]/api/v2/assets/[project-asset-UID]/data/?limit=100&start=100",
  "previous": null,
  "results": [
    {
      "_id": 101,
      "age": "35",
      "region": "north"
    }
  ]
}
```

The response includes:

- `count`: The total number of submissions matching the request.
- `next`: The URL for retrieving the next page of submissions.
- `previous`: The URL for retrieving the previous page, if available.
- `results`: The submission records returned in the current request.

The `results` field contains the actual submission data, while the other fields help you navigate through the available records.

<p class="note">
  For a description of the fields in each submission record, including system fields, question types, and repeat groups, see <a href="https://support.kobotoolbox.org/api_submission_data.html" class="reference">Working with submission data in the JSON API</a>.
</p>

### Understanding pagination

The KoboToolbox API uses **pagination** to return submissions in smaller batches rather than sending all records in a single request.

On the Global and European Union KoboToolbox Servers, the API returns:

- **100 submissions per request** by default.
- **Up to 1,000 submissions per request** when a higher limit is specified.

If your project contains more submissions than the number returned in a single request, you must retrieve additional pages to access the complete dataset.

### Retrieving submissions in batches

You can control which submissions are returned using two parameters:

- `limit`: Specifies the maximum number of submissions returned in a request.
- `start`: Specifies how many submissions to skip before returning results.

For example, to retrieve the first 100 submissions:

`https://[server-url]/api/v2/assets/[project-asset-UID]/data/?limit=100&start=0`

To retrieve the next 100 submissions:

`https://[server-url]/api/v2/assets/[project-asset-UID]/data/?limit=100&start=100`

You can also use the `next` URL provided in the API response to retrieve the next batch of submissions. When `next` is `null`, there are no additional pages to retrieve.

<p class="note">
  <strong>Note:</strong> Some applications and programming packages handle pagination automatically, allowing you to retrieve all submissions without manually requesting each page.
</p>

## Filtering submissions

The data endpoint allows you to retrieve only submissions that meet specific conditions. This can be useful when working with large datasets or when you only need a subset of your project data.

For example, the following filter retrieves submissions received after September 1, 2026:

```json
{"_submission_time": {"$gt": "2026-09-01T00:00:00"}}
```

In this example:

- `_submission_time` refers to the submission timestamp.
- `$gt` means "greater than."
- The date specifies the point after which submissions should be retrieved.

if your form contains a question named `region`, you could retrieve submissions where the response is `north` using:

```json
{"region": "north"}
```

### Applying filters to API requests

You can include these filters in an API request using the `query` parameter.

For example, the following `curl` command retrieves submissions in the northern region after the specified date:

```bash
curl -G \
  -H "Authorization: Token YOUR_API_KEY" \
  --data-urlencode 'query={
    "region": "north",
    "_submission_time": {
      "$gt": "2026-09-01T00:00:00"
    }
  }' \
  "https://kf.kobotoolbox.org/api/v2/assets/YOUR_PROJECT_UID/data/?format=json"
```

The `--data-urlencode` option ensures that the filter is correctly formatted in the request URL.

<p class="note">
  <strong>Note:</strong> Filters use the underlying question and choice names, rather than the labels displayed in the form. If you need more advanced filtering, see the API documentation for your KoboToolbox server.
</p>

## Automating data retrieval

The data endpoint allows external applications to retrieve updated project data without manually downloading new files.

You can configure scripts or applications to run at regular intervals, such as daily or weekly, to retrieve new submissions and update your analyses.

For example, an automated workflow could:

1. Connect to your KoboToolbox project using the API.
2. Retrieve submissions added or modified since the previous update.
3. Process the data using R or Python.
4. Update a report or dataset used for analysis.

You can use filters to retrieve only new or modified submissions, reducing the amount of data transferred with each request.

The frequency of updates depends on how your external application or script is configured. The data endpoint does not automatically send new submissions to connected applications.

<p class="note">
  <strong>Note:</strong> When automating data retrieval, ensure your script handles pagination, connection errors, and authentication securely.
</p>

### Retrieving new and modified submissions

Each submission includes two timestamps:

- `_submission_time`: The time when the server received the submission. This value never changes.
- `_date_modified`: The time when the submission was last modified. This value is updated when the submission is edited, when its validation status changes, or when an attachment is added or deleted.

A filter on `_submission_time` retrieves new submissions, but it does not retrieve submissions that were edited after your previous update. To retrieve both new and modified submissions, filter on `_date_modified` instead.

For example, the following `curl` command retrieves the submissions that were added or modified since the specified time:

```bash
curl -G \
  -H "Authorization: Token YOUR_API_KEY" \
  --data-urlencode 'query={
    "_date_modified": {
      "$gte": "2026-09-01T00:00:00+00:00"
    }
  }' \
  "https://kf.kobotoolbox.org/api/v2/assets/YOUR_PROJECT_UID/data/?format=json"
```

In this example:

- `$gte` means "greater than or equal to."
- The timestamp is the highest `_date_modified` value that you received in your previous update. Subtract a few minutes from it, so that changes made at the same moment as your previous update are not missed.

Some of the submissions returned may be ones you already retrieved. Use the `_id` field to match them with the submissions you already have, and replace those that changed.

<p class="note">
  <strong>Note:</strong> Deleted submissions are not returned by this filter. If the submissions from your server do not include <code>_date_modified</code>, the server runs a version of KoboToolbox from before this field was introduced. For more details, see <a href="https://support.kobotoolbox.org/api_submission_data.html#retrieving-only-new-and-modified-submissions" class="reference">Working with submission data in the JSON API</a>.
</p>

## Additional API documentation

The KoboToolbox API provides additional features for working with project data, including advanced filtering, sorting, and selecting specific fields. You can also use the API to create and deploy projects, manage permissions, and add, edit, or delete submissions.

For detailed information about the available endpoints, parameters, and response formats, see the interactive API documentation for your server:

- **Global KoboToolbox Server:** <a href="https://kf.kobotoolbox.org/api/v2/docs/" class="reference external">https://kf.kobotoolbox.org/api/v2/docs/</a>
- **European Union KoboToolbox Server:** <a href="https://eu.kobotoolbox.org/api/v2/docs/" class="reference external">https://eu.kobotoolbox.org/api/v2/docs/</a>
- **Private Server:** `https://[server-url]/api/v2/docs/`

## Troubleshooting

The following table outlines common issues when accessing the data endpoint.

| **Issue** | **Possible cause and solution** |
| :--- | :--- |
| Authentication error (401) | Your API key may be missing, invalid, or incorrectly formatted. Check the authentication header and API key. |
| Permission denied (403) | Your account may not have permission to view the project's submissions. Check your project permissions. |
| Endpoint not found (404) | The server URL, project asset UID, or endpoint path may be incorrect. Check the URL and make sure it uses the correct API version. |
| Only some submissions are returned | The API uses pagination. Check the `next` field and retrieve additional pages. |
| Unexpected submission values | The data endpoint returns stored question names and values rather than the labels used in exported files. |
| New submissions do not appear in an external application | The application may not have refreshed its data. Check how often the API request is run. |
| Edited submissions are not updated in an external application | A filter on `_submission_time` only returns new submissions. Filter on `_date_modified` to also retrieve submissions that were modified since the previous update. |
