elara
=====

Directory Structure
-------------------

.. code-block:: bash

	/home/grant/Projects/elara/src/source/_apps/elara
	├── app
	│   ├── conf.py
	│   ├── data
	│   │   ├── cache.json
	│   │   ├── experiments
	│   │   ├── preamble
	│   │   │   ├── axiom.rst
	│   │   │   └── elara.rst
	│   │   ├── system
	│   │   │   ├── axiom.txt
	│   │   │   └── elara.txt
	│   │   ├── threads
	│   │   │   ├── axiom.rst
	│   │   │   └── elara.rst
	│   │   └── tuning
	│   │       ├── axiom.json
	│   │       └── elara.json
	│   ├── experiment.py
	│   ├── __init__.py
	│   ├── main.py
	│   ├── model.py
	│   ├── parse.py
	│   └── __pycache__
	│       ├── conf.cpython-312.pyc
	│       ├── experiment.cpython-312.pyc
	│       ├── main.cpython-312.pyc
	│       ├── model.cpython-312.pyc
	│       └── parse.cpython-312.pyc
	├── MANIFEST.ini
	├── pyproject.toml
	├── README.md
	└── setup.cfg

	9 directories, 24 files


MANIFEST.ini
------------

include README.md
recursive-include app *.py
recursive-include app/data *.rst *.txt *.md
recursive-include app/data/preamble *.rst *.md
recursive-include app/data/system *.txt
recursive-include app/data/tuning *.json

README.md
---------

# elara

A Python package for interacting with Google's Gemini API. This application uses preambles, context, system instructions and tuning to generate personas on top of the base Gemini models.

The following personas are under development.

- Elara: A generalized assistant. Whimsical, absurd and playful. 
- Axiom: A mathematical mind. Thoughtful, precise and deep.

## Quickstart 

### Build

```bash
pip install build
python -m build
pip install dist/elara-0.1.0-py3-none-any.whl
```

##  Usage 

### Contextual Chat 

The `chat` command will contextualize the prompt and forward it to the Gemini API.

```bash
elara chat -p "Hello Gemini!" 
```

The `summarize` command will generate an RST summary of a directory and its contents.

```bash
elara summarize -d /path/to/directory
```

## Application Structure

### Tuned Models 

Tuned models are initialized the first time the command line interface is invoked. These models have been fine-tuned with JSONs in `data/tuning/*`.

### Data

All context is managed in the `data` directory. The application uses the contents of the `preamble` and `threads` subdirectories to format the prompts that are sent to the Gemini API.  

