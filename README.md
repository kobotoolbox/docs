# KoBoToolbox user documentation

This documentation is a work in progress while we transition over from our existing platform at [support.kobotoolbox.org](https://support.kobotoolbox.org).

Visit the work-in-progress support site [here](https://kobotoolbox-documentation.readthedocs.io/en/latest/). This page is updated automatically by Read the Docs based on the latest version of this repository.

## Local installation 

To build and test this documentation locally follow these steps: 

Prerequisites: 
* Python 3
* git

1. Open terminal
1. Clone repository: `git clone https://github.com/kobotoolbox/docs.git`
1. Change into the cloned directory: `cd docs` 
1. Create a virtual environment: `python -m venv koboenv`
1. Activate the virtual environment `source koboenv/bin/activate`
1. Build the html files: `make html`
1. Open the index page in the browser: `open _build/html/index.html`
1. Build and copy the html files into the `docs` folder with `make github` (if this is intended as a public update)