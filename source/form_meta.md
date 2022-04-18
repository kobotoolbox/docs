# Form Settings and Meta Questions

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/f9bb069f3517cb6d0b581aa7cec180b5ff707d2b/source/form_meta.md" class="reference">12
Aug 2021</a>

Form settings are optional advanced configurations of your form.

The `Form ID` is a unique name that every form must have to be valid. Later when
deploying your final form as a data collection project you must make sure to
have a unique name for your project. However, it's possible to still change that
name at that point.

Meta questions are hidden questions that can help you with your analysis later
on. Each of the meta questions will be included if ticked here. In detail, here
is what they stand for:

| Meta question   | Description                                                                  |
| :-------------- | :--------------------------------------------------------------------------- |
| Start Time      | Exact start date and time when starting the interview (timestamp)            |
| End Time        | Exact end date and time when finishing the interview                         |
| Today           | Day the interview is conducted                                               |
| Username        | The username of the enumerator if authentication is used for data collection |
| Audit           | Record an audit log while the survey is being completed                      |
| Device ID       | IMEI (International Mobile Equipment Identity)                               |
| Phone Number\*  | The cell phone number                                                        |
| SIM Serial\*    | SIM serial number                                                            |
| Subscriber ID\* | IMSI (International Mobile Subscriber Identity)                              |

<p class="note">These meta questions are relevant only to cell phones with a SIM card that have a phone number.</p>
