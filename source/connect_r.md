# Connecting KoboToolbox data to R

R is an open source programming language widely used for statistical analysis, data processing, and visualization. You can connect R to KoboToolbox through the KoboToolbox [Application Programming Interface (API)](https://support.kobotoolbox.org/api.html) to retrieve project data without manually downloading files.

There are different ways to connect KoboToolbox to R. You can send API requests directly using R packages such as `httr` and `jsonlite`, or use community-developed packages that simplify the connection and data retrieval process.

This article covers connecting KoboToolbox data to R using direct API requests and community-developed R packages, along with retrieving and updating project data.

## Using the KoboToolbox API in R

The KoboToolbox API allows external applications, including R, to access project data. By connecting R to the API, you can:
* Retrieve project submissions directly into R for analysis.
* Filter submissions based on specific conditions.
* Combine KoboToolbox data with other datasets.
* Automate data retrieval for recurring reports and analyses.
* Work with repeat group data, multilingual forms, and geographic data using compatible R packages.

### Choosing a connection method
There are two main approaches to connecting R to the KoboToolbox API:
* **Direct API requests:** Use R packages to send requests to the KoboToolbox API data endpoint and process the returned JSON data. This approach provides greater control over how data is retrieved and processed but requires more programming knowledge.
* **Community-developed R packages:** Use packages specifically designed to work with KoboToolbox, such as `robotoolbox` or `KoboconnectR`. These provide functions for connecting to the API and retrieving data with fewer lines of code.

Both approaches use the data endpoint of the KoboToolbox API and require appropriate access to your project data.

<p class="note">
  For more information about the data endpoint of the KoboToolbox API, see <a href="https://support.kobotoolbox.org/data_endpoint.html">Using the API data endpoint</a>.
</p>

### Preparing the connection

To connect R to KoboToolbox, you will typically need:
* **Server URL:** The web address of the KoboToolbox server where your account is hosted.
* **API key:** A personal authentication token that allows R to access KoboToolbox through the API.
* **Project asset UID:** A unique identifier for the KoboToolbox project you want to access.

<p class="note">
  For instructions on finding these details, see <a href="https://support.kobotoolbox.org/api.html">Getting started with the API</a>.
</p>

You will also need R installed on your computer. You can use R directly or through an integrated development environment such as RStudio.

<p class="note">
  <strong>Note:</strong> Keep your API key confidential. Avoid including it in scripts that may be shared publicly. You can store your credentials in an <code>.Renviron</code> file and access them through environment variables in R.
</p>

## Connecting to R using direct API requests

You can retrieve KoboToolbox project data using R packages that support HTTP requests and JSON processing.

For example:
* `httr` allows R to send requests to the KoboToolbox API.
* `jsonlite` converts JSON responses into data structures that can be processed in R.

This approach is useful when you want more control over API requests, including authentication, filtering, and pagination.

### Installing the required packages

Open R or RStudio and install the packages:
```
install.packages(c("httr", "jsonlite"))
```

Then load them into your R session:

```
library(httr)
library(jsonlite)
```

### Retrieving project submissions

The KoboToolbox API data endpoint provides access to submissions in JSON format.

The following example connects to a KoboToolbox project and retrieves its submissions:

```
library(httr)
library(jsonlite)

# Configure your connection
api_url <- "https://kf.kobotoolbox.org/api/v2/assets/YOUR_ASSET_UID/data/"
token <- Sys.getenv("KOBOTOOLBOX_TOKEN")

# Send the API request
response <- GET(
  api_url,
  add_headers(Authorization = paste("Token", token)),
  query = list(format = "json")
)

# Check for errors in the API response (no output if successful)
stop_for_status(response)

# Convert the JSON response into R data
data <- fromJSON(
  content(response, as = "text", encoding = "UTF-8")
)

# View the submissions
head(data$results) 
```

Replace `YOUR_ASSET_UID` with your project asset UID and update the server URL if needed. The example retrieves the API key from an environment variable named `KOBOTOOLBOX_TOKEN`.

The `GET()` function sends the request to KoboToolbox, while `fromJSON()` converts the response into data that R can process.

<p class="note">
  <strong>Note:</strong> The data endpoint uses pagination, meaning that a single request may not return all submissions. On KoboToolbox's public servers, the default is 100 submissions per request, with a maximum of 1,000. For more information, see <a href="https://support.kobotoolbox.org/data_endpoint.html">Using the API data endpoint</a>.
</p>

### Retrieving all submissions with pagination

For projects containing more submissions than the limit per request, you can use a loop to retrieve data in batches.

The following example retrieves submissions until no additional pages remain:

```
library(httr)
library(jsonlite)

api_url <- "https://kf.kobotoolbox.org/api/v2/assets/YOUR_ASSET_UID/data/"
token <- Sys.getenv("KOBOTOOLBOX_TOKEN")

start <- 0
limit <- 100
all_submissions <- list()

repeat {
  response <- GET(
    api_url,
    add_headers(Authorization = paste("Token", token)),
    query = list(
      format = "json",
      limit = limit,
      start = start
    )
  )

  stop_for_status(response)

  data <- fromJSON(
    content(response, as = "text", encoding = "UTF-8"),
    simplifyVector = FALSE
  )

  all_submissions <- c(all_submissions, data$results)

  cat("Fetched", length(data$results),
      "records (start =", start, ")\n")

  # Stop when the page is empty or contains fewer records than the limit
  if (n == 0 || n < limit) break

  start <- start + limit
}

cat("Total submissions:", length(all_submissions), "\n")

head(data$results)
```

This script retrieves submissions in batches of 100, stores the results in a list, and continues until all available pages have been retrieved.

You can then process the collected records using R functions or other packages, depending on your analysis needs.

## Connecting to R using robotoolbox

The [robotoolbox](https://dickoa.gitlab.io/robotoolbox/) package is a community-developed R package designed to simplify access to the KoboToolbox API.

It provides functions for authenticating requests, retrieving submissions, and processing KoboToolbox data without manually constructing API requests or handling pagination.

The package also supports several KoboToolbox-specific features:
* **Multilingual forms:** Work with question and choice labels in different form languages.
* **Repeat groups:** Retrieve related submission tables while preserving their relationships.
* **Geographic data:** Process geopoint, geotrace, and geoshape responses for use with spatial analysis and mapping tools.
* **Additional data:** Access audit logs and media attachments through supported functions.

### Installing and configuring robotoolbox

To install `robotoolbox`, run:

```
install.packages("robotoolbox")
```

Load the package and configure your KoboToolbox connection:

```
library(robotoolbox)

kobo_setup(
  url = "https://kf.kobotoolbox.org",
  token = Sys.getenv("KOBOTOOLBOX_TOKEN")
)
```

Replace the server URL if your account is hosted on the European Union KoboToolbox Server or a private server.

The example retrieves your API key from an environment variable instead of including it directly in the script.

### Retrieving project submissions

Once connected, you can list the projects available to your account:

```
kobo_asset_list()
```

To select a specific project, use its asset UID:

```
asset <- kobo_asset("YOUR_ASSET_UID")
```

Then retrieve the submissions:

```
data <- kobo_data(asset)
```

For forms without repeat groups, the function returns the submissions as a data frame. For forms containing repeat groups, it returns related tables using the `dm` package.

To preview data returned as a data frame, use:

```
# View the main submissions
head(data)

# View a repeat group
head(data$household_members)
```

The `robotoolbox` package handles pagination automatically, allowing you to retrieve submissions from larger projects without manually requesting each batch.

### Filtering submissions

You can also use `robotoolbox` to retrieve submissions that meet specific conditions.

For example, if your form contains a question named `region`, the following code retrieves submissions where the response is `north`:

```
filtered_data <- kobo_data(
  asset,
  query = '{"region": "north"}'
)
```

This applies the filter through the API before retrieving the data.

<p class="note">
  For more information about the available functions, see the <a href="https://dickoa.gitlab.io/robotoolbox/">robotoolbox documentation</a>.
</p>

## Other R packages for KoboToolbox

Several community-developed R packages provide additional options for retrieving and analyzing KoboToolbox data:
* [KoboconnectR:](https://asitav-sen.github.io/KoboconnectR/) Provides functions for retrieving KoboToolbox project data directly into R, including options for working with submission data and exports.
* [koboloadeR:](https://unhcr.github.io/koboloadeR/docs/) Developed by UNHCR to support survey data processing and analysis. It includes tools for working with repeat groups, preparing datasets, and generating statistical reports and visualizations.

<p class="note">
  <strong>Note:</strong> These packages are independently developed and maintained. Their features, installation requirements, and compatibility may change over time. Refer to each package's documentation for the latest instructions.
</p>

## Updating your data in R

Once connected to the KoboToolbox API, you can retrieve updated project data by running your R script again.

You can also schedule scripts to run at regular intervals to support recurring analyses and reports. For example, an automated workflow could retrieve new submissions daily, process the data, and update an analysis or visualization.

The frequency of updates depends on how the script is configured. KoboToolbox does not automatically send updated submissions to R through the data endpoint.

For more advanced workflows, you can use API filters to retrieve only submissions that meet specific conditions, rather than requesting the full dataset each time.


