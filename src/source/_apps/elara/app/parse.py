""" # parse.py
Module for formatting prompts and responses. It also handles context.
"""
import os
import subprocess
import textwrap

import conf

_personas = { } 

def personas():
    return [ key for key in _personas.keys() ]

def preamble(
    persona = conf.DEFAULTS["PERSONA"]
):
    return _personas[persona]["PREAMBLE"]

def training_data(
    persona = conf.DEFAULTS["PERSONA"]
):
    return _personas[persona]["TUNING"]

def init():
    os.makedirs(conf.PERSONA_DIR, exist_ok=True)
    os.makedirs(conf.TUNING_DIR, exist_ok=True)
    for root, _, files in os.walk(conf.PERSONA_DIR):
        for file in files:
            if os.path.splitext(file)[1] not in  [".rst", ".md"]:
                continue

            file_path = os.path.join(root, file)

            with open(file_path, "r") as f:
                payload  = f.read()
                
            _personas[os.path.splitext(file)[0]] = {}
            _personas[os.path.splitext(file)[0]]["PREAMBLE"] = payload

    for root, _, files in os.walk(conf.TUNING_DIR):
        for file in files:
            if os.path.splitext(file)[1] !=  ".json":
                continue

            file_path = os.path.join(root, file)

            with open(file_path, "r") as f:
                payload  = f.read()

            _personas[os.path.splitext(file)[0]]["TUNING"] = payload
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
                if ext not in conf.EXTENSIONS:
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)

                f.write(f"{relative_path}\n")
                f.write("-" * len(relative_path) + "\n\n")

                directive = ext in conf.SUMMARIZE["DIRECTIVES"].keys()

                if directive:
                    f.write(f"{conf.SUMMARIZE["DIRECTIVES"][ext]}\n\n")

                with open(file_path, "r") as infile:
                    content = infile.read()

                    # Indent content for RST directives
                    if directive:
                        content = textwrap.indent(content, "\t")

                    f.write(content)

                f.write("\n\n")

    print(f"Summary generated at: {output_file}")