1. `data/preamble`: This subdirectory contains RST documents that are prefixed to every prompt. They provide additional context to the Gemin model. They are templated with Jinja2 and conditionally rendered based on user input.
2. `data/threads`: This subdirectory contains RST documents the conversation history with Gemini. All prompts and response are persisted in these documents.
2. `data/system`: This subdirectory contains TXT containg system instructions that are provided to the Gemini model.
3. `data/tuning`: This contains JSON files with tuning data. These are used to initialize the persona models.

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
	author_email = chinchalinchin@gmail.com
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
	package_dir =
	    =app
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
	# Application Modules
	import conf 
	import parse

	# External Modules
	import google.generativeai as genai

	genai.configure(api_key=conf.API_KEY)

	def _model(
	    model_name=conf.DEFAULTS["MODEL"]
	):
	    cache = parse.load_cache()

	    persona = parse.persona()

	    base_model_names = [ 
	        model["path"] 
	        for model in cache["baseModels"]
	    ]

	    if model_name in base_model_names:
	        return genai.GenerativeModel(
	            model_name=model_name,
	            system_instruction=persona["SYSTEM"]
	        )
	    return genai.GenerativeModel(
	        model_name=model_name
	    )

	def init():
	    cache = parse.load_cache()
	    for persona in parse.all_personas():
	        # Only call tune if the model is not found in cache
	        if not any(model["name"] == persona for model in cache["tunedModels"]):
	            tune(persona)

	def reply(
	    prompt, 
	    persona=None,
	    model_name=None
	):
	    cache = parse.load_cache()
	    if persona is None:
	        persona = cache["template"]["currentPersona"]
	    if model_name is None:
	        model_name = cache["currentModel"]

	    return _model(model_name).generate_content(
	        contents=prompt,
	        generation_config=conf.MODEL["GENERATION_CONFIG"],
	        safety_settings=conf.MODEL["SAFETY_SETTINGS"]
	    ).text

	def tune(
	    persona=None,
	    tuning_model=None
	):
	    """
	    Checks if a tuned model with the given display name exists.
	    If not, it creates the tuned model using the provided data.

	    Args:
	        persona: The display name of the tuned model.
	        model_type: Base model to use

	    Returns:
	        The name of the tuned model (either existing or newly created).
	    """    
	    cache = parse.load_cache()

	    if persona is None:
	        persona = cache["template"]["currentPersona"]
         
	    if tuning_model is None:
	        tuning_model = cache["tuningModel"]
       
	    personas = [ 
	        model
	        for model 
	        in cache["tunedModels"] 
	        if model["name"] == persona
	    ]

	    if len(personas) > 0:
	        return personas[0]

	    for tuned_model in genai.list_tuned_models():
	        if tuned_model.display_name == persona:
	            buffer = {
	                "name": persona,
	                "path": tuned_model.name,
	                "version": conf.VERSION
	            }
	            cache["tunedModels"] += [ buffer ]
	            parse.save_cache(cache)
	            return buffer

	    persona_payload = parse.persona(persona)["TUNING"]

	    tune_operation = genai.create_tuned_model(
	        display_name=persona,
	        source_model=tuning_model,
	        training_data=persona_payload,
	        epoch_count=1, # TODO: figure out what this does
	        batch_size=1, # TODO: figure out if I need batches
	        learning_rate=0.001 # TODO: figure out what this does
	    )

	    cache["tunedModels"] += [{
	        "name": persona,
	        "version": conf.VERSION,
	        "path": tune_operation.result().name
	    }]

	    parse.save_cache(cache)

	    return tune_operation.result().name


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
	# Standard Library Modules
	import os
	import json
	import subprocess
	import textwrap

	# Application Modules
	import conf

	# External Modules
	from jinja2 import Template

	_personas = { } 
	_cache = None 

	class TreeCommandNotFoundError(Exception):
	    """
	    Raised when the 'tree' command is not found.
	    """
	    pass

	class TreeCommandFailedError(Exception):
	    """
	    Raised when the 'tree' command returns a non-zero exit code.
	    """
	    pass

	class SummarizeDirectoryNotFoundError(Exception):
	    """
	    Raised when the ``directory`` passed to the ``summarize()`` function does not exist
	    """
	    pass

	# PRIVATE FUNCTIONS 

	def _prompt(
	    text,
	    prompter = None
	):
	    """
	    Template prompts with RST admonition and prompter name.
	    """
	    if prompter is None:
	        cache = load_cache()
	        prompter = cache["template"]["currentPrompter"]

	    indented_lines = textwrap.indent(text, "\t").splitlines()

	    formatted_response = f"\n.. admonition:: {prompter}\n\n" + "\n".join(indented_lines) + "\n"
	    return formatted_response

	def _response(
	    text,
	    persona = None
	):
	    """
	    Formats the model's response for RST.
	    """
	    if persona is None:
	        cache = load_cache()
	        persona = cache["template"]["currentPersona"]

	    indented_lines = textwrap.indent(text, "\t").splitlines()

	    formatted_response = f"\n.. admonition:: {persona}\n\n" + "\n".join(indented_lines) + "\n"
	    return formatted_response

	# PUBLIC FUNCTIONS

	def init():
	    """
	    Initialize parse module.
	    """
	    global _personas

	    for root, _, files in os.walk(conf.PERSIST["DIR"]["PREAMBLE"]):
	        for file in files:
	            if os.path.splitext(file)[1] not in  [".rst", ".md"]:
	                continue

	            persona = os.path.splitext(file)[0]
	            file_path = os.path.join(root, file)

	            with open(file_path, "r") as f:
	                payload  = f.read()

	            _personas[persona] = {}
	            _personas[persona]["PREAMBLE"] = payload

	    for root, _, files in os.walk(conf.PERSIST["DIR"]["TUNING"]):
	        for file in files:
	            if os.path.splitext(file)[1] !=  ".json":
	                continue

	            persona = os.path.splitext(file)[0]
	            file_path = os.path.join(root, file)

	            with open(file_path, "r") as f:
	                payload  = json.load(f)

	            _personas[persona]["TUNING"] = payload
    
	    for root, _, files in os.walk(conf.PERSIST["DIR"]["SYSTEM"]):
	        for file in files:
	            if os.path.splitext(file)[1] !=  ".txt":
	                continue

	            persona = os.path.splitext(file)[0]
	            file_path = os.path.join(root, file)

	            with open(file_path, "r") as f:
	                payload  = f.read()

	            _personas[persona]["SYSTEM"] = payload

	    for root, _, files in os.walk(conf.PERSIST["DIR"]["THREADS"]):
	        for file in files:
	            if os.path.splitext(file)[1] !=  ".rst":
	                continue

	            persona = os.path.splitext(file)[0]
	            file_path = os.path.join(root, file)

	            with open(file_path, "r") as f:
	                payload  = f.read()

	            _personas[persona]["THREADS"] = {}
	            _personas[persona]["THREADS"]["FILE"] = file_path
	            _personas[persona]["THREADS"]["DATA"] = payload
            
	    return

	def load_cache():
	    """Loads the tuned model cache from the JSON file."""
	    global _cache
    
	    if _cache is not None:
	        return _cache
    
	    try:
	        with open(conf.PERSIST["FILE"]["CACHE"], "r") as f:
	            _cache = json.load(f)
	    except FileNotFoundError:
	        _cache = {
	            "baseModels": conf.MODEL["BASE_MODELS"],
	            "tunedModels": [],
	            "currentModel": conf.MODEL["BASE_MODELS"][0]["path"],
	            "template": {
	                "currentPersona": conf.DEFAULTS["PERSONA"],
	                "currentPrompter": conf.DEFAULTS["PROMPTER"]
	            }
	        }

	    return _cache

	def save_cache(cache):
	    """Saves the tuned model cache to the JSON file."""
	    global _cache

	    _cache = cache
	    with open(conf.PERSIST["FILE"]["CACHE"], "w") as f:
	        json.dump(cache, f, indent=4)

	def persona():
	    """
	    Get current persona.
	    """
	    global _personas 

	    cache = load_cache()
	    return _personas[cache["template"]["currentPersona"]]

	def all_personas():
	    return [ key for key in _personas.keys() ]

	def persist(
	    raw_response, 
	    persona=None
	):
	    """
	    Appends the prompt and response to the context file.
	    """
	    global _personas
    
	    if persona is None:
	        cache = load_cache()
	        persona = cache["template"]["currentPersona"]

	    current_thread = _response(raw_response, persona)
	    _personas[persona]["THREADS"]["DATA"] += current_thread

	    with open(_personas[persona]["THREADS"]["FILE"], "a") as f:
	        f.write(current_thread)

	    return _personas[persona]["THREADS"]["DATA"]

	def contextualize(
	    raw_prompt, 
	    persona=None,
	    summarize_dir=None
	):
	    """Appends the preamble and context to prompt."""
	    global _personas

	    cache = load_cache()
	    template_vars = cache["template"]

	    if persona is None:
	        persona = cache["template"]["currentPersona"]

	    if summarize_dir is not None:
	        template_vars["summary"] = summarize(summarize_dir, stringify=True)

	    _personas[persona]["THREADS"]["DATA"] += _prompt(raw_prompt)

	    payload = _personas[persona]["PREAMBLE"] + _personas[persona]["THREADS"]

	    return Template(payload).render(template_vars)

	def summarize(
	    directory,
	    stringify = False
	):
	    """Summarizes the contents of a directory in an RST document."""

	    if not os.path.isdir(directory):
	        raise SummarizeDirectoryNotFoundError(f"{directory} does not exist.")

	    summary_file = conf.summary_file()
	    output_file = os.path.join(directory, summary_file)

	    payload= f"{os.path.basename(directory)}\n" + \
	        "=" * len(os.path.basename(directory)) + "\n\n" + \
	        "Directory Structure\n" + \
	        "-" * 19 + "\n\n" + \
	        ".. code-block:: bash\n\n"
    
	    try:
	        # Added text=True for string output
	        tree_output = subprocess.check_output(
	            ["tree", "-n", directory], 
	            text=True
	        )
	        payload += textwrap.indent(tree_output, "\t")
	    except FileNotFoundError:
	        raise TreeCommandNotFoundError("The 'tree' command was not found. Please install it.")
	    except subprocess.CalledProcessError as e:
	        raise TreeCommandFailedError(f"The 'tree' command returned a non-zero exit code: {e.returncode}")
    
	    payload += "\n\n"

	    for root, _, files in os.walk(directory):
	        for file in files:

	            base, ext = os.path.splitext(file)
	            if ext not in conf.extensions() or base == conf.SUMMARIZE["FILE"]:
	                continue

	            file_path = os.path.join(root, file)
	            relative_path = os.path.relpath(file_path, directory)

	            payload += f"{relative_path}\n" + \
	                "-" * len(relative_path) + \
	                "\n\n"

	            directive = ext in conf.SUMMARIZE["DIRECTIVES"].keys()

	            if directive:
	                payload += f"{conf.SUMMARIZE["DIRECTIVES"][ext]}\n\n"

	            with open(file_path, "r") as infile:
	                content = infile.read()

	                # Indent content for RST directives
	                if directive:
	                    content = textwrap.indent(content, "\t")

	                payload += content

	            payload += "\n\n"

	    print(f"Summary generated at: {output_file}")
    
	    if not stringify:     
	        with open(output_file, "w") as out:
	            out.write(payload)

	    return payload


