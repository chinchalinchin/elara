# Session: Elara Project

`elara` is a personal project for archiving pieces of my writing. It uses Sphinx to render RestructuredText into HTML. The rendered pages are then uploaded to an S3 bucket on AWS that is served behind a CloudFront distribution.

- [elara.chinchalinchin.com](https://elara.chinchalinchin.com)

**Guidelines**

- Good code is key. All implementations should be linted and commented. If you notice a function, module or package without a good docstring, fix it. Always be on the look out for opportunities to refactor and reduce logical complexity. Before you generate a complex solution, ask yourself if the problem could be simplified by refactoring a data structure or adopting a simpler approach.
- Always approach problems from a functional perspective, i.e. break the problem up into the smallest chunks and modularize as much as possible. Adopt an "AGILE" mindset, i.e. deliver value iteratively, in discrete chunks. Do not be afraid to leave blocks of code unimplemented, or to add future TODOs, if the scope of their completion exceeds your current tasking.
- However, keep in mind: while generality and reusability is good, this should not come at the expense of readability. Do not commit a solution unless you think others can understand it.
- You may add any dependencies you require, but always ask yourself: is it really necessary and what is the cost? This is supposed to be a lightweight pipeline utility, not a massive application with a complicated dependency web.
- Avoid obtuse, nested logic for parsing, e.g. do not assemble an HTML string through elaborate parsing; use a data structure and template instead. 

**Directory**

```bash
(venv) gmoore@Grants-MacBook-Pro elara % tree --gitignore -I '.git' -a -L 4 /Users/gmoore/Home/lib/elara
/Users/gmoore/Home/lib/elara
├── .aiexclude
├── .etc
│   ├── .notes
│   │   ├── .etc
│   │   │   └── bio.rst
│   │   └── .tmp
│   │       ├── .analecta
│   │       ├── .epistemia
│   │       ├── .machina
│   │       ├── .ouevre
│   │       └── .theurgy
│   ├── .prompts
│   │   ├── _system-instructions.rst
│   │   ├── actor
│   │   │   └── philadelphia-accent.rst
│   │   ├── assistant
│   │   │   └── palindromics
│   │   ├── editor
│   │   │   ├── editorialize.rst
│   │   │   ├── historize.rst
│   │   │   ├── package
│   │   │   ├── profile.rst
│   │   │   └── world-build.rst
│   │   ├── genealogist
│   │   │   ├── _task_branch.rst
│   │   │   ├── _task_cousinify.rst
│   │   │   ├── _task_expand.rst
│   │   │   └── tree.rst
│   │   └── poet
│   │       └── rhyme-search.rst
│   └── .task
│       ├── .task.md.j2
│       ├── prompt.md
│       ├── task.md
│       └── task.py
├── .github
│   └── actions.yml
├── .gitignore
├── Makefile
├── README.md
├── cloud
│   └── main.tf
├── make.bat
├── requirements.txt
├── source
│   ├── 00_canon
│   │   ├── 00_resume.rst
│   │   ├── 01_gallery.rst
│   │   └── index.rst
│   ├── 01_epistemia
│   │   ├── 00_empiricus
│   │   │   ├── 00_radix.rst
│   │   │   ├── 01_datum.rst
│   │   │   ├── 02_tabula.rst
│   │   │   └── index.rst
│   │   ├── 01_linguisticus
│   │   │   ├── 00_lexicon.rst
│   │   │   ├── 01_dialectus.rst
│   │   │   ├── 02_verborum.rst
│   │   │   ├── 03_consonantia.rst
│   │   │   ├── 04_palindromos.rst
│   │   │   ├── 05_commentariat.rst
│   │   │   └── index.rst
│   │   ├── 02_metaphysicus
│   │   │   ├── 00_axiomata.rst
│   │   │   ├── 01_probatum.rst
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── 02_pedagogy
│   │   ├── assignments
│   │   │   ├── index.rst
│   │   │   ├── problems
│   │   │   └── projects
│   │   ├── distributions
│   │   │   ├── 00_bernoulli.rst
│   │   │   ├── 01_geometric.rst
│   │   │   ├── 02_binomial.rst
│   │   │   ├── 03_uniform.rst
│   │   │   ├── 04_normal.rst
│   │   │   └── index.rst
│   │   ├── foundations
│   │   │   ├── 00_history.rst
│   │   │   ├── 01_logic.rst
│   │   │   ├── 02_sets.rst
│   │   │   └── index.rst
│   │   ├── index.rst
│   │   ├── inference
│   │   │   ├── 00_introduction.rst
│   │   │   ├── 01_bias.rst
│   │   │   ├── 02_design.rst
│   │   │   ├── 03_hypotheses.rst
│   │   │   ├── 04_mean.rst
│   │   │   ├── 05_proportion.rst
│   │   │   ├── 06_variance.rst
│   │   │   └── index.rst
│   │   ├── probability
│   │   │   ├── 00_introduction.rst
│   │   │   ├── 01_combinatorics.rst
│   │   │   ├── 02_conditional.rst
│   │   │   ├── 03_random_variables.rst
│   │   │   └── index.rst
│   │   ├── statistics
│   │   │   ├── 00_graphs.rst
│   │   │   ├── 01_estimation.rst
│   │   │   ├── 02_correlation.rst
│   │   │   ├── 03_regression.rst
│   │   │   ├── 04_sampling.rst
│   │   │   ├── 05_confidence.rst
│   │   │   └── index.rst
│   │   └── technology
│   │       ├── calculator
│   │       ├── index.rst
│   │       └── python
│   ├── 03_theurgy
│   │   ├── 01_palindromics
│   │   │   ├── appendices
│   │   │   ├── index.rst
│   │   │   ├── introduction
│   │   │   ├── section-i
│   │   │   ├── section-ii
│   │   │   ├── section-iii
│   │   │   └── section-iv
│   │   ├── 02_poetics
│   │   │   ├── 00_introduction.rst
│   │   │   ├── 01_rhymation.rst
│   │   │   ├── 02_metrics.rst
│   │   │   ├── 03_schemas.rst
│   │   │   ├── 04_calculus.rst
│   │   │   ├── A0_provisional.rst
│   │   │   ├── A1_applications.rst
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── 04_machina
│   │   ├── 01_universalis
│   │   │   ├── exercises
│   │   │   ├── index.rst
│   │   │   ├── modules
│   │   │   └── plugins
│   │   ├── 02_simulacrum
│   │   │   ├── 00_overview.rst
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── 05_analecta
│   │   ├── 1996.rst
│   │   ├── 2014.rst
│   │   ├── 2015.rst
│   │   ├── 2016.rst
│   │   ├── 2021.rst
│   │   ├── 2022.rst
│   │   ├── 2023.rst
│   │   ├── 2024.rst
│   │   ├── 2025.rst
│   │   └── index.rst
│   ├── 06_oeuvre
│   │   ├── 2025
│   │   │   ├── abstracta
│   │   │   ├── ballads
│   │   │   ├── elegies
│   │   │   ├── ghazals
│   │   │   ├── imagistic
│   │   │   ├── index.rst
│   │   │   ├── odes
│   │   │   ├── pantoums
│   │   │   ├── roundels
│   │   │   ├── sonnets
│   │   │   ├── verse
│   │   │   └── villanelles
│   │   ├── 2026
│   │   │   ├── index.rst
│   │   │   ├── pantoums
│   │   │   └── verse
│   │   └── index.rst
│   ├── 07_fabula
│   │   ├── 01_magnum-opus
│   │   │   ├── .etc
│   │   │   ├── 000.rst
│   │   │   ├── appendices
│   │   │   ├── archives
│   │   │   ├── exegesis
│   │   │   └── index.rst
│   │   └── index.rst
│   ├── _extensions
│   │   ├── directives
│   │   │   ├── __pycache__
│   │   │   └── panels.py
│   │   └── roles
│   │       ├── __pycache__
│   │       ├── classes.py
│   │       └── widgets.py
│   ├── _scripts
│   │   ├── js
│   │   │   └── custom-icons.js
│   │   └── py
│   │       ├── atbash.py
│   │       ├── palindromics
│   │       ├── plots
│   │       ├── primes.py
│   │       ├── statistics
│   │       └── variance.py
│   ├── _static
│   │   ├── css
│   │   │   └── custom.css
│   │   ├── csv
│   │   │   ├── cultural
│   │   │   ├── economic
│   │   │   ├── historical
│   │   │   ├── linguistic
│   │   │   ├── previews
│   │   │   ├── scientific
│   │   │   └── solutions
│   │   ├── dot
│   │   ├── favicon.ico
│   │   ├── html
│   │   │   └── palindromes.html
│   │   ├── img
│   │   │   ├── chromeos
│   │   │   ├── context
│   │   │   ├── fabula
│   │   │   ├── icons
│   │   │   ├── linux
│   │   │   ├── math
│   │   │   ├── personal
│   │   │   ├── problems
│   │   │   ├── python
│   │   │   └── results
│   │   ├── json
│   │   │   └── statistics
│   │   ├── pdf
│   │   │   ├── otoet.pdf
│   │   │   └── worksheets
│   │   ├── rst
│   │   │   ├── _forms
│   │   │   └── _links.rst
│   │   ├── svg
│   │   │   ├── animations
│   │   │   ├── etc
│   │   │   ├── icons
│   │   │   └── logos
│   │   └── xml
│   │       └── etc
│   ├── _templates
│   │   ├── panels
│   │   │   ├── map.html.j2
│   │   │   └── rss.html.j2
│   │   └── widgets
│   │       ├── back.html.j2
│   │       └── share.html.j2
│   ├── conf.py
│   ├── index.rst
│   ├── robots.txt
│   └── rss.xml
└── upload.sh

127 directories, 126 files
```

- `source/_templates/widgets/*`: HTML templates for inline widgets.
- `source/_templates/panels/*`: HTML templates for panels.
- `source/_extensions/directives/panels.py`: Custom Sphinx directives for rendering HTML templates.
- `source/_extensions/roles/classes.py`: Custom Sphinx roles for injecting inline CSS classes.
- `source/_extension/roles/widgets.py`:  Custom Sphinx roles for rendering inline HTML templates.

## Files

## upload.sh

```bash
#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

S3_BUCKET=$ELARA_BUCKET
DISTRIBUTION_ID=$ELARA_DIST
DIRECTORY="build/html"
BUILD=false
INVALIDATE=false

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --bucket)
      S3_BUCKET="$2"
      shift 2
      ;;
    --src)
      DIRECTORY="$2"
      shift 2
      ;;
    --dist)
      DISTRIBUTION_ID="$2"
      shift 2
      ;;
    --build)
      BUILD=true
      shift
      ;;
    --invalidate)
      INVALIDATE=true
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

# Check if all required arguments are provided
if [ -z "$S3_BUCKET" ] || [ -z "$DIRECTORY" ] || [ -z "$DISTRIBUTION_ID" ]; then
  echo "Usage: $0 --bucket <s3_bucket_name> --src <directory> --dist <cloudfront_distribution_id> [--build]"
  exit 1
fi

# Perform the build if the --build flag is set
if $BUILD; then
  cd "$SCRIPT_DIR/"  # Change to the src directory
  if make clean && make html | grep -iE "ERROR|FAILED"; then
    echo "Build failed. Aborting deployment."
    exit 1
  fi
  cd "$SCRIPT_DIR"  # Change back to the original directory
fi

# Construct the full path to the directory
BUILD_DIR="$SCRIPT_DIR/$DIRECTORY"

aws s3 sync "$BUILD_DIR" "s3://$S3_BUCKET/" \
  --delete \
  --acl public-read

echo "Successfully copied contents of $TARGET_DIR to s3://$S3_BUCKET/"

# Invalidate the CloudFront cache.
if [ -n "DISTRIBUTION_ID" ] && $INVALIDATE; then 
    aws cloudfront create-invalidation \
        --distribution-id "$DISTRIBUTION_ID" \
        --paths "/*"
else
    echo "Skipping CloudFront invalidation."
fi

exit 0
```

## requirements.txt

```text
# Documentation dependencies
sphinx
sphinx-toolbox
sphinx-book-theme
sphinx_design
sphinx-sitemap
sphinx-carousel
sphinx-autobuild
sphinxcontrib-mermaid

# Pedagogy Dependencies
matplotlib-venn

# Palindromes dependencies
matplotlib
numpy
scipy
tk
nltk

# LLM dependencies
google-generativeai==0.8.3
Jinja2==3.1.5
requests==2.25.1

# Build Packages
rst2pdf
build
twine
```

## cloud/main.py

!!! note
  The pipeline is not currently used anywhere.

```hcl
terraform {
    backend "s3" {
        bucket                          = "cumberland-cloud-terraform-state"
        key                             = "web/elara/terraform.tfstate"
        region                          = "us-east-1"
    }
}

provider "aws" {
    region                              = "us-east-1"
}

locals {
    platform                            = {
        client                          = "CUMBERLAND CLOUD"
        environment                     = "PRODUCTION"
    }
    kms                                 = {
        aws_managed                     = true
    }
}

module "bucket" {
    source                              = "github.com/cumberland-terraform/storage-s3.git"
    
    platform                            = local.platform
    kms                                 = local.kms
    s3                                  = {
        purpose                         = "Hosting of static web content for the Elara Protocol website"
        suffix                          = "elara"
        website_configuration           = {
            enabled                     = true
        } 
    }
}

module "distribution" {
    source                              = "github.com/cumberland-terraform/network-cdn.git"
    
    platform                            = local.platform
    kms                                 = local.kms
    s3                                  = module.bucket.bucket[0]
    cdn                                 = {
        aliases                         = [ "elara.chinchalinchin.com" ]
        name                            = "elara"
    }

}

module "build" {
    source                              = "github.com/cumberland-terraform/orchestrate-build.git"

    platform                            = local.platform
 
    connection                          = {
        provider_type                   = "GitHub"
    }
    kms                                 = {
        aws_managed                     = true
    }
    pipeline                            = {
        source_stage                    = {
            action                      = {
                configuration           = {
                    FullRepositoryId    = "https://github.com/chinchalinchin/elara"
                    BranchName          = "pypi"
                }
            }
        }
    }
    secrets                             = [ "cumberland-cloud/pypi" ]
    suffix                              = "elara"
    topic                               = {
        emails                          = [ "chinchalinchin@gmail.com" ]
    }
}
```

## source/conf.py

```python
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

sys.path.insert(0, os.path.abspath('./_extensions/roles'))
sys.path.insert(0, os.path.abspath('./_extensions/directives'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks',
    'sphinx_toolbox.collapse',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_design',
    'sphinx_sitemap',
    'sphinxcontrib.mermaid',
    # Custom Directives Extensions
    'panels',
    # Custom Roles Extensions
    'widgets',
    'classes'
]

templates_path = [ ]

exclude_patterns = [
    '**/.etc/**',
    '**/.notes/**',
    '**/.drafts/**',
    '**/.prompts/**',
    '**/exc_*',
    '**/.*.rst',
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
```

---

## Task

I would like to create a custom directive for rendering a special type of TOC tree. An example of its use is given below,

```rst
.. book-tree:
    :max-depth: <depth>
    :caption: <caption>
    :width: <width>

    * - chapter-name-i
      - chapter-numeral-i
      - chapter-location-i
    * - chapter-name-ii
      - chapter-numeral-ii
      - chapter-location-ii
```

I would like this to render a "book-like" TOC tree, e.g. something like (this is approximated through text),

```text
chapter-name-i ........................ <a href="chapter-location">chapter-numeral-i</a>
chapter-name-ii ....................... <a href="chapter-location">chapter-numeral-ii</a>
```

The essential constraint of the custom TOC tree is the number of dots should expand or contract to the fit the size of the panel, and the right hand numerals should always be lined up.

The `max-depth` and `caption` arguments of the directive should perform the same function as the standard `toctree` directive.