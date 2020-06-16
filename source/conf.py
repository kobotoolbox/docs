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

project = 'KoBoToolbox'
copyright = '2020, KoBoToolbox'
author = 'KoBoToolbox'

# The full version, including alpha/beta/rc tags
# release = '1'


# -- General configuration ---------------------------------------------------

#fixing missing contents.rst file (https://stackoverflow.com/questions/56336234/build-fail-sphinx-error-contents-rst-not-found)
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = '_static/images/kobologo.svg'

# See: https://sphinx-rtd-theme.readthedocs.io
html_theme_options = {
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# We override all css, using a customized SASS sources from sphinx_rtd_theme
html_style = 'css/kobo_theme.css'

# # These paths are either relative to html_static_path
# # or fully qualified paths (eg. https://...)
# html_css_files = [
#     'css/custom.css',
# ]
# html_js_files = [
#     'js/custom.js',
# ]

# html_sidebars = {
#     "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
# }