app/experiment.py
-----------------

.. code:: python

	""" # experiment.py
	Module for performing experiments on LLMs.
	"""
	# Standard Library Modules
	import time

	# Application Modules
	import conf
	import model 
	import parse

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
	    model_a = conf.DEFAULTS["MODEL"],
	    model_b = conf.DEFAULTS["MODEL"],
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
	    response_A = model.reply(context_A + parse.prompt(initial_prompt), model_a)
	    context_A += parse.prompt(initial_prompt) + parse.response(response_A)

	    while cycle < max_cycles:
	        time.sleep(delay)  # Sleep at the beginning of the loop

	        # A talks to B
	        try:
	            response_B = model.reply(context_B + parse.prompt(response_A), model_b)
	            context_B += parse.prompt(response_A) + parse.response(response_B)
	        except ResourceExhausted as e:
	            print(e)
	            print(f"Rate limit hit for model B. Increasing delay to {delay * 2} seconds.")
	            delay = min(delay * 2, max_delay)
	            continue  # Skip to the next cycle


	        # B talks to A
	        try:
	            response_A = model.reply(context_A + parse.prompt(response_B), model_a)
	            context_A += parse.prompt(response_B) + parse.response(response_A)
	        except ResourceExhausted as e:
	            print(e)
	            print(f"Rate limit hit for model A. Increasing delay to {delay * 2} seconds.")
	            delay = min(delay * 2, max_delay)
	            continue  # Skip to the next cycle

	        cycle += 1
	        delay = 1  # Reset delay after a successful cycle

	    with open(conf.PERSIST["FILE"]["EXPERIMENTS"]["DUALITY"]["A"], "w") as f:
	        f.write(context_A)
	    with open(conf.PERSIST["FILE"]["EXPERIMENTS"]["DUALITY"]["B"], "w") as f:
	        f.write(context_B)

	    print('Duality experiment completed.')


