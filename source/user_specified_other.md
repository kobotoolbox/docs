# User-Specified "Other" Responses For Multiple-Choice Questions

Creating user-specified "Other" responses for multiple choice questions in one step is a feature that is currently on KoBo Toolbox's development roadmap. In the meantime, here's how to create them in your form manually using skip logic.

1. Add the desired question to your form as an ordinary multiple choice question. It either be of type "select one" (as shown here) or "select many".

.. image:: /images/user_specified_other/type.png

2. Add a followup question of type "Text" in which the respondent can manually specify their response when necessary

.. image:: /images/user_specified_other/text.png

NOTE: If using KoBoCollect app for data collection it's important not to display the second text question in a group on the same screen as it would not be visible otherwise. That's because Collect only shows questions on the same screen that are relevant at the moment the screen is first displayed. Just make sure to put it outside of the group when choosing to display multiple questions on the same screen. (When using Enketo Webforms this isn't a problem as it dynamically shows questions once they become relevant.) 

3. Add `skip logic <https://intercom.help/kobotoolbox/en/articles/592366-adding-skip-logic-to-your-form>`_ to the follow-up question so it's only shown when needed.

.. image:: /images/user_specified_other/skip_logic.png

4. Lastly, preview your form to ensure it behaves as expected.

.. image:: /images/user_specified_other/preview.png
