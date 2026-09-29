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

# Language and internationalization settings
language = 'en'
locale_dirs = ['../locales/']
gettext_compact = False

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
    'account-billing': 'sections/account-billing.html',
    'using-formbuilder': 'sections/using-formbuilder.html',
    'using-xlsform': 'sections/using-xlsform.html',
    'collecting-data': 'sections/collecting-data.html',
    'managing-projects': 'sections/managing-projects.html',
    'analyzing-data': 'sections/analyzing-data.html',
    'integrations': 'sections/integrations.html',
    'data-security-protection': 'sections/data-security-protection.html',
    'additional-resources': 'sections/additional-resources.html',
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
    'tabler-icons/tabler-outline.css',
    'tabler-icons/tabler-filled.css',
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

redirects = {"server": "creating_account.html",
            "acknowledge": "select_one_and_select_many.html",
             "activation_link": "creating_account.html#troubleshooting",
             "add_logo": "media.html",
             "adding_skip_to_matrix": "matrix_response.html#adding-skip-logic-to-a-question-matrix",
             "advanced_calculate": "calculations_xls.html",
             "archiving_projects": "managing_projects.html#archiving-and-deleting-projects",
             "audit_logging": "form_meta.html#audit-metadata-question",
             "calculations_constraints_matrix": "matrix_response.html#advanced-question-matrices",
             "collecting_signatures": "photo_audio_video_file.html#advanced-appearances",
             "data-offline": "data-collection-tools.html#offline-data-collection",
             "delete_project": "managing_projects.html#archiving-and-deleting-projects",
             "devices_for_data_collection": "kobocollect_on_android_latest.html#choosing-a-device-for-kobocollect",
             "enketo": "data_through_webforms.html",
             "excel_analyzer_guide": "analyzing-data.html",
             "export_gps": "mapping_gps.html#exporting-gps-data",
             "howto_edit_multiple_submissions": "editing_deleting_data.html",
             "howto_edit_single_submissions": "editing_deleting_data.html",
             "hxl": "question_options.html#hxl",
             "kobo_local_computer": "index.html",
             "kobo_your_servers": "index.html",
             "kobocollect-android": "data_collection_kobocollect.html",
             "lower_file_size": "photo_audio_video_file.html#parameters-for-media-questions",
             "new_form": "quick_start.html",
             "number_text_responses": "number_decimal_range.html",
             "overview_of_creating_a_project": "quick_start.html",
             "p_codes": "index.html",
             "photo_download": "managing_media_responses.html#downloading-media-files",
             "project_summary": "managing_projects.html",
             "public_collections_advanced_search": "using_public_collections.html#public-collections-advanced-search",
             "rating_ranking": "select_one_and_select_many.html",
             "record_validation": "viewing_validating_data.html#validating-your-data",
             "recovering_previous_formdata": "index.html",
             "responses_inside_question": "form_logic.html#question-referencing",
             "row_level_permissions": "managing_permissions.html",
             "software_architecture": "index.html",
             "stuck_in_pending": "export_download.html#troubleshooting",
             "text_and_note": "using-formbuilder.html",
             "troubleshooting_kobocollect": "data_collection_kobocollect.html#troubleshooting",
             "troubleshooting_webforms": "data_through_webforms.html#troubleshooting",
             "unique_serial_numbers": "calculations_xls.html#advanced-calculations",
             "user_specified_other": "skip_logic.html",
             "video_question_type": "photo_audio_video_file.html",
             "xls_url": "xlsform_with_kobotoolbox.html#importing-an-xlsform-via-url",
             "custom_format_web": "form_style.html",
             "alternative_enketo": "form_style.html"}