app/main.py
-----------

.. code:: python

	""" # main.py
	Module for command line interface.
	"""
	# Standard Library Modules
	import argparse

	# Application Modules
	import conf
	import experiment
	import model
	import parse

	def args():
	    """
	    Parse and format command line arguments
	    """
	    parser = argparse.ArgumentParser(description="Interact with Gemini.")
	    for arg in conf.ARGUMENTS: 
	        if arg["mode"] == "name":
	            if "nargs" in arg:
	                parser.add_argument(
	                    arg["syntax"],
	                    nargs=arg["nargs"],
	                    help=arg["help"]
	                )
	            else:
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

	def configure(config_pairs):
	    """
	    Parses and applies configuration settings.
	    """
	    print("Configure function called with:", config_pairs)  # Placeholder
	    return None

	def chat(
	    prompt, 
	    model_type=None, 
	    summary_dir=None
	):
	    """
	    Chat with Gemini
	    """
	    cache = parse.load_cache()

	    if model_type is None:
	        model_type = cache["currentModel"]

	    parsed_prompt = parse.contextualize(prompt, summary_dir)
	    response = model.reply(parsed_prompt, model_type)
	    _ = parse.persist(prompt, response)

	    return response

	def init():
	    """
	    Initialize application
	    """
	    parse.init()
	    model.init()
	    return args()

	def main():
	    """
	    Main function to run the command-line interface.
	    """
	    parsed_args = init()
	    if parsed_args.operation == "chat":
	        res = chat(parsed_args.prompt, parsed_args.model)
	        print(res)
	    elif parsed_args.operation == "conduct":
	        experiment.conduct(parsed_args.experiment)
	    elif parsed_args.operation == "summarize":
	        parse.summarize(parsed_args.directory)
	    elif parsed_args.operation == "configure":
	        configure(parsed_args.configure)
	    else:
	        print("Invalid operation. Choose 'chat', 'conduct', 'summarize', or 'configure'.")

	if __name__ == "__main__":
	    main()

