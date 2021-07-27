## Overview

> Currently, only locking set within the XLSForm itself is supported, but will be incorporated into the form-builder at some point in the future.

"Library locking" refers to the feature enabling various aspects of a survey to be "[locked](#locked)" when created from a template containing [locking attributes](#restrictions). All aspects of a form's editing are available to be locked through the assigning of "[locking profiles](#profile)" at the form, question or group level. These locking profiles can be assigned granular "[restrictions](#restriction)" that group together locking functionalities. Alternatively, the form can be fully locked down, preventing editing of all aspects of the form.

## Restrictions

There are three levels of restrictions that can be set:
1. [Question](#question-level-restrictions),
2. [Group](#group-level-restrictions), and
3. [Form](#form-level-restrictions)

Additionally, there is a [`kobo--lock_all`](#id1) Boolean that can set in the `settings` sheet that will render the survey completely locked.

### `kobo--lock_all`

If `kobo--lock_all` is set to `True`, then all additional granular restrictions are redundant as the form is _fully_ locked down. If it is set to `False` _or_ omitted from the `settings` sheet, then defined locking profiles can be used to control the locked behaviour:

XXX

The accepted strings for the value of `kobo--lock_all` are the same as in the `survey` sheet that [pyxform supports](https://github.com/XLSForm/pyxform/blob/43ea039250f44cff23b3ad10740fca54dfa12383/pyxform/aliases.py#L127-L142). No error will be thrown if an invalid string is used, only the form will not function as intended from the user's perspective.

> Note that the restriction name, such as `choice_add` below, is **predefined** and only the restrictions listed below are valid options.

### Question-level Restrictions

XXX

### Group-level Restrictions

XXX

### Form-level Restrictions

XXX

## XLSForm Configuration

There are three sheets where locking profiles are defined and set: `survey`, `settings` and [`kobo--locking-profiles`](#id2). The sheet of `kobo--locking-profiles` is not officially supported by [pyxform](https://github.com/XLSForm/pyxform) and is KoBoToolbox-specific.

Form-level restrictions are defined in the `settings` sheet and question and group-level restrictions are defined in the `survey` sheet.

From within the `kobo--locking-profiles` sheet, all the locking profiles are defined in a matrix structure, using the keyword "[locked](#locked)" to assign a "[restriction](#restriction)" to a specific "[profile](#profile)". For example:

### `kobo--locking-profiles`

> Define the profiles and assign them restrictions. Note that not all valid restrictions need to be included in the `restriction` column, but a [`FormPackLibraryLockingError`](#formpacklibrarylockingerror) will be thrown if an invalid restriction is included.

XXX

### `settings`

> Set form-level restrictions and [`kobo--lock_all`](#id1) Boolean (note again that `kobo--lock_all` can be _omitted_ if it's intended to be `False`)

XXX

> Note that omitting `kobo--lock_all` from the settings sheet is the equivalent of setting it to `False`.

### `survey`

> Set question and group-level restrictions

XXX

### Form Validation

The following cases will currently throw a [`FormPackLibraryLockingError`](#formpacklibrarylockingerror):
- If a locking profile name (column header in the `kobo--locking-profiles` sheet) is "locked" (the same as the locking keyword)
- If a restriction is listed in the `kobo--locking-profiles` `restriction` column that is invalid (not in the list of predefined restrictions)
- If there is a sheet called `kobo--locking-profiles` but no `restriction` column
- If no locking profiles are defined (column headers in the `kobo--locking-profiles` sheet)

Validation of the XLSForm library locking features will be expanded in the future.

### Caveats

In some spreadsheet editors, two single dashes (--) are automatically converted to an m-dash (—), therefore making it difficult to type `kobo--` into a cell. All instances of n- and m-dashes are converted into two single dashes (when prefixed with `kobo`). Therefore an XLSForm with the sheet name of "kobo—locking-profiles" will be converted to "kobo--locking-profiles" and similarly for the column headers. When the form is exported from the UI, the new double-dash will be exported and therefore the original and exported XLSForms will not be identical.

## JSON Representation

There are two attributes of the asset where locking information can be accessed and modified: `asset.summary` and `asset.content`.

If [`kobo--locking-profile`](#kobo-locking-profile) is a column name in the `survey` sheet, it will also be listed in the `asset.summary.columns` array.

In the summary, the following two Boolean attributes describe an overview of the form's locking structure (and locking appearance in the list view in the UI):
- `lock_all`, and
- `lock_any`

The logic by which each of those Booleans are set is as follows:
- `lock_all` is `True` _only_ if `kobo--lock_all` is set to `True` in the `settings` sheet, otherwise it's `False`
- `lock_any` is set to `True` if _any_ of the following cases are `True`:
  - `lock_all` is `True`,
  - A `kobo--locking-profile` is set in the `settings` sheet, or
  - _At least one_ `kobo--locking-profile` is set in the `survey` sheet

In the example above, the following will be present in the `asset.summary`:

XXX

In the content, an attribute of `content.kobo--locking-profiles` exists as an array of JSON objects with the following structure:

XXX

And finally in `content.survey`, each question that has been assigned a locking profile will have a `kobo--locking-profile` attribute as follows:

XXX

## Locking Profiles and Asset Types

Of the four asset types (`asset`, `template`, `question` and `block`), only `template`s and `survey`s handle library locking features and the locks are enforced _only_ on surveys. Practically, this means the following:

Assume an XLSForm containing valid locking features is imported:
- If imported as a `block` (imported through the Library section), then all traces of locking are excluded and/or stripped from the asset.

This results in a `block` asset that will be equivalent to a form uploaded without any locking features;
- If imported as a `survey` (imported through the Projects section) or `template` (not yet supported) then all locks are intact:
  - If, from within the form-builder:
    - a question is added to the library, then all locks are stripped from the new `question` asset
    - a group of questions is added to the library as a `block` (not yet support), then all locks are stripped
  - If a `template` is created _from_ the locked `survey` asset, then that `template` will inherit all the locks the `survey` had,
  - If a `survey` is created _from_ a locked `template`, the survey will inherit all the locks that the `template` had

XXX

### Importing Locked XLSForms

Import as a template.

## Terminology

#### `FormPackLibraryLockingError`

The exception class [defined in FormPack](https://github.com/kobotoolbox/formpack/pull/238/files?file-filters%5B%5D=.py#diff-8d95cd08d33d1507c0f4f5836d1936da466e7fc5ddf6bcf127daaac7761505faR8-R9) that will be thrown in the event of a library-locking-specific error.

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

