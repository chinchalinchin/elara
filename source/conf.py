# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from sphinx.application import Sphinx
import argparse
import os
import sys 

project = "elara"
toc_title = "elara"
copyright = '2023 - 2026, chinchalinchin industries'
author = 'Grant Moore'

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('./_extensions/_roles'))
sys.path.insert(0, os.path.abspath('./_extensions/_directives'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinx.ext.extlinks',
    'sphinx_toolbox.collapse',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_design',
    'sphinx_sitemap',
    'sphinxcontrib.mermaid',
    "sphinx_carousel.carousel",
      # Custom Directives Extensions
    'share',
    'map',
    'rss',
    # Custom Roles Extensions
    'back',
    'redacted',
    'small',
    'tiny',
    'underline',
    'handwritten',
    'strike'
]

templates_path = [ ]

exclude_patterns = [
    '_notes/**',
    '_drafts/**',
    '_prompts/**',
    '**/exc_*',
    '**/_*.rst'
]

plot_html_show_source_link = True

rst_prolog = """
.. include:: /_static/rst/_links.rst
"""

# -- HTML Configuration -------------------------------------------------

html_baseurl = 'https://elara.chinchalinchin.com'
html_favicon = '_static/favicon.ico'
html_extra_path = ['robots.txt']
html_theme = 'sphinx_book_theme'
html_static_path = [ 
    '_static',
    '_scripts'
]
html_css_files = [
    'css/custom.css'
]
html_js_files = [
   'js/custom-icons.js'
]
html_theme_options = {
    "analytics": {
        "google_analytics_id": "G-BRG311ZM0P"
    },
    "icon_links": [
        {
            "name": "Docker",
            "url": "https://hub.docker.com/u/chinchalinchin",
            "type": "fontawesome",
            "icon": "fa-custom fa-docker"
        },{
            "name": "GitHub",
            "url": "https://github.com/chinchalinchin/",
            "type": "fontawesome",
            "icon": "fa-custom fa-github"
        },{
            "name": "PyPi",
            "url": "https://pypi.org/user/chinchalinchin/",
            "type": "fontawesome",
            "icon": "fa-custom fa-pypi"
        },{
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/grant-moore-674677353/",
            "type": "fontawesome",
            "icon": "fa-custom fa-linkedin"
        },{
            "name": "Facebook",
            "url": "https://www.facebook.com/grant.moore.125836/",
            "type": "fontawesome",
            "icon": "fa-custom fa-facebook"
        }
   ]
}
html_title = "elara"
html_context = {
   "default_mode": "dark"
}

# -- Latex configuration -----------------------------------------------------

latex_engine = 'xelatex'
latex_preamble = r"""
\usepackage{babel}
\babelprovide[import, main]{coptic} 
\usepackage{amssymb}
\usepackage{amsmath}
\usepackage{cancel}
\usepackage[utf8]{inputenc} 
\usepackage{lmodern}
\usepackage{runic}
\usepackage{textcomp}
\usepackage{accents}
\usepackage[american]{babel}
\usepackage{csquotes}
"""
latex_elements = {
    'preamble': latex_preamble,
    'inputenc': '\\usepackage[utf][inputenc]'
}
# -- matplotlib configuration ------------------------------------------------------------

plot_html_show_source_link = True

# -- Mermaid configuration ---------------------------------------------------------------

mermaid_d3_zoom = True
mermaid_fullscreen = True

# -- Sphinx Application configuration -----------------------------------------------------

def build_pdf(source_dir, output_dir, filename):
    """
    Builds a PDF from a single RST file using Sphinx.

    Args:
        source_dir: The directory containing the RST file.
        output_dir: The directory to write the PDF to.
        filename: The name of the RST file (without the .rst extension).
    """
    conf_dir = os.path.dirname(os.path.abspath(__file__)) 

    app = Sphinx(
      srcdir=source_dir, 
      confdir=conf_dir, 
      outdir=output_dir, 
      doctreedir=output_dir + '/doctrees',
      buildername='latexpdf', 
      warningiserror=False
    )
    app.build(force_all=True, filenames=[filename + '.rst'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-src", required=True, help="Path to the source RST file")
    args = parser.parse_args()

    source_file = args.src
    source_dir = os.path.dirname(source_file) 
    filename = os.path.splitext(os.path.basename(source_file))[0] 
    output_dir = os.path.join(source_dir, "out")

    build_pdf(source_dir, output_dir, filename)