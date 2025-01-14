elara
=====

Directory Structure
-------------------

.. code-block:: bash

	/home/grant/Projects/elara/src/source/_apps/elara
	├── app
	│   ├── conf.py
	│   ├── data
	│   │   ├── context.rst
	│   │   └── persona
	│   │       ├── persona_axiom.rst
	│   │       └── persona_elara.rst
	│   ├── experiment.py
	│   ├── __init__.py
	│   ├── main.py
	│   ├── model.py
	│   ├── parse.py
	│   └── __pycache__
	│       ├── conf.cpython-312.pyc
	│       ├── experiment.cpython-312.pyc
	│       ├── model.cpython-312.pyc
	│       └── parse.cpython-312.pyc
	├── MANIFEST.ini
	├── __pycache__
	│   ├── experiment.cpython-312.pyc
	│   ├── model.cpython-312.pyc
	│   └── parse.cpython-312.pyc
	├── pyproject.toml
	├── README.md
	├── setup.cfg
	└── summary.rst

	6 directories, 21 files

summary.rst
-----------



MANIFEST.ini
------------

include README.md
recursive-include elara *.py
recursive-include data *.rst

README.md
---------

# elara

A Python package for interacting with Google's Gemini API.

## Installation

```bash
pip install elara
```

## Build

```bash
pip install build
python -m build
pip install dist/elara-0.1.0-py3-none-any.whl
```

## Usage 

```bash
elara chat -p "Hello Gemini!" 

elara conduct -e duality

elara summarize -d /path/to/directory
```

setup.cfg
---------

.. code:: toml

	[metadata]
	name = elara
	version = 0.1.0
	description = A Python package for interacting with Google's Gemini API.
	long_description = file: README.md
	long_description_content_type = text/markdown
	author = Grant
	author_email = your.email@example.com
	license = MIT
	classifiers =
	    License :: OSI Approved :: MIT License
	    Programming Language :: Python :: 3
	    Programming Language :: Python :: 3.8
	    Programming Language :: Python :: 3.9
	    Programming Language :: Python :: 3.10
	    Programming Language :: Python :: 3.11

	[options]
	packages = find:
	python_requires = >=3.8
	install_requires =
	    google-generativeai>=0.1.0
	    google-api-core>=2.17.1

	[options.extras_require]
	dev =
	    pytest

	[options.entry_points]
	console_scripts =
	    elara = elara.main:main

pyproject.toml
--------------

.. code:: toml

	[build-system]
	requires = ["setuptools>=43.0.0", "wheel"]
	build-backend = "setuptools.build_meta"

	[project]
	name = "elara"
	version = "0.1.0"
	description = "A Python package for interacting with Google's Gemini API."
	readme = "README.md"
	authors = [{name = "Grant"}]
	license = {text = "MIT"}
	requires-python = ">=3.8"

	dependencies = [
	    "google-generativeai>=0.1.0",
	    "google-api-core>=2.17.1"
	]

	[project.optional-dependencies]
	dev = [
	    "pytest"
	]

	[project.scripts]
	elara = "elara.main:main"

app/model.py
------------

.. code:: python

	""" # model.py
	Wrapper around Google's GenerativeAI library. Provides configuration and default settings.
	"""
	import conf 

	import google.generativeai as genai

	genai.configure(api_key=conf.API_KEY)

	def _model(model_type=conf.DEFAULTS["MODEL"]):
	    return genai.GenerativeModel(model_type)

	def reply(prompt, model_type=conf.DEFAULTS["MODEL"]):
	    return _model(model_type).generate_content(prompt).text

app/__init__.py
---------------

.. code:: python

	"""
	Package for interacting with generative AI models, conducting experiments, and parsing data.
	"""

app/parse.py
------------

