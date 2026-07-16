# Working with submission data in the JSON API
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/master/source/api_submission_data.md" class="reference">16 Jul 2026</a>


The JSON endpoint returns your submissions as structured data that scripts and applications can process record by record. This article describes how that JSON is shaped and how it behaves over time, so you can build integrations that stay correct when submissions are added, edited, validated, or deleted.

This article assumes you already have your server URL, API Key, and project asset UID. If not, start with [Getting started with the API](api.md). If you want a ready-made CSV or XLSX file instead of JSON, see [Using the API for synchronous exports](synchronous_exports.md).

This article includes:

-   [The data endpoint](#the-data-endpoint)
-   [System fields in the submission JSON](#system-fields-in-the-submission-json)
-   [Where the data keys come from](#where-the-data-keys-come-from)
-   [How each question type appears in the JSON](#how-each-question-type-appears-in-the-json)
-   [Filtering, sorting, and selecting fields](#filtering-sorting-and-selecting-fields)
-   [Paging through large projects](#paging-through-large-projects)
-   [What changes when a submission is edited](#what-changes-when-a-submission-is-edited)
-   [Repeat groups in the JSON](#repeat-groups-in-the-json)
-   [Form versions and older submissions](#form-versions-and-older-submissions)

## The data endpoint

Submission data lives at:

`https://[server-url]/api/v2/assets/[project asset UID]/data/?format=json`

The response is an envelope with a `count`, links to the `next` and `previous` pages, and the submissions themselves in `results`. A single submission can be fetched at `/data/[id]/`, where `[id]` is either the integer `_id` or the submission's `rootUuid`. For the v1-to-v2 endpoint changes and basic paging loops in Python and R, see [Migrating from v1 to v2 API](migrating_api.md).

<p class="note">
    <strong>Note:</strong> The interactive reference at <code>https://[server-url]/api/v2/docs/</code> lists every endpoint and its parameters, and lets you test requests in the browser.
</p>

## System fields in the submission JSON

Next to your form's questions, each record in `results` carries fields that KoboToolbox generates. The most commonly used ones (`_id`, `_uuid`, `meta/rootUuid`, `_submission_time`, `_submitted_by`, `__version__`) are described in [Viewing and validating your data](https://support.kobotoolbox.org/viewing_validating_data.html#system-generated-submission-fields). The JSON contains a few more:

| **Field**            | **What it holds**                                          |
| :------------------- | :--------------------------------------------------------- |
| `meta/instanceID`    | The identifier of this version of the record, as `uuid:...`. Matches the current `_uuid`. |
| `meta/deprecatedID`  | Only present after a record has been edited: the `_uuid` the record had before its latest edit. |
| `meta/rootUuid`      | The JSON path of the field shown as `rootUuid` in the data table and exports. Stays the same for the life of the record. |
| `_validation_status` | An object, not a label: `{"timestamp": 1752666000, "uid": "validation_status_approved", "by_whom": "username", "label": "Approved"}`. Empty (`{}`) when no status is set. Exports show only the label. |
| `_attachments`       | A list with one entry per media file: download and thumbnail URLs, the file name, and the attachment's own `id` and `uid`. |
| `_geolocation`       | A `[latitude, longitude]` pair taken from the record's geopoint question, or `[null, null]` if there is none. |
| `_status`            | Ingest status. In practice this is `submitted_via_web` for nearly all records. |
| `formhub/uuid`       | The internal identifier of the form the record was submitted against. |

Two things are worth knowing before you map these fields into a database:

- Treat `_uuid`, `meta/instanceID`, `meta/deprecatedID`, and `meta/rootUuid` as opaque strings. They usually look like a standard 36-character UUID (with a `uuid:` prefix on the `meta/` fields), but longer and differently shaped values exist in real projects. Reserve more room than 36 characters.
- `_tags` and `_notes` are not returned by the v2 data endpoint. You may still see them as columns in [exports](export_download.md).

## Where the data keys come from

Everything else in a record is keyed by your form's question names. To match those keys against the form definition, read the asset itself:

`https://[server-url]/api/v2/assets/[project asset UID]/?format=json`

The `content` object holds the survey rows and choice lists. (The project list at `/api/v2/assets/` leaves `content` out; request the single asset.) When you map survey rows to data keys, a few rules matter:

- A data key is the question's [Data Column Name](question_options.md), prefixed with the names of the groups it sits in: `group_name/question_name`. Group *labels* play no part in the key.
- Survey rows carry a `name`, and often a `$autoname` as well. When KoboToolbox generates or cleans up a name — for questions built without an explicit Data Column Name, and for most groups — the effective name is stored as `$autoname`. When both exist, `$autoname` is the one the data keys use, so read it first and fall back to `name`.
- Choice rows work the same way with `$autovalue` and `name`. The value stored in the data is the choice value, never the label. A select_multiple answer is a single string of choice values separated by spaces.
- A `label` on a survey or choice row is a list, not a string, with one entry per language in `content.translations` — the two are aligned by position. A project's unnamed default language appears in `translations` as `null`.

Three question types are stored in the asset in a compact form but arrive in the data under expanded keys that appear nowhere in the survey rows:

| **Question type** | **Data keys**                                             |
| :---------------- | :--------------------------------------------------------- |
| Rating            | One key per rated row: `[rating name]/[row name]`           |
| Ranking           | One key per rank position: `[ranking name]/[position name]` |
| Question Matrix   | One key per cell: `[matrix name]_[row name]/[matrix name]_[row name]_[column name]` |

If your script derives its expected fields from the survey rows alone, answers to these questions will look like unknown keys.

<p class="note">
    <strong>Note:</strong> The asset JSON also contains live counters such as <code>deployment__submission_count</code> that change with every incoming submission. If you cache the form definition and compare snapshots to detect form changes, compare the <code>content</code> object, not the whole asset.
</p>

## How each question type appears in the JSON

Two rules apply to every answer before the per-type details:

- **Answers are strings.** Submissions travel as XML text, so a Number question returns `"24"`, not `24`. Convert types on your side. (System fields are the exception: `_id` is a number and `_geolocation` is a list.)
- **Unanswered questions have no key.** A skipped question does not appear in the record at all — there is no `null` or empty string to find. Code that reads `record["question"]` directly will fail on the first skipped answer.

With that, the value each [question type](question_types.md) produces:

| **Question type**     | **What the value looks like**                              |
| :-------------------- | :---------------------------------------------------------- |
| Select One            | The choice value: `"yes"`                                    |
| Select Many           | Choice values separated by spaces, in one string: `"carpentry welding"` |
| Text                  | The entered text                                             |
| Number                | `"24"`                                                       |
| Decimal               | `"3.5"`                                                      |
| Date                  | `"2026-05-01"`                                               |
| Time                  | An ISO 8601 time, usually with a timezone offset: `"09:30:00.000+02:00"`. Sub-second precision and the offset format depend on the collection app. |
| Date & time           | `"2026-05-01T09:12:00.000+02:00"`, with the same variation as Time |
| Point                 | Latitude, longitude, altitude, and accuracy in one space-separated string: `"31.9539 35.9106 720.5 4.2"`. Altitude and accuracy can be absent — expect two to four values. |
| Line / Area           | A series of points in the same format, separated by semicolons |
| Photo / Audio / Video / File | The file name: `"my_photo-12_53_17.jpg"`. The file itself is listed in `_attachments`; match the value against each attachment's `media_file_basename` (its `filename` field holds the full storage path). |
| Barcode / QR Code     | The scanned text                                             |
| Note                  | Nothing — notes collect no answer and produce no key         |
| Acknowledge           | `"OK"` when ticked                                           |
| Rating                | One key per rated row (see the table above), each holding a scale choice value |
| Question Matrix       | One key per cell (see the table above), each holding a value of the cell's own type |
| Ranking               | One key per rank position (see the table above), each holding an item's choice value |
| Calculate             | The computed result, as text — see [Calculate questions](calculate_questions.md) |
| Hidden                | The stored value, as text                                    |
| Range                 | `"7"`                                                        |
| Select One from File / Select Many from File | Same as Select One / Select Many, with values from the uploaded file |

## Filtering, sorting, and selecting fields

The data endpoint accepts three query parameters that all take JSON:

| **Parameter** | **Example**                                 | **Effect**                                   |
| :------------ | :------------------------------------------ | :------------------------------------------- |
| `query`       | `query={"_submission_time": {"$gt": "2026-01-01"}}` | Return only matching records. MongoDB operators such as `$gt`, `$lt`, `$in`, `$and`, and `$or` are supported. |
| `sort`        | `sort={"_id": 1}`                           | Order results ascending (`1`) or descending (`-1`) by a field. |
| `fields`      | `fields=["_id", "_uuid", "group1/question1"]` | Return only the listed fields for each record. |

Remember to URL-encode the JSON when calling from code. Querying on your own question fields works too — use the full path including group names, exactly as the field appears in the JSON.

## Paging through large projects

On the official KoboToolbox servers, the data endpoint returns at most 1,000 records per request (self-hosted servers can configure a different cap). Asking for more with `limit` does not fail; the value is quietly reduced to the cap. To read a full project, follow the `next` link in the envelope until it is `null`.

The `next` link pages with `start` offsets, and offsets have a catch: they count positions in the result list, not records. If submissions are deleted while your loop is running, records slide backwards into positions your loop has already passed, and you never see them. For a nightly job on a project where nobody deletes data mid-run, this rarely matters. For long-running reads on busy projects, page by `_id` instead:

1. Sort by `_id` ascending: `sort={"_id": 1}`
2. Fetch a page, remember the highest `_id` you received
3. Request the next page with `query={"_id": {"$gt": [highest id]}}`
4. Stop when a page comes back with fewer records than you asked for

Each request then defines its position by the data itself. Deletions and new submissions cannot shift records in or out of pages you have already read.

## What changes when a submission is edited

Records do not stay still after collection. Answers get corrected, validation statuses get set, and attachments get removed. Each action changes the JSON differently:

| **Action**                    | **Changes in the JSON**                                                     | **Stays the same**            |
| :---------------------------- | :--------------------------------------------------------------------------- | :----------------------------- |
| Answers edited                | `_uuid` and `meta/instanceID` get a new value; `meta/deprecatedID` now holds the previous `_uuid`; the edited answers | `_id`, `meta/rootUuid`, `_submission_time` |
| Validation status set/changed | The `_validation_status` object                                              | Everything else                |
| Attachment deleted or replaced | The `_attachments` list                                                      | Everything else                |
| Submission deleted            | The record disappears from the endpoint                                      | —                              |

There is no "last modified" timestamp in the JSON. `_submission_time` records when the server first received the record and never changes afterwards, no matter how often the record is edited. A script that filters on `_submission_time` fetches new records but silently misses every edit.

<p class="note">
    <strong>Note:</strong> For how editing behaves in the web interface, and which fields the data table shows for edited records, see <a href="https://support.kobotoolbox.org/editing_deleting_data.html" class="reference">Editing and deleting data</a>.
</p>

## Repeat groups in the JSON

In exports, repeat groups become separate sheets joined by `_index` and `_parent_index`. The JSON has no such columns; a repeat group appears inside its parent record as a list, and the parent gains a `[repeat name]_count` field:

```json
{
  "_id": 4711,
  "family_name": "Ali",
  "household_members_count": "2",
  "household_members": [
    {"household_members/member_name": "Amal", "household_members/member_age": "3"},
    {"household_members/member_name": "Omar", "household_members/member_age": "7"}
  ]
}
```

Order within the list is the order in which the repeats were filled in. If you flatten repeats into their own database table, generate your own row numbers from the list position — and use `_id` as the parent key, not `_index`, which only exists in exports and [should not be used as a stable identifier](export_download.md).

To read about repeat groups in general, see [Grouping questions and repeating groups](group_repeat.md); for working with them in exports, see [Managing repeat group data](managing_repeat_groups.md).

## Form versions and older submissions

`__version__` identifies the form version a record was last submitted or edited with. Older records do not always carry it, and some store it under variant names such as `_version_`. The versions themselves are listed at:

`https://[server-url]/api/v2/assets/[project asset UID]/versions/`

Each version's detail page (`/versions/[version uid]/`) carries its own `content`, so a record can be interpreted against the exact form version its `__version__` names rather than the current one. The version list itself may omit `content`; request the single version.

Two behaviours surprise people who process data across redeployments:

- **Records can contain fields no current form version has.** If a question is removed, or its Data Column Name is renamed, old records keep the old field. A script that derives its column list from the current form definition will drop that data. Derive your columns from the data you actually receive, or from all versions.
- `date_deployed` on a version can be the boolean `false` rather than a date, when that version was never deployed.

For recovering data from earlier form versions in exports, see the "Include fields from all versions" option described in [Advanced export options](advanced_export.md).
