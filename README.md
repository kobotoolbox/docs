# KoboToolbox user documentation

This repository contains all the user content of KoboToolbox's official documentation, available at https://support.kobotoolbox.org/.

## Before you open an issue…

Please note that the purpose of the issue tracker on this repository is to track work on the *technical infrastructure* of the documentation site. For requests related to the content of the documentation, please:
* Post in Zulip [#Kobo support docs](https://chat.kobotoolbox.org/#narrow/stream/64-Kobo-support-docs) if you are a member of the Kobo team
* Otherwise, please share your feedback through our [Community Feedback Form](https://ee-eu.kobotoolbox.org/x/OPizwor2)
* For support requests or bug reports, please post in the [Community Forum](https://community.kobotoolbox.org/c/support-article/29)

## Local installation

To build and test this documentation locally follow these steps:

Prerequisites:
* Python 3.10 or later (Python 3.13+ supported)
* git
* npm

1. Open terminal
2. Clone repository: `git clone https://github.com/kobotoolbox/docs.git`
3. Change into the cloned directory: `cd docs`
4. Build the theme if you made any changes to it: `npm install && npm start`
5. Create a virtual environment: `python -m venv koboenv`
6. Activate the virtual environment `source koboenv/bin/activate`
7. Install requirements `pip install -r requirements.txt`
8. Build the html files: `make html`
9. Open the index page in the browser: `open _build/html/index.html`

Note: if you have Python 3, you might need to use `python3` command instead of `python` (and `pip3` instead of `pip`).

Each commit to `master` is automatically built into production.

## Development

When you already did everything from "Local installation" succesfully and just need to come back and work a bit more on the project, please use `dev.sh` script from the root of the project.

## Internationalization

The documentation supports multiple languages. The structure is:

- `source/` - English content (default language)
- `locales/es/` - Spanish translations
- `locales/fr/` - French translations

### Building translated documentation

To build everything (English plus all translated locales) in one step:

```bash
make html-all
```

This builds English into `_build/html/` and each locale into `_build/html/<lang>`.

To build a single language on its own:

```bash
# Build English (default)
make html

# Build Spanish
sphinx-build -b html locales/es _build/html/es

# Build French
sphinx-build -b html locales/fr _build/html/fr
```

### Adding new translations

1. Create the translated file in `locales/[lang]/` with the same filename as the English version (e.g., `locales/es/new_article.md`)
2. Add the file to the corresponding `locales/[lang]/index.rst` toctree

### Translating UI elements (header, search, footer, etc.)

The article content lives in the `.md`/`.rst` files, but the surrounding
theme chrome — the header navigation, language picker, search box, feedback
prompt, footer, and homepage forum/academy sections — is translated directly
in the Jinja templates.

Each template that contains UI text defines a translation dictionary keyed by
language code and selects the entry for the page's language. Sphinx exposes
the current language as the `language` variable (set per locale in each
`conf.py`: `source/conf.py` is `en`, `locales/es/conf.py` is `es`,
`locales/fr/conf.py` is `fr`). The templates fall back to English when a
language is missing.

The templates that hold translatable strings are:

- `source/_templates/partials/header.html` — nav links + language picker labels
- `source/_templates/partials/search.html` — search heading, description, placeholder, button
- `source/_templates/partials/community_questions.html` — forum and academy sections
- `source/_templates/layout.html` — breadcrumb, "back to top", feedback prompt, footer

A typical block looks like this:

```jinja
{% set lang = language or 'en' %}
{% set translations = {
  'en': { 'heading': 'What do you need help with?' },
  'es': { 'heading': '¿Con qué necesitas ayuda?' },
  'fr': { 'heading': 'Comment pouvons-nous vous aider ?' }
} %}
{% set t = translations.get(lang, translations['en']) %}

<h1>{{ t.heading }}</h1>
```

**To update or correct a UI string:** edit the matching value in that
template's translation dictionary.

**To add a brand-new UI string:** add the key to every language in the
dictionary (English is required as the fallback) and reference it with
`{{ t.<key> }}` in the markup.

**To add a whole new language** (e.g. `de`):

1. Add the language code to `LOCALES` in the `Makefile`.
2. Create `locales/de/conf.py` with `language = 'de'`.
3. Add a `'de'` entry to the translation dictionary in each template listed
   above, and add the language to the picker in `header.html` (the
   `languages` list and the `current_label` map).
4. Translate the `locales/de/` content files as described in
   "Adding new translations".

### The language picker

The dropdown language picker is rendered in
`source/_templates/partials/header.html` and styled in
`sass_source/sass/_header.scss` (the `.language-picker__*` classes). It links
to the current page in each locale using relative paths, so it works from any
page depth. Remember to run `npm start` after changing the SCSS so the
compiled CSS in `source/_static/css/` is regenerated.

> Note: the homepage "Topics" heading uses a `.. rst-class:: topics-section`
> directive (instead of relying on the auto-generated `#topics` id) so the
> homepage grid styling survives translated headings such as "Temas" /
> "Sujets". Keep that directive when editing any locale's `index.rst`.

## Custom theme development

We build our theme atop [Read The Docs theme](https://sphinx-rtd-theme.readthedocs.io) by replacing their `CSS` with our own (which is a heavily modified copy of theirs).

To develop the theme:

1. Install NPM dependencies: `npm install`
1. Build:
  1. To watch for style changes use `npm run dev`
  1. To build the styles once use `npm start`

Useful links:

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - templating language used in `.html` files
- [Official Sphinx documentation](https://www.sphinx-doc.org)
- [Alabaster theme source code](https://github.com/bitprophet/alabaster)
- [Sphinx source code](https://github.com/sphinx-doc/sphinx)
- [Basic Sphinx theme source code](https://github.com/sphinx-doc/sphinx/tree/3.x/sphinx/themes/basic)
