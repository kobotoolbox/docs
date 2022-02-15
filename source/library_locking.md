# Library locking
**Last updated:** <a href="https://github.com/kobotoolbox/docs/blob/c2e8c882fdd831549c2f7f4474a9d522bafc181b/source/library_locking.md" class="reference">2 Dec 2021</a>

"Library locking" refers to the feature enabling various aspects of a survey to be "[locked](#locked)" when created from a template containing [locking attributes](#restrictions). All aspects of a form's editing are available to be locked through the assigning of "[locking profiles](#profile)" at the form, question or group level. These locking profiles can be assigned granular "[restrictions](#restriction)" that group together locking functionalities. Alternatively, the form can be fully locked down, preventing all aspects of editing.

<p class="note">Currently, only locking set within the XLSForm itself is supported, but will be incorporated into the formbuilder at some point in the future.</p>

This feature may be useful in a large, distributed team setting where a standard template is used, with some locked features, and each team can make necessary local adjustments for their needs. The creator of the template can continue to make updates, but the locks will restrict changes to specified aspects of the form for those who [create a project based on the template](new_form.md).

<p class="note">Locking aspects of a form is separate from <a class="reference" href="managing_permissions.html">managing permissions to a project</a> or <a class="reference" href="row_level_permissions.html">row-level access</a>.

## Restrictions

There are three levels of restrictions that can be set:
1. [Question](#question-level-restrictions),
2. [Group](#group-level-restrictions), and
3. [Form](#form-level-restrictions)

Additionally, there is a [`kobo--lock_all`](#id1) Boolean that can set in the `settings` sheet that will render the survey completely locked.

### `kobo--lock_all`

If `kobo--lock_all` is set to `True`, then all additional granular restrictions are redundant as the form is _fully_ locked down. If it is set to `False` _or_ omitted from the `settings` sheet, then defined locking profiles can be used to control the locked behaviour:

__settings__

| kobo--lock_all |
|----------------|
| true           |

The accepted values for `kobo--lock_all` are the same as in the `survey` sheet that [pyxform supports](https://github.com/XLSForm/pyxform/blob/43ea039250f44cff23b3ad10740fca54dfa12383/pyxform/aliases.py#L127-L142). No error will be thrown if an invalid value is used, only the form will not function as intended from the user's perspective.

<p class="note">Note that the restriction name, such as <code>choice_add</code> below, is <strong>predefined</strong> and only the restrictions listed below are valid options.</p>

### Question-level restrictions

| Name                       | Description                                                        |
|----------------------------|--------------------------------------------------------------------|
| `choice_add`               | Add new choices to a `select_*` question                           |
| `choice_delete`            | Remove an existing choice from a `select_*` question               |
| `choice_value_edit`        | Edit a choice `name`                                               |
| `choice_label_edit`        | Edit a choice `label`                                              |
| `choice_order_edit`        | Reorder the choices of a `select_*` question                       |
| `question_delete`          | Delete a given question                                            |
| `question_label_edit`      | Edit an existing `label` or `hint`                                 |
| `question_settings_edit`   | Edit a question's settings (other than `constraint` or `relevant`) |
| `question_skip_logic_edit` | Edit a question's skip logic settings (`relevant`)                 |
| `question_validation_edit` | Edit a question's validation criteria settings (`constraint`)      |

### Group-level restrictions

| Name                        | Description                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------|
| `group_delete`              | Delete group modal __Delete everything__ button (or delete group button if paired with `group_split`)  |
| `group_split`               | Delete group modal __Ungroup questions__ button (or delete group button if paired with `group_delete`) |
| `group_label_edit`          | Edit a group `label`                                                                                   |
| `group_question_add`        | Adding or cloning questions inside given group (children groups included)                              |
| `group_question_delete`     | Delete any question from given group (children groups questions included)                              |
| `group_question_order_edit` | Changing order of questions inside given group (children groups included)                              |
| `group_settings_edit`       | Changing __All group settings__ from given group __Settings__                                          |
| `group_skip_logic_edit`     | Changing __Skip Logic__ from given group __Settings__                                                  |

### Form-level restrictions

| Name                  | Description                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------|
| `form_appearance`     | Changing form appearance from __Layout & Settings__                                              |
| `form_replace`        | Replacing form using __Replace Form__ modal                                                      |
| `group_add`           | Button for grouping questions                                                                    |
| `question_add`        | Using __Insert cascading select__ option and each __Add Question__ and __Clone Question__ button |
| `question_order_edit` | Changing any questions order                                                                     |
| `language_edit`       | Edit languages in __Translations Modal__                                                         |
| `form_meta_edit`      | Edit meta questions from __Layout & Settings__                                                   |

## XLSForm configuration

There are three sheets where locking profiles are defined and set: `survey`, `settings` and [`kobo--locking-profiles`](#id2). The sheet of `kobo--locking-profiles` is not officially supported by [pyxform](https://github.com/XLSForm/pyxform) and is KoboToolbox-specific.

Form-level restrictions are defined in the `settings` sheet and question and group-level restrictions are defined in the `survey` sheet.

From within the `kobo--locking-profiles` sheet, all the locking profiles are defined in a matrix structure, using the keyword "[locked](#locked)" to assign a "[restriction](#restriction)" to a specific "[profile](#profile)". For example:

__kobo--locking-profiles__

Define the profiles and assign them restrictions. There is no limit on the number of profiles that can be defined (`profile_1`, ..., `profile_n`) but there are **only three** colours that differentiate their locking appearance in the formbuilder.

| restriction       | profile_1 | profile_2 | profile_3 |
|-------------------|-----------|-----------|-----------|
| choice_add        | locked    |           |           |
| choice_delete     |           | locked    |           |
| choice_label_edit | locked    |           |           |
| choice_order_edit | locked    | locked    |           |
| form_appearance   |           |           | locked    |

<p class="note">Note that not all valid restrictions need to be included in the <code>restriction</code> column, but an error will be thrown if an invalid restriction is included.</p>

__settings__

Set form-level restrictions and [`kobo--lock_all`](#id1) Boolean.

| kobo--locking-profile | kobo--lock_all |
|-----------------------|----------------|
| profile_3             | false          |

<p class="note">Note that omitting <code>kobo--lock_all</code> from the <code>settings</code> sheet is equivalent to setting it to <code>False</code>.</p>

__survey__

Set question and group-level restrictions.

| type                 | name    | label               | kobo--locking-profile |
|----------------------|---------|---------------------|-----------------------|
| select_one countries | country | Select your country | profile_1             |
| select_one cities    | city    | Select your city    | profile_2             |

__choices__

No restrictions can be set in the `choices` sheet.

| list_name | name      | label                    |
| ---       | ---       | ---                      |
| countries | canada    | Canada                   |
| countries | usa       | United States of America |
| cities    | vancouver | Vancouver                |
| cities    | toronto   | Toronto                  |
| cities    | baltimore | Baltimore                |
| cities    | boston    | Boston                   |

<i>This example XLSForm can be downloaded <a download class="reference" href="/_static/files/library_locking/library-locking-example.xlsx">here</a>.</i>

### Import locked XLSForms

Import your XLSForm as a `template` through the KoboToolbox UI by navigating to your __Library__ and clicking on __NEW__ and then __Upload__. Ensure that you select `template` from the __Choose desired type__ drop-down menu and then import your XLSForm.

![choose template type](/images/library_locking/import-template.png)

The locked template will now show in your library list view with a lock symbol.

![library list](/images/library_locking/library-list-view.png)

### Create project from locked template

Once a locked template has been added to your library -- either directly through importing an XLSForm as a template, creating a template based on a locked survey or adding a locked template from the public collections -- you can create a new project. In the __Projects__ section of the UI, click on __NEW__ and then __Use a template__.

![create project from template](/images/library_locking/create-project-from-template.png)

- Choose the locked template you want to use to create the new project.

![select template](/images/library_locking/select-template-for-new-project.png)

- From there, continue to create the project.

![create project](/images/library_locking/create-project.png)

When this example locked template is used to create a new project, the formbuilder will look like the following:

- The grayed out areas are those that have been disabled through the restrictions.

![overview](/images/library_locking/formbuilder.png)

- A dialogue box above the first question will show an overview of some of the form's restrictions.

![dialogue box](/images/library_locking/formbuilder-dialogue-box.png)

- Each question with locking profiles will display, in its settings, which restrictions have been set.

![question restrictions](/images/library_locking/formbuilder-question-settings.png)

- Some form-level settings will also be greyed out.

![form-level restrictions](/images/library_locking/form-style.png)

### Form validation

The following cases will currently throw a `FormPackLibraryLockingError`:
- If a locking profile name (column header in the `kobo--locking-profiles` sheet) is "locked" (the same as the locking keyword)
- If a restriction listed in `kobo--locking-profiles` is invalid (not in the list of [predefined restrictions](#restrictions))
- If there is a sheet called `kobo--locking-profiles` but no `restriction` column
- If no locking profiles are defined (column headers in the `kobo--locking-profiles` sheet)

<p class="note">Validation of the XLSForm library locking features will be expanded in the future.</p>

### Caveats

In some spreadsheet editors, two single dashes (`--`) are automatically converted to an m-dash (—), therefore making it difficult to type `kobo--` into a cell. We therefore convert all instances of n- and m-dashes into two single dashes (when prefixed with `kobo`). An XLSForm with the sheet name of "kobo—locking-profiles" will be converted to `kobo--locking-profiles` and similarly for the column headers.

## JSON representation

There are two attributes of the asset where locking information can be accessed and modified: `asset.summary` and `asset.content`.

If [`kobo--locking-profile`](#kobo-locking-profile) is a column name in the `survey` sheet, it will also be listed in the `asset.summary.columns` array.

In `asset.summary`, the following two Boolean attributes describe an overview of the form's locking structure:
- `lock_all`, and
- `lock_any`

The logic by which each of those Booleans are set is as follows:
- `lock_all` is `True` _only_ if `kobo--lock_all` is set to `True` in the `settings` sheet, otherwise it's `False`
- `lock_any` is set to `True` if _any_ of the following cases are `True`:
  - `lock_all` is `True`,
  - A `kobo--locking-profile` is set in the `settings` sheet, or
  - _At least one_ `kobo--locking-profile` is set in the `survey` sheet

In the example above, the following will be present in the `asset.summary`:

```
{
  ...,
  "columns": [
    ...,
    "kobo--locking-profile"
  ],
  "lock_all": false,
  "lock_any": true,
  ...
}
```

In `asset.content`, an attribute of `content.kobo--locking-profiles` exists as an array of JSON objects with the following structure:

```
[
  {
    "name": "profile_1",
    "restrictions": [
      "choice_add",
      "choice_label_edit",
      "choice_order_edit"
    ]
  },
  ...
]
```

In `content.settings`, the following will be present in a JSON object:

```
{
  "kobo--locking-profile": "profile_3",
  "kobo--lock_all": false
}
```

And finally in `content.survey`, each question that has been assigned a locking profile will have a `kobo--locking-profile` attribute as follows:

```
[
  {
    "name": "country",
    "type": "select_one",
    ...
    "kobo--locking-profile": "profile_1"
  },
  {
    "name": "city",
    "type": "select_one",
    ...
    "kobo--locking-profile": "profile_2"
  },
  ...
]
```

## Locking profiles and asset types

Of the four asset types (`asset`, `template`, `question` and `block`), only `template`s and `survey`s handle library locking features and the locks are enforced _only_ on surveys. Practically, this means the following:

Assume an XLSForm containing valid locking features is imported:
- If imported as a `block`, then all traces of locking are excluded and/or stripped from the asset. This results in a `block` asset that will be equivalent to the same form uploaded without any locking features;
- If imported as a `survey` (imported through the __Projects__ section) or `template` then all locks are intact:
  - If, from within the formbuilder:
    - a question is added to the library, then all locks are stripped from the new `question` asset
    - a group of questions is added to the library as a `block`, then all locks are stripped
  - If a `template` is created _from_ the locked `survey` asset, then that `template` will inherit all the locks the `survey` had (but since it is a template, you are able to edit the contents in the formbuilder),
  - If a `survey` is created _from_ a locked `template`, the survey will inherit all the locks that the `template` had

| Original Asset Type | Process                 | Resulting Asset's Status |
|---------------------|-------------------------|--------------------------|
| `survey`            | -                       | locked                   |
| `survey`            | `survey` to `template`  | locked                   |
| `survey`            | `survey` to `question`  | not locked               |
| `survey`            | `survey` to `block`     | not locked               |
| `template`          | -                       | locked                   |
| `template`          | `template` to `survey`  | locked                   |
| `template`          | `template` to `question`| not locked               |
| `template`          | `template` to `block`   | not locked               |
| `block`             | -                       | not locked               |
| `block`             | import to `survey`      | not locked               |
| `block`             | import to `template`    | not locked               |
| `block`             | `block` to `question`   | not locked               |
| `question`          | -                       | not locked               |
| `question`          | import to `survey`      | not locked               |
| `question`          | import to `template`    | not locked               |
| `question`          | `question` to `block`   | not locked               |

## Terminology

#### `kobo--lock_all`

Attribute containing a Boolean value, set in the `settings` sheet and applies all locking restrictions to the form and all questions and groups (rendering granular locking profiles redundant).

#### `kobo--locking-profile`

Column name in the `survey` and `settings` sheets where the locking profile is assigned to a question or group (in `survey`) or to the form (in `settings`).

#### `kobo--locking-profiles`

Sheet name where restrictions are assigned to profiles.

#### `locked`

Keyword used to assign a restriction to a profile in the `kobo--locking-profiles` sheet.

#### Profile

The name assigned to a group of restrictions, defined in the `kobo--locking-profiles` sheet. It is assigned to questions and groups in the `survey` sheet and to the from in the `settings` sheet.

#### Restriction

A granular locking attribute that can be assigned to a profile and control the locking behaviour at the question, group or form level.

#### Unlocked

A form containing no locking attributes.

