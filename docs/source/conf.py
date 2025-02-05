# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from docutils import nodes
from docutils.parsers.rst import roles, directives
from sphinx.application import Sphinx
import argparse
import os

project = "elara protocol"
toc_title ="elara protocol"
copyright = '2025, chinchalinchin industries'
author = 'Grant Moore'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.graphviz',
    'sphinx_toolbox.collapse',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_design'
]

templates_path = [ ]

html_static_path = [ 
    '_static',
    '_static/css',
    '_apps'
]

html_css_files = [
    'custom.css'
] 

exclude_patterns = [
    '_apps/**',
    '_notes/**'
]

plot_html_show_source_link = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'

html_theme_options = { }

html_title = "elara protocol"

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
\usepackage[utf8]{inputenc} 
\usepackage{lmodern}
\usepackage{runic}
"""

latex_elements = {
    'preamble': latex_preamble,
    'inputenc': '\\usepackage[utf][inputenc]'
}

# -- Theme configuration -----------------------------------------------------

def build_pdf(source_dir, output_dir, filename):
    """
    Builds a PDF from a single RST file using Sphinx.

    Args:
        source_dir: The directory containing the RST file.
        output_dir: The directory to write the PDF to.
        filename: The name of the RST file (without the .rst extension).
    """
    # Calculate the correct confdir
    conf_dir = os.path.dirname(os.path.abspath(__file__)) 

    # Pass confdir to Sphinx initialization
    app = Sphinx(
      srcdir=source_dir, 
      confdir=conf_dir,  # Use the calculated confdir
      outdir=output_dir, 
      doctreedir=output_dir + '/doctrees',
      buildername='latexpdf', 
      warningiserror=False
    )
    app.build(force_all=True, filenames=[filename + '.rst'])

def center_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.paragraph(text=text)
    node['classes'].append('center')  # Add the CSS class to the <p> tag
    return [node], []

def center_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    # Create a paragraph node (<p>)
    node = nodes.paragraph(text='')
    node['classes'].append('center')

    # Create a nested paragraph with the content
    content_node = nodes.paragraph(text=''.join(content))
    node += content_node  # Add the content node as a child of the main node

    # This is the key change: remove the state_machine.view_list() call
    return [node]  

def setup(app: Sphinx):
    directives.register_directive('center', center_directive)
    roles.register_local_role('center', center_role)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-src", required=True, help="Path to the source RST file")
    args = parser.parse_args()

    source_file = args.src
    source_dir = os.path.dirname(source_file) 
    filename = os.path.splitext(os.path.basename(source_file))[0] 
    output_dir = os.path.join(source_dir, "out")

    build_pdf(source_dir, output_dir, filename)