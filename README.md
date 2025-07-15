# KoboToolbox user documentation

This repository contains all the user content of KoboToolbox's official documentation, available at https://support.kobotoolbox.org/.

## Before you open an issue…

Please note that the purpose of the issue tracker on this repository is to track work on the *technical infrastructure* of the documentation site. For requests related to the content of the documentation, please:
* Post in Zulip [#Kobo support docs](https://chat.kobotoolbox.org/#narrow/stream/64-Kobo-support-docs) if you are a member of the Kobo team
* Otherwise, please share your feedback through our [Community Feedback Form](https://ee-eu.kobotoolbox.org/x/OPizwor2)
* For support requests or bug reports, please post in the [community forum](https://community.kobotoolbox.org/c/support-article/29)

## Local installation

To build and test this documentation locally follow these steps:

Prerequisites:
* Python 3
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