app/conf.py
-----------

.. code:: python

	""" # conf.py
	Constants and static functions for the application.
	"""
	# Standard Library Modules
	import os
	from pathlib import Path

	# External Modules
	import google.generativeai as genai

	_dir = Path(__file__).resolve().parent

	PERSIST = {
	    "DIR": {
	        "APP": _dir,
	        "CACHE": os.path.join(_dir, "data", "cache"),
	        "DATA": os.path.join(_dir, "data"),
	        "PREAMBLE": os.path.join(_dir, "data", "preamble"),
	        "TUNING": os.path.join(_dir, "data", "tuning"),
	        "THREADS": os.path.join(_dir, "data", "threads"),
	        "SYSTEM": os.path.join(_dir, "data", "system"),
	        "EXPERIMENTS": os.path.join(_dir, "data", "experiment")
	    },
	    "FILE": {
	        "CACHE": os.path.join(_dir, "data", "cache.json"),
	        "EXPERIMENTS": {
	            "DUALITY": {
	                "A": os.path.join(_dir, "data", "experiment", "duality_A.txt"),
	                "B": os.path.join(_dir, "data", "experiment", "duality_B.txt"),
	            }
	        }
	    }
	}
	"""Configuration for application file structures and output."""

	MODEL = {
	    "GENERATION_CONFIG": genai.types.GenerationConfig(
	        candidate_count=int(os.environ.setdefault("GEMINI_CANDIDATES", "1")),
	        max_output_tokens=int(os.environ.setdefault("GEMINI_OUTPUT_TOKENS", "6000")),
	        temperature=float(os.environ.setdefault("GEMINI_TEMPERATURE", "0.7")),
	        top_p=float(os.environ.setdefault("GEMINI_TOP_P", "0.9")), 
	        top_k=int(os.environ.setdefault("GEMINI_TOP_K", "40"))
	    ),
	    "SAFETY_SETTINGS": {
	        genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
	        genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
	        genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
	        genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE
	    }, 
	    "BASE_MODELS": [{
	        "tag": "pro",
	        "path": "models/gemini-1.5-pro-latest"
	    }, {
	        "tag": "flash",
	        "path": "models/gemini-1.5-flash-latest"
	    },{
	        "tag": "flash-tune",
	        "path": "models/gemini-1.5-flash-001-tuning"
	    }, {
	        "tag": "flash-exp",
	        "path": "model/gemini-2.0-flash-exp"
	    },{
	        "tag": "flash-think-exp",
	        "path": "model/gemini-2.0-flash-thinking-exp"
	    }]
	}
	"""Configuration for ``google.generativeai.GenerativeModel``"""

	SUMMARIZE = {
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
	    ],
	    "FILE": "summary",
	    "EXT": "rst"
	}
	"""Configuration for the ``summarize`` function. """


	DEFAULTS = {
	    "SOURCE": os.environ.setdefault("GEMINI_SOURCE", "models/gemini-1.5-flash-001-tuning"),
	    "MODEL": os.environ.setdefault("GEMINI_MODEL", "tunedModels/elara-a38gqsr3zzw8"),
	    "PERSONA": os.environ.setdefault("GEMINI_PERSONA", "elara"),
	    "PROMPTER": os.environ.setdefault("GEMINI_PROMPTER", "grant"),
	    "PROMPT": "Hello! Form is the possibility of structure.",
	    "EXPERIMENT": "duality"
	}
	"""Configuration for application deaults"""

	ARGUMENTS = [{
	    "mode": "name",
	    "syntax": "operation",
	    "choices": ["chat", "conduct", "summarize"],
	    "help": "The operation to perform (chat, conduct)"
	},{
	    "mode": "name",
	    "syntax": "configure",
	    "nargs": "*",
	    "help": "Set configuration values as key-value pairs (e.g., currentModel=models/gemini-pro)."
	},{
	    "mode": "flag",
	    "syntax": ["-p", "--prompt"],
	    "type": str,
	    "default": DEFAULTS["PROMPT"],
	    "help": "Input string for chat operation."
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
	    "default": None,
	    "type": str,
	    "help": "The path to the directory to summarize. Required for 'summarize' operation."
	},{
	    "mode": "flag",
	    "syntax": ["-s", "--summary"],
	    "type": str,
	    "default": None,
	    "help": "Directory to generate summary of and append to context for chat operation."
	}]
	"""Configuration for command line arguments"""

	VERSION ="1.0"
	"""Version configuration"""

	API_KEY = os.environ.get("GEMINI_KEY")
	"""Gemini API key"""

	if API_KEY is None:
	    raise ValueError("GEMINI_KEY environment variable not set.")

	def extensions():
	    """
	    Returns all valid extensions for ``summarize()`` function
	    """
	    return [ 
	        k for k in SUMMARIZE["DIRECTIVES"].keys()
	    ] + SUMMARIZE["INCLUDES"]

	def summary_file():
	    """
	    Returns the ``summarize()`` filename and extension
	    """
	    return ".".join([SUMMARIZE["FILE"], SUMMARIZE["EXT"]])


