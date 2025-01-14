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

    _personas[persona]["THREADS"]["DATA"] += _response(raw_response, persona)

    with open(_personas[persona]["THREADS"]["FILE"], "w") as f:
        f.write(_personas[persona]["THREADS"]["DATA"] + "\n")

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

    payload = _personas[persona]["PREAMBLE"] + _personas[persona]["THREADS"]["DATA"]

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
