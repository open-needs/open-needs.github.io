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
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Open-Needs'
copyright = '2021, Open-Needs community'
author = 'Open-Needs community'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.plantuml",
    "sphinxcontrib.needs",
    "sphinx_panels",
    "sphinxcontrib.httpdomain",
    "sphinx_disqus.disqus",
    "sphinx_preview",
    "sphinx-jsonschema",
    "sphinx_data_viewer",
]

disqus_shortname = "open-needs-org"

preview_config = {
    # Each link on main body (article), but not if link is used for an image and
    # if link-target is github.com (does not allow iframe usage)
    "selector": "article p a:not(:has(>img),[href*='github.com'],[href*='githubusercontent'])",
    "not_selector": "div.needs_head a, h1 a, h2 a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "&nbsp;👁",
    "width": 500,
    "height": 400,
    "offset": {
        "left": 20,
        "top": 20
    },
    "timeout": 500,
}

local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml-1.2022.0.jar")
plantuml = f"java -jar {local_plantuml_path}"
plantuml_output_format = "svg_img"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'includes']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css'
]

html_title = 'Open-Needs'

html_logo = "_static/open-needs-logo.png"

html_theme_options = {
    "sidebar_hide_name": True,
    "announcement": "<em>Important:</em> This project is still in concept phase and most points are under discussion.",
}

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/open-needs-sidebar.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

html_extra_path = ['models']