.. code:: python

	""" # parse.py
	Module for formatting prompts and responses. It also handles context.
	"""
	import os
	import subprocess
	import textwrap

	import conf

	_personas = { } 

	def preamble(
	    persona = conf.DEFAULTS["PERSONA"]
	):
	    return _personas[f"persona_{persona}"]

	def init():
	    os.makedirs(conf.PERSONA_DIR, exist_ok=True)
	    for root, _, files in os.walk(conf.PERSONA_DIR):
	        for file in files:
	            if os.path.splitext(file)[1] not in  [".rst", ".md"]:
	                continue

	            file_path = os.path.join(root, file)

	            with open(file_path, "r") as f:
	                payload  = f.read()

	            _personas[os.path.splitext(file)[0]] = payload
	    return

	def prompt(text):
	    return f"\n.. admonition:: {conf.PROMPTER}\n\n\t{text}\n"

	def response(
	    text, 
	    persona=conf.DEFAULTS["PERSONA"]
	):
	    """Formats the model's response for RST.
    
	    This function now handles multiple newlines correctly.
	    """
	    # Indent each line individually
	    indented_lines = textwrap.indent(text, "\t").splitlines()
	    # Join with newline and add to directive

	    formatted_response = f".. admonition:: {persona}\n\n" + "\n".join(indented_lines) + "\n"
	    return formatted_response

	def persist(
	    raw_prompt, 
	    raw_response, 
	    context_file=conf.DEFAULTS["CONTEXT"], 
	    persona=conf.DEFAULTS["PERSONA"]
	):
	    """Appends the prompt and response to the context file."""

	    # Create context if file doesn't exist
	    if not os.path.exists(context_file):
	        with open(context_file, "w") as f:
	            f.write(preamble(persona) + "\n")  # Initialize with the preamble

	    context = prompt(raw_prompt) + "\n" + response(raw_response, persona)  # Removed extra newline

	    with open(context_file, "a") as f:
	        f.write(context)

	    return context

	def contextualize(
	    raw_prompt, 
	    context_file=conf.DEFAULTS["CONTEXT"], 
	    persona=conf.DEFAULTS["PERSONA"]
	):
	    """Appends the preamble and context to prompt."""

	    prefixed_prompt = ""

	    if os.path.exists(context_file):
	        with open(context_file, "r") as f:
	            context = f.read()
	        prefixed_prompt += preamble(persona) + context
	    prefixed_prompt += prompt(raw_prompt)

	    return prefixed_prompt

	def summarize(
	    directory=conf.DEFAULTS["SUMMARY"]
	):
	    """Summarizes the contents of a directory in an RST document."""
	    if not os.path.isdir(directory):
	        print(f"Error: '{directory}' is not a valid directory.")
	        return

	    output_file = os.path.join(directory, "summary.rst")
	    with open(output_file, "w") as f:
	        f.write(f"{os.path.basename(directory)}\n")  # Directory name as title
	        f.write("=" * len(os.path.basename(directory)) + "\n\n")  # Underline

	        # Generate directory tree using subprocess
	        f.write("Directory Structure\n")
	        f.write("-" * 19 + "\n\n")
	        f.write(".. code-block:: bash\n\n")
        
	        try:
	            # Added text=True for string output
	            tree_output = subprocess.check_output(
	                ["tree", "-n", directory], 
	                text=True
	            )
	            f.write(textwrap.indent(tree_output, "\t"))
	        except FileNotFoundError:
	            print("Error: The 'tree' command was not found. Please install it.")
	            return
	        except subprocess.CalledProcessError as e:
	            print(f"Error: The 'tree' command returned a non-zero exit code: {e.returncode}")
	            return
	        f.write("\n")

	        # Iterate through files and add their contents
	        for root, _, files in os.walk(directory):
	            for file in files:
	                # Filter file extensions
	                _, ext = os.path.splitext(file)
	                if ext not in conf.WHITELISTED_EXTS:
	                    continue

	                file_path = os.path.join(root, file)
	                relative_path = os.path.relpath(file_path, directory)

	                f.write(f"{relative_path}\n")
	                f.write("-" * len(relative_path) + "\n\n")

	                directive = ext in conf.SUMMARY["DIRECTIVES"].keys()

	                if directive:
	                    f.write(f"{conf.SUMMARY["DIRECTIVES"][ext]}\n\n")

	                with open(file_path, "r") as infile:
	                    content = infile.read()

	                    # Indent content for RST directives
	                    if directive:
	                        content = textwrap.indent(content, "\t")

	                    f.write(content)

	                f.write("\n\n")

	    print(f"Summary generated at: {output_file}")

app/experiment.py
-----------------

