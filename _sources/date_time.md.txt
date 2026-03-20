# Date and time questions in KoboToolbox
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/04d161b3ce12a8f18d4145536cbba7c2fa3149ae/source/date_time.md" class="reference">20 Mar 2026</a>

Date and time questions are used to collect temporal information such as event dates, appointment times, or timestamps. These question types ensure that responses are **captured in a standardized format**, which supports accurate sorting, filtering, calculations, and analysis.

This article explains the available date and time question types, how to add them in the Formbuilder, the appearance options you can apply, and platform-specific display differences to consider during data collection.

## Date and time question types

The following question types are available in the Formbuilder for respondents to enter dates and times:

| Question type | Description |
|:---|:---|
| <i class="k-icon-qt-date"></i> Date | Captures a specific calendar date, typically in the format of day, month, and year. |
| <i class="k-icon-qt-text"></i> Time | Captures a specific time in hours and minutes. |
| <i class="k-icon-qt-date-time"></i> Date & time | Captures both a date and a time in a single combined response. |

## Adding date and time questions in the Formbuilder

To add date and time questions to your form:

1. Click the + button. 
2. Enter your question label.
3. Click <i class="k-icon-plus"></i> **ADD QUESTION.**
4. Choose the appropriate question type. 

![Date time question](images/date_time/date_time.png)

## Appearances of date and time questions

The table below displays the default appearances for date and time questions:

![Date time questions in Enketo vs KoboCollect](images/date_time/table.png)

### Advanced appearances

You can apply advanced appearances to **Date** and **Date & time** questions to modify how they display and behave in your form. 

To add an advanced appearance:

1. Open the question settings by clicking <i class="k-icon-settings"></i> **Settings** to the right of the question. This will take you to the **Question Options** tab.
2. In **Appearance (Advanced)**, choose the desired appearance.
    - If the appearance is not listed, select **other** and type the name of the appearance in the text box, exactly as written below.
    - For Date & time questions, type the name of the appearance directly in the **Appearance (Advanced)** text box.

![Date time question appearance](images/date_time/appearance.png)

The following advanced appearances are available for **Date** and **Date & time** questions:

| Appearance | Description | Compatibility |
|:---|:---|:---|
| <code>month-year</code> | Captures a month and a year (**Date** questions only).<br>![Month year](images/date_time/month-year.png) | Enketo and KoboCollect |
| <code>year</code> | Captures only a year (**Date** questions only).<br>![Year](images/date_time/year.png) | Enketo and KoboCollect |
| <code>no-calendar</code> (other) | Displays a spinner to select the day, month, and year, instead of the default calendar-style picker.<br>![No calendar](images/date_time/no-calendar.png) | KoboCollect only |
| <code>coptic</code> (other) | Displays the Coptic calendar.<br>![Coptic calendar](images/date_time/coptic.png) | KoboCollect only |
| <code>ethiopian</code> (other) | Displays the Ethiopian calendar.<br>![Ethiopian calendar](images/date_time/ethiopian.png) | KoboCollect only |
| <code>islamic</code> (other) | Displays the Islamic calendar.<br>![Islamic calendar](images/date_time/islamic.png) | KoboCollect only |
| <code>bikram-sambat</code> (other) | Displays the Bikram Sambat calendar.<br>![Bikram-sambat calendar](images/date_time/bikram-sambat.png) | KoboCollect only |
| <code>myanmar</code> (other) | Displays the Myanmar calendar.<br>![Myanmar calendar](images/date_time/myanmar.png) | KoboCollect only |
| <code>persian</code> (other) | Displays the Persian calendar.<br>![Persian calendar](images/date_time/persian.png) | KoboCollect only |
| <code>buddhist</code> (other) | Displays the Buddhist calendar.<br>![Buddhist calendar](images/date_time/buddhist.png) | KoboCollect only |
