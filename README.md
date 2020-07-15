# KoBoToolbox user documentation

This documentation is a work in progress while we transition over from our existing platform at [support.kobotoolbox.org](https://support.kobotoolbox.org).

Visit the work-in-progress support site [here](https://kobotoolbox-documentation.readthedocs.io/en/latest/). This page is updated automatically by Read the Docs based on the latest version of this repository.

## Local installation 

To build and test this documentation locally follow these steps: 

Prerequisites: 
* Python 3
* git
* npm

1. Open terminal
1. Clone repository: `git clone https://github.com/kobotoolbox/docs.git`
1. Change into the cloned directory: `cd docs` 
1. Build the theme if you made any changes to it: `npm install && npm start`
1. Create a virtual environment: `python -m venv koboenv`
1. Activate the virtual environment `source koboenv/bin/activate`
1. Install requirements `pip install -r requirements.txt`
1. Build the html files: `make html`
1. Open the index page in the browser: `open _build/html/index.html`
1. Build and copy the html files into the `docs` folder with `make github` (if this is intended as a public update)

## Custom theme development

We build our theme atop [Read The Docs theme](https://sphinx-rtd-theme.readthedocs.io) by replacing their `CSS` with our own (which is a heavily modified copy of theirs).

To develop the theme:

1. Install NPM dependencies: `npm install`
1. Build:
  1. To watch for style changes use `npm run dev`
  1. To just build the styles use `npm start`