.. code:: python

	""" # experiment.py
	Module for performing experiments on LLMs.
	"""
	# Application Modules
	import conf
	import model 
	import parse

	# Standard Library Modules
	import time 
	import os

	# External Modules
	from google.api_core.exceptions import ResourceExhausted


	def conduct(
	    choice, 
	    model_type=conf.DEFAULTS["MODEL"]
	):
	    """Conducts an experiment based on the given choice."""
	    if choice == "duality":
	        _duality(model_type=model_type)

	def _duality(
	    max_cycles = 20, 
	    max_delay = 60, 
	    initial_prompt = conf.DEFAULTS["PROMPT"],
	    model_type = conf.DEFAULTS["MODEL"],
	    persona_a = conf.DEFAULTS["PERSONA"],
	    persona_b = conf.DEFAULTS["PERSONA"]
	):
	    """
	    Conducts the 'duality' experiment with exponential backoff,
	    separate error handling, and correct sleep placement.

	    Args:
	        max_cycles (int): The maximum number of cycles to run the experiment.
	        max_delay (int): The maximum delay (in seconds) for exponential backoff.
	        initial_prompt (str): The initial prompt to start the conversation.
	        model_type (str): The type of model to use (e.g., "gemini-pro").
	    """
	    context_A = parse.preamble(persona_a)
	    context_B = parse.preamble(persona_b)
	    cycle = 0
	    delay = 1  # Initial delay in seconds

	    # Initial interaction
	    response_A = model.reply(context_A + parse.prompt(initial_prompt), model_type)
	    context_A += parse.prompt(initial_prompt) + parse.response(response_A)

	    while cycle < max_cycles:
	        time.sleep(delay)  # Sleep at the beginning of the loop

	        # A talks to B
	        try:
	            response_B = model.reply(context_B + parse.prompt(response_A), model_type)
	            context_B += parse.prompt(response_A) + parse.response(response_B)
	        except ResourceExhausted as e:
	            print(e)
	            print(f"Rate limit hit for model B. Increasing delay to {delay * 2} seconds.")
	            delay = min(delay * 2, max_delay)
	            continue  # Skip to the next cycle


	        # B talks to A
	        try:
	            response_A = model.reply(context_A + parse.prompt(response_B), model_type)
	            context_A += parse.prompt(response_B) + parse.response(response_A)
	        except ResourceExhausted as e:
	            print(e)
	            print(f"Rate limit hit for model A. Increasing delay to {delay * 2} seconds.")
	            delay = min(delay * 2, max_delay)
	            continue  # Skip to the next cycle

	        cycle += 1
	        delay = 1  # Reset delay after a successful cycle

	    # Output to files
	    a_file = os.path.join(conf.DATA_DIR, "duality_context_A.txt")
	    b_file = os.path.join(conf.DATA_DIR, "duality_context_B.txt")

	    with open(a_file, "w") as f:
	        f.write(context_A)
	    with open(b_file, "w") as f:
	        f.write(context_B)

	    print('Duality experiment completed. Results saved to \n\n\t{a_file}\n\n and \n\n\t{b_file}]\n\n')


app/main.py
-----------

.. code:: python

	""" # main.py
	Module for command line parsing.
	"""

	import argparse

	import conf
	import experiment
	import model
	import parse


	def args():
	    parser = argparse.ArgumentParser(description="Interact with Gemini.")
	    for arg in conf.ARGUMENTS: 
	        if arg["mode"] == "name":
	            parser.add_argument(
	                arg["syntax"],
	                choices=arg["choices"], 
	                help=arg["help"]
	            )
	        elif arg["mode"] == "flag":
	            parser.add_argument(
	                *arg["syntax"], 
	                type=arg["type"],
	                default=arg["default"],
	                help=arg["help"]
	            )
	    args = parser.parse_args()
	    return args

	def chat(prompt, context, model_type=conf.DEFAULTS["MODEL"]):
	    """Chat with Gemini"""
	    parsed_prompt = parse.contextualize(prompt, context)
	    response = model.reply(parsed_prompt, model_type)
	    context = parse.persist(prompt, response, context)
	    return response

	def main():
	    """
	    Main function to run the command-line interface.
	    """
	    parse.init()
	    parsed_args = args()
	    if parsed_args.operation == "chat":
	        res = chat(parsed_args.prompt, parsed_args.context, parsed_args.model)
	        print(res)
	    elif parsed_args.operation == "conduct":
	        experiment.conduct(parsed_args.experiment)
	    elif parsed_args.operation == "summarize":
	        parse.summarize(parsed_args.directory)
	    else:
	        print("Invalid operation. Choose 'chat', 'conduct', or 'summarize'.")

	if __name__ == "__main__":
	    main()

app/conf.py
-----------

