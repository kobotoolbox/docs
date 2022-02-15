# User-Specified "Other" Responses for Multiple-Choice Questions

**Last updated:**
<a href="https://github.com/kobotoolbox/docs/blob/0dc2b1c2abdbd9df3155210e554f35dc6d1be2ed/source/user_specified_other.md" class="reference">14
Jun 2020</a>

Creating user-specified "Other" responses for multiple choice questions in one
step is a feature that is currently on KoboToolbox's development roadmap. In the
meantime, here's how to create them in your form manually using skip logic.

1. Add the desired question to your form as an ordinary multiple choice
   question. It can either be the "select one" (as shown here) or "select many"
   type.

    ![image](/images/user_specified_other/type.png)

2. Add a follow-up question of the "Text" type in which the respondent can
   manually specify their response when necessary.

    ![image](/images/user_specified_other/text.png)

    NOTE: If you are using the KoboCollect app for data collection, it's
    important not to display the second text question in a group on the same
    screen as it would not be visible otherwise. That's because KoboCollect only
    shows questions on the same screen that are relevant at the moment the
    screen is first displayed. Just make sure to put it outside of the group
    when choosing to display multiple questions on the same screen. (When using
    Enketo Webforms this isn't a problem as it dynamically shows questions once
    they become relevant.)

3. Add a [skip logic](skip_logic.md) to the previous follow-up question so it is
   only shown when needed.

    ![image](/images/user_specified_other/skip_logic.png)

4. Lastly, preview your form to ensure it behaves as expected.

    ![image](/images/user_specified_other/preview.png)