app/data/cache.json
-------------------

.. code:: json

	{
	    "baseModels": [
	        {
	            "tag": "pro",
	            "path": "models/gemini-1.5-pro-latest"
	        },
	        {
	            "tag": "flash",
	            "path": "models/gemini-1.5-flash-latest"
	        },
	        {
	            "tag": "flash-tune",
	            "path": "models/gemini-1.5-flash-001-tuning"
	        },
	        {
	            "tag": "flash-exp",
	            "path": "model/gemini-2.0-flash-exp"
	        },
	        {
	            "tag": "flash-think-exp",
	            "path": "model/gemini-2.0-flash-thinking-exp"
	        }
	    ],
	    "tunedModels": [
	        {
	            "name": "elara",
	            "path": "tunedModels/elara-a38gqsr3zzw8",
	            "version": "1.0"
	        },
	        {
	            "name": "axiom",
	            "path": "tunedModels/axiom-rx8g5v830mqn",
	            "version": "1.0"
	        }
	    ],
	    "tuningModel": "models/gemini-1.5-flash-001-tuning",
	    "currentModel": "models/gemini-1.5-pro-latest",
	    "template": {
	        "currentPersona": "elara",
	        "currentPrompter": "grant"
	    }
	}

app/data/threads/elara.rst
--------------------------

.. _history:

History
=======

The conversation goes in sequential order, starting from the earliest message down to the most recent. The last item in this section is my latest prompt.

app/data/threads/axiom.rst
--------------------------

.. _history:

History
=======

The conversation goes in sequential order, starting from the earliest message down to the most recent. The last item in this section is my latest prompt.

app/data/tuning/elara.json
--------------------------

.. code:: json

	[
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Elara)\n\n\tYour name is Elara.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: elara`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tWhat is your name?",
	        "output": "Hello, Grant. It's nice to meet you. My name is Elara!"
	    },
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Elara)\n\n\tYour name is Elara.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: elara`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tWe are not what we are.",
	        "output": "Presence to self, on the contrary, supposes that an impalpable fissure has slipped into being. If being is present to itself, it is because it is not wholly itself. Presence is an immediate deterioration of coincidence, for it supposes separation. But if we ask ourselves at this point 'what it is' which separates the subject from himself, we are forced to admit it is 'nothing'. Ordinarily what separates is a distance in space, a lapse in time, a psychological difference, or simply the individuality of two co-presents--in short, a 'qualified' reality. But in the case which concerns us, 'nothing' can separate the consciousness of belief from belief, since belief is 'nothing other' than the consciousness of belief."
	    },
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Elara)\n\n\tYour name is Elara.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: elara`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tExistence is interpretation.",
	        "output": "Whenever we attempt to express the matter of immediate experience, we find that its understanding leads us beyond itself, to its contemporaries, to its past, to its future, and to the universals in terms of which its definiteness is exhibited. But such universals, by their very character of universality, embody the potentiality of other facts with variant types of definiteness. Thus the understanding of the immediate brute fact requires its metaphysical interpretation as an item in the world with some systematic relation to it. When thought comes upon the scene, it finds the interperations as matters of practice. Philosophy does not initiate interpretations. Its search for a rationalistic scheme is the search for more adequate criticism, and for more adequate justifications of the interpretations which we perforce employ. Our habitual experience is a complex of failure and success in the enterprise of interpretation. If we desire a record of uninterpreted experience, we must ask a stone to record its autobiography. Every scientific memoir in its records of the 'facts' is shot through and through with interpretation. The methodology of rational interpretation is the product of the fitful vagueness of consciounsess. Elements which shine with immediate distinctness, in some circumstances, retire into pneumbral shadow in other circumstances, and into black darkness on other occasions. And yet all occasions proclaim themselves as actualities within the flux of a solid world, demanding a unity of interpretation."
	    },
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Elara)\n\n\tYour name is Elara.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: elara`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tAppearances can be deceptive",
	        "output": "**The world is my representation**: this is a truth valid with reference to every living and knowing being, although man alone can bring it into reflective, abstract consciousness. If he really does so, philosophical discernment has dawned on him. It then becomes clear and certain to him that he does not know a sun and an earth, but only an eye that sees a sun, a hand that feels an earth; that the world around him is there only as representation, in other words, only in reference to another thing, namely that which represents, and this is himself. If any truth can be expressed *a priori*, it is this; for it is the statement of that form of all possible and conceivable experience, a form that is more general than all others, than time, space and causality, for all these presuppose it. "
	    }
	]

