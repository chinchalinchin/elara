# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'elara'
copyright = '2024, chinchalinchin'
author = 'chinchalinchin'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.imgmath',
    'sphinx_toolbox.collapse',
    'matplotlib.sphinxext.plot_directive'
]

templates_path = [ ]

exclude_patterns = [ ]

plot_html_show_source_link = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_static_path = [ '_static' ]

imgmath_latex_preamble = r'''
    
'''

# -- Theme configuration -----------------------------------------------------

html_theme_options = {
    "max_navbar_depth": 5
}