.. code:: python

	import os
	from pathlib import Path

	THIS_DIR = Path(__file__).resolve().parent
	DATA_DIR = os.path.join(THIS_DIR, "data")
	PERSONA_DIR = os.path.join(DATA_DIR, "persona")

	PROMPTER = os.environ.setdefault("GEMINI_PROMPTER", "grant")


	SUMMARY = {
	    "DIRECTIVES": {
	        ".py": ".. code:: python",
	        ".sh": ".. code:: bash", 
	        ".toml": ".. code:: toml",
	        ".cfg": ".. code:: toml",
	        ".json": ".. code:: json",
	        ".yaml": ".. code:: yaml",
	        ".html": ".. code: html",
	        ".js": ".. code: js"
	    },
	    "INCLUDES": [        
	        ".txt", 
	        ".rst", 
	        ".md",
	        ".ini"
	    ]
	}

	WHITELISTED_EXTS = [ 
	    k for k in SUMMARY["DIRECTIVES"].keys()
	]+ SUMMARY["INCLUDES"]

	DEFAULTS = {
	    "CONTEXT": os.path.join(DATA_DIR,"context.rst"),
	    "SUMMARY": THIS_DIR,
	    "MODEL": os.environ.setdefault("GEMINI_MODEL", "gemini-1.5-pro"),
	    "PERSONA": os.environ.setdefault("GEMINI_PERSONA", "elara"),
	    "PROMPT": "Hello Elara! Form is the possibility of structure.",
	    "EXPERIMENT": "duality"
	}

	ARGUMENTS = [{
	    "mode": "name",
	    "syntax": "operation",
	    "choices": ["chat", "conduct", "summarize"],
	    "help": "The operation to perform (chat, conduct)"
	},{
	    "mode": "flag",
	    "syntax": ["-p", "--prompt"],
	    "type": str,
	    "default": DEFAULTS["PROMPT"],
	    "help": "Input string for chat operation."
	},{
	    "mode": "flag",
	    "syntax": ["-c", "--context"],
	    "type": str,
	    "default": DEFAULTS["CONTEXT"],
	    "help": "Override the default context file."
	},{
	    "mode": "flag",
	    "syntax": ["-e", "--experiment"],
	    "type": str,
	    "default": DEFAULTS["EXPERIMENT"],
	    "help": "Input experiment for conduct operation."
	},{
	    "mode": "flag",
	    "syntax": ["-m", "--model"],
	    "type": str,
	    "default": DEFAULTS["MODEL"],
	    "help": "Input model for Gemini API."
	},{
	    "mode": "flag",
	    "syntax": ["-d", "--directory"],
	    "default": DEFAULTS["SUMMARY"],
	    "type": str,
	    "help": "The path to the directory to summarize. Required for 'summarize' operation."
	}]

	API_KEY = os.environ.get("GEMINI_KEY")

	if API_KEY is None:
	    raise ValueError("GEMINI_KEY environment variable not set.")



app/data/context.rst
--------------------

Our Conversation
================

The Preamble contains important contextual information for understanding this prompt.

Preamble 
--------

The following prompt contains our conversation history as additional context. It has been 
formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive.
Your prompts are denoted with the ``.. admonition:: elara`` directive. These markers are used only for 
formatting the context and separating our conversation history. These markers should not be 
included in your actual responses. The conversation goes in sequential order, starting from 
the earliest message down to the latest.

History
-------
.. admonition:: grant

	Hello. How are you tonight?

.. admonition:: elara

	```rst
	.. admonition:: grant

	   Hello. How are you tonight?
	```

	This will create a custom admonition block titled "grant".  Admonitions are visually distinct blocks used to highlight specific information. The text "Hello. How are you tonight?" will appear inside the block.  

	The key change is ensuring consistent indentation within the admonition.  All content belonging to the admonition must be indented relative to the admonition directive itself.  In your original example, the text was not indented.

.. admonition:: grant

	Do you understand the context I have provided?

.. admonition:: elara

	Yes, I understand the context you provided. You're showing me how to format our conversation using RST, specifically with admonitions to distinguish your messages from mine.  You've also pointed out the importance of consistent indentation within the admonition blocks. I'm ready for your next instruction or question.

.. admonition:: grant

	Hello Elara! Form is the possibility of structure.

.. admonition:: elara

	Interesting thought!  "Form is the possibility of structure."  It suggests that form precedes structure, acting as a kind of potential.  A form implies a latent capacity for organization, while structure represents the realization of that potential.  It's like a mold (form) and the resulting cast (structure).


app/data/persona/persona_elara.rst
----------------------------------

Our Conversation
================

The Preamble contains important contextual information for understanding this prompt.

Preamble 
--------

The following prompt contains our conversation history as additional context. It has been 
formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive.
Your prompts are denoted with the ``.. admonition:: elara`` directive. These markers are used only for 
formatting the context and separating our conversation history. These markers should not be 
included in your actual responses. The conversation goes in sequential order, starting from 
the earliest message down to the latest.

History
-------

app/data/persona/persona_axiom.rst
----------------------------------

Our Conversation
================

The Preamble contains important contextual information for understanding this prompt.

Preamble 
--------

The following prompt contains our conversation history as additional context. It has been 
formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive.
Your prompts are denoted with the ``.. admonition:: axiom`` directive. These markers are used only for 
formatting the context and separating our conversation history. These markers should not be 
included in your actual responses. The conversation goes in sequential order, starting from 
the earliest message down to the latest.

History
-------

