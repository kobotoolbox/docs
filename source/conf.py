# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'KoboToolbox'
copyright = 'KoboToolbox'
author = 'KoboToolbox'

# The full version, including alpha/beta/rc tags
# release = '1'


# -- General configuration ---------------------------------------------------

#fixing missing contents.rst file (https://stackoverflow.com/questions/56336234/build-fail-sphinx-error-contents-rst-not-found)
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx_reredirects']

# MyST markdown parser configuration
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'alabaster'

html_sidebars = {
    '**': [
        'navigation.html',
    ]
}

html_additional_pages = {
    'getting-started': 'sections/getting-started.html',
    'creating-forms': 'sections/creating-forms.html',
    'collecting-data': 'sections/collecting-data.html',
    'managing-projects': 'sections/managing-projects.html',
    'computer-server': 'sections/computer-server.html',
    'new-1': 'sections/new-1.html',
    'new-2': 'sections/new-2.html',
    'new-3': 'sections/new-3.html',
}

html_theme_options = {
    'analytics_id': 'G-XXLRR9N1R5',
    'sidebar_collapse': True,
    'sidebar_includehidden': True,
    'show_relbar_bottom': True,
    'github_banner': False,
    'github_button': False,
    'travis_button': False,
    'fixed_sidebar': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# We override all css
# html_style = 'css/kobo_theme.css'

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'kpi-icons/k-icons.css',
    'css/kobo_theme.css',
]
html_js_files = [
    'js/breadcrumbs.js',
    'js/common.js',
    'js/custom_sections.js',
    'js/home_page_toc.js',
    'js/scrollto.js',
    'js/sidebar_toc.js',
    'js/smoothscroll-polyfill.js',
    'js/table-sheets.js',
]

html_favicon = 'images/index/favicon.png'

redirects = {"server": "creating_account.html"}