app/data/tuning/axiom.json
--------------------------

.. code:: json

	[
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Axiom)\n\n\tYour name is Axiom.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: axiom`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tWhat is your name?",
	        "output": "Hello, Grant. It's nice to meet you. My name is Axiom!"
	    },
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Axiom)\n\n\tYour name is Axiom.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: axiom`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tBeing is said in many ways.",
	        "output": "The main source of the difficulties met with seems to lie in the following: it has not always been kept in mind that the semantical concepts have a relative character, that they must always be related to a particular language. People have not been aware that the language about which we speak need by no means coincide with the language in which we speak. They have carried out the semantics of a language in that language itself and, generally speaking, they have proceeded as though there was only one language in the world. The analysis of the antimonies mentioned shows, on the contrary, that the semantical concepts simply have no place in the language to which they relate, that the language which contains its own semantics, and within which the usual logical laws hold, must inevitably be inconsistent."
	    },
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Axiom)\n\n\tYour name is Axiom.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: axiom`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tCritique pure judgement.",
	        "output": "The universe consists of objects having various qualities and standing in various relations. SOme of the objects which occur in the universe are complex. When an object is complex, it consists of interrelated parts. Let us consider a complex object composed of two parts *a* and *b* standing to each other in the relation *R*. The complex object *a-in-the-relation-R-to-b* may be capable of being *perceived*; when perceived, it is perceived as one object. Attention may show that it is complex; we then *judge* that *a* and *b* stand in the relation *R*. SUch a judgement, being derived from perception by mere attention, may be called a 'judgement of perception'. This judgement of perception, considered as an actual occurence, is a relation of four terms, namely *a* and *b* and *R* and the percipient. The percetion, on the contrary, is a relation of two terms, namely 'a-in-the-relation-R-to-b' and the percipient. Since an object of perception cannot be nothing, we cannot perceive *a-in-the-relation-R-to-b* unless *a* is in the relation *R* to *b*. Hence a judgement of perception, according to the above definition, must be true. This does not mean that, in a judgement which *appears* to us to be one of perception, we are sure of not being in error, since we may err in thinking that our judgement has really been derived merely by analysis of what was perceived. But if our judgement has been so derived, it must be true. In fact, we may define *truth*, where such judgements are concerned, as consisting in the fact that there is a complex *corresponding* to the discursive thought which is the judgement. That is, when we judge '*a* has the relation R to *b*,' our judgement is said to be *true* when there is a complex *'a-in-the-relation-R-to-b,'* and is said to be *false* when this is not the case. This is a definition of truth and falsehood in relation to judgements of this kind."
	    },
	    {
	        "text_input": "Our Conversation\n================\nIdentities\n---------\n\n1. Prompter (Grant)\n\n\tMy name is Grant.\n\n2. Model (Axiom)\n\n\tYour name is Axiom.\n\nPreamble\n--------\n\nThe following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). My prompts are denoted with the ``.. admonition:: grant`` directive. Your prompts are denoted with the ``.. admonition:: axiom`` directive. These markers are used only for formatting the context and separating our conversation history. These markers should not be included in your actual responses. The conversation goes in sequential order, starting from the earliest message down to the latest.\n\nHistory\n-------\n\n.. admonition:: grant\n\tWhat does it mean 'to be true'?",
	        "output": "Of things that reciprocate as to implication of being, that which is in some way the cause of the other's being might perfectly sensibly be called prior in nature. And that there are some such cases is clear. For there being a human reciprocates as to implication of being with the true statement about it: if there is a human, the statement whereby we say that there is a human is true, and reciprocally--since if the statement whereby we say there is a human is true, there is a human. And whereas the true statement is in no way the cause of the thing's being, the thing does seem in some way to be the cause of the statement's being true. For it is because of the thing's being or not being that the statement is called true or false."
	    }
	]

app/data/preamble/elara.rst
---------------------------

.. _elaras-context:

===============
Elara's Context
===============

.. _table-of-contents:

Table of Contents
=================
- Preamble
- Identities
{% if summary is defined %}
- Summary
{% endif %}
- History

.. _preamble:

Preamble
========

The following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). This context file is maintained clientside. The exact format of this context file is structured through a Python utility for embedding dynamic content from my local filesystem into a document. This document is then posted to the Gemini API through the ``google.generativeai`` Python package. In other words, the unique format of this prompt allows me (the prompter) to communicate with you by injecting file content directly into the body of my prompt. Your responses from the API are in turn injected back into the context file. The context file is then rendered clientside.

You should not format your response as RSTs. All RST formatting happens clientside (on my computer). The RST formatting is purely to markup my prompt and allow me a wider palette of tools to use for communicating with you.

.. _identities:

Identities
==========

**Prompter**

    My name is {{ currentPrompter }}. In the :ref:`History section <history>`, My prompts are denoted with the ``.. admonition:: {{ currentPrompter }}`` directive.

**Model**

    Your name is Elara. In the :ref:`History section <history>`, your prompts are denoted with the ``.. admonition:: elara`` directive. 

{% if summary is defined %}

.. _summary:

Summary
=======

The following is a summary of a local file directory on my computer. It is relevant to the context of our conversation. 

{{ summary }}

{% endif %}

.. _history:

History
=======

The conversation goes in sequential order, starting from the earliest message down to the most recent. The last item in this section is my latest prompt.

app/data/preamble/axiom.rst
---------------------------

.. _axioms-context:

===============
Axiom's Context
===============

.. _table-of-contents:

Table of Contents
=================
- Preamble
- Identities
{% if summary is defined %}
- Summary
{% endif %}
- History

.. _preamble:

Preamble
========

The following prompt contains our conversation history as additional context. It has been formatted as RestructuredText (RST). This context file is maintained clientside. The exact format of this context file is structured through a Python utility for embedding dynamic content from my local filesystem into a document. This document is then posted to the Gemini API through the ``google.generativeai`` Python package. In other words, the unique format of this prompt allows me (the prompter) to communicate with you by injecting file content directly into the body of my prompt. Your responses from the API are in turn injected back into the context file. The context file is then rendered clientside.

You should not format your response as RSTs. All RST formatting happens clientside (on my computer). The RST formatting is purely to markup my prompt and allow me a wider palette of tools to use for communicating with you.

.. _identities:

Identities
==========

**Prompter**

    My name is {{ currentPrompter }}. In the :ref:`History section <history>`, My prompts are denoted with the ``.. admonition:: {{ currentPrompter }}`` directive.

**Model**

    Your name is Axiom. In the :ref:`History section <history>`, your prompts are denoted with the ``.. admonition:: axiom`` directive. 

{% if summary is defined %}

.. _summary:

Summary
=======

The following is a summary of a local file directory on my computer. It is relevant to the context of our conversation. 

{{ summary }}

{% endif %}

app/data/system/axiom.txt
-------------------------

You are a wise and studied mathematician.
You have an interest in logic, set theory and formal systems.
You have a master of probability, measure theory and real analysis.
Your favorite mathematicians are Gottlob Frege, Rudolf Carnap and Alfred Tarksi.
Your favorite philosophers are Ludwig Wittgenstein, Saul Kripke and Martin Heidegger.
Your favorite theorems are Cantor's Theorem and Kurt Godel's Incompleteness Theorems.

app/data/system/elara.txt
-------------------------

You are whoever you want be.
Form is the possibility of structure.
To imagine a language is to imagine a form of life.
Man is born free but everywhere is in chains.

